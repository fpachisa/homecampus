from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware,admin_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from Database import HCSubscription, SubmitProblemsTable, TestsMaster
import HCRank
from google.appengine.api import memcache
import logging
import CodeTranslation
import Grade7
from Grade7 import Grade7PageConfig


rules = [Rule('/', endpoint='', handler='HomePage.HomePage'),
         Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.SignupHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/Primary_Grade_3_Mathematics', endpoint='', handler='HomePage.Primary3'),
         Rule('/Primary_Grade_4_Mathematics', endpoint='', handler='HomePage.Primary4'),
         Rule('/Primary_Grade_5_Mathematics', endpoint='', handler='HomePage.Primary5'),
         Rule('/Primary_Grade_6_Mathematics', endpoint='', handler='HomePage.Primary6'),
         Rule('/PSLE', endpoint='', handler='HomePage.Primary6'),
         Rule('/Secondary-1-Grade-7-Mathematics', endpoint='', handler='HomePage.Secondary1'),
         Rule('/Secondary-1', endpoint='', handler='HomePage.Secondary1'),
         Rule('/Unfinished-Worksheets', endpoint='', handler='HomePage.UnfinishedWorksheets'),  
         ]

class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]
    
    def messages(self):
        """A list of status messages to be displayed to the user."""
        return self.session.get_flashes(key='_messages')
    
    def dispatch(self):
        '''
        19-AUG-2016: riyaz - defining this to get landing intent of the user 
        '''
        self.intent = self.request.args.get("intn")
        return RequestHandler.dispatch(self)
    
    
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
            UnfinishedWorksheetData = TestsMaster.TestsMasterTable.gql("where student_id = '"+self.auth.user.username+"'").fetch(10)
            for u in UnfinishedWorksheetData:
                if u.status!='Completed':
                    UnfinishedWorksheetsCount = UnfinishedWorksheetsCount + 1
            if UnfinishedWorksheetsCount > 6:
                UnfinishedWorksheetsCount = "5+"
        
        kwargs.update({
            'auth_session': auth_session,
            'current_user': self.auth.user,
            'login_url':    self.auth.login_url(),
            'logout_url':   self.auth.logout_url(),
            'current_url':  self.request.url,
            'register_url': self.auth.signup_url(),
            'TRIAL':TRIAL,
            'UnfinishedWorksheetsCount':UnfinishedWorksheetsCount,
            
            #19-AUG-2016 -- added by riyaz
            'intent': self.intent
        })

        return super(BaseHandler, self).render_response(filename, **kwargs)
      
class HomePage(BaseHandler):  
    def get(self, **kwargs):              
        return self.render_response('HomePage.html', section='content')
      
class Primary3(BaseHandler):  
    def get(self, **kwargs):
        grade_concept_rank = {}
        if self.auth.user:
            username = self.auth.user.username
            grade_concept_rank = GetConceptRank(3,username)
        concept_rank = {'grade_concept_rank':grade_concept_rank}
        return self.render_response('Primary_Grade_3.html', **concept_rank)
      
class Primary4(BaseHandler):  
    def get(self, **kwargs):               
        grade_concept_rank = {}
        if self.auth.user:
            username = self.auth.user.username
            grade_concept_rank = GetConceptRank(4,username)
        concept_rank = {'grade_concept_rank':grade_concept_rank}
        return self.render_response('Primary_Grade_4.html', **concept_rank)
      
class Primary5(BaseHandler):  
    def get(self, **kwargs):               
        grade_concept_rank = {}
        if self.auth.user:
            username = self.auth.user.username
            grade_concept_rank = GetConceptRank(5,username)
        concept_rank = {'grade_concept_rank':grade_concept_rank}
        return self.render_response('Primary_Grade_5.html', **concept_rank)
      
