from tipfy import Rule
from Config import config
from tipfy import Tipfy


rules = [Rule('/auth/login', endpoint='', handler='Handlers.LoginHandler'),
         Rule('/auth/PracticeLogin', endpoint='', handler='Handlers.PracticeLoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),        
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/ForgotPassword', endpoint='', handler='Handlers.PasswordHandler'),
         Rule('/AddChild', endpoint='', handler='Handlers.AddChildHandler'),
         Rule('/ResetPassword', endpoint='', handler='Handlers.ResetPasswordHandler'),
         ]

    
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()