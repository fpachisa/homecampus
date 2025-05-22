'''
Created on May 18, 2012

@author: Farhat
'''
from tipfy import RequestHandler
from tipfy import Rule
from Config import config
import Config
from tipfy import Tipfy
from tipfy.auth import login_required,UserRequiredIfAuthenticatedMiddleware
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from HCTests import HCTests
from google.appengine.api import memcache
import logging
from Reports import Reports
from Database import HCSubscription, TestsMaster

rules = [
         Rule('/Tests', endpoint='', handler='GenerateTests.Tests'),
         Rule('/Tests/GenerateTests', endpoint='', handler='GenerateTests.GenerateTests'),
         Rule('/Tests/GetTest', endpoint='', handler='GenerateTests.GetTest'),
         Rule('/Tests/GetProblems', endpoint='', handler='GenerateTests.GetTestProblems'),
         Rule('/Tests/GetClickedProblem', endpoint='', handler='GenerateTests.GetClickedProblem'),
         Rule('/Tests/GenerateTestReport', endpoint='', handler='GenerateTests.GenerateTestReport'),
         Rule('/auth/login', endpoint='', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.SignupHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler')         
         ]
      
class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]

    def render_response(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session
        
        memcache.Client().delete(unicode(self.auth.user.username)+"_test_values")
        memcache.Client().add(unicode(self.auth.user.username)+"_test_values",Config.test_values,3600)        
        
        try:
            counter = Config.test_values['counter']
        except KeyError:
            counter = -1
        
        TRIAL = "N"
        if self.auth.user:
            HCUser = HCSubscription.HCSubscription.gql("where email = '"+self.auth.user.email+"' and status='ACTIVE'").fetch(1)
            for h in HCUser:
                if h.paypal_token in ["TRIAL","WAIVED"]:
                    TRIAL = "Y"
        
        UnfinishedWorksheetsCount = 0    
        if self.auth.user and not self.auth.user.IsParent and not self.auth.user.IsTeacher:
            UnfinishedWorksheetData = TestsMaster.TestsMasterTable.gql("where student_id = '"+self.auth.user.username+"'").fetch(1000)
            for u in UnfinishedWorksheetData:
                if u.status!='Completed':
                    UnfinishedWorksheetsCount = UnfinishedWorksheetsCount + 1

        kwargs.update({
            'auth_session': auth_session,
            'current_user': self.auth.user,
            'login_url':    self.auth.login_url(),
            'logout_url':   self.auth.logout_url(),
            'current_url':  self.request.url,
            'counter': counter,
            'TRIAL':TRIAL,
            'UnfinishedWorksheetsCount':UnfinishedWorksheetsCount
        })

        return super(BaseHandler, self).render_response(filename, **kwargs)

class BaseTemplate(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]
    
    def render_template(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session
            
        memcache.Client().delete(unicode(self.auth.user.username)+"_test_values")
        memcache.Client().add(unicode(self.auth.user.username)+"_test_values",Config.test_values,3600)        
        
        try:
            counter = Config.test_values['counter']
        except KeyError:
            counter = -1
        kwargs.update({
            'auth_session': auth_session,
            'current_user': self.auth.user,
            'login_url':    self.auth.login_url(),
            'logout_url':   self.auth.logout_url(),
            'current_url':  self.request.url,
            'counter': counter
        })

        return super(BaseTemplate, self).render_template(filename, **kwargs)

class Tests(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCTests.GenerateTests().GenerateTestPage(self.auth.user)
        return self.render_response('Tests/Tests.html', **Config.test_values)

class GenerateTests(BaseHandler):     
    @login_required 
    def post(self, **kwargs):
        test_name = self.request.form.get('test_name')
        create_user = self.auth.user
        username = self.request.form.get('username')
        grade = self.request.form.get('grade')
        concept = self.request.form.get('concept')
        TestMaster = {"test_name":test_name,"create_user":create_user,"username":username,"grade":grade,"concept":concept}
        if test_name == "":
            Config.test_values = HCTests.GenerateTests().GenerateTestPage(self.auth.user)
        else:
            Config.test_values = HCTests.GenerateTests().GenerateTest(TestMaster)
        return self.render_response('Tests/Tests.html', **Config.test_values)

class GetTest(BaseHandler):     
    @login_required 
    def post(self, **kwargs):
        TestId = unicode(self.request.form.get('TestId'))
        logging.info("test_id = "+TestId)
        '''Getting the first problem with counter = 1'''
        counter = 1
        Config.test_values = HCTests.GenerateTests().GetTestData(TestId,counter,self.auth.user)
        template_name = Config.test_values["template"]
        
        '''for some unknown reason template_name comes as none the first time so getting the data again'''
        while template_name is None or template_name == "":
            Config.test_values = HCTests.GenerateTests().GetTestData(TestId,counter,self.auth.user)
            template_name = Config.test_values["template"]
        
        Config.test_values['from_test'] = "Y"
        return self.render_response(template_name, **Config.test_values)
    
class GetTestProblems(BaseHandler):     
    @login_required 
    def post(self, **kwargs):
        TestId = unicode(self.request.form.get('TestId'))
        counter = int(self.request.form.get('counter'))
        answer_submitted = str(self.request.form.get('answer_submitted'))
        next = str(self.request.form.get('next'))
        logging.info("answer = "+answer_submitted)
        '''answer = None is when no answer is selected in multiple choice'''
        if answer_submitted!="None":
            HCTests.SubmitAnswer(TestId, counter, answer_submitted)
        if next=="Y":
            counter = counter + 1
        elif next=="N":
            counter = counter - 1
        Config.test_values = HCTests.GenerateTests().GetTestData(TestId,counter,self.auth.user)
        template_name = Config.test_values["template"]   
        
        '''for some unknown reason template_name comes as none the first time so getting the data again'''
        while template_name is None or template_name == "":
            Config.test_values = HCTests.GenerateTests().GetTestData(TestId,counter,self.auth.user)
            template_name = Config.test_values["template"]
            
        Config.test_values['from_test'] = "Y"
        return self.render_response(template_name, **Config.test_values)
    
class GetClickedProblem(BaseHandler):     
    @login_required 
    def post(self, **kwargs):
        TestId = unicode(self.request.form.get('TestId'))
        current_counter = int(self.request.form.get('current_counter'))
        clicked_counter = int(self.request.form.get('clicked_counter'))
        answer_submitted = str(self.request.form.get('answer_submitted'))
        '''answer = None is when no answer is selected in multiple choice'''
        if answer_submitted!="None":
            HCTests.SubmitAnswer(TestId, current_counter, answer_submitted)

        Config.test_values = HCTests.GenerateTests().GetTestData(TestId,clicked_counter,self.auth.user)
        template_name = Config.test_values["template"]        
        
        '''for some unknown reason template_name comes as none the first time so getting the data again'''
        while template_name is None or template_name == "":
            Config.test_values = HCTests.GenerateTests().GetTestData(TestId,clicked_counter,self.auth.user)
            template_name = Config.test_values["template"]
            
        Config.test_values['from_test'] = "Y"
        return self.render_response(template_name, **Config.test_values)
    
class GenerateTestReport(BaseHandler):
    @login_required 
    def post(self,**kwargs):
        TestId = unicode(self.request.form.get('TestId'))
        if TestId == "None":
            logging.info("trying to get TestId from memcache")
            TestId = memcache.Client().get(unicode(self.auth.user.username)+'_test_values')['test_id']
        try:
            counter = int(self.request.form.get('counter'))
        except:
            counter =  -1
        answer_submitted = str(self.request.form.get('answer_submitted'))
        logging.info(TestId)
        if counter != -1 and answer_submitted!="None":
            '''This is to check the last question submitted.'''
            HCTests.SubmitAnswer(TestId, counter, answer_submitted)
        Config.test_values = Reports.GenerateReports().GenerateTestReport(self.auth.user,TestId)
        return self.render_response('Reports/Test_Report.html', **Config.test_values)    

app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()

        