'''
Created on Sep 26, 2011

Module: Primary6Problems
Generates  problems for Primary 6

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''
import Problems.Primary6.Algebra.SimplifyingAlgebra
import Problems.Primary6.Algebra.EvaluationAlgebra
import Problems.Primary6.Fractions.DivideWholeNumber
import Problems.Primary6.Fractions.DivideProperFraction
import Problems.Primary6.Percentage.WholePart
import Problems.Primary6.Percentage.PercentIncDec
import Problems.Primary6.Speed.DistanceTimeSpeed
import Problems.Primary6.Measurement.CircleCircumference
import Problems.Primary6.Measurement.CircleRadiusDiameter
import Problems.Primary6.Measurement.CircleArea
import Problems.Primary6.Measurement.SemiCirclePerimeter
import Problems.Primary6.Measurement.SemiCircleArea
import Problems.Primary6.Measurement.CompositeFigures
import Problems.Primary6.Measurement.VolumeOfCubeCuboid
import Problems.Primary6.Ratio.P6RTWordProblems
import Problems.Primary6.DataAnalysis.P6DAWordProblems
import Problems.Primary6.Algebra.P6AGWordProblems
import Problems.Primary6.Fractions.P6FRWordProblems
import Problems.Primary6.Speed.P6SPWordProblems
import Problems.Primary6.Percentage.P6PRWordProblems
import Config
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
import CodeTranslation
import SaveProblem

rules = [Rule('/Grade_6_Math_Practice/Algebra_Simplify_Expressions', endpoint='', handler='Primary6Problems.P6AGSimplifyingExpression'),
         Rule('/Grade_6_Math_Practice/Algebra_Evaluate_Expressions', endpoint='', handler='Primary6Problems.P6AGEvaluationExpression'),        
         Rule('/Grade_6_Math_Practice/Divide_Whole_Number_Proper_Fraction', endpoint='', handler='Primary6Problems.P6FRDivideWholeNumber'),
         Rule('/Grade_6_Math_Practice/Divide_Proper_Fraction_by_Proper_Fraction', endpoint='', handler='Primary6Problems.P6FRDivideProperFraction'),         
         Rule('/Grade_6_Math_Practice/Percentage_Find_Whole_Given_Part', endpoint='', handler='Primary6Problems.P6PRFindWhole'),
         Rule('/Grade_6_Math_Practice/Percentage_Increase_Decrease', endpoint='', handler='Primary6Problems.P6PRIncDec'),
         Rule('/Grade_6_Math_Practice/Speed_Distance_Time', endpoint='', handler='Primary6Problems.P6SPDTS'),
         Rule('/Grade_6_Math_Practice/Measurement_Circle_Radius_Diameter', endpoint='', handler='Primary6Problems.P6MTRadius'),
         Rule('/Grade_6_Math_Practice/Measurement_Circle_Circumference', endpoint='', handler='Primary6Problems.P6MTCircumference'),
         Rule('/Grade_6_Math_Practice/Measurement_Circle_Area', endpoint='', handler='Primary6Problems.P6MTArea'),
         Rule('/Grade_6_Math_Practice/Measurement_Semi_Circle_Quadrant_Perimeter', endpoint='', handler='Primary6Problems.P6MTSemiPerimeter'),
         Rule('/Grade_6_Math_Practice/Measurement_Semi_Circle_Quadrant_Area', endpoint='', handler='Primary6Problems.P6MTSemiArea'),
         Rule('/Grade_6_Math_Practice/Area_Perimeter_of_Composite_Figures', endpoint='', handler='Primary6Problems.P6MTComposite'),
         Rule('/Grade_6_Math_Practice/Measurement_Volume_Cube_Cuboid', endpoint='', handler='Primary6Problems.P6MTVolume'),
         Rule('/Grade_6_Math_Practice/Ratio_Word_Problems', endpoint='', handler='Primary6Problems.P6RTWordProblems'),
         Rule('/Grade_6_Math_Practice/Data_Analysis_Pie_Chart', endpoint='', handler='Primary6Problems.P6DAWordProblems'),
         Rule('/Grade_6_Math_Practice/Algebra_Word_Problems', endpoint='', handler='Primary6Problems.P6AGWordProblems'),
         Rule('/Grade_6_Math_Practice/Fractions_Word_Problems', endpoint='', handler='Primary6Problems.P6FRWordProblems'),
         Rule('/Grade_6_Math_Practice/Speed_Word_Problems', endpoint='', handler='Primary6Problems.P6SPWordProblems'),
         Rule('/Grade_6_Math_Practice/Percentage_Word_Problems', endpoint='', handler='Primary6Problems.P6PRWordProblems'),
         
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
            'concept_display_full':"<a href='Primary_Grade_6_Mathematics'><font style='text-decoration:underline'>Grade 6</font></a> -- "+CodeTranslation.MainConcept[concept]+" -- "+concept_display,
            'practice_page':"/Primary_Grade_6_Mathematics",
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
    
class P6AGSimplifyingExpression(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Algebra.SimplifyingAlgebra.SimplifyingAlgebra().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6AGSimplifyingExpression"
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
        
        Config.template_values = Problems.Primary6.Algebra.SimplifyingAlgebra.SimplifyingAlgebra().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6AGSimplifyingExpression"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6AGEvaluationExpression(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Algebra.EvaluationAlgebra.EvaluationAlgebra().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6AGEvaluationExpression"
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
        
        Config.template_values = Problems.Primary6.Algebra.EvaluationAlgebra.EvaluationAlgebra().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6AGEvaluationExpression"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6FRDivideWholeNumber(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Fractions.DivideWholeNumber.DivideWholeNumber().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6FRDivideWholeNumber"
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
        
        Config.template_values = Problems.Primary6.Fractions.DivideWholeNumber.DivideWholeNumber().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6FRDivideWholeNumber"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6FRDivideProperFraction(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Fractions.DivideProperFraction.DivideProperFraction().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6FRDivideProperFraction"
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
        
        Config.template_values = Problems.Primary6.Fractions.DivideProperFraction.DivideProperFraction().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6FRDivideProperFraction"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)   

class P6PRFindWhole(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Percentage.WholePart.WholePart().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6PRFindWhole"
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
        
        Config.template_values = Problems.Primary6.Percentage.WholePart.WholePart().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6PRFindWhole"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6PRIncDec(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Percentage.PercentIncDec.PercentIncDec().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6PRIncDec"
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
        
        Config.template_values = Problems.Primary6.Percentage.PercentIncDec.PercentIncDec().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6PRIncDec"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6SPDTS(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Speed.DistanceTimeSpeed.DistanceTimeSpeed().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6SPDTS"
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
        
        Config.template_values = Problems.Primary6.Speed.DistanceTimeSpeed.DistanceTimeSpeed().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6SPDTS"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6MTRadius(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Measurement.CircleRadiusDiameter.CircleRadiusDiameter().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTRadius"
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
        
        Config.template_values = Problems.Primary6.Measurement.CircleRadiusDiameter.CircleRadiusDiameter().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTRadius"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6MTCircumference(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Measurement.CircleCircumference.CircleCircumference().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTCircumference"
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
        
        Config.template_values = Problems.Primary6.Measurement.CircleCircumference.CircleCircumference().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTCircumference"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6MTArea(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Measurement.CircleArea.CircleArea().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTArea"
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
        
        Config.template_values = Problems.Primary6.Measurement.CircleArea.CircleArea().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTArea"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6MTSemiPerimeter(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Measurement.SemiCirclePerimeter.SemiCirclePerimeter().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTSemiPerimeter"
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
        
        Config.template_values = Problems.Primary6.Measurement.SemiCirclePerimeter.SemiCirclePerimeter().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTSemiPerimeter"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6MTSemiArea(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Measurement.SemiCircleArea.SemiCircleArea().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTSemiArea"
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
        
        Config.template_values = Problems.Primary6.Measurement.SemiCircleArea.SemiCircleArea().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTSemiArea"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6MTComposite(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Measurement.CompositeFigures.CompositeFigures().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTComposite"
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
        
        Config.template_values = Problems.Primary6.Measurement.CompositeFigures.CompositeFigures().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTComposite"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6MTVolume(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Measurement.VolumeOfCubeCuboid.VolumeOfCubeCuboid().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTVolume"
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
        
        Config.template_values = Problems.Primary6.Measurement.VolumeOfCubeCuboid.VolumeOfCubeCuboid().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6MTVolume"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6RTWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Ratio.P6RTWordProblems.P6RTWordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6RTWordProblems"
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
        
        Config.template_values = Problems.Primary6.Ratio.P6RTWordProblems.P6RTWordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6RTWordProblems"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6DAWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.DataAnalysis.P6DAWordProblems.P6DAWordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6DAWordProblems"
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
        
        Config.template_values = Problems.Primary6.DataAnalysis.P6DAWordProblems.P6DAWordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6DAWordProblems"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6AGWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Algebra.P6AGWordProblems.P6AGWordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6AGWordProblems"
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
        
        Config.template_values = Problems.Primary6.Algebra.P6AGWordProblems.P6AGWordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6AGWordProblems"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6FRWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Fractions.P6FRWordProblems.P6FRWordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6FRWordProblems"
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
        
        Config.template_values = Problems.Primary6.Fractions.P6FRWordProblems.P6FRWordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6FRWordProblems"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6SPWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Speed.P6SPWordProblems.P6SPWordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6SPWordProblems"
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
        
        Config.template_values = Problems.Primary6.Speed.P6SPWordProblems.P6SPWordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6SPWordProblems"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)

class P6PRWordProblems(BaseHandler):
    @practice_login_required
    def get(self, **kwargs):     
        problem_type = memcache.Client().get(unicode(self.auth.user.username)+'_problem_type')
        if not problem_type:
            LastProblemID = 0
        else:
            LastProblemID = problem_type
        
        Config.template_values = Problems.Primary6.Percentage.P6PRWordProblems.P6PRWordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6PRWordProblems"
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
        
        Config.template_values = Problems.Primary6.Percentage.P6PRWordProblems.P6PRWordProblems().GenerateProblemSequential(LastProblemID)
        Config.template_values["concept"] = "P6PRWordProblems"
        template_name = Config.template_values["template"]       

        return self.render_template(template_name, **Config.template_values)
                                                                                    
app = Tipfy(rules=rules, config=config)

def main():
    app.run()

if __name__ == "__main__":
    main()