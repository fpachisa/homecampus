import Problems.Primary4.WholeNumbers.WriteInFigures
import Problems.Primary4.WholeNumbers.WriteInWords
import Problems.Primary4.WholeNumbers.PlaceValue
import Problems.Primary4.WholeNumbers.ComparingAndOrdering
import Problems.Primary4.WholeNumbers.RoundingOff
import Problems.Primary4.WholeNumbers.FactorMultiple
import Problems.Primary4.WholeNumbers.MultiplicationDivision
import Problems.Primary4.Fractions.MixedNumbersImproperFractions
import Problems.Primary4.Fractions.SimplifyingFractions
import Problems.Primary4.Fractions.AddLikeRelatedFractions
import Problems.Primary4.Fractions.SubtractLikeRelatedFractions
import Problems.Primary4.Fractions.MultiplyProperImproperFractions
import Problems.Primary4.Decimals.DecimalsTenths
import Problems.Primary4.Decimals.DecimalsHundredths
import Problems.Primary4.Decimals.DecimalsThousandths
import Problems.Primary4.Decimals.DecimalsComparingOrdering
import Problems.Primary4.Decimals.DecimalsRoundingOff
import Problems.Primary4.Decimals.DecimalsFractions
import Problems.Primary4.Decimals.DecimalsAddSub
import Problems.Primary4.Decimals.DecimalsMultiplyDivide
import Problems.Primary4.Measurement.MTTime24Hrs
import Problems.Primary4.Measurement.MTTimeDuration
import Problems.Primary4.Measurement.MTPerimeter
import Problems.Primary4.Measurement.MTArea
import Problems.Primary4.Measurement.MTCompositeFigures
import Problems.Primary4.DataAnalysis.P4DATablesBarGraphs
import Problems.Primary4.DataAnalysis.P4DALineGraphs
import Problems.Primary4.WholeNumbers.P4WNWordProblems
import Problems.Primary4.Decimals.P4DCWordProblems
import Problems.Primary4.Fractions.P4FRWordProblems

import Config
import CodeTranslation
from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware, practice_login_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from google.appengine.api import memcache
from Database import SubmitProblemsTable, HCGoals
import HCRank
import HCGoalsTargets
import SaveProblem


