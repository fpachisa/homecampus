from werkzeug.utils import cached_property

from tipfy import RequestHandler
from tipfy.auth import (login_required, user_required,
    UserRequiredIfAuthenticatedMiddleware, practice_login_required)
from tipfy.sessions import SessionMiddleware
from tipfy.utils import json_encode
from tipfyext.jinja2 import Jinja2Mixin
from tipfyext.wtforms import Form, fields, validators
from Models import HomeCampusUser
from google.appengine.api import mail
from google.appengine.runtime import DeadlineExceededError
import logging
import time
import Ideas
import CustomerFeedback
import random
from Database import HCSchoolInfo

# ----- Forms -----

REQUIRED = validators.required()

    
# ----- Handlers -----

class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]

    @cached_property
    def messages(self):
        """A list of status messages to be displayed to the user."""
        return self.session.get_flashes(key='_messages')

    def render_response(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session

        kwargs.update({
            'auth_session': auth_session,
            'current_user': self.auth.user,
            'login_url':    self.auth.login_url(),
            'logout_url':   self.auth.logout_url(),
            'current_url':  self.request.url,
        })
        if self.messages:
            kwargs['messages'] = json_encode([dict(body=body, level=level)
                for body, level in self.messages])

        return super(BaseHandler, self).render_response(filename, **kwargs)

    def redirect_path(self, default='/'):
        if '_continue' in self.session:
            url = self.session.pop('_continue')
        else:
            url = self.request.args.get('continue', '/')

        if not url.startswith('/'):
            url = default
        return url

    def _on_auth_redirect(self):
        """Redirects after successful authentication using third party
        services.
        """
        if '_continue' in self.session:
            url = self.session.pop('_continue')
        else:
            url = '/'

        if not self.auth.user:
            url = self.auth.signup_url()

        return self.redirect(url)

class PracticeLoginHandler(BaseHandler):
    def get(self, **kwargs):

        if self.auth.user:
            # User is already registered, so don't display the signup form.
            return self.redirect(self.redirect_path())
        
        if self.session.get('login_error'):
            login_error = self.session.get('login_error')
            del self.session['login_error']
            context = {
                #'form':self.form,
                'login_error':login_error,
            }
            template = "LoginPage.html"
        else:
            context = {
                #'form':self.form
            }
            template = "LoginPage.html"            
        return self.render_response(template, **context)

    def post(self, **kwargs):
        redirect_url = self.redirect_path()

        if self.auth.user:
            # User is already registered, so don't display the signup form.
            return self.redirect(redirect_url)


        username = self.request.form.get('username')
        password = self.request.form.get('password')

        res = self.auth.login_with_form(username, password)
        if res:
            return self.redirect(redirect_url)
        
        self.session['login_error'] = 'Either username or password is incorrect. Please try again.'
        return self.get(**kwargs)


class LoginHandler(BaseHandler):
    def get(self, **kwargs):
        redirect_url = self.redirect_path()

        if self.auth.user:
            # User is already registered, so don't display the signup form.
            # 30-APR-2013: After login we don't show subscribe page 
            '''if self.auth.user.authorized:
                return self.redirect(redirect_url)
            else:
                return self.redirect("/Subscribe")'''
            return self.redirect(redirect_url)
        
        if self.session.get('login_error'):
            login_error = self.session.get('login_error')
            del self.session['login_error']
            context = {
                #'form':self.form,
                'login_error':login_error
            }
        else:
            context = {
                #'form':self.form
            }            
        return self.render_response('LoginPage.html', **context)

    def post(self, **kwargs):
        redirect_url = self.redirect_path()
        
        if self.auth.user:
            # User is already registered, so don't display the signup form.
            # 30-APR-2013: After login we don't show subscribe page 
            '''if self.auth.user.authorized:
                return self.redirect(redirect_url)
            else:
                return self.redirect("/Subscribe")'''
            return self.redirect(redirect_url)
            
        username = self.request.form.get('username')
        password = self.request.form.get('password')

        res = self.auth.login_with_form(username, password)

        if res:
            # 30-APR-2013: After login we don't show subscribe page 
            '''if self.auth.user.authorized:
                return self.redirect(redirect_url)
            else:
                return self.redirect("/Subscribe")'''
            return self.redirect(redirect_url)
        

        self.session['login_error'] = 'Either username or password is incorrect. Please try again.'
        return self.get(**kwargs)

class LogoutHandler(BaseHandler):
    def get(self, **kwargs):
        self.auth.logout()
        #return self.redirect(self.redirect_path())
        #after logout redirect to homepage
        return self.redirect("/")
    
class RegisterHandler(BaseHandler):
    def get(self, **kwargs):
        redirect_url = self.redirect_path()

        if self.auth.user:
            # User is already registered, and is not a parent so don't display the registration form.
            # 30-APR-2013: After login we don't show subscribe page 
            '''if self.auth.user.authorized:
                return self.redirect(redirect_url)
            else:
                return self.redirect("/Subscribe")'''
            return self.redirect(redirect_url)
            
        if self.session.get('registration_message'):
            registration_message = self.session.get('registration_message')
            del self.session['registration_message']
            kwargs.update({
                       'registration_messages':registration_message
                       })
        return self.render_response('RegisterPage.html', **kwargs)

    def post(self, **kwargs):
        redirect_url = self.redirect_path()

        if self.auth.user:
            # User is already registered, so don't process the signup form.
            return self.redirect(redirect_url)
        
        registration_message = ""
        parent_first_name = self.request.form.get('parent_first_name')
        parent_last_name = self.request.form.get('parent_last_name')
        email = self.request.form.get('email')
        parent_password = self.request.form.get('parent_password')
        child_first_name = self.request.form.get('child_first_name')
        child_last_name = self.request.form.get('child_last_name')
        child_skill = self.request.form.get('skill_grade')
        username = self.request.form.get('username')
        child_password = self.request.form.get('child_password')

        kwargs.update({'parent_first_name':parent_first_name,
                       'parent_last_name':parent_last_name,
                       'email':email,
                       'child_first_name':child_first_name,
                       'child_last_name':child_last_name,
                       'child_skill':child_skill,
                       'username':username,
                       'child_info':[[child_first_name,username]],
                       'Ideas':Ideas.GenerateIdeas("any"),
                       'CustomerFeedback':random.choice(CustomerFeedback.CustomerFeedback)
                       })

        auth_id_parent = 'own|%s' % email
        auth_id_child = 'own|%s' % username
        parent_user = self.auth.get_user_entity(username=email)
        child_user = self.auth.get_user_entity(username=username)
        
        self.AlreadyRegistered = False
        if parent_user:
            registration_message = registration_message + "This email is already registered.<br>"
            self.AlreadyRegistered = True
        if child_user:
            registration_message = registration_message + "This child id is already registered.<br>"
            self.AlreadyRegistered = True
            
        try:
            if self.AlreadyRegistered:
                ''' DO NOTHING and exit !!'''
            else:                
                while not parent_user:                
                    parent_user = self.auth.create_user(email, auth_id_parent, password=parent_password,first_name=parent_first_name,
                                                 last_name=parent_last_name,email=email,IsParent=True
                                                 )

                while not child_user:   
                    child_user = self.auth.create_user(username, auth_id_child, password=child_password,email=email,
                                                       first_name=child_first_name,last_name=child_last_name,parent_first_name=parent_first_name,
                                                       parent_last_name=parent_last_name,IsParent=False,skill=child_skill
                                                 )
    
                if parent_user and child_user:
                    while self.auth.user:
                        self.auth.login_with_auth_id(parent_user.auth_id, True)
                    
                    self.sendMail(email, parent_first_name, parent_last_name, child_first_name, child_last_name, username)
                    return self.redirect("/")
                    #return self.render_response('SubscriptionPage.html', **kwargs)
                              
                else:
                    self.auth.logout()
                    self.DeleteUser(email)
                    self.DeleteUser(username)                    
                    registration_message = registration_message + "Error registering the users. Please try again. If the error persists please contact admin@homecampus.com.sg"
        
        except DeadlineExceededError:
            self.auth.logout()
            self.DeleteUser(email)
            self.DeleteUser(username)                    
            registration_message = registration_message + "Error registering the users. Please try again. If the error persists please contact admin@homecampus.com.sg"
            
        self.session['registration_message'] = registration_message
        parent_user = None
        child_user = None
        return self.get(**kwargs)

    def sendMail(self, email, first_name, last_name, child_first_name, child_last_name, username):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Welcome to Home Campus!!"
        SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
        SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(http://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="http://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">'
        SendMessage = SendMessage + 'Dear '+first_name+' '+last_name+','
        SendMessage = SendMessage + '<br /><br />Congratulations on your new registration to Home Campus!<br /><br />We hope you and your child will have a fun experience learning maths at Home Campus. So, <a href="http://my.homecampus.com.sg/SignIn"><font color="#0E820E">log in</font></a> and start using.<br /><br /><b><u>Registration details</u>:</b><br />'
        SendMessage = SendMessage + 'Parent username: '+email+'<br />Child username: '+username+'<br /><br />'
        
        #SendMessage = SendMessage + 'To start off, here\'s what you might like to check out:<br /></p><ul><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="http://my.homecampus.com.sg/Learn"><font color="#D92118"><b>Watch and Learn</b></font></a><br />Watch video lessons or read notes that are broken into bite-sized pieces</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="http://my.homecampus.com.sg/Practice"><font color="#2A91E1"><b>Unlimited Practice</b></font></a><br />Solve from a pool of unlimited questions with detailed step-by-step solutions</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="http://my.homecampus.com.sg/Elementary_Mathematics_Worksheets"><font color="#0E820E"><b>Worksheets on All Topics</b></font></a><br />Solve as many worksheets you like to check your knowledge</p></li><li><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;"><a href="http://my.homecampus.com.sg/Progress"><font color="#F6B937"><b>Monitor Progress</b></font></a><br />Identify areas of strengths and weaknesses through graphs, charts and reports</p></li></ul><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">This and much more await you.<br /><br />'
        
        SendMessage = SendMessage + 'Go ahead, explore and top math!!<br /><br /><p style="text-align:left; font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">Yours sincerely,<br />Team @ Home Campus<br /><strong><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></strong><br /><b><a href="http://my.homecampus.com.sg"><font color="#006666">www.homecampus.com.sg</font></a></b></p></td></tr></table></td></tr></tbody></table></div></td></tr></tbody></table>'
        
        message.html = SendMessage
        message.Send()         
    
    def DeleteUser(self, UserId):
            UserQuery = HomeCampusUser.gql("where username = '"+UserId+"'")
            UserData = UserQuery.fetch(1)
            for u in UserData:
                u.delete()

class AddChildHandler(BaseHandler):
    def get(self, **kwargs):
        redirect_url = "/"

        if self.auth.user and not self.auth.user.IsParent:
            # User is not a parent.
            return self.redirect(redirect_url)

        if not self.auth.user:
            # User is not logged in
            return self.redirect("/SignIn")
        
        if self.session.get('registration_message'):
            registration_message = self.session.get('registration_message')
            del self.session['registration_message']
            kwargs.update({
                       'registration_messages':registration_message
                       })
        return self.render_response('AddChildPage.html', **kwargs)

    def post(self, **kwargs):
        redirect_url = "/"

        if self.auth.user and not self.auth.user.IsParent:
            # User is not a parent.
            return self.redirect(redirect_url)
        
        registration_message = ""
        
        parent_first_name = self.auth.user.first_name
        parent_last_name = self.auth.user.last_name
        email = self.auth.user.email
        child_first_name = self.request.form.get('child_first_name')
        child_last_name = self.request.form.get('child_last_name')
        child_skill = self.request.form.get('skill_grade')
        username = self.request.form.get('username')
        child_password = self.request.form.get('child_password')
        #saving the current user in parent_user so after child user creation can be used again to login
        kwargs.update({'parent_first_name':parent_first_name,
                       'parent_last_name':parent_last_name,
                       'email':email,
                       'child_first_name':child_first_name,
                       'child_last_name':child_last_name,
                       'child_skill':child_skill,
                       'username':username,
                       'child_info':[[child_first_name,username]],
                       'Ideas':Ideas.GenerateIdeas("any"),
                       'CustomerFeedback':random.choice(CustomerFeedback.CustomerFeedback)
                       })
                    
        child_user = self.auth.get_user_entity(username=username)
        if child_user:
            registration_message = registration_message + "This user id is already registered.<br>"
        else:
            auth_id_child = 'own|%s' % username
            child_user = self.auth.create_user(username, auth_id_child, password=child_password,email=email,
                                               first_name=child_first_name,last_name=child_last_name,parent_first_name=parent_first_name,
                                               parent_last_name=parent_last_name,IsParent=False,skill=child_skill
                                         )
            user = self.auth.get_user_entity(username=email)
            self.auth.login_with_auth_id(user.auth_id, True)
            if child_user:
                #registration_message = registration_message + "Child user have been created successfully.<br>"
                self.sendMail(email, parent_first_name, parent_last_name, child_first_name, child_last_name, username)
                #return self.render_response('SubscriptionPage.html', **kwargs)
                return self.redirect("/")
            else:
                registration_message = registration_message + "Error registering child. Please try again. If error persists please contact admin.<br>"

        self.session['registration_message'] = registration_message
        #self.auth.logout()
        child_user = None        
        return self.get(**kwargs)

    def sendMail(self, email, first_name, last_name, child_first_name, child_last_name, username):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Welcome to Home Campus!!"
        SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
        SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(http://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="http://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">'
        SendMessage = SendMessage + 'Dear '+first_name+' '+last_name+','
        SendMessage = SendMessage + '<br /><br />Congratulations on successfully adding another child at Home Campus!<br /><br />We hope you and your children will have a fun experience learning maths at Home Campus. So, <a href="http://my.homecampus.com.sg/SignIn"><font color="#0E820E">log in</font></a> and start using.<br /><br /><b><u>Registration details</u>:</b><br />'
        SendMessage = SendMessage + 'Parent username: '+email+'<br />Child username: '+username+'<br /><br />'
        SendMessage = SendMessage + '<p style="text-align:left; font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">Yours sincerely,<br />Team @ Home Campus<br /><strong><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></strong><br /><b><a href="http://my.homecampus.com.sg"><font color="#006666">www.homecampus.com.sg</font></a></b></p></td></tr></table></td></tr></tbody></table></div></td></tr></tbody></table>'
        message.html = SendMessage
        message.Send()

class PasswordHandler(BaseHandler):
    def get(self, **kwargs):
        
        redirect_url = self.redirect_path()
        if self.auth.user:
            # User is already registered, so don't display the registration form.
            # 30-APR-2013: After login we don't show subscribe page 
            '''if self.auth.user.authorized:
                return self.redirect(redirect_url)
            else:
                return self.redirect("/Subscribe")'''
            return self.redirect(redirect_url)
                    
        if self.session.get('password_error'):
            password_error = self.session.get('password_error')[0]
            del self.session['password_error']
            context = {
                #'form':self.form,
                'password_error':password_error
            }
        else:
            context = {
                #'form':self.form
            }
        return self.render_response('ChangePasswordPage.html', **context)

    def post(self, **kwargs):
        redirect_url = self.redirect_path()

        if self.auth.user:
            # User is already registered, so don't process the signup form.
            # 30-APR-2013: After login we don't show subscribe page 
            '''if self.auth.user.authorized:
                return self.redirect(redirect_url)
            else:
                return self.redirect("/Subscribe")'''
            return self.redirect(redirect_url)
                    
        ParentChildChoice = self.request.form.get('ParentChildChoice')
        
        if ParentChildChoice == "parent":
            username = self.request.form.get('parent_username')
            password = self.request.form.get('parent_password')
            email = username
        elif ParentChildChoice == "child":
            username = self.request.form.get('child_username')
            password = self.request.form.get('child_password')
            email = unicode(self.request.form.get('child_email')).lower()
                        
        password_error = []

        user = self.auth.get_user_entity(username=username) 
        if user:
            if unicode(user.email).lower() != email:
                password_error.append("The email provided is not correct.")
                self.session['password_error'] = password_error
                return self.get(**kwargs)                 
            else:
                user.set_password(password)
                user.put()
                self.auth.login_with_auth_id(user.auth_id, True)
                self.sendMail(email, username)
        
                if self.auth.user:
                    # User is already registered, so don't process the signup form.
                    # 30-APR-2013: After login we don't show subscribe page 
                    '''if self.auth.user.authorized:
                        return self.redirect(redirect_url)
                    else:
                        return self.redirect("/Subscribe")'''
                    return self.redirect(redirect_url)
        else:
            password_error.append("This user id doesn't exist.")
            self.session['password_error'] = password_error
            return self.get(**kwargs)
    
    def sendMail(self, email, username):
        logging.info("Password reset mail send for "+username)
        message = mail.EmailMessage()
        message.to = email
        message.sender = "admin@homecampus.com.sg"
        message.subject = "HomeCampus: Password has been reset!!"
        SendMessage = "Password has been reset for username: "+username
        message.html = SendMessage
        message.Send()
        
class TeacherRegisterHandler(BaseHandler):
    def get(self, **kwargs):

        if self.auth.user:
            return self.redirect("/Teacher/Manage_Classroom")
            
        if self.session.get('registration_message'):
            registration_message = self.session.get('registration_message')
            del self.session['registration_message']
            kwargs.update({
                       'registration_messages':registration_message
                       })
        return self.render_response('TeacherRegisterPage.html', **kwargs)

    def post(self, **kwargs):
        redirect_url = self.redirect_path()

        if self.auth.user:
            # User is already registered, so don't process the signup form.
            return self.redirect(redirect_url)
        
        registration_message = ""
        teacher_first_name = self.request.form.get('teacher_first_name')
        teacher_last_name = self.request.form.get('teacher_last_name')
        email = self.request.form.get('email')
        teacher_password = self.request.form.get('teacher_password')

        kwargs.update({'teacher_first_name':teacher_first_name,
                       'teacher_last_name':teacher_last_name,
                       'email':email,
                       })

        auth_id_teacher = 'own|%s' % email
        teacher_user = self.auth.get_user_entity(username=email)
                
        self.AlreadyRegistered = False
        if teacher_user:
            registration_message = registration_message + "This email is already registered.<br>"
            self.AlreadyRegistered = True
            
        try:
            if self.AlreadyRegistered:
                ''' DO NOTHING and exit !!'''
            else:                
                while not teacher_user:                
                    teacher_user = self.auth.create_user(email, auth_id_teacher, password=teacher_password,first_name=teacher_first_name,
                                                 last_name=teacher_last_name,email=email,IsTeacher=True
                                                 )
    
                if teacher_user:
                    while self.auth.user:
                        self.auth.login_with_auth_id(teacher_user.auth_id, True)
                    
                    self.sendMail(email, teacher_first_name, teacher_last_name)
                    return self.redirect("/Teacher/Manage_Classroom")                              
                else:
                    self.auth.logout()
                    self.DeleteUser(email)                   
                    registration_message = registration_message + "Error registering the users. Please try again. If the error persists please contact admin@homecampus.com.sg"
        
        except DeadlineExceededError:
            self.auth.logout()
            self.DeleteUser(email)                   
            registration_message = registration_message + "Error registering the users. Please try again. If the error persists please contact admin@homecampus.com.sg"
            
        self.session['registration_message'] = registration_message
        teacher_user = None
        return self.get(**kwargs)

    ''' new email hase to be created for teachers '''
    def sendMail(self, email, first_name, last_name):
        message = mail.EmailMessage()
        message.to = email
        message.sender = "Home Campus <admin@homecampus.com.sg>"
        message.subject = "Welcome to Home Campus!!"
        SendMessage = '<html><head></head><body><!--CTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dt--><meta content="text/html; charset=utf-8" /><meta content="en-us" />'
        SendMessage = SendMessage + '<table description="lightestBgcolor" name="tid" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="padding: 0px 20px 20px 20px;"><div style="padding: 10px; margin: 0px;"><table align="left" width="560" cellpadding="0" cellspacing="0" style="font-family:Verdana;"><tbody><tr><td style="padding: 0px 20px; background: url(http://my.homecampus.com.sg/images/NewsLetter/HomeCampus_newsletter_header.png) no-repeat center;"><table description="mediumBorderBottomColor" name="tid" width="560" height="129" cellpadding="10" cellspacing="0" border="0"><tbody><tr><td style="text-align:left; width="300">&nbsp;</td><td ><br /><br /><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-size: 14px; padding: 2px 0px; margin: 1px;"><b><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></b></h3><h3 valign="baseline" align="right" style="font-family: Verdana, Helvetica, sans-serif; font-weight: bold; color: #006666; font-size: 13px; padding: 2px 0px; margin: 1px;"><a href="http://my.homecampus.com.sg" style="text-decoration:none;"><font color="#006666">www.homecampus.com.sg</font></a></h3></td></tr></tbody></table></td></tr><tr><td bgcolor="#ffffff" style="padding: 20px 20px 20px 20px;"><table width="560" cellpadding="0" cellspacing="0" border="0" ><tbody><tr><td valign="top" style="text-align:left;padding-bottom: 0px; padding-left: 0px; padding-right: 20px; padding-top: 0px;" colspan=2><p style="font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">'
        SendMessage = SendMessage + 'Dear '+first_name+' '+last_name+','
        SendMessage = SendMessage + '<br /><br />Congratulations on your new registration to Home Campus!<br /><br />We hope you and your students will have a fun experience learning maths at Home Campus. So, <a href="http://my.homecampus.com.sg/SignIn"><font color="#0E820E">log in</font></a> and start using.<br /><br /><b><u>Registration details</u>:</b><br />'
        SendMessage = SendMessage + 'Your username: '+email+'<br /><br /><br />'
        
        SendMessage = SendMessage + 'Let us know if you need help setting up your classrooms!!<br /><br /><p style="text-align:left; font-size: 12px; line-height: 1.7em; font-family:Verdana; color: #333333;">Yours sincerely,<br />Team @ Home Campus<br /><strong><font color="#D92118">Learn.</font> <font color="#2A91E1">Practice.</font> <font color="#F6B937">Progress.</font></strong><br /><b><a href="http://my.homecampus.com.sg"><font color="#006666">www.homecampus.com.sg</font></a></b></p></td></tr></table></td></tr></tbody></table></div></td></tr></tbody></table>'
        
        message.html = SendMessage
        message.Send()         
    
    def DeleteUser(self, UserId):
        UserQuery = HomeCampusUser.gql("where username = '"+UserId+"'")
        UserData = UserQuery.fetch(1)
        for u in UserData:
            u.delete()
