'''
Created on Feb 11, 2012

Module: AddLikeRelatedFractions
Generates "Addition subtraction proper fractions" problems for Primary 4

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
from Utils import Factors

class AddLikeRelatedFractions:
    
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
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType5","ProblemTypeMCQ5",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemType5(),self.GenerateProblemTypeMCQ5(),],
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
        #return self.GenerateProblemTypeMCQ5()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            }
        return self.ProblemType[problem_type]
            
    def GenerateProblemType1(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = randint(3,12)
        self.numerator1 = randint(1,self.denominator-1)
        self.numerator2 = randint(1,self.denominator-1)
        
        self.problem = "Add:<br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td> &nbsp;= <td>"
        self.problem = self.problem + "</tr></table>"
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator
        self.AnswerNumerator = self.numerator1 + self.numerator2
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,}            
    
    def ExplainType1(self,problem,answer1,answer2,numerator1,numerator2,denominator):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(answer1,answer2)
        #Adding the simplified fraction if possible        
        if gcf!=1:
            self.SimpleAnswer1 = answer1/gcf
            self.SimpleAnswer2 = answer2/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td>"              
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        if answer1%answer2!=0:
            self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td>"
        else:
            self.answer_text = self.answer_text + "<td>&nbsp;"+str(answer1/answer2)+"&nbsp;</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;and&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'> do have same denominator. They are like fractions.</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br>To add like fractions, simply add the two numerators.<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td><u>&nbsp;"+str(numerator1)+" + "+str(numerator2)+"&nbsp;</u><br>"+"&nbsp;"*(len(str(numerator1))+len(str(numerator2))+2)+str(denominator)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td><td><u>"+"&nbsp;"*len(str(answer2))+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td>"               
        if gcf!=1:
            self.solution_text = self.solution_text + "</tr><tr><td>It can be further simplified to </td></tr></table>"
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
            if self.SimpleAnswer2!=1:
                self.solution_text = self.solution_text + "<tr><td align='center'><u>"+"&nbsp;"*len(str(answer2))+"<del>"+str(answer1)+"</del>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;"*len(str(answer2))+"</u><br>"+"&nbsp;"*len(str(answer1))+"<del>"+str(self.answer2)+"</del>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
                self.solution_text = self.solution_text + "<td>&nbsp;= &nbsp;</td>"
                self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td></tr></table>"           
            else:
                self.solution_text = self.solution_text + "<tr><td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "</tr></table>"                       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType2(self):
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = randint(3,12)
        self.numerator1 = randint(1,self.denominator-1)
        self.numerator2 = randint(1,self.denominator-1)
        
        self.problem = "Add and express the fraction in its simplest form:<br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td> &nbsp;= <td>"
        self.problem = self.problem + "</tr></table>"
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator
        self.AnswerNumerator = self.numerator1 + self.numerator2
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator,self.AnswerDenominator)
        self.answer1 = self.AnswerNumerator/gcf
        self.answer2 = self.AnswerDenominator/gcf
        self.answer = str(self.answer1)+"/"+str(self.answer2)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,}            
    
    def ExplainType2(self,problem,answer1,answer2,numerator1,numerator2,denominator):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(numerator1+numerator2,denominator)
        self.SimpleAnswer1 = answer1
        self.SimpleAnswer2 = answer2
        if answer1%answer2!=0:
            self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td>"
        else:
            self.answer_text = self.answer_text + "<td>&nbsp;"+str(answer1/answer2)+"&nbsp;</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator))+str(numerator1)+"&nbsp;"*len(str(denominator))+"</u><br>&nbsp;"+str(denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;and&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator))+str(numerator2)+"&nbsp;"*len(str(denominator))+"</u><br>&nbsp;"+str(denominator)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'> do have same denominator. They are like fractions.</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br>To add like fractions, simply add the two numerators.<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td><u>&nbsp;"+str(numerator1)+" + "+str(numerator2)+"&nbsp;</u><br>"+"&nbsp;"*(len(str(numerator1))+len(str(numerator2))+2)+str(denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator))+str(numerator1+numerator2)+"&nbsp;"*len(str(denominator))+"</u><br>&nbsp;"+str(denominator)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        if gcf!=1:
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>It requires further simplification:</td></tr></table>"            
            if self.SimpleAnswer2!=1:
                self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
                self.solution_text = self.solution_text + "<tr><td align='center'><u>"+"&nbsp;"*len(str(answer2))+"<del>"+str(numerator1+numerator2)+"</del>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;"*len(str(answer2))+"</u><br>"+"&nbsp;"*len(str(answer1))+"<del>"+str(denominator)+"</del>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
                self.solution_text = self.solution_text + "<td>&nbsp;= &nbsp;</td>"
                self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td></tr></table>"
                self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td>"
                self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td></tr></table>"                
            else:
                self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td>"
                self.solution_text = self.solution_text + "<tr><td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td><td><u>"+"&nbsp;"*len(str(answer2))+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td></tr></table>"   
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType3(self):
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator1 = random.choice([4,6,8,9,10,12])
        self.denominator2 = random.choice(Factors.Factors().find_factors(self.denominator1))
        while self.denominator2 == 1 or self.denominator2 == self.denominator1:
            self.denominator2 = random.choice(Factors.Factors().find_factors(self.denominator1))
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        
        self.problem = "Add and express the fraction in its simplest form:<br><br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator1))+"</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator2))+"</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td> &nbsp;= <td>"
        self.problem = self.problem + "</tr></table>"
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator1
        self.AnswerNumerator = self.numerator1 + self.numerator2*self.denominator1/self.denominator2
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator,self.AnswerDenominator)
        self.answer1 = self.AnswerNumerator/gcf
        self.answer2 = self.AnswerDenominator/gcf
        self.answer = str(self.answer1)+"/"+str(self.answer2)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,self.denominator2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,}            
    
    def ExplainType3(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(numerator1+numerator2*denominator1/denominator2,denominator1)
        self.SimpleAnswer1 = answer1
        self.SimpleAnswer2 = answer2
        if answer1%answer2!=0:
            self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td>"
        else:
            self.answer_text = self.answer_text + "<td>&nbsp;"+str(answer1/answer2)+"&nbsp;</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator1)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;and&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator2))+str(numerator2)+"&nbsp;"*len(str(denominator2))+"</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'>&nbsp;do not have same denominator.</td></tr>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br>However, "+str(denominator2)+" is a factor of "+str(denominator1)+". To make both denominators equal multiply the smaller denominator with "+str(denominator1/denominator2)+"<br><br>"
        self.solution_text = self.solution_text + "Remember to multiply the numerator as well with the same number<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td>=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator1)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;+&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(numerator2)+" &times; "+str(denominator1/denominator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(denominator1/denominator2)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td>=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator1)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;+&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator2*denominator1/denominator2)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"       
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td>=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(numerator1)+" + "+str(numerator2*denominator1/denominator2)+"&nbsp;</u><br>"+"&nbsp;"*(len(str(numerator1))+len(str(numerator2))+2)+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator1+numerator2*denominator1/denominator2)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        if gcf!=1:
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>It requires further simplification:</td></tr></table>"            
            if self.SimpleAnswer2!=1:
                self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
                self.solution_text = self.solution_text + "<tr><td align='center'><u>"+"&nbsp;"*len(str(answer2))+"<del>"+str(numerator1+numerator2*denominator1/denominator2)+"</del>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;"*len(str(answer2))+"</u><br>"+"&nbsp;"*len(str(answer1))+"<del>"+str(denominator1)+"</del>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
                self.solution_text = self.solution_text + "<td>&nbsp;= &nbsp;</td>"
                self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td></tr></table>"
                self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td>"
                self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td></tr></table>"                
            else:
                self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td>"
                self.solution_text = self.solution_text + "<tr><td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td><td><u>"+"&nbsp;"*len(str(answer2))+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td></tr></table>"   
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType4(self):
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator1 = random.choice([4,6,8,9,10,12])
        self.denominator2 = random.choice(Factors.Factors().find_factors(self.denominator1))
        while self.denominator2 == 1 or self.denominator2 == self.denominator1:
            self.denominator2 = random.choice(Factors.Factors().find_factors(self.denominator1))
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        self.numerator3 = randint(1,self.denominator1-1)
        
        self.problem = "Add and express the fraction in its simplest form:<br><br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator1))+"</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator2))+"</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator3)+"&nbsp;"*len(str(self.denominator1))+"</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td> &nbsp;= <td>"
        self.problem = self.problem + "</tr></table>"
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator1
        self.AnswerNumerator = self.numerator1 + self.numerator2*self.denominator1/self.denominator2 + self.numerator3
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator,self.AnswerDenominator)
        self.answer1 = self.AnswerNumerator/gcf
        self.answer2 = self.AnswerDenominator/gcf
        self.answer = str(self.answer1)+"/"+str(self.answer2)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.numerator3,self.denominator1,self.denominator2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,}            
    
    def ExplainType4(self,problem,answer1,answer2,numerator1,numerator2,numerator3,denominator1,denominator2):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(numerator1+numerator2*denominator1/denominator2+numerator3,denominator1)
        self.SimpleAnswer1 = answer1
        self.SimpleAnswer2 = answer2
        if answer1%answer2!=0:
            self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td>"
        else:
            self.answer_text = self.answer_text + "<td>&nbsp;"+str(answer1/answer2)+"&nbsp;</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator1)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;and&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator2))+str(numerator2)+"&nbsp;"*len(str(denominator2))+"</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'>&nbsp;do not have same denominator.</td></tr>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br>However, "+str(denominator2)+" is a factor of "+str(denominator1)+". To make both denominators equal multiply the smaller denominator with "+str(denominator1/denominator2)+"<br><br>"
        self.solution_text = self.solution_text + "Remember to multiply the numerator as well with the same number<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td>=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator1)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;+&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(numerator2)+" &times; "+str(denominator1/denominator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(denominator1/denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;+&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator3)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td>=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator1)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;+&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator2*denominator1/denominator2)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"       
        self.solution_text = self.solution_text + "<td>&nbsp;+&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator3)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td>=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(numerator1)+" + "+str(numerator2*denominator1/denominator2)+" + "+str(numerator3)+"&nbsp;</u><br>"+"&nbsp;"*(len(str(numerator1))+len(str(numerator2))+len(str(numerator3))+4)+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator1+numerator2*denominator1/denominator2+numerator3)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        if gcf!=1:
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>It requires further simplification:</td></tr></table>"            
            if self.SimpleAnswer2!=1:
                self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
                self.solution_text = self.solution_text + "<tr><td align='center'><u>"+"&nbsp;"*len(str(answer2))+"<del>"+str(numerator1+numerator2*denominator1/denominator2+numerator3)+"</del>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;"*len(str(answer2))+"</u><br>"+"&nbsp;"*len(str(answer1))+"<del>"+str(denominator1)+"</del>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
                self.solution_text = self.solution_text + "<td>&nbsp;= &nbsp;</td>"
                self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td></tr></table>"
                self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td>"
                self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td></tr></table>"                
            else:
                self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td>"
                self.solution_text = self.solution_text + "<tr><td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td><td><u>"+"&nbsp;"*len(str(answer2))+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td></tr></table>"   
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType5(self):
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator1 = random.choice([4,6,8,9,10,12])
        self.denominator2 = random.choice(Factors.Factors().find_factors(self.denominator1))
        while self.denominator2 == 1 or self.denominator2 == self.denominator1:
            self.denominator2 = random.choice(Factors.Factors().find_factors(self.denominator1))
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        self.numerator3 = randint(1,self.denominator2-1)
        
        self.problem = "Add and express the fraction in its simplest form:<br><br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator1))+"</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator2))+"</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator3)+"&nbsp;"*len(str(self.denominator2))+"</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td> &nbsp;= <td>"
        self.problem = self.problem + "</tr></table>"
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator1
        self.multiplier = self.denominator1/self.denominator2
        self.AnswerNumerator = self.numerator1 + self.numerator2*self.multiplier + self.numerator3*self.multiplier
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator,self.AnswerDenominator)
        self.answer1 = self.AnswerNumerator/gcf
        self.answer2 = self.AnswerDenominator/gcf
        self.answer = str(self.answer1)+"/"+str(self.answer2)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.numerator3,self.denominator1,self.denominator2,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,}            
    
    def ExplainType5(self,problem,answer1,answer2,numerator1,numerator2,numerator3,denominator1,denominator2,multiplier):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(numerator1+numerator2*multiplier+numerator3*multiplier,denominator1)
        self.SimpleAnswer1 = answer1
        self.SimpleAnswer2 = answer2
        if answer1%answer2!=0:
            self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td>"
        else:
            self.answer_text = self.answer_text + "<td>&nbsp;1&nbsp;</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator1)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;,&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator2))+str(numerator2)+"&nbsp;"*len(str(denominator2))+"</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;and&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator2))+str(numerator3)+"&nbsp;"*len(str(denominator2))+"</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'>&nbsp;do not have same denominator.</td></tr>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br>However, "+str(denominator2)+" is a factor of "+str(denominator1)+". To make all denominators equal multiply the smaller denominator with "+str(denominator1/denominator2)+"<br><br>"
        self.solution_text = self.solution_text + "Remember to multiply the numerator as well with the same number<br><br>"
        
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td>=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator1)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;+&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(numerator2)+" &times; "+str(denominator1/denominator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(denominator1/denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;+&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(numerator3)+" &times; "+str(denominator1/denominator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(denominator1/denominator2)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td>=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator1)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;+&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator2*denominator1/denominator2)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"       
        self.solution_text = self.solution_text + "<td>&nbsp;+&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator3*denominator1/denominator2)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"

        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td>=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(numerator1)+" + "+str(numerator2*denominator1/denominator2)+" + "+str(numerator3*multiplier)+"&nbsp;</u><br>"+"&nbsp;"*(len(str(numerator1))+len(str(numerator2))+len(str(numerator3))+4)+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator1))+str(numerator1+numerator2*multiplier+numerator3*multiplier)+"&nbsp;"*len(str(denominator1))+"</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"

        if gcf!=1:
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>It requires further simplification:</td></tr></table>"            
            if self.SimpleAnswer2!=1:
                self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
                self.solution_text = self.solution_text + "<tr><td align='center'><u>"+"&nbsp;"*len(str(answer2))+"<del>"+str(numerator1+numerator2*denominator1/denominator2+numerator3*denominator1/denominator2)+"</del>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;"*len(str(answer2))+"</u><br>"+"&nbsp;"*len(str(answer1))+"<del>"+str(denominator1)+"</del>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
                self.solution_text = self.solution_text + "<td>&nbsp;= &nbsp;</td>"
                self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td></tr></table>"
                self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td>"
                self.solution_text = self.solution_text + "<td align='center'><u>"+"&nbsp;"*len(str(self.SimpleAnswer2))+str(self.SimpleAnswer1)+"&nbsp;"*len(str(self.SimpleAnswer2))+"</u><br>"+"&nbsp;"*len(str(self.SimpleAnswer1))+str(self.SimpleAnswer2)+"</td></tr></table>"                
            else:
                self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td>"
                self.solution_text = self.solution_text + "<tr><td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is &nbsp;&nbsp;</td><td><u>"+"&nbsp;"*len(str(answer2))+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td></tr></table>"   
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
        self.CheckAnswerType = 4             
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = randint(3,12)
        self.numerator1 = randint(1,self.denominator-1)
        self.numerator2 = randint(1,self.denominator-1)
        
        self.problem = "Add:<br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td> &nbsp;= <td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator
        self.AnswerNumerator = self.numerator1 + self.numerator2
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        
        if self.answer1%self.answer2 == 0:
            self.answer = [self.answer1/self.answer2,0,0]
        else:
            self.answer = [0,self.answer1,self.answer2]
            
        self.wrongAnswers = []
        '''generating 3 wrong answers and making sure any of it is not equal to the correct answer'''
        self.WrongMixed = 0
        self.WrongDenominator = self.AnswerDenominator
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator+1,self.WrongDenominator])
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator+2,self.WrongDenominator])
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator-1,self.WrongDenominator])
                           
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ1"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)      

    def GenerateProblemTypeMCQ2(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.CheckAnswerType = 4
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = randint(3,12)
        self.numerator1 = randint(1,self.denominator-1)
        self.numerator2 = randint(1,self.denominator-1)
        
        self.problem = "Add and express the fraction in its simplest form:<br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td> &nbsp;= <td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator
        self.AnswerNumerator = self.numerator1 + self.numerator2
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator,self.AnswerDenominator)
        self.answer1 = self.AnswerNumerator/gcf
        self.answer2 = self.AnswerDenominator/gcf
        self.answer3 = 0
        self.answer = [self.answer3,self.answer1,self.answer2]     
        
        self.wrongAnswers = []
        self.WrongMixed = 0
        self.WrongDenominator = self.AnswerDenominator
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator+1,random.choice([self.AnswerDenominator,self.answer2])])
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator+2,random.choice([self.AnswerDenominator,self.answer2])])
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator-1,random.choice([self.AnswerDenominator,self.answer2])])
        if gcf!=1:
            self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator,self.AnswerDenominator])
                    
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ2"
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)      

    def GenerateProblemTypeMCQ3(self):
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.grade = 4
        self.CheckAnswerType = 4     
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator1 = random.choice([4,6,8,9,10,12])
        self.denominator2 = random.choice(Factors.Factors().find_factors(self.denominator1))
        while self.denominator2 == 1 or self.denominator2 == self.denominator1:
            self.denominator2 = random.choice(Factors.Factors().find_factors(self.denominator1))
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        
        self.problem = "Add and express the fraction in its simplest form:<br><br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator1))+"</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator2))+"</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td> &nbsp;= <td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator1
        self.AnswerNumerator = self.numerator1 + self.numerator2*self.denominator1/self.denominator2
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator,self.AnswerDenominator)
        self.answer1 = self.AnswerNumerator/gcf
        self.answer2 = self.AnswerDenominator/gcf
        self.answer3 = 0
        self.answer = [self.answer3,self.answer1,self.answer2]     
        
        self.wrongAnswers = []
        self.WrongMixed = 0
        self.WrongDenominator = self.AnswerDenominator
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator+1,random.choice([self.AnswerDenominator,self.answer2])])
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator+2,random.choice([self.AnswerDenominator,self.answer2])])
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator-1,random.choice([self.AnswerDenominator,self.answer2])])
        if gcf!=1:
            self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator,self.AnswerDenominator])
                    
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ3"
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,self.denominator2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ4(self):
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.grade = 4
        self.CheckAnswerType = 4     
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator1 = random.choice([4,6,8,9,10,12])
        self.denominator2 = random.choice(Factors.Factors().find_factors(self.denominator1))
        while self.denominator2 == 1 or self.denominator2 == self.denominator1:
            self.denominator2 = random.choice(Factors.Factors().find_factors(self.denominator1))
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        self.numerator3 = randint(1,self.denominator1-1)
        
        self.problem = "Add and express the fraction in its simplest form:<br><br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator1))+"</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator2))+"</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator3)+"&nbsp;"*len(str(self.denominator1))+"</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td> &nbsp;= <td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator1
        self.AnswerNumerator = self.numerator1 + self.numerator2*self.denominator1/self.denominator2 + self.numerator3
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator,self.AnswerDenominator)
        self.answer1 = self.AnswerNumerator/gcf
        self.answer2 = self.AnswerDenominator/gcf
        self.answer3 = 0
        self.answer = [self.answer3,self.answer1,self.answer2]     
        
        self.wrongAnswers = []
        self.WrongMixed = 0
        self.WrongDenominator = self.AnswerDenominator
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator+1,random.choice([self.AnswerDenominator,self.answer2])])
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator+2,random.choice([self.AnswerDenominator,self.answer2])])
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator-1,random.choice([self.AnswerDenominator,self.answer2])])
        if gcf!=1:
            self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator,self.AnswerDenominator])
                    
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ4"
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.numerator3,self.denominator1,self.denominator2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ5(self):
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.grade = 4
        self.CheckAnswerType = 4     
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator1 = random.choice([4,6,8,9,10,12])
        self.denominator2 = random.choice(Factors.Factors().find_factors(self.denominator1))
        while self.denominator2 == 1 or self.denominator2 == self.denominator1:
            self.denominator2 = random.choice(Factors.Factors().find_factors(self.denominator1))
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        self.numerator3 = randint(1,self.denominator2-1)
        
        self.problem = "Add and express the fraction in its simplest form:<br><br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator1))+"</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator2))+"</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td> &nbsp;+&nbsp; <td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator3)+"&nbsp;"*len(str(self.denominator2))+"</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td> &nbsp;= <td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator1
        self.multiplier = self.denominator1/self.denominator2
        self.AnswerNumerator = self.numerator1 + self.numerator2*self.multiplier + self.numerator3*self.multiplier
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator,self.AnswerDenominator)
        self.answer1 = self.AnswerNumerator/gcf
        self.answer2 = self.AnswerDenominator/gcf
        self.answer3 = 0
        self.answer = [self.answer3,self.answer1,self.answer2]     
        
        self.wrongAnswers = []
        self.WrongMixed = 0
        self.WrongDenominator = self.AnswerDenominator
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator+1,random.choice([self.AnswerDenominator,self.answer2])])
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator+2,random.choice([self.AnswerDenominator,self.answer2])])
        self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator-1,random.choice([self.AnswerDenominator,self.answer2])])
        if gcf!=1:
            self.wrongAnswers.append([self.WrongMixed,self.AnswerNumerator,self.AnswerDenominator])
                    
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ5"
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.numerator3,self.denominator1,self.denominator2,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)
           
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
        if CheckAnswerType == 1:
                AnswerNumerator = int(str(answer).partition("/")[0])
                AnswerDenominator = int(str(answer).partition("/")[2])
                try:
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
            
        elif CheckAnswerType == 2:
                AnswerNumerator = int(str(answer).partition("/")[0])
                AnswerDenominator = int(str(answer).partition("/")[2])
                try:
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
                    return (AnswerNumerator==InputNumerator and AnswerDenominator==InputDenominator)
                except ValueError:
                    return False

        elif CheckAnswerType == 3:
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
        elif CheckAnswerType == 4:
            answer = str(answer)
            InputAnswer = "["+str(InputAnswer).partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[2]+"]"
            if(answer==InputAnswer):
                return True
            else:
                return False