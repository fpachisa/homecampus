from werkzeug.utils import cached_property
from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from tipfyext.wtforms import Form, fields
from google.appengine.api import mail
from Database import HCSubscription,HCPayment,HCBooks, TestsMaster
from Models import HomeCampusUser
from random import randint
import string
import logging
import SchoolCodes
import datetime
from tipfy import Response
from tipfy.json import json_encode

rules = [Rule('/Contact', endpoint='', handler='Contact.Contact'),
         Rule('/Refer', endpoint='', handler='Contact.Refer'),
         Rule('/FAQs', endpoint='', handler='Contact.FAQ'),
         Rule('/AboutHomeCampus', endpoint='', handler='Contact.AboutHomeCampus'),
         Rule('/PrivacyPolicy', endpoint='', handler='Contact.PrivacyPolicy'),
         Rule('/Disclaimer', endpoint='', handler='Contact.Disclaimer'),
         Rule('/MyProfile', endpoint='', handler='Contact.MyProfile'),
         Rule('/MyProfile/LoginAsChild', endpoint='', handler='Contact.LoginAsChild'),
         Rule('/Benefits', endpoint='', handler='Contact.Benefits'),
         Rule('/What_is_Singapore_Math', endpoint='', handler='Contact.SGMath'),
         Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),]
    
class ReferralForm(Form):
    YourName = fields.TextField('Your Name')
    FriendsName = fields.TextField("Your Friend's Name")
    email = fields.TextField("Your Friend's Email")  
    
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
        
        UnfinishedWorksheetsCount = 0    
        if self.auth.user and not self.auth.user.IsParent and not self.auth.user.IsTeacher:
            UnfinishedWorksheetData = TestsMaster.TestsMasterTable.gql("where student_id = '"+self.auth.user.username+"'").fetch(1000)
            for u in UnfinishedWorksheetData:
                if u.status!='Completed':
                    UnfinishedWorksheetsCount = UnfinishedWorksheetsCount + 1
       
        kwargs.update({'auth_session': auth_session,
                       'current_user': self.auth.user,
                       'login_url':    self.auth.login_url(),
                       'logout_url':   self.auth.logout_url(),
                       'current_url':  self.request.url,
                       'register_url': self.auth.signup_url(),
                       'TRIAL':TRIAL,
                       'UnfinishedWorksheetsCount':UnfinishedWorksheetsCount
        })
        return super(BaseHandler, self).render_response(filename, **kwargs)
      
class Contact(BaseHandler):  
    def get(self, **kwargs):            
        return self.render_response('Contact.html', **kwargs)
    
    def post(self, **kwargs):
        name = self.request.form.get('first_name')
        comment = self.request.form.get('comment')
        email = self.request.form.get('email')
        message = mail.EmailMessage()
        message.to = "admin@homecampus.com.sg"
        message.sender = "admin@homecampus.com.sg"
        message.subject = "comment from "+name
        message.body = "Email: "+ email+" | "+comment
        message.Send()
        kwargs.update({'thank':"Thank you for your feedback!!"})
        return self.get(**kwargs)
  
      
class Refer(BaseHandler):  
    def get(self, **kwargs):
        kwargs.update({'form':self.form,})
        #context = {'form':self.form }              
        return self.render_response('Refer.html', **kwargs)
    
    def post(self, **kwargs):
        if self.form.validate():
            YourName = self.form.YourName.data
            FriendsName = self.form.FriendsName.data           
            email = self.form.email.data
        message = mail.EmailMessage()
        message.bcc = "admin@homecampus.com.sg"
        message.sender = "admin@homecampus.com.sg"
        message.to = email
        message.subject = "Your friend "+YourName+" wants you to visit Home Campus"
        SendMessage = "Dear "+FriendsName+",<br><br>"
        SendMessage = SendMessage + "Your friend, "+YourName+", just visited http://www.homecampus.com.sg to learn and practice mathematics in a simple and fun way, and has highly recommended that you do the same."
        SendMessage = SendMessage + "<br><br>Regards,<br>The Home Campus Team<br>Learn. Practice. Progress.<br><br>http://www.homecampus.com.sg"
        message.html = SendMessage
        message.Send()
        return self.redirect("/Learn")

    @cached_property
    def form(self):
        return ReferralForm(self.request)    