rules = [Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.PracticeLoginHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/PracticeLogin', endpoint='auth/PracticeLogin', handler='Handlers.PracticeLoginHandler'),
         
         Rule('/Grade_4_Math_Practice/Whole_Numbers_Write_Figures', endpoint='', handler='Primary4Problems.P4WholeNumbersWriteInFigures'),
         Rule('/Grade_4_Math_Practice/Whole_Numbers_Write_Words', endpoint='', handler='Primary4Problems.P4WholeNumbersWriteInWords'),
         Rule('/Grade_4_Math_Practice/Whole_Numbers_Place_Values', endpoint='', handler='Primary4Problems.P4WholeNumbersPlaceValues'),
         Rule('/Grade_4_Math_Practice/Whole_Numbers_Comparing_Ordering', endpoint='', handler='Primary4Problems.P4WholeNumbersComparingOrdering'),
         Rule('/Grade_4_Math_Practice/Whole_Numbers_Rounding_Off', endpoint='', handler='Primary4Problems.P4WholeNumbersRoundingOff'),
         Rule('/Grade_4_Math_Practice/Whole_Numbers_Factors_Multiples', endpoint='', handler='Primary4Problems.P4WholeNumbersFactorMultiple'),
         Rule('/Grade_4_Math_Practice/Whole_Numbers_Multiplication_Division', endpoint='', handler='Primary4Problems.P4WholeNumbersMutliplyDivide'),
         Rule('/Grade_4_Math_Practice/Mixed_Numbers_Improper_Fractions', endpoint='', handler='Primary4Problems.P4FractionsMixedImproper'),
         Rule('/Grade_4_Math_Practice/Fractions_Simplifying', endpoint='', handler='Primary4Problems.P4FractionsSimplifying'),
         Rule('/Grade_4_Math_Practice/Add_Like_Related_Fractions', endpoint='', handler='Primary4Problems.P4FractionsAdd'),
         Rule('/Grade_4_Math_Practice/Subtract_Like_Related_Fractions', endpoint='', handler='Primary4Problems.P4FractionsSubtract'),
         Rule('/Grade_4_Math_Practice/Multiplication_Fractions_Whole_Numbers', endpoint='', handler='Primary4Problems.P4FractionsMultiplication'),         
         Rule('/Grade_4_Math_Practice/Decimals_Tenths', endpoint='', handler='Primary4Problems.P4DecimalsTenths'),
         Rule('/Grade_4_Math_Practice/Decimals_Hundredths', endpoint='', handler='Primary4Problems.P4DecimalsHundredths'),
         Rule('/Grade_4_Math_Practice/Decimals_Thousandths', endpoint='', handler='Primary4Problems.P4DecimalsThousandths'),
         Rule('/Grade_4_Math_Practice/Decimals_Comparing_Ordering', endpoint='', handler='Primary4Problems.P4DecimalsComparingOrdering'),
         Rule('/Grade_4_Math_Practice/Decimals_Rounding_Off', endpoint='', handler='Primary4Problems.P4DecimalsRoundingOff'),
         Rule('/Grade_4_Math_Practice/Decimals_Fractions', endpoint='', handler='Primary4Problems.P4DecimalsFractions'),
         Rule('/Grade_4_Math_Practice/Decimals_Addition_Subtraction', endpoint='', handler='Primary4Problems.P4DecimalsAddSub'),         
         Rule('/Grade_4_Math_Practice/Decimals_Multiplication_Division', endpoint='', handler='Primary4Problems.P4DecimalsMultiplyDivide'),

         Rule('/Grade_4_Math_Practice/Measurement_24-Hour_Clock', endpoint='', handler='Primary4Problems.P4MTTime24Hrs'),
         Rule('/Grade_4_Math_Practice/Measurement_Time_Duration', endpoint='', handler='Primary4Problems.P4MTTimeDuration'),
         Rule('/Grade_4_Math_Practice/Perimeter_Rectangle_Squares', endpoint='', handler='Primary4Problems.P4MTPerimeter'),
         Rule('/Grade_4_Math_Practice/Area_Rectangle_Squares', endpoint='', handler='Primary4Problems.P4MTArea'),
         Rule('/Grade_4_Math_Practice/Measurement_Composite_Figures', endpoint='', handler='Primary4Problems.P4MTCompositeFigures'),

         Rule('/Grade_4_Math_Practice/Data_Analysis_Tables_Bar_Graphs', endpoint='', handler='Primary4Problems.P4DATablesBarGraphs'),
         Rule('/Grade_4_Math_Practice/Data_Analysis_Line_Graphs', endpoint='', handler='Primary4Problems.P4DALineGraphs'),
         
         Rule('/Grade_4_Math_Practice/Whole_Numbers_Word_Problems', endpoint='', handler='Primary4Problems.P4WNWordProblems'),
         Rule('/Grade_4_Math_Practice/Decimals_Word_Problems', endpoint='', handler='Primary4Problems.P4DCWordProblems'),
         Rule('/Grade_4_Math_Practice/Fractions_Word_Problems', endpoint='', handler='Primary4Problems.P4FRWordProblems'),         
         ]

