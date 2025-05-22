import Problems.Primary3.WholeNumbers.P3WNPlaceValue
import Problems.Primary3.WholeNumbers.P3WNFiguresToWords
import Problems.Primary3.WholeNumbers.P3WNWordsToFigures
import Problems.Primary3.WholeNumbers.P3WNComparingOrdering
import Problems.Primary3.WholeNumbers.P3WNNumberPatterns
import Problems.Primary3.WholeNumbers.P3WNAddition
import Problems.Primary3.WholeNumbers.P3WNSubtraction
import Problems.Primary3.WholeNumbers.P3WNMultiplication
import Problems.Primary3.WholeNumbers.P3WNDivision
import Problems.Primary3.WholeNumbers.P3WNWordProblems
import Problems.Primary3.Money.P3MOAddition
import Problems.Primary3.Money.P3MOSubtraction
import Problems.Primary3.Money.P3MOWordProblems
import Problems.Primary3.LengthMassVolume.P3LMMetreCentiMetre
import Problems.Primary3.LengthMassVolume.P3LMKiloMetre
import Problems.Primary3.LengthMassVolume.P3LMKiloGram
import Problems.Primary3.LengthMassVolume.P3LMLitresMilli
import Problems.Primary3.LengthMassVolume.P3LMWordProblems
import Problems.Primary3.LengthMassVolume.P3LMWordProblems_2Steps
import Problems.Primary3.Time.P3TITellingTime
import Problems.Primary3.Time.P3TIConversionTime
import Problems.Primary3.Time.P3TIDuration
import Problems.Primary3.Time.P3TIAddition
import Problems.Primary3.Time.P3TISubtraction
import Problems.Primary3.Time.P3TIWordProblems
import Problems.Primary3.Angles.P3ANIdentifying
import Problems.Primary3.Angles.P3ANRightAngle
import Problems.Primary3.BarGraphs.P3BGBarGraphs
import Problems.Primary3.AreaPerimeter.P3APSquareUnits
import Problems.Primary3.AreaPerimeter.P3APSquareCmM
import Problems.Primary3.AreaPerimeter.P3APPerimeter
import Problems.Primary3.AreaPerimeter.P3APArea
import Problems.Primary3.AreaPerimeter.P3APWordProblems
import Problems.Primary3.Fractions.P3FRWhatIsFractions
import Problems.Primary3.Fractions.P3FREquivalentFractions
import Problems.Primary3.Fractions.P3FRSimplifyingFractions
import Problems.Primary3.Fractions.P3FRComparingOrdering
import Problems.Primary3.Fractions.P3FRAddition
import Problems.Primary3.Fractions.P3FRSubtraction
import Problems.Primary3.PerpendicularParallel.P3PPPerpendicularParallel

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
from Database import SubmitProblemsTable, HCGoals, TestsMaster
import HCRank
import HCGoalsTargets
import SaveProblem
import logging


