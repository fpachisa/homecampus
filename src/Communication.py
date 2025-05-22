from werkzeug.utils import cached_property
from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from google.appengine.api import mail
from Database import HCCommunication, HCSubscription, SubmitProblemsTable, TestsMaster, HCPayment
from Models import HomeCampusUser
import datetime
import logging
import string
import random
from tipfy import Response
import CodeTranslation

rules = [Rule('/Communication/Unsubscribe', endpoint='', handler='Communication.Unsubscribe'),
         Rule('/Communication/Day3', endpoint='', handler='Communication.Day3'),
         Rule('/Communication/Day7', endpoint='', handler='Communication.Day7'),
         Rule('/Communication/Day14', endpoint='', handler='Communication.Day14'),
         Rule('/Communication/Day20', endpoint='', handler='Communication.Day20'),
         Rule('/Communication/ReportForActiveUnsubscribedUsers', endpoint='', handler='Communication.ReportActiveUnsubscribed'),
         Rule('/Communication/ReportForUnfinishedWorksheets', endpoint='', handler='Communication.ReportForUnfinishedWorksheets'),
         Rule('/Communication/IncompleteTransactionReminder', endpoint='', handler='Communication.IncompleteTransactionReminder'),
         Rule('/Communication/NextPaymentReminder', endpoint='', handler='Communication.NextPaymentReminder'),
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

        kwargs.update({
            'auth_session': auth_session,
            'current_user': self.auth.user,
            'login_url':    self.auth.login_url(),
            'logout_url':   self.auth.logout_url(),
            'current_url':  self.request.url,
            'TRIAL':TRIAL
        })

        return super(BaseHandler, self).render_response(filename, **kwargs)
      
class Unsubscribe(BaseHandler):
    def get(self, **kwargs):
        '''3 represents user who is 3 days old at HC and 1 represents first communication'''
        UnsubscriptionKey = str(self.request.args.get('key'))
        email = str(self.request.args.get('email'))
        CommQuery = HCCommunication.HCCommunication().gql("where UnsubscriptionKey = '"+UnsubscriptionKey+"' and email ='"+email+"'")
        CommData = CommQuery.fetch(1)
        
        for c in CommData:
            logging.info("Unsubscribed: "+email)
            c.unsubscribed = True
            c.UpdateDate = datetime.datetime.now()
            c.put()
        
        emailDict = {'email':email}
        return self.render_response('Unsubscribe.html',**emailDict)
    
class Day3(BaseHandler):
   
    def get(self, **kwargs):
        '''3 represents user who is 3 days old at HC and 1 represents first communication'''
        UserList = GetUserList(3,1)
        
        logging.info("Day 3 email being sent...")        
        for i in range(len(UserList)):
            logging.info(UserList[i][0]+" "+UserList[i][1]+" - "+UserList[i][2])
            self.SendMail(UserList[i][0],UserList[i][1],UserList[i][2],UserList[i][3])

        response = Response("")
        response.status_code = 200
        return response

    def SendMail(self, first_name, last_name, email, UnsubscriptionKey):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Excel Math with Home Campus"
        SendMessage = 'Dear '+first_name+' '+last_name+','
        SendMessage = SendMessage + '<p>Thank you for joining Home Campus!</p><ul><li><strong><span style="color: #ff0000;"><a style="color: #ff0000;" href="https://my.homecampus.com.sg">Watch &amp; Learn</a><sup>FREE</sup>:</span></strong>&nbsp;Content broken into bite sized video tutorials and picture notes.</li><li style="margin-top: 20px;"><span style="color: #99cc00;"><strong><a style="color: #2a91e1;" href="my.homecampus.com.sg">Practice:</a></strong>&nbsp;<span style="color: #000000;">Unlimited questions with detailed step-by-step solutions.</span></span></li><li style="margin-top: 20px;"><a href="my.homecampus.com.sg"><strong><span style="color: #99cc00;"><span style="color: #0e820e;">Worksheets:</span></span></strong></a>&nbsp;Instant grading to assess your knowledge with unlimited topical worksheets.</li><li style="margin-top: 20px;"><strong><span style="color: #f6b937;"><a style="color: #ff9900;" href="my.homecampus.com.sg">Progess:</a></span></strong>&nbsp;Identify areas of strengths and weaknesses.</li></ul><p>&nbsp;</p><p>This and much more await you.</p><p>Happy Learning!</p><p>Team @ Home Campus</p><p><strong><span style="color: #d92118;">Learn.</span> <span style="color: #2a91e1;">Practice.</span> <span style="color: #f6b937;">Progress.</span></strong><br /><strong><a href="https://my.homecampus.com.sg"><span style="color: #006666;">my.homecampus.com.sg</span></a></strong></p><font color="#999999"><a href="https://my.homecampus.com.sg/FAQs" title="Home Campus FAQs" target="_new">FAQs</a> | <a href="https://www.facebook.com/HomeCampus" title="like Home Campus on Facebook" target="_new">Facebook</a> | <a href="https://www.youtube.com/HomeCampus" title="Home Campus @ YouTube" target="_new">YouTube</a> | <a href="https://my.homecampus.com.sg/Communication/Unsubscribe?key='+UnsubscriptionKey+'&email='+email+'">Unsubscribe</a></font>'
        message.html = SendMessage
        
        try:
            message.Send()
        except:
            pass

class Day7(BaseHandler):

    def get(self, **kwargs):
        '''3 represents user who is 14 days old at HC and 3 represents third communication'''
        UserList = GetUserList(14,5)
        
        logging.info("Day 14: "+str(len(UserList))+ " emails sent.")
        for i in range(len(UserList)):
            logging.info(UserList[i][0]+" "+UserList[i][1]+" - "+UserList[i][2])
            self.SendMail(UserList[i][0],UserList[i][1],UserList[i][2],UserList[i][3])
        
        response = Response("")
        response.status_code = 200
        return response

    def SendMail(self, first_name, last_name, email, UnsubscriptionKey):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Where will you spend your $9.44 today?"
        SendMessage = 'Dear '+first_name+' '+last_name+',<br><br>'
        SendMessage = SendMessage + '<p>Where will you spend your $9.44 today?</p><ul><li style="margin-bottom: 10px;"><strong><span style="color: #d92118;">On one month of Netflix.</span></strong></li><li style="margin-bottom: 10px;"><strong><span style="color: #2a91e1;">A fast food meal.</span></strong></li><li style="margin-bottom: 10px;"><strong><span style="color: #0e820e;">A designer bag after multiplying it by 200.</span></strong></li><li style="margin-bottom: 10px;"><strong><span style="color: #f6b937;"><span style="color: #ff9900;">To build a&nbsp;<a style="color: #ff9900;" href="my.homecampus.com.sg">strong foundation in Mathematics</a>&nbsp;for your child</span>.</span></strong></li></ul><p>&nbsp;</p><p>The choice is yours...Keep Learning!</p><p>&nbsp;</p><p><span style="color: #999999;"><a title="Home Campus FAQs" href="https://my.homecampus.com.sg/FAQs" target="_new">FAQs</a> | <a title="like Home Campus on Facebook" href="https://www.facebook.com/HomeCampus" target="_new">Facebook</a> | <a title="Home Campus @ YouTube" href="https://www.youtube.com/HomeCampus" target="_new">YouTube</a> | <a href="https://my.homecampus.com.sg/Communication/Unsubscribe?key='+UnsubscriptionKey+'&amp;email='+email+'">Unsubscribe</a></span></p>'
        message.html = SendMessage
        
        try:
            message.Send()
        except:
            pass
   

class Day14(BaseHandler):

    def get(self, **kwargs):
        '''3 represents user who is 7 days old at HC and 2 represents second communication'''
        UserList = GetUserList(7,4)
        
        logging.info("Day 7: "+str(len(UserList))+ " emails sent.")
        for i in range(len(UserList)):
            logging.info(UserList[i][0]+" "+UserList[i][1]+" - "+UserList[i][2])
            self.SendMail(UserList[i][0],UserList[i][1],UserList[i][2],UserList[i][3],UserList[i][4])

        response = Response("")
        response.status_code = 200
        return response

    def SendMail(self, first_name, last_name, email, UnsubscriptionKey, child_first_name):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Gift: 50% OFF "+ child_first_name + "'s Education"

        SendMessage = '<p>Dear '+first_name+' '+last_name+',<p>'
        SendMessage = SendMessage + "<p>I have noticed that "+child_first_name+ " is not availing of all the remarkable features of Home Campus as you have not upgraded your account yet.</p>"
        SendMessage = SendMessage + "<p>Learning is your child's right. To welcome "+child_first_name+" to the online school of math, here's a gift just for you - an exclusive 50% off the subscription, if you act now.</p><br>"
        SendMessage = SendMessage + '<a href="https://my.homecampus.com.sg/Subscribe/xgIPhAi6wFgnqcj" style="color:white;background-color:#0e820e;cursor:pointer;padding:10px;border-radius:15px;font-family:arial;font-size:14px;">50% Off Home Campus Subscription</a>'
        SendMessage = SendMessage + '<br><p>Do not miss out. This offer is available for 7 days only.</p>'
        SendMessage = SendMessage + "<p>Thank you for taking the time to have a look at our great learning tool for maths. We work hard every day to improve Home Campus for you. So if you have an idea for a new feature or would like to share what you liked or did not like, leave us your feedback.</p>"
        SendMessage = SendMessage + "<p>We would love to hear from you.</p>"
        SendMessage = SendMessage + "<p>Best regards,</p>"
        SendMessage = SendMessage + "<p>Farhat</p><p>Founder</p><p>Home Campus</p><br>"
        SendMessage = SendMessage + '<p><span style="color: #999999;">If you no longer want to receive any more messages from us, you can&nbsp;<a style="color: #999999;" href="https://my.homecampus.com.sg/Communication/Unsubscribe?key='+UnsubscriptionKey+'&amp;email='+email+'">unsubscribe here</a></span></p>'
        message.html = SendMessage
        
        try:
            message.Send()
        except:
            pass


class Day20(BaseHandler):

    def get(self, **kwargs):
        '''20 represents user who is 20 days old at HC and 6 represents sixth??? communication'''
        UserList = GetUserList(20,6)
        
        logging.info("Day 20: "+str(len(UserList))+ " emails sent.")
        for i in range(len(UserList)):
            logging.info(UserList[i][0]+" "+UserList[i][1]+" - "+UserList[i][2])
            self.SendMail(UserList[i][0],UserList[i][1],UserList[i][2],UserList[i][3],UserList[i][4])

        response = Response("")
        response.status_code = 200
        return response

    def SendMail(self, first_name, last_name, email, UnsubscriptionKey, child_first_name):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "How is "+ child_first_name + " doing in Math?"

        SendMessage = '<p>Dear '+first_name+' '+last_name+',<p>'
        SendMessage = SendMessage + "<p>Every child is bright, all they need is a little guidance.</p>"
        SendMessage = SendMessage + "<p>Let us together provide "+child_first_name+" the foundation s/he needs to excel in Math!</p>"
        SendMessage = SendMessage + "<p>We are giving "+child_first_name+" 50% off on Home Campus subscription. It's your turn now.</p>"
        SendMessage = SendMessage + '<br><p><a href="https://my.homecampus.com.sg/Subscribe/xgIPhAi6wFgnqcj" style="color:white;background-color:#0e820e;cursor:pointer;padding:10px;border-radius:15px;font-family:arial;font-size:14px;">50% Off Home Campus Subscription</a></p>'
        SendMessage = SendMessage + "<br><p>Best regards,</p>"
        SendMessage = SendMessage + "<p>Farhat</p><p>Founder</p><p>Home Campus</p><br>"
        SendMessage = SendMessage + '<p><span style="color: #999999;">If you no longer want to receive any more messages from us, you can&nbsp;<a style="color: #999999;" href="https://my.homecampus.com.sg/Communication/Unsubscribe?key='+UnsubscriptionKey+'&amp;email='+email+'">unsubscribe here</a></span></p>'
        message.html = SendMessage
        
        try:
            message.Send()
        except:
            pass
   

class ReportActiveUnsubscribed(BaseHandler):
   
    def get(self, **kwargs):
        UserList = GetActiveUnsubscribedUserList()
        logging.info("Active Unsubscribed User List: "+str(len(UserList))+ " emails sent.")
        for i in range(len(UserList)):
            parent_first_name = UserList[i][0]
            parent_last_name = UserList[i][1]
            email = UserList[i][2]
            student_name = UserList[i][3]
            problem_solved = UserList[i][4]
            correct_solved = UserList[i][5]
            UnsubscriptionKey = UserList[i][6]
            logging.info(student_name+" "+email+" - "+str(problem_solved))
            
            self.SendMail(parent_first_name,parent_last_name,email,student_name,problem_solved,correct_solved,UnsubscriptionKey)
        
        response = Response("")
        response.status_code = 200
        return response

    def SendMail(self,parent_first_name,parent_last_name,email,student_name,problem_solved,correct_solved,UnsubscriptionKey):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = student_name+"'s Progress Report"
        SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
        SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(https://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="https://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">'
        SendMessage = SendMessage + 'Dear '+parent_first_name+' '+parent_last_name+',<br><br>'
        SendMessage = SendMessage + "<font style='font-size:12px;'>Here is "+student_name+"'s fortnightly Maths report.</font><br><br>"
        SendMessage = SendMessage + 'Total Problems Solved: '+str(problem_solved)+"<br><br>"
        SendMessage = SendMessage + 'Problems Solved Correctly: '+str(correct_solved)+"<br><br>"
        SendMessage = SendMessage + "Click here for "+student_name+"'s <a href='https://my.homecampus.com.sg/Progress'>detailed report card</a>.<br><br><br><br>"
        SendMessage = SendMessage + '<table cellpadding="0" cellspacing="0" border="0" style="padding: 0px; font-size: 10px; line-height: 1.5em; font-family:Verdana; color: #999;"><tbody><tr><td height="10" bgcolor="#f7f7f2" style="text-align:left; padding-right: 10px; padding-left: 10px; padding-bottom: 1px; padding-top: 1px;"><font color="#999999"><a href="https://my.homecampus.com.sg/FAQs" title="Home Campus FAQs" target="_new">FAQs</a> | <a href="https://www.facebook.com/HomeCampus" title="like Home Campus on Facebook" target="_new">Like us on Facebook</a> | <a href="https://www.youtube.com/HomeCampus" title="Home Campus @ YouTube" target="_new">Follow on YouTube</a> | <a href="https://my.homecampus.com.sg/Communication/Unsubscribe?key='+UnsubscriptionKey+'&email='+email+'">Unsubscribe</a></font></td></tr></tbody></table><br><br>'
        message.html = SendMessage
        
        try:
            message.Send()
        except:
            pass

class ReportForUnfinishedWorksheets(BaseHandler):
   
    def get(self, **kwargs):
        UserList = GetUnfinishedWorksheetUserList()
        logging.info("Unfinished Worksheet User List: "+str(len(UserList))+ " emails sent.")
        for i in range(len(UserList)):
            parent_first_name = UserList[i][0]
            parent_last_name = UserList[i][1]
            email = UserList[i][2]
            student_name = UserList[i][3]
            URL = UserList[i][4]
            TopicName = UserList[i][5]
            UnsubscriptionKey = UserList[i][6]
            logging.info(student_name+" - "+email)
            
            self.SendMail(parent_first_name,parent_last_name,email,student_name,URL,TopicName,UnsubscriptionKey)
        
        response = Response("")
        response.status_code = 200
        return response

    def SendMail(self,parent_first_name,parent_last_name,email,student_name,URL,TopicName,UnsubscriptionKey):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = student_name+" has Unfinished Homework"
        SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
        SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(https://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="https://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">'
        SendMessage = SendMessage + 'Dear '+parent_first_name+' '+parent_last_name+',<br><br>'
        SendMessage = SendMessage + "<font style='font-size:12px;'>"+student_name+"'s maths homework on <i>"+TopicName+"</i> is due.</font><br><br>"
        SendMessage = SendMessage + "Click here to <a href='https://my.homecampus.com.sg"+URL+"'>complete and master the skill</a>.<br><br><br>"
        SendMessage = SendMessage + '<table cellpadding="0" cellspacing="0" border="0" style="padding: 0px; font-size: 10px; line-height: 1.5em; font-family:Verdana; color: #999;"><tbody><tr><td height="10" bgcolor="#f7f7f2" style="text-align:left; padding-right: 10px; padding-left: 10px; padding-bottom: 1px; padding-top: 1px;"><font color="#999999"><a href="https://my.homecampus.com.sg/FAQs" title="Home Campus FAQs" target="_new">FAQs</a> | <a href="https://www.facebook.com/HomeCampus" title="like Home Campus on Facebook" target="_new">Like us on Facebook</a> | <a href="https://www.youtube.com/HomeCampus" title="Home Campus @ YouTube" target="_new">Follow on YouTube</a> | <a href="https://my.homecampus.com.sg/Communication/Unsubscribe?key='+UnsubscriptionKey+'&email='+email+'">Unsubscribe</a></font></td></tr></tbody></table><br><br>'
        message.html = SendMessage
        
        try:
            message.Send()
        except:
            pass
         
class IncompleteTransactionReminder(BaseHandler):
   
    def get(self, **kwargs):
        UserList = GetUncompleteTransactionUserList()
        logging.info("Uncomplete Transaction User List: "+str(len(UserList))+ " emails sent.")
        for i in range(len(UserList)):
            parent_first_name = UserList[i][0]
            parent_last_name = UserList[i][1]
            email = UserList[i][2]
            UnsubscriptionKey = UserList[i][3]
            child_first_name = UserList[i][4]
            logging.info(parent_first_name+" - "+email)
            
            self.SendMail(parent_first_name,parent_last_name,email,UnsubscriptionKey,child_first_name)
        
        response = Response("")
        response.status_code = 200
        return response

    ''' changing this mail to more aggressive one :)

    def SendMail(self,parent_first_name,parent_last_name,email,UnsubscriptionKey):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Let Your Learning Journey Begin!!"
        SendMessage = 'Dear '+parent_first_name+' '+parent_last_name+',<br><br>'
        SendMessage = SendMessage + '<p>Thank you for joining&nbsp;<strong><a href="my.homecampus.com.sg">Home Campus!</a></strong></p><p>Let your math learning journey begin for as low as $4.88 per month.</p><p>&nbsp;</p><ul><li style="margin-bottom: 10px;"><strong><span style="color: #d92118;">Watch and Learn through bite-sized tutorials.</span></strong></li><li style="margin-bottom: 10px;"><strong><span style="color: #2a91e1;">Practice Unlimited Questions.</span></strong></li><li style="margin-bottom: 10px;"><strong><span style="color: #0e820e;">Solve as many Topical Worksheets as you need.</span></strong></li><li style="margin-bottom: 10px;"><strong><span style="color: #f6b937;"><span style="color: #ff9900;">Monitor Progress.</span></span></strong></li></ul><p>&nbsp;</p><p>&nbsp;</p><p><span style="color: #999999;"><a title="Home Campus FAQs" href="https://my.homecampus.com.sg/FAQs" target="_new">FAQs</a> | <a title="like Home Campus on Facebook" href="https://www.facebook.com/HomeCampus" target="_new">Facebook</a> | <a title="Home Campus @ YouTube" href="https://www.youtube.com/HomeCampus" target="_new">YouTube</a> | <a href="https://my.homecampus.com.sg/Communication/Unsubscribe?key='+UnsubscriptionKey+'&amp;email='+email+'">Unsubscribe</a></span></p>'
        message.html = SendMessage
        
        message.Send()'''

    def SendMail(self, first_name, last_name, email, UnsubscriptionKey, child_first_name):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Gift: 50% OFF "+ child_first_name + "'s Education"

        SendMessage = '<p>Dear '+first_name+' '+last_name+',<p>'
        SendMessage = SendMessage + "<p>I have noticed that "+child_first_name+ " is not availing of all the remarkable features of Home Campus as you have not upgraded your account yet.</p>"
        SendMessage = SendMessage + "<p>Learning is your child's right. To welcome "+child_first_name+" to the online school of math, here's a gift just for you - an exclusive 50% off the subscription, if you act now.</p>"
        SendMessage = SendMessage + '<a href="https://my.homecampus.com.sg/Subscribe/xgIPhAi6wFgnqcj" style="color:white;background-color:#0e820e;cursor:pointer;padding:10px;border-radius:15px;font-family:arial;font-size:14px;">50% Off Home Campus Subscription</a>'
        SendMessage = SendMessage + '<p>Do not miss out. This offer is available for 7 days only.</p>'
        SendMessage = SendMessage + "<p>Thank you for taking the time to have a look at our great learning tool for maths. We work hard every day to improve Home Campus for you. So if you have an idea for a new feature or would like to share what you liked or did not like, leave us your feedback.</p>"
        SendMessage = SendMessage + "<p>We would love to hear from you.</p>"
        SendMessage = SendMessage + "<p>Best regards,</p>"
        SendMessage = SendMessage + "<p>Farhat</p><p>Founder</p><p>Home Campus</p>"
        message.html = SendMessage
        
        try:
            message.Send()
        except:
            pass

''' This code for next payment auto reminder has been commented for now....please test before activating
class NextPaymentReminder(BaseHandler):
   
    def get(self, **kwargs):
        emailID = []
        logging.info("Sending payment reminder 7 days in advance")
        query_date1 = datetime.datetime.now() + datetime.timedelta(days = 7)
        query_date2 = datetime.datetime.now() + datetime.timedelta(days = 8)
        DateString1 = str(query_date1.year)+"-"+str(query_date1.month)+"-"+str(query_date1.day)
        DateString2 = str(query_date2.year)+"-"+str(query_date2.month)+"-"+str(query_date2.day)
        #Getting parent email for reminder
        NextPaymentData = HCPayment.HCPayment.gql("where next_payment_date > Date('"+DateString1+"') and next_payment_date < Date('"+DateString2+"')").fetch(10000)    
        for PID in NextPaymentData:
            SubscriptionData = HCSubscription.HCSubscription.gql("where profile_id = '"+PID.recurring_payment_id+"'")
            for SD in SubscriptionData:
                if SD.status == 'ACTIVE':
                    emailID.append(SD.email)
        self.SendMail(emailID)
        response = Response("")
        response.status_code = 200
        return response

    def SendMail(self,parent_first_name,parent_last_name,email,UnsubscriptionKey):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Next Payment Reminder"
        SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
        SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(https://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="https://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">'
        SendMessage = SendMessage + 'Thank you for subscribing to Home Campus!<br /><br />This is a gentle reminder that your next automatic payment will occur within 7 days.<br /><br />'
        SendMessage = SendMessage + '<table cellpadding="0" cellspacing="0" border="0" style="padding: 0px; font-size: 10px; line-height: 1.5em; font-family:Verdana; color: #999;"><tbody><tr><td height="10" bgcolor="#f7f7f2" style="text-align:left; padding-right: 10px; padding-left: 10px; padding-bottom: 1px; padding-top: 1px;"><font color="#999999"><a href="https://my.homecampus.com.sg/FAQs" title="Home Campus FAQs" target="_new">FAQs</a> | <a href="https://www.facebook.com/HomeCampus" title="like Home Campus on Facebook" target="_new">Like us on Facebook</a> | <a href="https://www.youtube.com/HomeCampus" title="Home Campus @ YouTube" target="_new">Follow on YouTube</a> | <a href="https://my.homecampus.com.sg/Communication/Unsubscribe?key='+UnsubscriptionKey+'&email='+email+'">Unsubscribe</a></font></td></tr></tbody></table><br><br>'
        message.html = SendMessage
        
        message.Send() 
'''

def GetUserList(Days,Key):
        UserList = []
        query_date1 = datetime.datetime.now() + datetime.timedelta(days = -Days)
        query_date2 = datetime.datetime.now() + datetime.timedelta(days = -Days-2)

        if len(str(query_date1.month))== 1:
            month1 = '0'+str(query_date1.month)
        else:
            month1 = str(query_date1.month)
        if len(str(query_date1.year))== 1:
            day1 = '0'+str(query_date1.day)
        else:
            day1 = str(query_date1.day)
        if len(str(query_date2.month))== 1:
            month2 = '0'+str(query_date2.month)
        else:
            month2 = str(query_date2.month)
        if len(str(query_date2.year))== 1:
            day2 = '0'+str(query_date2.day)
        else:
            day2 = str(query_date2.day)
        DateString1 = str(query_date1.year)+"-"+month1+"-"+day1+' 00:00:00'
        DateString2 = str(query_date2.year)+"-"+month2+"-"+day2+' 00:00:00'
        UserQuery = HomeCampusUser.gql("where created > DATETIME('"+DateString2+"') and created < DATETIME('"+DateString1+"')")
        UserData = UserQuery.fetch(10000)
        for u in UserData:
            if not u.IsParent and not u.IsTeacher and not u.authorized:
                CommQuery = HCCommunication.HCCommunication().gql("where email = '"+u.email+"'")
                CommData = CommQuery.fetch(1)
                if not CommData:
                    UnsubscriptionKey = ''.join(random.choice(string.ascii_uppercase + string.digits) for _x in range(8))
                    HCComm = HCCommunication.HCCommunication(email=u.email,
                                                             UnsubscriptionKey=UnsubscriptionKey,
                                                             LastCommunicationKey = str(Key))
                    HCComm.put()
                    UserList.append([u.parent_first_name,u.parent_last_name,u.email,UnsubscriptionKey,u.first_name,u.last_name])
                else:
                    for c in CommData:
                        '''Checking if the email has already been sent'''
                        if c.LastCommunicationKey < str(Key) and not c.unsubscribed:
                            if c.UnsubscriptionKey is None:
                                c.UnsubscriptionKey = ''.join(random.choice(string.ascii_uppercase + string.digits) for _x in range(8))
                            c.LastCommunicationKey = str(Key)
                            c.UpdateDate = datetime.datetime.now()
                            c.put()
                            UserList.append([u.parent_first_name,u.parent_last_name,u.email,c.UnsubscriptionKey,u.first_name,u.last_name])
        return UserList

def GetActiveUnsubscribedUserList():
    ActiveUnsubscribedParentList = []
    ActiveStudentsData = {}
    ParentsData = []
    query_date1 = datetime.datetime.now() + datetime.timedelta(days = -1)
    query_date2 = datetime.datetime.now() + datetime.timedelta(days = -15)
    if len(str(query_date1.month))== 1:
        month1 = '0'+str(query_date1.month)
    else:
        month1 = str(query_date1.month)
    if len(str(query_date1.year))== 1:
        day1 = '0'+str(query_date1.day)
    else:
        day1 = str(query_date1.day)
    if len(str(query_date2.month))== 1:
        month2 = '0'+str(query_date2.month)
    else:
        month2 = str(query_date2.month)
    if len(str(query_date2.year))== 1:
        day2 = '0'+str(query_date2.day)
    else:
        day2 = str(query_date2.day)
    DateString1 = str(query_date1.year)+"-"+month1+"-"+day1+' 00:00:00'
    DateString2 = str(query_date2.year)+"-"+month2+"-"+day2+' 00:00:00'    
    '''Getting active students solved questions for the past 15 days'''
    SolvedQuestionsData = SubmitProblemsTable.ProblemsTable.gql("where submit_date > DATETIME('"+DateString2+"') and submit_date < DATETIME('"+DateString1+"')").fetch(10000)    
    for SQD in SolvedQuestionsData:
        solvedQuestions = 1
        correctSolved = 0
        if SQD.student_id in ActiveStudentsData:
            solvedQuestions = ActiveStudentsData[SQD.student_id][0] + 1
            if SQD.correct:
                correctSolved = ActiveStudentsData[SQD.student_id][1] + 1
        else:
            if SQD.correct:
                correctSolved = 1
                
        ActiveStudentsData.update({SQD.student_id:[solvedQuestions,correctSolved]})

    '''Getting email and parents information for users who are not subscribed and created account atleast 12 days prior to today'''
    for ASD in ActiveStudentsData:
        StudentsUserData = HomeCampusUser.gql("where username = '"+ASD+"'").fetch(1)
        try:
            query_date3 = datetime.datetime.now() + datetime.timedelta(days = -12)
            if StudentsUserData[0].created < query_date3 and not StudentsUserData[0].authorized and not StudentsUserData[0].IsParent and not StudentsUserData[0].IsTeacher:
                student_first_name = StudentsUserData[0].first_name
                parent_first_name = StudentsUserData[0].parent_first_name
                parent_last_name = StudentsUserData[0].parent_last_name
                email = StudentsUserData[0].email
                solvedQuestions = ActiveStudentsData[ASD][0]
                correctSolved = ActiveStudentsData[ASD][1]
                ParentsData.append([student_first_name,parent_first_name,parent_last_name,email,solvedQuestions,correctSolved])
        except IndexError:
            pass   
    '''Sending only to users for which this report has not been send for past 15 days'''
    for u in range(len(ParentsData)):
        email = ParentsData[u][3]
        CommQuery = HCCommunication.HCCommunication().gql("where email = '"+email+"'")
        CommData = CommQuery.fetch(1)
        if not CommData:
            UnsubscriptionKey = ''.join(random.choice(string.ascii_uppercase + string.digits) for _x in range(8))
            HCComm = HCCommunication.HCCommunication(email=email,
                                                     UnsubscriptionKey=UnsubscriptionKey,
                                                     ActiveUnsubscribedReportdate = datetime.datetime.now())
            HCComm.put()
            ActiveUnsubscribedParentList.append([ParentsData[u][1],ParentsData[u][2],ParentsData[u][3],ParentsData[u][0],ParentsData[u][4],ParentsData[u][5],UnsubscriptionKey])
        else:
            for c in CommData:
                '''Checking if the email has already been sent'''
                if (c.ActiveUnsubscribedReportdate is None or c.ActiveUnsubscribedReportdate < query_date2) and not c.unsubscribed:
                    if c.UnsubscriptionKey is None:
                        c.UnsubscriptionKey = ''.join(random.choice(string.ascii_uppercase + string.digits) for _x in range(8))
                    c.ActiveUnsubscribedReportdate = datetime.datetime.now()
                    c.UpdateDate = datetime.datetime.now()
                    c.ActiveUnsubscribedReportdate = datetime.datetime.now()
                    c.put()
                    ActiveUnsubscribedParentList.append([ParentsData[u][1],ParentsData[u][2],ParentsData[u][3],ParentsData[u][0],ParentsData[u][4],ParentsData[u][5],c.UnsubscriptionKey])       
    
    return ActiveUnsubscribedParentList
       
def GetUnfinishedWorksheetUserList():
    ParentsEmailList = []
    StudentsData = {}
    ParentsData = []
    query_date1 = datetime.datetime.now() + datetime.timedelta(days = -5)
    query_date2 = datetime.datetime.now() + datetime.timedelta(days = -7)
    if len(str(query_date1.month))== 1:
        month1 = '0'+str(query_date1.month)
    else:
        month1 = str(query_date1.month)
    if len(str(query_date1.year))== 1:
        day1 = '0'+str(query_date1.day)
    else:
        day1 = str(query_date1.day)
    if len(str(query_date2.month))== 1:
        month2 = '0'+str(query_date2.month)
    else:
        month2 = str(query_date2.month)
    if len(str(query_date2.year))== 1:
        day2 = '0'+str(query_date2.day)
    else:
        day2 = str(query_date2.day)
    DateString1 = str(query_date1.year)+"-"+month1+"-"+day1+' 00:00:00'
    DateString2 = str(query_date2.year)+"-"+month2+"-"+day2+' 00:00:00'    

    '''Getting list of unfinished worksheets for past 5 days'''
    UnfinishedWorksheetsData = TestsMaster.TestsMasterTable.gql("where create_date > DATETIME('"+DateString2+"') and create_date < DATETIME('"+DateString1+"')").fetch(10000)    
    for UWD in UnfinishedWorksheetsData:
        if UWD.student_id not in StudentsData and UWD.status!='Completed':              
            StudentsData.update({UWD.student_id:UWD.sub_concept})

    '''Getting email and parents information for students who have not completed worksheets for 5 days'''
    for SD in StudentsData:
        StudentsUserData = HomeCampusUser.gql("where username = '"+SD+"'").fetch(1)
        try:
            if not StudentsUserData[0].authorized and not StudentsUserData[0].IsParent and not StudentsUserData[0].IsTeacher:
                student_first_name = StudentsUserData[0].first_name
                parent_first_name = StudentsUserData[0].parent_first_name
                parent_last_name = StudentsUserData[0].parent_last_name
                email = StudentsUserData[0].email
                try:
                    URL = CodeTranslation.WorksheetURL[StudentsData[SD]]
                except KeyError:
                    URL = ""
                try:
                    TopicName = CodeTranslation.MainConcept[StudentsData[SD]]
                except KeyError:
                    TopicName = ""
                ParentsData.append([student_first_name,parent_first_name,parent_last_name,email,URL,TopicName])
        except IndexError:
            pass   
    '''Sending only to users for which this report has not been send for past 10 days'''
    for u in range(len(ParentsData)):
        email = ParentsData[u][3]
        CommQuery = HCCommunication.HCCommunication().gql("where email = '"+email+"'")
        CommData = CommQuery.fetch(1)
        if not CommData:
            UnsubscriptionKey = ''.join(random.choice(string.ascii_uppercase + string.digits) for _x in range(8))
            HCComm = HCCommunication.HCCommunication(email=email,
                                                     UnsubscriptionKey=UnsubscriptionKey,
                                                     UnfinishedWorksheetReportdate = datetime.datetime.now())
            HCComm.put()
            ParentsEmailList.append([ParentsData[u][1],ParentsData[u][2],ParentsData[u][3],ParentsData[u][0],ParentsData[u][4],ParentsData[u][5],UnsubscriptionKey])
        else:
            for c in CommData:
                '''Checking if the email has already been sent'''
                if (c.UnfinishedWorksheetReportdate is None or c.UnfinishedWorksheetReportdate < query_date1) and not c.unsubscribed:
                    if c.UnsubscriptionKey is None:
                        c.UnsubscriptionKey = ''.join(random.choice(string.ascii_uppercase + string.digits) for _x in range(8))
                    c.UnfinishedWorksheetReportdate = datetime.datetime.now()
                    c.UpdateDate = datetime.datetime.now()
                    c.UnfinishedWorksheetReportdate = datetime.datetime.now()
                    c.put()
                    ParentsEmailList.append([ParentsData[u][1],ParentsData[u][2],ParentsData[u][3],ParentsData[u][0],ParentsData[u][4],ParentsData[u][5],c.UnsubscriptionKey])       
    
    return ParentsEmailList

def GetUncompleteTransactionUserList():
    UsedIdList = []
    UserData = []
    query_date1 = datetime.datetime.now() + datetime.timedelta(days = 1)
    query_date2 = datetime.datetime.now() + datetime.timedelta(days = -2)
    query_date3 = datetime.datetime.now() + datetime.timedelta(days = -30)
    if len(str(query_date1.month))== 1:
        month1 = '0'+str(query_date1.month)
    else:
        month1 = str(query_date1.month)
    if len(str(query_date1.year))== 1:
        day1 = '0'+str(query_date1.day)
    else:
        day1 = str(query_date1.day)
    if len(str(query_date2.month))== 1:
        month2 = '0'+str(query_date2.month)
    else:
        month2 = str(query_date2.month)
    if len(str(query_date2.year))== 1:
        day2 = '0'+str(query_date2.day)
    else:
        day2 = str(query_date2.day)
    DateString1 = str(query_date1.year)+"-"+month1+"-"+day1+' 00:00:00'
    DateString2 = str(query_date2.year)+"-"+month2+"-"+day2+' 00:00:00'    

    '''Getting list of incompleted transactions that happened 1 day ago'''
    IncompleteTransactionData = HCSubscription.HCSubscription.gql("where start_date > DATETIME('"+DateString2+"') and start_date <= DATETIME('"+DateString1+"') and status = 'DUMMY' ").fetch(10000)    
    for ITD in IncompleteTransactionData:
        if ITD.student_id not in UsedIdList:
            UserQuery = HomeCampusUser.gql("where username = '"+ITD.student_id+"' and authorized = False").fetch(1)
            for u in UserQuery:
                parent_first_name = u.parent_first_name
                parent_last_name = u.parent_last_name
                email = u.email
                child_first_name = u.first_name
                CommQuery = HCCommunication.HCCommunication().gql("where email = '"+email+"'")
                CommData = CommQuery.fetch(1)
                if not CommData:
                    UnsubscriptionKey = ''.join(random.choice(string.ascii_uppercase + string.digits) for _x in range(8))
                    HCComm = HCCommunication.HCCommunication(email=email,
                                                             UnsubscriptionKey=UnsubscriptionKey,
                                                             IncompleteTransactionReportdate = datetime.datetime.now())
                    HCComm.put()
                    UserData.append([parent_first_name,parent_last_name,email,UnsubscriptionKey,child_first_name])
                else:
                    for c in CommData:
                        '''Checking if the email has already been sent'''
                        if (c.IncompleteTransactionReportdate is None or c.IncompleteTransactionReportdate < query_date3) and not c.unsubscribed:
                            if c.UnsubscriptionKey is None:
                                c.UnsubscriptionKey = ''.join(random.choice(string.ascii_uppercase + string.digits) for _x in range(8))
                            c.IncompleteTransactionReportdate = datetime.datetime.now()
                            c.UpdateDate = datetime.datetime.now()
                            c.put()
                            UserData.append([parent_first_name,parent_last_name,email,c.UnsubscriptionKey,child_first_name])       
                
            UsedIdList.append(ITD.student_id)

        ITD.delete()
    
    return UserData
    
    
            
                   
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()