'''
Created on Jan 13, 2011

@author: Farhat
'''
from tipfy import RequestHandler
from tipfy import Rule
from Config import config
import Config
from tipfy import Tipfy
from tipfy.auth import login_required,UserRequiredIfAuthenticatedMiddleware,user_required,teacher_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from Reports import Reports
import logging
from Database import HCSubscription, TestsMaster
from Models import HomeCampusUser

rules = [
         Rule('/Progress', endpoint='', handler='GenerateReport.GenerateReports'),
         Rule('/Progress/Generate_Dashboard_Report', endpoint='', handler='GenerateReport.GenerateDashboardReport'),
         Rule('/Progress/Generate_Summary_Report', endpoint='', handler='GenerateReport.GenerateSummaryReport'),
         Rule('/Progress/Generate_Detail_Report', endpoint='', handler='GenerateReport.GenerateDetailReport'),
         Rule('/Progress/Generate_Problem_Report', endpoint='', handler='GenerateReport.GenerateProblemReport'),
         Rule('/Progress/Generate_Test_Summary_Report', endpoint='', handler='GenerateReport.GenerateTestSummaryReport'),
         Rule('/Progress/Generate_Test_Report', endpoint='', handler='GenerateReport.GenerateTestReport'),
         Rule('/Progress/Generate_HC_Goals_Report', endpoint='', handler='GenerateReport.GenerateGoalsReport'),
         Rule('/Progress/Report_by_Concept', endpoint='', handler='GenerateReport.GenerateConceptReport'),
         Rule('/Progress/Report_by_HCRank', endpoint='', handler='GenerateReport.GenerateRankReport'),
         Rule('/Progress/Generate_Student_Report', endpoint='', handler='GenerateReport.GenerateStudentReport'),         
         Rule('/auth/login', endpoint='', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.SignupHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),]
      
