'''
Created on May 18, 2012

@author: Farhat
'''
from tipfy import RequestHandler
from tipfy import Rule
from Config import config
import Config
from tipfy import Tipfy
from tipfy.auth import login_required,UserRequiredIfAuthenticatedMiddleware
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from HCTests import HCTests
from google.appengine.api import memcache
import logging
from Reports import Reports
from Database import HCSubscription, TestsMaster
from HCWorksheets import HCWorksheets
import CodeTranslation

rules = [
         Rule('/Elementary_Mathematics_Worksheets', endpoint='', handler='GenerateWorksheets.Worksheets'),
         Rule('/Grade_3_Math_Worksheets', endpoint='', handler='GenerateWorksheets.GenerateP3Worksheets'),
         Rule('/Grade_4_Math_Worksheets', endpoint='', handler='GenerateWorksheets.GenerateP4Worksheets'),
         Rule('/Grade_5_Math_Worksheets', endpoint='', handler='GenerateWorksheets.GenerateP5Worksheets'),
         Rule('/Grade_6_Math_Worksheets', endpoint='', handler='GenerateWorksheets.GenerateP6Worksheets'),
         Rule('/Grade_4_Math_Worksheets/Whole_Numbers', endpoint='', handler='GenerateWorksheets.GenerateP4WNWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Whole_Numbers_Write_Figures', endpoint='', handler='GenerateWorksheets.GenerateP4WholeNumbersWriteInFiguresWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Whole_Numbers_Write_Words', endpoint='', handler='GenerateWorksheets.GenerateP4WholeNumbersWriteInWordsWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Whole_Numbers_Place_Values', endpoint='', handler='GenerateWorksheets.GenerateP4WholeNumbersPlaceValuesWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Whole_Numbers_Comparing_Ordering', endpoint='', handler='GenerateWorksheets.GenerateP4WholeNumbersComparingOrderingWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Whole_Numbers_Rounding_Off', endpoint='', handler='GenerateWorksheets.GenerateP4WholeNumbersRoundingOffWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Whole_Numbers_Factors_Multiples', endpoint='', handler='GenerateWorksheets.GenerateP4WholeNumbersFactorMultipleWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Whole_Numbers_Multiplication_Division', endpoint='', handler='GenerateWorksheets.GenerateP4WholeNumbersMutliplyDivideWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Whole_Numbers_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP4WNWordProblemsWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Fractions', endpoint='', handler='GenerateWorksheets.GenerateP4FRWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Fractions_Simplifying', endpoint='', handler='GenerateWorksheets.GenerateP4FractionsSimplifyingWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Mixed_Numbers_Improper_Fractions', endpoint='', handler='GenerateWorksheets.GenerateP4FractionsMixedImproperWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Fractions_Add_Like', endpoint='', handler='GenerateWorksheets.GenerateP4FractionsAddWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Fractions_Subtract_Like', endpoint='', handler='GenerateWorksheets.GenerateP4FractionsSubtractWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Fractions_Multiplication', endpoint='', handler='GenerateWorksheets.GenerateP4FractionsMultiplicationWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Fractions_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP4FRWordProblemsWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Data_Analysis', endpoint='', handler='GenerateWorksheets.GenerateP4DAWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Data_Analysis_Tables_Bar_Graphs', endpoint='', handler='GenerateWorksheets.GenerateP4DATablesBarGraphsWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Data_Analysis_Line_Graphs', endpoint='', handler='GenerateWorksheets.GenerateP4DALineGraphsWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Decimals', endpoint='', handler='GenerateWorksheets.GenerateP4DCWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Decimals_Tenths', endpoint='', handler='GenerateWorksheets.GenerateP4DecimalsTenthsWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Decimals_Hundredths', endpoint='', handler='GenerateWorksheets.GenerateP4DecimalsHundredthsWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Decimals_Thousandths', endpoint='', handler='GenerateWorksheets.GenerateP4DecimalsThousandthsWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Decimals_Comparing_Ordering', endpoint='', handler='GenerateWorksheets.GenerateP4DecimalsComparingOrderingWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Decimals_Rounding_Off', endpoint='', handler='GenerateWorksheets.GenerateP4DecimalsRoundingOffWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Decimals_Fractions', endpoint='', handler='GenerateWorksheets.GenerateP4DecimalsFractionsWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Decimals_Addition_Subtraction', endpoint='', handler='GenerateWorksheets.GenerateP4DecimalsAddSubWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Decimals_Multiplication_Division', endpoint='', handler='GenerateWorksheets.GenerateP4DecimalsMultiplyDivideWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Decimals_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP4DCWordProblemsWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Measurement', endpoint='', handler='GenerateWorksheets.GenerateP4MTWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Measurement_24-Hour_Clock', endpoint='', handler='GenerateWorksheets.GenerateP4MTTime24HrsWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Measurement_Time_Duration', endpoint='', handler='GenerateWorksheets.GenerateP4MTTimeDurationWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Perimeter_Rectangle_Squares', endpoint='', handler='GenerateWorksheets.GenerateP4MTPerimeterWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Area_Rectangle_Squares', endpoint='', handler='GenerateWorksheets.GenerateP4MTAreaWorksheets'),
         Rule('/Grade_4_Math_Worksheets/Measurement_Composite_Figures', endpoint='', handler='GenerateWorksheets.GenerateP4MTCompositeFiguresWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Whole_Numbers', endpoint='', handler='GenerateWorksheets.GenerateP5WNWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Whole_Numbers_Write_Words', endpoint='', handler='GenerateWorksheets.GenerateP5WholeNumbersWriteInWordsWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Whole_Numbers_Write_Figures', endpoint='', handler='GenerateWorksheets.GenerateP5WholeNumbersWriteInFiguresWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Whole_Numbers_Place_Values', endpoint='', handler='GenerateWorksheets.GenerateP5WholeNumbersPlaceValueWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Whole_Numbers_Comparing_Ordering', endpoint='', handler='GenerateWorksheets.GenerateP5WholeNumbersComparingAndOrderingWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Whole_Numbers_Find_Pattern', endpoint='', handler='GenerateWorksheets.GenerateP5WholeNumbersFindPatternWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Whole_Numbers_Approximation_Estimation', endpoint='', handler='GenerateWorksheets.GenerateP5WholeNumbersApproximationEstimationWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Whole_Numbers_Multiplication_Division', endpoint='', handler='GenerateWorksheets.GenerateP5WholeNumbersMultiplyDivideWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Whole_Numbers_Order_Operations', endpoint='', handler='GenerateWorksheets.GenerateP5WholeNumbersOrderOfOperationWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Whole_Numbers_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP5WholeNumbersWordProblemsWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Fractions', endpoint='', handler='GenerateWorksheets.GenerateP5FRWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Fractions_Add_Subtract_Proper', endpoint='', handler='GenerateWorksheets.GenerateP5FractionsAddSubProperFractionsWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Fractions_Add_Subtract_Mixed', endpoint='', handler='GenerateWorksheets.GenerateP5FractionsAddSubMixedFractionsWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Fractions_Multiply_Proper_Improper', endpoint='', handler='GenerateWorksheets.GenerateP5FractionsMultProperImproperFractionsWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Fractions_Multiply_Mixed', endpoint='', handler='GenerateWorksheets.GenerateP5FractionsMultMixedFractionsWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Fractions_Divide', endpoint='', handler='GenerateWorksheets.GenerateP5FractionsDivideProperFractionsWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Fractions_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP5FractionsWordProblemsWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Decimals', endpoint='', handler='GenerateWorksheets.GenerateP5DCWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Decimals_Multiply_Divide', endpoint='', handler='GenerateWorksheets.GenerateP5DecimalsMultiplyDivideWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Decimals_Rounding_Off', endpoint='', handler='GenerateWorksheets.GenerateP5DecimalsRoundingWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Decimals_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP5DecimalsWordProblemsWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Percentage', endpoint='', handler='GenerateWorksheets.GenerateP5PRWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Percentage_Express_Percentage', endpoint='', handler='GenerateWorksheets.GenerateP5PercentageExpressAsPercentWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Percentage_Express_Decimal', endpoint='', handler='GenerateWorksheets.GenerateP5PercentageExpressAsDecimalWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Percentage_Express_Fraction', endpoint='', handler='GenerateWorksheets.GenerateP5PercentageExpressAsFractionWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Percentage_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP5PercentageWordProblemsWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Ratio', endpoint='', handler='GenerateWorksheets.GenerateP5RTWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Ratio_Simplest_Form', endpoint='', handler='GenerateWorksheets.GenerateP5RatioSimplestFormWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Ratio_Missing_Number', endpoint='', handler='GenerateWorksheets.GenerateP5RatioMissingNumberWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Ratio_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP5RatioWordProblemsWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Measurement', endpoint='', handler='GenerateWorksheets.GenerateP5MTWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Measurement_Unit_Conversion', endpoint='', handler='GenerateWorksheets.GenerateP5MeasurementUnitConversionWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Measurement_Area_Triangle', endpoint='', handler='GenerateWorksheets.GenerateP5MeasurementAreaOfTriangleWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Measurement_Volume_Cube_Cuboid', endpoint='', handler='GenerateWorksheets.GenerateP5MeasurementVolumeWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Measurement_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP5MeasurementWordProblemsWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Geometry', endpoint='', handler='GenerateWorksheets.GenerateP5GTWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Geometry_Angles', endpoint='', handler='GenerateWorksheets.GenerateP5GeometryAnglesWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Geometry_Triangles', endpoint='', handler='GenerateWorksheets.GenerateP5GeometryTrianglesWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Geometry_Four_Sided_Figures', endpoint='', handler='GenerateWorksheets.GenerateP5GeometryFourSidedWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Data_Analysis', endpoint='', handler='GenerateWorksheets.GenerateP5DAWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Data_Analysis_Find_Average', endpoint='', handler='GenerateWorksheets.GenerateP5DataAnalysisAverageWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Data_Analysis_Find_Total', endpoint='', handler='GenerateWorksheets.GenerateP5DataAnalysisTotalWorksheets'),
         Rule('/Grade_5_Math_Worksheets/Data_Analysis_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP5DataAnalysisWordProblemsWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Algebra', endpoint='', handler='GenerateWorksheets.GenerateP6AGWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Algebra_Simplify_Expressions', endpoint='', handler='GenerateWorksheets.GenerateP6AGSimplifyingExpressionWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Algebra_Evaluate_Expressions', endpoint='', handler='GenerateWorksheets.GenerateP6AGEvaluationExpressionWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Algebra_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP6AGWordProblemsWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Fractions', endpoint='', handler='GenerateWorksheets.GenerateP6FRWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Fractions_Divide_Whole_Number', endpoint='', handler='GenerateWorksheets.GenerateP6FRDivideWholeNumberWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Fractions_Divide_Proper', endpoint='', handler='GenerateWorksheets.GenerateP6FRDivideProperFractionWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Fractions_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP6FRWordProblemsWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Speed', endpoint='', handler='GenerateWorksheets.GenerateP6SPWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Speed_Distance_Time', endpoint='', handler='GenerateWorksheets.GenerateP6SPDTSWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Speed_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP6SPWordProblemsWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Ratio', endpoint='', handler='GenerateWorksheets.GenerateP6RTWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Percentage', endpoint='', handler='GenerateWorksheets.GenerateP6PRWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Percentage_Find_Whole_Given_Part', endpoint='', handler='GenerateWorksheets.GenerateP6PRFindWholeWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Percentage_Increase_Decrease', endpoint='', handler='GenerateWorksheets.GenerateP6PRIncDecWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Percentage_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP6PRWordProblemsWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Data_Analysis', endpoint='', handler='GenerateWorksheets.GenerateP6DAWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Data_Analysis_Pie_Chart', endpoint='', handler='GenerateWorksheets.GenerateP6DAWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Measurement', endpoint='', handler='GenerateWorksheets.GenerateP6MTWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Measurement_Circle_Radius_Diameter', endpoint='', handler='GenerateWorksheets.GenerateP6MTRadiusWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Measurement_Circle_Circumference', endpoint='', handler='GenerateWorksheets.GenerateP6MTCircumferenceWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Measurement_Circle_Area', endpoint='', handler='GenerateWorksheets.GenerateP6MTAreaWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Measurement_Semi_Circle_Quadrant_Perimeter', endpoint='', handler='GenerateWorksheets.GenerateP6MTSemiPerimeterWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Measurement_Semi_Circle_Quadrant_Area', endpoint='', handler='GenerateWorksheets.GenerateP6MTSemiAreaWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Measurement_Composite_Figures', endpoint='', handler='GenerateWorksheets.GenerateP6MTCompositeWorksheets'),
         Rule('/Grade_6_Math_Worksheets/Measurement_Volume_Cube_Cuboid', endpoint='', handler='GenerateWorksheets.GenerateP6MTVolumeWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Whole_Numbers', endpoint='', handler='GenerateWorksheets.GenerateP3WNWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Whole_Numbers_Number_Notation_Place_Values', endpoint='', handler='GenerateWorksheets.GenerateP3WNPlaceValuesWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Whole_Numbers_Figures_to_Words', endpoint='', handler='GenerateWorksheets.GenerateP3WNFiguresToWordsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Whole_Numbers_Words_to_Figures', endpoint='', handler='GenerateWorksheets.GenerateP3WNWordsToFiguresWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Whole_Numbers_Comparing_Ordering', endpoint='', handler='GenerateWorksheets.GenerateP3WNComparingOrderingWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Whole_Numbers_Patterns', endpoint='', handler='GenerateWorksheets.GenerateP3WNNumberPatternsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Whole_Numbers_Addition', endpoint='', handler='GenerateWorksheets.GenerateP3WNAdditionWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Whole_Numbers_Subtraction', endpoint='', handler='GenerateWorksheets.GenerateP3WNSubtractionWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Whole_Numbers_Multiplication', endpoint='', handler='GenerateWorksheets.GenerateP3WNMultiplicationWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Whole_Numbers_Division', endpoint='', handler='GenerateWorksheets.GenerateP3WNDivisionWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Whole_Numbers_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP3WNWordProblemsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Money', endpoint='', handler='GenerateWorksheets.GenerateP3MOWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Money_Addition', endpoint='', handler='GenerateWorksheets.GenerateP3MOAdditionWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Money_Subtraction', endpoint='', handler='GenerateWorksheets.GenerateP3MOSubtractionWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Money_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP3MOWordProblemsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Time', endpoint='', handler='GenerateWorksheets.GenerateP3TIWorksheets'),         
         Rule('/Grade_3_Math_Worksheets/Telling_Time', endpoint='', handler='GenerateWorksheets.GenerateP3TITellingTimeWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Time_Conversion_Hours_Minutes', endpoint='', handler='GenerateWorksheets.GenerateP3TIConversionTimeWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Time_Addition', endpoint='', handler='GenerateWorksheets.GenerateP3TIAdditionWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Time_Subtraction', endpoint='', handler='GenerateWorksheets.GenerateP3TISubtractionWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Time_Finding_Duration_Start_Finish', endpoint='', handler='GenerateWorksheets.GenerateP3TIDurationWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Time_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP3TIWordProblemsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Length_Mass_Volume', endpoint='', handler='GenerateWorksheets.GenerateP3LMWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Metres_Centimetres', endpoint='', handler='GenerateWorksheets.GenerateP3LMMetreCentiMetreWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Kilometres_Metres', endpoint='', handler='GenerateWorksheets.GenerateP3LMKiloMetreWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Kilograms_Grams', endpoint='', handler='GenerateWorksheets.GenerateP3LMKiloGramWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Litres_Millilitres', endpoint='', handler='GenerateWorksheets.GenerateP3LMLitresMilliWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Length_Mass_Volume_1-Step_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP3LMWordProblemsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Length_Mass_Volume_2-Step_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP3LMWordProblems_2StepsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Angles', endpoint='', handler='GenerateWorksheets.GenerateP3ANWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Identifying_Angles_in_Figures', endpoint='', handler='GenerateWorksheets.GenerateP3ANIdentifyingWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Right_Angles', endpoint='', handler='GenerateWorksheets.GenerateP3ANRightAngleWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Bar_Graphs', endpoint='', handler='GenerateWorksheets.GenerateP3BGBarGraphsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Area_in_Square_Units', endpoint='', handler='GenerateWorksheets.GenerateP3APSquareUnitsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Area_in_Square_cm_Square_m', endpoint='', handler='GenerateWorksheets.GenerateP3APSquareCmMWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Area_of_Squares_Rectangles', endpoint='', handler='GenerateWorksheets.GenerateP3APAreaWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Perimeter_of_Squares_Rectangles', endpoint='', handler='GenerateWorksheets.GenerateP3APPerimeterWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Area_Perimeter_Word_Problems', endpoint='', handler='GenerateWorksheets.GenerateP3APWordProblemsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/What_is_a_Fraction', endpoint='', handler='GenerateWorksheets.GenerateP3FRWhatIsFractionsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Equivalent-Fraction', endpoint='', handler='GenerateWorksheets.GenerateP3FREquivalentFractionsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Simplifying-Fractions', endpoint='', handler='GenerateWorksheets.GenerateP3FRSimplifyingFractionsWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Comparing-and-Ordering-Fractions', endpoint='', handler='GenerateWorksheets.GenerateP3FRComparingOrderingWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Adding-Fractions', endpoint='', handler='GenerateWorksheets.GenerateP3FRAdditionWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Subtracting-Fractions', endpoint='', handler='GenerateWorksheets.GenerateP3FRSubtractionWorksheets'),
         Rule('/Grade_3_Math_Worksheets/Identifying_Perpendicular_Parallel_Lines', endpoint='', handler='GenerateWorksheets.GenerateP3PPPerpendicularParallelWorksheets'),
         
         Rule('/Tests', endpoint='', handler='GenerateWorksheets.Worksheets'),
         Rule('/Worksheets/GenerateWorksheets', endpoint='', handler='GenerateWorksheets.GenerateWorksheets'),
         Rule('/Tests/GetTest', endpoint='', handler='GenerateTests.GetTest'),
         Rule('/Tests/GetProblems', endpoint='', handler='GenerateTests.GetTestProblems'),
         Rule('/Tests/GetClickedProblem', endpoint='', handler='GenerateTests.GetClickedProblem'),
         Rule('/Tests/GenerateTestReport', endpoint='', handler='GenerateTests.GenerateTestReport'),
         Rule('/auth/login', endpoint='', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.SignupHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler')         
         ]
      
class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]

    def render_response(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session
        
        if self.auth.user:
            memcache.Client().delete(unicode(self.auth.user.username)+"_test_values")
            memcache.Client().add(unicode(self.auth.user.username)+"_test_values",Config.test_values,3600)        
        
        try:
            counter = Config.test_values['counter']
        except KeyError:
            counter = -1
        
        TRIAL = "N"
        if self.auth.user:
            HCUser = HCSubscription.HCSubscription.gql("where email = '"+self.auth.user.email+"' and status='ACTIVE'").fetch(1)
            for h in HCUser:
                if h.paypal_token in ["TRIAL","WAIVED"]:
                    TRIAL = "Y"

        try:
            concept = Config.test_values['concept']
        except KeyError:
            concept = ""        
        
        TestData = self.TestData(concept)
        WorksheetGenerated = TestData['TestGenerated']
        WorksheetCompleted = TestData['TestCompleted']
        
        if not self.auth.user.authorized and WorksheetCompleted >= 2:
            SubscribeMessage="Y"
        else:
            SubscribeMessage="N"
        if not self.auth.user.authorized and WorksheetGenerated >= 2:
            StopGeneratingWorksheets="Y"
        else:
            StopGeneratingWorksheets="N"        
        
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
            'counter': counter,
            'TRIAL':TRIAL,
            'WorksheetGenerated':WorksheetGenerated+1,
            'SubscribeMessage':SubscribeMessage,
            'StopGeneratingWorksheets':StopGeneratingWorksheets,
            'UnfinishedWorksheetsCount':UnfinishedWorksheetsCount
        })
                    
        return super(BaseHandler, self).render_response(filename, **kwargs)
    
    def TestData(self,concept):
        '''checking if user has complete one test'''
        TestData1 = TestsMaster.TestsMasterTable.gql("where student_id = '"+unicode(self.auth.user)+"' and concept='"+concept+"' and created_by != '"+unicode(self.auth.user)+"'" ).fetch(10000)
        '''Also checking for teacher and parent where student id is not their own'''
        TestData2 = TestsMaster.TestsMasterTable.gql("where created_by = '"+unicode(self.auth.user)+"' and concept='"+concept+"'" ).fetch(10000)
        TestGenerated = 0
        TestCompleted = 0
        for t1 in TestData1:
            TestGenerated = TestGenerated + 1
            if t1.status == 'Completed':
                TestCompleted = TestCompleted + 1
        for t2 in TestData2:
            TestGenerated = TestGenerated + 1
            if t2.status == 'Completed':
                TestCompleted = TestCompleted + 1
        TestData = {'TestCompleted':TestCompleted,'TestGenerated':TestGenerated}
        return TestData
      
