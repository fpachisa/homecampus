'''
Created on May 20, 2012

@author: Farhat Pachisa
'''

from Models import HomeCampusUser
from Database import TestsMaster
from Database import TestProblems
from datetime import datetime
from google.appengine.api import memcache
import random
import GenerateP4TestProblems
import GenerateP5TestProblems
import GenerateP6TestProblems
import GenerateP3TestProblems
import Primary4ProblemTypes
import Primary5ProblemTypes
import Primary6ProblemTypes
import Primary3ProblemTypes
import Config
import string
import Submit
from CodeTranslation import TestConceptList 
import logging

class GenerateTests():
    
    def __init__(self):
        pass

    def GenerateTest(self, TestMaster,user):
        self.test_name = TestMaster["test_name"]
        self.create_user = TestMaster["create_user"]
        if user.IsTeacher:
            self.username = TestMaster["class_name"]
        else:
            self.username = TestMaster["username"]
        logging.info("username = "+self.username)
        self.grade = TestMaster["grade"]
        self.concept = TestMaster["concept"]
        self.sub_concept = TestMaster["sub_concept"]
        self.create_date = datetime.now()
        self.test_id = unicode(self.create_user)+str(self.create_date)
        self.test_id = string.join(self.test_id.split(),"")
        try:
            self.questions = MaxQuestions[self.sub_concept]  # see line 514
        except KeyError: 
            self.questions = 12 #default

        TestIndicator = ['0'] * self.questions
        
        #for _i in range(self.questions):
            #TestIndicator.append("0")
            
        TestMaster = TestsMaster.TestsMasterTable(test_id = self.test_id,
                                                  test_name = self.test_name,
                                                  student_id = self.username,
                                                  grade = int(self.grade),
                                                  concept = self.concept,
                                                  sub_concept = self.sub_concept,
                                                  created_by = unicode(self.create_user),
                                                  create_date = self.create_date,
                                                  status='New',
                                                  update_date = datetime.now(),
                                                  questions = self.questions,
                                                  TestIndicator = TestIndicator)
        TestMaster.put()
        
        '''Generating the concept list and storing it in TestProblems table'''
        if int(self.grade) == 4:
            ConceptList = Primary4ProblemTypes.P4ConceptList(self.questions, self.sub_concept)
        elif int(self.grade) == 5:
            ConceptList = Primary5ProblemTypes.P5ConceptList(self.questions, self.sub_concept)
        elif int(self.grade) == 6:
            ConceptList = Primary6ProblemTypes.P6ConceptList(self.questions, self.sub_concept)
        elif int(self.grade) == 3:
            ConceptList = Primary3ProblemTypes.P3ConceptList(self.questions, self.sub_concept)
                                    
        random.shuffle(ConceptList)

        for i in range(self.questions):
            test_id = self.test_id
            concept = ConceptList[i][0]
            counter = i+1
            problem_type = ConceptList[i][1]
            self.GenerateHCNewTestData(test_id, int(self.grade),user,concept,counter,problem_type)

    def GenerateHCNewTestData(self, TestId, grade,user,concept,counter,problem_type):
        if grade==4:
            ProblemDetails = GenerateP4TestProblems.GenerateP4TestProblems(concept,problem_type)
        elif grade==5:
            ProblemDetails = GenerateP5TestProblems.GenerateP5TestProblems(concept,problem_type)
        elif grade==6:
            ProblemDetails = GenerateP6TestProblems.GenerateP6TestProblems(concept,problem_type)
        elif grade==3:
            ProblemDetails = GenerateP3TestProblems.GenerateP3TestProblems(concept, problem_type)

        try:
            problem=ProblemDetails['problem']
        except KeyError:
            pass
        try:
            dollar_unit=ProblemDetails['dollar_unit']
        except KeyError:
            dollar_unit = ""
        try:
            unit=ProblemDetails['unit']
        except KeyError:
            unit = ""
        try:
            answer=str(ProblemDetails['answer'])
        except KeyError:
            answer = ""
        try:
            complexity_level=ProblemDetails['complexity_level']
        except KeyError:
            complexity_level = ""                    
        try:
            template=ProblemDetails['template']
        except KeyError:
            pass
        try:
            answer1=str(ProblemDetails['answer1'])
        except KeyError:
            answer1 = ""                    
        try:
            answer2=str(ProblemDetails['answer2'])
        except KeyError:
            answer2 = ""                    
        try:
            answer3=str(ProblemDetails['answer3'])
        except KeyError:
            answer3 = ""                    
        try:
            answer4=str(ProblemDetails['answer4'])
        except KeyError:
            answer4 = ""                    
        try:
            answerM1=str(ProblemDetails['answerM1'])
        except KeyError:
            answerM1 = ""                    
        try:
            answerM2=str(ProblemDetails['answerM2'])
        except KeyError:
            answerM2 = ""                    
        try:
            answerM3=str(ProblemDetails['answerM3'])
        except KeyError:
            answerM3 = ""                    
        try:
            answerM4=str(ProblemDetails['answerM4'])
        except KeyError:
            answerM4 = ""                    
        try:
            answerN1=str(ProblemDetails['answerN1'])
        except KeyError:
            answerN1 = ""                    
        try:
            answerN2=str(ProblemDetails['answerN2'])
        except KeyError:
            answerN2 = ""                    
        try:
            answerN3=str(ProblemDetails['answerN3'])
        except KeyError:
            answerN3 = ""                    
        try:
            answerN4=str(ProblemDetails['answerN4'])
        except KeyError:
            answerN4 = ""                    
        try:
            answerD1=str(ProblemDetails['answerD1'])
        except KeyError:
            answerD1 = ""                    
        try:
            answerD2=str(ProblemDetails['answerD2'])
        except KeyError:
            answerD2 = ""                    
        try:
            answerD3=str(ProblemDetails['answerD3'])
        except KeyError:
            answerD3 = ""                    
        try:
            answerD4=str(ProblemDetails['answerD4'])
        except KeyError:
            answerD4 = "" 
        try:
            value1=str(ProblemDetails['value1'])
        except KeyError:
            value1 = ""                    
        try:
            value2=str(ProblemDetails['value2'])
        except KeyError:
            value2 = ""                    
        try:
            value3=str(ProblemDetails['value3'])
        except KeyError:
            value3 = ""                    
        try:
            value4=str(ProblemDetails['value4'])
        except KeyError:
            value4 = ""                    
        try:
            explain=str(ProblemDetails['explain']['explain_text'])
        except KeyError:
            explain = ""                    
        try:
            CheckAnswerType=ProblemDetails['CheckAnswerType']
        except KeyError:
            CheckAnswerType = None                                                                                
        try:
            FunctionCall=ProblemDetails['FunctionCall']
        except KeyError:
            FunctionCall = "" 
        try:
            FractionAnswer=ProblemDetails['FractionAnswer']
        except KeyError:
            FractionAnswer = None 

        TestProblems.TestProblems(test_id = TestId,
                                  concept = concept,
                                  counter = counter,
                                  problem_type = problem_type,
                                  problem = problem,
                                  dollar_unit = dollar_unit,
                                  unit = unit,
                                  answer = answer,
                                  complexity_level = complexity_level,
                                  template = template,
                                  answer1 = answer1,
                                  answer2 = answer2,
                                  answer3 = answer3,
                                  answer4 = answer4,
                                  answerM1 = answerM1,
                                  answerM2 = answerM2,
                                  answerM3 = answerM3,
                                  answerM4 = answerM4,
                                  answerN1 = answerN1,
                                  answerN2 = answerN2,
                                  answerN3 = answerN3,
                                  answerN4 = answerN4,
                                  answerD1 = answerD1,
                                  answerD2 = answerD2,
                                  answerD3 = answerD3,
                                  answerD4 = answerD4,
                                  value1 = value1,
                                  value2 = value2,
                                  value3 = value3,
                                  value4 = value4,
                                  explain = explain,
                                  CheckAnswerType = CheckAnswerType,
                                  FunctionCall = FunctionCall,
                                  FractionAnswer = FractionAnswer).put()
                                  
    '''07-OCT-2013:This is required for old tests where all problems were not generated at one go. Can delete this after few months.'''
    def GenerateHCNewTestDataOLD(self, TestId, grade,user):
        logging.info("Test Id = "+TestId)
        logging.info("Grade = "+str(grade))
        grade = grade
        TestMasterQuery = TestsMaster.TestsMasterTable.gql("where test_id = '"+TestId+"'")
        TestMasterData = TestMasterQuery.fetch(1)
        for t in TestMasterData:
            grade = t.grade
        
        #just making sure that grade doesn't remain 0 or else no data will be fetched.
        if grade==0:
            TestMasterData = TestMasterQuery.fetch(1)
            for t in TestMasterData:
                grade = t.grade            
        
        #NewTestDataQuery = TestProblems.TestProblems.gql("where test_id = '"+TestId+"' and problem = null")
        NewTestDataQuery = TestProblems.TestProblems.gql("where test_id = '"+TestId+"'")
        #For teacher we are generating all questions at once..for other users only 5 questions at a time
        if user.IsTeacher:
            NewTestData = NewTestDataQuery.fetch(20)
        else:
            NewTestData = NewTestDataQuery.fetch(5)
        for n in NewTestData:
            concept = n.concept
            problem_type = n.problem_type
            if grade==4:
                ProblemDetails = GenerateP4TestProblems.GenerateP4TestProblems(concept,problem_type)
            elif grade==5:
                ProblemDetails = GenerateP5TestProblems.GenerateP5TestProblems(concept,problem_type)
            elif grade==6:
                ProblemDetails = GenerateP6TestProblems.GenerateP6TestProblems(concept,problem_type)
            elif grade==3:
                ProblemDetails = GenerateP3TestProblems.GenerateP3TestProblems(concept, problem_type)
            logging.info(ProblemDetails)
            try:
                n.problem=ProblemDetails['problem']
            except KeyError:
                pass
            try:
                n.dollar_unit=ProblemDetails['dollar_unit']
            except KeyError:
                pass
            try:
                n.unit=ProblemDetails['unit']
            except KeyError:
                pass
            try:
                n.answer=str(ProblemDetails['answer'])
            except KeyError:
                pass
            try:
                n.complexity_level=ProblemDetails['complexity_level']
            except KeyError:
                pass                    
            try:
                n.template=ProblemDetails['template']
            except KeyError:
                pass
            try:
                n.answer1=str(ProblemDetails['answer1'])
            except KeyError:
                pass                    
            try:
                n.answer2=str(ProblemDetails['answer2'])
            except KeyError:
                pass                    
            try:
                n.answer3=str(ProblemDetails['answer3'])
            except KeyError:
                pass                    
            try:
                n.answer4=str(ProblemDetails['answer4'])
            except KeyError:
                pass                    
            try:
                n.answerM1=str(ProblemDetails['answerM1'])
            except KeyError:
                pass                    
            try:
                n.answerM2=str(ProblemDetails['answerM2'])
            except KeyError:
                pass                    
            try:
                n.answerM3=str(ProblemDetails['answerM3'])
            except KeyError:
                pass                    
            try:
                n.answerM4=str(ProblemDetails['answerM4'])
            except KeyError:
                pass                    
            try:
                n.answerN1=str(ProblemDetails['answerN1'])
            except KeyError:
                pass                    
            try:
                n.answerN2=str(ProblemDetails['answerN2'])
            except KeyError:
                pass                    
            try:
                n.answerN3=str(ProblemDetails['answerN3'])
            except KeyError:
                pass                    
            try:
                n.answerN4=str(ProblemDetails['answerN4'])
            except KeyError:
                pass                    
            try:
                n.answerD1=str(ProblemDetails['answerD1'])
            except KeyError:
                pass                    
            try:
                n.answerD2=str(ProblemDetails['answerD2'])
            except KeyError:
                pass                    
            try:
                n.answerD3=str(ProblemDetails['answerD3'])
            except KeyError:
                pass                    
            try:
                n.answerD4=str(ProblemDetails['answerD4'])
            except KeyError:
                pass 
            try:
                n.value1=str(ProblemDetails['value1'])
            except KeyError:
                pass                    
            try:
                n.value2=str(ProblemDetails['value2'])
            except KeyError:
                pass                    
            try:
                n.value3=str(ProblemDetails['value3'])
            except KeyError:
                pass                    
            try:
                n.value4=str(ProblemDetails['value4'])
            except KeyError:
                pass                    
            try:
                n.explain=str(ProblemDetails['explain']['explain_text'])
            except KeyError:
                pass                    
            try:
                n.CheckAnswerType=ProblemDetails['CheckAnswerType']
            except KeyError:
                pass                                                                                
            try:
                n.FunctionCall=ProblemDetails['FunctionCall']
            except KeyError:
                pass 
            try:
                n.FractionAnswer=ProblemDetails['FractionAnswer']
            except KeyError:
                pass 
            n.put()

    def GetTestData(self, TestId, Counter, user):
        logging.info(TestId)
        logging.info(Counter)
        NewTestMasterQuery = TestsMaster.TestsMasterTable.gql("where test_id = '"+TestId+"'")
        NewTestMaster = NewTestMasterQuery.fetch(1)
        for n in NewTestMaster:
            questions = n.questions
        if questions < Counter:
            Counter = 1
        TestIndicator = list(NewTestMaster[0].TestIndicator)
        NewTestDataQuery = TestProblems.TestProblems.gql("where test_id = '"+TestId+"' and counter="+str(Counter))
        NewTestData = NewTestDataQuery.fetch(1)
        for n in NewTestData:
            if n.problem is None:
                '''07-OCT-2013:This is required for old tests where all problems were not generated at one go. Can delete this after few months.'''
                self.GenerateHCNewTestDataOLD(TestId, 0, user)
                NewTestData = NewTestDataQuery.fetch(1)
        for n in NewTestData:
            try:
                if n.answer_submitted!="" and n.answer_submitted!="None" and n.answer_submitted is not None:
                    NewTestMaster[0].TestIndicator[Counter-1] = "2"
                else:
                    NewTestMaster[0].TestIndicator[Counter-1] = "1"
            except IndexError:
                '''For old test there is no TestIndicator so creating one here'''
                TestIndicator = []
                for _i in range(questions):
                    TestIndicator.append("0")
                NewTestMaster[0].TestIndicator = list(TestIndicator)
                if n.answer_submitted!="" and n.answer_submitted!="None" and n.answer_submitted is not None:
                    NewTestMaster[0].TestIndicator[Counter-1] = "2"
                else:
                    NewTestMaster[0].TestIndicator[Counter-1] = "1"
            NewTestMaster[0].put()
            Config.test_values = {    'test_id':n.test_id,
                                      'concept':n.concept,
                                      'counter':n.counter,
                                      'questions':questions,
                                      'problem_type':n.problem_type,
                                      'problem':n.problem,
                                      'dollar_unit':n.dollar_unit,
                                      'unit':n.unit,
                                      'answer':n.answer,
                                      'answer_submitted':n.answer_submitted,
                                      'correct':n.correct,
                                      'time_taken':n.time_taken,
                                      'submit_date':n.submit_date,
                                      'complexity_level':n.complexity_level,
                                      'template':n.template,
                                      'answer1':n.answer1,
                                      'answer2':n.answer2,
                                      'answer3':n.answer3,
                                      'answer4':n.answer4,
                                      'answerM1':n.answerM1,
                                      'answerM2':n.answerM2,
                                      'answerM3':n.answerM3,
                                      'answerM4':n.answerM4,
                                      'answerN1':n.answerN1,
                                      'answerN2':n.answerN2,
                                      'answerN3':n.answerN3,
                                      'answerN4':n.answerN4,
                                      'answerD1':n.answerD1,
                                      'answerD2':n.answerD2,
                                      'answerD3':n.answerD3,
                                      'answerD4':n.answerD4,
                                      'value1':n.value1,
                                      'value2':n.value2,
                                      'value3':n.value3,
                                      'value4':n.value4,
                                      'explain':n.explain,
                                      'CheckAnswerType':n.CheckAnswerType,
                                      'status':n.status,
                                      'FunctionCall':n.FunctionCall,
                                      'FractionAnswer':n.FractionAnswer,
                                      'TestIndicator':TestIndicator
                                      }
            logging.info(n.template)
            logging.info(TestIndicator)
        return Config.test_values

