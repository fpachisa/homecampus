'''
Created on Oct 10, 2012

@author: Farhat
'''
from tipfy import RequestHandler
from tipfy import Rule
from Config import config
import Config
from tipfy import Tipfy
from tipfy.auth import login_required,UserRequiredIfAuthenticatedMiddleware,user_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from HCGoals import HCGoals
import simplejson as json
import logging
from Database import HCSubscription



rules = [
         Rule('/Goals', endpoint='', handler='GenerateGoals.Goals'),
         Rule('/Goals/Save_Goals', endpoint='', handler='GenerateGoals.SaveGoals'),
         Rule('/Goals/Grade_4_Decimal_Goals', endpoint='', handler='GenerateGoals.P4DCGoals'),         
         Rule('/Goals/Grade_4_Fractions_Goals', endpoint='', handler='GenerateGoals.P4FRGoals'),
         Rule('/Goals/Grade_4_Measurement_Goals', endpoint='', handler='GenerateGoals.P4MTGoals'),
         Rule('/Goals/Grade_4_Data_Analysis_Goals', endpoint='', handler='GenerateGoals.P4DAGoals'),
         Rule('/Goals/Grade_4_Whole_Numbers_Goals', endpoint='', handler='GenerateGoals.P4WNGoals'),
         Rule('/Goals/Grade_5_Data_Analysis_Goals', endpoint='', handler='GenerateGoals.P5DAGoals'),
         Rule('/Goals/Grade_5_Decimal_Goals', endpoint='', handler='GenerateGoals.P5DCGoals'),         
         Rule('/Goals/Grade_5_Fractions_Goals', endpoint='', handler='GenerateGoals.P5FRGoals'),
         Rule('/Goals/Grade_5_Geometry_Goals', endpoint='', handler='GenerateGoals.P5GTGoals'),
         Rule('/Goals/Grade_5_Measurement_Goals', endpoint='', handler='GenerateGoals.P5MTGoals'),
         Rule('/Goals/Grade_5_Percentage_Goals', endpoint='', handler='GenerateGoals.P5PRGoals'),
         Rule('/Goals/Grade_5_Ratio_Goals', endpoint='', handler='GenerateGoals.P5RTGoals'),
         Rule('/Goals/Grade_5_Whole_Numbers_Goals', endpoint='', handler='GenerateGoals.P5WNGoals'),
         Rule('/Goals/Grade_6_Algebra_Goals', endpoint='', handler='GenerateGoals.P6AGGoals'),
         Rule('/Goals/Grade_6_Data_Analysis_Goals', endpoint='', handler='GenerateGoals.P6DAGoals'),        
         Rule('/Goals/Grade_6_Fractions_Goals', endpoint='', handler='GenerateGoals.P6FRGoals'),
         Rule('/Goals/Grade_6_Measurement_Goals', endpoint='', handler='GenerateGoals.P6MTGoals'),
         Rule('/Goals/Grade_6_Percentage_Goals', endpoint='', handler='GenerateGoals.P6PRGoals'),
         Rule('/Goals/Grade_6_Ratio_Goals', endpoint='', handler='GenerateGoals.P6RTGoals'),
         Rule('/Goals/Grade_6_Speed_Goals', endpoint='', handler='GenerateGoals.P6SPGoals'),
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
            'TRIAL':TRIAL
        })

        return super(BaseHandler, self).render_response(filename, **kwargs)

class Goals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoalPage(self.auth.user)
        return self.render_response('Goals/Goals.html', **Config.goal_values)

class SaveGoals(BaseHandler):   
    @login_required   
    def post(self, **kwargs):
        DataArray = json.loads(self.request.form.get('DataArray'))
        StudentId = self.request.form.get('username')
        grade = self.request.form.get('grade')
        topic = self.request.form.get('topic')
        Config.goal_values = HCGoals.GenerateGoals().SaveGoals(self.auth.user,StudentId,grade,topic,DataArray)
        return self.render_response('Goals/Goals.html', **Config.goal_values)

class P4DCGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(4,'P4DC',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_4_Decimal_Goals.html', **Config.goal_values)

class P4FRGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(4,'P4FR',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_4_Fractions_Goals.html', **Config.goal_values)

class P4MTGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(4,'P4MT',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_4_Measurement_Goals.html', **Config.goal_values)

class P4DAGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(4,'P4DA',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_4_Data_Analysis_Goals.html', **Config.goal_values)

class P4WNGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(4,'P4WN',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_4_Whole_Numbers_Goals.html', **Config.goal_values)

class P5DAGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(5,'P5DA',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_5_Data_Analysis_Goals.html', **Config.goal_values)

class P5DCGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(5,'P5DC',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_5_Decimal_Goals.html', **Config.goal_values)

class P5FRGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(5,'P5FR',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_5_Fractions_Goals.html', **Config.goal_values)

class P5GTGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(5,'P5GT',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_5_Geometry_Goals.html', **Config.goal_values)

class P5MTGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(5,'P5MT',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_5_Measurement_Goals.html', **Config.goal_values)

class P5PRGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(5,'P5PR',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_5_Percentage_Goals.html', **Config.goal_values)

class P5RTGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(5,'P5RT',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_5_Ratio_Goals.html', **Config.goal_values)

class P5WNGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(5,'P5WN',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_5_Whole_Numbers_Goals.html', **Config.goal_values)

class P6AGGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(6,'P6AG',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_6_Algebra_Goals.html', **Config.goal_values)

class P6DAGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(6,'P6DA',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_6_Data_Analysis_Goals.html', **Config.goal_values)

class P6FRGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(6,'P6FR',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_6_Fractions_Goals.html', **Config.goal_values)

class P6MTGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(6,'P6MT',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_6_Measurement_Goals.html', **Config.goal_values)

class P6PRGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(6,'P6PR',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_6_Percentage_Goals.html', **Config.goal_values)

class P6RTGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(6,'P6RT',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_6_Ratio_Goals.html', **Config.goal_values)

class P6SPGoals(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        StudentId = self.request.args.get('username')
        Config.goal_values = HCGoals.GenerateGoals().GenerateGoals(6,'P6SP',StudentId,self.auth.user)
        return self.render_response('Goals/Grade_6_Speed_Goals.html', **Config.goal_values)


app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()

        