'''
Created on Feb 24, 2011

Module: MultMixedFractions
Generates "multiplication of mixed fraction with a whole number" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random
from random import randint
from Utils import LcmGcf
from decimal import Decimal

class MultMixedFractions:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        self.RandomQ = randint(1,10)
        #70% of the time it will generate MCQs
        if self.RandomQ > 3:
            self.ProblemType = random.choice([self.GenerateProblemTypeMCQ1()])
        else:
            self.ProblemType = random.choice([self.GenerateProblemType1()])
        return self.ProblemType
        #return self.GenerateProblemTypeMCQ1()           
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            }
        return self.ProblemType[problem_type]
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:"ProblemType1",2:"ProblemTypeMCQ1",}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemTypeMCQ1(),}
        
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(self.GenerateProblemType.values())
        else:
            if LastProblemID in self.ProblemType.values():
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if v == LastProblemID][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return self.GenerateProblemType[NextProblemKey]
            else:
                return random.choice(self.GenerateProblemType.values())
        #return self.GenerateProblemType1()
        
    def GenerateProblemType1(self):
        #Generating one mixed fraction and one whole number       
        self.denominator1 = randint(2,12)
        self.numerator1 = randint(self.denominator1+1,24)
        '''making sure mixed fraction is generated'''
        while self.numerator1%self.denominator1 == 0:
            self.numerator1 = randint(self.denominator1+1,24)
        self.mixed1, self.numerator11 = divmod(self.numerator1,self.denominator1)
        self.WholeNumber = randint(2,12)
        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td valign='middle'>"+str(self.mixed1)+"</td>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator11)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td valign='middle'>&nbsp; x &nbsp;</td>"
        self.problem = self.problem + "<td align='center' valign='middle'>"+str(self.WholeNumber)+"</td>"
        self.problem = self.problem + "<td align='center' valign='middle'>&nbsp;=</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator1
        self.AnswerNumerator = (self.denominator1*self.mixed1 + self.numerator11) * self.WholeNumber
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.AnswerNumerator), int(self.AnswerDenominator))

        self.answer1 = self.AnswerNumerator/gcf
        self.answer2 = self.AnswerDenominator/gcf
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.mixed1,self.numerator11,self.denominator1,self.WholeNumber)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1"}            
    
    def ExplainType1(self,problem,answer1,answer2,mixed1,numerator11,denominator1,WholeNumber):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        if answer1<answer2:
            self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td>"
        elif answer1%answer2 == 0:
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(answer1/answer2)+"&nbsp;</td>"
        else:
            mixed,answer11 = divmod(answer1,answer2)
            self.answer_text = self.answer_text +"<td align='center'>"+str(mixed)+"</td>"
            self.answer_text = self.answer_text +"<td align='center'><u>&nbsp;"+str(answer11)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td>"            
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Convert mixed fraction to an improper fraction.<br>"
        self.solution_text = self.solution_text + "To add mixed fractions, convert each mixed fraction to an improper fraction.<br>"
        self.solution_text = self.solution_text + "Multiply whole number by denominator, then add numerator to the product to get the new numerator.<br>"
        self.solution_text = self.solution_text + "Denominator stays the same.<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        numerator1 = (mixed1*denominator1+numerator11)
        self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td valign='center'> &times; </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(WholeNumber)+"&nbsp;</u><br>&nbsp; 1</td>"
        self.solution_text = self.solution_text + "<td align='center'> = </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(WholeNumber)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(1)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is:  </td><td align='center'><u>&nbsp;"+str(WholeNumber*numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"               
        if answer1>answer2:
            mixed,answer11 = divmod(answer1,answer2)
            self.solution_text = self.solution_text + "</tr></table><table class='FractionsTable' style='color:white'><tr><td>Above answer can be expressed as mixed number: </td>"
            self.solution_text = self.solution_text +"<td align='center'>"+str(mixed)+"</td>"
            self.solution_text = self.solution_text +"<td align='center'><u>&nbsp;"+str(answer11)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td>"            
        self.solution_text = self.solution_text + "</tr></table>"        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
                   
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type):
        
        '''Removing correct answers from the wrongAnswers list'''
        wrongAnswers = filter(self.removeCorrectAnswer,wrongAnswers)
                             
        '''Randomly selecting 3 wrong answers and adding the correct answer as well'''
        try:
            wrongAnswers = random.sample(wrongAnswers,3)
        except ValueError:
            pass
            
        wrongAnswers.append(answer)
        random.shuffle(wrongAnswers)
        try:
            self.answer1 = wrongAnswers[0]
            self.answer2 = wrongAnswers[1]
            self.answer3 = wrongAnswers[2]
            self.answer4 = wrongAnswers[3]        
        except IndexError:
            pass
        try:
            self.value1 = str(self.answer1[0])+"/"+str(self.answer1[1])+"/"+str(self.answer1[2])
            self.value2 = str(self.answer2[0])+"/"+str(self.answer2[1])+"/"+str(self.answer2[2])
            self.value3 = str(self.answer3[0])+"/"+str(self.answer3[1])+"/"+str(self.answer3[2])
            self.value4 = str(self.answer4[0])+"/"+str(self.answer4[1])+"/"+str(self.answer4[2])
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answerM1':self.answer1[0],'answerN1':self.answer1[1],'answerD1':self.answer1[2],
                'answerM2':self.answer2[0],'answerN2':self.answer2[1],'answerD2':self.answer2[2],
                'answerM3':self.answer3[0],'answerN3':self.answer3[1],'answerD3':self.answer3[2],
                'answerM4':self.answer4[0],'answerN4':self.answer4[1],'answerD4':self.answer4[2],
                'value1':self.value1,'value2':self.value2,'value3':self.value3,'value4':self.value4,
                'explain':explain,'problem_type':problem_type}           

    def GenerateProblemTypeMCQ1(self):
        #Generating one mixed fraction and one whole number       
        self.denominator1 = randint(2,12)
        self.numerator1 = randint(self.denominator1+1,24)
        '''making sure mixed fraction is generated'''
        while self.numerator1%self.denominator1 == 0:
            self.numerator1 = randint(self.denominator1+1,24)
        self.mixed1, self.numerator11 = divmod(self.numerator1,self.denominator1)
        self.WholeNumber = randint(2,12)
        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td valign='middle' align='right'>"+str(self.mixed1)+"</td>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator11)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td valign='middle'>&nbsp; x &nbsp;</td>"
        self.problem = self.problem + "<td align='center' valign='middle'>"+str(self.WholeNumber)+"</td>"
        self.problem = self.problem + "<td align='center' valign='middle'>&nbsp;=</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator1
        self.AnswerNumerator = (self.denominator1*self.mixed1 + self.numerator11) * self.WholeNumber
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.AnswerNumerator), int(self.AnswerDenominator))
     
        self.answer1 = self.AnswerNumerator/gcf
        self.answer2 = self.AnswerDenominator/gcf
        self.mixed,self.answer11 = divmod(self.answer1,self.answer2)
        self.answer = [self.mixed,self.answer11,self.answer2]
        
        self.wrongAnswers = []
        '''generating 5 wrong answers and making sure any of it is not equal to the correct answer'''
        i = 0
        while i!=5:
            self.WrongDenominator = randint(2,12)
            self.WrongNumerator = randint(self.WrongDenominator+1,36)            
            if Decimal(self.WrongNumerator)/Decimal(self.WrongDenominator)!=Decimal(self.AnswerNumerator)/Decimal(self.AnswerDenominator):
                self.WrongMixed,self.WrongNumerator = divmod(self.WrongNumerator,self.WrongDenominator)
                if [self.WrongMixed,self.WrongNumerator,self.WrongDenominator] not in self.wrongAnswers:
                    self.wrongAnswers.append([self.WrongMixed,self.WrongNumerator,self.WrongDenominator])
                    i = i+1
                           
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ1"
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.mixed1,self.numerator11,self.denominator1,self.WholeNumber)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)      
   
    def checkAnswer(self,template,answer,InputAnswer):
        if (template=="FractionMCQTypeProblems.html"):
            answer=str(answer)
            InputAnswer = "["+str(InputAnswer).partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[2]+"]"
            if(answer==InputAnswer):
                return True
            else:
                return False
        else:
            try:
                AnswerNumerator = int(str(answer).partition("/")[0])
                AnswerDenominator = int(str(answer).partition("/")[2])
                
                if " " in str(InputAnswer):             
                    InputMixed = int(str(InputAnswer).partition(" ")[0])
                    RemainingInput = str(InputAnswer).partition(" ")[2]
                    InputDenominator = int(str(RemainingInput).partition("/")[2])
                    InputNumerator = int(str(RemainingInput).partition("/")[0])+InputMixed*InputDenominator
                elif "/" in str(InputAnswer):
                    InputMixed = 0
                    InputNumerator = int(str(InputAnswer).partition("/")[0])
                    InputDenominator = int(str(InputAnswer).partition("/")[2])
                else:
                    InputNumerator = int(str(InputAnswer))
                    InputDenominator = 1
                return Decimal(AnswerNumerator)/Decimal(AnswerDenominator)==Decimal(InputNumerator)/Decimal(InputDenominator)
            except ValueError:
                return False