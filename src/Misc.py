from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
import datetime
from Database import SubmitProblemsTable
import logging
from tipfy import Response
from Models import HomeCampusUser
from google.appengine.api import mail

rules = [Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.SignupHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/MISC/Delete_DUMMY_Questions', endpoint='', handler='Misc.DeleteDummyQuestions'),
         Rule('/MISC/Generate_Register_Report', endpoint='', handler='Misc.GenerateRegisterReport'),
         Rule('/Explanation-Test', endpoint='', handler='Misc.ExplanationTest'),]
    
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
                       'register_url': self.auth.signup_url(),
        })
        return super(BaseHandler, self).render_response(filename, **kwargs)
      
class DeleteDummyQuestions(BaseHandler):  
    def get(self, **kwargs):
        
        submit_date = datetime.datetime.now() - datetime.timedelta(hours=2)
        DateString = str(submit_date.year)+"-"+str(submit_date.month)+"-"+str(submit_date.day)+" "+str(submit_date.hour)+":"+str(submit_date.minute)+":"+str(submit_date.second)
        HCProblemsQuery = SubmitProblemsTable.ProblemsTable.gql("where concept = 'DUMMY' and submit_date < DATETIME('"+DateString+"')")
        HCProblemsData = HCProblemsQuery.fetch(1000)
        i = 0
        for h in HCProblemsData:
            h.delete()
            i = i + 1
        logging.info("Total dummy problems deleted = "+str(i))
        response = Response("")
        response.status_code = 200
        return response
        
class GenerateRegisterReport(BaseHandler):  
    def get(self, **kwargs):
        
        generate_date = datetime.datetime.now() - datetime.timedelta(hours=24)
        DateString = str(generate_date.year)+"-"+str(generate_date.month)+"-"+str(generate_date.day)+" "+str(generate_date.hour)+":"+str(generate_date.minute)+":"+str(generate_date.second)
        HCUserQuery = HomeCampusUser.gql("where created > DATETIME('"+DateString+"')")
        HCUserData = HCUserQuery.fetch(10000)
        FBCount = 0
        GPlusCount = 0
        HCCount = 0
        UserData = []
        for h in HCUserData:
            if h.IsParent == True:
                if h.auth_id[:2]=="FB":
                    FBCount = FBCount + 1
                elif h.auth_id[:2]=="G+":
                    GPlusCount = GPlusCount + 1
                else:
                    HCCount = HCCount + 1
                UserData.append([h.first_name,h.last_name,h.email])
                
        message = mail.EmailMessage()
        message.to = "admin@homecampus.com.sg"
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Parent Registration Count for Today"
        SendMessage = 'Total user registered for today: '+str(FBCount+GPlusCount+HCCount)
        SendMessage = SendMessage + '<br><br>Facebook Users: '+str(FBCount)
        SendMessage = SendMessage + '<br><br>Google Users: '+str(GPlusCount)
        SendMessage = SendMessage + '<br><br>Homecampus Users: '+str(HCCount)
        
        Count = 1
        for i in range(len(UserData)):
            SendMessage = SendMessage + '<br><br>'+str(Count)+'. '+UserData[i][0]+' '+UserData[i][1]+': '+UserData[i][2]
            Count = Count + 1
        message.html = SendMessage
        '''preventing homecampu-dev1 to send mails'''
        if str(self.request.url)=="http://my.homecampus.com.sg/MISC/Generate_Register_Report" or str(self.request.url)=="http://homecampus-hrd.appspot.com/MISC/Generate_Register_Report":
            message.Send()
        
        response = Response("")
        response.status_code = 200
        return response

class ExplanationTest(BaseHandler):  
    def get(self, **kwargs):
        
        return self.render_response('Explanation-Test.html', section='content')
        

   
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()