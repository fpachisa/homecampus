from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware,admin_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from google.appengine.api import mail
import logging
from Database import HCSubscription
from Models import HomeCampusUser

rules = [Rule('/NewsLetter/April2012', endpoint='', handler='NewsLetter.April2012'),
         Rule('/NewsLetter/May2012', endpoint='', handler='NewsLetter.May2012'),
         Rule('/NewsLetter/June2012', endpoint='', handler='NewsLetter.June2012'),
         Rule('/NewsLetter/July2012', endpoint='', handler='NewsLetter.July2012'),
         Rule('/NewsLetter/August2012', endpoint='', handler='NewsLetter.August2012'),
         Rule('/NewsLetter/October2012', endpoint='', handler='NewsLetter.October2012'),
         Rule('/NewsLetter/November2012', endpoint='', handler='NewsLetter.November2012'),
         Rule('/NewsLetter/December2012', endpoint='', handler='NewsLetter.December2012'),
         Rule('/NewsLetter/January2013', endpoint='', handler='NewsLetter.January2013'),
         Rule('/NewsLetter/February2013', endpoint='', handler='NewsLetter.February2013'),
         Rule('/NewsLetter/March2013', endpoint='', handler='NewsLetter.March2013'),
         Rule('/NewsLetter', endpoint='', handler='NewsLetter.March2013'),
         Rule('/NewsLetter/HC/SendBulkNewsLetter', endpoint='', handler='NewsLetter.MailNewsLetter'),
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
        
        TRIAL = "N"
        if self.auth.user:
            HCUser = HCSubscription.HCSubscription.gql("where email = '"+self.auth.user.email+"' and status='ACTIVE'").fetch(1)
            for h in HCUser:
                if h.paypal_token in ["TRIAL","WAIVED"]:
                    TRIAL = "Y"
        
        kwargs.update({'auth_session': auth_session,
                       'current_user': self.auth.user,
                       'login_url':    self.auth.login_url(),
                       'logout_url':   self.auth.logout_url(),
                       'current_url':  self.request.url,
                       'register_url': self.auth.signup_url(),
                       'TRIAL':TRIAL
        })
        return super(BaseHandler, self).render_response(filename, **kwargs)

class April2012(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('NewsLetter/April2012.html', section='content')

class May2012(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('NewsLetter/May2012.html', section='content')

class June2012(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('NewsLetter/June2012.html', section='content')

class July2012(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('NewsLetter/July2012.html', section='content')

class August2012(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('NewsLetter/August2012.html', section='content')

class October2012(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('NewsLetter/October2012.html', section='content')

class November2012(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('NewsLetter/November2012.html', section='content')

class December2012(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('NewsLetter/December2012.html', section='content')

class January2013(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('NewsLetter/January2013.html', section='content')

class February2013(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('NewsLetter/February2013.html', section='content')

class March2013(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('NewsLetter/March2013.html', section='content')

class MailNewsLetter(BaseHandler):
    @admin_required
    def get(self, **kwargs):           
        return self.render_response('Send_News_Letter.html', **kwargs)

    def post(self,**kwargs):
        date1 = self.request.form.get('date1')
        date2 = self.request.form.get('date2')
        UserQuery = HomeCampusUser.gql("where created >= Date('"+date1+"') and created < Date('"+date2+"') and IsParent = True")
        UserData = UserQuery.fetch(10000)
        i = 0
        for user in UserData:
            first_name = user.first_name.capitalize()
            last_name = user.last_name.capitalize()
            email = user.email
            MailBulkNewsLetter(first_name,last_name,email)
            i+=1
        logging.info("Total emails send : "+str(i))
        return self.redirect("/NewsLetter/HC/SendBulkNewsLetter")
        
def MailBulkNewsLetter(first_name,last_name,email):        

    message = mail.EmailMessage()
    message.to = email
    message.sender = "Home Campus <admin@homecampus.com.sg>"
    message.subject = "Learn Maths Online - March Newsletter"
    
    
    SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
    SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(http://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="http://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">Dear '
    SendMessage = SendMessage + first_name + " "+ last_name+",<br><br>"
    #March 2013
    SendMessage = SendMessage + '</p></td></tr><tr><td valign="top" style="text-align:left; padding-left: 0px; padding-right: 0px;padding-bottom:0px;" ><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="http://my.homecampus.com.sg/Practice/Primary_Grade_3_Mathematics" title="Practice Grade 3 Maths" alt="We are excited to inform you that we have started adding content for Grade 3. We welcome all our third graders to come practice and sent their comments." style="text-decoration: none;"><img src="http://my.homecampus.com.sg/images/NewsLetter/HomeCampus_Newsletter_March_2013_1.png" alt="We are excited to inform you that we have started adding content for Grade 3. We welcome all our third graders to come practice and sent their comments." title="Practice Grade 3 Maths"/></a><br /><br /><a href="http://www.homecampus.com.sg" title="Practice Grade 3 Maths" alt="Practice Grade 3 Maths"><font color="#F7941C">Go Practice!!</font></a></p></td></tr></tbody></table><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left; padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">Have a marvellous March!!<br /></p><p style="text-align:left; font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><br />Yours sincerely,<br />Team @ Home Campus<br /><strong><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></strong><br /><b><a href="http://my.homecampus.com.sg"><font color="#006666">www.homecampus.com.sg</font></a></b></p></td></tr></tbody></table></td></tr><tr><td height="10"></td></tr><tr><td><table width="560" cellpadding="0" cellspacing="0" border="0" style="padding: 0px; font-size: 10px; line-height: 1.5em; font-family:Verdana; color: #999;"><tbody><tr><td colspan="4" height="10" bgcolor="#f7f7f2" style="text-align:left; padding-right: 10px; padding-left: 10px; padding-bottom: 1px; padding-top: 1px;"><font color="#999999">For FAQs about Home Campus, please visit  <a href="http://my.homecampus.com.sg/FAQs" title="Home Campus FAQs" target="_new">my.homecampus.com.sg/FAQs</a>. </font></td></tr><tr><td colspan="4" height="10" bgcolor="#f7f7f2" style="text-align:left; padding-right: 10px; padding-left: 10px; padding-bottom: 1px; padding-top: 1px;"><font color="#999999">Follow us on Facebook and YouTube at <a href="http://www.facebook.com/HomeCampus" title="like Home Campus on Facebook" target="_new">www.facebook.com/HomeCampus</a> and <a href="http://www.youtube.com/HomeCampus" title="Home Campus @ YouTube" target="_new">www.youtube.com/HomeCampus</a>.</font></td></tr></tbody></table></td></tr></tbody></table></div></td></tr></tbody></table>'    
    message.html = SendMessage
    
    message.Send()
    logging.info("Message send to "+first_name+" "+last_name)
    
                
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()