class BaseHandlerWorksheets(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]

    def render_response(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session
        
        if self.auth.user:
            memcache.Client().delete(unicode(self.auth.user.username)+"_test_values")
            memcache.Client().add(unicode(self.auth.user.username)+"_test_values",Config.test_values,3600)        
        
        try:
            counter = Config.test_values['counter']
        except KeyError:
            counter = -1
        
        TRIAL = "N"
        if self.auth.user:
            HCUser = HCSubscription.HCSubscription.gql("where email = '"+self.auth.user.email+"' and status='ACTIVE'").fetch(1)
            for h in HCUser:
                if h.paypal_token in ["TRIAL","WAIVED"]:
                    TRIAL = "Y"

        kwargs.update({
            'auth_session': auth_session,
            'current_user': self.auth.user,
            'login_url':    self.auth.login_url(),
            'logout_url':   self.auth.logout_url(),
            'current_url':  self.request.url,
            'counter': counter,
            'TRIAL':TRIAL
        })       
        return super(BaseHandlerWorksheets, self).render_response(filename, **kwargs)
    
class Worksheets(BaseHandlerWorksheets):
    '''To display worksheet concept no login is required and 1 test completed check is also not required for unsubscribed user'''    
    def get(self, **kwargs):
        return self.render_response('Worksheets/Worksheets.html', **Config.test_values)

class GenerateP3Worksheets(BaseHandlerWorksheets):  
    def get(self, **kwargs):               
        return self.render_response('Worksheets/Worksheets_Primary_Grade_3.html', section='content')

class GenerateP4Worksheets(BaseHandlerWorksheets):  
    def get(self, **kwargs):               
        return self.render_response('Worksheets/Worksheets_Primary_Grade_4.html', section='content')

class GenerateP5Worksheets(BaseHandlerWorksheets):  
    def get(self, **kwargs):               
        return self.render_response('Worksheets/Worksheets_Primary_Grade_5.html', section='content')

class GenerateP6Worksheets(BaseHandlerWorksheets):  
    def get(self, **kwargs):               
        return self.render_response('Worksheets/Worksheets_Primary_Grade_6.html', section='content')
    
class GenerateP4WNWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4WN","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Whole Numbers - All Topics","concept":"P4WN","grade":4,"display_concept":"G4_Whole_Numbers",
                                   "SubTopics":"P4WN"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)
    
