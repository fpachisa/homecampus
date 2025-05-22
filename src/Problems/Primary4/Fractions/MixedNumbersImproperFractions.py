'''
Created on Feb 2, 2012

Module: MixedNumbersImproperFractions
Generates "Mixed Numbers and Improper Fractions" problems for Primary 4

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
from decimal import Decimal
import logging

class MixedNumbersImproperFractions:
    
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
        #return self.GenerateProblemType1()
        
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
        self.denominator = randint(2,12)
        self.numerator = randint(self.denominator+1,24)
        '''making sure mixed fraction is generated'''
        while self.numerator%self.denominator == 0:
            self.numerator = randint(self.denominator+1,24)

        self.mixed, self.numerator1 = divmod(self.numerator,self.denominator)
        
        self.problem = "Convert below mixed number into improper fraction:"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<tr><td valing='center'>"+str(self.mixed)+"</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator
        self.AnswerNumerator = self.numerator
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.mixed,self.numerator,self.numerator1,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,}            
    
    def ExplainType1(self,problem,answer1,answer2,mixed,numerator,numerator1,denominator):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))
        #Adding the simplified fraction if possible
        if gcf!=1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td>"              
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Step 1: Split the mixed number as shown below.<br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td>"+str(mixed)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(denominator))+str(numerator1)+"&nbsp;"*len(str(denominator))+"</u><br>&nbsp;"+str(denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = "+str(mixed)+" +&nbsp;</td>"
        self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(denominator))+str(numerator1)+"&nbsp;"*len(str(denominator))+"</u><br>&nbsp;"+str(denominator)+"</td><tr></table>"
        self.solution_text = self.solution_text + "<br>Step 2: Multiply the whole number with the denominator of the fraction<br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp; = &nbsp;</td><td><u>"+"&nbsp;"*len(str(denominator))+str(mixed)+" &times; "+str(denominator)+"&nbsp;"*len(str(denominator))+"</u><br>"+"&nbsp;"*len(str(denominator))+"1 &times; "+str(denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;+&nbsp;</td><td><u>"+"&nbsp;"*len(str(denominator))+str(numerator1)+"&nbsp;"*len(str(denominator))+"</u><br>&nbsp;"+str(denominator)+"</td><tr></table>"
        self.solution_text = self.solution_text + "<br>Step 3: Add the fractions<br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp; = &nbsp;</td><td><u>"+"&nbsp;"*len(str(denominator))+str(mixed*denominator)+" + "+str(numerator1)+"&nbsp;"*len(str(denominator))+"</u><br>"+"&nbsp;"*(len(str(mixed*denominator+numerator1))+4)+str(denominator)+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        if gcf!=1:
            self.solution_text = self.solution_text + "<br>It can be further simplified to:"
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
            self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(answer2))+"<del>"+str(answer1)+"</del>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;"*len(str(answer2))+"</u><br>"+"&nbsp;"*len(str(answer1))+"<del>"+str(self.answer2)+"</del>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            self.solution_text = self.solution_text + "<td>&nbsp;= &nbsp;</td>"
            self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td></tr></table>"           
                       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType2(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        ''' Generating 2 proper unlike fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = randint(2,12)
        self.numerator = randint(self.denominator+1,24)
        '''making sure mixed fraction is generated'''
        while self.numerator%self.denominator == 0:
            self.numerator = randint(self.denominator+1,24)

        self.mixed, self.numerator1 = divmod(self.numerator,self.denominator)
        
        self.problem = "Convert below improper fraction into mixed number:"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<tr><td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"&nbsp;"*len(str(self.numerator))+"</td>"
        self.problem = self.problem + "</tr></table>"

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
                
        self.AnswerMixed = self.mixed
        self.AnswerDenominator = self.denominator
        self.AnswerNumerator = self.numerator1
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer3 = self.AnswerMixed
        self.answer = str(self.answer3)+" "+str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer1,self.answer2,self.answer3,self.numerator,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,}            
    
    def ExplainType2(self,problem,answer1,answer2,answer3,numerator,denominator):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        self.ordinal = {2:"half",3:"third",4:"fourth",5:"fifth",6:"sixth",7:"seventh",8:"eight",9:"ninth",10:"tenth",11:"eleventh",12:"twelfth"}
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))
        #Adding the simplified fraction if possible
        if gcf!=1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            self.answer_text = self.answer_text + "<td>"+str(answer3)+"</td>"
            self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td>"              
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td>"+str(answer3)+"</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Divide the numerator by denominator<br><br>"
        self.solution_text = self.solution_text + str(numerator)+" &divide; "+str(denominator)+" = "+str(answer3)+" R "+str(answer1)+"<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td>There are "+str(answer3)+" wholes and "+str(answer1)+" "+self.ordinal[answer2]+" in &nbsp;</td>"
        self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(denominator))+str(numerator)+"&nbsp;"*len(str(denominator))+"</u><br>"+"&nbsp;"*len(str(numerator))+str(denominator)+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(denominator))+str(numerator)+"&nbsp;"*len(str(denominator))+"</u><br>"+"&nbsp;"*len(str(numerator))+str(denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;= &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(answer3)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td></tr></table>"
        if gcf!=1:
            self.solution_text = self.solution_text + "<br>It can be further simplified to:"
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
            self.solution_text = self.solution_text + "<td>"+str(answer3)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.answer2))+"<del>"+str(self.answer1)+"</del>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+"<del>"+str(self.answer2)+"</del>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            self.solution_text = self.solution_text + "<td>&nbsp;= &nbsp;</td>"
            self.solution_text = self.solution_text + "<td>"+str(answer3)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td></tr></table>"           
        
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
        self.denominator = randint(2,12)
        self.numerator = randint(self.denominator+1,24)
        '''making sure mixed fraction is generated'''
        while self.numerator%self.denominator == 0:
            self.numerator = randint(self.denominator+1,24)

        self.mixed, self.numerator1 = divmod(self.numerator,self.denominator)
        
        self.problem = "Convert below mixed number into improper fraction:"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+str(self.mixed)+"</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator
        self.AnswerNumerator = self.numerator
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
        self.answer1 = self.AnswerNumerator/gcf
        self.answer2 = self.AnswerDenominator/gcf
        self.answer = [0,self.answer1,self.answer2]
        
        self.wrongAnswers = []
        '''generating 5 wrong answers and making sure any of it is not equal to the correct answer'''
        i = 0
        while i!=5:
            self.WrongDenominator = randint(2,12)
            self.WrongNumerator = randint(self.WrongDenominator+1,24)
            self.WrongMixed = 0            
            if(Decimal(self.WrongNumerator)/Decimal(self.WrongDenominator)!=Decimal(self.AnswerNumerator)/Decimal(self.AnswerDenominator) and self.WrongNumerator%self.WrongDenominator!=0):
                if [self.WrongMixed,self.WrongNumerator,self.WrongDenominator] not in self.wrongAnswers:
                    self.wrongAnswers.append([self.WrongMixed,self.WrongNumerator,self.WrongDenominator])
                    i = i+1
                           
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ1"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.mixed,self.numerator,self.numerator1,self.denominator)
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
        
        ''' Generating 2 proper unlike fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = randint(2,12)
        self.numerator = randint(self.denominator+1,24)
        '''making sure mixed fraction is generated'''
        while self.numerator%self.denominator == 0:
            self.numerator = randint(self.denominator+1,24)

        self.mixed, self.numerator1 = divmod(self.numerator,self.denominator)
        
        self.problem = "Convert below improper fraction into mixed number:"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<tr><td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"&nbsp;"*len(str(self.numerator))+"</td>"
        self.problem = self.problem + "</tr></table>"
                
        self.AnswerMixed = self.mixed
        self.AnswerDenominator = self.denominator
        self.AnswerNumerator = self.numerator1
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
        self.answer1 = self.AnswerNumerator/gcf
        self.answer2 = self.AnswerDenominator/gcf      
        self.answer3 = self.AnswerMixed
        self.answer = [self.answer3,self.answer1,self.answer2]     
        
        self.wrongAnswers = []
        '''generating 5 wrong answers and making sure any of it is not equal to the correct answer'''
        i = 0
        while i!=5:
            self.WrongDenominator = randint(2,12)
            self.WrongNumerator = randint(self.WrongDenominator+1,24)
            self.WrongMixed,self.WrongNumerator = divmod(self.WrongNumerator,self.WrongDenominator)            
            if(Decimal(self.WrongNumerator)/Decimal(self.WrongDenominator)!=Decimal(self.AnswerNumerator)/Decimal(self.AnswerDenominator) and self.WrongNumerator%self.WrongDenominator!=0):
                if [self.WrongMixed,self.WrongNumerator,self.WrongDenominator] not in self.wrongAnswers:
                    self.wrongAnswers.append([self.WrongMixed,self.WrongNumerator,self.WrongDenominator])
                    i = i+1
                    
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ2"
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer1,self.answer2,self.answer3,self.numerator,self.denominator)
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
                        AnswerGCF = LcmGcf.LcmGcf().find_gcf(AnswerNumerator,AnswerDenominator)
                        InputNumerator = int(str(InputAnswer).partition("/")[0])
                        InputDenominator = int(str(InputAnswer).partition("/")[2])
                        InputGCF = LcmGcf.LcmGcf().find_gcf(InputNumerator,InputDenominator)
                        return (AnswerNumerator/AnswerGCF==InputNumerator/InputGCF and AnswerDenominator/AnswerGCF==InputDenominator/InputGCF)
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
                        AnswerGCF = LcmGcf.LcmGcf().find_gcf(AnswerNumerator,AnswerDenominator)
                        InputGCF = LcmGcf.LcmGcf().find_gcf(InputNumerator,InputDenominator)
                        return (AnswerMixed==InputMixed and AnswerNumerator/AnswerGCF==InputNumerator/InputGCF and AnswerDenominator/AnswerGCF==InputDenominator/InputGCF)
                    except ValueError:
                        return False                                 
        elif CheckAnswerType == 3:          
            answer = str(answer)
            InputAnswer = "["+str(InputAnswer).partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[2]+"]"
            if(answer==InputAnswer):
                return True
            else:
                return False