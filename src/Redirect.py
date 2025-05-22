from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import login_required,UserRequiredIfAuthenticatedMiddleware,user_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from tipfy.app import App

rules = [Rule('/', endpoint='', handler='Redirect.RedirectPage'),]

class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]

    def render_response(self, filename, **kwargs):

        kwargs.update({ })

        return super(BaseHandler, self).render_response(filename, **kwargs)
      
class RedirectPage(BaseHandler):  
    def get(self, **kwargs):               
        return self.render_response('RedirectPage.html', section='content')
    
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()