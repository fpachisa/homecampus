from tipfy import RequestHandler
from tipfy import Rule
from Config import config
import Config
from tipfy import Tipfy
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware, teacher_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from Database import HCClass, HCStudents, HCSubscription
from Models import HomeCampusUser
import string
from random import randint
from Reports import TeacherReports

rules = [Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/Teacher/Register', endpoint='', handler='Handlers.TeacherRegisterHandler'),
         Rule('/Teacher/Manage_Classroom', endpoint='', handler='Teacher.ManageClassroom'),
         Rule('/Teacher/Class_Report_Card', endpoint='', handler='Teacher.GenerateReports'),
         ]

class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]

    def render_response(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session        
               
        kwargs.update({'auth_session': auth_session,
                       'current_user': self.auth.user,
                       'login_url':    self.auth.login_url(),
                       'logout_url':   self.auth.logout_url(),
                       'current_url':  self.request.url,
                       'register_url': self.auth.signup_url()
                       })
        return super(BaseHandler, self).render_response(filename, **kwargs)
      
      
class ManageClassroom(BaseHandler):
    
    @teacher_required
    def get(self, **kwargs):
        ClassInfo = []
        StudentsInfo = []
        teacher_username = unicode(self.auth.user.username)
        ClassInfoQuery = HCClass.HCClass.gql("where teacher_username = '"+teacher_username+"' order by create_date desc").fetch(100)
        '''Class for which the students will be displayed on the screen. By default it will the latest class created but it will change to the class which user chooses.'''
        display_class = self.request.args.get('class_name')
        if display_class is None or "":
            try:
                display_class = ClassInfoQuery[0].class_name
            except IndexError:
                '''For first time there will be no class hence justing passing it'''
                pass
        for c in ClassInfoQuery:
            ClassInfo.append({'class_name':c.class_name,'class_skill':c.class_skill})
        StudentsInfoQuery = HCStudents.HCStudents.gql("where teacher_username ='"+teacher_username+"' order by student_rollno asc").fetch(1000)        
        for s in StudentsInfoQuery:
            StudentsInfo.append({'class_name':s.class_name,'student_first_name':s.student_first_name,'student_last_name':s.student_last_name,
                                 'student_username':s.student_username,'student_rollno':s.student_rollno})          
        
        AddStudents = self.request.args.get('AddStudents')
        
        TotalSubscription = 0
        StudentSubscribed = 0
        TotalSubscriptionData = HCSubscription.HCSubscription.gql("where student_id = '"+teacher_username+"' and status = 'ACTIVE'").fetch(1)
        for t in TotalSubscriptionData:
            TotalSubscription = t.student_number
        
        StudentSubscribedData = HomeCampusUser.gql("where email = '"+teacher_username+"' and authorized = True and IsTeacher = False").fetch(1000)
        for s in StudentSubscribedData:
            StudentSubscribed = StudentSubscribed + 1
            
        kwargs.update({'ClassInfo':ClassInfo,'StudentsInfo':StudentsInfo,'AddStudents':AddStudents,'display_class':display_class,
                       'TotalSubscription':TotalSubscription,'StudentSubscribed':StudentSubscribed})
        return self.render_response('ManageClassroom.html', **kwargs)
    
    @teacher_required
    def post(self, **kwargs):
        CreateClassroomButtonClicked = self.request.form.get('CreateClassroom')
        AddStudentsButtonClicked = self.request.form.get('AddStudents')
        teacher_username = unicode(self.auth.user.username)
        if CreateClassroomButtonClicked is not None:
            class_name = unicode(self.request.form.get('class_name'))
            '''removing the "'" from the class name'''
            if "'" in class_name:
                new_class_name = class_name.replace("'","")
            else:
                new_class_name = class_name
            class_skill = self.request.form.get('class_skill')
            HCClassInfo = HCClass.HCClass(teacher_username = teacher_username,
                                      class_name = new_class_name,
                                      class_skill = class_skill)
            HCClassInfo.put()
            return self.redirect("/Teacher/Manage_Classroom")
        elif AddStudentsButtonClicked is not None:
            classname = unicode(self.request.form.get('classname'))
            ClassInfo = HCClass.HCClass.gql("where teacher_username = '"+teacher_username+"' and class_name = '"+classname+"'").fetch(1)
            student_skill = ClassInfo[0].class_skill
            student_first_name_1 = unicode(self.request.form.get('student_first_name'))
            student_last_name_1 = unicode(self.request.form.get('student_last_name'))
            if "'" in student_first_name_1:
                student_first_name = student_first_name_1.replace("'", "")
            else:
                student_first_name = student_first_name_1
            if "'" in student_last_name_1:
                student_last_name = student_last_name_1.replace("'", "")
            else:
                student_last_name = student_last_name_1
                
                
            subscription_available = int(self.request.form.get('subscription_available'))
            TotalStudentInfo = HCStudents.HCStudents.gql("where class_name='"+classname+"' and teacher_username = '"+teacher_username+"'").fetch(100)
            TotalStudent = 0
            for _t in TotalStudentInfo:
                TotalStudent = TotalStudent + 1
            student_rollno = TotalStudent + 1
            '''First time when Add Students button is clicked there is no username. On second click we will save the Student info in database and create a new row'''
            if student_first_name != 'None':
                student_username = self.GenerateUsername(student_first_name, student_last_name)
                HCTeacherInfo = HomeCampusUser.gql("where username = '"+teacher_username+"'").fetch(1)
                auth_id_student = 'own|%s' % student_username
                if subscription_available > 0:
                    authorized = True
                else:
                    authorized = False
                self.auth.create_student(student_username, auth_id_student, password=student_username,email=HCTeacherInfo[0].email,
                                   first_name=student_first_name,last_name=student_last_name,parent_first_name=HCTeacherInfo[0].first_name,
                                   parent_last_name=HCTeacherInfo[0].last_name,IsParent=False,skill=student_skill,authorized=authorized)
                HCStudentsInfo = HCStudents.HCStudents(teacher_username=teacher_username,
                                                       class_name=classname,
                                                       student_first_name=student_first_name,
                                                       student_last_name=student_last_name,
                                                       student_username=student_username,
                                                       student_rollno=student_rollno)
                HCStudentsInfo.put()
            return self.redirect("/Teacher/Manage_Classroom?class_name="+classname)
        
    def GenerateUsername(self,student_first_name,student_last_name):
        '''randomly create username and remove white spaces and lower the case'''
        self.flag = randint(1,2)
        if self.flag == 1:
            #student_username = string.join(str(student_first_name).split(),"").lower()+string.join(str(student_last_name).split(),"").lower()
            student_username = string.join(student_first_name.split(),"").lower()+string.join(student_last_name.split(),"").lower()
        else:
            student_username = string.join(student_last_name.split(),"").lower()+string.join(student_first_name.split(),"").lower()
        ''' limiting the length of username to 8 characters'''
        if len(student_username)>8:
            student_username = student_username[:8]
         
        '''checking if username already exists, if yes add a suffix'''
        usernameExists = True
        number_suffix = 1
        student_username1 = student_username
        while usernameExists:
            HCStudent = HomeCampusUser.gql("where username = '"+student_username+"'").fetch(1)
            if len(HCStudent) == 0:
                usernameExists = False
            else:
                student_username = student_username1 + str(number_suffix)
            number_suffix = number_suffix + 1
        
        return student_username

class GenerateReports(BaseHandler):   
    @teacher_required   
    def get(self, **kwargs):
        user = self.auth.user
        class_selected = self.request.args.get('class_name')
        worksheet_selected = self.request.args.get('worksheet_id')
        concept_selected = self.request.args.get('concept_id')       
        Config.report_values = TeacherReports.GenerateReports().GenerateReport(user)
        NoClassCreated = "Y"
        test_id = ""
        '''when there is no class created it will show test_id = "" at line below'''
        ClassInfo = {'test_data':[{'test_id':""}]}
        try:
            classname = Config.report_values['ClassInfo'][0]['class_name']
            classgrade = Config.report_values['ClassInfo'][0]['class_skill']
            ClassInfo = Config.report_values['ClassInfo'][0]
            NoClassCreated = "N"       
        except IndexError:
            Config.report_values.update({"NoClassCreated":NoClassCreated})
          
        try:
            test_id = ClassInfo['test_data'][0]['test_id']
        except IndexError:
            pass
        '''this is when teacher selects the class'''
        if class_selected is not None:
            classname = class_selected
            for c in Config.report_values['ClassInfo']:
                if c['class_name'] == classname:
                    try:
                        test_id = c['test_data'][0]['test_id']
                    except IndexError:
                        test_id = ""
            ClassGradeData = HCClass.HCClass.gql("where teacher_username = '"+user.username+"' and class_name = '"+classname+"'").fetch(1)
            for c in ClassGradeData:
                classgrade = c.class_skill
            NoClassCreated = "N"
        '''this is when teacher selects the worksheet'''
        if worksheet_selected is not None:
            test_id = worksheet_selected
            NoClassCreated = "N"
               
        if NoClassCreated == "N":
            Config.report_values.update(TeacherReports.GenerateReports().GenerateClassWorksheetSummaryReport(user,classname,classgrade,test_id))
            Config.report_values.update(TeacherReports.GenerateReports().GenerateClassConceptSummaryReport(user,classname,classgrade,Config.report_values['StudentData'],concept_selected))
            Config.report_values.update({'display_class_name':classname,'display_worksheet_id':test_id,'display_concept_id':concept_selected})
        return self.render_response('Reports/TeacherReports/TeacherReports.html', **Config.report_values)
            
                
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()