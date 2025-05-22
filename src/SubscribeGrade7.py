from tipfy import RequestHandler
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from google.appengine.api import mail
import Paypal_SinglePayment
import logging
from Database import HCBooks
from Models import HomeCampusUser
import datetime
import random


#TEST Parameters
#PAYPAL_USERNAME = 'admin_1354591843_biz_api1.homecampus.com.sg'
#PAYPAL_PASSWORD = '1354591863'
#PAYPAL_SIGNATURE = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AugDOlPVXEmykVDclx-Ft0Z8mhZ.'
#PAYPAL_SIG_URL = 'https://api-3t.sandbox.paypal.com/nvp'
#RETURNURL = 'http://homecampu-dev1-hrd.appspot.com/Subscribe/Grade7/Success'
#CANCELURL = 'http://homecampu-dev1-hrd.appspot.com/Subscribe/Grade7/Cancel'

#Production Parameters
PAYPAL_USERNAME = 'admin_api1.homecampus.com.sg'
PAYPAL_PASSWORD = 'TKGQJB9T3JUDL9Z2'
PAYPAL_SIGNATURE = 'A9vnkApYSeLAdBbiRdybn9R22.0DAZADhBeYLui-u3-YD0LO5ff47Bzs'
PAYPAL_SIG_URL = 'https://api-3t.paypal.com/nvp'
RETURNURL="http://my.homecampus.com.sg/Subscribe/Grade7/Success"
CANCELURL="http://my.homecampus.com.sg/Subscribe/Grade7/Cancel"
    
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
                       'TRIAL':'N'
                       })
        return super(BaseHandler, self).render_response(filename, **kwargs)
      
      
class Subscribe(BaseHandler):
    
    def get(self, **kwargs):
        
        if not self.auth.session:
            return self.redirect('/SignIn')
        
        ChildInfo = []
        
        if self.auth.user.IsParent:
            ParentQuery = HomeCampusUser.gql("where username = '"+self.auth.user.username+"'")
            ParentData = ParentQuery.fetch(1)
            
            StudentQuery = HomeCampusUser.gql("where email = '"+ParentData[0].email+"' and IsParent = False")
            StudentData = StudentQuery.fetch(5)

            for s in StudentData:
                ChildInfo.append([s.first_name,s.username])
        else:
            #First check if the child is a student of teacher, then a different subscription page is displayed
            StudentData = HomeCampusUser.gql("where username = '"+self.auth.user.username+"'").fetch(1)
            ParentTeacherData =  HomeCampusUser.gql("where email = '"+StudentData[0].email+"' and IsTeacher = True").fetch(1)
            if len(ParentTeacherData) == 1:
                kwargs.update({'teacher_name':ParentTeacherData[0].first_name+" "+ParentTeacherData[0].last_name})
                return self.render_response('Student_Subscription_Advise.html', **kwargs)
            else:
                ChildInfo.append([self.auth.user.first_name,self.auth.user.username])
        
        logging.info(self.auth.user.username)
               
        FeeMessage = random.choice(["<div style='margin-left:30px;padding:5px;'><font style='font-family:calibri;font-size:13px;color:#black;'>This amount keeps Home Campus running.<br>But you can edit the box to pay what it's worth to you.</font></div>"
                                    ])
        
        kwargs.update({'child_info':ChildInfo,
                       'FeeMessage':FeeMessage,})
        
        return self.render_response('SubscriptionPage-Grade7.html', **kwargs)
      

class SetExpressCheckout(BaseHandler):
    
    def get(self, **kwargs):
        
        amount = self.request.args.get('total_amount')
        username = self.request.args.get('username')
        book_code = self.request.args.get('book_code')
        start_date = datetime.datetime.now()
        pp = Paypal_SinglePayment.PayPal(PAYPAL_USERNAME, PAYPAL_PASSWORD,PAYPAL_SIGNATURE, PAYPAL_SIG_URL)
        ppResponse = pp.SetExpressCheckout(RETURNURL=RETURNURL,
                                     CANCELURL=CANCELURL,
                                     PAYMENTREQUEST_0_CURRENCYCODE="USD",
                                     PAYMENTREQUEST_0_AMT=amount,
                                     PAYMENTREQUEST_0_PAYMENTACTION="Sale",
                                     L_PAYMENTREQUEST_0_ITEMCATEGORY0="Digital",
                                     L_PAYMENTREQUEST_0_NAME0="Home Campus - Grade 7 Book",
                                     L_PAYMENTREQUEST_0_QTY0='1',
                                     L_PAYMENTREQUEST_0_AMT0=amount,
                                     )        
        logging.info(ppResponse)

        HCUser = HomeCampusUser.gql("where username = '"+username+"'").fetch(1)
        book_name = ""
        if book_code == "7A" or book_code == "7B":
            book_name = "Grade 7 Book "+book_code [1:]
            PT = HCBooks.HCBooks(paypal_token=ppResponse['TOKEN'][0],
                                                  username=username,
                                                  book_code=book_code,
                                                  book_name=book_name,
                                                  amount=amount,
                                                  start_date = start_date,
                                                  status="DUMMY",
                                                  email=HCUser[0].email)
        
            PT.put()
        elif book_code=="ALL":
            books = {"7A":"Grade 7 Book A","7B":"Grade 7 Book B",}
            for b in books:
                PT = HCBooks.HCBooks(paypal_token=ppResponse['TOKEN'][0],
                                                      username=username,
                                                      book_code=b,
                                                      book_name=books[b],
                                                      amount=amount,
                                                      start_date = start_date,
                                                      status="DUMMY",
                                                      email=HCUser[0].email)
            
                PT.put()             
            
        return ppResponse['TOKEN'][0]
      