class GenerateP4WholeNumbersWriteInFiguresWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4WN","P4WholeNumbersWriteInFigures")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Whole Numbers - Write in Figures","concept":"P4WN","grade":4,"display_concept":"G4_Whole_Numbers_Write_Figures",
                                   "SubTopics":"P4WholeNumbersWriteInFigures"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)
    
class GenerateP4WholeNumbersWriteInWordsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4WN","P4WholeNumbersWriteInWords")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Whole Numbers - Write in Words","concept":"P4WN","grade":4,"display_concept":"G4_Whole_Numbers_Write_Words",
                                   "SubTopics":"P4WholeNumbersWriteInWords"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)
    
class GenerateP4WholeNumbersPlaceValuesWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4WN","P4WholeNumbersPlaceValues")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Whole Numbers - Place Values","concept":"P4WN","grade":4,"display_concept":"G4_Whole_Numbers_Place_Values",
                                   "SubTopics":"P4WholeNumbersPlaceValues"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)
    
class GenerateP4WholeNumbersComparingOrderingWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4WN","P4WholeNumbersComparingOrdering")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Whole Numbers - Comparing Ordering","concept":"P4WN","grade":4,"display_concept":"G4_Whole_Numbers_Comparing_Ordering",
                                   "SubTopics":"P4WholeNumbersComparingOrdering"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)
    
class GenerateP4WholeNumbersRoundingOffWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4WN","P4WholeNumbersRoundingOff")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Whole Numbers - Rounding Off","concept":"P4WN","grade":4,"display_concept":"G4_Whole_Numbers_Rounding_Off",
                                   "SubTopics":"P4WholeNumbersRoundingOff"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)
    
class GenerateP4WholeNumbersFactorMultipleWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4WN","P4WholeNumbersFactorMultiple")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Whole Numbers - Factors Multiples","concept":"P4WN","grade":4,"display_concept":"G4_Whole_Numbers_Factors_Multiples",
                                   "SubTopics":"P4WholeNumbersFactorMultiple"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)
    
class GenerateP4WholeNumbersMutliplyDivideWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4WN","P4WholeNumbersMutliplyDivide")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Whole Numbers - Multiplication Division","concept":"P4WN","grade":4,"display_concept":"G4_Whole_Numbers_Multiplication_Division",
                                   "SubTopics":"P4WholeNumbersMutliplyDivide"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)
    
class GenerateP4WNWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4WN","P4WNWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Whole Numbers - Word Problems","concept":"P4WN","grade":4,"display_concept":"G4_Whole_Numbers_Word_Problems",
                                   "SubTopics":"P4WNWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4FRWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4FR","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Fractions - All Topics",
                                   "concept":"P4FR","grade":4,"display_concept":"G4_Fractions","SubTopics":"P4FR"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4FractionsSimplifyingWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4FR","P4FractionsSimplifying")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Fractions - Simplifying",
                                   "concept":"P4FR","grade":4,"display_concept":"G4_Fractions_Simplifying","SubTopics":"P4FractionsSimplifying"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4FractionsMixedImproperWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4FR","P4FractionsMixedImproper")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Fractions - Mixed and Improper",
                                   "concept":"P4FR","grade":4,"display_concept":"G4_Fractions_Mixed_Improper","SubTopics":"P4FractionsMixedImproper"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4FractionsAddWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4FR","P4FractionsAdd")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Fractions - Add Like",
                                   "concept":"P4FR","grade":4,"display_concept":"G4_Fractions_Add_Like","SubTopics":"P4FractionsAdd"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4FractionsSubtractWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4FR","P4FractionsSubtract")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Fractions - Subtract Like",
                                   "concept":"P4FR","grade":4,"display_concept":"G4_Fractions_Subtract_Like","SubTopics":"P4FractionsSubtract"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4FractionsMultiplicationWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4FR","P4FractionsMultiplication")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Fractions - Multiplication",
                                   "concept":"P4FR","grade":4,"display_concept":"G4_Fractions_Multiplication","SubTopics":"P4FractionsMultiplication"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4FRWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4FR","P4FRWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Fractions - Word Problems",
                                   "concept":"P4FR","grade":4,"display_concept":"G4_Fractions_Word_Problems","SubTopics":"P4FRWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DAWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DA","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Data Analysis - All Topics",
                                   "concept":"P4DA","grade":4,"display_concept":"G4_Data_Analysis","SubTopics":"P4DA"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DATablesBarGraphsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DA","P4DATablesBarGraphs")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Data Analysis - Tables/Bar Graphs",
                                   "concept":"P4DA","grade":4,"display_concept":"G4_Data_Analysis_Tables_Bar_Graphs","SubTopics":"P4DATablesBarGraphs"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DALineGraphsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DA","P4DALineGraphs")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Data Analysis - Line Graphs",
                                   "concept":"P4DA","grade":4,"display_concept":"G4_Data_Analysis_Line_Graphs","SubTopics":"P4DALineGraphs"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DCWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DC","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Decimals - All Topics",
                                   "concept":"P4DC","grade":4,"display_concept":"G4_Decimals","SubTopics":"P4DC"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DecimalsTenthsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DC","P4DecimalsTenths")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Decimals - Tenths",
                                   "concept":"P4DC","grade":4,"display_concept":"G4_Decimals_Tenths","SubTopics":"P4DecimalsTenths"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DecimalsHundredthsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DC","P4DecimalsHundredths")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Decimals - Hundredths",
                                   "concept":"P4DC","grade":4,"display_concept":"G4_Decimals_Hundredths","SubTopics":"P4DecimalsHundredths"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DecimalsThousandthsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DC","P4DecimalsThousandths")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Decimals - Thousandths",
                                   "concept":"P4DC","grade":4,"display_concept":"G4_Decimals_Thousandths","SubTopics":"P4DecimalsThousandths"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DecimalsComparingOrderingWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DC","P4DecimalsComparingOrdering")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Decimals - Comparing/Ordering",
                                   "concept":"P4DC","grade":4,"display_concept":"G4_Decimals_Comparing_Ordering","SubTopics":"P4DecimalsComparingOrdering"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DecimalsRoundingOffWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DC","P4DecimalsRoundingOff")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Decimals - Rounding Off",
                                   "concept":"P4DC","grade":4,"display_concept":"G4_Decimals_Rounding_Off","SubTopics":"P4DecimalsRoundingOff"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DecimalsFractionsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DC","P4DecimalsFractions")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Decimals - Fractions",
                                   "concept":"P4DC","grade":4,"display_concept":"G4_Decimals_Fractions","SubTopics":"P4DecimalsFractions"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DecimalsAddSubWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DC","P4DecimalsAddSub")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Decimals - Add Subtract",
                                   "concept":"P4DC","grade":4,"display_concept":"G4_Decimals_Add_Subtract","SubTopics":"P4DecimalsAddSub"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DecimalsMultiplyDivideWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DC","P4DecimalsMultiplyDivide")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Decimals - Multiply Divide",
                                   "concept":"P4DC","grade":4,"display_concept":"G4_Decimals_Multiply_Divide","SubTopics":"P4DecimalsMultiplyDivide"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4DCWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4DC","P4DCWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Decimals - Word Problems",
                                   "concept":"P4DC","grade":4,"display_concept":"G4_Decimals_Word_Problems","SubTopics":"P4DCWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4MTWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4MT", "All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Measurement - All Topics",
                                   "concept":"P4MT","grade":4,"display_concept":"G4_Measurement","SubTopics":"P4MT"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4MTTime24HrsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4MT", "P4MTTime24Hrs")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Measurement - 24-Hour Clock",
                                   "concept":"P4MT","grade":4,"display_concept":"G4_Measurement_24-Hour_Clock","SubTopics":"P4MTTime24Hrs"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4MTTimeDurationWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4MT", "P4MTTimeDuration")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Measurement - Time Duration",
                                   "concept":"P4MT","grade":4,"display_concept":"G4_Measurement_Time_Duration","SubTopics":"P4MTTimeDuration"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4MTPerimeterWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4MT", "P4MTPerimeter")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Measurement - Perimeter",
                                   "concept":"P4MT","grade":4,"display_concept":"G4_Measurement_Perimeter","SubTopics":"P4MTPerimeter"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4MTAreaWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4MT", "P4MTArea")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Measurement - Area",
                                   "concept":"P4MT","grade":4,"display_concept":"G4_Measurement_Area","SubTopics":"P4MTArea"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP4MTCompositeFiguresWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P4MT", "P4MTCompositeFigures")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_4_Mathematics'>Worksheets for Grade 4:</a></font>&nbsp;&nbsp;Measurement - Composite Figures",
                                   "concept":"P4MT","grade":4,"display_concept":"G4_Measurement_Composite_Figures","SubTopics":"P4MTCompositeFigures"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5WNWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5WN","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Whole Numbers - All Topics",
                                   "concept":"P5WN","grade":5,"display_concept":"G5_Whole_Numbers","SubTopics":"P5WN"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5WholeNumbersWriteInWordsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5WN","P5WholeNumbersWriteInWords")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Whole Numbers - Write Words",
                                   "concept":"P5WN","grade":5,"display_concept":"G5_Whole_Numbers_Write_Words","SubTopics":"P5WholeNumbersWriteInWords"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5WholeNumbersWriteInFiguresWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5WN","P5WholeNumbersWriteInFigures")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Whole Numbers - Write Figures",
                                   "concept":"P5WN","grade":5,"display_concept":"G5_Whole_Numbers_Write_Figures","SubTopics":"P5WholeNumbersWriteInFigures"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5WholeNumbersPlaceValueWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5WN","P5WholeNumbersPlaceValue")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Whole Numbers - Place Values",
                                   "concept":"P5WN","grade":5,"display_concept":"G5_Whole_Numbers_Place_Values","SubTopics":"P5WholeNumbersPlaceValue"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5WholeNumbersComparingAndOrderingWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5WN","P5WholeNumbersComparingAndOrdering")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Whole Numbers - Comparing Ordering",
                                   "concept":"P5WN","grade":5,"display_concept":"G5_Whole_Numbers_Comparing_Ordering","SubTopics":"P5WholeNumbersComparingAndOrdering"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5WholeNumbersFindPatternWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5WN","P5WholeNumbersFindPattern")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Whole Numbers - Find Pattern",
                                   "concept":"P5WN","grade":5,"display_concept":"G5_Whole_Numbers_Find_Pattern","SubTopics":"P5WholeNumbersFindPattern"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5WholeNumbersApproximationEstimationWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5WN","P5WholeNumbersApproximationEstimation")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Whole Numbers - Approximation Estimation",
                                   "concept":"P5WN","grade":5,"display_concept":"G5_Whole_Numbers_Approximation_Estimation","SubTopics":"P5WholeNumbersApproximationEstimation"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5WholeNumbersMultiplyDivideWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5WN","P5WholeNumbersMultiplyDivide")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Whole Numbers - Multiplication Division",
                                   "concept":"P5WN","grade":5,"display_concept":"G5_Whole_Numbers_Multiplication_Division","SubTopics":"P5WholeNumbersMultiplyDivide"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5WholeNumbersOrderOfOperationWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5WN","P5WholeNumbersOrderOfOperation")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Whole Numbers - Order of Operations",
                                   "concept":"P5WN","grade":5,"display_concept":"G5_Whole_Numbers_Order_Operations","SubTopics":"P5WholeNumbersOrderOfOperation"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5WholeNumbersWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5WN","P5WholeNumbersWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Whole Numbers - Word Problems",
                                   "concept":"P5WN","grade":5,"display_concept":"G5_Whole_Numbers_Word_Problems","SubTopics":"P5WholeNumbersWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5FRWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5FR","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Fractions - All Topics",
                                   "concept":"P5FR","grade":5,"display_concept":"G5_Fractions","SubTopics":"P5FR"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5FractionsAddSubProperFractionsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5FR","P5FractionsAddSubProperFractions")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Fractions - Add Subtract Proper",
                                   "concept":"P5FR","grade":5,"display_concept":"G5_Fractions_Add_Subtract_Proper","SubTopics":"P5FractionsAddSubProperFractions"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5FractionsAddSubMixedFractionsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5FR","P5FractionsAddSubMixedFractions")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Fractions - Add Subtract Mixed",
                                   "concept":"P5FR","grade":5,"display_concept":"G5_Fractions_Add_Subtract_Mixed","SubTopics":"P5FractionsAddSubMixedFractions"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5FractionsMultProperImproperFractionsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5FR","P5FractionsMultProperImproperFractions")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Fractions - Multiply Proper Improper",
                                   "concept":"P5FR","grade":5,"display_concept":"G5_Fractions_Multiply_Proper_Improper","SubTopics":"P5FractionsMultProperImproperFractions"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5FractionsMultMixedFractionsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5FR","P5FractionsMultMixedFractions")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Fractions - Multiply Mixed",
                                   "concept":"P5FR","grade":5,"display_concept":"G5_Fractions_Multiply_Mixed","SubTopics":"P5FractionsMultMixedFractions"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5FractionsDivideProperFractionsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5FR","P5FractionsDivideProperFractions")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Fractions - Divide",
                                   "concept":"P5FR","grade":5,"display_concept":"G5_Fractions_Divide","SubTopics":"P5FractionsDivideProperFractions"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5FractionsWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5FR","P5FractionsWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Fractions - Word Problems",
                                   "concept":"P5FR","grade":5,"display_concept":"G5_Fractions_Word_Problems","SubTopics":"P5FractionsWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5DCWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5DC","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Decimals - All Topics",
                                   "concept":"P5DC","grade":5,"display_concept":"G5_Decimals","SubTopics":"P5DC"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5DecimalsMultiplyDivideWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5DC","P5DecimalsMultiplyDivide")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Decimals - Multiply Divide",
                                   "concept":"P5DC","grade":5,"display_concept":"G5_Decimals_Multiply_Divide","SubTopics":"P5DecimalsMultiplyDivide"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5DecimalsRoundingWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5DC","P5DecimalsRounding")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Decimals - Rounding Off",
                                   "concept":"P5DC","grade":5,"display_concept":"G5_Decimals_Rounding_Off","SubTopics":"P5DecimalsRounding"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5DecimalsWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5DC","P5DecimalsWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Decimals - Word Problems",
                                   "concept":"P5DC","grade":5,"display_concept":"G5_Decimals_Word_Problems","SubTopics":"P5DecimalsWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5PRWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5PR","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Percentage - All Topics",
                                   "concept":"P5PR","grade":5,"display_concept":"G5_Percentage","SubTopics":"P5PR"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5PercentageExpressAsPercentWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5PR","P5PercentageExpressAsPercent")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Percentage - Express as Percentage",
                                   "concept":"P5PR","grade":5,"display_concept":"G5_Percentage_Express_Percentage","SubTopics":"P5PercentageExpressAsPercent"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5PercentageExpressAsDecimalWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5PR","P5PercentageExpressAsDecimal")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Percentage - Express as Decimal",
                                   "concept":"P5PR","grade":5,"display_concept":"G5_Percentage_Express_Decimal","SubTopics":"P5PercentageExpressAsDecimal"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5PercentageExpressAsFractionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5PR","P5PercentageExpressAsFraction")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Percentage - Express as Fraction",
                                   "concept":"P5PR","grade":5,"display_concept":"G5_Percentage_Express_Fraction","SubTopics":"P5PercentageExpressAsFraction"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5PercentageWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5PR","P5PercentageWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Percentage - Word Problems",
                                   "concept":"P5PR","grade":5,"display_concept":"G5_Percentage_Word_Problems","SubTopics":"P5PercentageWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5RTWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5RT","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Ratio - All Topics",
                                   "concept":"P5RT","grade":5,"display_concept":"G5_Ratio","SubTopics":"P5RT"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5RatioSimplestFormWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5RT","P5RatioSimplestForm")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Ratio - Simplest Form",
                                   "concept":"P5RT","grade":5,"display_concept":"G5_Ratio_Simplest_Form","SubTopics":"P5RatioSimplestForm"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5RatioMissingNumberWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5RT","P5RatioMissingNumber")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Ratio - Missing Number",
                                   "concept":"P5RT","grade":5,"display_concept":"G5_Ratio_Missing_Number","SubTopics":"P5RatioMissingNumber"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5RatioWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5RT","P5RatioWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Ratio - Word Problems",
                                   "concept":"P5RT","grade":5,"display_concept":"G5_Ratio_Word_Problems","SubTopics":"P5RatioWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5MTWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5MT","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Measurement - All Topics",
                                   "concept":"P5MT","grade":5,"display_concept":"G5_Measurement","SubTopics":"P5MT"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5MeasurementUnitConversionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5MT","P5MeasurementUnitConversion")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Measurement - Unit Conversion",
                                   "concept":"P5MT","grade":5,"display_concept":"G5_Measurement_Unit_Conversion","SubTopics":"P5MeasurementUnitConversion"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5MeasurementAreaOfTriangleWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5MT","P5MeasurementAreaOfTriangle")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Measurement - Area of Triangle",
                                   "concept":"P5MT","grade":5,"display_concept":"G5_Measurement_Area_Triangle","SubTopics":"P5MeasurementAreaOfTriangle"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5MeasurementVolumeWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5MT","P5MeasurementVolume")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Measurement - Volume",
                                   "concept":"P5MT","grade":5,"display_concept":"G5_Measurement_Volume","SubTopics":"P5MeasurementVolume"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5MeasurementWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5MT","P5MeasurementWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Measurement - Word Problems",
                                   "concept":"P5MT","grade":5,"display_concept":"G5_Measurement_Word_Problems","SubTopics":"P5MeasurementWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5GTWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5GT", "All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Geometry - All Topics",
                                   "concept":"P5GT","grade":5,"display_concept":"G5_Geometry","SubTopics":"P5GT"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5GeometryAnglesWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5GT", "P5GeometryAngles")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Geometry - Angles",
                                   "concept":"P5GT","grade":5,"display_concept":"G5_Geometry_Angles","SubTopics":"P5GeometryAngles"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5GeometryTrianglesWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5GT", "P5GeometryTriangles")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Geometry - Triangles",
                                   "concept":"P5GT","grade":5,"display_concept":"G5_Geometry_Triangles","SubTopics":"P5GeometryTriangles"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5GeometryFourSidedWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5GT", "P5GeometryFourSided")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Geometry - Four Sided",
                                   "concept":"P5GT","grade":5,"display_concept":"G5_Geometry_Four_Sided","SubTopics":"P5GeometryFourSided"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5DAWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5DA", "All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Data Analysis - All Topics",
                                   "concept":"P5DA","grade":5,"display_concept":"G5_Data_Analysis","SubTopics":"P5DA"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5DataAnalysisAverageWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5DA", "P5DataAnalysisAverage")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Data Analysis - Average",
                                   "concept":"P5DA","grade":5,"display_concept":"G5_Data_Analysis_Average","SubTopics":"P5DataAnalysisAverage"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5DataAnalysisTotalWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5DA", "P5DataAnalysisTotal")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Data Analysis - Total",
                                   "concept":"P5DA","grade":5,"display_concept":"G5_Data_Analysis_Total","SubTopics":"P5DataAnalysisTotal"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP5DataAnalysisWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P5DA", "P5DataAnalysisWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_5_Mathematics'>Worksheets for Grade 5:</a></font>&nbsp;&nbsp;Data Analysis - Word Problems",
                                   "concept":"P5DA","grade":5,"display_concept":"G5_Data_Analysis_Word_Problems","SubTopics":"P5DataAnalysisWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6AGWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6AG","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Algebra - All Topics",
                                   "concept":"P6AG","grade":6,"display_concept":"G6_Algebra","SubTopics":"P6AG"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6AGSimplifyingExpressionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6AG","P6AGSimplifyingExpression")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Algebra - Simplify",
                                   "concept":"P6AG","grade":6,"display_concept":"G6_Algebra_Simplify","SubTopics":"P6AGSimplifyingExpression"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6AGEvaluationExpressionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6AG","P6AGEvaluationExpression")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Algebra - Evaluate",
                                   "concept":"P6AG","grade":6,"display_concept":"G6_Algebra_Evaluate","SubTopics":"P6AGEvaluationExpression"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6AGWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6AG","P6AGWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Algebra - Word Problems",
                                   "concept":"P6AG","grade":6,"display_concept":"G6_Algebra_Word_Problems","SubTopics":"P6AGWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6FRWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6FR","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Fractions - All Topics",
                                   "concept":"P6FR","grade":6,"display_concept":"G6_Fractions","SubTopics":"P6FR"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6FRDivideWholeNumberWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6FR","P6FRDivideWholeNumber")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Fractions - Divide Whole Number",
                                   "concept":"P6FR","grade":6,"display_concept":"G6_Fractions_Divide_Whole","SubTopics":"P6FRDivideWholeNumber"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6FRDivideProperFractionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6FR","P6FRDivideProperFraction")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Fractions - Divide Proper",
                                   "concept":"P6FR","grade":6,"display_concept":"G6_Fractions_Divide_Proper","SubTopics":"P6FRDivideProperFraction"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6FRWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6FR","P6FRWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Fractions - Word Problems",
                                   "concept":"P6FR","grade":6,"display_concept":"G6_Fractions_Word Problems","SubTopics":"P6FRWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6SPWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6SP","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Speed - All Topics",
                                   "concept":"P6SP","grade":6,"display_concept":"G6_Speed","SubTopics":"P6SP"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6SPDTSWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6SP","P6SPDTS")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Speed - Distance Time",
                                   "concept":"P6SP","grade":6,"display_concept":"G6_Speed_Distance_Time","SubTopics":"P6SPDTS"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6SPWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6SP","P6SPWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Speed - Word Problems",
                                   "concept":"P6SP","grade":6,"display_concept":"G6_Speed_Word_Problems","SubTopics":"P6SPWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6RTWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6RT","P6RTWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Ratio - Word Problems",
                                   "concept":"P6RT","grade":6,"display_concept":"G6_Ratio_Word_Problems","SubTopics":"P6RTWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6PRWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6PR","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Percentage - All Topics",
                                   "concept":"P6PR","grade":6,"display_concept":"G6_Percentage","SubTopics":"P6PR"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6PRFindWholeWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6PR","P6PRFindWhole")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Percentage - Find Whole",
                                   "concept":"P6PR","grade":6,"display_concept":"G6_Percentage_Find_Whole","SubTopics":"P6PRFindWhole"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6PRIncDecWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6PR","P6PRIncDec")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Percentage - Change",
                                   "concept":"P6PR","grade":6,"display_concept":"G6_Percentage_Change","SubTopics":"P6PRIncDec"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6PRWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6PR","P6PRWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Percentage - Word Problems",
                                   "concept":"P6PR","grade":6,"display_concept":"G6_Percentage_Word_Problems","SubTopics":"P6PRWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6DAWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6DA","P6DAWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Data Analysis - Word Problems",
                                   "concept":"P6DA","grade":6,"display_concept":"G6_Data_Analysis","SubTopics":"P6DAWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6MTWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6MT","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Measurement - All Topics",
                                   "concept":"P6MT","grade":6,"display_concept":"G6_Measurement","SubTopics":"P6MT"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6MTRadiusWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6MT","P6MTRadius")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Measurement - Radius/Diameter",
                                   "concept":"P6MT","grade":6,"display_concept":"G6_Measurement_Radius_Diameter","SubTopics":"P6MTRadius"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6MTCircumferenceWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6MT","P6MTCircumference")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Measurement - Circumference",
                                   "concept":"P6MT","grade":6,"display_concept":"G6_Measurement_Circumference","SubTopics":"P6MTCircumference"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6MTAreaWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6MT","P6MTArea")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Measurement - Area",
                                   "concept":"P6MT","grade":6,"display_concept":"G6_Measurement_Area","SubTopics":"P6MTArea"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6MTSemiPerimeterWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6MT","P6MTSemiPerimeter")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Measurement - Perimeter",
                                   "concept":"P6MT","grade":6,"display_concept":"G6_Measurement_Perimeter","SubTopics":"P6MTSemiPerimeter"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6MTSemiAreaWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6MT","P6MTSemiArea")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Measurement - Semi-Circle Area",
                                   "concept":"P6MT","grade":6,"display_concept":"G6_Measurement_Semi_Circle_Area","SubTopics":"P6MTSemiArea"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6MTCompositeWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6MT","P6MTComposite")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Measurement - Composite",
                                   "concept":"P6MT","grade":6,"display_concept":"G6_Measurement_Composite","SubTopics":"P6MTComposite"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP6MTVolumeWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P6MT","P6MTVolume")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_6_Mathematics'>Worksheets for Grade 6:</a></font>&nbsp;&nbsp;Measurement - Volume",
                                   "concept":"P6MT","grade":6,"display_concept":"G6_Measurement_Volume","SubTopics":"P6MTVolume"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3WNWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3WN","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Whole Numbers - All Topics",
                                   "concept":"P3WN","grade":3,"display_concept":"G3_Whole_Numbers","SubTopics":"P3WN"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3WNPlaceValuesWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3WN","P3WNPlaceValues")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Whole Numbers - Place Values",
                                   "concept":"P3WN","grade":3,"display_concept":"G3_Whole_Numbers_Place_Values","SubTopics":"P3WNPlaceValues"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3WNFiguresToWordsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3WN","P3WNFiguresToWords")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Whole Numbers - Write Words",
                                   "concept":"P3WN","grade":3,"display_concept":"G3_Whole_Numbers_Write_Words","SubTopics":"P3WNFiguresToWords"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3WNWordsToFiguresWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3WN","P3WNWordsToFigures")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Whole Numbers - Write Figures",
                                   "concept":"P3WN","grade":3,"display_concept":"G3_Whole_Numbers_Write_Words","SubTopics":"P3WNWordsToFigures"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3WNComparingOrderingWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3WN","P3WNComparingOrdering")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Whole Numbers - Comparing Ordering",
                                   "concept":"P3WN","grade":3,"display_concept":"G3_Whole_Numbers_Comparing_Ordering","SubTopics":"P3WNComparingOrdering"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3WNNumberPatternsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3WN","P3WNNumberPatterns")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Whole Numbers - Patterns",
                                   "concept":"P3WN","grade":3,"display_concept":"G3_Whole_Numbers_Patterns","SubTopics":"P3WNNumberPatterns"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3WNAdditionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3WN","P3WNAddition")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Whole Numbers - Addition",
                                   "concept":"P3WN","grade":3,"display_concept":"G3_Whole_Numbers_Addition","SubTopics":"P3WNAddition"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3WNSubtractionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3WN","P3WNSubtraction")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Whole Numbers - Subtraction",
                                   "concept":"P3WN","grade":3,"display_concept":"G3_Whole_Numbers_Subtraction","SubTopics":"P3WNSubtraction"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3WNMultiplicationWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3WN","P3WNMultiplication")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Whole Numbers - Multiplication",
                                   "concept":"P3WN","grade":3,"display_concept":"G3_Whole_Numbers_Multiplication","SubTopics":"P3WNMultiplication"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3WNDivisionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3WN","P3WNDivision")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Whole Numbers - Division",
                                   "concept":"P3WN","grade":3,"display_concept":"G3_Whole_Numbers_Division","SubTopics":"P3WNDivision"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3WNWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3WN","P3WNWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Whole Numbers - Word Problems",
                                   "concept":"P3WN","grade":3,"display_concept":"G3_Whole_Numbers_Word_Problems","SubTopics":"P3WNWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3MOWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3MO","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Money - All Topics",
                                   "concept":"P3MO","grade":3,"display_concept":"G3_Money","SubTopics":"P3MO"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3MOAdditionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3MO","P3MOAddition")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Money - Addition",
                                   "concept":"P3MO","grade":3,"display_concept":"G3_Money_Addition","SubTopics":"P3MOAddition"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3MOSubtractionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3MO","P3MOSubtraction")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Money - Subtraction",
                                   "concept":"P3MO","grade":3,"display_concept":"G3_Money_Subtraction","SubTopics":"P3MOSubtraction"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3MOWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3MO","P3MOWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Money - Word Problems",
                                   "concept":"P3MO","grade":3,"display_concept":"G3_Money_Word_Problems","SubTopics":"P3MOWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3TIWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3TI","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Time - All Topics",
                                   "concept":"P3TI","grade":3,"display_concept":"G3_Time","SubTopics":"P3TI"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3TITellingTimeWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3TI","P3TITellingTime")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Time - Telling",
                                   "concept":"P3TI","grade":3,"display_concept":"G3_Time_Telling","SubTopics":"P3TITellingTime"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3TIConversionTimeWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3TI","P3TIConversionTime")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Time - Conversion",
                                   "concept":"P3TI","grade":3,"display_concept":"G3_Time_Conversion","SubTopics":"P3TIConversionTime"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3TIAdditionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3TI","P3TIAddition")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Time - Addition",
                                   "concept":"P3TI","grade":3,"display_concept":"G3_Time_Addition","SubTopics":"P3TIAddition"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3TISubtractionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3TI","P3TISubtraction")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Time - Subtraction",
                                   "concept":"P3TI","grade":3,"display_concept":"G3_Time_Subtraction","SubTopics":"P3TISubtraction"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3TIDurationWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3TI","P3TIDuration")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Time - Duration",
                                   "concept":"P3TI","grade":3,"display_concept":"G3_Time_Duration","SubTopics":"P3TIDuration"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3TIWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3TI","P3TIWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Time - Word Problems",
                                   "concept":"P3TI","grade":3,"display_concept":"G3_Time_Word_Problems","SubTopics":"P3TIWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3LMWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3LM","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Length Mass Volume",
                                   "concept":"P3LM","grade":3,"display_concept":"G3_Length_Mass_Volume","SubTopics":"P3LM"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3LMMetreCentiMetreWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3LM","P3LMMetreCentiMetre")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Metres and Centimetres",
                                   "concept":"P3LM","grade":3,"display_concept":"G3_Metres_Centimetres","SubTopics":"P3LMMetreCentiMetre"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3LMKiloMetreWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3LM","P3LMKiloMetre")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Kilometres and Metres",
                                   "concept":"P3LM","grade":3,"display_concept":"G3_Kilometres_Metres","SubTopics":"P3LMKiloMetre"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3LMKiloGramWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3LM","P3LMKiloGram")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Kilomgrams and Grams",
                                   "concept":"P3LM","grade":3,"display_concept":"G3_Kilograms_Grams","SubTopics":"P3LMKiloGram"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3LMLitresMilliWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3LM","P3LMLitresMilli")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Litres and Millilitres",
                                   "concept":"P3LM","grade":3,"display_concept":"G3_Litres_Millilitres","SubTopics":"P3LMLitresMilli"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3LMWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3LM","P3LMWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Measurement - Word Problems",
                                   "concept":"P3LM","grade":3,"display_concept":"G3_Measurement_Word_Problems","SubTopics":"P3LMWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3LMWordProblems_2StepsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3LM","P3LMWordProblems_2Steps")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Measurement - 2-Step Problems",
                                   "concept":"P3LM","grade":3,"display_concept":"G3_Measurement_2-Step_Problems","SubTopics":"P3LMWordProblems_2Steps"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3ANWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3AN","All Topics")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Angles - All Topics",
                                   "concept":"P3AN","grade":3,"display_concept":"G3_Angles","SubTopics":"P3AN"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3ANIdentifyingWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3AN","P3ANIdentifying")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Identifying Angles",
                                   "concept":"P3AN","grade":3,"display_concept":"G3_Identifying_Angles","SubTopics":"P3ANIdentifying"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3ANRightAngleWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3AN","P3ANRightAngle")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Right Angles",
                                   "concept":"P3AN","grade":3,"display_concept":"G3_Right_Angles","SubTopics":"P3ANRightAngle"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3BGBarGraphsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3BG","P3BGBarGraphs")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Interpreting Bar Graphs",
                                   "concept":"P3BG","grade":3,"display_concept":"G3_Bar_Graphs","SubTopics":"P3BGBarGraphs"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3APSquareUnitsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3AP","P3APSquareUnits")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Area in Square Units",
                                   "concept":"P3AP","grade":3,"display_concept":"G3_Area_Square_Units","SubTopics":"P3APSquareUnits"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3APSquareCmMWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3AP","P3APSquareCmM")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Area in Square cm / Square m",
                                   "concept":"P3AP","grade":3,"display_concept":"G3_Area_Square_cm_Square_m","SubTopics":"P3APSquareCmM"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3APAreaWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3AP","P3APArea")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Area of Squares / Rectangles",
                                   "concept":"P3AP","grade":3,"display_concept":"G3_Area_Squares_Rectangles","SubTopics":"P3APArea"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3APPerimeterWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3AP","P3APPerimeter")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Perimeter of Squares / Rectangles",
                                   "concept":"P3AP","grade":3,"display_concept":"G3_Perimeter_Squares_Rectangles","SubTopics":"P3APPerimeter"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3APWordProblemsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3AP","P3APWordProblems")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Word Problems",
                                   "concept":"P3AP","grade":3,"display_concept":"G3_Area_Perimeter_Word_Problems","SubTopics":"P3APWordProblems"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3FRWhatIsFractionsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3FR","P3FRWhatIsFractions")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;What is a Fraction?",
                                   "concept":"P3FR","grade":3,"display_concept":"G3_What_is_a_Fraction","SubTopics":"P3FRWhatIsFractions"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3FREquivalentFractionsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3FR","P3FREquivalentFractions")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Equivalent Fractions",
                                   "concept":"P3FR","grade":3,"display_concept":"G3_Equivalent_Fractions","SubTopics":"P3FREquivalentFractions"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3FRSimplifyingFractionsWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3FR","P3FRSimplifyingFractions")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Simplifying Fractions",
                                   "concept":"P3FR","grade":3,"display_concept":"G3_Simplifying_Fractions","SubTopics":"P3FRSimplifyingFractions"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3FRComparingOrderingWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3FR","P3FRComparingOrdering")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Comparing and Ordering",
                                   "concept":"P3FR","grade":3,"display_concept":"G3_Comparing_Ordering_Fractions","SubTopics":"P3FRComparingOrdering"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3FRAdditionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3FR","P3FRAddition")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Adding Fractions",
                                   "concept":"P3FR","grade":3,"display_concept":"G3_Adding_Fractions","SubTopics":"P3FRAddition"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3FRSubtractionWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3FR","P3FRSubtraction")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Subtracting Fractions",
                                   "concept":"P3FR","grade":3,"display_concept":"G3_Subtracting_Fractions","SubTopics":"P3FRSubtraction"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateP3PPPerpendicularParallelWorksheets(BaseHandler):   
    @login_required   
    def get(self, **kwargs):
        Config.test_values = HCWorksheets.GenerateWorksheets().GenerateWorksheetsPage(self.auth.user,"P3PP","P3PPPerpendicularParallel")
        Config.test_values.update({"header":"<font style='text-decoration:underline'><a href='/Primary_Grade_3_Mathematics'>Worksheets for Grade 3:</a></font>&nbsp;&nbsp;Perpendicular and Parallel Lines",
                                   "concept":"P3PP","grade":3,"display_concept":"G3_Perpendicular_Parallel_Lines","SubTopics":"P3PPPerpendicularParallel"})
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)

