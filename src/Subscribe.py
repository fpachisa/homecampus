from werkzeug.utils import cached_property
from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware, admin_required, login_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from google.appengine.api import mail
import Paypal
import logging
from Database import HCSubscription, HCPayment
from Models import HomeCampusUser
import datetime
import CustomerFeedback
from google.appengine.api import memcache
import random
from urllib import urlencode
from google.appengine.api import urlfetch
from tipfy import Response

rules = [Rule('/Subscribe', endpoint='', handler='Subscribe.Subscribe'),
         Rule('/Subscribe/xgIPhAi6wFgnqcj', endpoint='', handler='Subscribe.Subscribe50'),
         Rule('/Subscribe/Grade7', endpoint='', handler='SubscribeGrade7.Subscribe'),
         Rule('/Subscribe/Teacher', endpoint='', handler='Subscribe.SubscribeTeacher'),
         Rule('/Subscribe/Practice', endpoint='', handler='Subscribe.SubscribePractice'),
         Rule('/Subscribe/Start', endpoint='', handler='Subscribe.SetExpressCheckout'),
         Rule('/Subscribe/Grade7/Start', endpoint='', handler='SubscribeGrade7.SetExpressCheckout'),
         Rule('/Subscribe/Success', endpoint='', handler='Subscribe.CreateRecurringPaymentsProfile'),
         Rule('/Subscribe/Success/Annual', endpoint='', handler='Subscribe.CreateRecurringPaymentsProfileAnnual'),
         Rule('/Subscribe/Grade7/Success', endpoint='', handler='SubscribeGrade7.DoExpressCheckoutPayment'),
         Rule('/Subscribe/Cancel', endpoint='', handler='Subscribe.CancelTransaction'),
         Rule('/Subscribe/Grade7/Cancel', endpoint='', handler='SubscribeGrade7.CancelTransaction'),
         Rule('/Subscribe/CancelSubscription', endpoint='', handler='Subscribe.CancelSubscription'),
         Rule('/Subscribe/Refund', endpoint='', handler='Subscribe.Refund'),
         Rule('/Subscribe/Trial', endpoint='', handler='Subscribe.SubscriptionTrial'),
         Rule('/Subscribe/EndSubscriptionCheck', endpoint='', handler='Subscribe.EndSubscription'),
         Rule('/Subscribe/HCIPN', endpoint='', handler='Subscribe.HCIPN'),
         Rule('/Subscribe/Manual', endpoint='', handler='Subscribe.ManualSubscription'),
         Rule('/Subscribe/BillOutstandingAmount', endpoint='', handler='Subscribe.BillOutstandingAmount'),
         Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),]

#TEST Parameters
#PAYPAL_USERNAME = 'admin_1354591843_biz_api1.homecampus.com.sg'
#PAYPAL_PASSWORD = '1354591863'
#PAYPAL_SIGNATURE = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AugDOlPVXEmykVDclx-Ft0Z8mhZ.'
#PAYPAL_SIG_URL = 'https://api-3t.sandbox.paypal.com/nvp'
#RETURNURL = 'https://homecampu-dev1-hrd.appspot.com/Subscribe/Success'
#RETURNURLANNUAL = 'https://homecampu-dev1-hrd.appspot.com/Subscribe/Success/Annual'
#CANCELURL = 'https://homecampu-dev1-hrd.appspot.com/Subscribe/Cancel'

#Production Parameters
PAYPAL_USERNAME = 'admin_api1.homecampus.com.sg'
PAYPAL_PASSWORD = 'TKGQJB9T3JUDL9Z2'
PAYPAL_SIGNATURE = 'A9vnkApYSeLAdBbiRdybn9R22.0DAZADhBeYLui-u3-YD0LO5ff47Bzs'
PAYPAL_SIG_URL = 'https://api-3t.paypal.com/nvp'
RETURNURL="https://my.homecampus.com.sg/Subscribe/Success"
RETURNURLANNUAL="https://my.homecampus.com.sg/Subscribe/Success/Annual"
CANCELURL="https://my.homecampus.com.sg/Subscribe/Cancel"
    
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
      
      
class Subscribe(BaseHandler):
    
    def get(self, **kwargs):
        
        if not self.auth.session:
            return self.redirect('/SignIn?continue=%2FSubscribe')
        
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
        
        '''if len(ChildInfo) == 0:
            return self.redirect('/')'''
        
        logging.info(self.auth.user.username)
               
        FeeMessage = random.choice(["<div style='margin-left:30px;padding:5px;'><font style='font-family:calibri;font-size:13px;color:#black;'>This amount keeps Home Campus running.<br>But you can edit the box to pay what it's worth to you.</font></div>"
                                    ])
        
        kwargs.update({'child_info':ChildInfo,
                       'old_user':"YES",
                       'Ideas':"Not used",
                       'CustomerFeedback':random.choice(CustomerFeedback.CustomerFeedback),
                       'fees':float(random.randrange(355,505,10))/100,
                       'FeeMessage':FeeMessage,
                       'annual_amount':4.88,
                       'monthly_amount':8.88,})
        
        return self.render_response('SubscriptionPage.html', **kwargs)
    
class Subscribe50(BaseHandler):
    # this class is same as Subscribe ...only difference is the html page it calls
    def get(self, **kwargs):
        
        if not self.auth.session:
            return self.redirect('/SignIn?continue=%2FSubscribe/xgIPhAi6wFgnqcj')
        
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
        
        '''if len(ChildInfo) == 0:
            return self.redirect('/')'''
        
        logging.info(self.auth.user.username)
               
        FeeMessage = random.choice(["<div style='margin-left:30px;padding:5px;'><font style='font-family:calibri;font-size:13px;color:#black;'>This amount keeps Home Campus running.<br>But you can edit the box to pay what it's worth to you.</font></div>"
                                    ])
        
        kwargs.update({'child_info':ChildInfo,
                       'old_user':"YES",
                       'Ideas':"Not used",
                       'CustomerFeedback':random.choice(CustomerFeedback.CustomerFeedback),
                       'fees':float(random.randrange(355,505,10))/100,
                       'FeeMessage':FeeMessage,
                       'annual_amount':2.44,
                       'monthly_amount':8.88,})
        
        return self.render_response('SubscriptionPage50OFF.html', **kwargs)

    
      