class DoExpressCheckoutPayment(BaseHandler):
    
    def get(self, **kwargs):
        TOKEN = self.request.args.get('token')
        PAYERID = self.request.args.get('PayerID')
        pp = Paypal_SinglePayment.PayPal(PAYPAL_USERNAME, PAYPAL_PASSWORD,PAYPAL_SIGNATURE, PAYPAL_SIG_URL)
        GetECResponse = pp.GetExpressCheckoutDetails(TOKEN=TOKEN)
        CountryCode = GetECResponse['COUNTRYCODE'][0]
        logging.info(GetECResponse)
        ppResponse = pp.DoExpressCheckoutPayment(TOKEN=TOKEN,
                                                 PAYERID=PAYERID,
                                                 PAYMENTREQUEST_0_CURRENCYCODE="USD",
                                                 PAYMENTREQUEST_0_AMT=GetECResponse['PAYMENTREQUEST_0_AMT'][0],
                                                 PAYMENTREQUEST_0_PAYMENTACTION="Sale",
                                                 L_PAYMENTREQUEST_0_ITEMCATEGORY0="Digital",
                                                 L_PAYMENTREQUEST_0_NAME0="Home Campus - Grade 7 Book",
                                                 L_PAYMENTREQUEST_0_QTY0='1',
                                                 L_PAYMENTREQUEST_0_AMT0=GetECResponse['L_PAYMENTREQUEST_0_AMT0'][0],
                                                 )
        logging.info(ppResponse)
        if ppResponse['ACK'][0] in ["Success","SuccessWithWarning"]:
            TRANS_ID = ppResponse['PAYMENTINFO_0_TRANSACTIONID'][0]
            PayPalFee = ppResponse['PAYMENTINFO_0_FEEAMT'][0]
            self.AuthorizeUser(TOKEN, TRANS_ID, CountryCode, PayPalFee)
            return self.render_response('Success-Grade7.html')
        else:
            return self.render_response('Cancel-Grade7.html')

            
    def AuthorizeUser(self, token, trans_id, CountryCode="", PayPalFee=""):
        UserIDQuery = HCBooks.HCBooks.gql("where paypal_token = '"+token+"'")
        UserIDData = UserIDQuery.fetch(10)
        for u in UserIDData:
            u.transaction_id = trans_id
            u.country_code = CountryCode
            u.paypal_fee = PayPalFee
            u.status = "ACTIVE"
            u.authorized = True
            u.put()

        UserDataQuery = HomeCampusUser.gql("where username = '"+UserIDData[0].username+"'")
        UserData = UserDataQuery.fetch(1)
            
        sendMail(UserData[0].email, UserData[0].parent_first_name, UserData[0].parent_last_name, UserData[0].first_name, UserData[0].last_name, UserData[0].username)

def sendMail(email, first_name, last_name, child_first_name, child_last_name, username):
    message = mail.EmailMessage()
    message.to = email
    message.sender = "Home Campus <admin@homecampus.com.sg>"
    message.subject = "Your recent book purchase at Home Campus"
    SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
    SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(http://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="http://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">'
    SendMessage = SendMessage + 'Dear '+first_name+' '+last_name+','
    SendMessage = SendMessage + '<br /><br />Thank you for your recent book purchase at Home Campus!<br /><br />We hope you and your child will have a fun experience learning maths at Home Campus. So, <a href="http://my.homecampus.com.sg/SignIn"><font color="#0E820E">log in</font></a> and start using.<br /><br /><b><u>Registration details</u>:</b><br />'
    SendMessage = SendMessage + 'Parent username: '+email+'<br />Child username: '+username+'<br /><br />'
    SendMessage = SendMessage + 'Happy Learning!!<br /><br /><p style="text-align:left; font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">Yours sincerely,<br />Team @ Home Campus<br /><strong><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></strong><br /><b><a href="http://my.homecampus.com.sg"><font color="#006666">my.homecampus.com.sg</font></a></b></p></td></tr></table></td></tr></tbody></table></div></td></tr></tbody></table>'
    
    message.html = SendMessage
    message.Send()

class CancelTransaction(BaseHandler):

    def get(self, **kwargs):
        return self.render_response('Cancel-Grade7.html')