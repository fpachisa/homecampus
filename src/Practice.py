from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import login_required,UserRequiredIfAuthenticatedMiddleware,user_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from Database import HCSubscription, TestsMaster

rules = [Rule('/Practice', endpoint='PracticePage.html', handler='Practice.PracticePage'),
         Rule('/Practice/Primary_5_Mathematics', endpoint='', handler='Practice.Practice5'),
         Rule('/Practice/Primary_6_Mathematics', endpoint='', handler='Practice.Practice6'),
         Rule('/Practice/Primary_4_Mathematics', endpoint='', handler='Practice.Practice4'),
         Rule('/Practice/Primary_Grade_3_Mathematics', endpoint='', handler='Practice.Practice3'),
         Rule('/Practice/Primary_Grade_1_RAYAN_Mathematics', endpoint='', handler='Practice.Practice1'),
         Rule('/auth/login', endpoint='', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.SignupHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),]

class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]
    
    def messages(self):
        """A list of status messages to be displayed to the user."""
        return self.session.get_flashes(key='_messages')

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
            'UnfinishedWorksheetsCount':UnfinishedWorksheetsCount
        })

        return super(BaseHandler, self).render_response(filename, **kwargs)
      
class PracticePage(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('PracticePage.html', section='content')

class Practice5(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('Practice_Primary_5.html', section='content')

class Practice6(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('Practice_Primary_6.html', section='content')

class Practice4(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('Practice_Primary_4.html', section='content')

class Practice3(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('Practice_Primary_Grade_3.html', section='content')

class Practice1(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('Practice_Primary_1.html', section='content')
        
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()