class GenerateWorksheets(BaseHandlerWorksheets):     
    @login_required 
    def post(self, **kwargs):
        display_concept = self.request.form.get('display_concept')
        create_user = self.auth.user
        username = self.request.form.get('username')
        grade = self.request.form.get('grade')
        concept = self.request.form.get('concept')
        sub_concept = self.request.form.get('sub_concept')
        class_name = self.request.form.get('class_name')
        
        #
        # @riyaz: The cryptic-looking test names come from here ;P
        #
        if self.auth.user.IsTeacher:
            TestInfo = TeacherTestData(concept,class_name,self.auth.user.username,sub_concept)
            test_name = "T_"+str(display_concept)+"_"+str(TestInfo['test_counter']+1)
        else:
            TestInfo = TestData(concept,username,sub_concept)
            test_name = str(display_concept)+"_"+str(TestInfo['test_counter']+1)
        logging.info("test_name = "+test_name)
        
        TestMaster = {"test_name":test_name,"create_user":create_user,"username":username,"grade":grade,"concept":concept,"class_name":class_name,
                      "sub_concept":sub_concept}
        HCTests.GenerateTests().GenerateTest(TestMaster,self.auth.user)
        '''No values are passed as it reload the concept worksheet page and takes all the values from there'''
        Config.test_values = {}
        return self.render_response('Worksheets/GenerateWorksheets.html', **Config.test_values)
    

