'''
Created on Feb 7, 2012

Module: SimplifyingFractions
Generates "Expressing Mixed Numbers and Improper Fractions in its simplest form" problems for Primary 4

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random
from random import randint
from Utils import LcmGcf
from Utils import Factors

class SimplifyingFractions:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        self.RandomQ = randint(1,10)
        #70% of the time it will generate MCQs
        if self.RandomQ > 3:
            self.ProblemType = random.choice([self.GenerateProblemTypeMCQ1(),self.GenerateProblemTypeMCQ2()])
        else:
            self.ProblemType = random.choice([self.GenerateProblemType1(),self.GenerateProblemType2()])
        return self.ProblemType
        #return self.GenerateProblemTypeMCQ2()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    }
        
        #Creating one more problem type so it creates a list and not a list of lists
        self.ProblemTypes = []
        
        for i in self.ProblemType.values():
            for k in i:
                self.ProblemTypes.append(k)
                
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(random.choice(self.GenerateProblemType.values()))
        else:
            if LastProblemID in self.ProblemTypes:
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if LastProblemID in v][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return random.choice(self.GenerateProblemType[NextProblemKey])
            else:
                return random.choice(random.choice(self.GenerateProblemType.values()))
        #return self.GenerateProblemTypeMCQ2()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        ''' Generating 2 proper unlike fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = random.choice([4,6,8,9,10,12])
        self.mixed = randint(1,9)
        self.factors = Factors.Factors().find_factors(self.denominator)
        self.numerator1 = random.choice(self.factors)
        while self.numerator1==1 or self.numerator1==self.denominator:
            self.numerator1 = random.choice(self.factors)
        
        self.problem = "Express below mixed number in its simplest form:"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<tr><td valing='center'>"+str(self.mixed)+"</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "</tr></table>"

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(self.numerator1,self.denominator)        
        self.AnswerDenominator = self.denominator/gcf
        self.AnswerNumerator = self.numerator1/gcf
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer3 = self.mixed
        self.answer = str(self.answer3)+" "+str(self.answer1)+"/"+str(self.answer2)    
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.mixed,self.numerator1,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,}            
    
    def ExplainType1(self,problem,answer1,answer2,mixed,numerator1,denominator):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        self.answer_text = self.answer_text + "<td>"+str(mixed)+"</td>"
        self.answer_text = self.answer_text + "<td><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        gcf = LcmGcf.LcmGcf().find_gcf(numerator1, denominator) 
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Step 1: Find the common factor of "+str(numerator1)+" and "+str(denominator)+"<br><br>"
        self.solution_text = self.solution_text + "The common factor of "+str(numerator1)+" and "+str(denominator)+" is "+str(gcf)+"<br><br>"
        self.solution_text = self.solution_text + "Step 2: Divide both numerator and denominator by the common factor "+str(gcf)+"<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td>"+str(mixed)+"</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator))+"<del>"+str(numerator1)+"</del>"+str(answer1)+"&nbsp;"*len(str(denominator))+"</u><br>&nbsp;"+"<del>"+str(denominator)+"</del>"+str(answer2)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = "+str(mixed)+"</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(answer2))+str(answer1)+"&nbsp;"*len(str(answer2))+"</u><br>&nbsp;"+str(answer2)+"</td><tr></table>"
        self.solution_text = self.solution_text + "</tr></table>"
                       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType2(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.denominator = random.choice([4,6,8,9,10,12])
        self.numerator = randint(self.denominator+1,24)
        '''making sure whole number is not generated'''
        while self.numerator%self.denominator == 0:
            self.numerator = randint(self.denominator+1,24)
        
        gcf = LcmGcf.LcmGcf().find_gcf(self.numerator,self.denominator)
        
        while gcf==1 or gcf==self.denominator:
            self.numerator = self.numerator + 1
            gcf = LcmGcf.LcmGcf().find_gcf(self.numerator,self.denominator)
        
        self.problem = "Express below improper fraction in its simplest form:"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<tr><td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"&nbsp;"*len(str(self.numerator))+"</td>"
        self.problem = self.problem + "</tr></table>"

        gcf = LcmGcf.LcmGcf().find_gcf(self.numerator,self.denominator)                        

        self.answer1 = self.numerator/gcf
        self.answer2 = self.denominator/gcf
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer1,self.answer2,self.numerator,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,}            
    
    def ExplainType2(self,problem,answer1,answer2,numerator,denominator):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        gcf = LcmGcf.LcmGcf().find_gcf(numerator, denominator) 
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Step 1: Find the common factor of "+str(numerator)+" and "+str(denominator)+"<br><br>"
        self.solution_text = self.solution_text + "The common factor of "+str(numerator)+" and "+str(denominator)+" is "+str(gcf)+"<br><br>"
        self.solution_text = self.solution_text + "Step 2: Divide both numerator and denominator by the common factor "+str(gcf)+"<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td><u>"+"&nbsp;"*len(str(denominator))+"<del>"+str(numerator)+"</del>"+str(answer1)+"&nbsp;"*len(str(denominator))+"</u><br>&nbsp;"+"<del>"+str(denominator)+"</del>"+str(answer2)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;=&nbsp;</td><td><u>"+"&nbsp;"*len(str(answer2))+str(answer1)+"&nbsp;"*len(str(answer2))+"</u><br>&nbsp;"+str(answer2)+"</td><tr></table>"
        self.solution_text = self.solution_text + "</tr></table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
                   
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore,grade,CheckAnswerType):
                                    
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
                'explain':explain,'problem_type':problem_type,
                'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}       

    def GenerateProblemTypeMCQ1(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.CheckAnswerType = 3
                
        ''' Generating 2 proper unlike fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = random.choice([4,6,8,9,10,12])
        self.mixed = randint(1,9)
        self.factors = Factors.Factors().find_factors(self.denominator)
        self.numerator1 = random.choice(self.factors)
        while self.numerator1==1 or self.numerator1==self.denominator:
            self.numerator1 = random.choice(self.factors)
        
        self.problem = "Express below mixed number in its simplest form:"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<tr><td valing='center'>"+str(self.mixed)+"</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "</tr></table>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(self.numerator1,self.denominator)        
        self.AnswerDenominator = self.denominator/gcf
        self.AnswerNumerator = self.numerator1/gcf
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer3 = self.mixed   
        self.answer = [self.answer3,self.answer1,self.answer2]
        
        self.wrongAnswers = []
        '''generating 5 wrong answers and making sure any of it is not equal to the correct answer'''
        i = 0
        while i!=3:
            self.WrongDenominator = random.choice([self.AnswerDenominator,self.denominator])
            self.WrongNumerator = randint(1,self.WrongDenominator)
            self.WrongMixed = self.mixed            
            if(self.WrongNumerator!=self.AnswerNumerator):
                if [self.WrongMixed,self.WrongNumerator,self.WrongDenominator] not in self.wrongAnswers:
                    self.wrongAnswers.append([self.WrongMixed,self.WrongNumerator,self.WrongDenominator])
                    i = i+1
                           
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ1"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.mixed,self.numerator1,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)      

    def GenerateProblemTypeMCQ2(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.CheckAnswerType = 3
        

        self.denominator = random.choice([4,6,8,9,10,12])
        self.numerator = randint(self.denominator+1,24)
        '''making sure whole number is not generated'''
        while self.numerator%self.denominator == 0:
            self.numerator = randint(self.denominator+1,24)
        
        gcf = LcmGcf.LcmGcf().find_gcf(self.numerator,self.denominator)
        
        while gcf==1 or gcf==self.denominator:
            self.numerator = self.numerator + 1
            gcf = LcmGcf.LcmGcf().find_gcf(self.numerator,self.denominator)
        
        self.problem = "Express below improper fraction in its simplest form:"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<tr><td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"&nbsp;"*len(str(self.numerator))+"</td>"
        self.problem = self.problem + "</tr></table>"

        gcf = LcmGcf.LcmGcf().find_gcf(self.numerator,self.denominator)                        

        self.answer1 = self.numerator/gcf
        self.answer2 = self.denominator/gcf
        self.answer3 = 0
        self.answer = [self.answer3,self.answer1,self.answer2]     
        
        self.wrongAnswers = []
        '''generating 5 wrong answers and making sure any of it is not equal to the correct answer'''
        i = 0
        while i!=3:
            self.WrongDenominator = random.choice([self.answer2,self.denominator])
            self.WrongNumerator = randint(self.WrongDenominator+1,24)
            self.WrongMixed = 0           
            if(self.WrongNumerator!=self.answer1):
                if [self.WrongMixed,self.WrongNumerator,self.WrongDenominator] not in self.wrongAnswers:
                    self.wrongAnswers.append([self.WrongMixed,self.WrongNumerator,self.WrongDenominator])
                    i = i+1
                    
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ2"
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer1,self.answer2,self.numerator,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)      
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
        if CheckAnswerType == 1:
                if "/" in str(InputAnswer):
                    try:
                        AnswerNumerator = int(str(answer).partition("/")[0])
                        AnswerDenominator = int(str(answer).partition("/")[2])             
                        InputNumerator = int(str(InputAnswer).partition("/")[0])
                        InputDenominator = int(str(InputAnswer).partition("/")[2])
                        return (AnswerNumerator==InputNumerator and AnswerDenominator==InputDenominator)
                    except ValueError:
                        return False
                else:
                    return False
        elif CheckAnswerType == 2:
                if " " in str(InputAnswer):             
                    try:
                        InputMixed = int(str(InputAnswer).partition(" ")[0])
                        RemainingInput = str(InputAnswer).partition(" ")[2]
                        InputDenominator = int(str(RemainingInput).partition("/")[2])
                        InputNumerator = int(str(RemainingInput).partition("/")[0])            
                        AnswerMixed = int(str(answer).partition(" ")[0])
                        RemainingInput = str(answer).partition(" ")[2]
                        AnswerDenominator = int(str(RemainingInput).partition("/")[2])
                        AnswerNumerator = int(str(RemainingInput).partition("/")[0])
                        return (AnswerMixed==InputMixed and AnswerNumerator==InputNumerator and AnswerDenominator==InputDenominator)
                    except ValueError:
                        return False                                 
        elif CheckAnswerType == 3:
            answer = str(answer)
            InputAnswer = "["+str(InputAnswer).partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[2]+"]"
            if(answer==InputAnswer):
                return True
            else:
                return False