class SubscribeTeacher(BaseHandler):
    
    def get(self, **kwargs):
        
        if not self.auth.session:
            return self.redirect('/Register')
        kwargs.update({})
        
        return self.render_response('SubscriptionPage_Teacher.html', **kwargs)

class SetExpressCheckout(BaseHandler):
    
    def get(self, **kwargs):
        
        amount = self.request.args.get('total_amount')
        username = self.request.args.get('username')
        subscription_period = self.request.args.get('subscription_period')
        if subscription_period == "annual":
            RETURNURL = "https://my.homecampus.com.sg/Subscribe/Success/Annual"
            SubscriptionName = "Home Campus Annual Subscription"
        else:
            RETURNURL = "https://my.homecampus.com.sg/Subscribe/Success"
            SubscriptionName = "Home Campus Subscription"
        # for teacher student_number is how many students are subscribed and this value is passed from the subscribe page
        try:
            student_number = int(self.request.args.get('student_number'))
        except TypeError:
            student_number = 1
        start_date = datetime.datetime.now()
        
        pp = Paypal.PayPal(PAYPAL_USERNAME, PAYPAL_PASSWORD,PAYPAL_SIGNATURE, PAYPAL_SIG_URL)
        ppResponse = pp.SetExpressCheckout(RETURNURL=RETURNURL,
                                     CANCELURL=CANCELURL,
                                     PAYMENTREQUEST_0_CURRENCYCODE="USD",
                                     PAYMENTREQUEST_0_AMT=amount,
                                     PAYMENTREQUEST_0_PAYMENTACTION="Sale",
                                     L_PAYMENTREQUEST_0_ITEMCATEGORY0="Digital",
                                     L_PAYMENTREQUEST_0_NAME0=SubscriptionName,
                                     L_PAYMENTREQUEST_0_QTY0='1',
                                     L_PAYMENTREQUEST_0_AMT0=amount,
                                     L_BILLINGTYPE0="RecurringPayments",
                                     L_BILLINGAGREEMENTDESCRIPTION0="Home Campus Subscription",
                                     )
        logging.info(ppResponse)
        #subscription_period = int(subscription_period)
        end_date = start_date + datetime.timedelta(days = 1)
        HCUser = HomeCampusUser.gql("where username = '"+username+"'").fetch(1)
        PT = HCSubscription.HCSubscription(paypal_token=ppResponse['TOKEN'][0],
                                              student_id=username,
                                              amount=amount,
                                              period=int(1),
                                              start_date = start_date,
                                              end_date=end_date,
                                              status="DUMMY",
                                              email=HCUser[0].email,
                                              student_number=student_number)
        PT.put()
        return ppResponse['TOKEN'][0]
      
'''class DoExpressCheckoutPayment(BaseHandler):
    
    def get(self, **kwargs):
        TOKEN = self.request.args.get('token')
        PAYERID = self.request.args.get('PayerID')
        pp = Paypal.PayPal(PAYPAL_USERNAME, PAYPAL_PASSWORD,PAYPAL_SIGNATURE, PAYPAL_SIG_URL)
        GetECResponse = pp.GetExpressCheckoutDetails(TOKEN=TOKEN)
        CountryCode = GetECResponse['COUNTRYCODE'][0]
        logging.info(GetECResponse)
        ppResponse = pp.DoExpressCheckoutPayment(TOKEN=TOKEN,
                                                 PAYERID=PAYERID,
                                                 PAYMENTREQUEST_0_CURRENCYCODE="USD",
                                                 PAYMENTREQUEST_0_AMT=GetECResponse['PAYMENTREQUEST_0_AMT'][0],
                                                 PAYMENTREQUEST_0_PAYMENTACTION="Sale",
                                                 L_PAYMENTREQUEST_0_ITEMCATEGORY0="Digital",
                                                 L_PAYMENTREQUEST_0_NAME0="Home Campus Subscription",
                                                 L_PAYMENTREQUEST_0_QTY0='1',
                                                 L_PAYMENTREQUEST_0_AMT0=GetECResponse['L_PAYMENTREQUEST_0_AMT0'][0],
                                                 )
        logging.info(ppResponse)
        if ppResponse['ACK'][0] in ["Success","SuccessWithWarning"]:
            TRANS_ID = ppResponse['PAYMENTINFO_0_TRANSACTIONID'][0]
            PayPalFee = ppResponse['PAYMENTINFO_0_FEEAMT'][0]
            self.AuthorizeUser(TOKEN, TRANS_ID, CountryCode, PayPalFee)
            return self.render_response('Success.html')
        else:
            #DeleteSubscription(TOKEN)
            return self.render_response('Cancel.html')'''