class GetTest(BaseHandlerWorksheets):     
    @login_required 
    def post(self, **kwargs):
        TestId = unicode(self.request.form.get('TestId'))
        logging.info("test_id = "+TestId)
        '''Getting the first problem with counter = 1'''
        counter = 1
        Config.test_values = HCTests.GenerateTests().GetTestData(TestId,counter)
        template_name = Config.test_values["template"]
        
        '''for some unknown reason template_name comes as none the first time so getting the data again'''
        while template_name is None or template_name == "":
            Config.test_values = HCTests.GenerateTests().GetTestData(TestId,counter,self.auth.user)
            template_name = Config.test_values["template"]
        
        Config.test_values['from_test'] = "Y"
        return self.render_response(template_name, **Config.test_values)
    
class GetTestProblems(BaseHandlerWorksheets):     
    @login_required 
    def post(self, **kwargs):
        TestId = unicode(self.request.form.get('TestId'))
        counter = int(self.request.form.get('counter'))
        answer_submitted = str(self.request.form.get('answer_submitted'))
        next = str(self.request.form.get('next'))
        logging.info("answer = "+answer_submitted)
        '''answer = None is when no answer is selected in multiple choice'''
        if answer_submitted!="None":
            HCTests.SubmitAnswer(TestId, counter, answer_submitted)
        if next=="Y":
            counter = counter + 1
        elif next=="N":
            counter = counter - 1
        Config.test_values = HCTests.GenerateTests().GetTestData(TestId,counter)
        template_name = Config.test_values["template"]        
        
        '''for some unknown reason template_name comes as none the first time so getting the data again'''
        while template_name is None or template_name == "":
            Config.test_values = HCTests.GenerateTests().GetTestData(TestId,counter)
            template_name = Config.test_values["template"]
            
        Config.test_values['from_test'] = "Y"
        return self.render_response(template_name, **Config.test_values)
    
