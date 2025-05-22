import Problems.Primary1.WholeNumbers.P1WNAddition

import Config
import CodeTranslation
from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware, subscription_practice_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from google.appengine.api import memcache
from Database import SubmitProblemsTable, HCGoals, TestsMaster
import HCRank
import HCGoalsTargets


rules = [Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.PracticeLoginHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/PracticeLogin', endpoint='auth/PracticeLogin', handler='Handlers.PracticeLoginHandler'),
         Rule('/P1/Whole_Numbers/Rayan/Addition', endpoint='', handler='Primary1Problems.P1WholeNumbersAddition'),
         ]

class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]
    
    def render_template(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session
        
        concept_rank = memcache.Client().get(str(self.auth.user.username)+'_concept_rank')
        if not concept_rank:
            concept_rank = self.GetConceptRank()
            memcache.Client().add(str(self.auth.user.username)+'_concept_rank',concept_rank,3600)
        '''22-Aug-2011: if there is user inactivity of 10 minutes after loading the problem..the Config.template_values loses all data
        so storing in the session as well'''
        #self.session['template_values'] = Config.template_values
        '''05-Nov-2011 storing the template_values in memcache along with user id so its unique for each user. And not storing in session anymore'''
        memcache.Client().delete(str(self.auth.user.username)+"_template_values")
        memcache.Client().add(str(self.auth.user.username)+"_template_values",Config.template_values,3600)
        '''12-Jun-2012 Skip-->Try Next can also get the problem type now'''
        memcache.Client().delete(str(self.auth.user.username)+"_problem_type")
        memcache.Client().add(str(self.auth.user.username)+"_problem_type",Config.template_values["problem_type"])        
        concept = memcache.Client().get(str(self.auth.user.username)+'_template_values')['concept']
        try:
            concept_display = CodeTranslation.Concept_List[concept]
        except KeyError:
            concept_display = concept

        try:
            problems_attempted = concept_rank[concept][0]
            correct_problems = concept_rank[concept][1]
            Concept_HCScore = concept_rank[concept][2]
            Concept_HCRank = concept_rank[concept][3]
        except KeyError:
            problems_attempted = 0
            correct_problems = 0
            Concept_HCScore = 0
            Concept_HCRank = 'Academy Ninja'
        
        Concept_Goal = self.GetConceptGoal(concept)            
        
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
            'problems_attempted':problems_attempted,
            'correct_problems':correct_problems,
            'Concept_HCScore':Concept_HCScore,
            'Concept_HCRank':Concept_HCRank,
            'concept_display':concept_display,
            'ConceptID':concept,
            'Concept_Goal':Concept_Goal,
            'concept_display_full':"<a href='/Practice/Primary_Grade_1_RAYAN_Mathematics'>Grade 1</a> -- "+CodeTranslation.MainConcept[concept]+" -- "+concept_display,
            'UnfinishedWorksheetsCount':UnfinishedWorksheetsCount
        })

        return super(BaseHandler, self).render_template(filename, **kwargs)
    
    def GetConceptRank(self):
        Query = SubmitProblemsTable.ProblemsTable.gql("where student_id = '"+str(self.auth.user)+"'")
        Data = Query.fetch(10000)
        concept_list = []
        ConceptRank = {}
        for r in Data:
            if r.concept not in concept_list:
                concept_list.append(r.concept)
        
        for i in range(len(concept_list)):
            correct = 0
            total_problems = 0
            HCScore = 0
            #Concept_HCRank = ""
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
            ConceptRank[concept_list[i]] = [total_problems,correct,HCScore,Concept_HCRank]
        return ConceptRank
    
    def GetConceptGoal(self,concept):
        Query = HCGoals.HCGoals.gql("where student_id = '"+str(self.auth.user)+"' and subTopic='"+concept+"'")
        GoalsData = Query.fetch(1)
        if GoalsData != []:
            for g in GoalsData:
                goal = g.target
        else:
            try:
                goal = HCGoalsTargets.HCGoalsDict[concept]
            except KeyError:
                goal = 30
        return goal              
    
class P1WholeNumbersAddition(BaseHandler):
    @subscription_practice_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(str(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary1.WholeNumbers.P1WNAddition.P1WNAddition().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P1WNAddition"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)

app = Tipfy(rules=rules, config=config)

def main():
    app.run()

if __name__ == "__main__":
    main()