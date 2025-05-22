from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware,admin_required,login_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from google.appengine.api import mail
from Models import HomeCampusUser
from Database import HCSubscription
import datetime
import logging

rules = [Rule('/Waiver/Form', endpoint='', handler='Waiver.Waiver'),
         Rule('/Waiver/Account', endpoint='', handler='Waiver.WaivedAccount'),
         Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),]

    
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
      
class Waiver(BaseHandler):  
    @login_required
    def get(self, **kwargs):
        UserData = HomeCampusUser.gql("where username = '"+str(self.auth.user)+"'").fetch(1)
        for u in UserData:
            email = u.email
            first_name = u.first_name
        kwargs.update({'email':email,'first_name':first_name})
                    
        return self.render_response('WaiverForm.html', **kwargs)
    
    def post(self, **kwargs):
        name = self.request.form.get('name')
        email = self.request.form.get('email')
        country = self.request.form.get('country')
        reason = self.request.form.get('reason')

        if name =="" or email =="" or country =="" or reason =="":
            kwargs.update({'title':"Error",'review':"Please enter all information.",
                           'name':name,'email':email,'country':country,'reason':reason})
            return self.get(**kwargs)
        
        message = mail.EmailMessage()
        message.to = "admin@homecampus.com.sg"
        message.sender = "admin@homecampus.com.sg"
        message.subject = "Waiver Form "+name
        message.body = "Email: "+ email+" | Country: "+country+" | "+reason
        message.Send()
        kwargs.update({'title':"Thank You",'review':"Thanks for your interest. We will review your waiver request. If approved you will be notified via email."})

        return self.get(**kwargs)

       
class WaivedAccount(BaseHandler):
   
    @admin_required
    def get(self, **kwargs):           
        return self.render_response('WaivedAccount.html', **kwargs)
    
    @admin_required
    def post(self, **kwargs):
        email = self.request.form.get('email')
        period = self.request.form.get('period')
        self.AuthorizeUser(email, period)

        return self.get(**kwargs)
          
    def AuthorizeUser(self, email, period):

        UserDataQuery = HomeCampusUser.gql("where email = '"+email+"'")
        UserData = UserDataQuery.fetch(100)
        child_first_name = []
        child_last_name = []
        username = []
        
        for d in UserData:
            d.authorized = True
            if d.IsParent:
                first_name = d.first_name
                last_name = d.last_name
            else:
                child_first_name.append(d.first_name)
                child_last_name.append(d.last_name)
                username.append(d.username)
            d.put()
        logging.info(username)
        if len(username)!=0:
            self.CreateHCSubscription(period, username, email)
            #self.sendMail(email, first_name,last_name,child_first_name,child_last_name,username,period)
            
        
    def CreateHCSubscription(self, period, username,email):
        start_date = datetime.datetime.now()
        for i in range(len(username)):
            end_date = start_date + datetime.timedelta(days = int(period))
            ExistingUserQuery = HCSubscription.HCSubscription.gql("where student_id = '"+username[i]+"' and status = 'ACTIVE'")
            ExistingUserData = ExistingUserQuery.fetch(1)
            
            for e in ExistingUserData:
                if e.status == "ACTIVE":
                    e.status = "EXPIRED"
                    end_date = end_date + (e.end_date - datetime.datetime.now())
                    e.end_date = datetime.datetime.now()
                    e.put()
                    
            PT = HCSubscription.HCSubscription(paypal_token='WAIVED',
                                              student_id=username[i],
                                              amount='0',
                                              period=int(2),
                                              start_date=start_date,
                                              end_date=end_date,
                                              status="ACTIVE",
                                              email=email)
            PT.put()
        
    def sendMail(self, email, first_name, last_name, child_first_name, child_last_name, username, period):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Welcome to Home Campus!! (Subscription waived)"
        SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
        SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(http://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="http://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">'
        SendMessage = SendMessage + 'Dear '+first_name+' '+last_name+','
        SendMessage = SendMessage + '<br /><br />Congratulations on your new registration to Home Campus!<br /><br />To help your child excel in math, your Home Campus subscription has been waived for '+str(period)+' days. So, <a href="http://my.homecampus.com.sg/SignIn"><font color="#0E820E">log in</font></a> and start using.<br /><br /><b><u>Registration details</u>:</b><br />'
        SendMessage = SendMessage + 'Parent username: '+email+'<br />'
        for i in range(len(child_first_name)):
            SendMessage = SendMessage + 'Child username: '+username[i]+'<br />'
        SendMessage = SendMessage + '<br />To start off, here\'s what you might like to check out:<br /></p><ul><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="http://my.homecampus.com.sg/Learn"><font color="#D92118"><b>Watch and Learn</b></font></a><br />Watch video lessons or read notes that are broken into bite-sized pieces</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="http://my.homecampus.com.sg/Practice"><font color="#2A91E1"><b>Unlimited Practice</b></font></a><br />Solve from a pool of unlimited questions with detailed step-by-step solutions</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="http://my.homecampus.com.sg/Tests"><font color="#0E820E"><b>Create your Tests</b></font></a><br />Create and take your own tests to check your knowledge</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="http://my.homecampus.com.sg/Progress"><font color="#F6B937"><b>Monitor Progress</b></font></a><br />Identify areas of strengths and weaknesses through graphs, charts and reports</p></li></ul><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">This and much more await you. The best part is you get to decide to pay what you feel your education is worth.<br /><br />So, go ahead, explore and top math!!<br /><br /><p style="text-align:left; font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">Yours sincerely,<br />Team @ Home Campus<br /><strong><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></strong><br /><b><a href="http://my.homecampus.com.sg"><font color="#006666">www.homecampus.com.sg</font></a></b></p></td></tr></table></td></tr></tbody></table></div></td></tr></tbody></table>'
        message.html = SendMessage
        message.Send()        

       
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()