class GetClickedProblem(BaseHandlerWorksheets):     
    @login_required 
    def post(self, **kwargs):
        TestId = unicode(self.request.form.get('TestId'))
        current_counter = int(self.request.form.get('current_counter'))
        clicked_counter = int(self.request.form.get('clicked_counter'))
        answer_submitted = str(self.request.form.get('answer_submitted'))
        '''answer = None is when no answer is selected in multiple choice'''
        if answer_submitted!="None":
            HCTests.SubmitAnswer(TestId, current_counter, answer_submitted)

        Config.test_values = HCTests.GenerateTests().GetTestData(TestId,clicked_counter)
        template_name = Config.test_values["template"]        
        
        '''for some unknown reason template_name comes as none the first time so getting the data again'''
        while template_name is None or template_name == "":
            Config.test_values = HCTests.GenerateTests().GetTestData(TestId,clicked_counter)
            template_name = Config.test_values["template"]
            
        Config.test_values['from_test'] = "Y"
        return self.render_response(template_name, **Config.test_values)
    
class GenerateTestReport(BaseHandlerWorksheets):
    @login_required 
    def post(self,**kwargs):
        TestId = unicode(self.request.form.get('TestId'))
        if TestId == "None":
            logging.info("trying to get TestId from memcache")
            TestId = memcache.Client().get(unicode(self.auth.user.username)+'_test_values')['test_id']
        try:
            counter = int(self.request.form.get('counter'))
        except:
            counter =  -1
        answer_submitted = str(self.request.form.get('answer_submitted'))
        logging.info(TestId)
        if counter != -1 and answer_submitted!="None":
            '''This is to check the last question submitted.'''
            HCTests.SubmitAnswer(TestId, counter, answer_submitted)
        Config.test_values = Reports.GenerateReports().GenerateTestReport(self.auth.user,TestId)
        return self.render_response('Reports/Test_Report.html', **Config.test_values)    