class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]
    
    def render_template(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session
        
        concept_rank = memcache.Client().get(unicode(self.auth.user.username)+'_concept_rank')
        if not concept_rank:
            concept_rank = self.GetConceptRank()
            memcache.Client().add(unicode(self.auth.user.username)+'_concept_rank',concept_rank,3600)
        '''22-Aug-2011: if there is user inactivity of 10 minutes after loading the problem..the Config.template_values loses all data
        so storing in the session as well'''
        #self.session['template_values'] = Config.template_values
        '''05-Nov-2011 storing the template_values in memcache along with user id so its unique for each user. And not storing in session anymore'''
        memcache.Client().delete(unicode(self.auth.user.username)+"_template_values")
        memcache.Client().add(unicode(self.auth.user.username)+"_template_values",Config.template_values,3600)
        '''12-Jun-2012 Skip-->Try Next can also get the problem type now'''
        memcache.Client().delete(unicode(self.auth.user.username)+"_problem_type")
        memcache.Client().add(unicode(self.auth.user.username)+"_problem_type",Config.template_values["problem_type"])        
        concept = memcache.Client().get(unicode(self.auth.user.username)+'_template_values')['concept']
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

        # 01-JUL-2013 : for adding the Ninja progress bar
        Ninja_Stats = self.GetNinjaStats(Concept_HCRank, Concept_HCScore)        
        
        Concept_Goal = self.GetConceptGoal(concept)
       
        #02-MAY-2013: In addition to storing the template values in memcache the problem is also saved in the database as memcache is not wprking correctly always
        if not self.auth.user.IsParent:
            SaveProblem.SaveProblem().SaveProblem(unicode(self.auth.user.username),Config.template_values)

        #A user can keep getting new question if it keeps pressing F5...however these questions are saved with concept = dummy in the datastore ..
        #so preventing unauthorised users to get more than 10 dummy questions
        
        DummyQuestionCount = self.GetDummyQuestions()
        # if user is not subscribes he is allowed to attempt 10 questions only
        if not self.auth.user.authorized and (problems_attempted >= 7 or DummyQuestionCount>=10):
            SubscribeMessage="Y"
        else:
            SubscribeMessage="N"
                               
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
            'concept_display_full':"<a href='/Primary_Grade_4_Mathematics'><font style='text-decoration:underline'>Grade 4</font></a> -- "+CodeTranslation.MainConcept[concept]+" -- "+concept_display,
            'practice_page':"/Primary_Grade_4_Mathematics",
            'Ninja_max':Ninja_Stats[0],
            'Ninja_value':Ninja_Stats[1],
            'Ninja_title':Ninja_Stats[2],
            'Ninja_Start':Ninja_Stats[3],
            'Ninja_End':Ninja_Stats[4],
            'SubscribeMessage':SubscribeMessage,
        })
            
        return super(BaseHandler, self).render_template(filename, **kwargs)

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
        return super(BaseHandler, self).render_response(filename, **kwargs)
    
    def GetConceptRank(self):
        Query = SubmitProblemsTable.ProblemsTable.gql("where student_id = '"+unicode(self.auth.user)+"'")
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
 
    def GetNinjaStats(self,HCRank,HCScore):
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
    
    def GetConceptGoal(self,concept):
        Query = HCGoals.HCGoals.gql("where student_id = '"+unicode(self.auth.user)+"' and subTopic='"+concept+"'")
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
    
    def GetDummyQuestions(self):
        Query = SubmitProblemsTable.ProblemsTable.gql("where student_id = '"+unicode(self.auth.user)+"' and concept = 'DUMMY'")
        Data = Query.fetch(10)
        DummyQuestionCount = 0
        for _d in Data:
            DummyQuestionCount = DummyQuestionCount + 1
        return DummyQuestionCount         

    