class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]

    def render_response(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session
        
        TRIAL = "N"
        if self.auth.user:
            HCUser = HCSubscription.HCSubscription.gql("where email = '"+self.auth.user.email+"' and status='ACTIVE'").fetch(1)
            for h in HCUser:
                if h.paypal_token in ["TRIAL","WAIVED"]:
                    TRIAL = "Y"
        
        if self.auth.user.authorized:   
            SubscribeMessage="N"
        else:
            SubscribeMessage="Y"
        
        UnfinishedWorksheetsCount = 0    
        if self.auth.user and not self.auth.user.IsParent and not self.auth.user.IsTeacher:
            UnfinishedWorksheetData = TestsMaster.TestsMasterTable.gql("where student_id = '"+self.auth.user.username+"'").fetch(10)
            for u in UnfinishedWorksheetData:
                if u.status!='Completed':
                    UnfinishedWorksheetsCount = UnfinishedWorksheetsCount + 1
            if UnfinishedWorksheetsCount > 6:
                UnfinishedWorksheetsCount = "5+"           
        
        kwargs.update({
            'auth_session': auth_session,
            'current_user': self.auth.user,
            'login_url':    self.auth.login_url(),
            'logout_url':   self.auth.logout_url(),
            'current_url':  self.request.url,
            'TRIAL':TRIAL,
            'SubscribeMessage':SubscribeMessage,
            'UnfinishedWorksheetsCount':UnfinishedWorksheetsCount
        })

        return super(BaseHandler, self).render_response(filename, **kwargs)

class GenerateReports(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        user = self.auth.user
        if user.IsTeacher:
            return self.redirect("/Teacher/Class_Report_Card")
        Config.report_values = Reports.GenerateReports().GenerateReport(user)
        try:
            username = Config.report_values['Children'][0]['id']        
            grade = Config.report_values['Children'][0]['grade']
            Config.report_values.update(Reports.GenerateReports().GenerateSummaryReport(user,username,grade))
            Config.report_values.update(Reports.GenerateReports().GenerateTestSummaryReport(user,username,grade))
        except IndexError:
            Config.report_values.update({"NoUserCreated":"Y"})  
        return self.render_response('Reports/Reports.html', **Config.report_values)

class GenerateDashboardReport(BaseHandler):   
    @login_required   
    def post(self, **kwargs):
        user = self.auth.user
        username = unicode(self.request.form.get('username'))
        logging.info(username)
        grade = str(self.request.form.get('grade'))
        Config.report_values = Reports.GenerateReports().GenerateSummaryReport(user,username,grade)
        Config.report_values.update(Reports.GenerateReports().GenerateTestSummaryReport(user,username,grade))
        return self.render_response('Reports/Dashboard.html', **Config.report_values)
    
class GenerateSummaryReport(BaseHandler):   
    @login_required   
    def post(self, **kwargs):
        username = unicode(self.request.form.get('username'))
        grade = str(self.request.form.get('grade'))
        Config.report_values = Reports.GenerateReports().GenerateSummaryReport(self.auth.user,username,grade)
        return self.render_response('Reports/Summary_Report.html', **Config.report_values)
    
class GenerateDetailReport(BaseHandler):   
    @login_required   
    def post(self, **kwargs):
        username = unicode(self.request.form.get('username'))
        grade = str(self.request.form.get('grade'))
        topic = str(self.request.form.get('topic'))
        TopicName = str(self.request.form.get('TopicName'))
        Config.report_values = Reports.GenerateReports().GenerateDetailReport(self.auth.user,username,grade,topic,TopicName)   
        return self.render_response('Reports/Detail_Report.html', **Config.report_values)
    
class GenerateProblemReport(BaseHandler):   
    @login_required   
    def post(self, **kwargs):
        username = unicode(self.request.form.get('username'))
        grade = str(self.request.form.get('grade'))
        topic = str(self.request.form.get('topic'))
        TopicName = str(self.request.form.get('TopicName'))
        Config.report_values = Reports.GenerateReports().GenerateProblemReport(self.auth.user,username,grade,topic,TopicName)   
        return self.render_response('Reports/Problem_Report.html', **Config.report_values)
    
class GenerateTestSummaryReport(BaseHandler):   
    @login_required   
    def post(self, **kwargs):
        username = unicode(self.request.form.get('username'))
        grade = str(self.request.form.get('grade'))
        Config.report_values = Reports.GenerateReports().GenerateTestSummaryReport(self.auth.user,username,grade)   
        return self.render_response('Reports/Test_Summary_Report.html', **Config.report_values)
    
class GenerateGoalsReport(BaseHandler):   
    @login_required   
    def post(self, **kwargs):
        username = unicode(self.request.form.get('username'))
        grade = str(self.request.form.get('grade'))
        topic = str(self.request.form.get('topic'))
        Config.report_values = Reports.GenerateReports().GenerateGoalsReport(self.auth.user,username,grade,topic)   
        return self.render_response('Reports/Goals_Report.html', **Config.report_values)
        
class GenerateConceptReport(BaseHandler):   
    @login_required   
    def post(self, **kwargs):
        StudentId = unicode(self.request.form.get('StudentId'))
        Config.report_values = Reports.GenerateReports().GenerateConceptReport(self.auth.user,StudentId)   
        return self.render_response('Reports/Report_by_Concept.html', **Config.report_values)
    
class GenerateRankReport(BaseHandler):   
    @login_required   
    def post(self, **kwargs):
        StudentId = unicode(self.request.form.get('StudentId'))
        Config.report_values = Reports.GenerateReports().GenerateConceptReport(self.auth.user,StudentId)    
        return self.render_response('Reports/Report_by_Rank.html', **Config.report_values)
    
class GenerateTestReport(BaseHandler):   
    @login_required   
    def post(self, **kwargs):
        TestId = unicode(self.request.form.get('TestId'))
        Config.test_values = Reports.GenerateReports().GenerateTestReport(self.auth.user,TestId)
        
        if self.auth.user.authorized: 
            return self.render_response('Reports/Test_Report.html', **Config.test_values)
        else:
            logging.info(self.auth.user.username+" not authorized")
            return self.render_response('Reports/Report_Subscription_Advise.html', **Config.report_values)
        
class GenerateStudentReport(BaseHandler):   
    @teacher_required   
    def post(self, **kwargs):
        student_username = unicode(self.request.form.get('student_username'))
        user = self.auth.user
        logging.info(student_username)
        StudentQuery = HomeCampusUser.gql("where username = '"+student_username+"'").fetch(1)
        for s in StudentQuery:
            grade = s.skill
        logging.info(grade)
        #Config.report_values = Reports.GenerateReports().GenerateReport(user)
        #username = Config.report_values['Children'][0]['id']        
        #grade = Config.report_values['Children'][0]['grade']
        Config.report_values.update(Reports.GenerateReports().GenerateSummaryReport(user,student_username,grade))
        Config.report_values.update(Reports.GenerateReports().GenerateTestSummaryReport(user,student_username,grade))   
        return self.render_response('Reports/TeacherReports/StudentReport.html', **Config.report_values)
                                    
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()


            
    
    

    
        