def SubmitAnswer(TestId,Counter,answer_submitted):
    logging.info(" in submit answer :"+answer_submitted)
    NewTestDataQuery = TestProblems.TestProblems.gql("where test_id = '"+TestId+"' and counter="+str(Counter))
    NewTestData = NewTestDataQuery.fetch(1)
    for n in NewTestData:
        n.answer_submitted = answer_submitted
        if answer_submitted != "":
            n.submit_date = datetime.now()
        template_values = {"CheckAnswerType":n.CheckAnswerType,"template":n.template,"answer":n.answer}
        n.correct = Submit.CheckAnswer(n.concept,template_values,answer_submitted)
        n.put()
    TestMasterQuery = TestsMaster.TestsMasterTable.gql("where test_id = '"+TestId+"'")
    TestMasterData = TestMasterQuery.fetch(1)
    
    for t in TestMasterData:        
        if t.status == "New" and answer_submitted!="":
            t.status = "InProgress"
            t.update_date = datetime.now()
        if answer_submitted != "":
            t.TestIndicator[Counter-1] = "2"
        else:
            t.TestIndicator[Counter-1] = "1"
        t.put()

'''Defining how many questions to be generated for each concept type'''            
MaxQuestions = {'P5DA':10,
                'P5DC':12,
                'P5FR':12,
                'P5GT':10,
                'P5MT':12,
                'P5PR':10,
                'P5RT':10,
                'P5WN':12,
                'P6AG':12,
                'P6DA':5,
                'P6FR':8,
                'P6MT':12,
                'P6PR':10,
                'P6RT':10,
                'P6SP':10,
                'P4DA':10,
                'P3WN':12,
                'P3WNAddition':9,
                'P3WNComparingOrdering':10,
                'P3WNDivision':10,
                'P3WNFiguresToWords':6,
                'P3WNMultiplication':10,
                'P3WNNumberPatterns':6,
                'P3WNPlaceValues':10,
                'P3WNSubtraction':10,
                'P3WNWordsToFigures':6,
                'P3WNWordProblems':10,
                'P3MO':12,
                'P3MOAddition':10,
                'P3MOSubtraction':10,
                'P3MOWordProblems':10,
                'P3LM':12,
                'P3LMKiloGram':10,
                'P3LMKiloMetre':10,
                'P3LMLitresMilli':10,
                'P3LMMetreCentiMetre':10,
                'P3LMWordProblems_2Steps':10,
                'P3LMWordProblems':10,
                'P3TI':12,
                "P3TIAddition":9,
                "P3TIConversionTime":8,
                "P3TISubtraction":8,
                'P3TIDuration':10,
                'P3TITellingTime':10,
                'P3TIWordProblems':10,
                'P3AN':10,
                "P3ANIdentifying":6,
                "P3ANRightAngle":6,
                'P3BGBarGraphs':8,
                "P3APSquareUnits":8,
                "P3APSquareCmM":8,
                "P3APArea":8,
                "P3APPerimeter":8,
                "P3APWordProblems":8,
                "P3FRWhatIsFractions":8,
                "P3FREquivalentFractions":8,
                "P3FRSimplifyingFractions":7,
                "P3FRComparingOrdering":8,
                "P3FRAddition":8,
                "P3FRSubtraction":8,
                "P3PPPerpendicularParallel":8,
                'P4DecimalsAddSub':8,
                'P4DecimalsComparingOrdering':8,
                'P4DecimalsFractions':7,
                'P4DecimalsHundredths':10,
                'P4DecimalsMultiplyDivide':6,
                'P4DecimalsRoundingOff':6,
                'P4DecimalsTenths':10,
                'P4DecimalsThousandths':10,
                'P4DCWordProblems':9,
                'P4FractionsAdd':6,
                'P4FractionsMixedImproper':6,
                'P4FractionsMultiplication':6,
                'P4FractionsSimplifying':6,
                'P4FractionsSubtract':6,
                'P4FRWordProblems':7,
                'P4MTArea':6,
                'P4MTCompositeFigures':8,
                'P4MTPerimeter':6,
                'P4MTTime24Hrs':6,
                'P4MTTimeDuration':6,
                'P4WholeNumbersComparingOrdering':6,
                'P4WholeNumbersFactorMultiple':8,
                'P4WholeNumbersMutliplyDivide':6,
                'P4WholeNumbersPlaceValues':8,
                'P4WholeNumbersRoundingOff':6,
                'P4WholeNumbersWriteInFigures':6,
                'P4WholeNumbersWriteInWords':6,
                'P4WNWordProblems':8,
                'P4DATablesBarGraphs':6,
                'P4DALineGraphs':6,
                'P5DataAnalysisAverage':8,
                'P5DataAnalysisTotal':9,
                'P5DataAnalysisWordProblems':5,
                'P5DecimalsMultiplyDivide':8,
                'P5DecimalsRounding':8,
                'P5DecimalsWordProblems':10,
                'P5FractionsAddSubMixedFractions':8,
                'P5FractionsAddSubProperFractions':8,
                'P5FractionsMultProperImproperFractions':8,
                'P5FractionsMultMixedFractions':8,
                'P5FractionsDivideProperFractions':8,
                'P5FractionsWordProblems':10,
                'P5GeometryAngles':6,
                'P5GeometryFourSided':6,
                'P5GeometryTriangles':6,
                'P5MeasurementAreaOfTriangle':6,
                'P5MeasurementUnitConversion':6,
                'P5MeasurementVolume':6,
                'P5MeasurementWordProblems':5,
                'P5PercentageExpressAsDecimal':5,
                'P5PercentageExpressAsFraction':5,
                'P5PercentageExpressAsPercent':5,
                'P5PercentageWordProblems':8,
                'P5RatioMissingNumber':6,
                'P5RatioSimplestForm':6,
                'P5RatioWordProblems':8,
                'P5WholeNumbersWordProblems':10,
                'P5WholeNumbersApproximationEstimation':6,
                'P5WholeNumbersComparingAndOrdering':6,
                'P5WholeNumbersFindPattern':6,
                'P5WholeNumbersMultiplyDivide':6,
                'P5WholeNumbersOrderOfOperation':6,
                'P5WholeNumbersPlaceValue':8,
                'P5WholeNumbersWriteInFigures':5,
                'P5WholeNumbersWriteInWords':5,
                'P6AGEvaluationExpression':8,
                'P6AGSimplifyingExpression':5,
                'P6AGWordProblems':7,
                'P6DAWordProblems':6,
                'P6FRDivideProperFraction':7,
                'P6FRDivideWholeNumber':7,
                'P6FRWordProblems':5,
                'P6MTArea':6,
                'P6MTCircumference':6,
                'P6MTRadius':5,
                'P6MTComposite':8,
                'P6MTSemiArea':6,
                'P6MTSemiPerimeter':6,
                'P6MTVolume':6,
                'P6PRWordProblems':10,
                'P6PRIncDec':6,
                'P6PRFindWhole':6,
                'P6RTWordProblems':10,
                'P6SPWordProblems':10,
                'P6SPDTS':6,
               
                }            