class P4WholeNumbersWriteInFigures(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.WriteInFigures.WriteInFigures().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4WholeNumbersWriteInFigures"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.WriteInFigures.WriteInFigures().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4WholeNumbersWriteInFigures"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4WholeNumbersWriteInWords(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.WriteInWords.WriteInWords().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4WholeNumbersWriteInWords"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.WriteInWords.WriteInWords().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4WholeNumbersWriteInWords"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4WholeNumbersPlaceValues(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.PlaceValue.PlaceValue().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4WholeNumbersPlaceValues"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.PlaceValue.PlaceValue().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4WholeNumbersPlaceValues"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4WholeNumbersComparingOrdering(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.ComparingAndOrdering.ComparingAndOrdering().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4WholeNumbersComparingOrdering"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.ComparingAndOrdering.ComparingAndOrdering().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4WholeNumbersComparingOrdering"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4WholeNumbersRoundingOff(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.RoundingOff.RoundingOff().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4WholeNumbersRoundingOff"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.RoundingOff.RoundingOff().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4WholeNumbersRoundingOff"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4WholeNumbersFactorMultiple(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.FactorMultiple.FactorMultiple().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4WholeNumbersFactorMultiple"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.FactorMultiple.FactorMultiple().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4WholeNumbersFactorMultiple"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4WholeNumbersMutliplyDivide(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.MultiplicationDivision.MultiplicationDivision().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4WholeNumbersMutliplyDivide"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.MultiplicationDivision.MultiplicationDivision().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4WholeNumbersMutliplyDivide"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4FractionsMixedImproper(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Fractions.MixedNumbersImproperFractions.MixedNumbersImproperFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4FractionsMixedImproper"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Fractions.MixedNumbersImproperFractions.MixedNumbersImproperFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4FractionsMixedImproper"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4FractionsSimplifying(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Fractions.SimplifyingFractions.SimplifyingFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4FractionsSimplifying"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Fractions.SimplifyingFractions.SimplifyingFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4FractionsSimplifying"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4FractionsAdd(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Fractions.AddLikeRelatedFractions.AddLikeRelatedFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4FractionsAdd"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Fractions.AddLikeRelatedFractions.AddLikeRelatedFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4FractionsAdd"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4FractionsSubtract(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Fractions.SubtractLikeRelatedFractions.SubtractLikeRelatedFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4FractionsSubtract"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Fractions.SubtractLikeRelatedFractions.SubtractLikeRelatedFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4FractionsSubtract"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4FractionsMultiplication(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Fractions.MultiplyProperImproperFractions.MultiplyProperImproperFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4FractionsMultiplication"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Fractions.MultiplyProperImproperFractions.MultiplyProperImproperFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4FractionsMultiplication"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4DecimalsTenths(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsTenths.DecimalsTenths().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsTenths"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsTenths.DecimalsTenths().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsTenths"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4DecimalsHundredths(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsHundredths.DecimalsHundredths().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsHundredths"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsHundredths.DecimalsHundredths().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsHundredths"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4DecimalsThousandths(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsThousandths.DecimalsThousandths().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsThousandths"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsThousandths.DecimalsThousandths().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsThousandths"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4DecimalsComparingOrdering(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsComparingOrdering.DecimalsComparingOrdering().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsComparingOrdering"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsComparingOrdering.DecimalsComparingOrdering().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsComparingOrdering"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4DecimalsRoundingOff(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsRoundingOff.DecimalsRoundingOff().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsRoundingOff"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsRoundingOff.DecimalsRoundingOff().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsRoundingOff"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4DecimalsFractions(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsFractions.DecimalsFractions().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4DecimalsFractions"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsFractions.DecimalsFractions().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4DecimalsFractions"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4DecimalsAddSub(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsAddSub.DecimalsAddSub().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsAddSub"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsAddSub.DecimalsAddSub().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsAddSub"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4DecimalsMultiplyDivide(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsMultiplyDivide.DecimalsMultiplyDivide().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsMultiplyDivide"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.DecimalsMultiplyDivide.DecimalsMultiplyDivide().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DecimalsMultiplyDivide"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4MTTime24Hrs(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Measurement.MTTime24Hrs.MTTime24Hrs().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4MTTime24Hrs"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Measurement.MTTime24Hrs.MTTime24Hrs().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4MTTime24Hrs"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4MTTimeDuration(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Measurement.MTTimeDuration.MTTimeDuration().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4MTTimeDuration"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Measurement.MTTimeDuration.MTTimeDuration().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4MTTimeDuration"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4MTPerimeter(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Measurement.MTPerimeter.MTPerimeter().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4MTPerimeter"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Measurement.MTPerimeter.MTPerimeter().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4MTPerimeter"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4MTArea(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Measurement.MTArea.MTArea().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4MTArea"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Measurement.MTArea.MTArea().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4MTArea"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4MTCompositeFigures(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Measurement.MTCompositeFigures.MTCompositeFigures().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4MTCompositeFigures"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Measurement.MTCompositeFigures.MTCompositeFigures().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4MTCompositeFigures"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4DATablesBarGraphs(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.DataAnalysis.P4DATablesBarGraphs.P4DATablesBarGraphs().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DATablesBarGraphs"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.DataAnalysis.P4DATablesBarGraphs.P4DATablesBarGraphs().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4DATablesBarGraphs"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4DALineGraphs(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.DataAnalysis.P4DALineGraphs.P4DALineGraphs().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4DALineGraphs"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.DataAnalysis.P4DALineGraphs.P4DALineGraphs().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4DALineGraphs"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4WNWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.P4WNWordProblems.P4WNWordProblems().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4WNWordProblems"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.WholeNumbers.P4WNWordProblems.P4WNWordProblems().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P4WNWordProblems"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4DCWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.P4DCWordProblems.P4DCWordProblems().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4DCWordProblems"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Decimals.P4DCWordProblems.P4DCWordProblems().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4DCWordProblems"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P4FRWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Fractions.P4FRWordProblems.P4FRWordProblems().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4FRWordProblems"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary4.Fractions.P4FRWordProblems.P4FRWordProblems().GenerateProblemSequential(LastProblemID)                
        #Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblem()  
        Config.template_values["concept"] = "P4FRWordProblems"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)

app = Tipfy(rules=rules, config=config)

def main():
    app.run()

if __name__ == "__main__":
    main()