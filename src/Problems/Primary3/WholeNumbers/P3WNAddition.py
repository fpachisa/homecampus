'''
Created on Feb 28, 2013
Module: P3WNAddition
Generates the Addition problems for Primary 3

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

class P3WNAddition:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1a","ProblemType1b","ProblemTypeMCQ1a","ProblemTypeMCQ1b",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3a","ProblemType3b","ProblemTypeMCQ3a","ProblemTypeMCQ3b",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType5","ProblemTypeMCQ5",],
                            6:["ProblemType6a","ProblemType6b","ProblemType6c","ProblemTypeMCQ6a","ProblemTypeMCQ6b","ProblemTypeMCQ6c",],
                            7:["ProblemType7","ProblemTypeMCQ7",],
                            8:["ProblemType8","ProblemTypeMCQ8",],
                            9:["ProblemType9","ProblemTypeMCQ9",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1a(),self.GenerateProblemType1b(),self.GenerateProblemTypeMCQ1a(),self.GenerateProblemTypeMCQ1b(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3a(),self.GenerateProblemType3b(),self.GenerateProblemTypeMCQ3a(),self.GenerateProblemTypeMCQ3b(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemType5(),self.GenerateProblemTypeMCQ5(),],
                                    6:[self.GenerateProblemType6a(),self.GenerateProblemTypeMCQ6a(),self.GenerateProblemType6b(),self.GenerateProblemTypeMCQ6b(),
                                       self.GenerateProblemType6c(),self.GenerateProblemTypeMCQ6c(),],
                                    7:[self.GenerateProblemType7(),self.GenerateProblemTypeMCQ7(),],
                                    8:[self.GenerateProblemType8(),self.GenerateProblemTypeMCQ8(),],
                                    9:[self.GenerateProblemType9(),self.GenerateProblemTypeMCQ9(),],
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
        #return self.GenerateProblemTypeMCQ9()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1a":self.GenerateProblemType1a(),
                            "ProblemType1b":self.GenerateProblemType1b(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3a":self.GenerateProblemType3a(),
                            "ProblemType3b":self.GenerateProblemType3b(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6a":self.GenerateProblemType6a(),
                            "ProblemType6b":self.GenerateProblemType6b(),
                            "ProblemType6c":self.GenerateProblemType6c(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemTypeMCQ1a":self.GenerateProblemTypeMCQ1a(),
                            "ProblemTypeMCQ1b":self.GenerateProblemTypeMCQ1b(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3a":self.GenerateProblemTypeMCQ3a(),
                            "ProblemTypeMCQ3b":self.GenerateProblemTypeMCQ3b(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemTypeMCQ6a":self.GenerateProblemTypeMCQ6a(),
                            "ProblemTypeMCQ6b":self.GenerateProblemTypeMCQ6b(),
                            "ProblemTypeMCQ6c":self.GenerateProblemTypeMCQ6c(),
                            "ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),
                            "ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            "ProblemTypeMCQ9":self.GenerateProblemTypeMCQ9(),
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

        if self.number1 < self.number2: #to ensure that the first number is always bigger for display's sake
            temp = self.number2
            self.number2 = self.number1
            self.number1 = temp

        self.problem1 = "Find the sum of %d and %d."%(self.number1,self.number2)
        self.problem2 = "What is the sum of %d and %d?"%(self.number1,self.number2)
        self.problem3 = "What is %d + %d?"%(self.number1,self.number2)
        self.problem4 = "The sum of %d and %d is _____."%(self.number1,self.number2)
        self.problem5 = "%d + %d = ?"%(self.number1,self.number2)
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])
        
        self.answer = self.number1 + self.number2
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2)
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

        self.problem = "Add.<br><br><table><tr><td></td>"
        for i in range(len(self.digits1)):
            self.problem = self.problem + "<td>"+str(self.digits1[i])+"</td>"
        self.problem = self.problem + "</tr><tr><td style='text-align:right'>+</td>"
        
        if len(self.digits2) == 3:
            self.problem = self.problem +"<td></td>"
        for i in range(len(self.digits2)):
            self.problem = self.problem + "<td>"+str(self.digits2[i])+"</td>"            
        
        self.problem = self.problem + "</tr>"
        self.problem = self.problem + "<tr><td colspan=5 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line.png' /></td></tr>"
        self.problem = self.problem + "</table>"
        
        self.answer = int(self.number1) + int(self.number2)
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType1(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))
        
        self.solution_text = self.AdditionExplanation(number1,number2)        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, %s &nbsp;+&nbsp; %s &nbsp;=&nbsp; %d</font>"%(number1,number2,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain


    def GenerateProblemType2(self):       
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

        self.problem = "Find the missing number in the box.<br><br><table border=0><tr><td></td>"
        
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
            
        self.problem = self.problem + "</tr><tr><td>+</td>"
        
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
        
        self.sum = str(int(self.number1) + int(self.number2))
                
        if self.flag == 3:
            self.MissingDigit = randint(0,len(self.digits1)-1) 
            for i in range(len(self.digits1)):
                if i == self.MissingDigit:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
                    self.answer = self.sum[i:i+1]
                else:
                    self.problem = self.problem + "<td>"+str(self.sum)[i:i+1]+"</td>"
        else:
            for i in range(len(self.digits1)):
                self.problem = self.problem + "<td>"+str(self.sum)[i:i+1]+"</td>"            

        self.problem = self.problem + "</tr></table>"
                   
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.flag,self.number1,self.number2,self.sum)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType2(self,problem,answer,flag,number1,number2,total):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        if flag==1:
            self.solution_text = "<font class='ExplanationFont'>? &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d</font><br><br>"%(int(number2),int(total))
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; ?</font><br><br>"%(int(total),int(number2))
            self.solution_text = self.solution_text + self.SubtractionExplanation(int(total),int(number2))
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>The missing digit is: %s</font>"%(answer)
        elif flag==2:
            self.solution_text = "<font class='ExplanationFont'>%d &nbsp;+&nbsp; ? &nbsp;=&nbsp; %d</font><br><br>"%(int(number1),int(total))
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; ?</font><br><br>"%(int(total),int(number1))
            self.solution_text = self.solution_text + self.SubtractionExplanation(int(total),int(number1))
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>The missing digit is: %s</font>"%(answer)
        else:
            self.solution_text = "<font class='ExplanationFont'>%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; ?</font><br><br>"%(int(number1),int(number2))
            self.solution_text = self.solution_text + self.AdditionExplanation(int(number1),int(number2))
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>The missing digit is: %s</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text                
        
        return self.explain

    def GenerateProblemType3a(self):       
        '''e.g.:
        <An amusement park> received 1489 <visitors> on <Saturday> and 2489 <visitors> on <Sunday>. How many <visitors> did it receive on the two days altogether?'''

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
            
        self.items = [['An amusement park','visitors','Saturday','Sunday'],['A water park','visitors','Saturday','Sunday'],['A theme park','visitors','Saturday','Sunday'],['An animal safari park','visitors','Saturday','Sunday'],['A bird park','visitors','Saturday','Sunday'],['A zoo','visitors','Saturday','Sunday'],['A science museum','visitors','Saturday','Sunday'],['A shopping mall','shoppers','Saturday','Sunday'],['A cinema','moviegoers','Saturday','Sunday'],['A carnival','visitors','Saturday','Sunday']]
        self.days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        
        self.item = random.choice(self.items)
        
        self.Day1Index = randint(0,6)
        if self.Day1Index == 6:
            self.Day2Index = 0
        else:
            self.Day2Index = self.Day1Index + 1 
        
        self.problem = "%s received %d %s on %s and %d %s on %s. How many %s did it receive on the two days altogether?"%(self.item[0],self.number1,self.item[1],self.days[self.Day1Index],
                                                                                                                          self.number2,self.item[1],self.days[self.Day2Index],
                                                                                                                          self.item[1])
        
        self.answer = self.number1 + self.number2
        
        self.unit = self.item[1]
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.item[1],"on the two days",self.days[self.Day1Index],self.days[self.Day2Index],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit}

    def GenerateProblemType3b(self):       
        '''e.g.:
        <An art museum> received 1489 <visitors> in <March> and 2489 <visitors> in <April>. How many <visitors> did it receive in the two months altogether?'''

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

        if self.number1 < self.number2: #to ensure that the first number is always bigger for display's sake
            temp = self.number2
            self.number2 = self.number1
            self.number1 = temp
            
        self.items = [['An art museum','visitors','March','April'],['A vegetable farm','visitors','March','April'],['A strawberry farm','visitors','March','April'],['An animal farm','visitors','March','April'],['A grocery store','shoppers','March','April'],['A minimart','customers','March','April'],['A hotel','guests','March','April'],['A restaurant','guests','March','April'],['An airport','passengers','March','April'],['A post office','customers','March','April']]
        self.months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        
        self.item = random.choice(self.items)
        
        self.Month1Index = randint(0,10)
        self.Month2Index = self.Month1Index + 1 
        
        self.problem = "%s received %d %s in %s and %d %s in %s. How many %s did it receive in the two months altogether?"%(self.item[0],self.number1,self.item[1],self.months[self.Month1Index],
                                                                                                                          self.number2,self.item[1],self.months[self.Month2Index],
                                                                                                                          self.item[1])
        
        self.answer = self.number1 + self.number2
        
        self.unit = self.item[1]
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.item[1],"in the two months",self.months[self.Month1Index],self.months[self.Month2Index],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit}

    def ExplainType3(self,problem,answer,number1,number2,item1,endText,time1,time2,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)

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
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td></tr>"%(item1,self.color1,time1,self.color2,time2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.AdditionExplanation(number1, number2)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>It received %d %s %s altogether.</font>"%(answer,item1,endText)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        <A primary school has> 2658 <pupils>. <A secondary school has> 1239 <pupils>. What is the total number of <pupils in the two schools>?'''

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

        if self.number1 < self.number2: #to ensure that the first number is always bigger for display's sake
            temp = self.number2
            self.number2 = self.number1
            self.number1 = temp
            
        self.items = [['A primary school has','pupils','A secondary school has','pupils in the two schools','pupils','primary school','secondary school'],
                      ['A town has','residents','Its neighbouring town has','residents in the two towns','residents','town 1','town 2'],
                      ['A clothes company employs','workers','A shoes company employs','workers in the two companies','workers','clothes company','shoes company'],
                      ['A fish tank has','fishes','Another fish tank has','fishes in the two fish tanks','fishes','fish tank 1','fish tank 2'],
                      ['A national park has','trees','Another national park has','trees in the two national parks','trees','park 1','park 2'],
                      ['A wildlife sanctuary has','animals','Another wildlife sanctuary has','animals in the two wildlife sanctuaries','animals','sanctuary 1','sanctuary 2'],
                      ['A science college enrols','students','A management college enrols','students enrolled in the two colleges','students','science college','management college'],
                      ['A school library carries','books','A public library carries','books in the two libraries','books','school library','public library'],
                      ['Warehouse A can store','computers','Warehouse B can store','computers in the two warehouses','computers','Warehouse A','Warehouse B'],
                      ['A bookstore in a school carries','pens','A bookstore in a shopping centre carries','pens carried by the two bookstores','pens','bookstore 1','bookstore 2'],
                      ['A toys shop in a mall sold','toys','Another toys shop in the mall sold','toys sold by the two toys shops','toys','shop 1','shop 2'],
                      ['Grocery Store A sold','cans of milk','Grocery Store B sold','cans of milk sold by the two grocery stores','cans of milk','Store A','Store B'],
                      ['Farmer A sold','eggs','Farmer B sold','eggs sold by the two farmers','eggs','Farmer A','Farmer B'],
                      ['An art museum has','items on display','A science museum','items that the two museums have on display','items','art museum','science museum'],
                      ['A movie rental store carries','movie CDs','Another movie rental store carries','movie CDs that the two stores carry','movie CDs','store 1','store 2'],
                      ['Bakery A sold','muffins','Bakery B sold','muffins sold by the two bakeries','muffins','Bakery A','Bakery B'],
                      ['Ship A has','passengers','Ship B has','passengers on the two ships','passengers','Ship A','Ship B']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %d %s. %s %d %s. What is the total number of %s?"%(self.item[0],self.number1,self.item[1],
                                                                              self.item[2],self.number2,self.item[1],
                                                                              self.item[3])
        
        self.answer = self.number1 + self.number2
        
        self.unit = self.item[1]
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.item[3],self.item[4],self.item[5],self.item[6],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit}

    def ExplainType4(self,problem,answer,number1,number2,item3,item4,item5,item6,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)

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
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td></tr>"%(item4,self.color1,item5,self.color2,item6)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model
        
        self.solution_text = self.solution_text + self.AdditionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>There are %d %s.</font>"%(answer,item3)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        [Person.Unclename] <has> $1239 <in his bank account>. [Person.Auntyname] <has> $1239 <in her bank account>. <What is the total sum of money they have in their bank accounts?>'''

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

        if self.number1 < self.number2: #to ensure that the first number is always bigger for display's sake
            temp = self.number2
            self.number2 = self.number1
            self.number1 = temp
            
        self.names = [random.choice(PersonName.UncleName)] + [random.choice(PersonName.AuntyName)]
            
        self.items = [['has','in his bank account','in her bank account','What is the total sum of money they have in their bank accounts?','They have','in their bank accounts'],
                      ['earned','last month','last month','How much did they earn altogether last month?','They earned','altogether last month'],
                      ['spent','on himself','on herself','What is the total sum of money they spent on themselves?','They spent a total of','on themselves'],
                      ['donated',"to a kids' charity",'to a food bank','What is the total amount of money donated by the two people?','They donated',''],
                      ['had','in his savings account','in her savings account','What is the sum of money they had in their savings accounts altogether?','They had','in their savings accounts altogether'],
                      ['paid','in his travel expenses','in her travel expenses','How much money did they pay in their travel expenses altogether?','They paid','in their travel expenses altogether'],
                      ['won','in a lottery','in a lotto','What is the sum of money they won altogether?','They won','altogether'],
                      ['donated','to a library','to the same library','What is the sum of money the library received from the two donors?','The library received','from the two donors'],
                      ['spent','on air tickets for his holiday','on air tickets for her holiday','How much money did they spend altogether on air tickets for their holidays?','They spent','altogether on air tickets for their holidays'],
                      ['received','as a bonus','as a bonus','What is the sum of money they received altogether in bonuses?','They received','altogether in bonuses']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %s $%d %s. %s %s $%d %s. %s"%(self.names[0],self.item[0],self.number1,self.item[1],
                                                         self.names[1],self.item[0],self.number2,self.item[2],
                                                         self.item[3])
        
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.item[4],self.item[5],self.names)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def ExplainType5(self,problem,answer,number1,number2,item4,item5,names):
        self.answer_text = "<br>The correct answer is:<br>$%s"%(str(answer))

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
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td><td>$%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td></tr>"%(self.color1,names[0],self.color2,names[1])
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.AdditionExplanation(number1, number2)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s $%d %s.</font>"%(item4,answer,item5)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6a(self):       
        '''e.g.:
        [Person.Girlname] <had> 5224 <beads> and 2025 <marbles>. How many <beads> and <marbles> did she <have> altogether?'''

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
            
        self.name = random.choice(PersonName.GirlName)
            
        self.items = [['had','beads','marbles','have'],['collected','stamps','stickers','collect'],['had','rubberbands','buttons','have'],
                      ['bought','buttons','rubberbands','buy'],['won','points','stars','win'],['had','paper clips','push pins','have'],
                      ['bought','stickers','stamps','buy'],['collected','flags','stamps','collect'],['got','marbles','magnets','get'],
                      ['had','tacks','ice-cream sticks','have']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %s %d %s and %d %s. How many %s and %s did she %s altogether?"%(self.name,self.item[0],self.number1,self.item[1],
                                                                                           self.number2,self.item[2],self.item[1],self.item[2],self.item[3]) 
                
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6ab(self.problem,self.answer,self.number1,self.number2,"She",self.item[0],self.item[1],self.item[2],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def GenerateProblemType6b(self):       
        '''e.g.:
        [Person.name] <had> 5224 <beads> and [Person.name] <had> 2025 <marbles>. How many <beads> and <marbles> did they <have> altogether?'''

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
            
        self.names = random.sample(PersonName.PersonName,2)
            
        self.items = [['had','beads','marbles','have'],['collected','stamps','stickers','collect'],['had','rubberbands','buttons','have'],
                      ['bought','buttons','rubberbands','buy'],['won','points','stars','win'],['had','paper clips','push pins','have'],
                      ['bought','stickers','stamps','buy'],['collected','flags','stamps','collect'],['got','marbles','magnets','get'],
                      ['had','tacks','ice-cream sticks','have']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %s %d %s and %s %s %d %s. How many %s and %s did they %s altogether?"%(self.names[0],self.item[0],self.number1,self.item[1],
                                                                                                  self.names[1],self.item[0],self.number2,self.item[2],
                                                                                                  self.item[1],self.item[2],self.item[3]) 
                
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6ab(self.problem,self.answer,self.number1,self.number2,"They",self.item[0],self.item[1],self.item[2],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def ExplainType6ab(self,problem,answer,number1,number2,sheOrThey,item0,item1,item2,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)

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
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td></tr>"%(self.color1,item1,self.color2,item2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.AdditionExplanation(number1, number2)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s %s %d %s and %s altogether.</font>"%(sheOrThey,item0,answer,item1,item2)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6c(self):       
        '''e.g.:
        [Person.Boyname 1] collected 5224 <marbles>. [Person.Boyname 2] collected 2028 <marbles>. How many <marbles> did the two boys collect altogether?'''

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
            
        self.names = random.sample(PersonName.BoyName,2)
            
        self.items = ['marbles','stamps','stickers','flags','rubberbands','coins','keyrings','darts','animal cards','cards']

        self.item = random.choice(self.items)
               
        self.problem = "%s collected %d %s. %s collected %d %s. How many %s did the two boys collect altogether?"%(self.names[0],self.number1,self.item,
                                                                                                                   self.names[1],self.number2,self.item,
                                                                                                                   self.item) 
                
        self.answer = self.number1 + self.number2
        
        self.unit = self.item
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6c(self.problem,self.answer,self.number1,self.number2,self.item,self.names,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def ExplainType6c(self,problem,answer,number1,number2,item,names,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)

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
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td></tr>"%(item,self.color1,names[0],self.color2,names[1])
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.AdditionExplanation(number1, number2)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>They collected %d %s altogether.</font>"%(answer,item)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        <A grocery store sold> 2904 <chicken eggs> and 1290 <duck eggs>. How many <eggs did the grocery store sell> altogether?'''

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
            
        self.items = [['A grocery store sold','chicken eggs','duck eggs','eggs did the grocery store sell','The grocery store sold','eggs'],
                      ['A fruit vendor had','pears','mangoes','fruits did the fruit vendor have','The fruit vendor had','fruits'],
                      ['A farmer had','hens','ducks','birds did the farmer have','The farmer had','birds'],
                      ['A phone shop sold','SIM cards','calling cards','cards did the phone shop sell','The phone shop sold','cards'],
                      ['A post office sold','envelopes','stamps','envelopes and stamps did the post office sell','The post office sold','envelopes and stamps'],
                      ['A supermarket had','bags of rice flour','bags of icing sugar','bags of rice flour and icing sugar did the supermarket have','The supermarket had','bags of rice flour and icing sugar'],
                      ['An amusement park received','adults','children','people did the amusement park receive','The amusement park received','people'],
                      ['A school had','boys','girls','children did the school have','The school had','children'],
                      ['A library carried','books','DVDs','books and DVDs did the library carry','The library carried','books and DVDs'],
                      ['A baker baked','cupcakes','muffins','cupcakes and muffins did the baker bake','The baker baked','cupcakes and muffins'],
                      ['A hawker centre sold','plates of rice','bowls of soup','plates of rice and bowls of soup did the hawker centre sell','The hawker centre sold','plates of rice and bowls of soup']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %d %s and %d %s. How many %s altogether?"%(self.item[0],self.number1,self.item[1],self.number2,self.item[2],self.item[3]) 
                
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.item[1],self.item[2],self.item[4],self.item[5],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def ExplainType7(self,problem,answer,number1,number2,item1,item2,item4,item5,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)

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
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td></tr>"%(self.color1,item1,self.color2,item2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.AdditionExplanation(number1, number2)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s %d %s altogether.</font>"%(item4,answer,item5)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        <After> 1239 <birds migrated out of a village, there were> 8467 <birds left in the village>. How many <birds were there in the village> at first?'''

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
            
        self.items = [['After','birds migrated from a village, there were','birds left in the village','birds were there in the village','There were','birds in the village at first'],
                      ['After','people moved from the village to the town, there were','people left in the village','people were there in the village','There were','people in the village at first'],
                      ['After selling','buns, there were','buns left','buns were there','There were','buns at first'],
                      ['After','children left the school hall for their classrooms, there were','children left in the school hall','children were there in the school hall','There were','children in the school hall at first'],
                      ['After','workers completed their shifts at the factory, there were','workers left in the factory','workers were there in the factory','There were','workers in the factory at first'],
                      ['After sharing','of his stamps, the boy had','stamps left','stamps did the boy have','The boy had','stamps at first'],
                      ['After','spectators left a stadium, there were','spectators left in the stadium','spectators were there in the stadium','There were','spectators in the stadium at first'],
                      ['After','travelers left the airport, there were','travelers left at the airport','travelers were there at the airport','There were','travelers at the airport at first'],
                      ['After','passengers got off the train, there were','passengers left on the train','passengers were there on the train','There were','passengers on the train at first'],
                      ['After losing','of his marbles, the boy had','marbles left','marbles did the boy have','The boy had','marbles at first']]


        self.item = random.choice(self.items)
               
        self.problem = "%s %d %s %d %s. How many %s at first?"%(self.item[0],self.number1,self.item[1],self.number2,self.item[2],self.item[3]) 
                
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2,self.item[4],self.item[5],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def ExplainType8(self,problem,answer,number1,number2,item4,item5,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)

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
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>at first</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.AdditionExplanation(number1, number2)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s %d %s.</font>"%(item4,answer,item5)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        [Person.Unclename] bought a <computer> for $750 and a <printer> for $250. How much did he pay for the two items altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
            
        self.name = random.choice(PersonName.UncleName)
                    
        self.items = [['computer','printer',randint(500,1500),randint(100,400)],['sofa set','coffee table',randint(1000,3000),randint(200,800)],
                      ['bed frame','mattress',randint(500,1000),randint(500,2000)],['TV set','TV console',randint(500,1500),randint(500,1500)],
                      ['dining table set','recliner sofa',randint(500,2000),randint(500,2000)],['camera','printer',randint(500,1500),randint(100,400)],
                      ['book shelf','table',randint(500,1000),randint(100,1000)],['home entertainment system','couch',randint(500,2000),randint(500,2000)],
                      ['laptop','smart phone',randint(700,2000),randint(200,800)]]

        self.item = random.choice(self.items)
               
        self.problem = "%s bought a %s for $%d and a %s for $%d. How much did he pay for the two items altogether?"%(self.name,self.item[0],self.item[2],
                                                                                                                     self.item[1],self.item[3]) 
        self.number1 = self.item[2]
        self.number2 = self.item[3]
        
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[1],self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,"dollar_unit":self.dollar_unit}

    def ExplainType9(self,problem,answer,number1,number2,item0,item1,unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s"%(unit,str(answer))

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
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td><td>$%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.7em'>%s</font></td></tr>"%(self.color1,item0,self.color2,item1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.AdditionExplanation(number1, number2)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>He paid $%d for the two items altogether.</font>"%(answer)

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
        
        if self.number1 < self.number2: #to ensure that the first number is always bigger for display's sake
            temp = self.number2
            self.number2 = self.number1
            self.number1 = temp

            
        self.problem1 = "Find the sum of %d and %d."%(self.number1,self.number2)
        self.problem2 = "What is the sum of %d and %d?"%(self.number1,self.number2)
        self.problem3 = "What is %d + %d?"%(self.number1,self.number2)
        self.problem4 = "The sum of %d and %d is _____."%(self.number1,self.number2)
        self.problem5 = "%d + %d = ?"%(self.number1,self.number2)
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])
        
        self.answer = self.number1 + self.number2
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.answer+100,self.answer-100,self.answer+10,self.answer-10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2)
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

        self.problem = "Add.<br><br><table><tr><td></td>"
        for i in range(len(self.digits1)):
            self.problem = self.problem + "<td>"+str(self.digits1[i])+"</td>"
        self.problem = self.problem + "</tr><tr><td style='text-align:right'>+</td>"
        
        if len(self.digits2) == 3:
            self.problem = self.problem +"<td></td>"
        for i in range(len(self.digits2)):
            self.problem = self.problem + "<td>"+str(self.digits2[i])+"</td>"            
        self.problem = self.problem + "</tr>"
        self.problem = self.problem + "<tr><td colspan=5 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line.png' /></td></tr>"
        self.problem = self.problem + "</table>"
        
        self.answer = int(self.number1) + int(self.number2)
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.answer+100,self.answer-100,self.answer+10,self.answer-10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ2(self):

        '''e.g.:
            Find the missing number.
              1 2 3 4
            + 2 3 4 _
            ---------
              3 5 7 8'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ2"
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

        self.problem = "Find the missing number in the box.<br><br><table><tr><td></td>"
        
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
            
        self.problem = self.problem + "</tr><tr><td>+</td>"
        
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
        
        self.sum = str(int(self.number1) + int(self.number2))
                
        if self.flag == 3:
            self.MissingDigit = randint(0,len(self.digits1)-1) 
            for i in range(len(self.digits1)):
                if i == self.MissingDigit:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
                    self.answer = self.sum[i:i+1]
                else:
                    self.problem = self.problem + "<td>"+str(self.sum)[i:i+1]+"</td>"
        else:
            for i in range(len(self.digits1)):
                self.problem = self.problem + "<td>"+str(self.sum)[i:i+1]+"</td>"            

        self.problem = self.problem + "</tr></table>"
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        
        for i in range(10):
            if i != int(self.answer):
                self.wrongAnswers.append(i)
                                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.flag,self.number1,self.number2,self.sum)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ3a(self):
        '''e.g.:
        <An amusement park> received 1489 <visitors> on <Saturday> and 2489 <visitors> on <Sunday>. How many <visitors> did it receive on the two days altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ3a"
        self.CheckAnswerType = 1


        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
        
        if self.number1 < self.number2: #to ensure that the first number is always bigger for display's sake
            temp = self.number2
            self.number2 = self.number1
            self.number1 = temp
            
        self.items = [['An amusement park','visitors','Saturday','Sunday'],['A water park','visitors','Saturday','Sunday'],['A theme park','visitors','Saturday','Sunday'],['An animal safari park','visitors','Saturday','Sunday'],['A bird park','visitors','Saturday','Sunday'],['A zoo','visitors','Saturday','Sunday'],['A science museum','visitors','Saturday','Sunday'],['A shopping mall','shoppers','Saturday','Sunday'],['A cinema','moviegoers','Saturday','Sunday'],['A carnival','visitors','Saturday','Sunday']]
        self.days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        
        self.item = random.choice(self.items)
        
        self.Day1Index = randint(0,6)
        if self.Day1Index == 6:
            self.Day2Index = 0
        else:
            self.Day2Index = self.Day1Index + 1 
        
        self.problem = "%s received %d %s on %s and %d %s on %s. How many %s did it receive on the two days altogether?"%(self.item[0],self.number1,self.item[1],self.days[self.Day1Index],
                                                                                                                          self.number2,self.item[1],self.days[self.Day2Index],
                                                                                                                          self.item[1])
        
        self.answer = self.number1 + self.number2
        
        self.unit = self.item[1]
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.answer+100,self.answer-100,self.answer+10,self.answer-10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.item[1],"on the two days",self.days[self.Day1Index],self.days[self.Day2Index],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ3b(self):
        '''e.g.:
        <An art museum> received 1489 <visitors> in <March> and 2489 <visitors> in <April>. How many <visitors> did it receive in the two months altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ3b"
        self.CheckAnswerType = 1


        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.items = [['An art museum','visitors','March','April'],['A vegetable farm','visitors','March','April'],['A strawberry farm','visitors','March','April'],['An animal farm','visitors','March','April'],['A grocery store','shoppers','March','April'],['A minimart','customers','March','April'],['A hotel','guests','March','April'],['A restaurant','guests','March','April'],['An airport','passengers','March','April'],['A post office','customers','March','April']]
        self.months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        
        self.item = random.choice(self.items)
        
        self.Month1Index = randint(0,10)
        self.Month2Index = self.Month1Index + 1 
        
        self.problem = "%s received %d %s in %s and %d %s in %s. How many %s did it receive in the two months altogether?"%(self.item[0],self.number1,self.item[1],self.months[self.Month1Index],
                                                                                                                          self.number2,self.item[1],self.months[self.Month2Index],
                                                                                                                          self.item[1])
        
        self.answer = self.number1 + self.number2
        
        self.unit = self.item[1]
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.answer+100,self.answer-100,self.answer+10,self.answer-10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.item[1],"in the two months",self.months[self.Month1Index],self.months[self.Month2Index],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ4(self):
        '''e.g.:
        <A primary school has> 2658 <pupils>. <A secondary school has> 1239 <pupils>. What is the total number of <pupils in the two schools>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ4"
        self.CheckAnswerType = 1


        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
        
        if self.number1 < self.number2: #to ensure that the first number is always bigger for display's sake
            temp = self.number2
            self.number2 = self.number1
            self.number1 = temp

        self.items = [['A primary school has','pupils','A secondary school has','pupils in the two schools','pupils','primary school','secondary school'],
                      ['A town has','residents','Its neighbouring town has','residents in the two towns','residents','town 1','town 2'],
                      ['A clothes company employs','workers','A shoes company employs','workers in the two companies','workers','clothes company','shoes company'],
                      ['A fish tank has','fishes','Another fish tank has','fishes in the two fish tanks','fishes','fish tank 1','fish tank 2'],
                      ['A national park has','trees','Another national park has','trees in the two national parks','trees','park 1','park 2'],
                      ['A wildlife sanctuary has','animals','Another wildlife sanctuary has','animals in the two wildlife sanctuaries','animals','sanctuary 1','sanctuary 2'],
                      ['A science college enrols','students','A management college enrols','students enrolled in the two colleges','students','science college','management college'],
                      ['A school library carries','books','A public library carries','books in the two libraries','books','school library','public library'],
                      ['Warehouse A can store','computers','Warehouse B can store','computers in the two warehouses','computers','Warehouse A','Warehouse B'],
                      ['A bookstore in a school carries','pens','A bookstore in a shopping centre carries','pens carried by the two bookstores','pens','bookstore 1','bookstore 2'],
                      ['A toys shop in a mall sold','toys','Another toys shop in the mall sold','toys sold by the two toys shops','toys','shop 1','shop 2'],
                      ['Grocery Store A sold','cans of milk','Grocery Store B sold','cans of milk sold by the two grocery stores','cans of milk','Store A','Store B'],
                      ['Farmer A sold','eggs','Farmer B sold','eggs sold by the two farmers','eggs','Farmer A','Farmer B'],
                      ['An art museum has','items on display','A science museum','items that the two museums have on display','items','art museum','science museum'],
                      ['A movie rental store carries','movie CDs','Another movie rental store carries','movie CDs that the two stores carry','movie CDs','store 1','store 2'],
                      ['Bakery A sold','muffins','Bakery B sold','muffins sold by the two bakeries','muffins','Bakery A','Bakery B'],
                      ['Ship A has','passengers','Ship B has','passengers on the two ships','passengers','Ship A','Ship B']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %d %s. %s %d %s. What is the total number of %s?"%(self.item[0],self.number1,self.item[1],
                                                                              self.item[2],self.number2,self.item[1],
                                                                              self.item[3])
        
        self.answer = self.number1 + self.number2
        
        self.unit = self.item[1]
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.answer+100,self.answer-100,self.answer+10,self.answer-10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.item[3],self.item[4],self.item[5],self.item[6],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ5(self):
        '''e.g.:
        [Person.Unclename] <has> $1239 <in his bank account>. [Person.Auntyname] <has> $1239 <in her bank account>. <What is the total sum of money they have in their bank accounts?>'''

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
            
        if self.number1 < self.number2: #to ensure that the first number is always bigger for display's sake
            temp = self.number2
            self.number2 = self.number1
            self.number1 = temp
            
        self.names = [random.choice(PersonName.UncleName)] + [random.choice(PersonName.AuntyName)]
            
        self.items = [['has','in his bank account','in her bank account','What is the total sum of money they have in their bank accounts?','They have','in their bank accounts'],
                      ['earned','last month','last month','How much did they earn altogether last month?','They earned','altogether last month'],
                      ['spent','on himself','on herself','What is the total sum of money they spent on themselves?','They spent a total of','on themselves'],
                      ['donated',"to a kids' charity",'to a food bank','What is the total amount of money donated by the two people?','They donated',''],
                      ['had','in his savings account','in her savings account','What is the sum of money they had in their savings accounts altogether?','They had','in their savings accounts altogether'],
                      ['paid','in his travel expenses','in her travel expenses','How much money did they pay in their travel expenses altogether?','They paid','in their travel expenses altogether'],
                      ['won','in a lottery','in a lotto','What is the sum of money they won altogether?','They won','altogether'],
                      ['donated','to a library','to the same library','What is the sum of money the library received from the two donors?','The library received','from the two donors'],
                      ['spent','on air tickets for his holiday','on air tickets for her holiday','How much money did they spend altogether on air tickets for their holidays?','They spent','altogether on air tickets for their holidays'],
                      ['received','as a bonus','as a bonus','What is the sum of money they received altogether in bonuses?','They received','altogether in bonuses']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %s $%d %s. %s %s $%d %s. %s"%(self.names[0],self.item[0],self.number1,self.item[1],
                                                         self.names[1],self.item[0],self.number2,self.item[2],
                                                         self.item[3])
        
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.answer+100,self.answer-100,self.answer+10,self.answer-10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.item[4],self.item[5],self.names)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ6a(self):
        '''e.g.:
        [Person.Girlname] <had> 5224 <beads> and 2025 <marbles>. How many <beads> and <marbles> did she <have> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ6a"
        self.CheckAnswerType = 1


        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.name = random.choice(PersonName.GirlName)
            
        self.items = [['had','beads','marbles','have'],['collected','stamps','stickers','collect'],['had','rubberbands','buttons','have'],
                      ['bought','buttons','rubberbands','buy'],['won','points','stars','win'],['had','paper clips','push pins','have'],
                      ['bought','stickers','stamps','buy'],['collected','flags','stamps','collect'],['got','marbles','magnets','get'],
                      ['had','tacks','ice-cream sticks','have']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %s %d %s and %d %s. How many %s and %s did she %s altogether?"%(self.name,self.item[0],self.number1,self.item[1],
                                                                                           self.number2,self.item[2],self.item[1],self.item[2],self.item[3]) 
                
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = ""
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.answer+100,self.answer-100,self.answer+10,self.answer-10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6ab(self.problem,self.answer,self.number1,self.number2,"She",self.item[0],self.item[1],self.item[2],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ6b(self):
        '''e.g.:
        [Person.name] <had> 5224 <beads> and [Person.name] <had> 2025 <marbles>. How many <beads> and <marbles> did they <have> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ6b"
        self.CheckAnswerType = 1


        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.names = random.sample(PersonName.PersonName,2)
            
        self.items = [['had','beads','marbles','have'],['collected','stamps','stickers','collect'],['had','rubberbands','buttons','have'],
                      ['bought','buttons','rubberbands','buy'],['won','points','stars','win'],['had','paper clips','push pins','have'],
                      ['bought','stickers','stamps','buy'],['collected','flags','stamps','collect'],['got','marbles','magnets','get'],
                      ['had','tacks','ice-cream sticks','have']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %s %d %s and %s %s %d %s. How many %s and %s did they %s altogether?"%(self.names[0],self.item[0],self.number1,self.item[1],
                                                                                                  self.names[1],self.item[0],self.number2,self.item[2],
                                                                                                  self.item[1],self.item[2],self.item[3]) 
                
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = ""
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.answer+100,self.answer-100,self.answer+10,self.answer-10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6ab(self.problem,self.answer,self.number1,self.number2,"They",self.item[0],self.item[1],self.item[2],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ6c(self):
        '''e.g.:
        [Person.Boyname 1] collected 5224 <marbles>. [Person.Boyname 2] collected 2028 <marbles>. How many <marbles> did the two boys collect altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ6c"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.names = random.sample(PersonName.BoyName,2)
            
        self.items = ['marbles','stamps','stickers','flags','rubberbands','coins','keyrings','darts','animal cards','cards']

        self.item = random.choice(self.items)
               
        self.problem = "%s collected %d %s. %s collected %d %s. How many %s did the two boys collect altogether?"%(self.names[0],self.number1,self.item,
                                                                                                                   self.names[1],self.number2,self.item,
                                                                                                                   self.item) 
                
        self.answer = self.number1 + self.number2
        
        self.unit = self.item
        self.dollar_unit = ""
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.answer+100,self.answer-100,self.answer+10,self.answer-10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6c(self.problem,self.answer,self.number1,self.number2,self.item,self.names,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ7(self):
        '''e.g.:
        <A grocery store sold> 2904 <chicken eggs> and 1290 <duck eggs>. How many <eggs did the grocery store sell> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ7"
        self.CheckAnswerType = 1


        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.items = [['A grocery store sold','chicken eggs','duck eggs','eggs did the grocery store sell','The grocery store sold','eggs'],
                      ['A fruit vendor had','pears','mangoes','fruits did the fruit vendor have','The fruit vendor had','fruits'],
                      ['A farmer had','hens','ducks','birds did the farmer have','The farmer had','birds'],
                      ['A phone shop sold','SIM cards','calling cards','cards did the phone shop sell','The phone shop sold','cards'],
                      ['A post office sold','envelopes','stamps','envelopes and stamps did the post office sell','The post office sold','envelopes and stamps'],
                      ['A supermarket had','bags of rice flour','bags of icing sugar','bags of rice flour and icing sugar did the supermarket have','The supermarket had','bags of rice flour and icing sugar'],
                      ['An amusement park received','adults','children','people did the amusement park receive','The amusement park received','people'],
                      ['A school had','boys','girls','children did the school have','The school had','children'],
                      ['A library carried','books','DVDs','books and DVDs did the library carry','The library carried','books and DVDs'],
                      ['A baker baked','cupcakes','muffins','cupcakes and muffins did the baker bake','The baker baked','cupcakes and muffins'],
                      ['A hawker centre sold','plates of rice','bowls of soup','plates of rice and bowls of soup did the hawker centre sell','The hawker centre sold','plates of rice and bowls of soup']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %d %s and %d %s. How many %s altogether?"%(self.item[0],self.number1,self.item[1],self.number2,self.item[2],self.item[3]) 
                
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = ""
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.answer+100,self.answer-100,self.answer+10,self.answer-10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.item[1],self.item[2],self.item[4],self.item[5],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ8(self):
        '''e.g.:
        <After> 1239 <birds migrated out of a village, there were> 8467 <birds left in the village>. How many <birds were there in the village> at first?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ8"
        self.CheckAnswerType = 1

        self.flag = randint(1,10)
        
        if self.flag <9:
            self.number1 = randint(1000,8888)
            self.sum = randint(self.number1+1000,9999)
            self.number2 = self.sum - self.number1
        else:
            self.number1 = randint(100,900)
            self.number2 = randint(100,900)
            
        self.items = [['After','birds migrated from a village, there were','birds left in the village','birds were there in the village','There were','birds in the village at first'],
                      ['After','people moved from the village to the town, there were','people left in the village','people were there in the village','There were','people in the village at first'],
                      ['After selling','buns, there were','buns left','buns were there','There were','buns at first'],
                      ['After','children left the school hall for their classrooms, there were','children left in the school hall','children were there in the school hall','There were','children in the school hall at first'],
                      ['After','workers completed their shifts at the factory, there were','workers left in the factory','workers were there in the factory','There were','workers in the factory at first'],
                      ['After sharing','of his stamps, the boy had','stamps left','stamps did the boy have','The boy had','stamps at first'],
                      ['After','spectators left a stadium, there were','spectators left in the stadium','spectators were there in the stadium','There were','spectators in the stadium at first'],
                      ['After','travelers left the airport, there were','travelers left at the airport','travelers were there at the airport','There were','travelers at the airport at first'],
                      ['After','passengers got off the train, there were','passengers left on the train','passengers were there on the train','There were','passengers on the train at first'],
                      ['After losing','of his marbles, the boy had','marbles left','marbles did the boy have','The boy had','marbles at first']]


        self.item = random.choice(self.items)
               
        self.problem = "%s %d %s %d %s. How many %s at first?"%(self.item[0],self.number1,self.item[1],self.number2,self.item[2],self.item[3]) 
                
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = ""
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.answer+100,self.answer-100,self.answer+10,self.answer-10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2,self.item[4],self.item[5],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ9(self):
        '''e.g.:
        [Person.Unclename] bought a <computer> for $750 and a <printer> for $250. How much did he pay for the two items altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ9"
        self.CheckAnswerType = 1

            
        self.name = random.choice(PersonName.UncleName)
                    
        self.items = [['computer','printer',randint(500,1500),randint(100,400)],['sofa set','coffee table',randint(1000,3000),randint(200,800)],
                      ['bed frame','mattress',randint(500,1000),randint(500,2000)],['TV set','TV console',randint(500,1500),randint(500,1500)],
                      ['dining table set','recliner sofa',randint(500,2000),randint(500,2000)],['camera','printer',randint(500,1500),randint(100,400)],
                      ['book shelf','table',randint(500,1000),randint(100,1000)],['home entertainment system','couch',randint(500,2000),randint(500,2000)],
                      ['laptop','smart phone',randint(700,2000),randint(200,800)]]

        self.item = random.choice(self.items)
               
        self.problem = "%s bought a %s for $%d and a %s for $%d. How much did he pay for the two items altogether?"%(self.name,self.item[0],self.item[2],
                                                                                                                     self.item[1],self.item[3]) 
        self.number1 = self.item[2]
        self.number2 = self.item[3]
        
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.answer+100,self.answer-100,self.answer+10,self.answer-10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[1],self.dollar_unit)
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