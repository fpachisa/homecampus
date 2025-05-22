
import Problems.Primary5.WholeNumbers.WriteInFigures
import Problems.Primary5.WholeNumbers.WriteInWords
import Problems.Primary5.WholeNumbers.ApproximationEstimation
import Problems.Primary5.WholeNumbers.ComparingAndOrdering
import Problems.Primary5.WholeNumbers.FindPattern
import Problems.Primary5.WholeNumbers.MultiplyDivide
import Problems.Primary5.WholeNumbers.OrderOfOperation
import Problems.Primary5.WholeNumbers.PlaceValue
import Problems.Primary5.WholeNumbers.WordProblems
import Problems.Primary5.Fractions.AddSubMixedFractions
import Problems.Primary5.Fractions.AddSubProperFractions
import Problems.Primary5.Fractions.DivideProperFractions
import Problems.Primary5.Fractions.MultMixedFractions
import Problems.Primary5.Fractions.MultProperImproperFractions
import Problems.Primary5.Fractions.WordProblems
import Problems.Primary5.Decimals.MultiplyDivide
import Problems.Primary5.Decimals.Rounding
import Problems.Primary5.Decimals.WordProblems
import Problems.Primary5.Percentage.ExpressAsPercent
import Problems.Primary5.Percentage.ExpressAsDecimal
import Problems.Primary5.Percentage.ExpressAsFraction
import Problems.Primary5.Percentage.WordProblems
import Problems.Primary5.Ratio.SimplestForm
import Problems.Primary5.Ratio.MissingNumber
import Problems.Primary5.Ratio.WordProblems
import Problems.Primary5.Measurement.UnitConversion
import Problems.Primary5.Measurement.AreaOfTriangle
import Problems.Primary5.Measurement.Volume
import Problems.Primary5.Measurement.WordProblems
import Problems.Primary5.Geometry.Angles
import Problems.Primary5.Geometry.Triangles
import Problems.Primary5.Geometry.FourSidedFigures
import Problems.Primary5.DataAnalysis.FindAverage
import Problems.Primary5.DataAnalysis.FindTotal
import Problems.Primary5.DataAnalysis.WordProblems
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