class CreateRecurringPaymentsProfile(BaseHandler):
    
    def get(self, **kwargs):
        TOKEN = self.request.args.get('token')
        pp = Paypal.PayPal(PAYPAL_USERNAME, PAYPAL_PASSWORD,PAYPAL_SIGNATURE, PAYPAL_SIG_URL)
        GetECResponse = pp.GetExpressCheckoutDetails(TOKEN=TOKEN)
        CountryCode = GetECResponse['COUNTRYCODE'][0]
        logging.info(GetECResponse)
        # when it's > 16 hrs in UTC time, its already next day in SG and for that reason profilestartdate is less than the current date
        # To overcome this just checking the timestamp of ECResponse and accordingly adjusting the PROFILESTARTDATE        
        PROFILESTARTDATE = datetime.date.today()
        ECTimeStamp =  str(GetECResponse['TIMESTAMP'][0]) #e.g.: 2013-10-20T16:08:06Z
        try:
            ECHour = int(ECTimeStamp.partition('T')[2][:2])
            if ECHour >= 16:
                PROFILESTARTDATE = datetime.date.today()+datetime.timedelta(days = 1)
        except SyntaxError:
            pass

        ppResponse = pp.CreateRecurringPaymentsProfile(TOKEN=TOKEN,
                                                 PROFILESTARTDATE=PROFILESTARTDATE,
                                                 DESC='Home Campus Subscription',
                                                 MAXFAILEDPAYMENTS=3,
                                                 AUTOBILLOUTAMT='NoAutoBill',
                                                 BILLINGPERIOD='Month',
                                                 BILLINGFREQUENCY=1,
                                                 AMT=GetECResponse['PAYMENTREQUEST_0_AMT'][0],
                                                 CURRENCYCODE="USD",
                                                 L_PAYMENTREQUEST_0_ITEMCATEGORY0="Digital",
                                                 L_PAYMENTREQUEST_0_NAME0="Home Campus Subscription",
                                                 L_PAYMENTREQUEST_0_QTY0='1',
                                                 L_PAYMENTREQUEST_0_AMT0=GetECResponse['L_PAYMENTREQUEST_0_AMT0'][0],
                                                 EMAIL=GetECResponse['EMAIL'][0],
                                                 INITAMT='0'
                                                 )
        logging.info(ppResponse)
        if ppResponse['PROFILESTATUS'][0] in ["ActiveProfile"]:
            Profile_ID = ppResponse['PROFILEID'][0]
            self.AuthorizeUser(TOKEN, Profile_ID, CountryCode)
            return self.render_response('Success.html')
        else:
            #DeleteSubscription(TOKEN)
            return self.render_response('Cancel.html')
             
    def AuthorizeUser(self, token, profile_id, CountryCode="", PayPalFee=""):
        UserIDQuery = HCSubscription.HCSubscription.gql("where paypal_token = '"+token+"'")
        UserIDData = UserIDQuery.fetch(1)
        UserIDData[0].profile_id = profile_id
        UserIDData[0].country_code = CountryCode
        #UserIDData[0].paypal_fee = PayPalFee
        UserIDData[0].status = "ACTIVE"
        student_number = UserIDData[0].student_number
        
        ExistingUserQuery = HCSubscription.HCSubscription.gql("where student_id = '"+UserIDData[0].student_id+"' and status = 'ACTIVE'")
        ExistingUserData = ExistingUserQuery.fetch(1)
        
        for e in ExistingUserData:
            if e.status == "ACTIVE":
                e.status = "EXPIRED"
                end_date = UserIDData[0].end_date + (e.end_date - datetime.datetime.now())
                UserIDData[0].end_date = end_date
                e.end_date = datetime.datetime.now()
                e.put()
        
        UserIDData[0].put()

        #this if block for teachers, only for teachers the student is greater than 1
        if student_number > 1:
            UserDataQuery = HomeCampusUser.gql("where username = '"+UserIDData[0].student_id+"' and IsTeacher = True")
            UserData = UserDataQuery.fetch(1)
            UserData[0].authorized = True
            UserData[0].put()
            
            StudentDataQuery = HomeCampusUser.gql("where email = '"+UserData[0].email+"' and IsTeacher = False and authorized = False")
            StudentData = StudentDataQuery.fetch(student_number)
            for s in StudentData:
                s.authorized = True
                s.put()            
            
        else:
            UserDataQuery = HomeCampusUser.gql("where username = '"+UserIDData[0].student_id+"'")
            UserData = UserDataQuery.fetch(1)
            UserData[0].authorized = True
            UserData[0].put()
        

            ParentDataQuery = HomeCampusUser.gql("where email = '"+UserData[0].email+"' and IsParent = True")
            ParentData = ParentDataQuery.fetch(1)
            ParentData[0].authorized = True
            ParentData[0].put()
            
            sendMail(UserData[0].email, UserData[0].parent_first_name, UserData[0].parent_last_name, UserData[0].first_name, UserData[0].last_name, UserData[0].username, "Monthly")

class CreateRecurringPaymentsProfileAnnual(BaseHandler):
    
    def get(self, **kwargs):
        TOKEN = self.request.args.get('token')
        pp = Paypal.PayPal(PAYPAL_USERNAME, PAYPAL_PASSWORD,PAYPAL_SIGNATURE, PAYPAL_SIG_URL)
        GetECResponse = pp.GetExpressCheckoutDetails(TOKEN=TOKEN)
        CountryCode = GetECResponse['COUNTRYCODE'][0]
        logging.info(GetECResponse)
        # when it's > 16 hrs in UTC time, its already next day in SG and for that reason profilestartdate is less than the current date
        # To overcome this just checking the timestamp of ECResponse and accordingly adjusting the PROFILESTARTDATE        
        PROFILESTARTDATE = datetime.date.today()
        ECTimeStamp =  str(GetECResponse['TIMESTAMP'][0]) #e.g.: 2013-10-20T16:08:06Z
        try:
            ECHour = int(ECTimeStamp.partition('T')[2][:2])
            if ECHour >= 16:
                PROFILESTARTDATE = datetime.date.today()+datetime.timedelta(days = 1)
        except SyntaxError:
            pass

        ppResponse = pp.CreateRecurringPaymentsProfile(TOKEN=TOKEN,
                                                 PROFILESTARTDATE=PROFILESTARTDATE,
                                                 DESC='Home Campus Subscription',
                                                 MAXFAILEDPAYMENTS=3,
                                                 AUTOBILLOUTAMT='NoAutoBill',
                                                 BILLINGPERIOD='Year',
                                                 BILLINGFREQUENCY=1,
                                                 AMT=GetECResponse['PAYMENTREQUEST_0_AMT'][0],
                                                 CURRENCYCODE="USD",
                                                 L_PAYMENTREQUEST_0_ITEMCATEGORY0="Digital",
                                                 L_PAYMENTREQUEST_0_NAME0="Home Campus Subscription",
                                                 L_PAYMENTREQUEST_0_QTY0='1',
                                                 L_PAYMENTREQUEST_0_AMT0=GetECResponse['L_PAYMENTREQUEST_0_AMT0'][0],
                                                 EMAIL=GetECResponse['EMAIL'][0],
                                                 INITAMT='0'
                                                 )
        logging.info(ppResponse)
        if ppResponse['PROFILESTATUS'][0] in ["ActiveProfile"]:
            Profile_ID = ppResponse['PROFILEID'][0]
            self.AuthorizeUser(TOKEN, Profile_ID, CountryCode)
            return self.render_response('Success.html')
        else:
            #DeleteSubscription(TOKEN)
            return self.render_response('Cancel.html')
             
    def AuthorizeUser(self, token, profile_id, CountryCode="", PayPalFee=""):
        UserIDQuery = HCSubscription.HCSubscription.gql("where paypal_token = '"+token+"'")
        UserIDData = UserIDQuery.fetch(1)
        UserIDData[0].profile_id = profile_id
        UserIDData[0].country_code = CountryCode
        #UserIDData[0].paypal_fee = PayPalFee
        UserIDData[0].status = "ACTIVE"
        UserIDData[0].period = 12
        student_number = UserIDData[0].student_number
        
        ExistingUserQuery = HCSubscription.HCSubscription.gql("where student_id = '"+UserIDData[0].student_id+"' and status = 'ACTIVE'")
        ExistingUserData = ExistingUserQuery.fetch(1)
        
        for e in ExistingUserData:
            if e.status == "ACTIVE":
                e.status = "EXPIRED"
                end_date = UserIDData[0].end_date + (e.end_date - datetime.datetime.now())
                UserIDData[0].end_date = end_date
                e.end_date = datetime.datetime.now()
                e.put()
        
        UserIDData[0].put()

        #this if block for teachers, only for teachers the student is greater than 1
        if student_number > 1:
            UserDataQuery = HomeCampusUser.gql("where username = '"+UserIDData[0].student_id+"' and IsTeacher = True")
            UserData = UserDataQuery.fetch(1)
            UserData[0].authorized = True
            UserData[0].put()
            
            StudentDataQuery = HomeCampusUser.gql("where email = '"+UserData[0].email+"' and IsTeacher = False and authorized = False")
            StudentData = StudentDataQuery.fetch(student_number)
            for s in StudentData:
                s.authorized = True
                s.put()            
            
        else:
            UserDataQuery = HomeCampusUser.gql("where username = '"+UserIDData[0].student_id+"'")
            UserData = UserDataQuery.fetch(1)
            UserData[0].authorized = True
            UserData[0].put()
        

            ParentDataQuery = HomeCampusUser.gql("where email = '"+UserData[0].email+"' and IsParent = True")
            ParentData = ParentDataQuery.fetch(1)
            ParentData[0].authorized = True
            ParentData[0].put()
            
            sendMail(UserData[0].email, UserData[0].parent_first_name, UserData[0].parent_last_name, UserData[0].first_name, UserData[0].last_name, UserData[0].username, "Annually")
        
        
    