rules = [Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.PracticeLoginHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/PracticeLogin', endpoint='auth/PracticeLogin', handler='Handlers.PracticeLoginHandler'),

         Rule('/Grade_3_Math_Practice/Whole_Numbers_Number_Notation_Place_Values', endpoint='', handler='Primary3Problems.P3WholeNumbersPlaceValues'),
         Rule('/Grade_3_Math_Practice/Whole_Numbers_Figures_to_Words', endpoint='', handler='Primary3Problems.P3WNFiguresToWords'),
         Rule('/Grade_3_Math_Practice/Whole_Numbers_Words_to_Figures', endpoint='', handler='Primary3Problems.P3WNWordsToFigures'),
         Rule('/Grade_3_Math_Practice/Whole_Numbers_Comparing_Ordering', endpoint='', handler='Primary3Problems.P3WNComparingOrdering'),
         Rule('/Grade_3_Math_Practice/Whole_Numbers_Patterns', endpoint='', handler='Primary3Problems.P3WNNumberPatterns'),
         Rule('/Grade_3_Math_Practice/Whole_Numbers_Addition', endpoint='', handler='Primary3Problems.P3WNAddition'),
         Rule('/Grade_3_Math_Practice/Whole_Numbers_Subtraction', endpoint='', handler='Primary3Problems.P3WNSubtraction'),
         Rule('/Grade_3_Math_Practice/Whole_Numbers_Multiplication', endpoint='', handler='Primary3Problems.P3WNMultiplication'),
         Rule('/Grade_3_Math_Practice/Whole_Numbers_Division', endpoint='', handler='Primary3Problems.P3WNDivision'),
         Rule('/Grade_3_Math_Practice/Whole_Numbers_Word_Problems', endpoint='', handler='Primary3Problems.P3WNWordProblems'),
         Rule('/Grade_3_Math_Practice/Money_Addition', endpoint='', handler='Primary3Problems.P3MOAddition'),
         Rule('/Grade_3_Math_Practice/Money_Subtraction', endpoint='', handler='Primary3Problems.P3MOSubtraction'),
         Rule('/Grade_3_Math_Practice/Money_Word_Problems', endpoint='', handler='Primary3Problems.P3MOWordProblems'),
         Rule('/Grade_3_Math_Practice/Metres_Centimetres', endpoint='', handler='Primary3Problems.P3LMMetreCentiMetre'),
         Rule('/Grade_3_Math_Practice/Kilometres_Metres', endpoint='', handler='Primary3Problems.P3LMKiloMetre'),
         Rule('/Grade_3_Math_Practice/Kilograms_Grams', endpoint='', handler='Primary3Problems.P3LMKiloGram'),
         Rule('/Grade_3_Math_Practice/Litres_Millilitres', endpoint='', handler='Primary3Problems.P3LMLitresMilli'),
         Rule('/Grade_3_Math_Practice/Length_Mass_Volume_1-Step_Word_Problems', endpoint='', handler='Primary3Problems.P3LMWordProblems'),
         Rule('/Grade_3_Math_Practice/Length_Mass_Volume_2-Step_Word_Problems', endpoint='', handler='Primary3Problems.P3LMWordProblems_2Steps'),
         Rule('/Grade_3_Math_Practice/Telling_Time', endpoint='', handler='Primary3Problems.P3TITellingTime'),
         Rule('/Grade_3_Math_Practice/Time_Conversion_Hours_Minutes', endpoint='', handler='Primary3Problems.P3TIConversionTime'),
         Rule('/Grade_3_Math_Practice/Time_Finding_Duration_Start_Finish', endpoint='', handler='Primary3Problems.P3TIDuration'),
         Rule('/Grade_3_Math_Practice/Time_Addition', endpoint='', handler='Primary3Problems.P3TIAddition'),
         Rule('/Grade_3_Math_Practice/Time_Subtraction', endpoint='', handler='Primary3Problems.P3TISubtraction'),
         Rule('/Grade_3_Math_Practice/Time_Word_Problems', endpoint='', handler='Primary3Problems.P3TIWordProblems'),
         Rule('/Grade_3_Math_Practice/Identifying_Angles_in_Figures', endpoint='', handler='Primary3Problems.P3ANIdentifying'),
         Rule('/Grade_3_Math_Practice/Right_Angles', endpoint='', handler='Primary3Problems.P3ANRightAngle'),
         Rule('/Grade_3_Math_Practice/Bar_Graphs', endpoint='', handler='Primary3Problems.P3BGBarGraphs'),         
         Rule('/Grade_3_Math_Practice/Area_in_Square_Units', endpoint='', handler='Primary3Problems.P3APSquareUnits'),
         Rule('/Grade_3_Math_Practice/Area_in_Square_cm_Square_m', endpoint='', handler='Primary3Problems.P3APSquareCmM'),
         Rule('/Grade_3_Math_Practice/Perimeter_of_Squares_Rectangles', endpoint='', handler='Primary3Problems.P3APPerimeter'),
         Rule('/Grade_3_Math_Practice/Area_of_Squares_Rectangles', endpoint='', handler='Primary3Problems.P3APArea'),
         Rule('/Grade_3_Math_Practice/Area_Perimeter_Word_Problems', endpoint='', handler='Primary3Problems.P3APWordProblems'),
         Rule('/Grade_3_Math_Practice/What_is_a_Fraction', endpoint='', handler='Primary3Problems.P3FRWhatIsFractions'),
         Rule('/Grade_3_Math_Practice/Equivalent-Fraction', endpoint='', handler='Primary3Problems.P3FREquivalentFractions'),
         Rule('/Grade_3_Math_Practice/Simplifying-Fractions', endpoint='', handler='Primary3Problems.P3FRSimplifyingFractions'),
         Rule('/Grade_3_Math_Practice/Comparing-and-Ordering-Fractions', endpoint='', handler='Primary3Problems.P3FRComparingOrdering'),
         Rule('/Grade_3_Math_Practice/Adding-Fractions', endpoint='', handler='Primary3Problems.P3FRAddition'),
         Rule('/Grade_3_Math_Practice/Subtracting-Fractions', endpoint='', handler='Primary3Problems.P3FRSubtraction'),
         Rule('/Grade_3_Math_Practice/Identifying_Perpendicular_Parallel_Lines', endpoint='', handler='Primary3Problems.P3PPPerpendicularParallel'),
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
        
        concept = memcache.Client().get(unicode(self.auth.user.username)+'_template_values')['concept']
        
        '''12-Jun-2012 Skip-->Try Next can also get the problem type now'''
        memcache.Client().delete(unicode(self.auth.user.username)+"_"+concept+"_problem_type")
        memcache.Client().add(unicode(self.auth.user.username)+"_"+concept+"_problem_type",Config.template_values["problem_type"])        
        
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
        
        #converting score to percentage for each sub-topic
        Ninja_percentage = (float(Ninja_Stats[1]) / float(Ninja_Stats[0])) * 100
        
        
        Concept_Goal = self.GetConceptGoal(concept)

        #02-MAY-2013: In addition to storing the template values in memcache the problem is also saved in the database as memcache is not wprking correctly always
        if not self.auth.user.IsParent:
            SaveProblem.SaveProblem().SaveProblem(unicode(self.auth.user.username),Config.template_values)

        #A user can keep getting new question if it keeps pressing F5...however these questions are saved with concept = dummy in the datastore ..
        #so preventing unauthorised users to get more than 10 dummy questions
        
        # DummyQuestionCount = self.GetDummyQuestions()
        # if user is not subscribes he is allowed to attempt 10 questions only
        if not self.auth.user.authorized and (problems_attempted >= 7):# or DummyQuestionCount>=10):
            SubscribeMessage="Y"
        else:
            SubscribeMessage="N"
        
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
            'concept_display_full':"<a href='/Primary_Grade_3_Mathematics'>Grade 3</a> &nbsp;&gt;&gt;&nbsp; "+CodeTranslation.MainConcept[concept]+" &nbsp;&gt;&gt;&nbsp; "+concept_display,
            'practice_page':"/Primary_Grade_3_Mathematics",
            'Ninja_max':Ninja_Stats[0],
            'Ninja_value':Ninja_Stats[1],
            'Ninja_title':Ninja_Stats[2],
            'Ninja_Start':Ninja_Stats[3],
            'Ninja_End':Ninja_Stats[4],
            'Ninja_Percentage': Ninja_percentage,
            'SubscribeMessage':SubscribeMessage,
            'UnfinishedWorksheetsCount':UnfinishedWorksheetsCount          
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
            Ninja_title = str(Ninja_max+1-Ninja_value)+" more points to next Ninja rank"
            Ninja_Start = "Academy Ninja"
            Ninja_End = "Lower Ninja"
        elif HCScore > 40 and HCScore <= 90:
            Ninja_max = 90 - 40
            Ninja_value = HCScore - 40
            Ninja_title = str(Ninja_max+1-Ninja_value)+" more points to next Ninja rank"
            Ninja_Start = "Lower Ninja"
            Ninja_End = "Middle Ninja"
        elif HCScore > 90 and HCScore <= 150:
            Ninja_max =150 - 90
            Ninja_value = HCScore - 90
            Ninja_title = str(Ninja_max+1-Ninja_value)+" more points to next Ninja rank"
            Ninja_Start = "Middle Ninja"
            Ninja_End = "Elite Ninja"
        elif HCScore > 150 and HCScore <= 230:
            Ninja_max = 230 - 150 
            Ninja_value = HCScore - 150
            Ninja_title = str(Ninja_max+1-Ninja_value)+" more points to next Ninja rank"
            Ninja_Start = "Elite Ninja"
            Ninja_End = "Special Elite"
        elif HCScore > 230 and HCScore <= 400:
            Ninja_max = 400 - 230
            Ninja_value = HCScore - 230
            Ninja_title = str(Ninja_max+1-Ninja_value)+" more points to next Ninja rank"
            Ninja_Start = "Special Elite"
            Ninja_End = "Sage"                        
        elif HCScore > 400 and HCScore <= 1000:
            Ninja_max = 1000 - 400
            Ninja_value = HCScore - 400
            Ninja_title = str(Ninja_max+1-Ninja_value)+" more points to next Ninja rank"
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
        '''
        21-AUG-2016 - No Longer Required
        Query = SubmitProblemsTable.ProblemsTable.gql("where student_id = '"+unicode(self.auth.user)+"' and concept = 'DUMMY'")
        Data = Query.fetch(10)
        DummyQuestionCount = 0
        for _d in Data:
            DummyQuestionCount = DummyQuestionCount + 1
        return DummyQuestionCount
        '''
        return None  
    
class P3WholeNumbersPlaceValues(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNPlaceValues"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNPlaceValue.P3WNPlaceValue().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNPlaceValues"
        template_name = Config.template_values["template"]
        
        Problem_Details = self.render_template(template_name, **Config.template_values)
            
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNPlaceValues"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNPlaceValue.P3WNPlaceValue().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNPlaceValues"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3WNFiguresToWords(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNFiguresToWords"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNFiguresToWords.P3WNFiguresToWords().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNFiguresToWords"
        template_name = Config.template_values["template"]
        
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNFiguresToWords"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNFiguresToWords.P3WNFiguresToWords().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNFiguresToWords"
        template_name = Config.template_values["template"]
              
        return self.render_template(template_name, **Config.template_values)
    
class P3WNWordsToFigures(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNWordsToFigures"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNWordsToFigures.P3WNWordsToFigures().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNWordsToFigures"
        template_name = Config.template_values["template"]
        
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNWordsToFigures"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNWordsToFigures.P3WNWordsToFigures().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNWordsToFigures"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3WNComparingOrdering(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNComparingOrdering"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNComparingOrdering.P3WNComparingOrdering().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNComparingOrdering"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNComparingOrdering"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNComparingOrdering.P3WNComparingOrdering().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNComparingOrdering"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3WNNumberPatterns(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNNumberPatterns"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNNumberPatterns.P3WNNumberPatterns().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNNumberPatterns"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNNumberPatterns"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNNumberPatterns.P3WNNumberPatterns().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNNumberPatterns"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3WNAddition(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNAddition"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNAddition.P3WNAddition().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNAddition"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNAddition"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNAddition.P3WNAddition().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNAddition"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3WNSubtraction(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNSubtraction"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNSubtraction.P3WNSubtraction().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNSubtraction"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNSubtraction"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNSubtraction.P3WNSubtraction().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNSubtraction"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3WNMultiplication(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNMultiplication"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNMultiplication.P3WNMultiplication().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNMultiplication"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNMultiplication"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNMultiplication.P3WNMultiplication().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNMultiplication"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3WNDivision(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNDivision"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNDivision.P3WNDivision().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNDivision"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNDivision"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNDivision.P3WNDivision().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNDivision"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3WNWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNWordProblems"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNWordProblems.P3WNWordProblems().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNWordProblems"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3WNWordProblems"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.WholeNumbers.P3WNWordProblems.P3WNWordProblems().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3WNWordProblems"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3MOAddition(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3MOAddition"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Money.P3MOAddition.P3MOAddition().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3MOAddition"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3MOAddition"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Money.P3MOAddition.P3MOAddition().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3MOAddition"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3MOSubtraction(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3MOSubtraction"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Money.P3MOSubtraction.P3MOSubtraction().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3MOSubtraction"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3MOSubtraction"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Money.P3MOSubtraction.P3MOSubtraction().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3MOSubtraction"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3MOWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3MOWordProblems"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Money.P3MOWordProblems.P3MOWordProblems().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3MOWordProblems"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3MOWordProblems"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Money.P3MOWordProblems.P3MOWordProblems().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3MOWordProblems"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3LMMetreCentiMetre(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3LMMetreCentiMetre"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.LengthMassVolume.P3LMMetreCentiMetre.P3LMMetreCentiMetre().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3LMMetreCentiMetre"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3LMMetreCentiMetre"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.LengthMassVolume.P3LMMetreCentiMetre.P3LMMetreCentiMetre().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3LMMetreCentiMetre"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
    
class P3LMKiloMetre(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3LMKiloMetre"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.LengthMassVolume.P3LMKiloMetre.P3LMKiloMetre().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3LMKiloMetre"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3LMKiloMetre"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.LengthMassVolume.P3LMKiloMetre.P3LMKiloMetre().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3LMKiloMetre"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)  
    
class P3LMKiloGram(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3LMKiloGram"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.LengthMassVolume.P3LMKiloGram.P3LMKiloGram().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3LMKiloGram"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3LMKiloGram"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.LengthMassVolume.P3LMKiloGram.P3LMKiloGram().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3LMKiloGram"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)  
    
class P3LMLitresMilli(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3LMLitresMilli"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.LengthMassVolume.P3LMLitresMilli.P3LMLitresMilli().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3LMLitresMilli"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3LMLitresMilli"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.LengthMassVolume.P3LMLitresMilli.P3LMLitresMilli().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3LMLitresMilli"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)  
    
class P3LMWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3LMWordProblems"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.LengthMassVolume.P3LMWordProblems.P3LMWordProblems().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3LMWordProblems"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3LMWordProblems"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.LengthMassVolume.P3LMWordProblems.P3LMWordProblems().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3LMWordProblems"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)  
    
class P3LMWordProblems_2Steps(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3LMWordProblems_2Steps"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.LengthMassVolume.P3LMWordProblems_2Steps.P3LMWordProblems_2Steps().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3LMWordProblems_2Steps"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3LMWordProblems_2Steps"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.LengthMassVolume.P3LMWordProblems_2Steps.P3LMWordProblems_2Steps().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3LMWordProblems_2Steps"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)  
    
class P3TITellingTime(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3TITellingTime"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Time.P3TITellingTime.P3TITellingTime().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3TITellingTime"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3TITellingTime"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Time.P3TITellingTime.P3TITellingTime().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3TITellingTime"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)  
    
class P3TIConversionTime(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3TIConversionTime"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Time.P3TIConversionTime.P3TIConversionTime().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3TIConversionTime"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3TIConversionTime"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Time.P3TIConversionTime.P3TIConversionTime().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3TIConversionTime"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)  
    
class P3TIDuration(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3TIDuration"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Time.P3TIDuration.P3TIDuration().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3TIDuration"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3TIDuration"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Time.P3TIDuration.P3TIDuration().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3TIDuration"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)  
    
class P3TIAddition(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3TIAddition"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Time.P3TIAddition.P3TIAddition().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3TIAddition"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3TIAddition"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Time.P3TIAddition.P3TIAddition().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3TIAddition"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)  
    
class P3TISubtraction(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3TISubtraction"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Time.P3TISubtraction.P3TISubtraction().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3TISubtraction"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3TISubtraction"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Time.P3TISubtraction.P3TISubtraction().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3TISubtraction"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)  
    
class P3TIWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3TIWordProblems"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Time.P3TIWordProblems.P3TIWordProblems().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3TIWordProblems"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3TIWordProblems"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Time.P3TIWordProblems.P3TIWordProblems().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3TIWordProblems"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)  
    
class P3ANIdentifying(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3ANIdentifying"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Angles.P3ANIdentifying.P3ANIdentifying().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3ANIdentifying"
        template_name = Config.template_values["template"]
        
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3ANIdentifying"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Angles.P3ANIdentifying.P3ANIdentifying().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3ANIdentifying"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)  
    
class P3ANRightAngle(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3ANRightAngle"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Angles.P3ANRightAngle.P3ANRightAngle().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3ANRightAngle"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3ANRightAngle"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Angles.P3ANRightAngle.P3ANRightAngle().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3ANRightAngle"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)  
    
class P3BGBarGraphs(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3BGBarGraphs"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.BarGraphs.P3BGBarGraphs.P3BGBarGraphs().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3BGBarGraphs"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3BGBarGraphs"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.BarGraphs.P3BGBarGraphs.P3BGBarGraphs().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3BGBarGraphs"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  
    
class P3APSquareUnits(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3APSquareUnits"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.AreaPerimeter.P3APSquareUnits.P3APSquareUnits().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3APSquareUnits"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3APSquareUnits"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.AreaPerimeter.P3APSquareUnits.P3APSquareUnits().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3APSquareUnits"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  
    
class P3APSquareCmM(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3APSquareCmM"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.AreaPerimeter.P3APSquareCmM.P3APSquareCmM().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3APSquareCmM"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3APSquareCmM"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.AreaPerimeter.P3APSquareCmM.P3APSquareCmM().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3APSquareCmM"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  
    
class P3APPerimeter(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3APPerimeter"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.AreaPerimeter.P3APPerimeter.P3APPerimeter().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3APPerimeter"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3APPerimeter"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.AreaPerimeter.P3APPerimeter.P3APPerimeter().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3APPerimeter"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  
    
class P3APArea(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3APArea"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.AreaPerimeter.P3APArea.P3APArea().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3APArea"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3APArea"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.AreaPerimeter.P3APArea.P3APArea().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3APArea"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  
    
class P3APWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3APWordProblems"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.AreaPerimeter.P3APWordProblems.P3APWordProblems().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3APWordProblems"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3APWordProblems"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.AreaPerimeter.P3APWordProblems.P3APWordProblems().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3APWordProblems"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  
    
class P3FRWhatIsFractions(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3FRWhatIsFractions"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Fractions.P3FRWhatIsFractions.P3FRWhatIsFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3FRWhatIsFractions"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3FRWhatIsFractions"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Fractions.P3FRWhatIsFractions.P3FRWhatIsFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3FRWhatIsFractions"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  
    
class P3FREquivalentFractions(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3FREquivalentFractions"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Fractions.P3FREquivalentFractions.P3FREquivalentFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3FREquivalentFractions"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3FREquivalentFractions"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Fractions.P3FREquivalentFractions.P3FREquivalentFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3FREquivalentFractions"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  
    
class P3FRSimplifyingFractions(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3FRSimplifyingFractions"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Fractions.P3FRSimplifyingFractions.P3FRSimplifyingFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3FRSimplifyingFractions"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3FRSimplifyingFractions"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Fractions.P3FRSimplifyingFractions.P3FRSimplifyingFractions().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3FRSimplifyingFractions"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  
    
class P3FRComparingOrdering(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3FRComparingOrdering"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Fractions.P3FRComparingOrdering.P3FRComparingOrdering().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3FRComparingOrdering"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3FRComparingOrdering"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Fractions.P3FRComparingOrdering.P3FRComparingOrdering().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3FRComparingOrdering"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  
    
class P3FRAddition(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3FRAddition"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Fractions.P3FRAddition.P3FRAddition().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3FRAddition"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3FRAddition"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Fractions.P3FRAddition.P3FRAddition().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3FRAddition"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  
    
class P3FRSubtraction(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3FRSubtraction"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Fractions.P3FRSubtraction.P3FRSubtraction().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3FRSubtraction"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3FRSubtraction"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.Fractions.P3FRSubtraction.P3FRSubtraction().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3FRSubtraction"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  
    
class P3PPPerpendicularParallel(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3PPPerpendicularParallel"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.PerpendicularParallel.P3PPPerpendicularParallel.P3PPPerpendicularParallel().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3PPPerpendicularParallel"
        template_name = Config.template_values["template"]
               
        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+"_P3PPPerpendicularParallel"+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary3.PerpendicularParallel.P3PPPerpendicularParallel.P3PPPerpendicularParallel().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P3PPPerpendicularParallel"
        template_name = Config.template_values["template"]
        logging.info(Config.template_values)    
        return self.render_template(template_name, **Config.template_values)  

app = Tipfy(rules=rules, config=config)

def main():
    app.run()

if __name__ == "__main__":
    main()