def TestData(concept,username,sub_concept):
    '''checking if user has complete one test'''
    TestQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+unicode(username)+"' and concept='"+concept+"'" )
    TestData = TestQuery.fetch(10000)
    TestGenerated = 0
    TestCompleted = 0
    for t in TestData:
        TestGenerated = TestGenerated + 1
        if t.status == 'Completed':
            TestCompleted = TestCompleted + 1

    SubConceptTestData = TestsMaster.TestsMasterTable.gql("where student_id = '"+unicode(username)+"' and sub_concept='"+sub_concept+"'" ).fetch(10000)
    test_counter = 0
    for t in SubConceptTestData:
        test_counter = test_counter + 1
            
    TestData = {'TestCompleted':TestCompleted,'TestGenerated':TestGenerated,'test_counter':test_counter}
    return TestData

def TeacherTestData(concept,username,create_user,sub_concept):
    '''checking if user has complete one test'''
    TestQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+unicode(username)+"' and concept='"+concept+"' and created_by = '"+create_user+"'" )
    TestData = TestQuery.fetch(10000)
    TestGenerated = 0
    TestCompleted = 0
    for t in TestData:
        TestGenerated = TestGenerated + 1
        if t.status == 'Completed':
            TestCompleted = TestCompleted + 1

    SubConceptTestData = TestsMaster.TestsMasterTable.gql("where student_id = '"+unicode(username)+"' and sub_concept='"+sub_concept+"' and created_by = '"+create_user+"'" ).fetch(10000)
    test_counter = 0
    for t in SubConceptTestData:
        test_counter = test_counter + 1
            
    TestData = {'TestCompleted':TestCompleted,'TestGenerated':TestGenerated,'test_counter':test_counter}
    return TestData


def GenerateSubtopicsDict(topic):
    '''Generating subtopic id/name dict'''
    SubTopics = []
    SubTopicsId = CodeTranslation.SubTopics[topic]
    for i in range(len(SubTopicsId)):
        SubTopics.append({"id":SubTopicsId[i],"name":CodeTranslation.Concept_List[SubTopicsId[i]]})
    
    return SubTopics

app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()

        