rules = [Rule('/Grade_5_Math_Practice/Whole_Numbers_Write_Figures', endpoint='', handler='Primary5Problems.P5WholeNumbersWriteInFigures'),
         Rule('/Grade_5_Math_Practice/Whole_Numbers_Write_Words', endpoint='', handler='Primary5Problems.P5WholeNumbersWriteInWords'),
         Rule('/Grade_5_Math_Practice/Whole_Numbers_Place_Values', endpoint='', handler='Primary5Problems.P5WholeNumbersPlaceValue'),
         Rule('/Grade_5_Math_Practice/Whole_Numbers_Comparing_Ordering', endpoint='', handler='Primary5Problems.P5WholeNumbersCAndO'),
         Rule('/Grade_5_Math_Practice/Whole_Numbers_Find_Pattern', endpoint='', handler='Primary5Problems.P5WholeNumbersFindPattern'),
         Rule('/Grade_5_Math_Practice/Whole_Numbers_Approximation_Estimation', endpoint='', handler='Primary5Problems.P5WholeNumbersApproxEstimate'),
         Rule('/Grade_5_Math_Practice/Whole_Numbers_Multiplication_Division', endpoint='', handler='Primary5Problems.P5WholeNumbersMultiplyDivide'),
         Rule('/Grade_5_Math_Practice/Whole_Numbers_Order_Operations', endpoint='', handler='Primary5Problems.P5WholeNumbersOrderOperation'),
         Rule('/Grade_5_Math_Practice/Whole_Numbers_Word_Problems', endpoint='', handler='Primary5Problems.P5WholeNumbersWordProblems'),         
         Rule('/Grade_5_Math_Practice/Add_Subtract_Proper_Fractions', endpoint='', handler='Primary5Problems.P5FractionsAddSubProperFractions'),
         Rule('/Grade_5_Math_Practice/Add_Subtract_Mixed_Fractions', endpoint='', handler='Primary5Problems.P5FractionsAddSubMixedFractions'),
         Rule('/Grade_5_Math_Practice/Multiply_Proper_Improper_Fractions', endpoint='', handler='Primary5Problems.P5FractionsMultProperImproperFractions'),
         Rule('/Grade_5_Math_Practice/Multiply_Mixed_Fraction_Whole_Number', endpoint='', handler='Primary5Problems.P5FractionsMultMixedFractions'),
         Rule('/Grade_5_Math_Practice/Divide_Proper_Fraction_Whole_Number', endpoint='', handler='Primary5Problems.P5FractionsDivideProperFractions'),
         Rule('/Grade_5_Math_Practice/Fractions_Word_Problems', endpoint='', handler='Primary5Problems.P5FractionsWordProblems'),         
         Rule('/Grade_5_Math_Practice/Decimals_Multiply_Divide', endpoint='', handler='Primary5Problems.P5DecimalsMultiplyDivide'),
         Rule('/Grade_5_Math_Practice/Decimals_Rounding_Off', endpoint='', handler='Primary5Problems.P5DecimalsRounding'),
         Rule('/Grade_5_Math_Practice/Decimals_Word_Problems', endpoint='', handler='Primary5Problems.P5DecimalsWordProblems'),
         Rule('/Grade_5_Math_Practice/Express_as_Percentage', endpoint='', handler='Primary5Problems.P5PercentageExpressAsPercent'),
         Rule('/Grade_5_Math_Practice/Express_as_Decimal', endpoint='', handler='Primary5Problems.P5PercentageExpressAsDecimal'),
         Rule('/Grade_5_Math_Practice/Express_as_Fraction', endpoint='', handler='Primary5Problems.P5PercentageExpressAsFraction'),
         Rule('/Grade_5_Math_Practice/Percentage_Word_Problems', endpoint='', handler='Primary5Problems.P5PercentageWordProblems'),
         Rule('/Grade_5_Math_Practice/Ratio_Simplest_Form', endpoint='', handler='Primary5Problems.P5RatioSimplestForm'),
         Rule('/Grade_5_Math_Practice/Ratio_Missing_Number', endpoint='', handler='Primary5Problems.P5RatioMissingNumber'),
         Rule('/Grade_5_Math_Practice/Ratio_Word_Problems', endpoint='', handler='Primary5Problems.P5RatioWordProblems'),        
         Rule('/Grade_5_Math_Practice/Measurement_Unit_Conversion', endpoint='', handler='Primary5Problems.P5MeasurementUnitConversion'),
         Rule('/Grade_5_Math_Practice/Measurement_Area_Triangle', endpoint='', handler='Primary5Problems.P5MeasurementAreaOfTriangle'),
         Rule('/Grade_5_Math_Practice/Measurement_Volume_Cube_Cuboid', endpoint='', handler='Primary5Problems.P5MeasurementVolume'),
         Rule('/Grade_5_Math_Practice/Measurement_Word_Problems', endpoint='', handler='Primary5Problems.P5MeasurementWordProblems'),
         Rule('/Grade_5_Math_Practice/Geometry_Find_Unknown_Angles', endpoint='', handler='Primary5Problems.P5GeometryAngles'),
         Rule('/Grade_5_Math_Practice/Triangles_Find_Unknown_Angles', endpoint='', handler='Primary5Problems.P5GeometryTriangles'),
         Rule('/Grade_5_Math_Practice/Find_Unknown_Angles_in_Four_Sided_Figures', endpoint='', handler='Primary5Problems.P5GeometryFourSided'),                  
         Rule('/Grade_5_Math_Practice/Data_Analysis_Find_Average', endpoint='', handler='Primary5Problems.P5DataAnalysisAverage'),
         Rule('/Grade_5_Math_Practice/Data_Analysis_Find_Total', endpoint='', handler='Primary5Problems.P5DataAnalysisTotal'),
         Rule('/Grade_5_Math_Practice/Data_Analysis_Word_Problems', endpoint='', handler='Primary5Problems.P5DataAnalysisWordProblems'),

         Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.PracticeLoginHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/PracticeLogin', endpoint='auth/PracticeLogin', handler='Handlers.PracticeLoginHandler'),]

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
            'concept_display_full':"<a href='/Primary_Grade_5_Mathematics'><font style='text-decoration:underline'>Grade 5</font></a> -- "+CodeTranslation.MainConcept[concept]+" -- "+concept_display,
            'practice_page':"/Primary_Grade_5_Mathematics",
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
    
class P5WholeNumbersWriteInFigures(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.WholeNumbers.WriteInFigures.WriteInFigures().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P5WholeNumbersWriteInFigures"
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
                   
        Config.template_values = Problems.Primary5.WholeNumbers.WriteInFigures.WriteInFigures().GenerateProblemSequential(LastProblemID)                
        Config.template_values["concept"] = "P5WholeNumbersWriteInFigures"
        template_name = Config.template_values["template"]
               
        return self.render_template(template_name, **Config.template_values)
            
class P5WholeNumbersWriteInWords(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblemSequential(LastProblemID)                                  
        Config.template_values["concept"] = "P5WholeNumbersWriteInWords"
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
                   
        Config.template_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateProblemSequential(LastProblemID)                                  
        Config.template_values["concept"] = "P5WholeNumbersWriteInWords"
        template_name = Config.template_values["template"]
        return self.render_template(template_name, **Config.template_values)          

class P5WholeNumbersPlaceValue(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.WholeNumbers.PlaceValue.PlaceValue().GenerateProblemSequential(LastProblemID) 
        Config.template_values["concept"] = "P5WholeNumbersPlaceValue"
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
                   
        Config.template_values = Problems.Primary5.WholeNumbers.PlaceValue.PlaceValue().GenerateProblemSequential(LastProblemID) 
        Config.template_values["concept"] = "P5WholeNumbersPlaceValue"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)
        
class P5WholeNumbersCAndO(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.WholeNumbers.ComparingAndOrdering.ComparingAndOrdering().GenerateProblemSequential(LastProblemID) 
        Config.template_values["concept"] = "P5WholeNumbersComparingAndOrdering"
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
                   
        Config.template_values = Problems.Primary5.WholeNumbers.ComparingAndOrdering.ComparingAndOrdering().GenerateProblemSequential(LastProblemID) 
        Config.template_values["concept"] = "P5WholeNumbersComparingAndOrdering"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5WholeNumbersFindPattern(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.WholeNumbers.FindPattern.FindPattern().GenerateProblemSequential(LastProblemID) 
        Config.template_values["concept"] = "P5WholeNumbersFindPattern"
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
                   
        Config.template_values = Problems.Primary5.WholeNumbers.FindPattern.FindPattern().GenerateProblemSequential(LastProblemID) 
        Config.template_values["concept"] = "P5WholeNumbersFindPattern"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5WholeNumbersApproxEstimate(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.WholeNumbers.ApproximationEstimation.ApproximationEstimation().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5WholeNumbersApproximationEstimation"
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
                   
        Config.template_values = Problems.Primary5.WholeNumbers.ApproximationEstimation.ApproximationEstimation().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5WholeNumbersApproximationEstimation"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5WholeNumbersMultiplyDivide(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.WholeNumbers.MultiplyDivide.MultiplyDivide().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5WholeNumbersMultiplyDivide"
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
                   
        Config.template_values = Problems.Primary5.WholeNumbers.MultiplyDivide.MultiplyDivide().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5WholeNumbersMultiplyDivide"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5WholeNumbersOrderOperation(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.WholeNumbers.OrderOfOperation.OrderOfOperation().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5WholeNumbersOrderOfOperation"
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
                   
        Config.template_values = Problems.Primary5.WholeNumbers.OrderOfOperation.OrderOfOperation().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5WholeNumbersOrderOfOperation"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)
        
class P5WholeNumbersWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary5.WholeNumbers.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5WholeNumbersWordProblems"
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
        
        Config.template_values = Problems.Primary5.WholeNumbers.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5WholeNumbersWordProblems"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)
    
class P5FractionsAddSubProperFractions(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.Fractions.AddSubProperFractions.AddSubProperFractions().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5FractionsAddSubProperFractions"
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
                   
        Config.template_values = Problems.Primary5.Fractions.AddSubProperFractions.AddSubProperFractions().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5FractionsAddSubProperFractions"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5FractionsAddSubMixedFractions(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.Fractions.AddSubMixedFractions.AddSubMixedFractions().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5FractionsAddSubMixedFractions"
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
                   
        Config.template_values = Problems.Primary5.Fractions.AddSubMixedFractions.AddSubMixedFractions().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5FractionsAddSubMixedFractions"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)
        
class P5FractionsMultProperImproperFractions(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        #Config.template_values = Problems.Primary5.Fractions.MultProperImproperFractions.MultProperImproperFractions().GenerateProblemSequential(LastProblemID)
        Config.template_values = Problems.Primary5.Fractions.MultProperImproperFractions.MultProperImproperFractions().GenerateProblem()      
        Config.template_values["concept"] = "P5FractionsMultProperImproperFractions"
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
                   
        #Config.template_values = Problems.Primary5.Fractions.MultProperImproperFractions.MultProperImproperFractions().GenerateProblemSequential(LastProblemID)
        Config.template_values = Problems.Primary5.Fractions.MultProperImproperFractions.MultProperImproperFractions().GenerateProblem()      
        Config.template_values["concept"] = "P5FractionsMultProperImproperFractions"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)        

class P5FractionsMultMixedFractions(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        #Config.template_values = Problems.Primary5.Fractions.MultMixedFractions.MultMixedFractions().GenerateProblemSequential(LastProblemID)
        Config.template_values = Problems.Primary5.Fractions.MultMixedFractions.MultMixedFractions().GenerateProblem()      
        Config.template_values["concept"] = "P5FractionsMultMixedFractions"
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
                   
        #Config.template_values = Problems.Primary5.Fractions.MultMixedFractions.MultMixedFractions().GenerateProblemSequential(LastProblemID)
        Config.template_values = Problems.Primary5.Fractions.MultMixedFractions.MultMixedFractions().GenerateProblem()      
        Config.template_values["concept"] = "P5FractionsMultMixedFractions"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)
        
class P5FractionsDivideProperFractions(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        #Config.template_values = Problems.Primary5.Fractions.DivideProperFractions.DivideProperFractions().GenerateProblemSequential(LastProblemID)
        Config.template_values = Problems.Primary5.Fractions.DivideProperFractions.DivideProperFractions().GenerateProblem()      
        Config.template_values["concept"] = "P5FractionsDivideProperFractions"
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
                   
        #Config.template_values = Problems.Primary5.Fractions.DivideProperFractions.DivideProperFractions().GenerateProblemSequential(LastProblemID)
        Config.template_values = Problems.Primary5.Fractions.DivideProperFractions.DivideProperFractions().GenerateProblem()      
        Config.template_values["concept"] = "P5FractionsDivideProperFractions"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)        
        
class P5FractionsWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.Fractions.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        #Config.template_values = Problems.Primary5.Fractions.WordProblems.WordProblems().GenerateProblem()      
        Config.template_values["concept"] = "P5FractionsWordProblems"
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
                   
        Config.template_values = Problems.Primary5.Fractions.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        #Config.template_values = Problems.Primary5.Fractions.WordProblems.WordProblems().GenerateProblem()      
        Config.template_values["concept"] = "P5FractionsWordProblems"
        template_name = Config.template_values["template"]
        return self.render_template(template_name, **Config.template_values)
    
class P5DecimalsMultiplyDivide(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.Decimals.MultiplyDivide.MultiplyDivide().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5DecimalsMultiplyDivide"
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
                   
        Config.template_values = Problems.Primary5.Decimals.MultiplyDivide.MultiplyDivide().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5DecimalsMultiplyDivide"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5DecimalsRounding(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.Decimals.Rounding.Rounding().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5DecimalsRounding"
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
                   
        Config.template_values = Problems.Primary5.Decimals.Rounding.Rounding().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5DecimalsRounding"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5DecimalsWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.Decimals.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5DecimalsWordProblems"
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
                   
        Config.template_values = Problems.Primary5.Decimals.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5DecimalsWordProblems"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5PercentageExpressAsPercent(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.Percentage.ExpressAsPercent.ExpressAsPercent().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5PercentageExpressAsPercent"
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
                   
        Config.template_values = Problems.Primary5.Percentage.ExpressAsPercent.ExpressAsPercent().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5PercentageExpressAsPercent"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5PercentageExpressAsDecimal(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        Config.template_values = Problems.Primary5.Percentage.ExpressAsDecimal.ExpressAsDecimal().GenerateProblem()    
        Config.template_values["concept"] = "P5PercentageExpressAsDecimal"
        template_name = Config.template_values["template"]

        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):
        Config.template_values = Problems.Primary5.Percentage.ExpressAsDecimal.ExpressAsDecimal().GenerateProblem()    
        Config.template_values["concept"] = "P5PercentageExpressAsDecimal"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5PercentageExpressAsFraction(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        Config.template_values = Problems.Primary5.Percentage.ExpressAsFraction.ExpressAsFraction().GenerateProblem()    
        Config.template_values["concept"] = "P5PercentageExpressAsFraction"
        template_name = Config.template_values["template"]

        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):
        Config.template_values = Problems.Primary5.Percentage.ExpressAsFraction.ExpressAsFraction().GenerateProblem()    
        Config.template_values["concept"] = "P5PercentageExpressAsFraction"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5PercentageWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.Percentage.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5PercentageWordProblems"
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
                   
        Config.template_values = Problems.Primary5.Percentage.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5PercentageWordProblems"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5RatioSimplestForm(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        Config.template_values = Problems.Primary5.Ratio.SimplestForm.SimplestForm().GenerateProblem()    
        Config.template_values["concept"] = "P5RatioSimplestForm"
        template_name = Config.template_values["template"]

        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):
        Config.template_values = Problems.Primary5.Ratio.SimplestForm.SimplestForm().GenerateProblem()    
        Config.template_values["concept"] = "P5RatioSimplestForm"
        template_name = Config.template_values["template"]
        return self.render_template(template_name, **Config.template_values)

class P5RatioMissingNumber(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        Config.template_values = Problems.Primary5.Ratio.MissingNumber.MissingNumber().GenerateProblem()    
        Config.template_values["concept"] = "P5RatioMissingNumber"
        template_name = Config.template_values["template"]

        Problem_Details =  self.render_template(template_name, **Config.template_values)
        Config.template_values = {'Problem_Details':Problem_Details}
        return self.render_response('Practice_Question_Page.html', **Config.template_values)

    @practice_login_required
    def post(self, **kwargs):
        Config.template_values = Problems.Primary5.Ratio.MissingNumber.MissingNumber().GenerateProblem()    
        Config.template_values["concept"] = "P5RatioMissingNumber"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5RatioWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.Ratio.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5RatioWordProblems"
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
                   
        Config.template_values = Problems.Primary5.Ratio.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5RatioWordProblems"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)
    
class P5MeasurementUnitConversion(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.Measurement.UnitConversion.UnitConversion().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5MeasurementUnitConversion"
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
                   
        Config.template_values = Problems.Primary5.Measurement.UnitConversion.UnitConversion().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5MeasurementUnitConversion"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5MeasurementAreaOfTriangle(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.Measurement.AreaOfTriangle.AreaOfTriangle().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5MeasurementAreaOfTriangle"
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
                   
        Config.template_values = Problems.Primary5.Measurement.AreaOfTriangle.AreaOfTriangle().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5MeasurementAreaOfTriangle"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5MeasurementVolume(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
                   
        Config.template_values = Problems.Primary5.Measurement.Volume.Volume().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5MeasurementVolume"
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
                   
        Config.template_values = Problems.Primary5.Measurement.Volume.Volume().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5MeasurementVolume"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5MeasurementWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary5.Measurement.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5MeasurementWordProblems"
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
        
        Config.template_values = Problems.Primary5.Measurement.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5MeasurementWordProblems"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)
    
class P5GeometryAngles(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary5.Geometry.Angles.Angles().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5GeometryAngles"
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
        
        Config.template_values = Problems.Primary5.Geometry.Angles.Angles().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5GeometryAngles"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5GeometryTriangles(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary5.Geometry.Triangles.Triangles().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5GeometryTriangles"
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
        
        Config.template_values = Problems.Primary5.Geometry.Triangles.Triangles().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5GeometryTriangles"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P5GeometryFourSided(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary5.Geometry.FourSidedFigures.FourSidedFigures().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5GeometryFourSided"
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
        
        Config.template_values = Problems.Primary5.Geometry.FourSidedFigures.FourSidedFigures().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5GeometryFourSided"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P5DataAnalysisAverage(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary5.DataAnalysis.FindAverage.FindAverage().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5DataAnalysisAverage"
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
        
        Config.template_values = Problems.Primary5.DataAnalysis.FindAverage.FindAverage().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5DataAnalysisAverage"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5DataAnalysisTotal(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary5.DataAnalysis.FindTotal.FindTotal().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5DataAnalysisTotal"
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
        
        Config.template_values = Problems.Primary5.DataAnalysis.FindTotal.FindTotal().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5DataAnalysisTotal"
        template_name = Config.template_values["template"]

        return self.render_template(template_name, **Config.template_values)

class P5DataAnalysisWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary5.DataAnalysis.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5DataAnalysisWordProblems"
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
        
        Config.template_values = Problems.Primary5.DataAnalysis.WordProblems.WordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P5DataAnalysisWordProblems"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

app = Tipfy(rules=rules, config=config)

def main():
    app.run()

if __name__ == "__main__":
    main()