class HCIPN(BaseHandler):
    def post(self):
        params = self.request.form.copy()
        encoded_params = 'cmd=_notify-validate&'+urlencode(params)
        logging.info(params)
        try:
            #checking the data only for payment IPN and cancel subscription
            if params['txn_type'] == "recurring_payment":
                if self.VerifyIPNData(encoded_params,params):
                    logging.info("IPN Message Verified:")
                    self.SavePaymentInfo(params)
                else:
                    logging.info("incorrect IPN Message:")
            # update the status to CANCELLED and it will auto cancel on end date
            if params['txn_type'] == "recurring_payment_profile_cancel":
                if self.VerifyIPNData2(encoded_params,params):
                    logging.info("IPN Message Verified:")
                    self.InactiveSubscription(params)
                else:
                    logging.info("incorrect IPN Message:")
            # update the end date when payment is skipped to keep the account ACTIVE for next five days
            if params['txn_type'] == "recurring_payment_skipped":
                if self.VerifyIPNData2(encoded_params,params):
                    logging.info("IPN Message Verified:")
                    #self.ChangeEndDate(params)
                    self.SuspendAccount(params)
                else:
                    logging.info("incorrect IPN Message:")
        except KeyError:
            pass

        '''sending a blank response with code 200 to PayPal so it stops sending IPN message'''
        response = Response("")
        response.status_code = 200
        return response
    
    def VerifyIPNData(self,encoded_params,params):
        Verified = False
        status = urlfetch.fetch(
                     url = "https://www.paypal.com/cgi-bin/webscr",
                     method = urlfetch.POST,  
                     payload = encoded_params,
                    ).content
        if status == "VERIFIED" and params['receiver_id']=="VGPSLFH4UAY5U" and params['receiver_email']=="admin@homecampus.com.sg":
            Verified = True
        
        return Verified
    
    '''recurring_payment_profile_cancel doesn't have receiver id'''
    def VerifyIPNData2(self,encoded_params,params):
        Verified = False
        status = urlfetch.fetch(
                     url = "https://www.paypal.com/cgi-bin/webscr",
                     method = urlfetch.POST,  
                     payload = encoded_params,
                    ).content
        if status == "VERIFIED" and params['receiver_email']=="admin@homecampus.com.sg":
            Verified = True
        
        return Verified
    
    def SavePaymentInfo(self,params):
        '''original next payment date is in unicode u'03:00:00 Aug 23, 2013 PDT'..stripping it and making it datetime'''
        end_date = datetime.datetime.strptime(params['next_payment_date'][:-4],'%H:%M:%S %b %d, %Y') + datetime.timedelta(days = 2)
        HCSubscriptionData = HCSubscription.HCSubscription.gql("where profile_id = '"+params['recurring_payment_id']+"'").fetch(1)
        amount = HCSubscriptionData[0].amount
        PaymentData = HCPayment.HCPayment.gql("where transaction_id='"+params['txn_id']+"'").fetch(1)
        '''Payment to be processed if received completed payment first time...ignore if it is received multiple times'''
        ProcessPayment = False
        if not PaymentData:
            PaymentData = HCPayment.HCPayment(transaction_id=params['txn_id'],
                                              transaction_type=params['txn_type'],
                                              payer_email=params['payer_email'],
                                              next_payment_date=datetime.datetime.strptime(params['next_payment_date'][:-4],'%H:%M:%S %b %d, %Y'),
                                              payer_id=params['payer_id'],
                                              recurring_payment_id=params['recurring_payment_id'],
                                              payment_status=params['payment_status'],
                                              amount=params['mc_gross'],
                                              payment_date=datetime.datetime.strptime(params['payment_date'][:-4],'%H:%M:%S %b %d, %Y')
                                              )
            '''Only completed status has paypal fee'''
            if params['payment_status'] == "Completed":
                PaymentData.paypal_fee=params['mc_fee']
            PaymentData.put()
            ProcessPayment = True
        else:
            if not PaymentData[0].payment_status == params['payment_status']:
                PaymentData[0].payment_status = params['payment_status']
                '''Only completed status has paypal fee'''
                if params['payment_status'] == "Completed":
                    PaymentData[0].paypal_fee=params['mc_fee']
                PaymentData[0].put()
                ProcessPayment = True
        
        #process if only payment_status == "Completed" and amount is what agreed
        if ProcessPayment:
            if params['payment_status']=="Completed" and float(params['mc_gross'])>=float(amount):
                HCSubscriptionData[0].end_date = end_date
                HCSubscriptionData[0].status = 'ACTIVE'
                HCSubscriptionData[0].put()
                #Making sure child and parent account is authorized
                UserDataQuery = HomeCampusUser.gql("where username = '"+HCSubscriptionData[0].student_id+"'")
                UserData = UserDataQuery.fetch(1)
                if not UserData[0].authorized:
                    UserData[0].authorized = True
                    UserData[0].put()
        
                ParentDataQuery = HomeCampusUser.gql("where email = '"+HCSubscriptionData[0].email+"' and IsParent = True")
                ParentData = ParentDataQuery.fetch(1)
                if not ParentData[0].authorized:
                    ParentData[0].authorized = True
                    ParentData[0].put()        

    def InactiveSubscription(self, params):
        logging.info("Cancelling user profile in HCSubscription...")
        HCSubscriptionQuery = HCSubscription.HCSubscription.gql("where profile_id = '"+params['recurring_payment_id']+"'")
        HCSubscriptionData = HCSubscriptionQuery.fetch(1)
        HCSubscriptionData[0].status = "CANCELLED"
        HCSubscriptionData[0].put()
        logging.info("User profile cancelled...")

    def ChangeEndDate(self, params):
        logging.info("Payment skipped...changing end date")
        HCSubscriptionQuery = HCSubscription.HCSubscription.gql("where profile_id = '"+params['recurring_payment_id']+"'")
        HCSubscriptionData = HCSubscriptionQuery.fetch(1)
        end_date = HCSubscriptionData[0].end_date + datetime.timedelta(days = 5)
        HCSubscriptionData[0].end_date = end_date
        HCSubscriptionData[0].put()      

    def SuspendAccount(self, params):
        logging.info("Payment skipped...suspending account")
        HCSubscriptionQuery = HCSubscription.HCSubscription.gql("where profile_id = '"+params['recurring_payment_id']+"'")
        HCSubscriptionData = HCSubscriptionQuery.fetch(1)
        '''not changing the status as user can't cancel if status changed to SUSPENDED'''
        '''
        for h in HCSubscriptionData:
            #end_date is changed only for the 1st payment skip
            if h.status != "SUSPENDED":
                h.end_date = datetime.datetime.now()
                h.status = "SUSPENDED"
                h.put()'''

        #child and parent account are de-authorized
        UserDataQuery = HomeCampusUser.gql("where username = '"+HCSubscriptionData[0].student_id+"'")
        UserData = UserDataQuery.fetch(1)
        UserData[0].authorized = False
        UserData[0].put()

        #before suspending parent account making sure that there are no other ACTIVE child account associated with this parent.
        NoActiveChild = True
        ChildData = HomeCampusUser.gql("where email = '"+HCSubscriptionData[0].email+"' and IsParent = False").fetch(10)
        for c in ChildData:
            if c.authorized and c.username!=HCSubscriptionData[0].student_id:
                NoActiveChild = False
        
        if NoActiveChild:
            ParentDataQuery = HomeCampusUser.gql("where email = '"+HCSubscriptionData[0].email+"' and IsParent = True")
            ParentData = ParentDataQuery.fetch(1)
            ParentData[0].authorized = False
            ParentData[0].put()  
                                   