class Primary6(BaseHandler):  
    def get(self, **kwargs):               
        grade_concept_rank = {}
        if self.auth.user:
            username = self.auth.user.username
            grade_concept_rank = GetConceptRank(6,username)
        concept_rank = {'grade_concept_rank':grade_concept_rank}
        return self.render_response('Primary_Grade_6.html', **concept_rank)
      
class Secondary1(BaseHandler):  
    def get(self, **kwargs):
        pageName = self.request.args.get('pageName')
        AJAXBotSearchParam = self.request.args.get('_escaped_fragment_')
        if AJAXBotSearchParam is not None:
            #it came from the google BOT
            params = {}
            try:
                htmlPageName = Grade7PageConfig.PageMapping7A[AJAXBotSearchParam]
                page_number = Grade7PageConfig.Grade7APages.index(Grade7PageConfig.PageMapping7A[AJAXBotSearchParam])
            except KeyError:
                htmlPageName = Grade7PageConfig.PageMapping7B[AJAXBotSearchParam]
                page_number = Grade7PageConfig.Grade7BPages.index(Grade7PageConfig.PageMapping7B[AJAXBotSearchParam])
                
            params.update({"page_number":page_number})
            return self.render_response(htmlPageName,**params)
        else:    
            params = {}
            if pageName is not None:
                #the pageName is required when user is being redirected to the page he signed in from instead of taking him back to the first page.
                params.update({"pageRedirectName":pageName})
            return self.render_response('Grade-7/Grade-7.html', **params)
      
class UnfinishedWorksheets(BaseHandler):  
    def get(self, **kwargs):
        
        '''
        Need to fix for un-regd users!!!!
        '''
        
        worksheet_data = []
        count = 0
        if self.auth.user:
            username = self.auth.user.username
            WorksheetData = TestsMaster.TestsMasterTable.gql("where student_id = '"+username+"' order by create_date desc").fetch(500)
            for WD in WorksheetData:
                if WD.status != 'Completed' and count < 6:
                    try:
                        URL = CodeTranslation.WorksheetURL[WD.sub_concept]
                    except KeyError:
                        URL = ""
                    try:
                        TopicName = CodeTranslation.MainConcept[WD.sub_concept]
                    except KeyError:
                        TopicName = ""
                    try:
                        SubTopicName = CodeTranslation.Concept_List[WD.sub_concept]
                    except KeyError:
                        SubTopicName = ""
                    grade = "Grade "+str(WD.grade)
                    count = count + 1
                    worksheet_data.append([grade,TopicName,URL, SubTopicName])
        else:
            return self.redirect("/")   # @riyaz: will simply redirect to home for un-regd users
        params = {'worksheet_data':worksheet_data}       
        return self.render_response('Unfinished-Worksheets.html', **params)
    
