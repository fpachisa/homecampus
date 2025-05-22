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
import Problems.Primary6.Algebra.SimplifyingAlgebra
import Problems.Primary6.Algebra.EvaluationAlgebra
import Problems.Primary6.Fractions.DivideWholeNumber
import Problems.Primary6.Fractions.DivideProperFraction
import Problems.Primary6.Percentage.WholePart
import Problems.Primary6.Percentage.PercentIncDec
import Problems.Primary6.Speed.DistanceTimeSpeed
import Problems.Primary6.Measurement.CircleCircumference
import Problems.Primary6.Measurement.CircleArea
import Problems.Primary6.Measurement.CircleRadiusDiameter
import Problems.Primary6.Measurement.SemiCircleArea
import Problems.Primary6.Measurement.SemiCirclePerimeter
import Problems.Primary6.Measurement.CompositeFigures
import Problems.Primary6.Measurement.VolumeOfCubeCuboid
import Problems.Primary4.WholeNumbers.WriteInWords
import Problems.Primary4.WholeNumbers.WriteInFigures
import Problems.Primary4.WholeNumbers.RoundingOff
import Problems.Primary4.WholeNumbers.PlaceValue
import Problems.Primary4.WholeNumbers.FactorMultiple
import Problems.Primary4.WholeNumbers.ComparingAndOrdering
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
import Problems.Primary6.Ratio.P6RTWordProblems
import Problems.Primary6.DataAnalysis.P6DAWordProblems
import Problems.Primary6.Algebra.P6AGWordProblems
import Problems.Primary6.Fractions.P6FRWordProblems
import Problems.Primary6.Speed.P6SPWordProblems
import Problems.Primary6.Percentage.P6PRWordProblems
import Problems.Primary4.DataAnalysis.P4DATablesBarGraphs
import Problems.Primary4.DataAnalysis.P4DALineGraphs
import Problems.Primary4.WholeNumbers.P4WNWordProblems
import Problems.Primary4.Decimals.P4DCWordProblems
import Problems.Primary4.Fractions.P4FRWordProblems

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

import Problems.Primary1.WholeNumbers.P1WNAddition

import SubmitProblem
import Config
from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from google.appengine.api import memcache
from Database import SubmitProblemsTable

import logging

import HCRank

rules = [Rule('/submit', endpoint='/submit', handler='Submit.Submit')]