class CancelTransaction(BaseHandler):

    def get(self, **kwargs):
        return self.render_response('Cancel.html')

class CancelSubscription(BaseHandler):
   
    @login_required
    def get(self, **kwargs):
        
        if not self.auth.user or (self.auth.user and not self.auth.user.IsParent):
            return self.redirect("/")
        
        ChildInfo = []

        ParentQuery = HomeCampusUser.gql("where username = '"+self.auth.user.username+"'")
        ParentData = ParentQuery.fetch(1)
        
        StudentQuery = HomeCampusUser.gql("where email = '"+ParentData[0].email+"' and IsParent = False and authorized = True")
        StudentData = StudentQuery.fetch(5)
        '''Student should be authorized in HomeCampusUser table and active in HCSubscription table with a paypal profile_id'''
        for s in StudentData:
            ActiveStudentQuery = HCSubscription.HCSubscription.gql("where student_id = '"+s.username+"' and status = 'ACTIVE'")
            ActiveStudentData = ActiveStudentQuery.fetch(1)
            for a in ActiveStudentData:
                if a.profile_id is not None:
                    ChildInfo.append([s.first_name,s.username])
        
        logging.info(self.auth.user.username)
               
        kwargs.update({'child_info':ChildInfo,
                       })                  
        return self.render_response('CancelSubscription.html', **kwargs)

    def post(self, **kwargs):
        user_id = self.request.form.get('user_id')
        logging.info(user_id)
        HCSubscriptionQuery = HCSubscription.HCSubscription.gql("where student_id = '"+user_id+"' and status = 'ACTIVE'")
        HCSubscriptionData = HCSubscriptionQuery.fetch(1)
        try:
            profile_id = HCSubscriptionData[0].profile_id
        except IndexError:
            kwargs.update({'child_not_subscribed':"Y",})
            return self.get(**kwargs)
        pp = Paypal.PayPal(PAYPAL_USERNAME, PAYPAL_PASSWORD,PAYPAL_SIGNATURE, PAYPAL_SIG_URL)
        ppResponse = pp.ManageRecurringPaymentsProfileStatus(PROFILEID=profile_id,
                                                             ACTION='Cancel',
                                                             NOTE='Your subscription for user '+str(user_id)+' has been cancelled.'
                                                             )
        logging.info(ppResponse)
        if ppResponse['ACK'][0] in ["Success","SuccessWithWarning"]:
            self.DeAuthorzie(user_id,profile_id)
        
        kwargs.update({'cancelled':"Y",
                       })             
        return self.get(**kwargs)

    def DeAuthorzie(self, user_id, profile_id):
        HCSubscriptionQuery = HCSubscription.HCSubscription.gql("where profile_id = '"+profile_id+"'")
        HCSubscriptionData = HCSubscriptionQuery.fetch(1)
        HCSubscriptionData[0].status = "CANCELLED"
        HCSubscriptionData[0].put()
       
