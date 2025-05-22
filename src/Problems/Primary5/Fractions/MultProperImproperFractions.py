'''
Created on Feb 24, 2011

Module: MultProperImproperFractions
Generates "multiplication of proper and improper fractions" problems for Primary 5

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

class MultProperImproperFractions:
    
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
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        ''' Generating 2 proper unlike fractions(numerator>denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = random.choice([randint(1,20),randint(1,self.denominator1-1)])
        self.numerator2 = random.choice([randint(1,20),randint(1,self.denominator2-1)])
        
        self.problem = "<table class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td valign='center'>&nbsp; x &nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td align='center'>&nbsp;=</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator1*self.denominator2
        self.AnswerNumerator = self.numerator1*self.numerator2
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,self.denominator2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1"}            
    
    def ExplainType1(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.answer1), int(self.answer2))
        '''Adding the simplified fraction if possible'''
        if gcf!=1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"              
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer1)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td valign='center'> &times; </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'> = </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is </td><td align='center'><u>&nbsp;"+str(numerator1*numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator1*denominator2)+"</td>"               
        if gcf!=1:
            self.solution_text = self.solution_text + "</tr><tr><td>It can be further simplified to </td>"
            if self.SimpleAnswer2!=1:
                self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.solution_text = self.solution_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "</tr></table>"        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
                   
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type):
                                    
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
        ''' Generating 2 proper unlike fractions(numerator>denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = random.choice([randint(1,20),randint(1,self.denominator1-1)])
        self.numerator2 = random.choice([randint(1,20),randint(1,self.denominator2-1)])
        
        self.problem = "<table class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td valign='center'>&nbsp; x &nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td align='center'>&nbsp;=</td>"
        self.problem = self.problem + "</tr></table>"

        self.AnswerDenominator = self.denominator1*self.denominator2
        self.AnswerNumerator = self.numerator1*self.numerator2
        
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
        '''Simplifying the fraction if possible'''
        self.SimpleAnswerNumerator = self.AnswerNumerator/gcf
        self.SimpleAnswerDenominator = self.AnswerDenominator/gcf
        
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
     
        self.SimpleAnswer1 = self.SimpleAnswerNumerator
        self.SimpleAnswer2 = self.SimpleAnswerDenominator
        self.answer = [0,self.SimpleAnswer1,self.SimpleAnswer2]
        
        self.wrongAnswers = []
        '''generating 5 wrong answers and making sure any of it is not equal to the correct answer'''
        i = 0
        while i!=5:
            self.WrongDenominator1 = randint(2,12)
            self.WrongNumerator1 = randint(1,12)
            self.WrongDenominator2 = randint(2,12)
            self.WrongNumerator2 = randint(1,12)                      
            self.WrongDenominator = self.WrongDenominator1*self.WrongDenominator2
            self.WrongNumerator = self.WrongNumerator1*self.WrongNumerator2
             
            if(Decimal(self.WrongNumerator)/Decimal(self.WrongDenominator)!=Decimal(self.answer1)/Decimal(self.answer2)):
                if [self.WrongNumerator,self.WrongDenominator] not in self.wrongAnswers:
                    self.wrongAnswers.append([0,self.WrongNumerator,self.WrongDenominator])
                    i = i + 1
                           
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ1"
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,self.denominator2)
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
                AnswerNumerator = str(answer).partition("/")[0]
                AnswerDenominator = str(answer).partition("/")[2]

                gcf = LcmGcf.LcmGcf().find_gcf(int(AnswerNumerator), int(AnswerDenominator))

                '''Simplifying the fraction if possible'''
                SimpleAnswerNumerator = int(AnswerNumerator)/gcf
                SimpleAnswerDenominator = int(AnswerDenominator)/gcf
                
                InputNumerator = str(InputAnswer).partition("/")[0]
                InputDenominator = str(InputAnswer).partition("/")[2]
                '''Making sure the InputAnswer denominator value is 1 even if its not entered in case the answer is 1 so that we don't get ValueError'''
                if InputDenominator=="":
                    InputDenominator="1"
                
                if ((int(AnswerNumerator)==int(InputNumerator) and int(AnswerDenominator)==int(InputDenominator)) or ((int(SimpleAnswerNumerator)==int(InputNumerator) and int(SimpleAnswerDenominator)==int(InputDenominator)))):
                    return True
            except ValueError:
                return False