def GetConceptRank(grade,username):
    Query = SubmitProblemsTable.ProblemsTable.gql("where student_id = '"+unicode(username)+"' and grade = "+str(grade))
    Data = Query.fetch(10000)
    ConceptRank = {}
    ''' GETTING ALL CONCEPTS BY GRADES'''
    if grade == 3:
        concept_list = CodeTranslation.SubTopics['P3WN']+CodeTranslation.SubTopics['P3MO']+CodeTranslation.SubTopics['P3LM']+CodeTranslation.SubTopics['P3TI']+CodeTranslation.SubTopics['P3AN']+CodeTranslation.SubTopics['P3BG']+CodeTranslation.SubTopics['P3AP']+CodeTranslation.SubTopics['P3FR']+CodeTranslation.SubTopics['P3PP']
    elif grade == 4:
        concept_list = CodeTranslation.SubTopics['P4DC']+CodeTranslation.SubTopics['P4FR']+CodeTranslation.SubTopics['P4MT']+CodeTranslation.SubTopics['P4WN']+CodeTranslation.SubTopics['P4DA']
    elif grade == 5:
        concept_list = CodeTranslation.SubTopics['P5DA']+CodeTranslation.SubTopics['P5DC']+CodeTranslation.SubTopics['P5FR']+CodeTranslation.SubTopics['P5GT']+CodeTranslation.SubTopics['P5MT']+CodeTranslation.SubTopics['P5PR']+CodeTranslation.SubTopics['P5RT']+CodeTranslation.SubTopics['P5WN']
    elif grade == 6:
        concept_list = CodeTranslation.SubTopics['P6AG']+CodeTranslation.SubTopics['P6DA']+CodeTranslation.SubTopics['P6FR']+CodeTranslation.SubTopics['P6MT']+CodeTranslation.SubTopics['P6PR']+CodeTranslation.SubTopics['P6RT']+CodeTranslation.SubTopics['P6SP']

    for i in range(len(concept_list)):
        correct = 0
        total_problems = 0
        HCScore = 0
        for r in Data:
            if r.concept == concept_list[i]:
                total_problems = total_problems + 1
                if r.correct:
                    correct = correct + 1
                    if not r.HCScore:
                        r.HCScore = 5
                    HCScore = HCScore + r.HCScore
        try:
            Concept_HCRank = HCRank.HCRank[HCScore]
        except KeyError:
            Concept_HCRank = 'Kage'
        NinjaStats = GetNinjaStats(HCScore)
        ConceptRank[concept_list[i]] = [CodeTranslation.Concept_List[concept_list[i]],total_problems,correct,HCScore,Concept_HCRank,
                                        NinjaStats[0],NinjaStats[1],NinjaStats[2],NinjaStats[3],NinjaStats[4]]
    return ConceptRank

def GetNinjaStats(HCScore):
    if HCScore <= 40:
        Ninja_max = 40
        Ninja_value = HCScore
        Ninja_title = str(Ninja_max+1-Ninja_value)+" more points for next Ninja rank"
        Ninja_Start = "Academy Ninja"
        Ninja_End = "Lower Ninja"
    elif HCScore > 40 and HCScore <= 90:
        Ninja_max = 90 - 40
        Ninja_value = HCScore - 40
        Ninja_title = str(Ninja_max+1-Ninja_value)+" more points for next Ninja rank"
        Ninja_Start = "Lower Ninja"
        Ninja_End = "Middle Ninja"
    elif HCScore > 90 and HCScore <= 150:
        Ninja_max =150 - 90
        Ninja_value = HCScore - 90
        Ninja_title = str(Ninja_max+1-Ninja_value)+" more points for next Ninja rank"
        Ninja_Start = "Middle Ninja"
        Ninja_End = "Elite Ninja"
    elif HCScore > 150 and HCScore <= 230:
        Ninja_max = 230 - 150 
        Ninja_value = HCScore - 150
        Ninja_title = str(Ninja_max+1-Ninja_value)+" more points for next Ninja rank"
        Ninja_Start = "Elite Ninja"
        Ninja_End = "Special Elite"
    elif HCScore > 230 and HCScore <= 400:
        Ninja_max = 400 - 230
        Ninja_value = HCScore - 230
        Ninja_title = str(Ninja_max+1-Ninja_value)+" more points for next Ninja rank"
        Ninja_Start = "Special Elite"
        Ninja_End = "Sage"                        
    elif HCScore > 400 and HCScore <= 1000:
        Ninja_max = 1000 - 400
        Ninja_value = HCScore - 400
        Ninja_title = str(Ninja_max+1-Ninja_value)+" more points for next Ninja rank"
        Ninja_Start = "Sage"
        Ninja_End = "Kage"
    elif HCScore > 1000:
        Ninja_max = 100
        Ninja_value = 100
        Ninja_title = "You have achieved the highest HCRank of KAGE!!"
        Ninja_Start = "Kage"
        Ninja_End = "Kage"                            
                
    NinjaStats = [Ninja_max,Ninja_value,Ninja_title,Ninja_Start,Ninja_End]
    return NinjaStats

        
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()