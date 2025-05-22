'''
Created on Oct 06, 2011

Module: FindAverage
Generates "Finding the average" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random
from random import randint
from Problems import PersonName

class FindAverage:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"easy":[self.GenerateProblemType1(),
                                    self.GenerateProblemTypeMCQ1()],
                            "medium":[self.GenerateProblemType2(),
                            self.GenerateProblemTypeMCQ2()],
                            }
        try:
            return random.choice(self.ProblemType[level])
        except KeyError:
            return random.choice(random.choice(self.ProblemType.values()))
        #return self.GenerateProblemTypeMCQ2() 
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3a","ProblemTypeMCQ3a","ProblemType3b","ProblemTypeMCQ3b",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType5","ProblemTypeMCQ5",],
                            6:["ProblemType6","ProblemTypeMCQ6",],
                            7:["ProblemType7","ProblemTypeMCQ7",],
                            8:["ProblemType8a","ProblemTypeMCQ8a","ProblemType8b","ProblemTypeMCQ8b",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3a(),self.GenerateProblemTypeMCQ3a(),self.GenerateProblemType3b(),self.GenerateProblemTypeMCQ3b(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemType5(),self.GenerateProblemTypeMCQ5(),],
                                    6:[self.GenerateProblemType6(),self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemType7(),self.GenerateProblemTypeMCQ7(),],
                                    8:[self.GenerateProblemType8a(),self.GenerateProblemTypeMCQ8a(),self.GenerateProblemType8b(),self.GenerateProblemTypeMCQ8b(),],
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
        #return self.GenerateProblemType2()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3a":self.GenerateProblemType3a(),
                            "ProblemType3b":self.GenerateProblemType3b(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8a":self.GenerateProblemType8a(),
                            "ProblemType8b":self.GenerateProblemType8b(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3a":self.GenerateProblemTypeMCQ3a(),
                            "ProblemTypeMCQ3b":self.GenerateProblemTypeMCQ3b(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),
                            "ProblemTypeMCQ8a":self.GenerateProblemTypeMCQ8a(),
                            "ProblemTypeMCQ8b":self.GenerateProblemTypeMCQ8b(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g.:
        Find the average of the given numbers. (Write your answer correct up to 2 decimal places)'''
        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.number1 = randint(0,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.ProblemSelection = randint(1,3)
        self.problem1 = "Find the average of the numbers given below:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem2 = "Find the average of the following set of numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem3 = "For the following, find the average.<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem4 = "What is the average of the following set?<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4]) 
        if self.ProblemSelection == 1:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.problem = self.problem + str(self.number1)+", "+str(self.number2)+", "+str(self.number3)+"<br>"
            self.answer = (self.number1 + self.number2 + self.number3)/3
            self.flag = 1
        elif self.ProblemSelection == 2:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.problem = self.problem + str(self.number1)+", "+str(self.number2)+", "+str(self.number3)+", "+str(self.number4)+"<br>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4)/4
            self.flag = 2
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.problem = self.problem + str(self.number1)+", "+str(self.number2)+", "+str(self.number3)+", "+str(self.number4)+", "+str(self.number5)+"<br>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5
            self.flag = 3                    
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}
    
    def ExplainType1(self,problem,answer,number1,number2,number3,number4,number5,flag):
        self.answer_text = "The correct answer is:<br>"+str(answer)
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average of a set of data</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>Sum of the data</u><br>Number of data</td></tr></table>"
        if flag == 1:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Sum of the data</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1+number2+number3)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of data</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average of the set</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+str(number1+number2+number3)+"</u><br>3</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+str(answer)+"</td></tr></table>"
        elif flag == 2:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Sum of the data</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+" + "+str(number4)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1+number2+number3+number4)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of data</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>4</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average of the set</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+str(number1+number2+number3+number4)+"</u><br>4</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+str(answer)+"</td></tr></table>"
        elif flag == 3:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Sum of the data</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+" + "+str(number4)+" + "+str(number5)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1+number2+number3+number4+number5)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of data</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>5</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average of the set</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+str(number1+number2+number3+number4+number5)+"</u><br>5</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Data-Analysis/Finding-Average" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.:
        Find the average of the given numbers. (Write your answer correct up to 1 decimal place)'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(0,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.ProblemSelection = randint(1,3)
        self.UnitSelection = randint(1,10)
        self.dollar = ""
        self.unit = ""
        if self.UnitSelection == 7 or self.UnitSelection == 8:
            self.dollar = "$"
        elif self.UnitSelection == 9 or self.UnitSelection == 10:
            self.unit = random.choice(["m","cm","km","kg"])
        self.problem1 = "Find the average of the set given below correct to the nearest tenth:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem2 = "Find the average of the following set. Write your answer correct to the nearest tenth.<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem3 = "For the following, find the average. Give your answer correct to 1 decimal place.<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem4 = "What is the average of the following set correct to 1 decimal place?<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4]) 
        if self.ProblemSelection == 1:
            self.problem = self.problem + self.dollar+str(self.number1)+" "+self.unit+", "+self.dollar+str(self.number2)+" "+self.unit+", "+self.dollar+str(self.number3)+" "+self.unit+"<br>"
            self.answer = round(float(self.number1 + self.number2 + self.number3)/3,1)
            self.flag = 1
        elif self.ProblemSelection == 2:
            self.problem = self.problem + self.dollar+str(self.number1)+" "+self.unit+", "+self.dollar+str(self.number2)+" "+self.unit+", "+self.dollar+str(self.number3)+" "+self.unit+", "+self.dollar+str(self.number4)+" "+self.unit+"<br>"
            self.answer = round(float(self.number1 + self.number2 + self.number3 + self.number4)/4,1)
            self.flag = 2
        else:
            self.problem = self.problem + self.dollar+str(self.number1)+" "+self.unit+", "+self.dollar+str(self.number2)+" "+self.unit+", "+self.dollar+str(self.number3)+" "+self.unit+", "+self.dollar+str(self.number4)+" "+self.unit+", "+self.dollar+str(self.number5)+" "+self.unit+"<br>"
            self.answer = round(float(self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5,1)
            self.flag = 3                    
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.dollar,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':2,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"dollar_unit":self.dollar,"unit":self.unit}
    
    def ExplainType2(self,problem,answer,number1,number2,number3,number4,number5,flag,dollar,unit):
        self.answer_text = "The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average of a set of data</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>Sum of the data</u><br>Number of data</td></tr></table>"
        if flag == 1:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Sum of the data</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1)+" "+unit+" + "+dollar+str(number2)+" "+unit+" + "+dollar+str(number3)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1+number2+number3)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of data</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average of the set</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+dollar+str(number1+number2+number3)+" "+unit+"</u><br>3</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+dollar+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 2:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Sum of the data</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+" + "+str(number4)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1+number2+number3+number4)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of data</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>4</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average of the set</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+dollar+str(number1+number2+number3+number4)+" "+unit+"</u><br>4</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+dollar+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 3:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Sum of the data</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+" + "+str(number4)+" + "+str(number5)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1+number2+number3+number4+number5)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of data</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>5</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average of the set</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+dollar+str(number1+number2+number3+number4+number5)+" "+unit+"</u><br>5</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+dollar+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Data-Analysis/Finding-Average" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3a(self):
        '''e.g.:
        [Person.name] had <number> bags of [marbles]. The table below shows the number of [marbles] in the <number> bags.'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.item = random.choice(['marbles','beads','shells','forks','spoons','plates','rubberbands','apples','oranges','pears',
                     'peaches','potatoes','guavas','kiwifruits','candies','coasters','straws']) 
        
        self.problem1 = self.name + " had "+str(self.NumberOfItem)+" bags of "+self.item+". The table below shows the number of "+self.item+" in the "+str(self.NumberOfItem)+" bags.<br><br>"
        self.problem2 = "The table below shows the number of "+self.item+" that "+self.name + " had in "+str(self.NumberOfItem)+" bags.<br><br>"
        
        self.problem = random.choice([self.problem1,self.problem2])
        self.problem = self.problem + "<table class='Reports'><tr><td style='background-color:#307554;color:#fff;'>Bag</td>"
        for i in range(self.NumberOfItem):
            self.problem = self.problem + "<td>Bag "+str(i+1)+"</td>"
        self.problem = self.problem + "</tr><tr><td style='background-color:#307554;color:#fff;'>"+self.item.capitalize()+"</td>"
        for i in range(self.NumberOfItem-1):
            self.problem = self.problem + "<td>"+str(self.numbers[i])+"</td>"
        
        if self.NumberOfItem == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.problem = self.problem + "<td>"+str(self.number3)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3)/3
            self.flag = 1
        elif self.NumberOfItem == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.problem = self.problem + "<td>"+str(self.number4)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4)/4
            self.flag = 2
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.problem = self.problem + "<td>"+str(self.number5)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5
            self.flag = 3                    

        self.problem = self.problem + "</tr></table>"
        self.question1 = "<br>What was the average number of "+self.item+" in each bag?"
        self.question2 = "<br>Find the average number of "+self.item+" in each bag."
        self.question = random.choice([self.question1,self.question2])
        self.problem = self.problem + self.question
        
        self.unit = self.item
        self.holder = "bag"
        self.holders = "bags"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.unit,self.holder,self.holders)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3a",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}
    
    def ExplainType3(self,problem,answer,number1,number2,number3,number4,number5,flag,unit,holder,holders):
        self.answer_text = "The correct answer is:<br>"+str(answer)
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average number of "+unit+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>Total number of "+unit+"</u><br>Number of "+holders+"</td></tr></table>"
        if flag == 1:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total number of "+unit+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1+number2+number3)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+holders+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average number of "+unit+" in each "+holder+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+str(number1+number2+number3)+"</u><br>3</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+str(answer)+"</td></tr></table>"
        elif flag == 2:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total number of "+unit+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+" + "+str(number4)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1+number2+number3+number4)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+holders+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>4</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average number of "+unit+" in each "+holder+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+str(number1+number2+number3+number4)+"</u><br>4</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+str(answer)+"</td></tr></table>"
        elif flag == 3:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total number of "+unit+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+" + "+str(number4)+" + "+str(number5)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1+number2+number3+number4+number5)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+holders+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>5</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average number of "+unit+" in each "+holder+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+str(number1+number2+number3+number4+number5)+"</u><br>5</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Data-Analysis/Finding-Average" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3b(self):
        '''e.g.:
        The table below shows the number of [pencils] in <number> boxes.'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.item = random.choice(['pencils', 'sharpeners', 'erasers', 'rulers', 'pens', 'crayons', 'highlighters', 'markers', 'cookies', 'bars of chocolate', 'cans of juice']) 
        
        self.problem = "The table below shows the number of "+self.item+" in "+str(self.NumberOfItem)+" boxes.<br><br>"
        self.problem = self.problem + "<table class='Reports'><tr><td style='background-color:#307554;color:#fff;'>Box</td>"
        for i in range(self.NumberOfItem):
            self.problem = self.problem + "<td>Box "+str(i+1)+"</td>"
        self.problem = self.problem + "</tr><tr><td style='background-color:#307554;color:#fff;'>"+self.item.capitalize()+"</td>"
        for i in range(self.NumberOfItem-1):
            self.problem = self.problem + "<td>"+str(self.numbers[i])+"</td>"
        
        if self.NumberOfItem == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.problem = self.problem + "<td>"+str(self.number3)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3)/3
            self.flag = 1
        elif self.NumberOfItem == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.problem = self.problem + "<td>"+str(self.number4)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4)/4
            self.flag = 2
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.problem = self.problem + "<td>"+str(self.number5)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5
            self.flag = 3                    

        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "<br>Find the average number of "+self.item+" in each box."
        
        self.unit = self.item
        self.holder = "box"
        self.holders = "boxes"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.unit,self.holder,self.holders)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3b",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def GenerateProblemType4(self):
        '''e.g.:
        [Person.name] spent a total of $<amount> on <number> different [books]. Find the average cost of the [books].'''
        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.number1 = randint(2,20)
        self.number2 = randint(2,20)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.dollar = "$"
        self.unit=""
        self.name = random.choice(PersonName.PersonName)
        self.item = random.choice(['books', 'toys', 'pens', 'rolls of coloured strings', 'water bottles', 'soccer balls', 'keychains', 'bracelets', 'plants']) 
        self.total = 0
        for i in range(self.NumberOfItem):
            self.total = self.total + self.numbers[i]
            
        self.problem1 = self.name + " spent a total of $"+str(self.total)+" on "+str(self.NumberOfItem)+" "+self.item+". Find the average cost of the "+self.item+". Round off your answer to two decimal places, if required"
        self.problem2 = self.name+" bought "+str(self.NumberOfItem)+" "+self.item+" for $"+str(self.total)+". What was the average cost of the "+self.item+"? Give your answer correct to the hundredths place."
        self.problem3 = str(self.NumberOfItem)+" dissimilar "+self.item+" cost $"+str(self.total)+". Find the average cost of the "+self.item+" rounded off to two decimal places."
        self.problem4 = "The cost of "+str(self.NumberOfItem)+" different "+self.item+" is $"+str(self.total)+". What is the average cost of the "+self.item+", correct to two decimal places?"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
            
        if self.NumberOfItem == 3:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3)/3,2))
            self.flag = 1
        elif self.NumberOfItem == 4:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4)/4,2))
            self.flag = 2
        else:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5,2))
            self.flag = 3                    
        
        if len(self.answer.partition(".")[2])==1:
            self.answer = self.answer + "0"        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.dollar,self.unit,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':2,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"$"}
    
    def ExplainType4(self,problem,answer,number1,number2,number3,number4,number5,flag,dollar,unit,item):
        self.answer_text = "The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average cost</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>Total cost of the "+self.item+"</u><br>Number of "+self.item+"</td></tr></table>"
        if flag == 1:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total cost of the "+self.item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1+number2+number3)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+self.item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average cost of the "+self.item+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+dollar+str(number1+number2+number3)+" "+unit+"</u><br>3</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+dollar+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 2:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total cost of the "+self.item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1+number2+number3+number4)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+self.item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>4</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average cost of the "+self.item+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+dollar+str(number1+number2+number3+number4)+" "+unit+"</u><br>4</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+dollar+str(answer)+"</td></tr></table>"
        elif flag == 3:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total cost of the "+self.item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1+number2+number3+number4+number5)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+self.item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>5</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average cost of the "+self.item+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+dollar+str(number1+number2+number3+number4+number5)+" "+unit+"</u><br>5</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+dollar+str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Data-Analysis/Finding-Average" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):
        '''e.g.:
        The total mass of <number> [packages] is <decimal> kg. What is the average mass of the [packages]?'''
        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.number1 = float(randint(2000,4000))/100
        self.number2 = float(randint(2000,4000))/100
        self.number3 = float(randint(2000,4000))/100
        self.number4 = float(randint(2000,4000))/100
        self.number5 = float(randint(2000,4000))/100
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.dollar = ""
        self.unit="kg"
        self.item = random.choice(['boys', 'girls', 'children', 'people', 'cartons', 'boxes', 'suitcases', 'sacks of sugar', 'sacks of rice']) 
        self.total = 0
        for i in range(self.NumberOfItem):
            self.total = self.total + self.numbers[i]
            
        self.problem1 = "The total mass of "+str(self.NumberOfItem)+" "+self.item+" is "+str(self.total)+" kg. What is the average mass of the "+self.item+"? Round off your answer to two decimal places, if required."
        self.problem2 = "What is the average mass of "+str(self.NumberOfItem)+" "+self.item+" if their total mass is "+str(self.total)+" kg? Round off your answer to the nearest hundredth, if required."
        self.problem3 = str(self.NumberOfItem)+" "+self.item+" have a total mass of "+str(self.total)+" kg. Find their average mass, correct to the hundredths place."
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
            
        if self.NumberOfItem == 3:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3)/3,2))
            self.flag = 1
        elif self.NumberOfItem == 4:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4)/4,2))
            self.flag = 2
        else:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5,2))
            self.flag = 3                    
        
        if len(self.answer.partition(".")[2])==1:
            self.answer = self.answer + "0"        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.dollar,self.unit,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'CheckAnswerType':2,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",'unit':'kg'}
    
    def ExplainType5(self,problem,answer,number1,number2,number3,number4,number5,flag,dollar,unit,item):
        self.answer_text = "The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average mass</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>Total mass of all "+item+"</u><br>Number of "+item+"</td></tr></table>"
        if flag == 1:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total mass of all "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1+number2+number3)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average mass of the "+item+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+dollar+str(number1+number2+number3)+" "+unit+"</u><br>3</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+dollar+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 2:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total mass of all "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1+number2+number3+number4)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>4</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average mass of the "+item+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+dollar+str(number1+number2+number3+number4)+" "+unit+"</u><br>4</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+dollar+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 3:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total mass of all "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1+number2+number3+number4+number5)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>5</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average mass of the "+item+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+dollar+str(number1+number2+number3+number4+number5)+" "+unit+"</u><br>5</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+dollar+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Data-Analysis/Finding-Average" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):
        '''e.g.:
        The table below shows the [marks] scored by <number> [pupils] in a [test].'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.names = random.sample(PersonName.PersonName,5)
        self.items = random.choice([['marks','pupils','a test','pupil'],['marks','students','an exam','student'],['points','players','a basketball game','player'],
                                    ['runs','players','a cricket game','player'],['points','friends','a video game','friend'],['points','players','a volleyball video game','player'],
                                    ['points','kids','a computer game','kid']]) 
        
        self.problem = "The table below shows the "+self.items[0]+" scored by "+str(self.NumberOfItem)+" "+self.items[1]+" in "+self.items[2]+".<br><br>"
        self.problem = self.problem + "<table class='Reports'><tr><td style='background-color:#307554;color:#fff;'>"+self.items[3].capitalize()+"</td>"
        for i in range(self.NumberOfItem):
            self.problem = self.problem + "<td>"+self.names[i]+"</td>"
        self.problem = self.problem + "</tr><tr><td style='background-color:#307554;color:#fff;'>"+self.items[0].capitalize()+"</td>"
        for i in range(self.NumberOfItem-1):
            self.problem = self.problem + "<td>"+str(self.numbers[i])+"</td>"
        
        if self.NumberOfItem == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.problem = self.problem + "<td>"+str(self.number3)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3)/3
            self.flag = 1
        elif self.NumberOfItem == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.problem = self.problem + "<td>"+str(self.number4)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4)/4
            self.flag = 2
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.problem = self.problem + "<td>"+str(self.number5)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5
            self.flag = 3                    

        self.problem = self.problem + "</tr></table>"
        self.ask1 = "<br>What was their average score?"
        self.ask2 = "<br>Find their average score."
        self.ask = random.choice([self.ask1,self.ask2])
        self.problem = self.problem+self.ask
        
        self.unit = self.items[0]
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.unit,self.items[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}
    
    def ExplainType6(self,problem,answer,number1,number2,number3,number4,number5,flag,unit,pupil):
        self.answer_text = "The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average score</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>Total "+unit+" scored by all "+pupil+"</u><br>Number of "+pupil+"</td></tr></table>"
        if flag == 1:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total "+unit+" scored by all "+pupil+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1+number2+number3)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+pupil+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average score</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;text-align:left'><u>"+str(number1+number2+number3)+"</u><br>&nbsp;3</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 2:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total "+unit+" scored by all "+pupil+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+" + "+str(number4)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1+number2+number3+number4)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+pupil+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>4</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average score</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;text-align:left'><u>"+str(number1+number2+number3+number4)+"</u><br>&nbsp;4</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 3:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total "+unit+" scored by all "+pupil+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+" + "+str(number4)+" + "+str(number5)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1+number2+number3+number4+number5)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+pupil+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>5</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average score</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;text-align:left'><u>"+str(number1+number2+number3+number4+number5)+"</u><br>&nbsp;5</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Data-Analysis/Finding-Average" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):
        '''e.g.:
        The table below shows the number of [shirts sewn] by [Person.Girlname] in <number> days.'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.name = random.choice(PersonName.GirlName)
        self.items = random.choice([['shirts sewn','shirts she sewed','Shirts','shirts','shirts sewn'],['skirts sewn','skirts she sewed','Skirts','skirts','skirts sewn'],
                                    ['cushion covers sewn','cushion covers she sewed','Cushion covers','cushion covers','cushion covers sewn'],['curtains sewn','curtains she sewed','Curtains','curtains','curtains sewn'],
                                    ['glasses of lemonade sold','glasses of lemonade she sold','Glasses','glasses','glasses sold'],['toys sold','toys she sold','Toys','toys','toys sold'],
                                    ['pizza orders received','pizza orders she received','Pizza orders','orders','orders received'],['rolls of lace bought','rolls of lace she bought','Rolls','rolls','rolls bought'],
                                    ['mathematics problems solved','problems solved','Problems','problems','problems solved'],['pages of a novel read','pages she read','Pages','pages','pages read']])
        
        self.problem = "The table below shows the number of "+self.items[0]+" by "+self.name+" in "+str(self.NumberOfItem)+" days.<br><br>"
        self.problem = self.problem + "<table class='Reports'><tr><td style='background-color:#307554;color:#fff;'>Day</td>"
        for i in range(self.NumberOfItem):
            self.problem = self.problem + "<td>Day "+str(i+1)+"</td>"
        self.problem = self.problem + "</tr><tr><td style='background-color:#307554;color:#fff;'>"+self.items[2]+"</td>"
        for i in range(self.NumberOfItem-1):
            self.problem = self.problem + "<td>"+str(self.numbers[i])+"</td>"
        
        if self.NumberOfItem == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.problem = self.problem + "<td>"+str(self.number3)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3)/3
            self.flag = 1
        elif self.NumberOfItem == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.problem = self.problem + "<td>"+str(self.number4)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4)/4
            self.flag = 2
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.problem = self.problem + "<td>"+str(self.number5)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5
            self.flag = 3                    

        self.problem = self.problem + "</tr></table>"
        self.ask1 = "<br>What was the average number of "+self.items[1]+" per day?"
        self.ask2 = "<br>Find the average number of "+self.items[1]+" per day."
        self.ask = random.choice([self.ask1,self.ask2])
        self.problem = self.problem+self.ask
        
        self.unit = self.items[3]
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.unit,self.items[4])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}
    
    def ExplainType7(self,problem,answer,number1,number2,number3,number4,number5,flag,unit,pupil):
        self.answer_text = "The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average number of "+pupil+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>Total number of "+pupil+"</u><br>Number of days</td></tr></table>"
        if flag == 1:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total number of "+pupil+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1+number2+number3)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of days</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average number of "+pupil+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+str(number1+number2+number3)+"</u><br>3</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+str(answer)+"</td></tr></table>"
        elif flag == 2:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total number of "+pupil+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+" + "+str(number4)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1+number2+number3+number4)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of days</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>4</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average number of "+pupil+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+str(number1+number2+number3+number4)+"</u><br>4</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+str(answer)+"</td></tr></table>"
        elif flag == 3:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total number of "+pupil+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+" + "+str(number2)+" + "+str(number3)+" + "+str(number4)+" + "+str(number5)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1+number2+number3+number4+number5)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of days</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>5</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average number of "+pupil+"</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+str(number1+number2+number3+number4+number5)+"</u><br>5</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Data-Analysis/Finding-Average" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8a(self):
        '''e.g.:
        The total length of <number> [strips of ribbon] is <decimal> cm. Find the average length of the [ribbons].'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = float(randint(2000,4000))/100
        self.number2 = float(randint(2000,4000))/100
        self.number3 = float(randint(2000,4000))/100
        self.number4 = float(randint(2000,4000))/100
        self.number5 = float(randint(2000,4000))/100
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.dollar = ""
        self.unit="cm"
        self.items = random.choice([['strips of ribbon','ribbons'],['pieces of lace','laces'],['strips of tape','tapes'],['pieces of wire','wires'],
                                    ['pieces of string','strings'],['sticks','sticks'],['straws','straws'],['twigs','twigs'],['pencils','pencils']]) 
        self.total = 0
        for i in range(self.NumberOfItem):
            self.total = self.total + self.numbers[i]
            
        self.problem1 = "The total length of "+str(self.NumberOfItem)+" "+self.items[0]+" is "+str(self.total)+" cm. Find the average length of the "+self.items[1]+". Round off your answer to two decimal places, if required."
        self.problem2 = str(self.NumberOfItem)+" "+self.items[0]+" have a total length of "+str(self.total)+" cm. What is the average length of the "+self.items[1]+"? Give your answer correct to the hundredths place."
        self.problem3 = "What is the average length of "+str(self.NumberOfItem)+" "+self.items[0]+", if their total length is "+str(self.total)+" cm? Find your answer correct to the nearest hundredth."
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
            
        if self.NumberOfItem == 3:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3)/3,2))
            self.flag = 1
        elif self.NumberOfItem == 4:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4)/4,2))
            self.flag = 2
        else:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5,2))
            self.flag = 3                    
        
        if len(self.answer.partition(".")[2])==1:
            self.answer = self.answer + "0"        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.dollar,self.unit,self.items[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8a",'CheckAnswerType':2,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",'unit':'cm'}
    
    def ExplainType8(self,problem,answer,number1,number2,number3,number4,number5,flag,dollar,unit,item):
        self.answer_text = "The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average length</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>Total length of all "+item+"</u><br>Number of "+item+"</td></tr></table>"
        if flag == 1:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total length of all "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1+number2+number3)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average length</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+dollar+str(number1+number2+number3)+" "+unit+"</u><br>3</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+dollar+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 2:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total length of all "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1+number2+number3+number4)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>4</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average length</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+dollar+str(number1+number2+number3+number4)+" "+unit+"</u><br>4</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+dollar+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 3:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total length of all "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number1+number2+number3+number4+number5)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>5</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Average length</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>"+dollar+str(number1+number2+number3+number4+number5)+" "+unit+"</u><br>5</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:center'>"+dollar+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Data-Analysis/Finding-Average" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8b(self):
        '''e.g.:
        The total length of <number> [pieces of fabric] is <decimal> m. What is the average length of the fabrics?'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = float(randint(200,400))/100
        self.number2 = float(randint(200,400))/100
        self.number3 = float(randint(200,400))/100
        self.number4 = float(randint(200,400))/100
        self.number5 = float(randint(200,400))/100
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.dollar = ""
        self.unit="m"
        self.items = random.choice([['strips of cloth','cloths'],['pieces of ribbon','ribbons'],['sheets of foil','foils'],['sheets of wrapper','wrappers'],
                                    ['pieces of rope','ropes'],['pieces of cable','cables'],['pieces of thread','threads'],['poles','poles'],['pipes','pipes'],
                                    ['logs of wood','logs']]) 
        self.total = 0
        for i in range(self.NumberOfItem):
            self.total = self.total + self.numbers[i]
            
        self.problem1 = "The total length of "+str(self.NumberOfItem)+" "+self.items[0]+" is "+str(self.total)+" m. Find the average length of the "+self.items[1]+". Round off your answer to two decimal places, if required."
        self.problem2 = str(self.NumberOfItem)+" "+self.items[0]+" have a total length of "+str(self.total)+" m. What is the average length of the "+self.items[1]+"? Give your answer correct to the hundredths place."
        self.problem3 = "What is the average length of "+str(self.NumberOfItem)+" "+self.items[0]+", if their total length is "+str(self.total)+" m? Find your answer correct to the nearest hundredth."
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
            
        if self.NumberOfItem == 3:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3)/3,2))
            self.flag = 1
        elif self.NumberOfItem == 4:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4)/4,2))
            self.flag = 2
        else:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5,2))
            self.flag = 3                    
        
        if len(self.answer.partition(".")[2])==1:
            self.answer = self.answer + "0"        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.dollar,self.unit,self.items[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8b",'CheckAnswerType':2,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",'unit':'m'}
    
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,
                    CheckAnswerType,grade,complexity_level,HCScore):
        
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
                'CheckAnswerType':CheckAnswerType,'grade':5,"complexity_level":complexity_level,"HCScore":HCScore}      

    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        Find the average of the given numbers. (Write your answer correct up to 2 decimal places)'''
        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.number1 = randint(0,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.ProblemSelection = randint(1,3)
        self.problem1 = "Find the average of the numbers given below:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem2 = "Find the average of the following set of numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem3 = "For the following, find the average.<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem4 = "What is the average of the following set?<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4]) 
        if self.ProblemSelection == 1:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.problem = self.problem + str(self.number1)+", "+str(self.number2)+", "+str(self.number3)+"<br>"
            self.answer = (self.number1 + self.number2 + self.number3)/3
            self.flag = 1
        elif self.ProblemSelection == 2:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.problem = self.problem + str(self.number1)+", "+str(self.number2)+", "+str(self.number3)+", "+str(self.number4)+"<br>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4)/4
            self.flag = 2
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.problem = self.problem + str(self.number1)+", "+str(self.number2)+", "+str(self.number3)+", "+str(self.number4)+", "+str(self.number5)+"<br>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5
            self.flag = 3                    
        
        self.problem_type = "ProblemTypeMCQ1"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 5
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        Find the average of the numbers given below. Write your answer correct up to 1 decimal places)'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(0,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.ProblemSelection = randint(1,3)
        self.UnitSelection = randint(1,10)
        self.dollar = ""
        self.unit = ""
        if self.UnitSelection == 7 or self.UnitSelection == 8:
            self.dollar = "$"
        elif self.UnitSelection == 9 or self.UnitSelection == 10:
            self.unit = random.choice(["m","cm","km","kg"])
        self.problem1 = "Find the average of the given set correct to the nearest tenth:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem2 = "Find the average of the following set. Give your answer correct to the nearest tenth.<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem3 = "For the following, find the average. Give your answer correct to 1 decimal place.<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem4 = "What is the average of the following set correct to 1 decimal place?<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4]) 
        if self.ProblemSelection == 1:
            self.problem = self.problem + self.dollar+str(self.number1)+" "+self.unit+", "+self.dollar+str(self.number2)+" "+self.unit+", "+self.dollar+str(self.number3)+" "+self.unit+"<br>"
            self.answer = round(float(self.number1 + self.number2 + self.number3)/3,1)
            self.flag = 1
        elif self.ProblemSelection == 2:
            self.problem = self.problem + self.dollar+str(self.number1)+" "+self.unit+", "+self.dollar+str(self.number2)+" "+self.unit+", "+self.dollar+str(self.number3)+" "+self.unit+", "+self.dollar+str(self.number4)+" "+self.unit+"<br>"
            self.answer = round(float(self.number1 + self.number2 + self.number3 + self.number4)/4,1)
            self.flag = 2
        else:
            self.problem = self.problem + self.dollar+str(self.number1)+" "+self.unit+", "+self.dollar+str(self.number2)+" "+self.unit+", "+self.dollar+str(self.number3)+" "+self.unit+", "+self.dollar+str(self.number4)+" "+self.unit+", "+self.dollar+str(self.number5)+" "+self.unit+"<br>"
            self.answer = round(float(self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5,1)
            self.flag = 3                    
        
        self.problem_type = "ProblemTypeMCQ2"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 5
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.dollar,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ3a(self):
        '''e.g.:
        [Person.name] had <number> bags of [marbles]. The table below shows the number of [marbles] in the <number> bags.'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.item = random.choice(['marbles','beads','shells','forks','spoons','plates','rubberbands','apples','oranges','pears',
                     'peaches','potatoes','guavas','kiwifruits','candies','coasters','straws']) 
        
        self.problem = self.name + " had "+str(self.NumberOfItem)+" bags of "+self.item+". The table below shows the number of "
        self.problem = self.problem + self.item + " in the "+str(self.NumberOfItem)+" bags.<br><br>"
        self.problem = self.problem + "<table class='Reports'><tr><td style='background-color:#307554;color:#fff;'>Bag</td>"
        for i in range(self.NumberOfItem):
            self.problem = self.problem + "<td>Bag "+str(i+1)+"</td>"
        self.problem = self.problem + "</tr><tr><td style='background-color:#307554;color:#fff;'>"+self.item.capitalize()+"</td>"
        for i in range(self.NumberOfItem-1):
            self.problem = self.problem + "<td>"+str(self.numbers[i])+"</td>"
        
        if self.NumberOfItem == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.problem = self.problem + "<td>"+str(self.number3)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3)/3
            self.flag = 1
        elif self.NumberOfItem == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.problem = self.problem + "<td>"+str(self.number4)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4)/4
            self.flag = 2
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.problem = self.problem + "<td>"+str(self.number5)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5
            self.flag = 3                    

        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "<br>What was the average number of "+self.item+" in each bag?"
        
        self.unit = self.item
        self.holder = "bag"
        self.holders = "bags"
        
        self.problem_type = "ProblemTypeMCQ3a"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 5
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))
        for i in range(self.NumberOfItem):
            if str(self.numbers[0]) not in self.wrongAnswers:
                self.wrongAnswers.append(str(self.numbers[i]))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.unit,self.holder,self.holders)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ3b(self):
        '''e.g.:
        The table below shows the number of [pencils] in <number> boxes.'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.item = random.choice(['pencils', 'sharpeners', 'erasers', 'rulers', 'pens', 'crayons', 'highlighters', 'markers', 'cookies', 'bars of chocolate', 'cans of juice']) 
        
        self.problem = "The table below shows the number of "+self.item+" in "+str(self.NumberOfItem)+" boxes.<br><br>"
        self.problem = self.problem + "<table class='Reports'><tr><td style='background-color:#307554;color:#fff;'>Box</td>"
        for i in range(self.NumberOfItem):
            self.problem = self.problem + "<td>Box "+str(i+1)+"</td>"
        self.problem = self.problem + "</tr><tr><td style='background-color:#307554;color:#fff;'>"+self.item.capitalize()+"</td>"
        for i in range(self.NumberOfItem-1):
            self.problem = self.problem + "<td>"+str(self.numbers[i])+"</td>"
        
        if self.NumberOfItem == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.problem = self.problem + "<td>"+str(self.number3)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3)/3
            self.flag = 1
        elif self.NumberOfItem == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.problem = self.problem + "<td>"+str(self.number4)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4)/4
            self.flag = 2
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.problem = self.problem + "<td>"+str(self.number5)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5
            self.flag = 3                    

        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "<br>Find the average number of "+self.item+" in each box."
        
        self.unit = self.item
        self.holder = "box"
        self.holders = "boxes"
        
        self.problem_type = "ProblemTypeMCQ3b"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 5
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))
        for i in range(self.NumberOfItem):
            if str(self.numbers[0]) not in self.wrongAnswers:
                self.wrongAnswers.append(str(self.numbers[i]))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.unit,self.holder,self.holders)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ4(self):
        '''e.g.:
        [Person.name] spent a total of $<amount> on <number> different [books]. Find the average cost of the [books].'''
        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.number1 = randint(2,20)
        self.number2 = randint(2,20)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.dollar = "$"
        self.unit=""
        self.name = random.choice(PersonName.PersonName)
        self.item = random.choice(['books', 'toys', 'pens', 'rolls of string', 'water bottles', 'soccer balls', 'keychains', 'bracelets', 'plants'])
        self.total = 0
        for i in range(self.NumberOfItem):
            self.total = self.total + self.numbers[i]
            
        self.problem1 = self.name + " spent a total of $"+str(self.total)+" on "+str(self.NumberOfItem)+" "+self.item+". Find the average cost of the "+self.item+". Round off your answer to two decimal places, if required"
        self.problem2 = self.name+" bought "+str(self.NumberOfItem)+" "+self.item+" for $"+str(self.total)+". What was the average cost of the "+self.item+"? Give your answer correct to the hundredths place."
        self.problem3 = str(self.NumberOfItem)+" dissimilar "+self.item+" cost $"+str(self.total)+". Find the average cost of the "+self.item+" rounded off to two decimal places."
        self.problem4 = "The cost of "+str(self.NumberOfItem)+" different "+self.item+" is $"+str(self.total)+". What is the average cost of the "+self.item+", correct to two decimal places?"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
            
        if self.NumberOfItem == 3:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3)/3,2))
            self.flag = 1
        elif self.NumberOfItem == 4:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4)/4,2))
            self.flag = 2
        else:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5,2))
            self.flag = 3                    
        
        if len(self.answer.partition(".")[2])==1:
            self.answer = self.answer + "0"        
        
        self.problem_type = "ProblemTypeMCQ4"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 5
        
        self.wrongAnswers = []

        for i in range(2):
            wrongAnswer = str(((float(self.answer)*100+5*(i+1))/100))
            if len(wrongAnswer.partition(".")[2])==1:
                wrongAnswer = wrongAnswer + "0"
            self.wrongAnswers.append(wrongAnswer)        
        
        for i in range(2):
            wrongAnswer = str(((float(self.answer)*100-5*(i+1))/100))
            if len(wrongAnswer.partition(".")[2])==1:
                wrongAnswer = wrongAnswer + "0"
            self.wrongAnswers.append(wrongAnswer)        


        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.dollar,self.unit,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ5(self):
        '''e.g.:
        The total mass of <number> [packages] is <decimal> kg. What is the average mass of the [packages]?'''
        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.number1 = float(randint(2000,4000))/100
        self.number2 = float(randint(2000,4000))/100
        self.number3 = float(randint(2000,4000))/100
        self.number4 = float(randint(2000,4000))/100
        self.number5 = float(randint(2000,4000))/100
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.dollar = ""
        self.unit="kg"
        self.item = random.choice(['boys', 'girls', 'children', 'people', 'cartons', 'boxes', 'suitcases', 'sacks of sugar', 'sacks of rice']) 
        self.total = 0
        for i in range(self.NumberOfItem):
            self.total = self.total + self.numbers[i]
            
        self.problem1 = "The total mass of "+str(self.NumberOfItem)+" "+self.item+" is "+str(self.total)+" kg. What is the average mass of the "+self.item+"? Round off your answer to two decimal places, if required."
        self.problem2 = "What is the average mass of "+str(self.NumberOfItem)+" "+self.item+" if their total mass is "+str(self.total)+" kg? Round off your answer to the nearest hundredth, if required."
        self.problem3 = str(self.NumberOfItem)+" "+self.item+" have a total mass of "+str(self.total)+" kg. Find their average mass, correct to the hundredths place."
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
            
        if self.NumberOfItem == 3:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3)/3,2))
            self.flag = 1
        elif self.NumberOfItem == 4:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4)/4,2))
            self.flag = 2
        else:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5,2))
            self.flag = 3                    
        
        if len(self.answer.partition(".")[2])==1:
            self.answer = self.answer + "0"        
        
        self.problem_type = "ProblemTypeMCQ5"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 5
        
        self.wrongAnswers = []
        
        for i in range(2):
            wrongAnswer = str(((float(self.answer)*100+5*(i+1))/100))
            if len(wrongAnswer.partition(".")[2])==1:
                wrongAnswer = wrongAnswer + "0"
            self.wrongAnswers.append(wrongAnswer)        
        
        for i in range(2):
            wrongAnswer = str(((float(self.answer)*100-5*(i+1))/100))
            if len(wrongAnswer.partition(".")[2])==1:
                wrongAnswer = wrongAnswer + "0"
            self.wrongAnswers.append(wrongAnswer)        


        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.dollar,self.unit,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ6(self):
        '''e.g.:
        The table below shows the [marks] scored by <number> [pupils] in a [test].'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.names = random.sample(PersonName.PersonName,5)
        self.items = random.choice([['marks','pupils','a test','pupil'],['marks','students','an exam','student'],['points','players','a basketball game','player'],
                                    ['runs','players','a cricket game','player'],['points','friends','a video game','friend'],['points','players','a volleyball video game','player'],
                                    ['points','kids','a computer game','kid']]) 
        
        self.problem = "The table below shows the "+self.items[0]+" scored by "+str(self.NumberOfItem)+" "+self.items[1]+" in "+self.items[2]+".<br><br>"
        self.problem = self.problem + "<table class='Reports'><tr><td style='background-color:#307554;color:#fff;'>"+self.items[3].capitalize()+"</td>"
        for i in range(self.NumberOfItem):
            self.problem = self.problem + "<td>"+self.names[i]+"</td>"
        self.problem = self.problem + "</tr><tr><td style='background-color:#307554;color:#fff;'>"+self.items[0].capitalize()+"</td>"
        for i in range(self.NumberOfItem-1):
            self.problem = self.problem + "<td>"+str(self.numbers[i])+"</td>"
        
        if self.NumberOfItem == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.problem = self.problem + "<td>"+str(self.number3)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3)/3
            self.flag = 1
        elif self.NumberOfItem == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.problem = self.problem + "<td>"+str(self.number4)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4)/4
            self.flag = 2
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.problem = self.problem + "<td>"+str(self.number5)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5
            self.flag = 3                    

        self.problem = self.problem + "</tr></table>"
        self.ask1 = "<br>What was their average score?"
        self.ask2 = "<br>Find their average score."
        self.ask = random.choice([self.ask1,self.ask2])
        self.problem = self.problem+self.ask
        
        self.unit = self.items[0]
        
        self.problem_type = "ProblemTypeMCQ6"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 5
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))
        for i in range(self.NumberOfItem):
            if str(self.numbers[0]) not in self.wrongAnswers:
                self.wrongAnswers.append(str(self.numbers[i]))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.unit,self.items[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ7(self):
        '''e.g.:
        The table below shows the number of [shirts sewn] by [Person.Girlname] in <number> days.'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.name = random.choice(PersonName.GirlName)
        self.items = random.choice([['shirts sewn','shirts she sewed','Shirts','shirts','shirts sewn'],['skirts sewn','skirts she sewed','Skirts','skirts','skirts sewn'],
                                    ['cushion covers sewn','cushion covers she sewed','Cushion covers','cushion covers','cushion covers sewn'],['curtains sewn','curtains she sewed','Curtains','curtains','curtains sewn'],
                                    ['glasses of lemonade sold','glasses of lemonade she sold','Glasses','glasses','glasses sold'],['toys sold','toys she sold','Toys','toys','toys sold'],
                                    ['pizza orders received','pizza orders she received','Pizza orders','orders','orders received'],['rolls of lace bought','rolls of lace she bought','Rolls','rolls','rolls bought'],
                                    ['mathematics problems solved','problems solved','Problems','problems','problems solved'],['pages of a novel read','pages she read','Pages','pages','pages read']])
        
        self.problem = "The table below shows the number of "+self.items[0]+" by "+self.name+" in "+str(self.NumberOfItem)+" days.<br><br>"
        self.problem = self.problem + "<table class='Reports'><tr><td style='background-color:#307554;color:#fff;'>Day</td>"
        for i in range(self.NumberOfItem):
            self.problem = self.problem + "<td>Day "+str(i+1)+"</td>"
        self.problem = self.problem + "</tr><tr><td style='background-color:#307554;color:#fff;'>"+self.items[2]+"</td>"
        for i in range(self.NumberOfItem-1):
            self.problem = self.problem + "<td>"+str(self.numbers[i])+"</td>"
        
        if self.NumberOfItem == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.problem = self.problem + "<td>"+str(self.number3)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3)/3
            self.flag = 1
        elif self.NumberOfItem == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.problem = self.problem + "<td>"+str(self.number4)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4)/4
            self.flag = 2
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.problem = self.problem + "<td>"+str(self.number5)+"</td>"
            self.answer = (self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5
            self.flag = 3                    

        self.problem = self.problem + "</tr></table>"
        self.ask1 = "<br>What was the average number of "+self.items[1]+" per day?"
        self.ask2 = "<br>Find the average number of "+self.items[1]+" per day."
        self.ask = random.choice([self.ask1,self.ask2])
        self.problem = self.problem+self.ask
        
        self.unit = self.items[3]
        
        self.problem_type = "ProblemTypeMCQ7"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 5
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))
        for i in range(self.NumberOfItem):
            if str(self.numbers[0]) not in self.wrongAnswers:
                self.wrongAnswers.append(str(self.numbers[i]))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.unit,self.items[4])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ8a(self):
        '''e.g.:
        The total length of <number> [strips of ribbon] is <decimal> cm. Find the average length of the [ribbons].'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = float(randint(2000,4000))/100
        self.number2 = float(randint(2000,4000))/100
        self.number3 = float(randint(2000,4000))/100
        self.number4 = float(randint(2000,4000))/100
        self.number5 = float(randint(2000,4000))/100
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.dollar = ""
        self.unit="cm"
        self.items = random.choice([['strips of ribbon','ribbons'],['pieces of lace','laces'],['strips of tape','tapes'],['pieces of wire','wires'],
                                    ['pieces of string','strings'],['sticks','sticks'],['straws','straws'],['twigs','twigs'],['pencils','pencils']]) 
        self.total = 0
        for i in range(self.NumberOfItem):
            self.total = self.total + self.numbers[i]
            
        self.problem1 = "The total length of "+str(self.NumberOfItem)+" "+self.items[0]+" is "+str(self.total)+" cm. Find the average length of the "+self.items[1]+". Round off your answer to two decimal places, if required."
        self.problem2 = str(self.NumberOfItem)+" "+self.items[0]+" have a total length of "+str(self.total)+" cm. What is the average length of the "+self.items[1]+"? Give your answer correct to the hundredths place."
        self.problem3 = "What is the average length of "+str(self.NumberOfItem)+" "+self.items[0]+", if their total length is "+str(self.total)+" cm? Find your answer correct to the nearest hundredth."
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
            
        if self.NumberOfItem == 3:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3)/3,2))
            self.flag = 1
        elif self.NumberOfItem == 4:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4)/4,2))
            self.flag = 2
        else:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5,2))
            self.flag = 3                    
        
        if len(self.answer.partition(".")[2])==1:
            self.answer = self.answer + "0"        
        
        self.problem_type = "ProblemTypeMCQ8a"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 5
        
        self.wrongAnswers = []
        
        for i in range(2):
            wrongAnswer = str(((float(self.answer)*100+5*(i+1))/100))
            if len(wrongAnswer.partition(".")[2])==1:
                wrongAnswer = wrongAnswer + "0"
            self.wrongAnswers.append(wrongAnswer)        
        
        for i in range(2):
            wrongAnswer = str(((float(self.answer)*100-5*(i+1))/100))
            if len(wrongAnswer.partition(".")[2])==1:
                wrongAnswer = wrongAnswer + "0"
            self.wrongAnswers.append(wrongAnswer)        


        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.dollar,self.unit,self.items[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ8b(self):
        '''e.g.:
        The total length of <number> [pieces of fabric] is <decimal> m. What is the average length of the fabrics?'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = float(randint(200,400))/100
        self.number2 = float(randint(200,400))/100
        self.number3 = float(randint(200,400))/100
        self.number4 = float(randint(200,400))/100
        self.number5 = float(randint(200,400))/100
        self.numbers = [self.number1,self.number2,self.number3,self.number4,self.number5]
        self.NumberOfItem = randint(3,5)
        self.dollar = ""
        self.unit="m"
        self.items = random.choice([['strips of cloth','cloths'],['pieces of ribbon','ribbons'],['sheets of foil','foils'],['sheets of wrapper','wrappers'],
                                    ['pieces of rope','ropes'],['pieces of cable','cables'],['pieces of thread','threads'],['poles','poles'],['pipes','pipes'],
                                    ['logs of wood','logs']]) 
        self.total = 0
        for i in range(self.NumberOfItem):
            self.total = self.total + self.numbers[i]
            
        self.problem1 = "The total length of "+str(self.NumberOfItem)+" "+self.items[0]+" is "+str(self.total)+" m. Find the average length of the "+self.items[1]+". Round off your answer to two decimal places, if required."
        self.problem2 = str(self.NumberOfItem)+" "+self.items[0]+" have a total length of "+str(self.total)+" m. What is the average length of the "+self.items[1]+"? Give your answer correct to the hundredths place."
        self.problem3 = "What is the average length of "+str(self.NumberOfItem)+" "+self.items[0]+", if their total length is "+str(self.total)+" m? Find your answer correct to the nearest hundredth."
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
            
        if self.NumberOfItem == 3:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3)/3,2))
            self.flag = 1
        elif self.NumberOfItem == 4:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4)/4,2))
            self.flag = 2
        else:
            self.answer = str(round(float(self.number1 + self.number2 + self.number3 + self.number4 + self.number5)/5,2))
            self.flag = 3                    
        
        if len(self.answer.partition(".")[2])==1:
            self.answer = self.answer + "0"        
        
        self.problem_type = "ProblemTypeMCQ8b"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 5
        
        self.wrongAnswers = []
        
        for i in range(2):
            wrongAnswer = str(((float(self.answer)*100+5*(i+1))/100))
            if len(wrongAnswer.partition(".")[2])==1:
                wrongAnswer = wrongAnswer + "0"
            self.wrongAnswers.append(wrongAnswer)        
        
        for i in range(2):
            wrongAnswer = str(((float(self.answer)*100-5*(i+1))/100))
            if len(wrongAnswer.partition(".")[2])==1:
                wrongAnswer = wrongAnswer + "0"
            self.wrongAnswers.append(wrongAnswer)        


        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.flag,self.dollar,self.unit,self.items[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
        if CheckAnswerType == 1:
            try:
                return (str(answer)==str(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswerType == 2:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False              