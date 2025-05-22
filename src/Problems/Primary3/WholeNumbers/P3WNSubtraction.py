'''
Created on Mar 03, 2013
Module: P3WNSubtraction
Generates the Subtraction problems for Primary 3

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
  

History:
  
'''
import random
from Problems import PersonName
from random import randint

class P3WNSubtraction:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1a","ProblemType1b","ProblemTypeMCQ1a","ProblemTypeMCQ1b",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4a","ProblemTypeMCQ4a","ProblemType4b","ProblemTypeMCQ4b",],
                            5:["ProblemType5","ProblemTypeMCQ5",],
                            6:["ProblemType6","ProblemTypeMCQ6",],
                            7:["ProblemType7a","ProblemType7b","ProblemType7c","ProblemTypeMCQ7a","ProblemTypeMCQ7b","ProblemTypeMCQ7c",],
                            8:["ProblemType8a","ProblemTypeMCQ8a","ProblemType8b","ProblemTypeMCQ8b",],
                            9:["ProblemType9","ProblemTypeMCQ9",],
                            10:["ProblemType10a","ProblemTypeMCQ10a","ProblemType10b","ProblemTypeMCQ10b",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1a(),self.GenerateProblemType1b(),self.GenerateProblemTypeMCQ1a(),self.GenerateProblemTypeMCQ1b(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4a(),self.GenerateProblemTypeMCQ4a(),self.GenerateProblemType4b(),self.GenerateProblemTypeMCQ4b(),],
                                    5:[self.GenerateProblemType5(),self.GenerateProblemTypeMCQ5(),],
                                    6:[self.GenerateProblemType6(),self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemType7a(),self.GenerateProblemTypeMCQ7a(),self.GenerateProblemType7b(),self.GenerateProblemTypeMCQ7b(),
                                       self.GenerateProblemType7c(),self.GenerateProblemTypeMCQ7c(),],
                                    8:[self.GenerateProblemType8a(),self.GenerateProblemTypeMCQ8a(),self.GenerateProblemType8b(),self.GenerateProblemTypeMCQ8b(),],
                                    9:[self.GenerateProblemType9(),self.GenerateProblemTypeMCQ9(),],
                                    10:[self.GenerateProblemType10a(),self.GenerateProblemTypeMCQ10a(),self.GenerateProblemType10b(),self.GenerateProblemTypeMCQ10b(),],
                                    }
        
        #Creating one more problem type so it creates a list and not a list of lists
        self.ProblemTypes = []
        
        for i in self.ProblemType.values():
            for k in i:
                self.ProblemTypes.append(k)
                
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(self.GenerateProblemType[1])
        else:
            if LastProblemID in self.ProblemTypes:
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if LastProblemID in v][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return random.choice(self.GenerateProblemType[NextProblemKey])
            else:
                return random.choice(self.GenerateProblemType[1])
        #return self.GenerateProblemType3()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1a":self.GenerateProblemType1a(),"ProblemType1b":self.GenerateProblemType1b(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4a":self.GenerateProblemType4a(),"ProblemType4b":self.GenerateProblemType4b(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7a":self.GenerateProblemType7a(),"ProblemType7b":self.GenerateProblemType7b(),"ProblemType7c":self.GenerateProblemType7c(),
                            "ProblemType8a":self.GenerateProblemType8a(),"ProblemType8b":self.GenerateProblemType8b(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10a":self.GenerateProblemType10a(),"ProblemType10b":self.GenerateProblemType10b(),
                            "ProblemTypeMCQ1a":self.GenerateProblemTypeMCQ1a(),"ProblemTypeMCQ1b":self.GenerateProblemTypeMCQ1b(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4a":self.GenerateProblemTypeMCQ4a(),"ProblemTypeMCQ4b":self.GenerateProblemTypeMCQ4b(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemTypeMCQ7a":self.GenerateProblemTypeMCQ7a(),"ProblemTypeMCQ7b":self.GenerateProblemTypeMCQ7b(),"ProblemTypeMCQ7c":self.GenerateProblemTypeMCQ7c(),
                            "ProblemTypeMCQ8a":self.GenerateProblemTypeMCQ8a(),"ProblemTypeMCQ8b":self.GenerateProblemTypeMCQ8b(),
                            "ProblemTypeMCQ9":self.GenerateProblemTypeMCQ9(),
                            "ProblemTypeMCQ10a":self.GenerateProblemTypeMCQ10a(),"ProblemTypeMCQ10b":self.GenerateProblemTypeMCQ10b(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1a(self):       
        '''e.g.:
        Find the sum of 8792 and 123.'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.flag = randint(1,10)
        
        if self.flag < 5:
            self.number1 = randint(1000,8888)
            self.number2 = randint(100,888)
        elif self.flag >=5 and self.flag<9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(50,1000)
            self.number2 = randint(50,1000)
        
        self.sum = self.number1 + self.number2
        
        self.problem1 = "Find the difference between %d and %d."%(self.sum,self.number1)
        self.problem2 = "What is the difference between %d and %d?"%(self.sum,self.number1)
        self.problem3 = "What is %d &minus; %d?"%(self.sum,self.number1)
        self.problem4 = "The difference between %d and %d is _____."%(self.sum,self.number1)
        self.problem5 = "%d &minus; %d = ?"%(self.sum,self.number1)
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])
        
        self.answer = self.number2
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.sum,self.number1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def GenerateProblemType1b(self):       
        '''e.g.:
        Add.
         8792
        + 123
        ------'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''first digit can't be zero'''
        self.digits1 = [randint(1,7)]
        self.number1 = str(self.digits1[0])        
        for i in range(3):
            self.digits1.append(randint(0,9))         
            self.number1 = self.number1 + str(self.digits1[i+1])

        self.digits2 = [randint(1,8-self.digits1[0])]        
        self.number2 = str(self.digits2[0])        
        for i in range(randint(2,3)):
            self.digits2.append(randint(0,9)) 
            self.number2 = self.number2 + str(self.digits2[i+1])
            
        self.sum = str(int(self.number1) + int(self.number2))
        
        self.SumDigits = []
        for i in range(len(self.sum)):
            self.SumDigits.append(self.sum[i:i+1])

        self.problem = "Subtract.<br><br><table><tr><td></td>"
        for i in range(len(self.SumDigits)):
            self.problem = self.problem + "<td>"+str(self.SumDigits[i])+"</td>"
        self.problem = self.problem + "</tr><tr><td style='text-align:right'>&minus;</td>"

        for i in range(len(self.digits1)):
            self.problem = self.problem + "<td>"+str(self.digits1[i])+"</td>"
        
        self.problem = self.problem + "</tr>"
        self.problem = self.problem + "<tr><td colspan=5 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line.png' /></td></tr>"
        self.problem = self.problem + "</table>"
        
        self.answer = self.number2
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.sum,self.number1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType1(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        self.solution_text =  self.SubtractionExplanation(number1, number2)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, %d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d</font>"%(int(number1),int(number2),int(answer))

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        The sum of two numbers is 4567. If one of the numbers is 2345, what is the other number?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.flag = randint(1,10)
        
        if self.flag < 5:
            self.number1 = randint(1000,8888)
            self.number2 = randint(100,888)
        elif self.flag >=5 and self.flag<9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(50,1000)
            self.number2 = randint(50,1000)
            while self.number1 == self.number2:
                self.number2 = randint(50,100)
        
        self.sum = self.number1 + self.number2
        
        self.flag1 = randint(1,3)
        
        if self.flag1 == 1:
            self.problem = "The sum of two numbers is %d. If one of the numbers is %d, what is the other number?"%(self.sum,self.number1)
        elif self.flag1 == 2:
            if self.number1 < self.number2:
                self.number1,self.number2 = self.number2,self.number1
            self.problem = "The sum of two numbers is %d. If the bigger number is %d, what is the smaller number?"%(self.sum,self.number1)
        elif self.flag1 == 3:
            if self.number1 > self.number2:
                self.number1,self.number2 = self.number2,self.number1
            self.problem = "The sum of two numbers is %d. If the smaller number is %d, what is the bigger number?"%(self.sum,self.number1)
        
        self.answer = self.number2
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.sum,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType2(self,problem,answer,total,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        if number1>number2:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        elif number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(total)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.SubtractionExplanation(total, number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>The other number is: %s</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
            Find the missing number.
              1 2 3 4
            + 2 3 4 _
            ---------
              3 5 7 8'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''first digit can't be zero'''
        self.digits1 = [randint(1,7)]
        self.number1 = str(self.digits1[0])        
        for i in range(3):
            self.digits1.append(randint(0,9))         
            self.number1 = self.number1 + str(self.digits1[i+1])

        self.digits2 = [randint(1,8-self.digits1[0])]        
        self.number2 = str(self.digits2[0])        
        for i in range(randint(2,3)):
            self.digits2.append(randint(0,9)) 
            self.number2 = self.number2 + str(self.digits2[i+1])
        
        self.sum = str(int(self.number1) + int(self.number2))
        
        self.SumDigits = []
        for i in range(len(self.sum)):
            self.SumDigits.append(self.sum[i:i+1])

        self.digits1 = self.SumDigits
        
        self.problem = "Find the missing number.<br><br><table><tr><td></td>"
        
        self.flag = randint(1,3)
        
        if self.flag == 1:
            self.MissingDigit = randint(0,len(self.digits1)-1) 
            for i in range(len(self.digits1)):
                if i == self.MissingDigit:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
                    self.answer = self.digits1[i]
                else:
                    self.problem = self.problem + "<td>"+str(self.digits1[i])+"</td>"
        else:
            for i in range(len(self.digits1)):
                self.problem = self.problem + "<td>"+str(self.digits1[i])+"</td>"
            
        self.problem = self.problem + "</tr><tr><td>&minus;</td>"
        
        if len(self.digits2) == 3:
            self.problem = self.problem +"<td></td>"
        
        if self.flag == 2:
            self.MissingDigit = randint(0,len(self.digits2)-1) 
            for i in range(len(self.digits2)):
                if i == self.MissingDigit:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
                    self.answer = self.digits2[i]
                else:
                    self.problem = self.problem + "<td>"+str(self.digits2[i])+"</td>"
        else:
            for i in range(len(self.digits2)):
                self.problem = self.problem + "<td>"+str(self.digits2[i])+"</td>"
        
        self.problem = self.problem + "</tr>"
        self.problem = self.problem + "<tr><td colspan=5 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line.png' /></td></tr>"       

        self.problem = self.problem + "<tr><td></td>"
        
        self.difference = self.number1
                
        if self.flag == 3:
            self.MissingDigit = randint(0,len(self.digits1)-1) 
            for i in range(len(self.digits1)):
                if i == self.MissingDigit:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
                    self.answer = self.difference[i:i+1]
                else:
                    self.problem = self.problem + "<td>"+str(self.difference)[i:i+1]+"</td>"
        else:
            for i in range(len(self.digits1)):
                self.problem = self.problem + "<td>"+str(self.difference)[i:i+1]+"</td>"            

        self.problem = self.problem + "</tr></table>"
                   
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.flag,self.sum,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType3(self,problem,answer,flag,total,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        if int(number2)>int(number1):
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        elif int(number2)==int(number1):
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'

        #end of model

        if flag==1:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(int(number2),int(number1))
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(self.color1,self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
            self.solution_text = self.solution_text + "</table><br><br>"
            self.solution_text = self.solution_text + self.AdditionExplanation(int(number1),int(number2))
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>The missing digit is: %s</font>"%(answer)
        elif flag==2:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td><td>%d</td></tr>"%(int(number1))
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(self.color1,self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(int(total))
            self.solution_text = self.solution_text + "</table><br><br>"
            self.solution_text = self.solution_text + self.SubtractionExplanation(int(total),int(number1))
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>The missing digit is: %s</font>"%(answer)
        else:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>?</td></tr>"%(int(number2))
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(self.color1,self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(int(total))
            self.solution_text = self.solution_text + "</table><br><br>"
            self.solution_text = self.solution_text + self.SubtractionExplanation(int(total),int(number2))
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>The missing digit is: %s</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4a(self):       
        '''e.g.:
        <An amusement park> received 1489 <visitors> on <Saturday> and 2489 <visitors> on <Sunday>. How many more <visitors> did it receive on <Sunday> than on <Saturday>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            while self.number1 == self.number2:
                self.number2 = randint(100,999)
        
        if self.number1 > self.number2:
            self.number1,self.number2 = self.number2,self.number1
        
        self.items = [['An amusement park','visitors','Saturday','Sunday'],
                      ['A water park','visitors','Saturday','Sunday'],
                      ['A theme park','visitors','Saturday','Sunday'],
                      ['An animal safari park','visitors','Saturday','Sunday'],
                      ['A bird park','visitors','Saturday','Sunday'],
                      ['A zoo','visitors','Saturday','Sunday'],
                      ['A science museum','visitors','Saturday','Sunday'],
                      ['A shopping mall','shoppers','Saturday','Sunday'],
                      ['A cinema','moviegoers','Saturday','Sunday'],
                      ['A carnival','visitors','Saturday','Sunday']]
        self.days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        
        self.item = random.choice(self.items)
        
        self.Day1Index = randint(0,6)
        if self.Day1Index == 6:
            self.Day2Index = 0
        else:
            self.Day2Index = self.Day1Index + 1 
        
        problemFlag = randint(1,2)
        if problemFlag==1:
            self.problem = "%s received %d %s on %s and %d %s on %s. How many more %s did it receive on %s than on %s?"%(self.item[0],self.number1,self.item[1],self.days[self.Day1Index],
                                                                                                                              self.number2,self.item[1],self.days[self.Day2Index],
                                                                                                                              self.item[1],self.days[self.Day2Index],self.days[self.Day1Index])        
        else:
            self.problem = "%s received %d %s on %s and %d %s on %s. What is the difference between the number of %s it received on the two days?"%(self.item[0],self.number1,self.item[1],self.days[self.Day1Index],
                                                                                                                              self.number2,self.item[1],self.days[self.Day2Index],
                                                                                                                              self.item[1])
        #self.problem = random.choice([self.problem1,self.problem2])
        self.answer = self.number2 - self.number1
        
        self.unit = self.item[1]
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,problemFlag,self.number2,self.number1,self.days[self.Day2Index],self.days[self.Day1Index],self.item[1],'on','days',self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit}

    def GenerateProblemType4b(self):       
        '''e.g.:
        <An art museum> received 1489 <visitors> in <March> and 2489 <visitors> in <April>. How many more <visitors> did it receive in <April> than in <March>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            while self.number1 == self.number2:
                self.number2 = randint(100,999)
        
        if self.number1 > self.number2:
            self.number1,self.number2 = self.number2,self.number1
            
        self.items = [['An art museum','visitors','March','April'],['A vegetable farm','visitors','March','April'],['A strawberry farm','visitors','March','April'],['An animal farm','visitors','March','April'],['A grocery store','shoppers','March','April'],['A minimart','customers','March','April'],['A hotel','guests','March','April'],['A restaurant','guests','March','April'],['An airport','passengers','March','April'],['A post office','customers','March','April']]
        self.months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        
        self.item = random.choice(self.items)
        
        self.Month1Index = randint(0,10)
        self.Month2Index = self.Month1Index + 1 

        problemFlag = randint(1,2)
        if problemFlag==1:
            self.problem = "%s received %d %s in %s and %d %s in %s. How many more %s did it receive in %s than in %s?"%(self.item[0],self.number1,self.item[1],self.months[self.Month1Index],
                                                                                                                        self.number2,self.item[1],self.months[self.Month2Index],
                                                                                                                        self.item[1],self.months[self.Month2Index],self.months[self.Month1Index])
        else:
            self.problem = "%s received %d %s in %s and %d %s in %s. What is the difference between the number of %s it received in the two months?"%(self.item[0],self.number1,self.item[1],self.months[self.Month1Index],
                                                                                                                        self.number2,self.item[1],self.months[self.Month2Index],
                                                                                                                        self.item[1])
        
        #self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.number2 - self.number1
        
        self.unit = self.item[1]
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,problemFlag,self.number2,self.number1,self.months[self.Month2Index],self.months[self.Month1Index],self.item[1],'in','months',self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit}

    def ExplainType4(self,problem,answer,problemFlag,number2,number1,DayMonth2,DayMonth1,item1,inOrOn,daysOrMonths,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        if number1>answer:
            firstBrace = 'medium'
            secondBrace = 'small'
        else:
            firstBrace = 'small'
            secondBrace = 'medium'
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td></tr>"%(DayMonth1,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(DayMonth2,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_large.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.SubtractionExplanation(number2,number1)
        if problemFlag==1:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>It received %d more %s %s %s than %s %s.</font>"%(answer,item1,inOrOn,DayMonth2,inOrOn,DayMonth1)
        else:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>The difference between the number of %s it received %s the two %s is %d.</font>"%(item1,inOrOn,daysOrMonths,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        <A primary school has> 2658 <pupils>. <A secondary school has> 1239 <pupils>. What is the difference between the number of <pupils in the two schools>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            while self.number1 == self.number2:
                self.number2 = randint(100,999)
            
        self.items = [['A primary school has','pupils','A secondary school has','pupils in the two schools','pupils','primary school','secondary school'],
                      ['A town has','residents','Its neighbouring town has','residents in the two towns','residents','town 1','town 2'],
                      ['A clothes company employs','workers','A shoes company employs','workers that the two companies employ','workers','clothes company','shoes company'],
                      ['A fish tank has','fishes','Another fish tank has','fishes in the two fish tanks','fishes','fish tank 1','fish tank 2'],
                      ['A national park has','trees','Another national park has','trees in the two national parks','trees','park 1','park 2'],
                      ['A wildlife sanctuary keeps','animals','Another wildlife sanctuary keeps','animals that the two wildlife sanctuaries keep','animals','sanctuary 1','sanctuary 2'],
                      ['A science college enrols','students','A management college enrols','students that the two colleges enrol','students','science college','management college'],
                      ['A school library carries','books','A public library carries','books that the two libraries carry','books','school library','public library'],
                      ['Warehouse A can store','computers','Warehouse B can store','computers that the two warehouses can store','computers','Warehouse A','Warehouse B'],
                      ['A bookstore in a school carries','pens','A bookstore in a shopping centre carries','pens that the two bookstores carry','pens','bookstore 1','bookstore 2'],
                      ['A toys shop in a mall sold','toys','Another toys shop in the mall sold','toys sold by the two toys shops','toys','toys shop 1','toys shop 2'],
                      ['Grocery Store A sold','cans of milk','Grocery Store B sold','cans of milk sold by the two grocery stores','cans','Store A','Store B'],
                      ['Farmer A sold','eggs','Farmer B sold','eggs sold by the two farmers','eggs','Farmer A','Farmer B'],
                      ['An art museum has','items on display','A science museum','items that the two museums have on display','items','art museum','science museum'],
                      ['A movie rental store carries','movie CDs','Another movie rental store carries','movie CDs that the two stores carry','movie CDs','store 1','store 2'],
                      ['Bakery A sold','muffins','Bakery B sold','muffins sold by the two bakeries','muffins','Bakery A','Bakery B'],
                      ['Ship A has','passengers','Ship B has','passengers on the two ships','passengers','Ship A','Ship B']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %d %s. %s %d %s. What is the difference between the number of %s?"%(self.item[0],self.number1,self.item[1],
                                                                              self.item[2],self.number2,self.item[1],
                                                                              self.item[3])
        
        self.answer = abs(self.number1 - self.number2)
        
        self.unit = self.item[4]
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.item[3],self.item[5],self.item[6],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit}

    def ExplainType5(self,problem,answer,number1,number2,item3,item5,item6,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        if number1<number2:
            if number1>=answer:
                firstBrace = 'medium'
                secondBrace = 'small'
            else:
                firstBrace = 'small'
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>?</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td></tr>"%(item5,self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(item6,self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(number2)
            self.solution_text = self.solution_text + "</table><br><br>"
        else:
            if number2>=answer:
                firstBrace = 'medium'
                secondBrace = 'small'
            else:
                firstBrace = 'small'
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(item5,self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td></tr>"%(item6,self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>?</td></tr>"%(number2)
            self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.SubtractionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>The difference between the number of %s is %d.</font>"%(item3,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        [Person.Unclename] <had> $1239 <in his savings>. He <withdrew> $123 <from his savings>. How much money <had he left in his savings?>'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.name = random.choice(PersonName.UncleName)
            
        self.items = [['had','in his savings','withdrew','from his savings','had he left in his savings','He had',' left in his savings','withdrew','left'],
                      ['earned','at his job','spent','of his earnings and saved the rest','did he save','He saved','','spent','saved'],
                      ['won','in a game','gave','of his winnings to his daughter and kept the rest for himself','did he keep for himself','He kept',' for himself','daughter','for himself'],
                      ['had','with him','spent','to buy furniture for his house','had he left','He had',' left','spent','left'],
                      ['received','as a bonus','used','to buy gifts for his family and saved the rest','did he save','He saved','','bought gifts','saved'],
                      ['had','in his wallet','spent','on shopping','did he have left in his wallet','He had',' left in his wallet','spent','left'],
                      ['had','with him','used','to buy books','did he have left','He had',' left','bought books','left'],
                      ['received a donation of','for his library','used','of it to buy books','did he have left','He had',' left','bought books','left'],
                      ['had','at first','spent','on air tickets','did he have left','He had',' left','air tickets','left'],
                      ['won','in a lottery','used','to buy gifts for his family','did he have left','He had',' left','bought gifts','left']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %s $%d %s. He %s $%d %s. How much money %s?"%(self.name,self.item[0],self.sum,self.item[1],
                                                                        self.item[2],self.number1,self.item[3],self.item[4])
        
        self.answer = self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.sum,self.number1,self.item[5],self.item[6],self.item[7],self.item[8])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def ExplainType6(self,problem,answer,total,number1,item5,item6,item7,item8):
        self.answer_text = "<br>The correct answer is:<br>$%s"%(str(answer))

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        if number1>answer:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        elif number1==answer:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td><td>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em'>%s</font></td></tr>"%(self.color1,item7,self.color2,item8)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%d</td></tr>"%(total)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.SubtractionExplanation(total,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s $%d%s.</font>"%(item5,answer,item6)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7a(self):       
        '''e.g.:
        [Person.Girlname] <had> 5224 <beads> and <marbles>. If she <had> 2020 <beads>, find the number of <marbles> she <had>.'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.name = random.choice(PersonName.GirlName)
            
        self.items = [['had','beads','marbles','had'],['collected','stamps','stickers','collected'],
                      ['had','rubberbands','buttons','had'],['bought','buttons','rubberbands','bought'],
                      ['won','points','stars','won'],['had','paper clips','push pins','had'],
                      ['bought','stickers','stamps','bought'],['collected','flags','stamps','collected'],
                      ['got','marbles','magnets','got'],['had','tacks','ice-cream sticks','had']]


        self.item = random.choice(self.items)
               
        self.problem = "%s %s %d %s and %s. If she %s %d %s, find the number of %s she %s."%(self.name,self.item[0],self.sum,self.item[1],
                                                                                             self.item[2],self.item[0],self.number1,self.item[1],
                                                                                             self.item[2],self.item[0]) 
                
        self.answer = self.number2
        
        self.unit = self.item[2]
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.sum,self.number1,'She',self.item[0],self.item[2],self.item[1],self.item[2],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def GenerateProblemType7b(self):       
        '''e.g.:
        [Person.Girlname 1] and [Person.Girlname 2] had 5224 <beads> altogether. If [Person.Girlname 1] had 2023 <beads>, how many <beads> had [Person.Girlname 2]?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.names = random.sample(PersonName.GirlName,2)
            
        self.items = ['beads','stamps','rubberbands','buttons','pushpins','safety pins','stickers','flags','pins','tacks']


        self.item = random.choice(self.items)
               
        self.problem = "%s and %s had %d %s altogether. If %s had %d %s, how many %s had %s?"%(self.names[0],self.names[1],self.sum,self.item,
                                                                                               self.names[0],self.number1,self.item,self.item,self.names[1]) 
                
        self.answer = self.number2
        
        self.unit = self.item
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.sum,self.number1,self.names[1],'had',self.item,self.names[0],self.names[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def GenerateProblemType7c(self):       
        '''e.g.:
        [Person.Boyname 1] and [Person.Boyname 2] collected 5224 <marbles> altogether. If [Person.Boyname 1] collected 2023 <marbles>, how many <marbles> did [Person.Boyname 2] collect?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.names = random.sample(PersonName.BoyName,2)
            
        self.items = ['marbles','stamps','stickers','flags','rubberbands','coins','keyrings','darts','animal cards','cards']


        self.item = random.choice(self.items)
               
        self.problem = "%s and %s collected %d %s altogether. If %s collected %d %s, how many %s did %s collect?"%(self.names[0],self.names[1],self.sum,self.item,
                                                                                               self.names[0],self.number1,self.item,self.item,self.names[1]) 
                
        self.answer = self.number2
        
        self.unit = self.item
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.sum,self.number1,self.names[1],'collected',self.item,self.names[0],self.names[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def ExplainType7(self,problem,answer,total,number1,name,item0,item2,itemName1,itemName2,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        if number1>answer:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        elif number1==answer:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em'>%s</font></td></tr>"%(self.color1,itemName1,self.color2,itemName2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(total)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.SubtractionExplanation(total,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s %s %d %s.</font>"%(name,item0,answer,item2)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8a(self):       
        '''e.g.:
        <A grocery store sold> 6904 <chicken eggs> and <duck eggs>. If <it sold> 2045 <chicken eggs>, how many <duck eggs> did <it sell>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.items = [['A grocery store sold','chicken eggs','duck eggs','it sold','it sell','It sold'],
                      ['A fruit vendor had','pears','mangoes','he had','he have','He had'],
                      ['A farmer had','hens','ducks','he had','he have','He had'],
                      ['A phone shop sold','SIM cards','calling cards','it sold','it sell','It sold'],
                      ['A post office sold','envelopes','stamps','it sold','it sell','It sold'],
                      ['A supermarket had','bags of flour','bags of sugar','it had','it have','It had'],
                      ['An amusement park received','children','adults','it received','it receive','It received'],
                      ['A school had','boys','girls','it had','it have','It had'],
                      ['A library carried','books','DVDs','it carried','it carry','It carried'],
                      ['A baker baked','cupcakes','muffins','he baked','he bake','He baked'],
                      ['A hawker centre sold','plates of rice','bowls of soup','it sold','it sell','It sold']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %d %s and %s altogether. If %s %d %s, how many %s did %s?"%(self.item[0],self.sum,self.item[1],self.item[2],self.item[3],self.number1,
                                                                            self.item[1],self.item[2],self.item[4]) 
                
        self.answer = self.number2
        
        self.unit = self.item[2]
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.sum,self.number1,self.item[2],self.item[5],self.item[1],self.item[2],1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def GenerateProblemType8b(self):       
        '''e.g.:
        <A grocery store sold> 3904 <chicken eggs> and 2102 <duck eggs>. How many more <chicken eggs> than <duck eggs> did <it sell>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.items = [['A grocery store sold','chicken eggs','duck eggs','it sell','It sold','more chicken eggs than duck eggs'],
                      ['A fruit vendor had','pears','mangoes','he have','He had','more pears than mangoes'],
                      ['A farmer had','hens','ducks','he have','He had','more hens than ducks'],
                      ['A phone shop sold','SIM cards','calling cards','it sell','It sold','more SIM cards than phone cards'],
                      ['A post office sold','envelopes','stamps','it sell','It sold','more envelopes than stamps'],
                      ['A supermarket had','bags of flour','packets of sugar','it have','It had','more bags of flour than packets of sugar'],
                      ['An amusement park received','children','adults','it receive','It received','more children than adults'],
                      ['A school had','boys','girls','it have','It had','more boys than girls'],
                      ['A library carried','books','DVDs','it carry','It carried','more books than DVDs'],
                      ['A baker baked','cupcakes','muffins','he bake','He baked','more cupcakes than muffins'],
                      ['A hawker centre sold','plates of rice','bowls of soup','it sell','It sold','more plates of rice than bowls of soup']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %d %s and %d %s. How many more %s than %s did %s?"%(self.item[0],self.sum,self.item[1],self.number1,self.item[2],
                                                                               self.item[1],self.item[2],self.item[3]) 
                
        self.answer = self.number2
        
        self.unit = ""
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.sum,self.number1,self.item[5],self.item[4],self.item[1],self.item[2],2,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def ExplainType8(self,problem,answer,total,number1,item2,item5,thing1,thing2,flag,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        if flag==1:
            if number1>answer:
                firstBrace = 'large'
                secondBrace = 'medium'
                totalBrace = 'large1medium1'
            elif number1==answer:
                firstBrace = 'medium'
                secondBrace = 'medium'
                totalBrace = 'medium2'
            else:
                firstBrace = 'medium'
                secondBrace = 'large'
                totalBrace = 'large1medium1'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>?</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em'>%s</font></td></tr>"%(self.color1,thing1,self.color2,thing2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(total)
            self.solution_text = self.solution_text + "</table><br><br>"
        else:
            if number1>=answer:
                firstBrace = 'medium'
                secondBrace = 'small'
            else:
                firstBrace = 'small'
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(total)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(thing1,self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td></tr>"%(thing2,self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>?</td></tr>"%(number1)
            self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.SubtractionExplanation(total,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s %d %s.</font>"%(item5,answer,item2)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        There were 8467 <birds in a village>. 1239 <birds migrated out of the village>. How many <birds were left in the village>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.items1 = [['birds in a village','birds migrated out of the village','birds were left in the village','birds','migrated','left'],
                       ['children who took a maths test','children got 5 stars on the maths test','children did not get 5 stars on the maths test','children','5 stars','others'],
                       ['workers in a factory','workers left the factory','workers were left in the factory','workers','left the factory','still in the factory'],
                       ['people on a beach','people left the beach','people were left on the beach','people','left the beach','still on the beach'],
                       ['spectators in a stadium','spectators left the stadium','spectators were left in the stadium','spectators','left the stadium','still in the stadium'],
                       ['passengers at a railway station','passengers boarded a train','passengers were left at the railway station','passengers','boarded the train','left at the station'],
                       ['beads at first','beads were used to make a necklace','beads were left','beads','necklace','left'],
                       ['plants at a nursery','plants were sold','plants were left','plants','sold','left'],
                       ['loaves of bread made by a bakery','loaves of bread were sold','loaves of bread were left unsold','loaves of bread','sold','left'],
                       ['oranges on a farm','oranges were picked','oranges on the farm were not picked','oranges','picked','not picked'],
                       ['people in a village','people moved from the village to the town','people were left in the village','people','moved to town','left in the village'],
                       ['children in the school hall','left the school hall for their classrooms','children were left in the school hall','children','left for classrooms','left in school hall'],
                       ['travelers at the airport','travelers left the airport','travelers were left at the airport','travelers','left the airport','still at the airport'],
                       ['passengers on the train','passengers got off the train','passengers were left on the train','passengers','got off the train','left on the train']]

        self.item1 = random.choice(self.items1)

        self.items2 = [['birds living in a village migrated away from the village','birds were left in the village','birds','migrated','left'],
                       ['children who took a test got 5 stars on the test','children did not get 5 stars on the test','children','5 stars','others'],
                       ['workers who work in a factory left the factory','workers were left in the factory','workers','left the factory','still in the factory'],
                       ['people who were on a beach left the beach','people were left on the beach','people','left the beach','still on the beach'],
                       ['spectators who were watching a soccer game in a stadium left the stadium','spectators were left in the stadium','spectators','left the stadium','still in the stadium'],
                       ['passengers who were waiting at a railway station boarded a train','passengers were left at the railway station','passengers','boarded the train','left at the station'],
                       ['beads were used to make a necklace','beads were left','beads','necklace','left'],
                       ['plants at a nursery were sold','plants were left','plants','sold','left'],
                       ['loaves of bread made by a bakery were sold','loaves of bread were left unsold','loaves of bread','loaves of bread','sold','left'],
                       ['mangoes on a farm were picked','mangoes on the farm were not picked','mangoes','picked','not picked'],
                       ['people who lived in a village moved to the town','people were left in the village','people','moved to town','left in the village'],
                       ['children who had assembled in the school hall left for their classrooms','children were left in the school hall','children','left for classrooms','left in school hall'],
                       ['travelers waiting at the airport for their flights took off','travelers were left at the airport','travelers','left the airport','still at the airport'],
                       ['passengers on a train got off the train','passengers were left on the train','passengers','got off the train','left on the train']]
        
        self.item2 = random.choice(self.items2)
               
        problemFlag = randint(1,2)
        if problemFlag==1:
            self.problem = "There were %d %s. %d %s. How many %s?"%(self.sum,self.item1[0],self.number1,self.item1[1],self.item1[2])
            tempItem1 = self.item1[2]
            tempItem2 = self.item1[3]
            tempItem3 = self.item1[4]
            tempItem4 = self.item1[5]
        else:
            self.problem = "%d out of %d %s. How many %s?"%(self.number1,self.sum,self.item2[0],self.item2[1])
            tempItem1 = self.item2[1] 
            tempItem2 = self.item2[2]
            tempItem3 = self.item2[3]
            tempItem4 = self.item2[4]
        
        #self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.number2
        
        self.unit = ""
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.sum,self.number1,tempItem1,tempItem2,tempItem3,tempItem4,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def ExplainType9(self,problem,answer,total,number1,item,item2,item3,item4,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]        
        if number1>answer:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        elif number1==answer:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td></tr>"%(item2,self.color1,item3,self.color2,item4)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(total)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.SubtractionExplanation(total,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d %s.</font>"%(answer,item)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType10a(self):       
        '''e.g.:
        [Person.Unclename] bought a <computer> and a <printer> for $1750. If the <computer> cost $1000, what was the cost of the <printer>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
            
        self.name = random.choice(PersonName.UncleName)
                    
        self.items = [['computer','printer',randint(500,1500),randint(100,400)],['sofa set','coffee table',randint(1000,3000),randint(200,800)],
                      ['bed frame','mattress',randint(500,1000),randint(500,2000)],['TV set','TV console',randint(500,1500),randint(500,1500)],
                      ['dining table set','recliner sofa',randint(500,2000),randint(500,2000)],['camera','printer',randint(500,1500),randint(100,400)],
                      ['book shelf','table',randint(500,1000),randint(100,1000)],['DVD player','couch',randint(500,2000),randint(500,2000)],
                      ['laptop','smart phone',randint(700,2000),randint(200,800)]]

        self.item = random.choice(self.items)

        self.number1 = self.item[2]
        self.number2 = self.item[3]
        
        self.sum = self.number1 + self.number2
               
        self.problem = "%s bought a %s and a %s for $%d. If the %s cost $%d, what was the cost of the %s?"%(self.name,self.item[0],self.item[1],self.sum,
                                                                                                            self.item[0],self.number1,self.item[1]) 
        self.answer = self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10a(self.problem,self.answer,self.sum,self.number1,self.item[0],self.item[1],self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def ExplainType10a(self,problem,answer,total,number1,item0,item1,unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s"%(unit,str(answer))

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]        
        if number1>answer:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        elif number1==answer:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td><td>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.75em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.75em'>%s</font></td></tr>"%(self.color1,item0,self.color2,item1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%d</td></tr>"%(total)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.SubtractionExplanation(total,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>The cost of the %s was $%d.</font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType10b(self):       
        '''e.g.:
        [Person.Unclename] bought a <computer> for $1250 and a <printer> for $750. How much more did he pay for the <computer> than for the <printer>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
            
        self.name = random.choice(PersonName.UncleName)
                    
        self.items = [['computer','printer',randint(500,1500),randint(100,400)],['sofa set','coffee table',randint(1000,3000),randint(200,800)],
                      ['bed frame','mattress',randint(500,1000),randint(500,2000)],['TV set','TV console',randint(500,1500),randint(500,1500)],
                      ['dining table set','recliner sofa',randint(500,2000),randint(500,2000)],['camera','printer',randint(500,1500),randint(100,400)],
                      ['book shelf','table',randint(500,1000),randint(100,1000)],['DVD player','couch',randint(500,2000),randint(500,2000)],
                      ['laptop','smart phone',randint(700,2000),randint(200,800)]]

        self.item = random.choice(self.items)

        self.number1 = self.item[2]
        self.number2 = self.item[3]
        
        if self.number1 < self.number2:
            self.number1,self.number2 = self.number2,self.number1
               
        self.problem = "%s bought a %s for $%d and a %s for $%d. How much more did he pay for the %s than for the %s?"%(self.name,self.item[0],self.number1,
                                                                                                                        self.item[1],self.number2,self.item[0],self.item[1]) 
        self.answer = self.number1 - self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10b(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[1],self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def ExplainType10b(self,problem,answer,number1,number2,item0,item1,unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s"%(unit,str(answer))

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]        
        if number2>=answer:
            firstBrace = 'medium'
            secondBrace = 'small'
        else:
            firstBrace = 'small'
            secondBrace = 'medium'
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(item0,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td></tr>"%(item1,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td><td>?</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.SubtractionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>He paid $%d more for the %s than for the %s.</font>"%(answer,item0,item1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore,CheckAnswerType):
        
        '''Removing correct answers from the wrongAnswers list'''
        wrongAnswers = filter(self.removeCorrectAnswer,wrongAnswers)
        
        self.answer1=''
        self.answer2=''
        self.answer3=''
        self.answer4=''
                             
        '''Randomly selecting 3 wrong answers and adding the correct answer as well'''
        try:
            wrongAnswers = random.sample(wrongAnswers,3)
        except ValueError:
            pass
            
        wrongAnswers.append(answer)
        random.shuffle(wrongAnswers)
        try:
            self.answer1 = str(wrongAnswers[0])
            self.answer2 = str(wrongAnswers[1])
            self.answer3 = str(wrongAnswers[2])
            self.answer4 = str(wrongAnswers[3])        
        except IndexError:
            pass
        try:
            self.value1 = self.answer1
            self.value2 = self.answer2
            self.value3 = self.answer3
            self.value4 = self.answer4
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'answer4':self.answer4,'value1':self.value1,'value2':self.value2
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type,
                'grade':3,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}
        
    def GenerateProblemTypeMCQ1a(self):
        '''e.g.:
        Find the sum of 8792 and 123.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1a"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag < 5:
            self.number1 = randint(1000,8888)
            self.number2 = randint(100,888)
        elif self.flag >=5 and self.flag<9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(50,1000)
            self.number2 = randint(50,1000)
        
        self.sum = self.number1 + self.number2
        
        self.problem1 = "Find the difference between %d and %d."%(self.sum,self.number1)
        self.problem2 = "What is the difference between %d and %d?"%(self.sum,self.number1)
        self.problem3 = "What is %d &minus; %d?"%(self.sum,self.number1)
        self.problem4 = "The difference between %d and %d is _____."%(self.sum,self.number1)
        self.problem5 = "%d &minus; %d = ?"%(self.sum,self.number1)
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])
        
        self.answer = self.number2
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+100]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+100]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+100]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+100]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.sum,self.number1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ1b(self):
        '''e.g.:
        Add.
         8792
        + 123
        ------'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1b"
        self.CheckAnswerType = 1

        
        '''first digit can't be zero'''
        self.digits1 = [randint(1,7)]
        self.number1 = str(self.digits1[0])        
        for i in range(3):
            self.digits1.append(randint(0,9))         
            self.number1 = self.number1 + str(self.digits1[i+1])

        self.digits2 = [randint(1,8-self.digits1[0])]        
        self.number2 = str(self.digits2[0])        
        for i in range(randint(2,3)):
            self.digits2.append(randint(0,9)) 
            self.number2 = self.number2 + str(self.digits2[i+1])
            
        self.sum = str(int(self.number1) + int(self.number2))
        
        self.SumDigits = []
        for i in range(len(self.sum)):
            self.SumDigits.append(self.sum[i:i+1])

        self.problem = "Subtract.<br><br><table><tr><td></td>"
        for i in range(len(self.SumDigits)):
            self.problem = self.problem + "<td>"+str(self.SumDigits[i])+"</td>"
        self.problem = self.problem + "</tr><tr><td style='text-align:right'>&minus;</td>"

        for i in range(len(self.digits1)):
            self.problem = self.problem + "<td>"+str(self.digits1[i])+"</td>"
        
        self.problem = self.problem + "</tr>"
        self.problem = self.problem + "<tr><td colspan=5 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line.png' /></td></tr>"
        self.problem = self.problem + "</table>"
        
        self.answer = int(self.number2)
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+100]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+100]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+100]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+100]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.sum,self.number1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        The sum of two numbers is 4567. If one of the numbers is 2345, what is the other number?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ2"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag < 5:
            self.number1 = randint(1000,8888)
            self.number2 = randint(100,888)
        elif self.flag >=5 and self.flag<9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(50,1000)
            self.number2 = randint(50,1000)
            while self.number1 == self.number2:
                self.number2 = randint(50,100)
        
        self.sum = self.number1 + self.number2
        
        self.flag1 = randint(1,3)
        
        if self.flag1 == 1:
            self.problem = "The sum of two numbers is %d. If one of the numbers is %d, what is the other number?"%(self.sum,self.number1)
        elif self.flag1 == 2:
            if self.number1 < self.number2:
                self.number1,self.number2 = self.number2,self.number1
            self.problem = "The sum of two numbers is %d. If the bigger number is %d, what is the smaller number?"%(self.sum,self.number1)
        elif self.flag1 == 3:
            if self.number1 > self.number2:
                self.number1,self.number2 = self.number2,self.number1
            self.problem = "The sum of two numbers is %d. If the smaller number is %d, what is the bigger number?"%(self.sum,self.number1)
        
        self.answer = self.number2
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+100]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+100]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+100]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+100]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.sum,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
            Find the missing number.
              1 2 3 4
            + 2 3 4 _
            ---------
              3 5 7 8'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ3"
        self.CheckAnswerType = 1
        
        '''first digit can't be zero'''
        self.digits1 = [randint(1,7)]
        self.number1 = str(self.digits1[0])        
        for i in range(3):
            self.digits1.append(randint(0,9))         
            self.number1 = self.number1 + str(self.digits1[i+1])

        self.digits2 = [randint(1,8-self.digits1[0])]        
        self.number2 = str(self.digits2[0])        
        for i in range(randint(2,3)):
            self.digits2.append(randint(0,9)) 
            self.number2 = self.number2 + str(self.digits2[i+1])
        
        self.sum = str(int(self.number1) + int(self.number2))
        
        self.SumDigits = []
        for i in range(len(self.sum)):
            self.SumDigits.append(self.sum[i:i+1])

        self.digits1 = self.SumDigits
        
        self.problem = "Find the missing number.<br><br><table><tr><td></td>"
        
        self.flag = randint(1,3)
        
        if self.flag == 1:
            self.MissingDigit = randint(0,len(self.digits1)-1) 
            for i in range(len(self.digits1)):
                if i == self.MissingDigit:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
                    self.answer = self.digits1[i]
                else:
                    self.problem = self.problem + "<td>"+str(self.digits1[i])+"</td>"
        else:
            for i in range(len(self.digits1)):
                self.problem = self.problem + "<td>"+str(self.digits1[i])+"</td>"
            
        self.problem = self.problem + "</tr><tr><td>&minus;</td>"
        
        if len(self.digits2) == 3:
            self.problem = self.problem +"<td></td>"
        
        if self.flag == 2:
            self.MissingDigit = randint(0,len(self.digits2)-1) 
            for i in range(len(self.digits2)):
                if i == self.MissingDigit:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
                    self.answer = self.digits2[i]
                else:
                    self.problem = self.problem + "<td>"+str(self.digits2[i])+"</td>"
        else:
            for i in range(len(self.digits2)):
                self.problem = self.problem + "<td>"+str(self.digits2[i])+"</td>"
        
        self.problem = self.problem + "</tr>"
        self.problem = self.problem + "<tr><td colspan=5 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line.png' /></td></tr>"       

        self.problem = self.problem + "<tr><td></td>"
        
        self.difference = self.number1
                
        if self.flag == 3:
            self.MissingDigit = randint(0,len(self.digits1)-1) 
            for i in range(len(self.digits1)):
                if i == self.MissingDigit:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
                    self.answer = self.difference[i:i+1]
                else:
                    self.problem = self.problem + "<td>"+str(self.difference)[i:i+1]+"</td>"
        else:
            for i in range(len(self.digits1)):
                self.problem = self.problem + "<td>"+str(self.difference)[i:i+1]+"</td>"            

        self.problem = self.problem + "</tr></table>"
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        
        for i in range(9):
            if i != int(self.answer):
                self.wrongAnswers.append(str(i))
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.flag,self.sum,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ4a(self):
        '''e.g.:
        <An amusement park> received 1489 <visitors> on <Saturday> and 2489 <visitors> on <Sunday>. How many more <visitors> did it receive on <Sunday> than on <Saturday>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ4a"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            while self.number1 == self.number2:
                self.number2 = randint(100,999)
        
        if self.number1 > self.number2:
            self.number1,self.number2 = self.number2,self.number1
        
        self.items = [['An amusement park','visitors','Saturday','Sunday'],['A water park','visitors','Saturday','Sunday'],['A theme park','visitors','Saturday','Sunday'],['An animal safari park','visitors','Saturday','Sunday'],['A bird park','visitors','Saturday','Sunday'],['A zoo','visitors','Saturday','Sunday'],['A science museum','visitors','Saturday','Sunday'],['A shopping mall','shoppers','Saturday','Sunday'],['A cinema','moviegoers','Saturday','Sunday'],['A carnival','visitors','Saturday','Sunday']]
        self.days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        
        self.item = random.choice(self.items)
        
        self.Day1Index = randint(0,6)
        if self.Day1Index == 6:
            self.Day2Index = 0
        else:
            self.Day2Index = self.Day1Index + 1 
        
        problemFlag = randint(1,2)
        if problemFlag==1:
            self.problem = "%s received %d %s on %s and %d %s on %s. How many more %s did it receive on %s than on %s?"%(self.item[0],self.number1,self.item[1],self.days[self.Day1Index],
                                                                                                                              self.number2,self.item[1],self.days[self.Day2Index],
                                                                                                                              self.item[1],self.days[self.Day2Index],self.days[self.Day1Index])        
        else:
            self.problem = "%s received %d %s on %s and %d %s on %s. What is the difference between the number of %s it received on the two days?"%(self.item[0],self.number1,self.item[1],self.days[self.Day1Index],
                                                                                                                              self.number2,self.item[1],self.days[self.Day2Index],
                                                                                                                              self.item[1])
        #self.problem = random.choice([self.problem1,self.problem2])
        self.answer = self.number2 - self.number1
        
        self.unit = self.item[1]
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+100]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+100]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+100]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+100]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,problemFlag,self.number2,self.number1,self.days[self.Day2Index],self.days[self.Day1Index],self.item[1],'on','days',self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ4b(self):
        '''e.g.:
        <An art museum> received 1489 <visitors> in <March> and 2489 <visitors> in <April>. How many more <visitors> did it receive in <April> than in <March>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ4b"
        self.CheckAnswerType = 1


        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            while self.number1 == self.number2:
                self.number2 = randint(100,999)
        
        if self.number1 > self.number2:
            self.number1,self.number2 = self.number2,self.number1
            
        self.items = [['An art museum','visitors','March','April'],['A vegetable farm','visitors','March','April'],['A strawberry farm','visitors','March','April'],['An animal farm','visitors','March','April'],['A grocery store','shoppers','March','April'],['A minimart','customers','March','April'],['A hotel','guests','March','April'],['A restaurant','guests','March','April'],['An airport','passengers','March','April'],['A post office','customers','March','April']]
        self.months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        
        self.item = random.choice(self.items)
        
        self.Month1Index = randint(0,10)
        self.Month2Index = self.Month1Index + 1 
        
        problemFlag = randint(1,2)
        if problemFlag==1:
            self.problem = "%s received %d %s in %s and %d %s in %s. How many more %s did it receive in %s than in %s?"%(self.item[0],self.number1,self.item[1],self.months[self.Month1Index],
                                                                                                                        self.number2,self.item[1],self.months[self.Month2Index],
                                                                                                                        self.item[1],self.months[self.Month2Index],self.months[self.Month1Index])
        else:
            self.problem = "%s received %d %s in %s and %d %s in %s. What is the difference between the number of %s it received in the two months?"%(self.item[0],self.number1,self.item[1],self.months[self.Month1Index],
                                                                                                                        self.number2,self.item[1],self.months[self.Month2Index],
                                                                                                                        self.item[1])
        
        #self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.number2 - self.number1
        
        self.unit = self.item[1]
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+100]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+100]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+100]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+100]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,problemFlag,self.number2,self.number1,self.months[self.Month2Index],self.months[self.Month1Index],self.item[1],'in','months',self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ5(self):
        '''e.g.:
        <A primary school has> 2658 <pupils>. <A secondary school has> 1239 <pupils>. What is the difference between the number of <pupils in the two schools>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ5"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            while self.number1 == self.number2:
                self.number2 = randint(100,999)
            
        self.items = [['A primary school has','pupils','A secondary school has','pupils in the two schools','pupils','primary school','secondary school'],
                      ['A town has','residents','Its neighbouring town has','residents in the two towns','residents','town 1','town 2'],
                      ['A clothes company employs','workers','A shoes company employs','workers that the two companies employ','workers','clothes company','shoes company'],
                      ['A fish tank has','fishes','Another fish tank has','fishes in the two fish tanks','fishes','fish tank 1','fish tank 2'],
                      ['A national park has','trees','Another national park has','trees in the two national parks','trees','park 1','park 2'],
                      ['A wildlife sanctuary keeps','animals','Another wildlife sanctuary keeps','animals that the two wildlife sanctuaries keep','animals','sanctuary 1','sanctuary 2'],
                      ['A science college enrols','students','A management college enrols','students that the two colleges enrol','students','science college','management college'],
                      ['A school library carries','books','A public library carries','books that the two libraries carry','books','school library','public library'],
                      ['Warehouse A can store','computers','Warehouse B can store','computers that the two warehouses can store','computers','Warehouse A','Warehouse B'],
                      ['A bookstore in a school carries','pens','A bookstore in a shopping centre carries','pens that the two bookstores carry','pens','bookstore 1','bookstore 2'],
                      ['A toys shop in a mall sold','toys','Another toys shop in the mall sold','toys sold by the two toys shops','toys','toys shop 1','toys shop 2'],
                      ['Grocery Store A sold','cans of milk','Grocery Store B sold','cans of milk sold by the two grocery stores','cans','Store A','Store B'],
                      ['Farmer A sold','eggs','Farmer B sold','eggs sold by the two farmers','eggs','Farmer A','Farmer B'],
                      ['An art museum has','items on display','A science museum','items that the two museums have on display','items','art museum','science museum'],
                      ['A movie rental store carries','movie CDs','Another movie rental store carries','movie CDs that the two stores carry','movie CDs','store 1','store 2'],
                      ['Bakery A sold','muffins','Bakery B sold','muffins sold by the two bakeries','muffins','Bakery A','Bakery B'],
                      ['Ship A has','passengers','Ship B has','passengers on the two ships','passengers','Ship A','Ship B']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %d %s. %s %d %s. What is the difference between the number of %s?"%(self.item[0],self.number1,self.item[1],
                                                                              self.item[2],self.number2,self.item[1],
                                                                              self.item[3])
        
        self.answer = abs(self.number1 - self.number2)

        self.unit = self.item[4]
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+20]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+20]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+20]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+20]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.item[3],self.item[5],self.item[6],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ6(self):
        '''e.g.:
        [Person.Unclename] <had> $1239 <in his savings>. He <withdrew> $123 <from his savings>. How much money <had he left in his savings?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ6"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.name = random.choice(PersonName.UncleName)
            
        self.items = [['had','in his savings','withdrew','from his savings','had he left in his savings','He had',' left in his savings','withdrew','left'],
                      ['earned','at his job','spent','of his earnings and saved the rest','did he save','He saved','','spent','saved'],
                      ['won','in a game','gave','of his winnings to his daughter and kept the rest for himself','did he keep for himself','He kept',' for himself','daughter','for himself'],
                      ['had','with him','spent','to buy furniture for his house','had he left','He had',' left','spent','left'],
                      ['received','as a bonus','used','to buy gifts for his family and saved the rest','did he save','He saved','','bought gifts','saved'],
                      ['had','in his wallet','spent','on shopping','did he have left in his wallet','He had',' left in his wallet','spent','left'],
                      ['had','with him','used','to buy books','did he have left','He had',' left','bought books','left'],
                      ['received a donation of','for his library','used','of it to buy books','did he have left','He had',' left','bought books','left'],
                      ['had','at first','spent','on air tickets','did he have left','He had',' left','air tickets','left'],
                      ['won','in a lottery','used','to buy gifts for his family','did he have left','He had',' left','bought gifts','left']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %s $%d %s. He %s $%d %s. How much money %s?"%(self.name,self.item[0],self.sum,self.item[1],
                                                                        self.item[2],self.number1,self.item[3],self.item[4])
        
        self.answer = self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+20]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+20]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+20]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+20]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.sum,self.number1,self.item[5],self.item[6],self.item[7],self.item[8])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ7a(self):
        '''e.g.:
        [Person.Girlname] <had> 5224 <beads> and <marbles>. If she <had> 2020 <beads>, find the number of <marbles> she <had>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ7a"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.name = random.choice(PersonName.GirlName)
            
        self.items = [['had','beads','marbles','had'],['collected','stamps','stickers','collected'],
                      ['had','rubberbands','buttons','had'],['bought','buttons','rubberbands','bought'],
                      ['won','points','stars','won'],['had','paper clips','push pins','had'],
                      ['bought','stickers','stamps','bought'],['collected','flags','stamps','collected'],
                      ['got','marbles','magnets','got'],['had','tacks','ice-cream sticks','had']]


        self.item = random.choice(self.items)
               
        self.problem = "%s %s %d %s and %s. If she %s %d %s, find the number of %s she %s."%(self.name,self.item[0],self.sum,self.item[1],
                                                                                             self.item[2],self.item[0],self.number1,self.item[1],
                                                                                             self.item[2],self.item[0]) 
                
        self.answer = self.number2
        
        self.unit = self.item[2]
        self.dollar_unit = ""
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+20]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+20]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+20]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+20]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.sum,self.number1,'She',self.item[0],self.item[2],self.item[1],self.item[2],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ7b(self):
        '''e.g.:
        [Person.Girlname 1] and [Person.Girlname 2] had 5224 <beads> altogether. If [Person.Girlname 1] had 2023 <beads>, how many <beads> had [Person.Girlname 2]?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ7b"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.names = random.sample(PersonName.GirlName,2)
            
        self.items = ['beads','stamps','rubberbands','buttons','pushpins','safety pins','stickers','flags','pins','tacks']


        self.item = random.choice(self.items)
               
        self.problem = "%s and %s had %d %s altogether. If %s had %d %s, how many %s had %s?"%(self.names[0],self.names[1],self.sum,self.item,
                                                                                               self.names[0],self.number1,self.item,self.item,self.names[1]) 
                
        self.answer = self.number2
        
        self.unit = self.item
        self.dollar_unit = ""
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+20]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+20]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+20]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+20]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.sum,self.number1,self.names[1],'had',self.item,self.names[0],self.names[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ7c(self):
        '''e.g.:
        [Person.Boyname 1] and [Person.Boyname 2] collected 5224 <marbles> altogether. If [Person.Boyname 1] collected 2023 <marbles>, how many <marbles> did [Person.Boyname 2] collect?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ7c"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.names = random.sample(PersonName.BoyName,2)
            
        self.items = ['marbles','stamps','stickers','flags','rubberbands','coins','keyrings','darts','animal cards','cards']


        self.item = random.choice(self.items)
               
        self.problem = "%s and %s collected %d %s altogether. If %s collected %d %s, how many %s did %s collect?"%(self.names[0],self.names[1],self.sum,self.item,
                                                                                               self.names[0],self.number1,self.item,self.item,self.names[1]) 
                
        self.answer = self.number2
        
        self.unit = self.item
        self.dollar_unit = ""
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+20]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+20]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+20]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+20]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.sum,self.number1,self.names[1],'collected',self.item,self.names[0],self.names[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ8a(self):
        '''e.g.:
        <A grocery store sold> 6904 <chicken eggs> and <duck eggs>. If <it sold> 2045 <chicken eggs>, how many <duck eggs> did <it sell>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ8a"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.items = [['A grocery store sold','chicken eggs','duck eggs','it sold','it sell','It sold'],
                      ['A fruit vendor had','pears','mangoes','he had','he have','He had'],
                      ['A farmer had','hens','ducks','he had','he have','He had'],
                      ['A phone shop sold','SIM cards','calling cards','it sold','it sell','It sold'],
                      ['A post office sold','envelopes','stamps','it sold','it sell','It sold'],
                      ['A supermarket had','bags of flour','bags of sugar','it had','it have','It had'],
                      ['An amusement park received','children','adults','it received','it receive','It received'],
                      ['A school had','boys','girls','it had','it have','It had'],
                      ['A library carried','books','DVDs','it carried','it carry','It carried'],
                      ['A baker baked','cupcakes','muffins','he baked','he bake','He baked'],
                      ['A hawker centre sold','plates of rice','bowls of soup','it sold','it sell','It sold']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %d %s and %s altogether. If %s %d %s, how many %s did %s?"%(self.item[0],self.sum,self.item[1],self.item[2],self.item[3],self.number1,
                                                                            self.item[1],self.item[2],self.item[4]) 
                
        self.answer = self.number2
        
        self.unit = self.item[2]
        self.dollar_unit = ""
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+20]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+20]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+20]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+20]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.sum,self.number1,self.item[2],self.item[5],self.item[1],self.item[2],1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ8b(self):
        '''e.g.:
        <A grocery store sold> 3904 <chicken eggs> and 2102 <duck eggs>. How many more <chicken eggs> than <duck eggs> did <it sell>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ8b"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.items = [['A grocery store sold','chicken eggs','duck eggs','it sell','It sold','more chicken eggs than duck eggs'],
                      ['A fruit vendor had','pears','mangoes','he have','He had','more pears than mangoes'],
                      ['A farmer had','hens','ducks','he have','He had','more hens than ducks'],
                      ['A phone shop sold','SIM cards','calling cards','it sell','It sold','more SIM cards than phone cards'],
                      ['A post office sold','envelopes','stamps','it sell','It sold','more envelopes than stamps'],
                      ['A supermarket had','bags of flour','packets of sugar','it have','It had','more bags of flour than packets of sugar'],
                      ['An amusement park received','children','adults','it receive','It received','more children than adults'],
                      ['A school had','boys','girls','it have','It had','more boys than girls'],
                      ['A library carried','books','DVDs','it carry','It carried','more books than DVDs'],
                      ['A baker baked','cupcakes','muffins','he bake','He baked','more cupcakes than muffins'],
                      ['A hawker centre sold','plates of rice','bowls of soup','it sell','It sold','more plates of rice than bowls of soup']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %d %s and %d %s. How many more %s than %s did %s?"%(self.item[0],self.sum,self.item[1],self.number1,self.item[2],
                                                                               self.item[1],self.item[2],self.item[3]) 
                
        self.answer = self.number2
        
        self.unit = ""
        self.dollar_unit = ""
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+20]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+20]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+20]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+20]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.sum,self.number1,self.item[5],self.item[4],self.item[1],self.item[2],2,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ9(self):
        '''e.g.:
        There were 8467 <birds in a village>. 1239 <birds migrated out of the village>. How many <birds were left in the village>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ9"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.sum = self.number1 + self.number2
            
        self.items1 = [['birds in a village','birds migrated out of the village','birds were left in the village','birds','migrated','left'],
                       ['children who took a maths test','children got 5 stars on the maths test','children did not get 5 stars on the maths test','children','5 stars','others'],
                       ['workers in a factory','workers left the factory','workers were left in the factory','workers','left the factory','still in the factory'],
                       ['people on a beach','people left the beach','people were left on the beach','people','left the beach','still on the beach'],
                       ['spectators in a stadium','spectators left the stadium','spectators were left in the stadium','spectators','left the stadium','still in the stadium'],
                       ['passengers at a railway station','passengers boarded a train','passengers were left at the railway station','passengers','boarded the train','left at the station'],
                       ['beads at first','beads were used to make a necklace','beads were left','beads','necklace','left'],
                       ['plants at a nursery','plants were sold','plants were left','plants','sold','left'],
                       ['loaves of bread made by a bakery','loaves of bread were sold','loaves of bread were left unsold','loaves of bread','sold','left'],
                       ['oranges on a farm','oranges were picked','oranges on the farm were not picked','oranges','picked','not picked'],
                       ['people in a village','people moved from the village to the town','people were left in the village','people','moved to town','left in the village'],
                       ['children in the school hall','left the school hall for their classrooms','children were left in the school hall','children','left for classrooms','left in school hall'],
                       ['travelers at the airport','travelers left the airport','travelers were left at the airport','travelers','left the airport','still at the airport'],
                       ['passengers on the train','passengers got off the train','passengers were left on the train','passengers','got off the train','left on the train']]

        self.item1 = random.choice(self.items1)

        self.items2 = [['birds living in a village migrated away from the village','birds were left in the village','birds','migrated','left'],
                       ['children who took a test got 5 stars on the test','children did not get 5 stars on the test','children','5 stars','others'],
                       ['workers who work in a factory left the factory','workers were left in the factory','workers','left the factory','still in the factory'],
                       ['people who were on a beach left the beach','people were left on the beach','people','left the beach','still on the beach'],
                       ['spectators who were watching a soccer game in a stadium left the stadium','spectators were left in the stadium','spectators','left the stadium','still in the stadium'],
                       ['passengers who were waiting at a railway station boarded a train','passengers were left at the railway station','passengers','boarded the train','left at the station'],
                       ['beads were used to make a necklace','beads were left','beads','necklace','left'],
                       ['plants at a nursery were sold','plants were left','plants','sold','left'],
                       ['loaves of bread made by a bakery were sold','loaves of bread were left unsold','loaves of bread','loaves of bread','sold','left'],
                       ['mangoes on a farm were picked','mangoes on the farm were not picked','mangoes','picked','not picked'],
                       ['people who lived in a village moved to the town','people were left in the village','people','moved to town','left in the village'],
                       ['children who had assembled in the school hall left for their classrooms','children were left in the school hall','children','left for classrooms','left in school hall'],
                       ['travelers waiting at the airport for their flights took off','travelers were left at the airport','travelers','left the airport','still at the airport'],
                       ['passengers on a train got off the train','passengers were left on the train','passengers','got off the train','left on the train']]
        
        self.item2 = random.choice(self.items2)
               
        problemFlag = randint(1,2)
        if problemFlag==1:
            self.problem = "There were %d %s. %d %s. How many %s?"%(self.sum,self.item1[0],self.number1,self.item1[1],self.item1[2])
            tempItem1 = self.item1[2]
            tempItem2 = self.item1[3]
            tempItem3 = self.item1[4]
            tempItem4 = self.item1[5]
        else:
            self.problem = "%d out of %d %s. How many %s?"%(self.number1,self.sum,self.item2[0],self.item2[1])
            tempItem1 = self.item2[1] 
            tempItem2 = self.item2[2]
            tempItem3 = self.item2[3]
            tempItem4 = self.item2[4]

        #self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.number2
        
        self.unit = ""
        self.dollar_unit = ""
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+20]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+20]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+20]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+20]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.sum,self.number1,tempItem1,tempItem2,tempItem3,tempItem4,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ10a(self):
        '''e.g.:
        [Person.Unclename] bought a <computer> and a <printer> for $1750. If the <computer> cost $1000, what was the cost of the <printer>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ10a"
        self.CheckAnswerType = 1
            
        self.name = random.choice(PersonName.UncleName)
                    
        self.items = [['computer','printer',randint(500,1500),randint(100,400)],['sofa set','coffee table',randint(1000,3000),randint(200,800)],
                      ['bed frame','mattress',randint(500,1000),randint(500,2000)],['TV set','TV console',randint(500,1500),randint(500,1500)],
                      ['dining table set','recliner sofa',randint(500,2000),randint(500,2000)],['camera','printer',randint(500,1500),randint(100,400)],
                      ['book shelf','table',randint(500,1000),randint(100,1000)],['DVD player','couch',randint(500,2000),randint(500,2000)],
                      ['laptop','smart phone',randint(700,2000),randint(200,800)]]

        self.item = random.choice(self.items)

        self.number1 = self.item[2]
        self.number2 = self.item[3]
        
        self.sum = self.number1 + self.number2
               
        self.problem = "%s bought a %s and a %s for $%d. If the %s cost $%d, what was the cost of the %s?"%(self.name,self.item[0],self.item[1],self.sum,
                                                                                                            self.item[0],self.number1,self.item[1]) 
        self.answer = self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+20]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+20]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+20]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+20]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10a(self.problem,self.answer,self.sum,self.number1,self.item[0],self.item[1],self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ10b(self):
        '''e.g.:
        [Person.Unclename] bought a <computer> for $1250 and a <printer> for $750. How much more did he pay for the <computer> than for the <printer>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ10b"
        self.CheckAnswerType = 1
            
        self.name = random.choice(PersonName.UncleName)
                    
        self.items = [['computer','printer',randint(500,1500),randint(100,400)],['sofa set','coffee table',randint(1000,3000),randint(200,800)],
                      ['bed frame','mattress',randint(500,1000),randint(500,2000)],['TV set','TV console',randint(500,1500),randint(500,1500)],
                      ['dining table set','recliner sofa',randint(500,2000),randint(500,2000)],['camera','printer',randint(500,1500),randint(100,400)],
                      ['book shelf','table',randint(500,1000),randint(100,1000)],['DVD player','couch',randint(500,2000),randint(500,2000)],
                      ['laptop','smart phone',randint(700,2000),randint(200,800)]]

        self.item = random.choice(self.items)

        self.number1 = self.item[2]
        self.number2 = self.item[3]
        
        if self.number1 < self.number2:
            self.number1,self.number2 = self.number2,self.number1
               
        self.problem = "%s bought a %s for $%d and a %s for $%d. How much more did he pay for the %s than for the %s?"%(self.name,self.item[0],self.number1,
                                                                                                                        self.item[1],self.number2,self.item[0],self.item[1]) 
        self.answer = self.number1 - self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
                
        self.template = "MCQTypeProblems.html"
        
        if self.answer > 20:
            self.wrongAnswers = [self.answer-10,self.answer-20,self.answer+10,self.answer+20]
        elif self.answer > 10:
            self.wrongAnswers = [self.answer-10,self.answer-5,self.answer+10,self.answer+20]
        elif self.answer > 5:
            self.wrongAnswers = [self.answer+5,self.answer-5,self.answer+10,self.answer+20]
        else:
            self.wrongAnswers = [self.answer+5,self.answer+15,self.answer+10,self.answer+20]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10b(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[1],self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
   
    def AdditionExplanation(self,number1,number2):
        
        thousands1,hundreds1 = divmod(int(number1),1000)
        hundreds1,tens1 = divmod(hundreds1,100)
        tens1,ones1 = divmod(tens1,10)

        thousands2,hundreds2 = divmod(int(number2),1000)
        hundreds2,tens2 = divmod(hundreds2,100)
        tens2,ones2 = divmod(tens2,10)

        carryOverToTens,sumOnes = divmod(ones1+ones2,10)
        carryOverToHundreds,sumTens = divmod(tens1+tens2+carryOverToTens,10)
        carryOverToThousands,sumHundreds = divmod(hundreds1+hundreds2+carryOverToHundreds,10)
        sumThousands = thousands1+thousands2+carryOverToThousands
        
        if carryOverToThousands==1:
            if len(str(number1))==4:
                thousands1_td = "<sup>1</sup>%d"%(thousands1)
            else:
                thousands1_td = "&nbsp;" #thousands place digit of number1 is 0           
        else:
            if len(str(number1))==4:
                thousands1_td = "%d"%(thousands1)
            else:
                thousands1_td = "&nbsp;" #thousands place digit of number1 is 0

        if carryOverToHundreds==1:
            if len(str(number1))>=3:
                hundreds1_td = "<sup>1</sup>%d"%(hundreds1)
            else:
                hundreds1_td = "&nbsp;" #hundreds place digit of number1 is 0           
        else:
            if len(str(number1))>=3:
                hundreds1_td = "%d"%(hundreds1)
            else:
                hundreds1_td = "&nbsp;" #hundreds place digit of number1 is 0           

        if carryOverToTens==1:
            tens1_td = "<sup>1</sup>%d"%(tens1)
        else:
            tens1_td = "%d"%(tens1)

        #checks to make sure not to display the leading 0s
        if len(str(number2))==4:
            thousands2_td = "%d"%(thousands2)
        else:
            thousands2_td = "&nbsp;" #thousands place digit of number2 is 0
        if len(str(number2))>=3:
            hundreds2_td = "%d"%(hundreds2)
        else:
            hundreds2_td = "&nbsp;" #hundreds place digit of number2 is 0
        
        if sumThousands==0:
            thousandsAnswer_td = "&nbsp;"
        else:
            thousandsAnswer_td = "%d"%(sumThousands)
        
        self.solution_text = "<table class='ExplanationMoneyTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%s</td><td>%s</td><td>%s</td><td>%d</td></tr>"%(thousands1_td,hundreds1_td,tens1_td,ones1)
        self.solution_text = self.solution_text + "<tr><td>+</td><td>%s</td><td>%s</td><td>%d</td><td>%d</td></tr>"%(thousands2_td,hundreds2_td,tens2,ones2)
        self.solution_text = self.solution_text + "<tr><td colspan=5 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%s</td><td>%d</td><td>%d</td><td>%d </td></tr>"%(thousandsAnswer_td,sumHundreds,sumTens,sumOnes)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        return self.solution_text

    def SubtractionExplanation(self,number1,number2):
        
        if int(number1)<int(number2):
            number1,number2 = number2,number1

        thousands1,hundreds1 = divmod(int(number1),1000)
        hundreds1,tens1 = divmod(hundreds1,100)
        tens1,ones1 = divmod(tens1,10)

        thousands2,hundreds2 = divmod(int(number2),1000)
        hundreds2,tens2 = divmod(hundreds2,100)
        tens2,ones2 = divmod(tens2,10)

        number3 = int(number1) - int(number2)
        thousands3,hundreds3 = divmod(number3,1000)
        hundreds3,tens3 = divmod(hundreds3,100)
        tens3,ones3 = divmod(tens3,10)

        borrowedFromTens = 0
        borrowedFromHundreds = 0
        borrowedFromThousands = 0
        if ones1>=ones2:
            ones1_td = "%d"%(ones1)
        else:
            ones1_td = "<sup>1</sup>%d"%(ones1)
            borrowedFromTens = 1

        if tens1==0:
            if borrowedFromTens==1:
                tens1_td = "<sup>9</sup><del><sup>1</sup>0</del>"
                borrowedFromHundreds = 1
            if borrowedFromTens==0 and tens2==0: # 0-0
                tens1_td = "0"
            if borrowedFromTens==0 and tens2>0:
                tens1_td = "<sup>1</sup>0"
                borrowedFromHundreds = 1
        else: # tens1>0
            if borrowedFromTens==1:
                if tens1-1>=tens2:
                    tens1_td = "<sup>%d</sup><del>%d</del>"%(tens1-1,tens1)
                else:
                    tens1_td = "<sup><sup>1</sup>%d</sup><del>%d</del>"%(tens1-1,tens1)
                    borrowedFromHundreds = 1
            if borrowedFromTens==0 and tens1>=tens2:
                tens1_td = "%d"%(tens1)
            if borrowedFromTens==0 and tens1<tens2:
                tens1_td = "<sup>1</sup>%d"%(tens1)
                borrowedFromHundreds=1
        
        if hundreds1==0:
            if borrowedFromHundreds==1:
                hundreds1_td = "<sup>9</sup><del><sup>1</sup>0</del>"
                borrowedFromThousands = 1
            if borrowedFromHundreds==0 and hundreds2==0: # 0-0
                hundreds1_td = "0"
            if borrowedFromHundreds==0 and hundreds2>0:
                hundreds1_td = "<sup>1</sup>0"
                borrowedFromThousands = 1
        else: # hundreds1>0
            if borrowedFromHundreds==1:
                if hundreds1-1>=hundreds2:
                    hundreds1_td = "<sup>%d</sup><del>%d</del>"%(hundreds1-1,hundreds1)
                else:
                    hundreds1_td = "<sup><sup>1</sup>%d</sup><del>%d</del>"%(hundreds1-1,hundreds1)
                    borrowedFromThousands = 1
            if borrowedFromHundreds==0 and hundreds1>=hundreds2:
                hundreds1_td = "%d"%(hundreds1)
            if borrowedFromHundreds==0 and hundreds1<hundreds2:
                hundreds1_td = "<sup>1</sup>%d"%(hundreds1)
                borrowedFromThousands=1

        if number1>999: # 4-digit number
            if borrowedFromThousands==1:
                thousands1_td = "<sup>%d</sup><del>%d</del>"%(thousands1-1,thousands1)
            else:
                thousands1_td = "%d"%(thousands1)
        else: # 3-digit number
            thousands1_td = "&nbsp;"

        #checks to make sure not to display the leading 0s
        if len(str(number2))==4:
            thousands2_td = "%d"%(thousands2)
        else:
            thousands2_td = "&nbsp;" #thousands place digit of number2 is 0
        if len(str(number2))>=3:
            hundreds2_td = "%d"%(hundreds2)
        else:
            hundreds2_td = "&nbsp;" #hundreds place digit of number2 is 0'''
        
        if len(str(number3))==1:
            onesAnswer_td = "%d"%(ones3)
            tensAnswer_td = "&nbsp;"
            hundredsAnswer_td="&nbsp;"
            thousandsAnswer_td = "&nbsp;"
        elif len(str(number3))==2:
            onesAnswer_td = "%d"%(ones3)
            tensAnswer_td = "%d"%(tens3)
            hundredsAnswer_td="&nbsp;"
            thousandsAnswer_td = "&nbsp;"
        elif len(str(number3))==3:
            onesAnswer_td = "%d"%(ones3)
            tensAnswer_td = "%d"%(tens3)
            hundredsAnswer_td="%d"%(hundreds3)
            thousandsAnswer_td = "&nbsp;"
        else:
            onesAnswer_td = "%d"%(ones3)
            tensAnswer_td = "%d"%(tens3)
            hundredsAnswer_td="%d"%(hundreds3)
            thousandsAnswer_td = "%d"%(thousands3)
        
        self.solution_text = "<table class='ExplanationMoneyTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"%(thousands1_td,hundreds1_td,tens1_td,ones1_td)
        self.solution_text = self.solution_text + "<tr><td>&minus;</td><td>%s</td><td>%s</td><td>%d</td><td>%d</td></tr>"%(thousands2_td,hundreds2_td,tens2,ones2)
        self.solution_text = self.solution_text + "<tr><td colspan=5 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%s</td><td>%s</td><td>%s</td><td>%s </td></tr>"%(thousandsAnswer_td,hundredsAnswer_td,tensAnswer_td,onesAnswer_td)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        return self.solution_text

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False