class Refund(BaseHandler):
   
    @admin_required
    def get(self, **kwargs):           
        return self.render_response('Refund.html', **kwargs)
    
    @admin_required
    def post(self, **kwargs):
        user_id = self.request.form.get('user_id')
        transaction_id = self.request.form.get('trans_id')
        refund_type = self.request.form.get('refund_type')
        amount = self.request.form.get('amount')
        note = self.request.form.get('note')

        pp = Paypal.PayPal(PAYPAL_USERNAME, PAYPAL_PASSWORD,PAYPAL_SIGNATURE, PAYPAL_SIG_URL)
        ppResponse = pp.RefundTransaction(TRANSACTIONID=transaction_id,
                                          REFUNDTYPE=refund_type,
                                          AMT=amount,
                                          CURRENCYCODE='USD',
                                          NOTE=note
                                                 )
        logging.info(ppResponse)
        if ppResponse['ACK'][0] in ["Success","SuccessWithWarning"]:
            self.DeAuthorzie(user_id,transaction_id)
        return self.get(**kwargs)

    def DeAuthorzie(self, user_id, transaction_id):
        
        DeAuthorizeChild(user_id)

        HCSubscriptionQuery = HCSubscription.HCSubscription.gql("where transaction_id = '"+transaction_id+"'")
        HCSubscriptionData = HCSubscriptionQuery.fetch(1)
        HCSubscriptionData[0].status = "REFUND"
        HCSubscriptionData[0].end_date = datetime.datetime.now()
        HCSubscriptionData[0].put()
        
        #Deauthorize parent as well if no child is authorized
        DeAuthorizeParent(user_id)
    
