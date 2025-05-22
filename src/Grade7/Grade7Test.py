from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy, Response
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from Database import HCSubscription
import logging
from Grade7 import Grade7TestQuestions, Grade7TestCheckAnswers
from Database import HCGrade7TestMaster, HCGrade7TestQuestions
import datetime
import string

rules = [Rule('/', endpoint='', handler='HomePage.HomePage'),
         Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.SignupHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/Grade-7-Topical-Test-By-Name', endpoint='', handler='Grade7.Grade7Test.Grade7TestLoadByName'),
         Rule('/Grade-7-Topical-Test-Save-Answer', endpoint='', handler='Grade7.Grade7Test.Grade7SaveTestAnswer'),
         Rule('/Grade-7-Topical-Test-Save-Time', endpoint='', handler='Grade7.Grade7Test.Grade7SaveTestTime'),
         Rule('/Grade-7-Topical-Test-Save-And-Load', endpoint='', handler='Grade7.Grade7Test.Grade7SaveAndLoadTest'),
         Rule('/Grade-7-Topical-Test-Submit', endpoint='', handler='Grade7.Grade7Test.Grade7SubmitTest'),
         
         ]

class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]

    def render_template(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session
        
        TRIAL = "N"
        if self.auth.user:
            HCUser = HCSubscription.HCSubscription.gql("where email = '"+self.auth.user.email+"' and status='ACTIVE'").fetch(1)
            for h in HCUser:
                if h.paypal_token in ["TRIAL","WAIVED"]:
                    TRIAL = "Y"
            
        kwargs.update({
            'auth_session': auth_session,
            'current_user': self.auth.user,
            'login_url':    self.auth.login_url(),
            'logout_url':   self.auth.logout_url(),
            'current_url':  self.request.url,
            'register_url': self.auth.signup_url(),
            'TRIAL':TRIAL
        })

        return super(BaseHandler, self).render_template(filename, **kwargs)
     
class Grade7TestLoadByName(BaseHandler):  
    def post(self, **kwargs):
        student_id = str(self.request.form.get('student_id'))
        htmlPageLeft = str(self.request.form.get('leftPage'))
        htmlPageRight = str(self.request.form.get('rightPage'))
        test_topic = str(self.request.form.get('test_topic'))
        attempt = int(self.request.form.get('attempt'))
        test_id = test_topic+"_"+str(attempt)
        test_start = str(self.request.form.get('test_start'))
        total_marks = int(self.request.form.get('total_marks'))
        if test_start == 'Y':
            self.saveNewTestMaster(student_id,test_topic,attempt,test_id,total_marks)

        Grade7TestMasterData = HCGrade7TestMaster.HCGrade7TestMaster.gql("where student_id = '"+student_id+"' and test_id = '"+test_id+"'").fetch(1)
        elapsed_time_seconds = 0
        try:
            elapsed_time_seconds = Grade7TestMasterData[0].elapsed_time        
        except IndexError:
            pass
        params = generateTestPageParameters(test_id,student_id)
        params.update({"test_id":test_id,"student_id":student_id,"elapsed_time_seconds":elapsed_time_seconds,'test_attempt':attempt})

        leftPageHtml = self.render_template(htmlPageLeft,**params)
        rightPageHtml = self.render_template(htmlPageRight,**params)

        responseText = leftPageHtml+"PAGEBREAK"+rightPageHtml

        response = Response(responseText)        
        return response

    def saveNewTestMaster(self, student_id,test_topic,attempt,test_id,total_marks):        
        Grade7TestMaster = HCGrade7TestMaster.HCGrade7TestMaster(test_id=test_id,
                                                                 test_topic=test_topic,
                                                                 student_id=student_id,
                                                                 start_date=datetime.datetime.now(),
                                                                 test_status="In Progress",
                                                                 elapsed_time=0,
                                                                 attempt=attempt,
                                                                 total_marks=total_marks
                                                                 )
        Grade7TestMaster.put()
     
class Grade7SaveAndLoadTest(BaseHandler):  
    def post(self, **kwargs):
        test_id = str(self.request.form.get('test_id'))
        student_id = str(self.request.form.get('student_id'))
        htmlPageLeft = str(self.request.form.get('leftPage'))
        htmlPageRight = str(self.request.form.get('rightPage'))
        total_elapsed_time = int(self.request.form.get('total_elapsed_time'))
        answer_ids = str(self.request.form.get('answer_ids')).split("#%$")
        
        Grade7TestMasterData = HCGrade7TestMaster.HCGrade7TestMaster.gql("where student_id = '"+student_id+"' and test_id = '"+test_id+"'").fetch(1)
        Grade7TestMasterData[0].elapsed_time = total_elapsed_time
        attempt = Grade7TestMasterData[0].attempt
        Grade7TestMasterData[0].put()
        '''Saving unattepted answers so that explanation can be shown later'''
        for i in range(len(answer_ids)):
            answer_id = answer_ids[i]
            Grade7TestQuestionData = HCGrade7TestQuestions.HCGrade7TestQuestions.gql("where student_id = '"+student_id+"' and answer_id = '"+answer_id+"' and test_id = '"+test_id+"'").fetch(1)
            if len(Grade7TestQuestionData)==0 and answer_id!='':
                question_id = Grade7TestQuestions.AllQuestions[answer_id]["QuestionId"]
                question_marks = Grade7TestQuestions.AllQuestions[answer_id]["Mark"]
                Grade7TestQuestion = HCGrade7TestQuestions.HCGrade7TestQuestions(test_id=test_id,
                                                                                 question_id=question_id,
                                                                                 answer_id=answer_id,
                                                                                 student_id=student_id,
                                                                                 save_date=datetime.datetime.now(),
                                                                                 question_marks=question_marks,
                                                                                 entered_answer='',
                                                                                 scored_marks=0,
                                                                                 )
                Grade7TestQuestion.put()                
        params = generateTestPageParameters(test_id,student_id)
        params.update({"test_id":test_id,"student_id":student_id,"elapsed_time_seconds":total_elapsed_time,'test_attempt':attempt})

        leftPageHtml = self.render_template(htmlPageLeft,**params)
        rightPageHtml = self.render_template(htmlPageRight,**params)

        responseText = leftPageHtml+"PAGEBREAK"+rightPageHtml

        response = Response(responseText)        
        return response

class Grade7SaveTestAnswer(BaseHandler):  
    def post(self, **kwargs):
        test_id = str(self.request.form.get('test_id'))
        answer_id = str(self.request.form.get('answer_id'))
        entered_answer = str(self.request.form.get('entered_answer'))
        student_id = unicode(self.request.form.get('student_id'))
        
        elapsed_time = int(self.request.form.get('elapsed_time'))
        Grade7TestMasterData = HCGrade7TestMaster.HCGrade7TestMaster.gql("where student_id = '"+student_id+"' and test_id = '"+test_id+"'").fetch(1)
        Grade7TestMasterData[0].elapsed_time = elapsed_time
        Grade7TestMasterData[0].put()
        CheckAndSaveAnswer(student_id, test_id, answer_id,entered_answer)        

        response = Response("")        
        return response

def CheckAndSaveAnswer(student_id, test_id, answer_id,entered_answer):
        Grade7TestQuestionData = HCGrade7TestQuestions.HCGrade7TestQuestions.gql("where student_id = '"+student_id+"' and answer_id = '"+answer_id+"' and test_id = '"+test_id+"'").fetch(1)
        #If answer is saved earlier we are simply overwriting or else creating a new entry in the datastore
        checkAnswerType = Grade7TestQuestions.AllQuestions[answer_id]["CheckAnswerType"]
        correct_answer = Grade7TestQuestions.AllQuestions[answer_id]["Answer"]
        question_id = Grade7TestQuestions.AllQuestions[answer_id]["QuestionId"]
        question_marks = Grade7TestQuestions.AllQuestions[answer_id]["Mark"]
        if question_id == "FMRTT1_7":
            correct = Grade7TestCheckAnswers.CheckAnswerForFMRTT1_7(student_id,test_id,answer_id,entered_answer)
        elif question_id == "FMRTT1_11":
            correct = Grade7TestCheckAnswers.CheckAnswerForFMRTT1_11(student_id,test_id,answer_id,entered_answer)
        else:        
            correct = CheckAnswer(checkAnswerType,correct_answer,entered_answer)
        scored_marks = 0
        if correct:
            scored_marks = question_marks           

        try:
            Grade7TestQuestionData[0].entered_answer = entered_answer
            Grade7TestQuestionData[0].save_date = datetime.datetime.now()
            Grade7TestQuestionData[0].correct = correct
            Grade7TestQuestionData[0].scored_marks = scored_marks
            Grade7TestQuestionData[0].put()
        except IndexError:
            Grade7TestQuestion = HCGrade7TestQuestions.HCGrade7TestQuestions(test_id=test_id,
                                                                             question_id=question_id,
                                                                             answer_id=answer_id,
                                                                             student_id=student_id,
                                                                             entered_answer=entered_answer,
                                                                             save_date=datetime.datetime.now(),
                                                                             question_marks=question_marks,
                                                                             scored_marks=scored_marks,
                                                                             correct=correct
                                                                             )
            Grade7TestQuestion.put()
 
                
class Grade7SaveTestTime(BaseHandler):  
    def post(self, **kwargs):
        test_id = str(self.request.form.get('test_id'))
        total_seconds_elapsed = int(self.request.form.get('total_seconds_elapsed'))
        student_id = unicode(self.request.form.get('student_id'))
        Grade7TestMasterData = HCGrade7TestMaster.HCGrade7TestMaster.gql("where student_id = '"+student_id+"' and test_id = '"+test_id+"'").fetch(1)
        Grade7TestMasterData[0].elapsed_time = total_seconds_elapsed
        Grade7TestMasterData[0].put()
        response = Response("")        
        return response     

class Grade7SubmitTest(BaseHandler):  
    def post(self, **kwargs):
        test_id = str(self.request.form.get('test_id'))
        total_seconds_elapsed = int(self.request.form.get('total_seconds_elapsed'))
        student_id = unicode(self.request.form.get('student_id'))
        answer_ids = str(self.request.form.get('answer_ids')).split("#%$")
        saved_answer_ids = []     
        test_score = 0
        Grade7TestQuestionData = HCGrade7TestQuestions.HCGrade7TestQuestions.gql("where student_id = '"+student_id+"' and test_id = '"+test_id+"'").fetch(100)
        for tq in Grade7TestQuestionData:
            '''sometimes there are duplicate entry is saved for same answer_id so making sure when counting the marks its counted only once'''
            if tq.answer_id not in saved_answer_ids:
                '''sometimes there are duplicate entries for same answer one with input answer and one with null as both check answer and ">>" page click tries to save the same answer..'''
                if tq.correct is not None:
                    saved_answer_ids.append(tq.answer_id)
                    test_score = test_score + tq.scored_marks

        '''Saving unattempted answers so that explanation can be shown later'''
        for i in range(len(answer_ids)):
            answer_id = answer_ids[i]
            if answer_id not in saved_answer_ids:
                question_id = Grade7TestQuestions.AllQuestions[answer_id]["QuestionId"]
                question_marks = Grade7TestQuestions.AllQuestions[answer_id]["Mark"]
                Grade7TestQuestion = HCGrade7TestQuestions.HCGrade7TestQuestions(test_id=test_id,
                                                                                 question_id=question_id,
                                                                                 answer_id=answer_id,
                                                                                 student_id=student_id,
                                                                                 save_date=datetime.datetime.now(),
                                                                                 question_marks=question_marks,
                                                                                 entered_answer='',
                                                                                 scored_marks=0,
                                                                                 )
                Grade7TestQuestion.put() 
        
            
        Grade7TestMasterData = HCGrade7TestMaster.HCGrade7TestMaster.gql("where student_id = '"+student_id+"' and test_id = '"+test_id+"'").fetch(1)
        Grade7TestMasterData[0].elapsed_time = total_seconds_elapsed
        Grade7TestMasterData[0].test_status = "Completed"
        Grade7TestMasterData[0].test_score = test_score
        Grade7TestMasterData[0].end_date = datetime.datetime.now()
        Grade7TestMasterData[0].put()
        
        response = Response("")        
        return response



def CheckAnswer(checkAnswerType,correct_answer,entered_answer):
    if checkAnswerType == 1:
        try:
            return int(correct_answer)==int(entered_answer)
        except ValueError:
            return False
    elif checkAnswerType == 2:
        '''checking for comma separated answer'''
        try:
            correct_answer = str(correct_answer).split(",")
            entered_answer = string.join(entered_answer.split(),"")
            entered_answer = str(entered_answer).split(",")
            correct_answer.sort()
            entered_answer.sort()
            return correct_answer == entered_answer
        except ValueError:
            return False       
    elif checkAnswerType == 3:
        '''checking for string and MCQ answers'''
        try:
            correct_answer = string.join(str(correct_answer).split(),"")
            entered_answer = string.join(str(entered_answer).split(),"")
            return correct_answer == entered_answer
        except ValueError:
            return False                 
    elif checkAnswerType == 4:
        '''checking for float'''
        try:
            return float(correct_answer) == float(entered_answer)
        except ValueError:
            return False               
    elif checkAnswerType == 5:
        '''checking for multiple correct answers in a list'''
        try:
            return string.join(str(entered_answer).lower().split(),"") in (string.join(answer.lower().split(),"") for answer in correct_answer)
        except ValueError:
            return False 
    elif checkAnswerType == 6:
        '''checking for comma separated float answer'''
        try:          
            correct_answer = str(correct_answer).split(",")
            entered_answer = string.join(entered_answer.split(),"")
            entered_answer = str(entered_answer).split(",")
            float_correct_answer = []
            float_entered_answer = []
            for i in range(len(correct_answer)):
                float_correct_answer.append(float(correct_answer[i]))
            for i in range(len(entered_answer)):
                float_entered_answer.append(float(entered_answer[i]))                
            return float_correct_answer == float_entered_answer
        except ValueError:
            return False 
    elif checkAnswerType == 7:
        '''case-insensitive string check'''
        try:
            correct_answer = string.join(str(correct_answer).split(),"")
            entered_answer = string.join(str(entered_answer).split(),"")
            return correct_answer.lower() == entered_answer.lower()
        except ValueError:
            return False 

   
def generateTestPageParameters(test_id, student_id ):
    params = {}
    Grade7TestMasterData = HCGrade7TestMaster.HCGrade7TestMaster.gql("where student_id = '"+student_id+"' and test_id = '"+test_id+"'").fetch(1)
    for m in Grade7TestMasterData:
        params.update({'test_status':m.test_status})
    Grade7TestData = HCGrade7TestQuestions.HCGrade7TestQuestions.gql("where student_id = '"+student_id+"' and test_id = '"+test_id+"'").fetch(100)
    for q in Grade7TestData:
        if q.answer_id in params and params[q.answer_id+"_correct"] is not None:
            '''Do Nothing as sometimes there are duplicate entries for same answer one with input answer and one with null as both check answer and ">>" page click tries to save the same answer..so if correct answer has been added to params then we are not overwriting it with null answer'''
        else:
            params.update({q.answer_id:q.entered_answer,q.answer_id+"_correct":q.correct,
                           q.answer_id+"_explain":Grade7TestQuestions.AllQuestions[q.answer_id]["Explanation"]})
    logging.info(params)  
    return params
        
def CreateTimeString(seconds):
    hours = seconds/3600
    if hours < 10:
        hours = "0"+str(hours)
    seconds = seconds % 3600
    minutes = seconds/60
    if minutes < 10:
        minutes = "0"+str(minutes)
    seconds = seconds % 60
    if seconds < 10:
        seconds = "0"+str(seconds)
    timeString = str(hours)+":"+str(minutes)+":"+str(seconds)
    return timeString

          
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()