class FAQ(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('FAQs.html', section='content')

class AboutHomeCampus(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('AboutHomeCampus.html', section='content')

class PrivacyPolicy(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('PrivacyPolicy.html', section='content')

class Disclaimer(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('Disclaimer.html', section='content')

class Benefits(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('Benefits.html', section='content')

class SGMath(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('Singapore_Math.html', section='content')

class MyProfile(BaseHandler):  
    def get(self, **kwargs):
        if not self.auth.user or (self.auth.user and not self.auth.user.IsParent):
            return self.redirect("/")
        
        username = self.auth.user.username
        DisplayData = []
        PaymentData = []
        BooksData = []
        subscribe = "N"
        cancel = "N"
        ChildUserData = HomeCampusUser.gql("where email = '"+username+"' and IsParent = False").fetch(1000)
        for c in ChildUserData:
            name = c.first_name+" "+c.last_name
            username = c.username
            logging.info("username: " + username)
            HCSubscriptionData = HCSubscription.HCSubscription.gql("where student_id = '"+c.username+"' and status ='ACTIVE'").fetch(1)
            try:
                if HCSubscriptionData[0].transaction_id is None and HCSubscriptionData[0].profile_id is None:
                    status = HCSubscriptionData[0].paypal_token
                    '''When the user is manually subscribed, the paypal token is set as MANUAL or When free subscription is given to school, the paypal token is set as SCHOOL'''
                    if status == "MANUAL":
                        status = "Subscribed"
                        cancel = "Y"

                    elif status == "SCHOOL":
                        status = "Subscribed"
                    
                else:
                    status = "Subscribed"
                    if not HCSubscriptionData[0].profile_id is None:
                        cancel = "Y"
                expiry_date = HCSubscriptionData[0].end_date
                display_date = expiry_date.strftime("%d-%B-%Y")
            except IndexError:
                HCSubscriptionData = HCSubscription.HCSubscription.gql("where student_id = '"+c.username+"' and status ='CANCELLED'").fetch(1)
                try:
                    status = "Cancelled"
                    subscribe="Y"
                    expiry_date = HCSubscriptionData[0].end_date
                    display_date = expiry_date.strftime("%d-%B-%Y")
                except IndexError:
                    status = "Not Subscribed"
                    display_date = "Not applicable"
                    subscribe = "Y"
            DisplayData.append([name,username,status,display_date,subscribe])
            
            SubscriptionHistory = HCSubscription.HCSubscription.gql("where student_id = '"+c.username+"' and transaction_id != null").fetch(1000)
            for s in SubscriptionHistory:
                PaymentData.append([s.start_date.strftime("%d-%B-%Y"),name,s.amount,s.period])
                '''this profile id will used in next query to get payment details'''
            #21-AUG-2013: recurring payments are now stored in a new table
            SubscriptionHistory = HCSubscription.HCSubscription.gql("where student_id = '"+c.username+"' and profile_id != null").fetch(1000)
            profile_id = []
            for s in SubscriptionHistory:
                '''this profile id will used in next query to get payment details'''
                profile_id.append(s.profile_id)
            for p in range(len(profile_id)):
                HCPaymentHistory = HCPayment.HCPayment.gql("where recurring_payment_id = '"+str(profile_id[p])+"'").fetch(1000)
                for h in HCPaymentHistory:
                    if h.payment_status == "Completed":
                        PaymentData.append([h.payment_date.strftime("%d-%B-%Y"),name,h.amount,s.period])
            
            '''Books data'''
            HCBooksData = HCBooks.HCBooks.gql("where username = '"+c.username+"' and status ='ACTIVE'").fetch(100)
            for BD in HCBooksData:
                BooksData.append([BD.start_date.strftime("%d-%B-%Y"),name,BD.amount,BD.book_name])
            
        kwargs.update({'ChildUserData':DisplayData,'Subscribe':subscribe,'Cancel':cancel,'PaymentData':PaymentData,'BooksData':BooksData})              
        return self.render_response('MyProfile.html', **kwargs)
    
    def post(self, **kwargs):
        if not self.auth.user or (self.auth.user and not self.auth.user.IsParent):
            return self.redirect("/")       
        child_first_name_1 = unicode(self.request.form.get('child_first_name'))
        child_last_name_1 = unicode(self.request.form.get('child_last_name'))
        school_code = unicode(self.request.form.get('school_code'))
        child_skill = unicode(self.request.form.get('skill_grade'))
        
        # 05-Oct-2016 - riyaz
        # to prevent crashing when empty form is submitted
        if child_first_name_1 is None or child_first_name_1 == "":
            kwargs.update({"form_error": -1, "last_name_val": child_last_name_1})
            return self.get(**kwargs)
        
        if child_last_name_1 is None or child_last_name_1 == "":
            kwargs.update({"form_error": -2, "first_name_val": child_first_name_1})
            return self.get(**kwargs)
        
        if child_skill is None or child_skill == "":
            kwargs.update({"form_error": -3, "first_name_val": child_first_name_1, "last_name_val": child_last_name_1})
            return self.get(**kwargs)
        
        # Not checking for school code
        
        if "'" in child_first_name_1:
            child_first_name = child_first_name_1.replace("'", "")
        else:
            child_first_name = child_first_name_1
        if "'" in child_last_name_1:
            child_last_name = child_last_name_1.replace("'", "")
        else:
            child_last_name = child_last_name_1
        username = self.GenerateUsername(child_first_name, child_last_name)
        auth_id_child = 'own|%s' % username

        authorized = False
        if school_code.upper() in SchoolCodes.SchoolCodes:
            authorized = True
            
        self.auth.create_student(username, auth_id_child, password=username,email=self.auth.user.email,
                           first_name=child_first_name,last_name=child_last_name,parent_first_name=self.auth.user.first_name,
                           parent_last_name=self.auth.user.last_name,IsParent=False,skill=child_skill,authorized=authorized,school_code=school_code.upper())
        
        '''authorizing parent and adding record in HCSubscription table'''
        if authorized:
            parentData = HomeCampusUser.gql("where email = '"+self.auth.user.email+"' and IsParent = True").fetch(1)
            parentData[0].authorized = True
            parentData[0].put()

            PT = HCSubscription.HCSubscription(paypal_token="SCHOOL",
                                                  student_id=username,
                                                  amount="0",
                                                  period=int(1),
                                                  start_date = datetime.datetime.now(),
                                                  end_date= datetime.datetime.now() + datetime.timedelta(days = 180),
                                                  status="ACTIVE",
                                                  email=self.auth.user.email,
                                                  student_number=1)
            PT.put()
            
        self.sendMail(self.auth.user.email, self.auth.user.first_name, self.auth.user.last_name, child_first_name, child_last_name, username, self.auth.user.auth_id)
        kwargs.update({'UserAdded':"Y",'child_username':username})
        return self.get(**kwargs)

    def GenerateUsername(self,student_first_name,student_last_name):
        '''randomly create username and remove white spaces and lower the case'''
        self.flag = randint(1,2)
        if self.flag == 1:
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

    def sendMail(self, email, first_name, last_name, child_first_name, child_last_name, username, auth_id):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Welcome to Home Campus!!"
        SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
        SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(http://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="http://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">'
        SendMessage = SendMessage + 'Dear '+first_name+' '+last_name+','
        SendMessage = SendMessage + '<br /><br />Congratulations on your new registration to Home Campus!<br /><br />We hope you and your child will have a fun experience learning maths at Home Campus. So, <a href="http://my.homecampus.com.sg/SignIn"><font color="#0E820E">log in</font></a> and start using.<br /><br /><b><u>Registration details</u>:</b><br />'
        '''If user registers via FB or Gplus there is no username'''
        if str(auth_id)[:2]=="FB":
            SendMessage = SendMessage + 'Parent username: Login with Facebook'
        elif str(auth_id)[:2]=="G+":
            SendMessage = SendMessage + 'Parent username: Login with Google'            
        else:
            SendMessage = SendMessage + 'Parent username: '+email
        SendMessage = SendMessage + '<br />Child username: '+username+'<br /><br />'       
        SendMessage = SendMessage + 'Go ahead, explore and top math!!<br /><br /><p style="text-align:left; font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">Yours sincerely,<br />Team @ Home Campus<br /><strong><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></strong><br /><b><a href="http://my.homecampus.com.sg"><font color="#006666">www.homecampus.com.sg</font></a></b></p></td></tr></table></td></tr></tbody></table></div></td></tr></tbody></table>'
        
        message.html = SendMessage
        message.Send()

class LoginAsChild(BaseHandler):  
    def post(self, **kwargs):
        child_username = unicode(self.request.form.get('username'))
        auth_id = 'own|%s' % child_username
        logging.info(auth_id)
        self.auth.login_with_auth_id(auth_id, True)
        
        #15-07-2016 -- Riyaz
        #Sending JSON insted of plain text
        success = False
        skill = ""
        
        if self.auth.user:
            skill = str(self.auth.user.skill)
            success = True
        
        return Response(json_encode( {'success': success, 'skill': skill} ))
                   
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()