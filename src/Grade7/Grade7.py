from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy, Response
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from Database import HCBooks
import logging
from Grade7 import Grade7PageConfig, Grade7Questions, Grade7CheckAnswers
from Database import HCGrade7Questions, HCGrade7TestMaster
import datetime
import string
from Models import HomeCampusUser

rules = [Rule('/', endpoint='', handler='HomePage.HomePage'),
         Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.SignupHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/Grade-7-Book-Page-Load', endpoint='', handler='Grade7.Grade7.Grade7PageLoad'),
         Rule('/Grade-7-Book-Page-Load-By-Name', endpoint='', handler='Grade7.Grade7.Grade7PageLoadByName'),
         Rule('/Grade-7-Book-Save-Answer', endpoint='', handler='Grade7.Grade7.Grade7SaveAnswer'),
         Rule('/Grade-7-Book-Submit-Answer', endpoint='', handler='Grade7.Grade7.Grade7SubmitAnswer'),
         Rule('/Grade-7-Book-Clear-Answer', endpoint='', handler='Grade7.Grade7.Grade7ClearAnswer'),
         Rule('/Grade-7', endpoint='', handler='HomePage.Secondary1'),     
         ]

class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]

    def render_template(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session
           
        kwargs.update({
            'auth_session': auth_session,
            'current_user': self.auth.user,
            'login_url':    self.auth.login_url(),
            'logout_url':   self.auth.logout_url(),
            'current_url':  self.request.url,
            'register_url': self.auth.signup_url()
        })

        return super(BaseHandler, self).render_template(filename, **kwargs)
     
class Grade7PageLoad(BaseHandler):  
    def post(self, **kwargs):
        left_page_number = int(self.request.form.get('leftPage'))
        right_page_number = int(self.request.form.get('rightPage'))
        book_code = str(self.request.form.get('book_code'))

        paramsLeft = {'page_number':left_page_number,'page_class':"leftPageNumberClass",'book_code':book_code,}
        paramsRight = {'page_number':right_page_number,'page_class':"rightPageNumberClass",'book_code':book_code,}
                
        if book_code == "7A":
            htmlPageLeft = Grade7PageConfig.Grade7APages[left_page_number]
            htmlPageRight = Grade7PageConfig.Grade7APages[right_page_number]
            '''getting the page name for AJAX # tag'''
            pageName = htmlPageRight[htmlPageRight.rindex("/")+1:-5]
            
            '''checking if the page requires login or subscription for access'''
            if htmlPageLeft in Grade7PageConfig.RequiresLogin7A:
                paramsLeft.update({'nextFreeTopic':Grade7PageConfig.RequiresLogin7A[htmlPageLeft][1],'currentPageName':pageName})
                htmlPageLeft = getHtmlPage(htmlPageLeft,self.auth.user,Grade7PageConfig.RequiresLogin7A[htmlPageLeft][0],Grade7PageConfig.RequiresLogin7A[htmlPageLeft][1],book_code)
                
            '''checking if the page requires login or subscription for access'''
            if htmlPageRight in Grade7PageConfig.RequiresLogin7A:
                paramsRight.update({'nextFreeTopic':Grade7PageConfig.RequiresLogin7A[htmlPageRight][1],'currentPageName':pageName})
                htmlPageRight = getHtmlPage(htmlPageRight,self.auth.user,Grade7PageConfig.RequiresLogin7A[htmlPageRight][0],Grade7PageConfig.RequiresLogin7A[htmlPageRight][1],book_code)               
           
        elif book_code == "7B":
            htmlPageLeft = Grade7PageConfig.Grade7BPages[left_page_number]
            htmlPageRight = Grade7PageConfig.Grade7BPages[right_page_number]
            
            '''getting the page name for AJAX # tag'''
            pageName = htmlPageRight[htmlPageRight.rindex("/")+1:-5]
            
            '''checking if the page requires login or subscription for access'''
            if htmlPageLeft in Grade7PageConfig.RequiresLogin7B:
                paramsLeft.update({'nextFreeTopic':Grade7PageConfig.RequiresLogin7B[htmlPageLeft][1],'currentPageName':pageName})
                htmlPageLeft = getHtmlPage(htmlPageLeft,self.auth.user,Grade7PageConfig.RequiresLogin7B[htmlPageLeft][0],Grade7PageConfig.RequiresLogin7B[htmlPageLeft][1],book_code)
                
            '''checking if the page requires login or subscription for access'''
            if htmlPageRight in Grade7PageConfig.RequiresLogin7B:
                paramsRight.update({'nextFreeTopic':Grade7PageConfig.RequiresLogin7B[htmlPageRight][1],'currentPageName':pageName})
                htmlPageRight = getHtmlPage(htmlPageRight,self.auth.user,Grade7PageConfig.RequiresLogin7B[htmlPageRight][0],Grade7PageConfig.RequiresLogin7B[htmlPageRight][1],book_code)           
           
        elif book_code == "7C":
            htmlPageLeft = Grade7PageConfig.Grade7CPages[left_page_number]
            htmlPageRight = Grade7PageConfig.Grade7CPages[right_page_number]
            
            '''getting the page name for AJAX # tag'''
            pageName = htmlPageRight[htmlPageRight.rindex("/")+1:-5]
            
            '''checking if the page requires login or subscription for access'''
            if htmlPageLeft in Grade7PageConfig.RequiresLogin7C:
                paramsLeft.update({'nextFreeTopic':Grade7PageConfig.RequiresLogin7C[htmlPageLeft][1],'currentPageName':pageName})
                htmlPageLeft = getHtmlPage(htmlPageLeft,self.auth.user,Grade7PageConfig.RequiresLogin7C[htmlPageLeft][0],Grade7PageConfig.RequiresLogin7C[htmlPageLeft][1],book_code)
                
            '''checking if the page requires login or subscription for access'''
            if htmlPageRight in Grade7PageConfig.RequiresLogin7C:
                paramsRight.update({'nextFreeTopic':Grade7PageConfig.RequiresLogin7C[htmlPageRight][1],'currentPageName':pageName})
                htmlPageRight = getHtmlPage(htmlPageRight,self.auth.user,Grade7PageConfig.RequiresLogin7C[htmlPageRight][0],Grade7PageConfig.RequiresLogin7C[htmlPageRight][1],book_code)           
    
    
        #if both right and left page are locked then we don't show duplicate lock pages..instead right page is made simple.
        if htmlPageLeft == htmlPageRight and htmlPageRight == "/Grade-7/Login-Lock-Page.html":
            htmlPageRight = "/Grade-7/Login-Lock-Page-Simple.html"
        if htmlPageLeft == htmlPageRight and (htmlPageRight == "/Grade-7/7A-Auth-Lock-Page.html" or htmlPageRight == "/Grade-7/7B-Auth-Lock-Page.html"):
            htmlPageRight = "/Grade-7/Auth-Lock-Page-Simple.html"
                   
        if self.auth.user:
            paramsLeft.update(GeneratePageParameters(htmlPageLeft,book_code,self.auth.user))
            paramsRight.update(GeneratePageParameters(htmlPageRight,book_code,self.auth.user))            
        
        '''Getting left and right page html and next page numbers so that on arrow click the correct pages are loaded'''
        leftPageHtml = self.render_template(htmlPageLeft,**paramsLeft)
        leftArrowHtml = '<div id="'+book_code+str(left_page_number-1)+'" class="leftTurnArrow" onclick="leftTurnArrowClick(this)"></div>'
        rightPageHtml = self.render_template(htmlPageRight,**paramsRight)
        rightArrowHtml = '<div id="'+book_code+str(right_page_number+1)+'" class="rightTurnArrow" onclick="rightTurnArrowClick(this)"></div>'        
        

        responseText = leftPageHtml+"PAGEBREAK"+leftArrowHtml+"PAGEBREAK"+rightPageHtml+"PAGEBREAK"+rightArrowHtml+"PAGEBREAK"+pageName

        response = Response(responseText)        
        return response
     
class Grade7PageLoadByName(BaseHandler):  
    def post(self, **kwargs):
        page_name = str(self.request.form.get('pageName'))
        if page_name in Grade7PageConfig.PageMapping7A:
            book_code = "7A"
            page_number = Grade7PageConfig.Grade7APages.index(Grade7PageConfig.PageMapping7A[page_name])
        elif page_name in Grade7PageConfig.PageMapping7B:
            book_code = "7B"
            page_number = Grade7PageConfig.Grade7BPages.index(Grade7PageConfig.PageMapping7B[page_name])
        elif page_name in Grade7PageConfig.PageMapping7C:
            book_code = "7C"
            page_number = Grade7PageConfig.Grade7CPages.index(Grade7PageConfig.PageMapping7C[page_name])
        
        if page_number%2 == 0:
            left_page_number = page_number
            right_page_number = page_number+1
        else:
            left_page_number = page_number-1
            right_page_number = page_number          
 
        paramsLeft = {'page_number':left_page_number,'page_class':"leftPageNumberClass",'book_code':book_code,}
        paramsRight = {'page_number':right_page_number,'page_class':"rightPageNumberClass",'book_code':book_code,}
                
        if book_code == "7A":
            htmlPageLeft = Grade7PageConfig.Grade7APages[left_page_number]
            htmlPageRight = Grade7PageConfig.Grade7APages[right_page_number]
            '''getting the page name for AJAX # tag'''
            pageName = htmlPageRight[htmlPageRight.rindex("/")+1:-5]
            
            '''checking if the page requires login or subscription for access'''
            if htmlPageLeft in Grade7PageConfig.RequiresLogin7A:
                paramsLeft.update({'nextFreeTopic':Grade7PageConfig.RequiresLogin7A[htmlPageLeft][1],'currentPageName':pageName})
                htmlPageLeft = getHtmlPage(htmlPageLeft,self.auth.user,Grade7PageConfig.RequiresLogin7A[htmlPageLeft][0],Grade7PageConfig.RequiresLogin7A[htmlPageLeft][1],book_code)
                
            '''checking if the page requires login or subscription for access'''
            if htmlPageRight in Grade7PageConfig.RequiresLogin7A:
                paramsRight.update({'nextFreeTopic':Grade7PageConfig.RequiresLogin7A[htmlPageRight][1],'currentPageName':pageName})
                htmlPageRight = getHtmlPage(htmlPageRight,self.auth.user,Grade7PageConfig.RequiresLogin7A[htmlPageRight][0],Grade7PageConfig.RequiresLogin7A[htmlPageRight][1],book_code)               
           
        elif book_code == "7B":
            htmlPageLeft = Grade7PageConfig.Grade7BPages[left_page_number]
            htmlPageRight = Grade7PageConfig.Grade7BPages[right_page_number]
            
            '''getting the page name for AJAX # tag'''
            pageName = htmlPageRight[htmlPageRight.rindex("/")+1:-5]
            
            '''checking if the page requires login or subscription for access'''
            if htmlPageLeft in Grade7PageConfig.RequiresLogin7B:
                paramsLeft.update({'nextFreeTopic':Grade7PageConfig.RequiresLogin7B[htmlPageLeft][1],'currentPageName':pageName})
                htmlPageLeft = getHtmlPage(htmlPageLeft,self.auth.user,Grade7PageConfig.RequiresLogin7B[htmlPageLeft][0],Grade7PageConfig.RequiresLogin7B[htmlPageLeft][1],book_code)
                
            '''checking if the page requires login or subscription for access'''
            if htmlPageRight in Grade7PageConfig.RequiresLogin7B:
                paramsRight.update({'nextFreeTopic':Grade7PageConfig.RequiresLogin7B[htmlPageRight][1],'currentPageName':pageName})
                htmlPageRight = getHtmlPage(htmlPageRight,self.auth.user,Grade7PageConfig.RequiresLogin7B[htmlPageRight][0],Grade7PageConfig.RequiresLogin7B[htmlPageRight][1],book_code)           

        elif book_code == "7C":
            htmlPageLeft = Grade7PageConfig.Grade7CPages[left_page_number]
            htmlPageRight = Grade7PageConfig.Grade7CPages[right_page_number]
            
            '''getting the page name for AJAX # tag'''
            pageName = htmlPageRight[htmlPageRight.rindex("/")+1:-5]
            
            '''checking if the page requires login or subscription for access'''
            if htmlPageLeft in Grade7PageConfig.RequiresLogin7C:
                paramsLeft.update({'nextFreeTopic':Grade7PageConfig.RequiresLogin7C[htmlPageLeft][1],'currentPageName':pageName})
                htmlPageLeft = getHtmlPage(htmlPageLeft,self.auth.user,Grade7PageConfig.RequiresLogin7C[htmlPageLeft][0],Grade7PageConfig.RequiresLogin7C[htmlPageLeft][1],book_code)
                
            '''checking if the page requires login or subscription for access'''
            if htmlPageRight in Grade7PageConfig.RequiresLogin7C:
                paramsRight.update({'nextFreeTopic':Grade7PageConfig.RequiresLogin7C[htmlPageRight][1],'currentPageName':pageName})
                htmlPageRight = getHtmlPage(htmlPageRight,self.auth.user,Grade7PageConfig.RequiresLogin7C[htmlPageRight][0],Grade7PageConfig.RequiresLogin7C[htmlPageRight][1],book_code)           
    
    
        #if both right and left page are locked then we don't show duplicate lock pages..instead right page is made simple.
        if htmlPageLeft == htmlPageRight and htmlPageRight == "/Grade-7/Login-Lock-Page.html":
            htmlPageRight = "/Grade-7/Login-Lock-Page-Simple.html"
        if htmlPageLeft == htmlPageRight and (htmlPageRight == "/Grade-7/7A-Auth-Lock-Page.html" or htmlPageRight == "/Grade-7/7B-Auth-Lock-Page.html"):
            htmlPageRight = "/Grade-7/Auth-Lock-Page-Simple.html"
                   
        if self.auth.user:
            paramsLeft.update(GeneratePageParameters(htmlPageLeft,book_code,self.auth.user))
            paramsRight.update(GeneratePageParameters(htmlPageRight,book_code,self.auth.user))            
        
        '''Getting left and right page html and next page numbers so that on arrow click the correct pages are loaded'''
        leftPageHtml = self.render_template(htmlPageLeft,**paramsLeft)
        leftArrowHtml = '<div id="'+book_code+str(left_page_number-1)+'" class="leftTurnArrow" onclick="leftTurnArrowClick(this)"></div>'
        rightPageHtml = self.render_template(htmlPageRight,**paramsRight)
        rightArrowHtml = '<div id="'+book_code+str(right_page_number+1)+'" class="rightTurnArrow" onclick="rightTurnArrowClick(this)"></div>'        
        

        responseText = leftPageHtml+"PAGEBREAK"+leftArrowHtml+"PAGEBREAK"+rightPageHtml+"PAGEBREAK"+rightArrowHtml+"PAGEBREAK"+pageName+"PAGEBREAK"+book_code

        response = Response(responseText)        
        return response

def getHtmlPage(pageName,user,subscriptionRequired,nextFreePage,book_code):
    htmlPage = pageName
    if not user:
        htmlPage = "/Grade-7/Login-Lock-Page.html"
    else:
        userAuthorised = False
        if user.IsParent:
            UserAuthorization = HCBooks.HCBooks.gql("where email = '"+user.email+"' and book_code = '"+book_code+"' and authorized = True").fetch(1)
        else:
            UserAuthorization = HCBooks.HCBooks.gql("where username = '"+user.username+"' and book_code = '"+book_code+"' and authorized = True").fetch(1)
        for UA in UserAuthorization:
            userAuthorised = UA.authorized
            
        if subscriptionRequired and not userAuthorised:
            if book_code == "7A":
                htmlPage = "/Grade-7/7A-Auth-Lock-Page.html"
            elif book_code == "7B":
                htmlPage = "/Grade-7/7B-Auth-Lock-Page.html"
            
    return htmlPage
           
class Grade7SaveAnswer(BaseHandler):  
    def post(self, **kwargs):
        logging.info("save answer")
        question_id = str(self.request.form.get('question_id'))
        question_type = str(self.request.form.get('question_type'))
        answer_id = str(self.request.form.get('answer_id'))
        entered_answer = unicode(self.request.form.get('entered_answer'))
        student_id = unicode(self.request.form.get('student_id'))
        Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and answer_id = '"+answer_id+"'").fetch(1)
        #If answer is saved earlier we are simply overwriting or else creating a new entry in the datastore
        try:
            Grade7QuestionData[0].entered_answer = entered_answer
            Grade7QuestionData[0].save_date = datetime.datetime.now()
            Grade7QuestionData[0].put()
        except IndexError:
            Grade7Question = HCGrade7Questions.HCGrade7Questions(question_id=question_id,
                                                                 answer_id=answer_id,
                                                                 student_id=student_id,
                                                                 entered_answer=entered_answer,
                                                                 question_type=question_type,
                                                                 save_date=datetime.datetime.now()
                                                                 )
            Grade7Question.put()
        response = Response("")        
        return response
     
class Grade7SubmitAnswer(BaseHandler):  
    def post(self, **kwargs):
        question_type = str(self.request.form.get('question_type'))
        student_id = unicode(self.request.form.get('student_id'))
        answers = unicode(self.request.form.get('answers')).split("#%$")
        #checking if all the questions are saved in the database if not then saving them
        i = 0
        while i < len(answers):
            question_id = answers[i]
            answer_id = answers[i+1]
            entered_answer = answers[i+2]
            checkAnswerType = Grade7Questions.AllQuestions[answer_id]["CheckAnswerType"]
            correct_answer = Grade7Questions.AllQuestions[answer_id]["Answer"]
            Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and answer_id = '"+answer_id+"'").fetch(1)
            try:
                Grade7QuestionData[0].submit_date = datetime.datetime.now()
                Grade7QuestionData[0].submitted = True
                Grade7QuestionData[0].entered_answer = entered_answer
                Grade7QuestionData[0].correct = CheckAnswer(checkAnswerType,correct_answer,entered_answer)
                Grade7QuestionData[0].put()                
            except IndexError:
                Grade7Question = HCGrade7Questions.HCGrade7Questions(question_id=question_id,
                                                                     answer_id=answer_id,
                                                                     student_id=student_id,
                                                                     entered_answer=entered_answer,
                                                                     question_type=question_type,
                                                                     save_date=datetime.datetime.now(),
                                                                     submit_date=datetime.datetime.now(),
                                                                     submitted=True,
                                                                     correct=CheckAnswer(checkAnswerType,correct_answer,entered_answer)
                                                                     )
                Grade7Question.put()
            i=i+3                             
            
            #for some questions there are multiple input answer box and all answers need to be evaluate together. For e.g look at question PCMedium_1
            if question_id == "PCMedium_1" and answer_id == "PCMedium_1_6_answer":
                Grade7CheckAnswers.CheckAnswerForPCMedium_1(student_id)
            elif question_id == "PCMedium_2" and answer_id == "PCMedium_2_3_answer":
                Grade7CheckAnswers.CheckAnswerForPCMedium_2(student_id,question_id,26)
            elif question_id == "PCMedium_3" and answer_id == "PCMedium_3_3_answer":
                Grade7CheckAnswers.CheckAnswerForPCMedium_2(student_id,question_id,77)
            elif question_id == "PCMedium_4" and answer_id == "PCMedium_4_3_answer":
                Grade7CheckAnswers.CheckAnswerForPCMedium_2(student_id,question_id,103)
            elif question_id == "PCAdvanced_2":
                Grade7CheckAnswers.CheckAnswerForPCAdvanced_2(student_id)                                                 
            elif question_id == "PFEasy_1":
                Grade7CheckAnswers.CheckAnswerForPFEasy_1(student_id)
            elif question_id == "PFEasy_6" and answer_id == "PFEasy_6_5_answer":
                Grade7CheckAnswers.CheckAnswerForPFEasy_6(student_id)             
            elif question_id == "PFEasy_7" and answer_id == "PFEasy_7_5_answer":
                Grade7CheckAnswers.CheckAnswerForPFEasy_7(student_id)             
            elif question_id == "PFEasy_13" and answer_id == "PFEasy_13_6_answer":
                Grade7CheckAnswers.CheckAnswerForPFEasy_13(student_id)             
            elif question_id == "PFMedium_1" and answer_id == "PFMedium_1_4_answer":
                Grade7CheckAnswers.CheckAnswerForPFMedium_1(student_id)             
            elif question_id == "PFMedium_2" and answer_id == "PFMedium_2_4_answer":
                Grade7CheckAnswers.CheckAnswerForPFMedium_2(student_id)             
            elif question_id == "PFMedium_3" and answer_id == "PFMedium_3_7_answer":
                Grade7CheckAnswers.CheckAnswerForPFMedium_3(student_id)             
            elif question_id == "PFAdvanced_1" and answer_id == "PFAdvanced_1_3_answer":
                Grade7CheckAnswers.CheckAnswerForPFAdvanced_1(student_id)             
            elif question_id == "HCFAdvanced_6" and answer_id == "HCFAdvanced_6_2_answer":
                Grade7CheckAnswers.CheckAnswerForHCFAdvanced_6(student_id)             
            elif question_id == "SSREasy_7" and answer_id == "SSREasy_7_5_answer":
                Grade7CheckAnswers.CheckAnswerForSSREasy_7(student_id)             
            elif question_id == "CCREasy_7" and answer_id == "CCREasy_7_5_answer":
                Grade7CheckAnswers.CheckAnswerForCCREasy_7(student_id)
            elif question_id == "C9SFEAdvanced_1" and answer_id == "C9SFEAdvanced_1_2_answer":
                Grade7CheckAnswers.CheckAnswerForC9SFEAdvanced_1(student_id)
                
        response = Response("")        
        return response
     
class Grade7ClearAnswer(BaseHandler):  
    def post(self, **kwargs):
        student_id = unicode(self.request.form.get('student_id'))
        answer_ids = str(self.request.form.get('answer_ids')).split(",")
        
        for i in range(len(answer_ids)):
            answer_id = answer_ids[i]
            Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and answer_id = '"+answer_id+"'").fetch(2)
            '''sometimes it saves 2 entries of the same question due to save and submit both trying to access the datastore..if that's the case then we keep only one entry and delete the other'''
            for g in range(len(Grade7QuestionData)):
                if g==0:
                    Grade7QuestionData[g].submitted = False
                    Grade7QuestionData[g].entered_answer = ""
                    Grade7QuestionData[g].correct = None
                    Grade7QuestionData[g].put()
                elif g==1:
                    Grade7QuestionData[g].delete()                                    
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
                                
def GeneratePageParameters(htmlPage,book_code,user):
    params = {}
    if book_code=="7A":
        if htmlPage=="/Grade-7/Chapter-1/Factors-and-Multiples-Easy-Questions-1.html":
            params = GetParameters('FactorsMultiples',user.username)
        elif htmlPage=="/Grade-7/Chapter-1/Factors-and-Multiples-Easy-Questions-2.html":
            params = GetParameters('FactorsMultiples',user.username)
        elif htmlPage=="/Grade-7/Chapter-1/Factors-and-Multiples-Easy-Questions-3.html":
            params = GetParameters('FactorsMultiples',user.username)
        elif htmlPage=="/Grade-7/Chapter-1/Factors-and-Multiples-Medium-Questions-1.html":
            params = GetParameters('FactorsMultiples',user.username)                                    
        elif htmlPage=="/Grade-7/Chapter-1/Factors-and-Multiples-Medium-Questions-2.html":
            params = GetParameters('FactorsMultiples',user.username)                                    
        elif htmlPage=="/Grade-7/Chapter-1/Factors-and-Multiples-Medium-Questions-3.html":
            params = GetParameters('FactorsMultiples',user.username)                                    
        elif htmlPage=="/Grade-7/Chapter-1/Factors-and-Multiples-Medium-Questions-4.html":
            params = GetParameters('FactorsMultiples',user.username)                                    
        elif htmlPage=="/Grade-7/Chapter-1/Factors-and-Multiples-Advanced-Questions-1.html":
            params = GetParameters('FactorsMultiples',user.username)                                    
        elif htmlPage=="/Grade-7/Chapter-1/Prime-and-Composite-Numbers-Easy-Questions-1.html":
            params = GetParameters('PrimeComposite',user.username) 
        elif htmlPage=="/Grade-7/Chapter-1/Prime-and-Composite-Numbers-Medium-Questions-1.html":
            params = GetParameters('PrimeComposite',user.username) 
        elif htmlPage=="/Grade-7/Chapter-1/Prime-and-Composite-Numbers-Advanced-Questions-1.html":
            params = GetParameters('PrimeComposite',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Prime-Factorisation-Index-Notation-Easy-Questions-1.html":
            params = GetParameters('PrimeFactorisation',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Prime-Factorisation-Index-Notation-Easy-Questions-2.html":
            params = GetParameters('PrimeFactorisation',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Prime-Factorisation-Index-Notation-Easy-Questions-3.html":
            params = GetParameters('PrimeFactorisation',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Prime-Factorisation-Index-Notation-Medium-Questions-1.html":
            params = GetParameters('PrimeFactorisation',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Prime-Factorisation-Index-Notation-Medium-Questions-2.html":
            params = GetParameters('PrimeFactorisation',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Prime-Factorisation-Index-Notation-Advanced-Questions-1.html":
            params = GetParameters('PrimeFactorisation',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Prime-Factorisation-Index-Notation-Advanced-Questions-2.html":
            params = GetParameters('PrimeFactorisation',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Highest-Common-Factor-Easy-Questions-1.html":
            params = GetParameters('HCF',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Highest-Common-Factor-Medium-Questions-1.html":
            params = GetParameters('HCF',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Highest-Common-Factor-Advanced-Questions-1.html":
            params = GetParameters('HCF',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Highest-Common-Factor-Advanced-Questions-2.html":
            params = GetParameters('HCF',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Lowest-Common-Multiple-Easy-Questions-1.html":
            params = GetParameters('LCM',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Lowest-Common-Multiple-Medium-Questions-1.html":
            params = GetParameters('LCM',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Lowest-Common-Multiple-Advanced-Questions-1.html":
            params = GetParameters('LCM',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Lowest-Common-Multiple-Advanced-Questions-2.html":
            params = GetParameters('LCM',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Squares-and-Square-Roots-Easy-Questions-1.html":
            params = GetParameters('SSR',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Squares-and-Square-Roots-Easy-Questions-2.html":
            params = GetParameters('SSR',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Squares-and-Square-Roots-Medium-Questions-1.html":
            params = GetParameters('SSR',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Squares-and-Square-Roots-Advanced-Questions-1.html":
            params = GetParameters('SSR',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Squares-and-Square-Roots-Advanced-Questions-2.html":
            params = GetParameters('SSR',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Cubes-and-Cube-Roots-Easy-Questions-1.html":
            params = GetParameters('CCR',user.username)         
        elif htmlPage=="/Grade-7/Chapter-1/Cubes-and-Cube-Roots-Easy-Questions-2.html":
            params = GetParameters('CCR',user.username) 
        elif htmlPage=="/Grade-7/Chapter-1/Cubes-and-Cube-Roots-Medium-Questions-1.html":
            params = GetParameters('CCR',user.username)
        elif htmlPage=="/Grade-7/Chapter-1/Cubes-and-Cube-Roots-Advanced-Questions-1.html":
            params = GetParameters('CCR',user.username)              
        elif htmlPage=="/Grade-7/Chapter-1/Cubes-and-Cube-Roots-Advanced-Questions-2.html":
            params = GetParameters('CCR',user.username)              
        elif htmlPage=="/Grade-7/Chapter-1/Topical-Test-1-Factors-Multiples-Roots.html":
            params = GetTestParameters('FMR_Topical_Test_1',user)
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Review-Easy-Questions-1.html":
            params = GetParameters('PercentageReview',user.username)
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Review-Easy-Questions-2.html":
            params = GetParameters('PercentageReview',user.username)
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Review-Medium-Questions-1.html":
            params = GetParameters('PercentageReview',user.username)                                     
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Review-Medium-Questions-2.html":
            params = GetParameters('PercentageReview',user.username) 
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Review-Medium-Questions-3.html":
            params = GetParameters('PercentageReview',user.username)
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Review-Advanced-Questions-1.html":
            params = GetParameters('PercentageReview',user.username)
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Review-Advanced-Questions-2.html":
            params = GetParameters('PercentageReview',user.username)
        elif htmlPage=="/Grade-7/Chapter-5/Reverse-Percentage-Easy-Questions-1.html":
            params = GetParameters('ReversePercentages',user.username)
        elif htmlPage=="/Grade-7/Chapter-5/Reverse-Percentage-Easy-Questions-2.html":
            params = GetParameters('ReversePercentages',user.username)
        elif htmlPage=="/Grade-7/Chapter-5/Reverse-Percentage-Medium-Questions-1.html":
            params = GetParameters('ReversePercentages',user.username)
        elif htmlPage=="/Grade-7/Chapter-5/Reverse-Percentage-Medium-Questions-2.html":
            params = GetParameters('ReversePercentages',user.username)
        elif htmlPage=="/Grade-7/Chapter-5/Reverse-Percentage-Advanced-Questions-1.html":
            params = GetParameters('ReversePercentages',user.username)
        elif htmlPage=="/Grade-7/Chapter-5/Reverse-Percentage-Advanced-Questions-2.html":
            params = GetParameters('ReversePercentages',user.username)
        elif htmlPage=="/Grade-7/Chapter-5/Reverse-Percentage-Advanced-Questions-3.html":
            params = GetParameters('ReversePercentages',user.username)            
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Increase-Decrease-Easy-Questions-1.html":
            params = GetParameters('PercentageIncreaseDecrease',user.username)            
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Increase-Decrease-Easy-Questions-2.html":
            params = GetParameters('PercentageIncreaseDecrease',user.username)            
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Increase-Decrease-Medium-Questions-1.html":
            params = GetParameters('PercentageIncreaseDecrease',user.username)            
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Increase-Decrease-Medium-Questions-2.html":
            params = GetParameters('PercentageIncreaseDecrease',user.username)            
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Increase-Decrease-Advanced-Questions-1.html":
            params = GetParameters('PercentageIncreaseDecrease',user.username)            
        elif htmlPage=="/Grade-7/Chapter-5/Percentage-Increase-Decrease-Advanced-Questions-2.html":
            params = GetParameters('PercentageIncreaseDecrease',user.username)
        elif htmlPage=="/Grade-7/Chapter-5/Topical-Test-1-Percentage.html":
            params = GetTestParameters('PR_Topical_Test_1',user)                      
        elif htmlPage=="/Grade-7/Chapter-6/Distance-Time-Speed-Easy-Questions-1.html":
            params = GetParameters('DistanceTimeSpeed',user.username)            
        elif htmlPage=="/Grade-7/Chapter-6/Distance-Time-Speed-Easy-Questions-2.html":
            params = GetParameters('DistanceTimeSpeed',user.username)            
        elif htmlPage=="/Grade-7/Chapter-6/Distance-Time-Speed-Medium-Questions-1.html":
            params = GetParameters('DistanceTimeSpeed',user.username)            
        elif htmlPage=="/Grade-7/Chapter-6/Distance-Time-Speed-Medium-Questions-2.html":
            params = GetParameters('DistanceTimeSpeed',user.username)            
        elif htmlPage=="/Grade-7/Chapter-6/Distance-Time-Speed-Advanced-Questions-1.html":
            params = GetParameters('DistanceTimeSpeed',user.username)            
        elif htmlPage=="/Grade-7/Chapter-6/Distance-Time-Speed-Advanced-Questions-2.html":
            params = GetParameters('DistanceTimeSpeed',user.username)            
        elif htmlPage=="/Grade-7/Chapter-6/Distance-Time-Speed-Advanced-Questions-3.html":
            params = GetParameters('DistanceTimeSpeed',user.username)            
        elif htmlPage=="/Grade-7/Chapter-6/Types-of-Speed-Easy-Questions-1.html":
            params = GetParameters('TypesOfSpeed',user.username)            
        elif htmlPage=="/Grade-7/Chapter-6/Types-of-Speed-Easy-Questions-2.html":
            params = GetParameters('TypesOfSpeed',user.username)            
        elif htmlPage=="/Grade-7/Chapter-6/Types-of-Speed-Medium-Questions-1.html":
            params = GetParameters('TypesOfSpeed',user.username) 
        elif htmlPage=="/Grade-7/Chapter-6/Types-of-Speed-Medium-Questions-2.html":
            params = GetParameters('TypesOfSpeed',user.username) 
        elif htmlPage=="/Grade-7/Chapter-6/Types-of-Speed-Advanced-Questions-1.html":
            params = GetParameters('TypesOfSpeed',user.username) 
        elif htmlPage=="/Grade-7/Chapter-6/Types-of-Speed-Advanced-Questions-2.html":
            params = GetParameters('TypesOfSpeed',user.username) 
        elif htmlPage=="/Grade-7/Chapter-6/Types-of-Speed-Advanced-Questions-3.html":
            params = GetParameters('TypesOfSpeed',user.username) 
        elif htmlPage=="/Grade-7/Chapter-6/Topical-Test-1-Speed.html":
            params = GetTestParameters('SP_Topical_Test_1',user)
        elif htmlPage=="/Grade-7/Chapter-2/Numbers-Integers-Easy-Questions-1.html":
            params = GetParameters('NumbersIntegers',user.username)                                  
        elif htmlPage=="/Grade-7/Chapter-2/Numbers-Integers-Easy-Questions-2.html":
            params = GetParameters('NumbersIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Numbers-Integers-Medium-Questions-1.html":
            params = GetParameters('NumbersIntegers',user.username)                                  
        elif htmlPage=="/Grade-7/Chapter-2/Numbers-Integers-Medium-Questions-2.html":
            params = GetParameters('NumbersIntegers',user.username)                                  
        elif htmlPage=="/Grade-7/Chapter-2/Numbers-Integers-Medium-Questions-3.html":
            params = GetParameters('NumbersIntegers',user.username)                                  
        elif htmlPage=="/Grade-7/Chapter-2/Numbers-Integers-Medium-Questions-4.html":
            params = GetParameters('NumbersIntegers',user.username)                                  
        elif htmlPage=="/Grade-7/Chapter-2/Numbers-Integers-Advanced-Questions-1.html":
            params = GetParameters('NumbersIntegers',user.username)                                  
        elif htmlPage=="/Grade-7/Chapter-2/Numbers-Integers-Advanced-Questions-2.html":
            params = GetParameters('NumbersIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Numbers-Integers-Advanced-Questions-3.html":
            params = GetParameters('NumbersIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Numbers-Integers-Advanced-Questions-4.html":
            params = GetParameters('NumbersIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Numbers-Integers-Advanced-Questions-5.html":
            params = GetParameters('NumbersIntegers',user.username)                                                                      
        elif htmlPage=="/Grade-7/Chapter-2/Addition-Subtraction-Integers-Easy-Questions-1.html":
            params = GetParameters('AdditionSubtractionIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Addition-Subtraction-Integers-Medium-Questions-1.html":
            params = GetParameters('AdditionSubtractionIntegers',user.username)                                             
        elif htmlPage=="/Grade-7/Chapter-2/Addition-Subtraction-Integers-Medium-Questions-2.html":
            params = GetParameters('AdditionSubtractionIntegers',user.username)                                             
        elif htmlPage=="/Grade-7/Chapter-2/Addition-Subtraction-Integers-Medium-Questions-3.html":
            params = GetParameters('AdditionSubtractionIntegers',user.username)                                             
        elif htmlPage=="/Grade-7/Chapter-2/Addition-Subtraction-Integers-Medium-Questions-4.html":
            params = GetParameters('AdditionSubtractionIntegers',user.username)                                             
        elif htmlPage=="/Grade-7/Chapter-2/Addition-Subtraction-Integers-Advanced-Questions-1.html":
            params = GetParameters('AdditionSubtractionIntegers',user.username)                                             
        elif htmlPage=="/Grade-7/Chapter-2/Addition-Subtraction-Integers-Advanced-Questions-2.html":
            params = GetParameters('AdditionSubtractionIntegers',user.username)                                             
        elif htmlPage=="/Grade-7/Chapter-2/Addition-Subtraction-Integers-Advanced-Questions-3.html":
            params = GetParameters('AdditionSubtractionIntegers',user.username)                                             
        elif htmlPage=="/Grade-7/Chapter-2/Addition-Subtraction-Integers-Advanced-Questions-4.html":
            params = GetParameters('AdditionSubtractionIntegers',user.username)    
        elif htmlPage=="/Grade-7/Chapter-2/Multiplication-Division-Integers-Easy-Questions-1.html":
            params = GetParameters('MultiplicationDivisionIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Multiplication-Division-Integers-Easy-Questions-2.html":
            params = GetParameters('MultiplicationDivisionIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Multiplication-Division-Integers-Medium-Questions-1.html":
            params = GetParameters('MultiplicationDivisionIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Multiplication-Division-Integers-Medium-Questions-2.html":
            params = GetParameters('MultiplicationDivisionIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Multiplication-Division-Integers-Medium-Questions-3.html":
            params = GetParameters('MultiplicationDivisionIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Multiplication-Division-Integers-Advanced-Questions-1.html":
            params = GetParameters('MultiplicationDivisionIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Multiplication-Division-Integers-Advanced-Questions-2.html":
            params = GetParameters('MultiplicationDivisionIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Multiplication-Division-Integers-Advanced-Questions-3.html":
            params = GetParameters('MultiplicationDivisionIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Multiplication-Division-Integers-Advanced-Questions-4.html":
            params = GetParameters('MultiplicationDivisionIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Multiplication-Division-Integers-Advanced-Questions-5.html":
            params = GetParameters('MultiplicationDivisionIntegers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Rational-Real-Numbers-Easy-Questions-1.html":
            params = GetParameters('RationalRealNumbers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Rational-Real-Numbers-Easy-Questions-2.html":
            params = GetParameters('RationalRealNumbers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Rational-Real-Numbers-Medium-Questions-1.html":
            params = GetParameters('RationalRealNumbers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Rational-Real-Numbers-Medium-Questions-2.html":
            params = GetParameters('RationalRealNumbers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Rational-Real-Numbers-Advanced-Questions-1.html":
            params = GetParameters('RationalRealNumbers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Rational-Real-Numbers-Advanced-Questions-2.html":
            params = GetParameters('RationalRealNumbers',user.username)
        elif htmlPage=="/Grade-7/Chapter-2/Topical-Test-1-Real-Numbers.html":
            params = GetTestParameters('RRN_Topical_Test_1',user)            
        elif htmlPage=="/Grade-7/Chapter-3/Rounding-Off-Easy-Questions-1.html":
            params = GetParameters('RoundingOff',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Rounding-Off-Easy-Questions-2.html":
            params = GetParameters('RoundingOff',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Rounding-Off-Medium-Questions-1.html":
            params = GetParameters('RoundingOff',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Rounding-Off-Medium-Questions-2.html":
            params = GetParameters('RoundingOff',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Rounding-Off-Advanced-Questions-1.html":
            params = GetParameters('RoundingOff',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Rounding-Off-Advanced-Questions-2.html":
            params = GetParameters('RoundingOff',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Rounding-Off-To-Significant-Figures-Easy-Questions-1.html":
            params = GetParameters('SignificantFigures',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Rounding-Off-To-Significant-Figures-Easy-Questions-2.html":
            params = GetParameters('SignificantFigures',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Rounding-Off-To-Significant-Figures-Medium-Questions-1.html":
            params = GetParameters('SignificantFigures',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Rounding-Off-To-Significant-Figures-Medium-Questions-2.html":
            params = GetParameters('SignificantFigures',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Rounding-Off-To-Significant-Figures-Advanced-Questions-1.html":
            params = GetParameters('SignificantFigures',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Rounding-Off-To-Significant-Figures-Advanced-Questions-2.html":
            params = GetParameters('SignificantFigures',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Estimation-Easy-Questions-1.html":
            params = GetParameters('Estimation',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Estimation-Easy-Questions-2.html":
            params = GetParameters('Estimation',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Estimation-Medium-Questions-1.html":
            params = GetParameters('Estimation',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Estimation-Medium-Questions-2.html":
            params = GetParameters('Estimation',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Estimation-Advanced-Questions-1.html":
            params = GetParameters('Estimation',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Estimation-Advanced-Questions-2.html":
            params = GetParameters('Estimation',user.username)
        elif htmlPage=="/Grade-7/Chapter-3/Topical-Test-1-Approximation-Estimation.html":
            params = GetTestParameters('AE_Topical_Test_1',user) 
        elif htmlPage=="/Grade-7/Chapter-4/Ratio-Easy-Questions-1.html":
            params = GetParameters('Ratio',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Ratio-Easy-Questions-2.html":
            params = GetParameters('Ratio',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Ratio-Easy-Questions-3.html":
            params = GetParameters('Ratio',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Ratio-Medium-Questions-1.html":
            params = GetParameters('Ratio',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Ratio-Medium-Questions-2.html":
            params = GetParameters('Ratio',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Ratio-Medium-Questions-3.html":
            params = GetParameters('Ratio',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Ratio-Advanced-Questions-1.html":
            params = GetParameters('Ratio',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Ratio-Advanced-Questions-2.html":
            params = GetParameters('Ratio',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Rate-Easy-Questions-1.html":
            params = GetParameters('Rate',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Rate-Easy-Questions-2.html":
            params = GetParameters('Rate',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Rate-Medium-Questions-1.html":
            params = GetParameters('Rate',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Rate-Medium-Questions-2.html":
            params = GetParameters('Rate',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Rate-Medium-Questions-3.html":
            params = GetParameters('Rate',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Rate-Advanced-Questions-1.html":
            params = GetParameters('Rate',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Rate-Advanced-Questions-2.html":
            params = GetParameters('Rate',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Rate-Advanced-Questions-3.html":
            params = GetParameters('Rate',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Rate-Advanced-Questions-4.html":
            params = GetParameters('Rate',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Rate-Advanced-Questions-5.html":
            params = GetParameters('Rate',user.username)
        elif htmlPage=="/Grade-7/Chapter-4/Topical-Test-1-Rate-Ratio.html":
            params = GetTestParameters('RRP_Topical_Test_1',user)
    elif book_code=="7B":
        if htmlPage=="/Grade-7/Chapter-7/Interpreting-Algebraic-Notations-Easy-Questions-1.html":
            params = GetParameters('AlgebraicNotations',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Interpreting-Algebraic-Notations-Easy-Questions-2.html":
            params = GetParameters('AlgebraicNotations',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Interpreting-Algebraic-Notations-Easy-Questions-3.html":
            params = GetParameters('AlgebraicNotations',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Interpreting-Algebraic-Notations-Easy-Questions-4.html":
            params = GetParameters('AlgebraicNotations',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Interpreting-Algebraic-Notations-Medium-Questions-1.html":
            params = GetParameters('AlgebraicNotations',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Interpreting-Algebraic-Notations-Medium-Questions-2.html":
            params = GetParameters('AlgebraicNotations',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Interpreting-Algebraic-Notations-Medium-Questions-3.html":
            params = GetParameters('AlgebraicNotations',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Interpreting-Algebraic-Notations-Medium-Questions-4.html":
            params = GetParameters('AlgebraicNotations',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Interpreting-Algebraic-Notations-Advanced-Questions-1.html":
            params = GetParameters('AlgebraicNotations',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Interpreting-Algebraic-Notations-Advanced-Questions-2.html":
            params = GetParameters('AlgebraicNotations',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Interpreting-Algebraic-Notations-Advanced-Questions-3.html":
            params = GetParameters('AlgebraicNotations',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Interpreting-Algebraic-Notations-Advanced-Questions-4.html":
            params = GetParameters('AlgebraicNotations',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Evaluating-Algebraic-Expressions-Easy-Questions-1.html":
            params = GetParameters('AlgebraicExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Evaluating-Algebraic-Expressions-Easy-Questions-2.html":
            params = GetParameters('AlgebraicExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Evaluating-Algebraic-Expressions-Medium-Questions-1.html":
            params = GetParameters('AlgebraicExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Evaluating-Algebraic-Expressions-Medium-Questions-2.html":
            params = GetParameters('AlgebraicExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Evaluating-Algebraic-Expressions-Medium-Questions-3.html":
            params = GetParameters('AlgebraicExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Evaluating-Algebraic-Expressions-Medium-Questions-4.html":
            params = GetParameters('AlgebraicExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Evaluating-Algebraic-Expressions-Advanced-Questions-1.html":
            params = GetParameters('AlgebraicExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Evaluating-Algebraic-Expressions-Advanced-Questions-2.html":
            params = GetParameters('AlgebraicExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Evaluating-Algebraic-Expressions-Advanced-Questions-3.html":
            params = GetParameters('AlgebraicExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Real-World-Algebraic-Expressions-Easy-Questions-1.html":
            params = GetParameters('RealWorldAlgebra',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Real-World-Algebraic-Expressions-Easy-Questions-2.html":
            params = GetParameters('RealWorldAlgebra',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Real-World-Algebraic-Expressions-Medium-Questions-1.html":
            params = GetParameters('RealWorldAlgebra',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Real-World-Algebraic-Expressions-Medium-Questions-2.html":
            params = GetParameters('RealWorldAlgebra',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Real-World-Algebraic-Expressions-Medium-Questions-3.html":
            params = GetParameters('RealWorldAlgebra',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Real-World-Algebraic-Expressions-Advanced-Questions-1.html":
            params = GetParameters('RealWorldAlgebra',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Real-World-Algebraic-Expressions-Advanced-Questions-2.html":
            params = GetParameters('RealWorldAlgebra',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Real-World-Algebraic-Expressions-Advanced-Questions-3.html":
            params = GetParameters('RealWorldAlgebra',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Real-World-Algebraic-Expressions-Advanced-Questions-4.html":
            params = GetParameters('RealWorldAlgebra',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Real-World-Algebraic-Expressions-Advanced-Questions-5.html":
            params = GetParameters('RealWorldAlgebra',user.username)
        elif htmlPage=="/Grade-7/Chapter-7/Topical-Test-1-Introduction-to-Algebra.html":
            params = GetTestParameters('IAG_Topical_Test_1',user)            
        elif htmlPage=="/Grade-7/Chapter-8/Addition-Subtraction-Of-Linear-Expressions-Easy-Questions-1.html":
            params = GetParameters('AdditionSubtractionLinearExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Addition-Subtraction-Of-Linear-Expressions-Easy-Questions-2.html":
            params = GetParameters('AdditionSubtractionLinearExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Addition-Subtraction-Of-Linear-Expressions-Easy-Questions-3.html":
            params = GetParameters('AdditionSubtractionLinearExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Addition-Subtraction-Of-Linear-Expressions-Easy-Questions-4.html":
            params = GetParameters('AdditionSubtractionLinearExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Addition-Subtraction-Of-Linear-Expressions-Medium-Questions-1.html":
            params = GetParameters('AdditionSubtractionLinearExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Addition-Subtraction-Of-Linear-Expressions-Medium-Questions-2.html":
            params = GetParameters('AdditionSubtractionLinearExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Addition-Subtraction-Of-Linear-Expressions-Medium-Questions-3.html":
            params = GetParameters('AdditionSubtractionLinearExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Addition-Subtraction-Of-Linear-Expressions-Advanced-Questions-1.html":
            params = GetParameters('AdditionSubtractionLinearExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Addition-Subtraction-Of-Linear-Expressions-Advanced-Questions-2.html":
            params = GetParameters('AdditionSubtractionLinearExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Addition-Subtraction-Of-Linear-Expressions-Advanced-Questions-3.html":
            params = GetParameters('AdditionSubtractionLinearExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Addition-Subtraction-Of-Linear-Expressions-Advanced-Questions-4.html":
            params = GetParameters('AdditionSubtractionLinearExpressions',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Easy-Questions-1.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Easy-Questions-2.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Easy-Questions-3.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Easy-Questions-4.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Easy-Questions-5.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Medium-Questions-1.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Medium-Questions-2.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Medium-Questions-3.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Medium-Questions-4.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Medium-Questions-5.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Medium-Questions-6.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Advanced-Questions-1.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Advanced-Questions-2.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Advanced-Questions-3.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Advanced-Questions-4.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Algebra-Factorisation-Advanced-Questions-5.html":
            params = GetParameters('AlgebraFactorisation',user.username)
        elif htmlPage=="/Grade-7/Chapter-8/Topical-Test-1-Algebraic-Manipulations.html":
            params = GetTestParameters('AGM_Topical_Test_1',user)              
        elif htmlPage=="/Grade-7/Chapter-9/Linear-Equations-in-OneV-Easy-Questions-1.html":
            params = GetParameters('LinearEquationsInOneV',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Linear-Equations-in-OneV-Easy-Questions-2.html":
            params = GetParameters('LinearEquationsInOneV',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Linear-Equations-in-OneV-Medium-Questions-1.html":
            params = GetParameters('LinearEquationsInOneV',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Linear-Equations-in-OneV-Medium-Questions-2.html":
            params = GetParameters('LinearEquationsInOneV',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Linear-Equations-in-OneV-Advanced-Questions-1.html":
            params = GetParameters('LinearEquationsInOneV',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Linear-Equations-in-OneV-Advanced-Questions-2.html":
            params = GetParameters('LinearEquationsInOneV',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Linear-Equations-in-OneV-Advanced-Questions-3.html":
            params = GetParameters('LinearEquationsInOneV',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Simple-Fractional-Equations-Easy-Questions-1.html":
            params = GetParameters('SimpleFractionalEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Simple-Fractional-Equations-Easy-Questions-2.html":
            params = GetParameters('SimpleFractionalEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Simple-Fractional-Equations-Medium-Questions-1.html":
            params = GetParameters('SimpleFractionalEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Simple-Fractional-Equations-Medium-Questions-2.html":
            params = GetParameters('SimpleFractionalEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Simple-Fractional-Equations-Advanced-Questions-1.html":
            params = GetParameters('SimpleFractionalEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Simple-Fractional-Equations-Advanced-Questions-2.html":
            params = GetParameters('SimpleFractionalEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Simple-Fractional-Equations-Advanced-Questions-3.html":
            params = GetParameters('SimpleFractionalEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Simple-Fractional-Equations-Advanced-Questions-4.html":
            params = GetParameters('SimpleFractionalEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Applications-of-Linear-Equations-Easy-Questions-1.html":
            params = GetParameters('ApplicationOfLinearEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Applications-of-Linear-Equations-Easy-Questions-2.html":
            params = GetParameters('ApplicationOfLinearEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Applications-of-Linear-Equations-Medium-Questions-1.html":
            params = GetParameters('ApplicationOfLinearEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Applications-of-Linear-Equations-Medium-Questions-2.html":
            params = GetParameters('ApplicationOfLinearEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Applications-of-Linear-Equations-Advanced-Questions-1.html":
            params = GetParameters('ApplicationOfLinearEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Applications-of-Linear-Equations-Advanced-Questions-2.html":
            params = GetParameters('ApplicationOfLinearEquations',user.username)
        elif htmlPage=="/Grade-7/Chapter-9/Topical-Test-1-Linear-Equations.html":
            params = GetTestParameters('C9LE_Topical_Test_1',user)           
        elif htmlPage=="/Grade-7/Chapter-10/Simple-Inequalities-Easy-Questions-1.html":
            params = GetParameters('SimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Simple-Inequalities-Easy-Questions-2.html":
            params = GetParameters('SimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Simple-Inequalities-Easy-Questions-3.html":
            params = GetParameters('SimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Simple-Inequalities-Easy-Questions-4.html":
            params = GetParameters('SimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Simple-Inequalities-Easy-Questions-5.html":
            params = GetParameters('SimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Simple-Inequalities-Medium-Questions-1.html":
            params = GetParameters('SimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Simple-Inequalities-Medium-Questions-2.html":
            params = GetParameters('SimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Simple-Inequalities-Advanced-Questions-1.html":
            params = GetParameters('SimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Simple-Inequalities-Advanced-Questions-2.html":
            params = GetParameters('SimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Applications-Of-Simple-Inequalities-Easy-Questions-1.html":
            params = GetParameters('AppOfSimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Applications-Of-Simple-Inequalities-Easy-Questions-2.html":
            params = GetParameters('AppOfSimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Applications-Of-Simple-Inequalities-Medium-Questions-1.html":
            params = GetParameters('AppOfSimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Applications-Of-Simple-Inequalities-Medium-Questions-2.html":
            params = GetParameters('AppOfSimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Applications-Of-Simple-Inequalities-Advanced-Questions-1.html":
            params = GetParameters('AppOfSimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Applications-Of-Simple-Inequalities-Advanced-Questions-2.html":
            params = GetParameters('AppOfSimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Applications-Of-Simple-Inequalities-Advanced-Questions-3.html":
            params = GetParameters('AppOfSimpleInequalities',user.username)
        elif htmlPage=="/Grade-7/Chapter-10/Topical-Test-1-Simple-Inequalities.html":
            params = GetTestParameters('C10SI_Topical_Test_1',user)
    elif book_code=="7C":
        if htmlPage=="/Grade-7/Chapter-11/Points-Lines-Planes-Easy-Questions-1.html":
            params = GetParameters('PointsLinesPlanes',user.username)
        elif htmlPage=="/Grade-7/Chapter-11/Points-Lines-Planes-Easy-Questions-2.html":
            params = GetParameters('PointsLinesPlanes',user.username)
            
            
    return params

def GetParameters(QuestionType,username):
    params = {}
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+username+"' and question_type = '"+QuestionType+"'").fetch(100)
    for q in Grade7QuestionData:
        params.update({q.answer_id:q.entered_answer})
        if q.correct is not None:
            params.update({q.answer_id+"_correct":q.correct,
                           q.answer_id+"_explain":Grade7Questions.AllQuestions[q.answer_id]["Explanation"]})
    return params

def GetTestParameters(TestTopic,user):
    usernames = []
    test_data = []
    showTryAgainButton = 'Y'
    if user.IsParent:      
        ChildUserData = HomeCampusUser.gql("where email = '"+user.email+"' and IsParent = False").fetch(5)
        for c in ChildUserData:
            usernames.append([c.username,c.first_name,c.last_name])
    else:
        usernames.append([user.username,user.first_name,user.last_name])
            
    for username in usernames:
        Grade7TestData = HCGrade7TestMaster.HCGrade7TestMaster.gql("where student_id = '"+username[0]+"' and test_topic = '"+TestTopic+"' order by attempt asc").fetch(5)
        for t in Grade7TestData:
            if t.end_date is not None:
                end_date = t.end_date.strftime("%d %B %Y")
            else:
                end_date = " - "
            if t.test_score is not None:
                test_score = str(t.test_score) + "/" + str(t.total_marks)
            else:
                test_score = " - "
            if t.test_status == "In Progress":
                showTryAgainButton = 'N'
            test_data.append({'student_id':username[0],'student_name':username[1],'test_id':t.test_id,'attempt':t.attempt,'start_date':t.start_date.strftime("%d %B %Y"),'end_date':end_date,
                              'status':t.test_status,'score':test_score,'time_taken':CreateTimeString(t.elapsed_time),'status':t.test_status})
    
    '''Only 5 attempts are allowed for each test and these are used for child login only'''
    attempt = len(test_data)
    if attempt >=5:
        showTryAgainButton = 'N'  
    params = {'childData':usernames,'test_data':test_data,'showTryAgainButton':showTryAgainButton,'test_attempt':attempt+1}
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