class Submit(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware()]
    def post(self):
        '''22-Aug-2011: if there is user inactivity of 10 minutes after loading the problem..the Config.template_values loses all data
        so storing in the session as well'''
        '''try:
            concept = Config.template_values["concept"]
        except KeyError:
            Config.template_values = self.session.get('template_values')
            concept = str(Config.template_values["concept"])'''
        '''05-Nov-2011 getting the template_values from memcache based on userid'''
        student_id = str(self.request.form.get('student_id'))
        template_values = memcache.Client().get(student_id+'_template_values')
        logging.info(student_id+": In submit")
        logging.info(template_values)
        '''deleting the template_values from memcache as its not required now here and will help to detect if two people using same id'''
        memcache.Client().delete(student_id+"_template_values")
        if not template_values:
            self.ErrorMessage = {'explain_text':"Show error message"}
            return self.render_response("Explanation.html", **self.ErrorMessage)
        '''adding the problem_type to memcache to make use of it in Primary6Problems.py to get the previous problem type'''
        '''12-Jun-2012 not required here as its been added to memcache in Primary4/5/6Problems.py while generating the problem'''
        #memcache.Client().delete(student_id+"_problem_type")
        #memcache.Client().add(student_id+"_problem_type",template_values["problem_type"])
        concept = str(template_values["concept"])
        #Creating the SubmitObject to store in the google datastore
        answer = template_values["answer"]
        submitted = self.request.form.get('answer')

        SubmitObject={
                      "student_id":self.request.form.get('student_id'),
                      "grade":int(self.request.form.get('grade')),
                      "concept":concept,
                      "problem_type":template_values["problem_type"],
                      "problem":template_values["problem"],
                      "answer":answer,
                      "answer_submitted":submitted,
                      "time_taken":int(self.request.form.get('time_taken')),
                      "complexity_level":self.request.form.get('complexity_level'),
                      }

        self.explain_dict = template_values["explain"]        
        template_name = str(self.explain_dict["explain_template"])  
        session_problems_attempted = self.session.get('problems_attempted')        
        if not session_problems_attempted:
            self.session['problems_attempted'] = 1
            session_problems_attempted = 1
        else:
            session_problems_attempted = int(session_problems_attempted) + 1
        concept_rank = memcache.Client().get(student_id+'_concept_rank')
        if not concept_rank:
            concept_rank = self.GetConceptRank()
            memcache.Client().add(student_id+'_concept_rank',concept_rank,3600)
        try:
            problems_attempted = concept_rank[concept][0]
            correct_problems = concept_rank[concept][1]
            Concept_HCScore = concept_rank[concept][2]
        except KeyError:
            problems_attempted = 0
            correct_problems = 0
            Concept_HCScore = 0
        problems_attempted = problems_attempted + 1
        SessionHCScore = self.session.get('SessionHCScore')
        if not SessionHCScore:
            self.session['SessionHCScore'] = 0
            SessionHCScore = 0
        self.session['problems_attempted'] = session_problems_attempted
        #checking the answer
        if(CheckAnswer(concept,template_values,submitted)):
            session_correct_problems = self.session.get('correct_problems')
            if not session_correct_problems:
                self.session['correct_problems'] = 1
                session_correct_problems = 1
            else:
                session_correct_problems = int(session_correct_problems) + 1
            self.session['correct_problems'] = session_correct_problems
            correct_problems = correct_problems + 1
            SubmitObject["correct"]=True
            SubmitObject["HCScore"]=int(self.request.form.get('HCScore'))
            SessionHCScore = SessionHCScore + int(self.request.form.get('HCScore'))
            Concept_HCScore = Concept_HCScore + int(self.request.form.get('HCScore'))
            self.session['SessionHCScore'] = SessionHCScore
            # when getting data from session (after inactivity of 10 minutes) the data is in unicode..so converting to str
            explain_text = str(self.explain_dict["explain_text"])
            explain_text = "CorrectANSWERSEPARATOR#"+concept+"ANSWERSEPARATOR"+explain_text
        else:
            SubmitObject["correct"]=False
            SubmitObject["HCScore"]=0
            explain_text = str(self.explain_dict["explain_text"])
            explain_text = "InCorrectANSWERSEPARATOR#"+concept+"ANSWERSEPARATOR"+explain_text
        
        try:
            Concept_HCRank = HCRank.HCRank[Concept_HCScore]
        #8-Mar-2012: Catching the KeyError for more than 1000 points
        except KeyError:
            Concept_HCRank = "Sage"
        concept_rank[concept] = [problems_attempted,correct_problems,Concept_HCScore,Concept_HCRank]
        memcache.Client().set(student_id+'_concept_rank',concept_rank,3600)
        self.explain = {"explain_text":explain_text}
        #Entering the data  in the Google data store

        try:
            SubmitObject["dollar_unit"]=template_values['dollar_unit']
        except KeyError:
            pass
        try:
            SubmitObject["unit"]=template_values['unit']
        except KeyError:
            pass                  
        try:
            SubmitObject["template"]=template_values['template']
        except KeyError:
            pass
        try:
            SubmitObject["answer1"]=str(template_values['answer1'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answer2"]=str(template_values['answer2'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answer3"]=str(template_values['answer3'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answer4"]=str(template_values['answer4'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answerM1"]=str(template_values['answerM1'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answerM2"]=str(template_values['answerM2'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answerM3"]=str(template_values['answerM3'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answerM4"]=str(template_values['answerM4'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answerN1"]=str(template_values['answerN1'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answerN2"]=str(template_values['answerN2'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answerN3"]=str(template_values['answerN3'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answerN4"]=str(template_values['answerN4'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answerD1"]=str(template_values['answerD1'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answerD2"]=str(template_values['answerD2'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answerD3"]=str(template_values['answerD3'])
        except KeyError:
            pass                    
        try:
            SubmitObject["answerD4"]=str(template_values['answerD4'])
        except KeyError:
            pass 
        try:
            SubmitObject["value1"]=str(template_values['value1'])
        except KeyError:
            pass                    
        try:
            SubmitObject["value2"]=str(template_values['value2'])
        except KeyError:
            pass                    
        try:
            SubmitObject["value3"]=str(template_values['value3'])
        except KeyError:
            pass                    
        try:
            SubmitObject["value4"]=str(template_values['value4'])
        except KeyError:
            pass                    
        try:
            SubmitObject["explain"]=str(template_values['explain']['explain_text'])
        except KeyError:
            pass                    
        try:
            SubmitObject["FunctionCall"]=template_values['FunctionCall']
        except KeyError:
            pass 
        try:
            SubmitObject["FractionAnswer"]=template_values['FractionAnswer']
        except KeyError:
            pass 
        
        SubmitProblem.SubmitProblem(SubmitObject)
        return self.render_response(template_name, **self.explain)
    
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

        
def CheckAnswer(concept,template_values,submitted):
    
    # in some concepts word problems can have different answers. To check them we need different versions of CheckAnswer function
    try:
        CheckAnswerType = template_values["CheckAnswerType"]
    except KeyError:
        CheckAnswerType = 1
    
    if CheckAnswerType =="None" or CheckAnswerType is None or CheckAnswerType == "":
        CheckAnswerType = 1
        
    #submitted = self.request.form.get('answer')
    if not submitted:
        submitted = ""
    if (concept=="P5WholeNumbersWriteInFigures"):
        return Problems.Primary5.WholeNumbers.WriteInFigures.WriteInFigures().checkAnswer(template_values["template"],template_values["answer"], submitted)
    elif (concept=="P5WholeNumbersWriteInWords"):
        return Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().checkAnswer(template_values["template"],template_values["answer"], submitted)
    elif (concept=="P5WholeNumbersPlaceValue"):
        return Problems.Primary5.WholeNumbers.PlaceValue.PlaceValue().checkAnswer(template_values["template"],template_values["answer"], submitted)
    elif (concept=="P5WholeNumbersComparingAndOrdering"):
        return Problems.Primary5.WholeNumbers.ComparingAndOrdering.ComparingAndOrdering().checkAnswer(template_values["template"],template_values["answer"], submitted)
    elif (concept=="P5WholeNumbersFindPattern"):
        return Problems.Primary5.WholeNumbers.FindPattern.FindPattern().checkAnswer(template_values["template"],template_values["answer"], submitted)
    elif (concept=="P5WholeNumbersApproximationEstimation"):
        return Problems.Primary5.WholeNumbers.ApproximationEstimation.ApproximationEstimation().checkAnswer(template_values["template"],template_values["answer"], submitted)
    elif (concept=="P5WholeNumbersMultiplyDivide"):
        return Problems.Primary5.WholeNumbers.MultiplyDivide.MultiplyDivide().checkAnswer(template_values["template"],template_values["answer"], submitted)
    elif (concept=="P5WholeNumbersOrderOfOperation"):
        return Problems.Primary5.WholeNumbers.OrderOfOperation.OrderOfOperation().checkAnswer(template_values["template"],template_values["answer"], submitted)        
    elif (concept=="P5WholeNumbersWordProblems"):
        return Problems.Primary5.WholeNumbers.WordProblems.WordProblems().checkAnswer(template_values["template"],template_values["answer"], submitted, CheckAnswerType)        
    elif (concept=="P5FractionsAddSubProperFractions"):
        return Problems.Primary5.Fractions.AddSubProperFractions.AddSubProperFractions().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5FractionsAddSubMixedFractions"):
        return Problems.Primary5.Fractions.AddSubMixedFractions.AddSubMixedFractions().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5FractionsMultProperImproperFractions"):
        return Problems.Primary5.Fractions.MultProperImproperFractions.MultProperImproperFractions().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5FractionsMultMixedFractions"):
        return Problems.Primary5.Fractions.MultMixedFractions.MultMixedFractions().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5FractionsDivideProperFractions"):
        return Problems.Primary5.Fractions.DivideProperFractions.DivideProperFractions().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5FractionsWordProblems"):
        return Problems.Primary5.Fractions.WordProblems.WordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5DecimalsMultiplyDivide"):
        return Problems.Primary5.Decimals.MultiplyDivide.MultiplyDivide().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5DecimalsRounding"):
        return Problems.Primary5.Decimals.Rounding.Rounding().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5DecimalsWordProblems"):
        return Problems.Primary5.Decimals.WordProblems.WordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P5PercentageExpressAsPercent"):
        return Problems.Primary5.Percentage.ExpressAsPercent.ExpressAsPercent().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5PercentageExpressAsDecimal"):
        return Problems.Primary5.Percentage.ExpressAsDecimal.ExpressAsDecimal().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5PercentageExpressAsFraction"):
        return Problems.Primary5.Percentage.ExpressAsFraction.ExpressAsFraction().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5PercentageWordProblems"):
        return Problems.Primary5.Percentage.WordProblems.WordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P5RatioSimplestForm"):
        return Problems.Primary5.Ratio.SimplestForm.SimplestForm().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5RatioMissingNumber"):
        return Problems.Primary5.Ratio.MissingNumber.MissingNumber().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5RatioWordProblems"):
        return Problems.Primary5.Ratio.WordProblems.WordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P5MeasurementUnitConversion"):
        return Problems.Primary5.Measurement.UnitConversion.UnitConversion().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5MeasurementAreaOfTriangle"):
        return Problems.Primary5.Measurement.AreaOfTriangle.AreaOfTriangle().checkAnswer(template_values["template"],template_values["answer"],submitted)                
    elif (concept=="P5MeasurementVolume"):
        return Problems.Primary5.Measurement.Volume.Volume().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)                
    elif (concept=="P5MeasurementWordProblems"):
        return Problems.Primary5.Measurement.WordProblems.WordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)                
    elif (concept=="P5GeometryAngles"):
        return Problems.Primary5.Geometry.Angles.Angles().checkAnswer(template_values["template"],template_values["answer"],submitted)
    elif (concept=="P5GeometryTriangles"):
        return Problems.Primary5.Geometry.Triangles.Triangles().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P5GeometryFourSided"):
        return Problems.Primary5.Geometry.FourSidedFigures.FourSidedFigures().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P5DataAnalysisAverage"):
        return Problems.Primary5.DataAnalysis.FindAverage.FindAverage().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P5DataAnalysisTotal"):
        return Problems.Primary5.DataAnalysis.FindTotal.FindTotal().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P5DataAnalysisWordProblems"):
        return Problems.Primary5.DataAnalysis.WordProblems.WordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6AGSimplifyingExpression"):
        return Problems.Primary6.Algebra.SimplifyingAlgebra.SimplifyingAlgebra().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6AGEvaluationExpression"):
        return Problems.Primary6.Algebra.EvaluationAlgebra.EvaluationAlgebra().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6FRDivideWholeNumber"):
        return Problems.Primary6.Fractions.DivideWholeNumber.DivideWholeNumber().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6FRDivideProperFraction"):
        return Problems.Primary6.Fractions.DivideProperFraction.DivideProperFraction().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6PRFindWhole"):
        return Problems.Primary6.Percentage.WholePart.WholePart().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6PRIncDec"):
        return Problems.Primary6.Percentage.PercentIncDec.PercentIncDec().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6SPDTS"):
        return Problems.Primary6.Speed.DistanceTimeSpeed.DistanceTimeSpeed().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6MTRadius"):
        return Problems.Primary6.Measurement.CircleRadiusDiameter.CircleRadiusDiameter().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6MTCircumference"):
        return Problems.Primary6.Measurement.CircleCircumference.CircleCircumference().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6MTArea"):
        return Problems.Primary6.Measurement.CircleArea.CircleArea().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6MTSemiPerimeter"):
        return Problems.Primary6.Measurement.SemiCirclePerimeter.SemiCirclePerimeter().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6MTSemiArea"):
        return Problems.Primary6.Measurement.SemiCircleArea.SemiCircleArea().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6MTComposite"):
        return Problems.Primary6.Measurement.CompositeFigures.CompositeFigures().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6MTVolume"):
        return Problems.Primary6.Measurement.VolumeOfCubeCuboid.VolumeOfCubeCuboid().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6RTWordProblems"):
        return Problems.Primary6.Ratio.P6RTWordProblems.P6RTWordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6DAWordProblems"):
        return Problems.Primary6.DataAnalysis.P6DAWordProblems.P6DAWordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6AGWordProblems"):
        return Problems.Primary6.Algebra.P6AGWordProblems.P6AGWordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6FRWordProblems"):
        return Problems.Primary6.Fractions.P6FRWordProblems.P6FRWordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6SPWordProblems"):
        return Problems.Primary6.Speed.P6SPWordProblems.P6SPWordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P6PRWordProblems"):
        return Problems.Primary6.Percentage.P6PRWordProblems.P6PRWordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4WholeNumbersWriteInFigures"):
        return Problems.Primary4.WholeNumbers.WriteInFigures.WriteInFigures().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4WholeNumbersWriteInWords"):
        return Problems.Primary4.WholeNumbers.WriteInWords.WriteInWords().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4WholeNumbersPlaceValues"):
        return Problems.Primary4.WholeNumbers.PlaceValue.PlaceValue().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4WholeNumbersComparingOrdering"):
        return Problems.Primary4.WholeNumbers.ComparingAndOrdering.ComparingAndOrdering().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4WholeNumbersRoundingOff"):
        return Problems.Primary4.WholeNumbers.RoundingOff.RoundingOff().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4WholeNumbersFactorMultiple"):
        return Problems.Primary4.WholeNumbers.FactorMultiple.FactorMultiple().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4WholeNumbersMutliplyDivide"):
        return Problems.Primary4.WholeNumbers.MultiplicationDivision.MultiplicationDivision().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4FractionsMixedImproper"):
        return Problems.Primary4.Fractions.MixedNumbersImproperFractions.MixedNumbersImproperFractions().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4FractionsSimplifying"):
        return Problems.Primary4.Fractions.SimplifyingFractions.SimplifyingFractions().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4FractionsAdd"):
        return Problems.Primary4.Fractions.AddLikeRelatedFractions.AddLikeRelatedFractions().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4FractionsSubtract"):
        return Problems.Primary4.Fractions.SubtractLikeRelatedFractions.SubtractLikeRelatedFractions().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4FractionsMultiplication"):
        return Problems.Primary4.Fractions.MultiplyProperImproperFractions.MultiplyProperImproperFractions().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4DecimalsTenths"):
        return Problems.Primary4.Decimals.DecimalsTenths.DecimalsTenths().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4DecimalsHundredths"):
        return Problems.Primary4.Decimals.DecimalsHundredths.DecimalsHundredths().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4DecimalsThousandths"):
        return Problems.Primary4.Decimals.DecimalsThousandths.DecimalsThousandths().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4DecimalsComparingOrdering"):
        return Problems.Primary4.Decimals.DecimalsComparingOrdering.DecimalsComparingOrdering().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4DecimalsRoundingOff"):
        return Problems.Primary4.Decimals.DecimalsRoundingOff.DecimalsRoundingOff().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4DecimalsFractions"):
        return Problems.Primary4.Decimals.DecimalsFractions.DecimalsFractions().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4DecimalsAddSub"):
        return Problems.Primary4.Decimals.DecimalsAddSub.DecimalsAddSub().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4DecimalsMultiplyDivide"):
        return Problems.Primary4.Decimals.DecimalsMultiplyDivide.DecimalsMultiplyDivide().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4MTTime24Hrs"):
        return Problems.Primary4.Measurement.MTTime24Hrs.MTTime24Hrs().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4MTTimeDuration"):
        return Problems.Primary4.Measurement.MTTimeDuration.MTTimeDuration().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4MTPerimeter"):
        return Problems.Primary4.Measurement.MTPerimeter.MTPerimeter().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4MTArea"):
        return Problems.Primary4.Measurement.MTArea.MTArea().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4MTCompositeFigures"):
        return Problems.Primary4.Measurement.MTCompositeFigures.MTCompositeFigures().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4DATablesBarGraphs"):
        return Problems.Primary4.DataAnalysis.P4DATablesBarGraphs.P4DATablesBarGraphs().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4DALineGraphs"):
        return Problems.Primary4.DataAnalysis.P4DALineGraphs.P4DALineGraphs().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4WNWordProblems"):
        return Problems.Primary4.WholeNumbers.P4WNWordProblems.P4WNWordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4DCWordProblems"):
        return Problems.Primary4.Decimals.P4DCWordProblems.P4DCWordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P4FRWordProblems"):
        return Problems.Primary4.Fractions.P4FRWordProblems.P4FRWordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)

    elif (concept=="P3WNPlaceValues"):
        return Problems.Primary3.WholeNumbers.P3WNPlaceValue.P3WNPlaceValue().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3WNFiguresToWords"):
        return Problems.Primary3.WholeNumbers.P3WNFiguresToWords.P3WNFiguresToWords().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3WNWordsToFigures"):
        return Problems.Primary3.WholeNumbers.P3WNWordsToFigures.P3WNWordsToFigures().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3WNComparingOrdering"):
        return Problems.Primary3.WholeNumbers.P3WNComparingOrdering.P3WNComparingOrdering().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3WNNumberPatterns"):
        return Problems.Primary3.WholeNumbers.P3WNNumberPatterns.P3WNNumberPatterns().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3WNAddition"):
        return Problems.Primary3.WholeNumbers.P3WNAddition.P3WNAddition().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3WNSubtraction"):
        return Problems.Primary3.WholeNumbers.P3WNSubtraction.P3WNSubtraction().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3WNMultiplication"):
        return Problems.Primary3.WholeNumbers.P3WNMultiplication.P3WNMultiplication().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3WNDivision"):
        return Problems.Primary3.WholeNumbers.P3WNDivision.P3WNDivision().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3WNWordProblems"):
        return Problems.Primary3.WholeNumbers.P3WNWordProblems.P3WNWordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3MOAddition"):
        return Problems.Primary3.Money.P3MOAddition.P3MOAddition().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3MOSubtraction"):
        return Problems.Primary3.Money.P3MOSubtraction.P3MOSubtraction().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3MOWordProblems"):
        return Problems.Primary3.Money.P3MOWordProblems.P3MOWordProblems().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3LMMetreCentiMetre"):
        return Problems.Primary3.LengthMassVolume.P3LMMetreCentiMetre.P3LMMetreCentiMetre().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3LMKiloMetre"):
        return Problems.Primary3.LengthMassVolume.P3LMKiloMetre.P3LMKiloMetre().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)
    elif (concept=="P3LMKiloGram"):
        return Problems.Primary3.LengthMassVolume.P3LMKiloGram.P3LMKiloGram().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)

    elif (concept=="P1WNAddition"):
        return Problems.Primary1.WholeNumbers.P1WNAddition.P1WNAddition().checkAnswer(template_values["template"],template_values["answer"],submitted,CheckAnswerType)

    return False              

app = Tipfy(rules=rules, config=config)    

def main():
    app.run()

if __name__ == "__main__":
    main()