class SubscriptionTrial(BaseHandler):
    #30-APR-2013: Will not be used going forward
    def get(self, **kwargs):
        
        # This if for account created between  last two
        '''create_date = datetime.datetime.now() + datetime.timedelta(days = -2)
        DateString = str(create_date.year)+"-"+str(create_date.month)+"-"+str(create_date.day)

        create_date1 = datetime.datetime.now() + datetime.timedelta(minutes = -60)
        DateString1 = str(create_date1.year)+"-"+str(create_date1.month)+"-"+str(create_date1.day)+" "+str(create_date1.hour)+":"+str(create_date1.minute)+":"+str(create_date1.second)

        
        HCUser = HomeCampusUser.gql("where created > DATE('"+DateString+"') and created < DATETIME('"+DateString1+"') and IsParent = False")
        start_date = datetime.datetime.now()
        end_date = start_date + datetime.timedelta(days = 7)
        for u in HCUser:
            HCSubscriptionQuery = HCSubscription.HCSubscription.gql("where student_id ='"+u.username+"' and status='ACTIVE'")
            HCSubscriptionData = HCSubscriptionQuery.fetch(1)
            if not HCSubscriptionData:               
                PT = HCSubscription.HCSubscription(paypal_token='TRIAL',
                                                  student_id=u.username,
                                                  amount='0',
                                                  period=0,
                                                  start_date=start_date,
                                                  end_date=end_date,
                                                  status="ACTIVE",
                                                  email=u.email)
                PT.put()
                
                u.authorized = True
                u.put()
                HCParentUser = HomeCampusUser.gql("where email = '"+u.email+"' and IsParent = True and authorized = False").fetch(1)
                for h in HCParentUser:
                    h.authorized = True
                    h.put()
                    self.sendMail(u.email, h.first_name, h.last_name, u.username)
                    logging.info("Trial subscription was send to "+u.first_name)'''
            
        return self.redirect("/")
    
    def sendMail(self, email, first_name, last_name, username):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Your FREE Trial of Maths at Home Campus!!"
        SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
        SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(https://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="https://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">'
        SendMessage = SendMessage + 'Dear '+first_name+' '+last_name+','
        SendMessage = SendMessage + '<br /><br />Congratulations on your new registration to Home Campus!<br /><br />To help your child excel in math, you are invited to try Home Campus <font color="#D92118"><b>completely FREE of charge</b></font> for the next 7 days. So, <a href="https://my.homecampus.com.sg/SignIn"><font color="#0E820E">log in</font></a> and start using.<br /><br /><b><u>Registration details</u>:</b><br />'
        SendMessage = SendMessage + 'Parent username: '+email+'<br />Child username: '+username+'<br /><br />'
        SendMessage = SendMessage + 'To start off, here\'s what you might like to check out:<br /></p><ul><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="https://my.homecampus.com.sg/Learn"><font color="#D92118"><b>Watch and Learn</b></font></a><br />Watch video lessons or read notes that are broken into bite-sized pieces</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="https://my.homecampus.com.sg/Practice"><font color="#2A91E1"><b>Unlimited Practice</b></font></a><br />Solve from a pool of unlimited questions with detailed step-by-step solutions</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="https://my.homecampus.com.sg/Elementary_Mathematics_Worksheets"><font color="#0E820E"><b>Worksheets on All Topics</b></font></a><br />Solve as many worksheets as you like to check your knowledge</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="https://my.homecampus.com.sg/Progress"><font color="#F6B937"><b>Monitor Progress</b></font></a><br />Identify areas of strengths and weaknesses through graphs, charts and reports</p></li></ul><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">This and much more await you. The best part is you get to decide to pay what you feel your education is worth.<br /><br />So, go ahead, explore and top math!!<br /><br /><p style="text-align:left; font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">Yours sincerely,<br />Team @ Home Campus<br /><strong><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></strong><br /><b><a href="https://my.homecampus.com.sg"><font color="#006666">www.homecampus.com.sg</font></a></b></p></td></tr></table></td></tr></tbody></table></div></td></tr></tbody></table>'
        message.html = SendMessage
        
        message.Send() 
                
class EndSubscription(BaseHandler):
   
    def get(self, **kwargs):
        
        expiry_date = datetime.datetime.now()
        DateString = str(expiry_date.year)+"-"+str(expiry_date.month)+"-"+str(expiry_date.day)
        HCSubscriptionACTIVE = HCSubscription.HCSubscription.gql("where end_date < Date('"+DateString+"') and status='ACTIVE'").fetch(100)
        HCSubscriptionCANCELLED = HCSubscription.HCSubscription.gql("where end_date < Date('"+DateString+"') and status='CANCELLED'").fetch(100)
        HCSubscriptionData = HCSubscriptionACTIVE + HCSubscriptionCANCELLED
        for h in HCSubscriptionData:
            h.status = "EXPIRED"
            DeAuthorizeChild(h.student_id)
            logging.info(h.student_id+" subscription expired")
            '''25 Apr 2013: This call has been moved to DeAuthorizechild function as some parent were not getting deauthorized'''
            #DeAuthorizeParent(h.student_id)
            h.put()
        if not HCSubscriptionData:
            logging.info("No subscription expired today!!")
        response = Response("")
        response.status_code = 200
        return response

class BillOutstandingAmount(BaseHandler):
    
    def get(self, **kwargs):
        
        pp = Paypal.PayPal(PAYPAL_USERNAME, PAYPAL_PASSWORD,PAYPAL_SIGNATURE, PAYPAL_SIG_URL)
        '''only checking for past 25 days payment skip..ignoring the older ones'''
        check_date = datetime.datetime.now() + datetime.timedelta(days=-25)
        DateString = str(check_date.year)+"-"+str(check_date.month)+"-"+str(check_date.day)
        HCSubscriptionSUSPENDED = HCSubscription.HCSubscription.gql("where end_date > Date('"+DateString+"') and status='SUSPENDED'").fetch(100)
        for h in HCSubscriptionSUSPENDED:
            ppResponse = pp.BillOutstandingAmount(PROFILEID=h.profile_id)
            logging.info(ppResponse)
        response = Response("")
        response.status_code = 200
        return response       

                
def DeleteSubscription(token):
    UserIDQuery = HCSubscription.HCSubscription.gql("where paypal_token = '"+token+"'")
    UserIDData = UserIDQuery.fetch(1)
    
    try:
        UserIDData[0].delete()
    except IndexError:
        None 
        
def DeAuthorizeChild(student_id):
    UserDataQuery = HomeCampusUser.gql("where username = '"+student_id+"'")
    UserData = UserDataQuery.fetch(1)
    UserData[0].authorized = False
    UserData[0].put()
    DeAuthorizeParent(student_id)
    
def DeAuthorizeParent(student_id):                     
    
    UserDataQuery = HomeCampusUser.gql("where username = '"+student_id+"'")
    UserData = UserDataQuery.fetch(1)
    email = UserData[0].email
    
    ParentAuthorize = False
    ChildrenDataQuery = HomeCampusUser.gql("where email = '"+email+"' and IsParent = False")
    ChildrenData = ChildrenDataQuery.fetch(1000)
    for c in ChildrenData:
        if c.authorized:
            #atleast one children is authorized
            ParentAuthorize = True
            
    if not ParentAuthorize:
        ParentDataQuery = HomeCampusUser.gql("where email = '"+email+"' and IsParent = True")
        ParentData = ParentDataQuery.fetch(1)
        ParentData[0].authorized = False
        ParentData[0].put()

    
'''class SubscriptionBulkTrial(BaseHandler):
    
    def get(self, **kwargs):
        
        date1 = str(self.request.args.get('start_date'))
        date2 = str(self.request.args.get('end_date'))
        # This if for account created between  last two
        
        HCParent = HomeCampusUser.gql("where created > DATE('"+date1+"') and created < DATE('"+date2+"') and IsParent = True")
        start_date = datetime.datetime.now()
        end_date = start_date + datetime.timedelta(days = 14)
        i = 0
        for p in HCParent:
            i = i + 1
            if not p.authorized:
                HCChild = HomeCampusUser.gql("where email = '"+p.email+"' and IsParent = False and authorized = False").fetch(1)
                for c in HCChild:
                    username = c.username
                    PT = HCSubscription.HCSubscription(paypal_token='TRIAL',
                                                      student_id=c.username,
                                                      amount='0',
                                                      period=0,
                                                      start_date=start_date,
                                                      end_date=end_date,
                                                      status="ACTIVE",
                                                      email=p.email)
                    PT.put()
                    c.authorized = True
                    c.put()
                    
                    p.authorized = True
                    p.put()
                    self.sendMail(p.email, p.first_name, p.last_name, username)

                    logging.info("Trial subscription was send to "+p.first_name)
        logging.info("Total Parent registration = "+str(i))
            
        return self.redirect("/")
    
    def sendMail(self, email, first_name, last_name, username):
        message = mail.EmailMessage()
        message.to = email

        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Your Ticket to a Mathemagical Journey"
        SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
        SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(https://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="https://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">'
        SendMessage = SendMessage + 'Hello '+first_name+' '+last_name+','
        SendMessage = SendMessage + '<br /><br />It has been a while since we saw you at Home Campus, your portable <b>School of Elementary Mathematics</b>. It would delight you to see how much the site has transformed since then. Come <a href="https://www.homecampus.com.sg" alt="check out the all new Home Campus" title="check out the all new Home Campus"><font color="#0E820E">check out</font></a> all of its features for <b>FREE</b> for the <u>next 14 days</u>.<br><br>Here\'s your user info for quick reference:<br><br>'
        SendMessage = SendMessage + 'Parent id: '+email+'<br />Child id: '+username+'<br /><br />'
        SendMessage = SendMessage + 'Following is a gist of some of the stuff you might like to check out:<br /></p><ul><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="https://my.homecampus.com.sg/Learn"><font color="#D92118"><b>Watch and Learn</b></font></a><br />Watch video lessons or read pictorial notes that are broken into bite-sized pieces</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="https://my.homecampus.com.sg/Practice"><font color="#2A91E1"><b>Unlimited Practice</b></font></a><br />Solve from a pool of unlimited questions with detailed step-by-step solutions. Topics include Algebra, Whole Numbers, Fractions, Decimals, Percentage, Ratio, Time, Money, Measurement, Speed, Geometry, Average, Graphs, Charts, and many more.</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="https://my.homecampus.com.sg/Tests"><font color="#0E820E"><b>Create your Tests</b></font></a><br />Take unique topical tests that you can create yourself to check your knowledge</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="https://my.homecampus.com.sg/Progress"><font color="#F6B937"><b>Monitor Progress</b></font></a><br />Identify areas of strengths and weaknesses of your child through graphs, charts and reports</p></li></ul><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">This and much more await you. So, go ahead, explore and top math!!<br /><br /><p style="text-align:left; font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">Yours sincerely,<br />Team @ Home Campus<br /><strong><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></strong><br /><b><a href="https://my.homecampus.com.sg"><font color="#006666">www.homecampus.com.sg</font></a></b></p></td></tr></table></td></tr></tbody></table></div></td></tr></tbody></table>'

        message.html = SendMessage
        
        message.Send() 
'''

class ManualSubscription(BaseHandler):
   
    @admin_required
    def get(self, **kwargs):           
        return self.render_response('ManualSubscription.html', **kwargs)
    
    @admin_required
    def post(self, **kwargs):
        email = self.request.form.get('email')
        child_username = self.request.form.get('username')
        period = self.request.form.get('period')
        self.AuthorizeUser(email,child_username, period)

        return self.get(**kwargs)
          
    def AuthorizeUser(self, email, child_username, period):

        UserDataQuery = HomeCampusUser.gql("where email = '"+email+"' and IsParent = True")
        UserData = UserDataQuery.fetch(1)
        first_name = ""
        last_name = ""
        for d in UserData:
            d.authorized = True
            first_name = d.first_name
            last_name = d.last_name
            d.put()      
        
        ChildData = HomeCampusUser.gql("where username = '"+child_username+"'").fetch(1)       
        child_first_name = ""
        child_last_name = ""
        
        for c in ChildData:
            c.authorized = True
            child_first_name = c.first_name
            child_last_name = c.last_name
            c.put()

        logging.info(child_username)
        self.CreateHCSubscription(period, child_username, email)
        #sendMail(email, first_name,last_name,child_first_name,child_last_name,child_username)
            
        
    def CreateHCSubscription(self, period, username,email):
        start_date = datetime.datetime.now()
        end_date = start_date + datetime.timedelta(days = int(period))
        ExistingUserQuery = HCSubscription.HCSubscription.gql("where student_id = '"+username+"' and status = 'ACTIVE'")
        ExistingUserData = ExistingUserQuery.fetch(1)
            
        for e in ExistingUserData:
            if e.status == "ACTIVE":
                e.status = "EXPIRED"
                end_date = end_date + (e.end_date - datetime.datetime.now())
                e.end_date = datetime.datetime.now()
                e.put()
                
        PT = HCSubscription.HCSubscription(paypal_token='MANUAL',
                                          student_id=username,
                                          amount='0',
                                          period=int('1'),
                                          start_date=start_date,
                                          end_date=end_date,
                                          status="ACTIVE",
                                          email=email,
                                          student_number=1)
        PT.put()

def sendMail(email, first_name, last_name, child_first_name, child_last_name, username, period):
    message = mail.EmailMessage()
    message.to = email
    message.bcc = 'admin@homecampus.com.sg'
    message.sender = "Home Campus <admin@homecampus.com.sg>"
    message.subject = "Welcome to Home Campus!!"
    SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
    SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(https://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="https://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">'
    SendMessage = SendMessage + 'Dear '+first_name+' '+last_name+','
    SendMessage = SendMessage + '<br /><br />Thanks for your subscription to Home Campus!<br /><br />We hope you and your child will have a fun experience learning maths at Home Campus. So, <a href="https://my.homecampus.com.sg/SignIn"><font color="#0E820E">log in</font></a> and start using.<br /><br /><b><u>Registration details</u>:</b><br />'
    SendMessage = SendMessage + 'Parent username: '+email+'<br />Child username: '+username+'<br /><br />'
    SendMessage = SendMessage + 'To start off, here\'s what you might like to check out:<br /></p><ul><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="https://my.homecampus.com.sg"><font color="#D92118"><b>Watch and Learn</b></font></a><br />Watch video lessons or read notes that are broken into bite-sized pieces</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="https://my.homecampus.com.sg"><font color="#2A91E1"><b>Unlimited Practice</b></font></a><br />Solve from a pool of unlimited questions with detailed step-by-step solutions</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="https://my.homecampus.com.sg"><font color="#0E820E"><b>Worksheets on All Topics</b></font></a><br />Solve as many worksheets you like to check your knowledge</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="https://my.homecampus.com.sg/Progress"><font color="#F6B937"><b>Monitor Progress</b></font></a><br />Identify areas of strengths and weaknesses through graphs, charts and reports</p></li></ul><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">This and much more await you.<br /><br />So, go ahead, explore and top math!!<br />'
    if period == "Monthly":
        SendMessage = SendMessage + '<p style="text-align:left; font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">You will be automatically billed monthly. You can cancel it anytime at MyProfile page under Parent\'s login.</p><br><br>'
    else:
        SendMessage = SendMessage + '<p style="text-align:left; font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">You will be automatically billed annually. You can cancel it anytime at MyProfile page under Parent\'s login.</p><br><br>'
    SendMessage = SendMessage + '<p style="text-align:left; font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">Yours sincerely,<br />Team @ Home Campus<br /><strong><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></strong><br /><b><a href="https://my.homecampus.com.sg"><font color="#006666">www.homecampus.com.sg</font></a></b></p></td></tr></table></td></tr></tbody></table></div></td></tr></tbody></table>'
    
    message.html = SendMessage
    message.Send()
               
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()