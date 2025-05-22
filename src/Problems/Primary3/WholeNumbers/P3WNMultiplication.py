'''
Created on Apr 01, 2013
Module: P3WNMultiplication
Generates the Multiplication problems for Primary 3

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

class P3WNMultiplication:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType5","ProblemTypeMCQ5",],
                            6:["ProblemType6","ProblemTypeMCQ6",],
                            7:["ProblemType7","ProblemTypeMCQ7",],
                            8:["ProblemType8","ProblemTypeMCQ8",],
                            9:["ProblemType9","ProblemTypeMCQ9",],
                            10:["ProblemType10","ProblemTypeMCQ10",],
                            11:["ProblemType11","ProblemTypeMCQ11",],
                            12:["ProblemType12","ProblemTypeMCQ12",],
                            13:["ProblemType13a","ProblemTypeMCQ13a","ProblemType13b","ProblemTypeMCQ13b",],
                            14:["ProblemType14","ProblemTypeMCQ14",],
                            15:["ProblemType15a","ProblemTypeMCQ15a","ProblemType15b","ProblemTypeMCQ15b",],
                            16:["ProblemType16","ProblemTypeMCQ16",],
                            17:["ProblemType17","ProblemTypeMCQ17",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemType5(),self.GenerateProblemTypeMCQ5(),],
                                    6:[self.GenerateProblemType6(),self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemType7(),self.GenerateProblemTypeMCQ7(),],
                                    8:[self.GenerateProblemType8(),self.GenerateProblemTypeMCQ8(),],
                                    9:[self.GenerateProblemType9(),self.GenerateProblemTypeMCQ9(),],
                                    10:[self.GenerateProblemType10(),self.GenerateProblemTypeMCQ10(),],
                                    11:[self.GenerateProblemType11(),self.GenerateProblemTypeMCQ11(),],
                                    12:[self.GenerateProblemType12(),self.GenerateProblemTypeMCQ12(),],
                                    13:[self.GenerateProblemType13a(),self.GenerateProblemTypeMCQ13a(),self.GenerateProblemType13b(),self.GenerateProblemTypeMCQ13b(),],
                                    14:[self.GenerateProblemType14(),self.GenerateProblemTypeMCQ14(),],
                                    15:[self.GenerateProblemType15a(),self.GenerateProblemTypeMCQ15a(),self.GenerateProblemType15b(),self.GenerateProblemTypeMCQ15b(),],
                                    16:[self.GenerateProblemType16(),self.GenerateProblemTypeMCQ16(),],
                                    17:[self.GenerateProblemType17(),self.GenerateProblemTypeMCQ17(),],
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
        #return self.GenerateProblemTypeMCQ15b()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),"ProblemType2":self.GenerateProblemType2(),"ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),"ProblemType5":self.GenerateProblemType5(),"ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),"ProblemType8":self.GenerateProblemType8(),"ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10":self.GenerateProblemType10(),"ProblemType11":self.GenerateProblemType11(),"ProblemType12":self.GenerateProblemType12(),
                            "ProblemType13a":self.GenerateProblemType13a(),"ProblemType13b":self.GenerateProblemType13b(),
                            "ProblemType14":self.GenerateProblemType14(),
                            "ProblemType15a":self.GenerateProblemType15a(),"ProblemType15b":self.GenerateProblemType15b(),
                            "ProblemType16":self.GenerateProblemType16(),"ProblemType17":self.GenerateProblemType17(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),"ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),"ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),"ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),"ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            "ProblemTypeMCQ9":self.GenerateProblemTypeMCQ9(),"ProblemTypeMCQ10":self.GenerateProblemTypeMCQ10(),
                            "ProblemTypeMCQ11":self.GenerateProblemTypeMCQ11(),"ProblemTypeMCQ12":self.GenerateProblemTypeMCQ12(),
                            "ProblemTypeMCQ13a":self.GenerateProblemTypeMCQ13a(),"ProblemTypeMCQ13b":self.GenerateProblemTypeMCQ13b(),
                            "ProblemTypeMCQ14":self.GenerateProblemTypeMCQ14(),
                            "ProblemTypeMCQ15a":self.GenerateProblemTypeMCQ15a(),"ProblemTypeMCQ15b":self.GenerateProblemTypeMCQ15b(),
                            "ProblemTypeMCQ16":self.GenerateProblemTypeMCQ16(),"ProblemTypeMCQ17":self.GenerateProblemTypeMCQ17(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        Find the product of %d and %d.'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.numbers = random.choice([[2,random.sample([1,2,3,4],3)],
                                      [3,random.sample([1,2,3],3)],
                                      [4,random.sample([1,1,2,2],3)],
                                      [random.choice([5,6,7,8,9]),[1,1,1]]
                                      ])
        
        self.number1 = self.numbers[0]
        self.number2 = ""
        
        for i in range(len(self.numbers[1])):
            self.number2 = self.number2 + str(self.numbers[1][i])
        
        self.number2 = int(self.number2)
        
        self.flag = randint(1,7)
        self.flag1 = 0
        if self.flag < 7:        
            self.problem1 = "Find the product of %d and %d."%(self.number2,self.number1)
            self.problem2 = "What is the product of %d and %d?"%(self.number2,self.number1)
            self.problem3 = "What is %d &times; %d?"%(self.number2,self.number1)
            self.problem4 = "The product of %d and %d is ____."%(self.number2,self.number1)
            self.problem5 = "%d &times; %d = ?"%(self.number2,self.number1)
            self.problem6 = "Multiply.<br><br><table border=0><tr>"
            self.problem6 = self.problem6 + "<td>&nbsp;</td><td>"+str(self.number2)[0]+"</td><td>"+str(self.number2)[1]+"</td><td>"+str(self.number2)[2]+"</td></tr>"
            self.problem6 = self.problem6 + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>"+str(self.number1)+"</td></tr>"
            self.problem6 = self.problem6 + "<tr><td colspan=4 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line_4.png' /></td></tr></table>"
            self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6])
            self.answer = self.number1 * self.number2
        else:       
            self.flag1 = randint(1,2)
            if self.flag1 == 1:
                self.problem = ""
                for i in range(self.number1-1):
                    self.problem = self.problem + str(self.number2)+" + "
                self.problem = self.problem + str(self.number2)+" &nbsp;=&nbsp; _____ &nbsp;&times;&nbsp; "+str(self.number1)
                self.answer =  self.number2
            else:
                self.problem = ""
                for i in range(self.number1-1):
                    self.problem = self.problem + str(self.number2)+" + "
                self.problem = self.problem + str(self.number2)+" &nbsp;=&nbsp; "+str(self.number2)+" &nbsp;&times;&nbsp; ___"
                self.answer =  self.number1               
  
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.flag,self.flag1,self.number2,self.number1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType1(self,problem,answer,flag,flag1,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        if flag<7:
            self.solution_text =  self.MultiplicationExplanation(number1,number2)
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, %d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d</font>"%(int(number1),int(number2),int(answer))
        else:
            if flag1==1:
                self.solution_text = "<font class='ExplanationFont'>&nbsp;&nbsp;&nbsp;&nbsp;"
                for i in range(number2-1):
                    self.solution_text = self.solution_text + str(number1)+" + "
                self.solution_text = self.solution_text + str(number1)+"<br><br>=&nbsp; %d &nbsp;&times;&nbsp; %d"%(number1,number2)
                self.solution_text = self.solution_text + "<br><br>So, the missing number is %d.</font>"%(number1)
            else:
                self.solution_text = "<font class='ExplanationFont'>&nbsp;&nbsp;&nbsp;&nbsp;"
                for i in range(number2-1):
                    self.solution_text = self.solution_text + str(number1)+" + "
                self.solution_text = self.solution_text + str(number1)+"<br><br>=&nbsp; "+str(number1)+" &nbsp;&times;&nbsp; %d"%(number2)
                self.solution_text = self.solution_text + "<br><br>So, the missing number is %d.</font>"%(number2)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        What is the number in the box? / Find the missing number.
            1 2 _
        &times;     3
        -------------
            3 6 9'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.numbers = random.choice([[2,random.sample([1,2,3,4],3)],
                                      [3,random.sample([1,2,3],3)],
                                      [4,random.sample([1,1,2,2],3)],
                                      [random.choice([5,6,7,8,9]),[1,1,1]]
                                      ])
        
        self.number1 = self.numbers[0]
        self.number2 = ""
        
        for i in range(len(self.numbers[1])):
            self.number2 = self.number2 + str(self.numbers[1][i])
        
        self.number2 = int(self.number2)
        self.number = self.number1 * self.number2
        
        self.flag = randint(1,2)
        
        self.problem = "Find the missing digit.<br><br>"
        if self.flag == 1:
            self.missingDigit = randint(0,2)        
            self.problem = self.problem + "<table border=0><tr><td>&nbsp;</td>"
            for i in range(3):
                if i!=self.missingDigit:
                    self.problem = self.problem + "<td>"+str(self.number2)[i]+"</td>"
                else:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
            self.problem = self.problem + "</tr>"
            self.problem = self.problem + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>"+str(self.number1)+"</td></tr>"
            self.problem = self.problem + "<tr><td colspan=4 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line_4.png' /></td></tr>"
            self.problem = self.problem + "<tr><td>&nbsp;</td><td>"+str(self.number)[0]+"</td><td>"+str(self.number)[1]+"</td><td>"+str(self.number)[2]+"</td></tr></table>"
            self.answer = str(self.number2)[self.missingDigit]
        else:
            self.missingDigit = randint(0,2)        
            self.problem = self.problem + "<table border=0>"
            self.problem = self.problem + "<tr><td>&nbsp;</td><td>"+str(self.number2)[0]+"</td><td>"+str(self.number2)[1]+"</td><td>"+str(self.number2)[2]+"</td></tr>"
            self.problem = self.problem + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>"+str(self.number1)+"</td></tr>"
            self.problem = self.problem + "<tr><td colspan=4 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line_4.png' /></td></tr>"
            self.problem = self.problem + "<tr><td>&nbsp;</td>"
            for i in range(3):
                if i!=self.missingDigit:
                    self.problem = self.problem + "<td>"+str(self.number)[i]+"</td>"
                else:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
            self.problem = self.problem + "</tr></table>"
            self.answer = str(self.number)[self.missingDigit]

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.flag,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType2(self,problem,answer,flag,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        if flag==1:
            self.solution_text = "<font class='ExplanationFont'>? &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number1*number2)
            self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; ?</font><br><br><br>"%(number1*number2,number1)
            self.solution_text = self.solution_text + self.DivisionExplanation(number2*number1,number1)
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the missing digit is: %d</font>"%(int(answer))
        else:
            self.solution_text = self.MultiplicationExplanation(number2,number1)
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the missing digit is: %d</font>"%(int(answer))

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        There are 32 children in a <class/group/club/team/party/room>. Each child collects 3 <stamps>. How many <stamps> does the <class/group/club/team/party/room> collect altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.numbers = random.choice([[2,random.sample([1,2,3,4],2)],
                                      [3,random.sample([1,2,3],2)],
                                      [4,random.sample([1,1,2,2],2)],
                                      [random.choice([5,6,7,8,9]),[1,1]]
                                      ])
        
        self.number1 = self.numbers[0]
        self.number2 = ""
        
        for i in range(len(self.numbers[1])):
            self.number2 = self.number2 + str(self.numbers[1][i])
        
        self.number2 = int(self.number2)
        
        self.item1 = random.choice(['class','group','club','team'])
        self.item2 = random.choice(['stamps','picture postcards','coins','beads','seashells','twigs','dried leaves','animal cards','coins','comic books','storybooks'])
        
        self.problem = "There are %d children in a %s. Each child collects %d %s. How many %s does the %s collect altogether?"%(self.number2,self.item1,
                                                                                                                                self.number1,self.item2,self.item2,self.item1)
  
        self.answer = self.number1 * self.number2
        
        self.unit = self.item2
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.item1,self.item2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,number1,number2,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'><font style='font-size:0.7em'>child 1</font></td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'><font style='font-size:0.7em'>child 2</font></td><td colspan=2 style='height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>. . . . .</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px'><font style='font-size:0.7em'>child %d</font></td></tr>"%(item2,self.color1,self.color1,self.color1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5><img src='/images/explanation/P3_model_down_brace_small5.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; ?</font><br><br><br>"%(number2,number1)
        self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>The %s collects %d %s altogether.</font>"%(item1,answer,item2)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        [Person.Unclename] sells 122 <apples> in 1 <day/week>. How many <apples> does he sell in 4 <days/weeks>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.numbers = random.choice([[2,random.sample([1,2,3,4],2)],
                                      [3,random.sample([1,2,3],2)],
                                      [4,random.sample([1,1,2,2],2)],
                                      [random.choice([5,6,7,8,9]),[1,1]]
                                      ])
        
        self.number1 = self.numbers[0]
        self.number2 = ""
        
        for i in range(len(self.numbers[1])):
            self.number2 = self.number2 + str(self.numbers[1][i])
        
        self.number2 = int(self.number2)
        
        self.name = random.choice(PersonName.UncleName)
        
        self.item1 = random.choice(['day','week'])
        self.item2 = random.choice(['apples','tickets','pears','pumpkins','watermelons','muffins','cakes','carpets','books','pots'])
        
        self.problem = "%s sells %d %s in 1 %s. How many %s does he sell in %d %ss?"%(self.name,self.number2,self.item2,self.item1,self.item2,
                                                                                      self.number1,self.item1)
  
        self.answer = self.number1 * self.number2
        
        self.unit = self.item2
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.item1,self.item2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,number1,number2,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item2)
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'><font style='font-size:0.7em'>Day %d</font></td>"%(self.color1,x+1)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; ?</font><br><br><br>"%(number2,number1)
        self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>He sells %d %s in %d %ss.</font>"%(answer,item2,number1,item1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        7 &times; 3 = ______ &minus; 4'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(3,9)
        self.number2 = randint(3,9)
        self.number4 = randint(3,9)
        self.number3 = self.number1*self.number2 + self.number4
        
        self.flag = randint(1,2)
        
        self.problem = "Find the missing number in the blank.<br><br>"
        if self.flag == 1:
            self.problem = self.problem + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&minus;&nbsp; ___"%(self.number1,self.number2,self.number3)
            self.answer = self.number4
        else:
            self.problem = self.problem + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; ___ &nbsp;&minus;&nbsp; %d"%(self.number1,self.number2,self.number4)
            self.answer = self.number3
            
        self.unit = ""
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.flag,self.number1,self.number2,self.number3,self.number4,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,flag,number1,number2,number3,number4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if flag==1:
            self.solution_text = "<table class='ExplanationTable' border=0>"
            self.solution_text = self.solution_text + "<tr><td>%d &nbsp;&times;&nbsp; %d</td><td>=</td><td>%d &nbsp;&minus;&nbsp; ?</td></tr>"%(number1,number2,number3)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;'>%d</td><td>=</td><td>%d &nbsp;&minus;&nbsp; ?</td></tr>"%(number1*number2,number3)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;'>?</td><td>=</td><td>%d &nbsp;&minus;&nbsp; %d</td></tr>"%(number3,number1*number2)
            self.solution_text = self.solution_text + "<tr><td></td><td>=</td><td>%d</td></tr>"%(answer)
            self.solution_text = self.solution_text + "</table><br>"
        else:
            self.solution_text = "<table class='ExplanationTable' border=0>"
            self.solution_text = self.solution_text + "<tr><td>%d &nbsp;&times;&nbsp; %d</td><td>=</td><td>? &nbsp;&minus;&nbsp; %d</td></tr>"%(number1,number2,number4)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right'>%d</td><td>=</td><td>? &nbsp;&minus;&nbsp; %d</td></tr>"%(number1*number2,number4)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;'>?</td><td>=</td><td>%d &nbsp;+&nbsp; %d</td></tr>"%(number1*number2,number4)
            self.solution_text = self.solution_text + "<tr><td></td><td>=</td><td>%d</td></tr>"%(answer)
            self.solution_text = self.solution_text + "</table><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the missing number is: %d</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        Find the product of %d and %d.'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(3,9)
        self.number2 = randint(112,189)

        self.problem1 = "Find the product of %d and %d."%(self.number2,self.number1)
        self.problem2 = "What is the product of %d and %d?"%(self.number2,self.number1)
        self.problem3 = "What is %d &times; %d?"%(self.number2,self.number1)
        self.problem4 = "The product of %d and %d is ____."%(self.number2,self.number1)
        self.problem5 = "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; ?"%(self.number2,self.number1)
        self.problem6 = "Multiply.<br><br><table border=0><tr>"
        self.problem6 = self.problem6 + "<td>&nbsp;</td><td>"+str(self.number2)[0]+"</td><td>"+str(self.number2)[1]+"</td><td>"+str(self.number2)[2]+"</td></tr>"
        self.problem6 = self.problem6 + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>"+str(self.number1)+"</td></tr>"
        self.problem6 = self.problem6 + "<tr><td colspan=4 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line_4.png' /></td></tr></table>"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6])
        self.answer = self.number1 * self.number2
  
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType6(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        self.solution_text =  self.MultiplicationExplanation(number2,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, %d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d</font>"%(int(number2),int(number1),int(answer))

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        What is the number in the box? / Find the missing number.
            1 2 _
        &times;     3
        -------------
            3 6 9'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.numbers = random.choice([[3,randint(112,288)],
                                     [4,randint(112,223)],
                                     [5,randint(112,188)],
                                     [6,randint(112,150)],
                                     [7,randint(112,140)],
                                     [8,randint(112,124)],])
        
        self.number1 = self.numbers[0]
        self.number2 = self.numbers[1]
        self.number = self.number1 * self.number2
        
        self.flag = randint(1,2)

        self.problem = "Find the missing digit.<br><br>"
        if self.flag == 1:
            self.missingDigit = randint(0,2)        
            self.problem = self.problem + "<table border=0><tr><td>&nbsp;</td>"
            for i in range(3):
                if i!=self.missingDigit:
                    self.problem = self.problem + "<td>"+str(self.number2)[i]+"</td>"
                else:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
            self.problem = self.problem + "</tr>"
            self.problem = self.problem + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>"+str(self.number1)+"</td></tr>"
            self.problem = self.problem + "<tr><td colspan=4 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line_4.png' /></td></tr>"
            self.problem = self.problem + "<tr><td>&nbsp;</td><td>"+str(self.number)[0]+"</td><td>"+str(self.number)[1]+"</td><td>"+str(self.number)[2]+"</td></tr></table>"
            self.answer = str(self.number2)[self.missingDigit]
        else:
            self.missingDigit = randint(0,2)        
            self.problem = self.problem + "<table border=0>"
            self.problem = self.problem + "<tr><td>&nbsp;</td><td>"+str(self.number2)[0]+"</td><td>"+str(self.number2)[1]+"</td><td>"+str(self.number2)[2]+"</td></tr>"
            self.problem = self.problem + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>"+str(self.number1)+"</td></tr>"
            self.problem = self.problem + "<tr><td colspan=4 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line_4.png' /></td></tr>"
            self.problem = self.problem + "<tr><td>&nbsp;</td>"
            for i in range(3):
                if i!=self.missingDigit:
                    self.problem = self.problem + "<td>"+str(self.number)[i]+"</td>"
                else:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
            self.problem = self.problem + "</tr></table>"
            self.answer = str(self.number)[self.missingDigit]

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.flag,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType7(self,problem,answer,flag,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        if flag==1:
            self.solution_text = "<font class='ExplanationFont'>? &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number1*number2)
            self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; ?</font><br><br><br>"%(number1*number2,number1)
            self.solution_text = self.solution_text + self.DivisionExplanation(number2*number1,number1)
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the missing digit is: %d</font>"%(int(answer))
        else:
            self.solution_text = "<font class='ExplanationFont'>%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; ?</font><br><br><br>"%(number2,number1)
            self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,number1)
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the missing digit is: %d</font>"%(int(answer))


        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        There are 123 <lorries> in a <parking garage>. <Each lorry has 6 wheels. How many wheels are there in all?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['lorries','parking garage','Each lorry has 6 wheels. How many wheels are there in all?','6','wheels','There are','in all','lorry'],
                      ['cars','car park','Each car has 4 wheels. How many wheels are there in all?','4','wheels','There are','in all','car'],
                      ['cars','showroom','Each car has 6 lights. How many lights are there in all?','6','lights','There are','in all','car'],
                      ['animals','zoo','A boy counts 4 legs on each animal. How many legs does he count altogether?','4','legs','He counts','altogether','animal'],
                      ['birds','park','Each bird has 2 feet. How many feet are there in all?','2','feet','There are','in all','bird'],
                      ['walls','museum','Each wall has 7 paintings. How many paintings are there in all?','7','paintings','There are','in all','wall'],
                      ['apartments','building','Each apartment has 8 windows. How many windows are there altogether?','8','windows','There are','altogether','apartment'],
                      ['pupils','school','The school principal gives away 3 books to each pupil. How many books does the principal give away altogether?','3','books','The principal gives away','altogether','pupil']]
        
        self.item = random.choice(self.items)

        self.number1 = int(self.item[3])
        self.number2 = randint(112,189)
        
        self.problem = "There are %d %s in a %s. %s"%(self.number2,self.item[0],self.item[1],self.item[2])
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[4]
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2,self.item[5],self.item[6],self.item[7],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,number1,number2,item5,item6,item7,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'><font style='font-size:0.7em'>%s 1</font></td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'><font style='font-size:0.7em'>%s 2</font></td><td colspan=2 style='height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>. . . . .</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px'><font style='font-size:0.7em'>%s %d</font></td></tr>"%(unit,self.color1,item7,self.color1,item7,self.color1,item7,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5><img src='/images/explanation/P3_model_down_brace_small5.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s %d %s %s.</font>"%(item5,int(answer),unit,item6)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        <Child tickets at an amusement park> are sold at $16 each. [Person.Unclename] bought 4 <child tickets>. How much did he pay?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['Child tickets at an amusement park','child tickets',randint(12,40)],
                      ['Adult tickets at an amusement park','adult tickets',randint(12,40)],
                      ['Entrance tickets to a water park','entrance tickets',randint(12,40)],
                      ['Child tickets at a theme park','child tickets',randint(12,40)],
                      ['Adult tickets at a theme park','adult tickets',randint(12,40)],
                      ['Entrance tickets to an animal safari','entrance tickets',randint(12,40)],
                      ['Tram tickets at Singapore Night Safari','tram tickets',randint(12,40)],
                      ['Tram tickets at a bird park','tram tickets',randint(12,40)],
                      ['Adult tickets to Singapore Zoo','adult tickets',randint(12,40)],
                      ['Tickets to a musical show','tickets',randint(12,40)],
                      ['Entrance tickets at a science museum','entrance tickets',randint(12,40)],
                      ['Entrance tickets at a coins and stamps museum','entrance tickets',randint(12,40)],
                      ['Coupon booklets at a carnival','coupon booklets',randint(12,40)]]
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.UncleName)
        self.number1 = randint(3,9)
        self.number2 = self.item[2]

        self.problem = "%s are sold at $%d each. %s bought %d %s. How much did he pay?"%(self.item[0],self.number2,self.name,self.number1,self.item[1])
        self.answer = self.number1 * self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,number1,number2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item1)
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'><font style='font-size:0.8em'>%d</font></td>"%(self.color1,x+1)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>He paid $%d.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:
        [Person.Auntyname] bought 6 <chairs> for $123 each. How much did she pay for the <chairs> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = ['chairs','tables','couches','mattresses','phones','bicycles','TV sets','washing machines','coffee tables','computer tables','office tables','airplane tickets','refrigerators']
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.AuntyName)
        self.number1 = randint(3,9)
        self.number2 = randint(100,500)

        self.problem = "%s bought %d %s for $%d each. How much did she pay for the %s altogether?"%(self.name,self.number1,self.item,self.number2,self.item)
        self.answer = self.number1 * self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.number1,self.number2,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,number1,number2,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item)
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'><font style='font-size:0.75em'>%d</font></td>"%(self.color1,x+1)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>She paid $%d for the %s altogether.</font>"%(answer,item)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:
        There are 43 <pages> in a <photo album>. Each <page> has 8 <photos>. How many <photos> are there in the <photo album>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['pages','photo album','page','photos'],
                      ['sheets of stickers','sticker book','sheet','stickers'],
                      ['boxes of crayons','carton','box','crayons'],
                      ['bundles of paper','box','bundle','sheets'],
                      ['stacks of cards','box','stack','sheets'],
                      ['packs of files','carton','pack','files'],
                      ['packets of cookies','tin','packet','cookies'],
                      ['bags of marbles','jar','bag','marbles'],
                      ['bags of fruit','basket','bag','fruits'],
                      ['bags of candies','jar','bag','candies']]
               
        self.item = random.choice(self.items)

        self.number1 = randint(3,9)
        self.number2 = randint(30,80)

        self.problem = "There are %d %s in a %s. Each %s has %d %s. How many %s are there in the %s?"%(self.number2,self.item[0],self.item[1],self.item[2],
                                                                                                       self.number1,self.item[3],self.item[3],self.item[1])
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[3]
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.number1,self.number2,self.item[1],self.item[2],self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,number1,number2,item1,item2,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'><font style='font-size:0.7em'>%s 1</font></td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'><font style='font-size:0.7em'>%s 2</font></td><td colspan=2 style='height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>. . . . .</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px'><font style='font-size:0.7em'>%s %d</font></td></tr>"%(unit,self.color1,item2,self.color1,item2,self.color1,item2,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5><img src='/images/explanation/P3_model_down_brace_small5.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>There are %d %s in the %s.</font>"%(answer,item3,item1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType12(self):       
        '''e.g.:
        [Person.Auntyname] <bought> 5 <boxes> of <muffins> <for a party>. If there were 6 <muffins> in each <box>, how many <muffins> did she <buy>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['bought','boxes','muffins','for a Christmas party at work','box','buy'],
                      ['baked','boxes','tarts','for her class','box','bake'],
                      ['sold','bags','curry puffs','to a customer','bag','sell'],
                      ['bought','plates','nuggets','at a food court','plate','buy'],
                      ['sold','boxes','nuggets','to a customer','box','sell'],
                      ["fried","bags","nuggets","for her son's birthday party","bag","fry"],
                      ['bought','tins','cookies','for a party','tin','buy'],
                      ['baked','trays','cookies','for a birthday party','tray','bake'],
                      ['bought','bunches','bananas','at a supermarket','bunch','buy'],
                      ['made','trays','cupcakes','for her birthday','tray','make'],
                      ['bought','packets','mechanical pencils','for her grandchildren','packet','buy'],
                      ['sold','packets','sticker sheets','at her book store','packet','sell']]
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.AuntyName)
        self.number1 = randint(3,9)
        self.number2 = randint(4,9)

        self.problem = "%s %s %d %s of %s %s. If there were %d %s in each %s, how many %s did she %s altogether?"%(self.name,self.item[0],self.number1,self.item[1],
                                                                                                        self.item[2],self.item[3],self.number2,self.item[2],
                                                                                                        self.item[4],self.item[2],self.item[5])
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[2]
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[2],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType12(self,problem,answer,number1,number2,item0,item2,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item2)
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'><font style='font-size:0.75em'>%s %d</font></td>"%(self.color1,item4,x+1)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(number1,number2,answer)
        self.solution_text = self.solution_text + "She %s %d %s altogether.</font>"%(item0,answer,item2)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType13a(self):       
        '''e.g.:
        [Person.Name] <gets> $8 <of pocketmoney a day>. How much <pocketmoney> does he/she <get> in a <year>?<br><br>(Hint: There are 365 days in a year.)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['gets','in pocketmoney a day','pocketmoney','get','year','in pocketmoney in a year'],
                      ['spends','a day on food and drinks','money','spend on food and drinks','year','on food and drinks in a year'],
                      ['saves','a day','money','save','year','in a year'],
                      ['receives','a day for doing odd jobs','money','receive','year for doing odd jobs','in a year for doing odd jobs'],
                      ['gives away','a day to poor children','money','give away to poor children','year','to poor children in a year']]
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.BoyName)
        self.number1 = randint(3,9)

        self.problem = "%s %s $%d %s. How much %s does he %s in a %s?<br><br>[Hint: There are 365 days in a year.]"%(self.name,self.item[0],self.number1,
                                                                                                        self.item[1],self.item[2],self.item[3],
                                                                                                        self.item[4])
        self.answer = self.number1 * 365
        
        self.unit = ""
        self.dollar_unit = "$"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.number1,365,self.item[0],self.item[5],1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,'dollar_unit':self.dollar_unit}

    def GenerateProblemType13b(self):       
        '''e.g.:
        [Person.Name] <earns> $560 <a month>. How much <money> does he/she <earn> in 5 months?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['earns','a month','money','earn',''],
                      ['gets','in pocketmoney a month','pocketmoney','get','in pocketmoney'],
                      ['spends','a month on groceries','money','spend on groceries','on groceries'],
                      ['saves','a month','money','save',''],
                      ['donates','a month to charity','money','donate to charity','to charity']]
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.GirlName)
        self.number1 = randint(3,9)
        self.number2 = randint(112,800)

        self.problem = "%s %s $%d %s. How much %s does she %s in %d months?"%(self.name,self.item[0],self.number2,self.item[1],self.item[2],
                                                                                self.item[3],self.number1)
        
        self.answer = self.number1 * self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[4],2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType13(self,problem,answer,number1,number2,item0,item5,flag,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if flag==1:
            #beginning of model
            self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
            
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'><font style='font-size:0.7em'>Day 1</font></td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'><font style='font-size:0.7em'>Day 2</font></td><td colspan=2 style='height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>. . . . .</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px'><font style='font-size:0.7em'>Day 365</font></td></tr>"%(unit,self.color1,self.color1,self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5><img src='/images/explanation/P3_model_down_brace_small5.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>?</td></tr>"
            self.solution_text = self.solution_text + "</table><br><br>"
            #end of model

            self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,number1)
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>He %s $%d %s.</font>"%(item0,answer,item5)
        else:
            #beginning of model
            self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
            
            self.solution_text = "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td></tr>"%(number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
    
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'></td>"
            for x in range(0, number1):
                self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'><font style='font-size:0.75em'>Month %d</font></td>"%(self.color1,x+1)
            self.solution_text = self.solution_text + "</tr>"
    
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number1,number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number1)
            self.solution_text = self.solution_text + "</table><br><br>"
            #end of model

            self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,number1)
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>She %s $%d %s in %d months.</font>"%(item0,answer,item5,number1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType14(self):       
        '''e.g.:
        How many <postcards> did [Person.name] <make> in a week if he/she <made> 121 <postcards> each day of the week?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['postcards','make','made'],
                      ['kites','sell','sold'],
                      ['pies','bake','baked'],
                      ['exam papers','correct','corrected'],
                      ['fruits','pick','picked'],
                      ['decorative cards','make','made'],
                      ['math questions','solve','solved'],
                      ['handkerchiefs','stitch','stitched'],
                      ['sea shells','collect','collected'],
                      ['dishes','wash','washed']]
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.GirlName)
        self.number1 = 7
        self.number2 = randint(112,198)

        self.problem = "How many %s did %s %s in a week if she %s %d %s each day of the week?"%(self.item[0],self.name,self.item[1],
                                                                                                self.item[2],self.number2,self.item[0])
        
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[0]
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.number2,self.item[0],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType14(self,problem,answer,number2,item0,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<font class='ExplanationFont'> 1 week &nbsp;=&nbsp; 7 days</font><br><br>"

        self.solution_text = self.solution_text + "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item0)
        for x in range(0, 7):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'><font style='font-size:0.75em'>Day %d</font></td>"%(self.color1,x+1)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=7 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small7.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=7>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,7)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>She %s %d %s in a week.</font>"%(item2,answer,item0)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType15a(self):       
        '''e.g.:
        [Person.Name] <had> 4 <jars> <containing> 230 <marbles> each. How many <marbles> did [Person.Name] <have> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['had','jars','containing','marbles','have','jar'],['had','cases','containing','tacks','have','case'],
                      ['collected','albums','of','stamps','collect','album'],['shared','packets','containing','magnets','share','packet'],
                      ['bought','packs','containing','rubberbands','buy','pack'],['bought','packets','of','beads','buy','packet'],
                      ['sold','packs','with','buttons','sell','pack'],['sold','bags','containing','ice-cream sticks','sell','bag'],
                      ['won','games','with','points','win','game'],['won','game sets','with','stars','win','set'],
                      ['got','cases','containing','push pins','get','case'],['received','cases','with','paper clips','receive','case'],
                      ['made','bags','of','flags','make','bag'],['made','scrapbooks','with','stickers','make','book']]
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.PersonName)
        self.number1 = randint(3,9)
        self.number2 = randint(112,198)

        self.problem = "%s %s %d %s %s %d %s each. How many %s did %s %s altogether?"%(self.name,self.item[0],self.number1,self.item[1],
                                                                                       self.item[2],self.number2,self.item[3],self.item[3],
                                                                                       self.name,self.item[4])
        
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[3]
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.name,self.number1,self.number2,self.item[0],self.item[3],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType15a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,'dollar_unit':self.dollar_unit}

    def GenerateProblemType15b(self):       
        '''e.g.:
        A <supplier> <supplied> 4 identical <boxes> <containing> 230 <T-shirts> each. How many <T-shirts> did the <supplier> <supply> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['supplier','supplied','boxes','containing','T-shirts','supply','box'],
                      ['shopkeeper','bought','cartons','containing','shirts','buy','carton'],
                      ['department store','purchased','bags','of','frocks','purchase','store'],
                      ['tailor','stitched','lots','of','scarves','stitch','lot'],
                      ['tailor','sewed','bundles','of','ties','sew','bundle'],
                      ['factory','produced','batches','of','phones','produce','batch'],
                      ['fruiterer','packed','cartons','with','pears','pack','carton'],
                      ['grocery store','bought','sacks','containing','potatoes','buy','sack'],
                      ['farmer','packed','boxes','with','carrots','pack','box'],
                      ['farmer','planted','fields','with','fruit trees','plant','field'],
                      ['vendor','bought','boxes','of','spoons','buy','box'],
                      ['manufacturer','produced','lots','of','batteries','produce','lot'],
                      ['printer','printed','batches','of','posters','print','batch'],
                      ['bookstore','purchased','boxes','containing','erasers','purchase','box'],
                      ['library','had','shelves','containing','books','have','shelf']]

        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.PersonName)
        self.number1 = randint(3,9)
        self.number2 = randint(112,198)

        self.problem = "A %s %s %d identical %s %s %d %s each. How many %s did the %s %s altogether?"%(self.item[0],self.item[1],self.number1,
                                                                                                       self.item[2],self.item[3],self.number2,
                                                                                                       self.item[4],self.item[4],self.item[0],
                                                                                                       self.item[5])
        
        doer = "The %s"%(self.item[0])
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[4]
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,doer,self.number1,self.number2,self.item[1],self.item[4],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType15b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType15(self,problem,answer,name,number1,number2,item0,item3,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item3)
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'><font style='font-size:0.7em'>%s %d</font></td>"%(self.color1,item,x+1)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s %s %d %s altogether.</font>"%(name,item0,answer,item3)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType16(self):       
        '''e.g.:
        [Person.Girlname 1], [Person.Girlname 2], [Person.Girlname 3], [Person.Girlname 4] and [Person.Girlname 5] each had 224 <photos>. How many <photos> did they have altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = ['photos','ribbons','sea shells','erasers','crayons','markers','hair clips','gummies','can tabs','hair ties','cards','rings']

        self.item = random.choice(self.items)

        self.names = random.sample(PersonName.GirlName,5)
        
        self.number1 = randint(3,5)
        self.number2 = randint(112,298)


        if self.number1 == 3:
            self.problem = "%s, %s and %s each had %d %s. How many %s did they have altogether?"%(self.names[0],self.names[1],self.names[2],
                                                                                                  self.number2,self.item,self.item)
        elif self.number1 == 4:
            self.problem = "%s, %s, %s and %s each had %d %s. How many %s did they have altogether?"%(self.names[0],self.names[1],self.names[2],
                                                                                                  self.names[3],self.number2,self.item,self.item)
        else:
            self.problem = "%s, %s, %s, %s and %s each had %d %s. How many %s did they have altogether?"%(self.names[0],self.names[1],
                                                                                                          self.names[2],self.names[3],
                                                                                                          self.names[4],self.number2,
                                                                                                          self.item,self.item)
                
        self.answer = self.number1 * self.number2
        
        self.unit = self.item
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType16(self.problem,self.answer,self.number1,self.number2,self.item,self.names,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType16",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType16(self,problem,answer,number1,number2,item,names,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item)
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'><font style='font-size:0.75em'>%s</font></td>"%(self.color1,names[x])
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>They had %d %s altogether.</font>"%(answer,item)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType17(self):       
        '''e.g.:
        [Person.Girlname 1] <got> 480 <points in a computer game>. [Person.Girlname 2] <got> twice/thrice as many <points> as [Person.Girlname 1]. How many <points> did [Person.Girlname 2] <get>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['got','points in a computer game','points','get'],['had','plums with her','plums','have'],
                      ['baked','buns in her bakery','buns','bake'],['clicked','photos during her vacation','photos','click'],
                      ['used','beads to make a necklace','beads','use'],['collected','stamps in an album','stamps','collect'],
                      ['collected','books for a book drive','books','collect'],['gave away','marbles','marbles','give away'],
                      ['gave away','sweets to her friends','sweets','give away'],
                      ['solved','questions to prepare for her maths exam','questions','solve']]

        self.item = random.choice(self.items)

        self.names = random.sample(PersonName.GirlName,2)
        
        self.number1s = random.choice([[2,"twice"],
                                       [3,"thrice"],
                                       [4,"4 times"],
                                       [5,"5 times"]
                                       ])
        self.number1 = self.number1s[0]
        self.number2 = randint(112,198)

        self.problem = "%s %s %d %s. %s %s %s as many %s as %s. How many %s did %s %s?"%(self.names[0],self.item[0],self.number2,self.item[1],
                                                                                         self.names[1],self.item[0],self.number1s[1],self.item[2],
                                                                                         self.names[0],self.item[2],self.names[1],self.item[3])
                
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[2]
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType17(self.problem,self.answer,self.number1,self.number2,self.names,self.item[0],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType17",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType17(self,problem,answer,number1,number2,name,item0,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td></tr>"%(name[0],self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(name[1])
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + self.MultiplicationExplanation(number2,number1)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s %s %d %s.</font>"%(name[1],item0,answer,item2)

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
        
    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        Find the product of %d and %d.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1"
        self.CheckAnswerType = 1

        self.numbers = random.choice([[2,random.sample([1,2,3,4],3)],
                                      [3,random.sample([1,2,3],3)],
                                      [4,random.sample([1,1,2,2],3)],
                                      [random.choice([5,6,7,8,9]),[1,1,1]]
                                      ])
        
        self.number1 = self.numbers[0]
        self.number2 = ""
        
        for i in range(len(self.numbers[1])):
            self.number2 = self.number2 + str(self.numbers[1][i])
        
        self.number2 = int(self.number2)
        
        self.flag = randint(1,7)
        self.flag1 = 0
        
        self.wrongAnswers = []        
        
        if self.flag < 7:        
            self.problem1 = "Find the product of %d and %d."%(self.number2,self.number1)
            self.problem2 = "What is the product of %d and %d?"%(self.number2,self.number1)
            self.problem3 = "What is %d &times; %d?"%(self.number2,self.number1)
            self.problem4 = "The product of %d and %d is ____."%(self.number2,self.number1)
            self.problem5 = "%d &times; %d = ?"%(self.number2,self.number1)
            self.problem6 = "Multiply.<br><br><table><tr>"
            self.problem6 = self.problem6 + "<td>&nbsp;</td><td>"+str(self.number2)[0]+"</td><td>"+str(self.number2)[1]+"</td><td>"+str(self.number2)[2]+"</td></tr>"
            self.problem6 = self.problem6 + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>"+str(self.number1)+"</td></tr>"
            self.problem6 = self.problem6 + "<tr><td colspan=4 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line_4.png' /></td></tr></table>"
            self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6])
            self.answer = self.number1 * self.number2
            self.wrongAnswers = [(self.number1-1)*self.number2,self.number1*(self.number2-1),self.number1*(self.number2-10)]
            if self.number1!=2:
                self.wrongAnswers.append((self.number1-2)*self.number2)
        else:       
            self.flag1 = randint(1,2)
            if self.flag1 == 1:
                self.problem = ""
                for i in range(self.number1-1):
                    self.problem = self.problem + str(self.number2)+" + "
                self.problem = self.problem + str(self.number2)+" &nbsp;=&nbsp; _____ &nbsp;&times;&nbsp; "+str(self.number1)
                self.answer =  self.number2
                self.wrongAnswers = [self.number2-10,self.number1,self.number2-1]
            else:
                self.problem = ""
                for i in range(self.number1-1):
                    self.problem = self.problem + str(self.number2)+" + "
                self.problem = self.problem + str(self.number2)+" &nbsp;=&nbsp; "+str(self.number2)+" &nbsp;&times;&nbsp; ___"
                self.answer =  self.number1
                self.wrongAnswers = [self.number2,self.number1-1,self.number1+1]               
                
        self.template = "MCQTypeProblems.html"          
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.flag,self.flag1,self.number2,self.number1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        What is the number in the box? / Find the missing number.
            1 2 _
        &times;     3
        -------------
            3 6 9'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ2"
        self.CheckAnswerType = 1

        self.numbers = random.choice([[2,random.sample([1,2,3,4],3)],
                                      [3,random.sample([1,2,3],3)],
                                      [4,random.sample([1,1,2,2],3)],
                                      [random.choice([5,6,7,8,9]),[1,1,1]]
                                      ])
        
        self.number1 = self.numbers[0]
        self.number2 = ""
        
        for i in range(len(self.numbers[1])):
            self.number2 = self.number2 + str(self.numbers[1][i])
        
        self.number2 = int(self.number2)
        self.number = self.number1 * self.number2
        
        self.flag = randint(1,2)

        self.problem = "Find the missing digit.<br><br>"
        if self.flag == 1:
            self.missingDigit = randint(0,2)        
            self.problem = self.problem + "<table border=0><tr><td>&nbsp;</td>"
            for i in range(3):
                if i!=self.missingDigit:
                    self.problem = self.problem + "<td>"+str(self.number2)[i]+"</td>"
                else:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
            self.problem = self.problem + "</tr>"
            self.problem = self.problem + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>"+str(self.number1)+"</td></tr>"
            self.problem = self.problem + "<tr><td colspan=4 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line_4.png' /></td></tr>"
            self.problem = self.problem + "<tr><td>&nbsp;</td><td>"+str(self.number)[0]+"</td><td>"+str(self.number)[1]+"</td><td>"+str(self.number)[2]+"</td></tr></table>"
            self.answer = str(self.number2)[self.missingDigit]
        else:
            self.missingDigit = randint(0,2)        
            self.problem = self.problem + "<table border=0>"
            self.problem = self.problem + "<tr><td>&nbsp;</td><td>"+str(self.number2)[0]+"</td><td>"+str(self.number2)[1]+"</td><td>"+str(self.number2)[2]+"</td></tr>"
            self.problem = self.problem + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>"+str(self.number1)+"</td></tr>"
            self.problem = self.problem + "<tr><td colspan=4 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line_4.png' /></td></tr>"
            self.problem = self.problem + "<tr><td>&nbsp;</td>"
            for i in range(3):
                if i!=self.missingDigit:
                    self.problem = self.problem + "<td>"+str(self.number)[i]+"</td>"
                else:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
            self.problem = self.problem + "</tr></table>"
            self.answer = str(self.number)[self.missingDigit]
        
        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = str(randint(0,9))
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer!= self.answer:
                self.wrongAnswers.append(self.wrongAnswer)
                            
        self.template = "MCQTypeProblems.html"          
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.flag,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
        There are 32 children in a <class/group/club/team/party/room>. Each child collects 3 <stamps>. How many <stamps> does the <class/group/club/team/party/room> collect altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ3"
        self.CheckAnswerType = 1

        self.numbers = random.choice([[2,random.sample([1,2,3,4],2)],
                                      [3,random.sample([1,2,3],2)],
                                      [4,random.sample([1,1,2,2],2)],
                                      [random.choice([5,6,7,8,9]),[1,1]]
                                      ])
        
        self.number1 = self.numbers[0]
        self.number2 = ""
        
        for i in range(len(self.numbers[1])):
            self.number2 = self.number2 + str(self.numbers[1][i])
        
        self.number2 = int(self.number2)
        
        self.item1 = random.choice(['class','group','club','team'])
        self.item2 = random.choice(['stamps','picture postcards','coins','beads','seashells','twigs','dried leaves','animal cards','coins','comic books','storybooks'])
        
        self.problem = "There are %d children in a %s. Each child collects %d %s. How many %s does the %s collect altogether?"%(self.number2,self.item1,
                                                                                                                                self.number1,self.item2,self.item2,self.item1)
  
        self.answer = self.number1 * self.number2
        
        self.unit = self.item2
        self.dollar_unit = ""

        self.template = "MCQTypeProblems.html"          

        self.wrongAnswers = [(self.number1-1)*self.number2,self.number1*(self.number2-1),self.number1*(self.number2-2)]
        if self.number1!=2:
            self.wrongAnswers.append((self.number1-2)*self.number2)
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.item1,self.item2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ4(self):
        '''e.g.:
        [Person.Unclename] sells 122 <apples> in 1 <day/week>. How many <apples> does he sell in 4 <days/weeks>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ4"
        self.CheckAnswerType = 1

        self.numbers = random.choice([[2,random.sample([1,2,3,4],2)],
                                      [3,random.sample([1,2,3],2)],
                                      [4,random.sample([1,1,2,2],2)],
                                      [random.choice([5,6,7,8,9]),[1,1]]
                                      ])
        
        self.number1 = self.numbers[0]
        self.number2 = ""
        
        for i in range(len(self.numbers[1])):
            self.number2 = self.number2 + str(self.numbers[1][i])
        
        self.number2 = int(self.number2)
        
        self.name = random.choice(PersonName.UncleName)
        
        self.item1 = random.choice(['day','week'])
        self.item2 = random.choice(['apples','tickets','pears','pumpkins','watermelons','muffins','cakes','carpets','books','pots'])
        
        self.problem = "%s sells %d %s in 1 %s. How many %s does he sell in %d %ss?"%(self.name,self.number2,self.item2,self.item1,self.item2,
                                                                                      self.number1,self.item1)
  
        self.answer = self.number1 * self.number2
        
        self.unit = self.item2
        self.dollar_unit = ""

        self.template = "MCQTypeProblems.html"          

        self.wrongAnswers = [(self.number1-1)*self.number2,self.number1*(self.number2-1),self.number1*(self.number2-2)]
        if self.number1!=2:
            self.wrongAnswers.append((self.number1-2)*self.number2)
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.item1,self.item2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ5(self):
        '''e.g.:
        7 &times; 3 = ______ &minus; 4'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ5"
        self.CheckAnswerType = 1

        self.number1 = randint(3,9)
        self.number2 = randint(3,9)
        self.number4 = randint(3,9)
        self.number3 = self.number1*self.number2 + self.number4
        
        self.flag = randint(1,2)

        self.problem = "Find the missing number in the blank.<br><br>"        
        if self.flag == 1:
            self.problem = self.problem + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&minus;&nbsp; ___"%(self.number1,self.number2,self.number3)
            self.answer = self.number4
            self.wrongAnswers = []
            while len(self.wrongAnswers)!=3:
                self.wrongAnswer = randint(0,9)
                if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                    self.wrongAnswers.append(self.wrongAnswer)
        else:
            self.problem = self.problem + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; ___ &nbsp;&minus;&nbsp; %d"%(self.number1,self.number2,self.number4)
            self.answer = self.number3
            self.wrongAnswers = [self.answer-1,self.answer+1,self.answer-2,self.answer+2]

        self.unit = ""
        self.dollar_unit = ""

        self.template = "MCQTypeProblems.html"          
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.flag,self.number1,self.number2,self.number3,self.number4,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ6(self):
        '''e.g.:
        Find the product of %d and %d.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ6"
        self.CheckAnswerType = 1

        self.number1 = randint(3,9)
        self.number2 = randint(112,189)

        self.problem1 = "Find the product of %d and %d."%(self.number2,self.number1)
        self.problem2 = "What is the product of %d and %d?"%(self.number2,self.number1)
        self.problem3 = "What is %d &times; %d?"%(self.number2,self.number1)
        self.problem4 = "The product of %d and %d is ____."%(self.number2,self.number1)
        self.problem5 = "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; ?"%(self.number2,self.number1)
        self.problem6 = "Multiply.<br><br><table border=0><tr>"
        self.problem6 = self.problem6 + "<td>&nbsp;</td><td>"+str(self.number2)[0]+"</td><td>"+str(self.number2)[1]+"</td><td>"+str(self.number2)[2]+"</td></tr>"
        self.problem6 = self.problem6 + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>"+str(self.number1)+"</td></tr>"
        self.problem6 = self.problem6 + "<tr><td colspan=4 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line_4.png' /></td></tr></table>"

        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6])
        self.answer = self.number1 * self.number2
        
        self.wrongAnswers = [(self.number1-1)*self.number2,self.number2,self.number1*(self.number2-1),self.number1*(self.number2-10)]
  
        self.template = "MCQTypeProblems.html"          
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ7(self):
        '''e.g.:
        What is the number in the box? / Find the missing number.
            1 2 _
        &times;     3
        -------------
            3 6 9'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ7"
        self.CheckAnswerType = 1

        self.numbers = random.choice([[3,randint(112,288)],
                                     [4,randint(112,223)],
                                     [5,randint(112,188)],
                                     [6,randint(112,150)],
                                     [7,randint(112,140)],
                                     [8,randint(112,124)],])
        
        self.number1 = self.numbers[0]
        self.number2 = self.numbers[1]
        self.number = self.number1 * self.number2
        
        self.flag = randint(1,2)
        
        self.problem = "Find the missing digit.<br><br>"
        if self.flag == 1:
            self.missingDigit = randint(0,2)        
            self.problem = self.problem + "<table border=0><tr><td>&nbsp;</td>"
            for i in range(3):
                if i!=self.missingDigit:
                    self.problem = self.problem + "<td>"+str(self.number2)[i]+"</td>"
                else:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
            self.problem = self.problem + "</tr>"
            self.problem = self.problem + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>"+str(self.number1)+"</td></tr>"
            self.problem = self.problem + "<tr><td colspan=4 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line_4.png' /></td></tr>"
            self.problem = self.problem + "<tr><td>&nbsp;</td><td>"+str(self.number)[0]+"</td><td>"+str(self.number)[1]+"</td><td>"+str(self.number)[2]+"</td></tr></table>"
            self.answer = str(self.number2)[self.missingDigit]
        else:
            self.missingDigit = randint(0,2)        
            self.problem = self.problem + "<table border=0>"
            self.problem = self.problem + "<tr><td>&nbsp;</td><td>"+str(self.number2)[0]+"</td><td>"+str(self.number2)[1]+"</td><td>"+str(self.number2)[2]+"</td></tr>"
            self.problem = self.problem + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>"+str(self.number1)+"</td></tr>"
            self.problem = self.problem + "<tr><td colspan=4 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/P3ProblemImages/operation_line_4.png' /></td></tr>"
            self.problem = self.problem + "<tr><td>&nbsp;</td>"
            for i in range(3):
                if i!=self.missingDigit:
                    self.problem = self.problem + "<td>"+str(self.number)[i]+"</td>"
                else:
                    self.problem = self.problem + "<td style='vertical-align:bottom;padding:0px 0px 0px 0px'><img src='/images/P3ProblemImages/empty_digit_box.png' /></td>"
            self.problem = self.problem + "</tr></table>"
            self.answer = str(self.number)[self.missingDigit]
  
        self.template = "MCQTypeProblems.html"          
        
        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = str(randint(0,9))
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer)
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.flag,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ8(self):
        '''e.g.:
        There are 123 <lorries> in a <parking garage>. <Each lorry has 6 wheels. How many wheels are there in all?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ8"
        self.CheckAnswerType = 1
        
        self.items = [['lorries','parking garage','Each lorry has 6 wheels. How many wheels are there in all?','6','wheels','There are','in all','lorry'],
                      ['cars','car park','Each car has 4 wheels. How many wheels are there in all?','4','wheels','There are','in all','car'],
                      ['cars','showroom','Each car has 6 lights. How many lights are there in all?','6','lights','There are','in all','car'],
                      ['animals','zoo','A boy counts 4 legs on each animal. How many legs does he count altogether?','4','legs','He counts','altogether','animal'],
                      ['birds','park','Each bird has 2 feet. How many feet are there in all?','2','feet','There are','in all','bird'],
                      ['walls','museum','Each wall has 7 paintings. How many paintings are there in all?','7','paintings','There are','in all','wall'],
                      ['apartments','building','Each apartment has 8 windows. How many windows are there altogether?','8','windows','There are','altogether','apartment'],
                      ['pupils','school','The school principal gives away 3 books to each pupil. How many books does the principal give away altogether?','3','books','The principal gives away','altogether','pupil']]
        
        self.item = random.choice(self.items)

        self.number1 = int(self.item[3])
        self.number2 = randint(112,189)
        
        self.problem = "There are %d %s in a %s. %s"%(self.number2,self.item[0],self.item[1],self.item[2])
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[4]
        self.dollar_unit = ""
  
        self.template = "MCQTypeProblems.html"          
        
        self.wrongAnswers = [self.number1*(self.number2-1),self.number1*(self.number2+1),self.number1*(self.number2-2),self.number1*(self.number2+2)]
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2,self.item[5],self.item[6],self.item[7],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ9(self):
        '''e.g.:
        <Child tickets at an amusement park> are sold at $16 each. [Person.Unclename] bought 4 <child tickets>. How much did he pay?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ9"
        self.CheckAnswerType = 1
        
        self.items = [['Child tickets at an amusement park','child tickets',randint(12,40)],
                      ['Adult tickets at an amusement park','adult tickets',randint(12,40)],
                      ['Entrance tickets to a water park','entrance tickets',randint(12,40)],
                      ['Child tickets at a theme park','child tickets',randint(12,40)],
                      ['Adult tickets at a theme park','adult tickets',randint(12,40)],
                      ['Entrance tickets to an animal safari','entrance tickets',randint(12,40)],
                      ['Tram tickets at Singapore Night Safari','tram tickets',randint(12,40)],
                      ['Tram tickets at a bird park','tram tickets',randint(12,40)],
                      ['Adult tickets to Singapore Zoo','adult tickets',randint(12,40)],
                      ['Tickets to a musical show','tickets',randint(12,40)],
                      ['Entrance tickets at a science museum','entrance tickets',randint(12,40)],
                      ['Entrance tickets at a coins and stamps museum','entrance tickets',randint(12,40)],
                      ['Coupon booklets at a carnival','coupon booklets',randint(12,40)]]
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.UncleName)
        self.number1 = randint(3,9)
        self.number2 = self.item[2]

        self.problem = "%s are sold at $%d each. %s bought %d %s. How much did he pay?"%(self.item[0],self.number2,self.name,self.number1,self.item[1])
        self.answer = self.number1 * self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
  
        self.template = "MCQTypeProblems.html"          
        
        self.wrongAnswers = [self.number1*(self.number2-1),self.number1*(self.number2+1),self.number1*(self.number2-2),self.number1*(self.number2+2)]
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ10(self):
        '''e.g.:
        [Person.Auntyname] bought 6 <chairs> for $123 each. How much did she pay for the <chairs> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ10"
        self.CheckAnswerType = 1
        
        self.items = ['chairs','tables','couches','mattresses','phones','bicycles','TV sets','washing machines','coffee tables','computer tables','office tables','airplane tickets','refrigerators']
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.AuntyName)
        self.number1 = randint(3,9)
        self.number2 = randint(100,500)

        self.problem = "%s bought %d %s for $%d each. How much did she pay for the %s altogether?"%(self.name,self.number1,self.item,self.number2,self.item)
        self.answer = self.number1 * self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
  
        self.template = "MCQTypeProblems.html"          
        
        self.wrongAnswers = [self.number1*(self.number2-1),self.number1*(self.number2+1),self.number1*(self.number2-2),self.number1*(self.number2+2)]
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.number1,self.number2,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ11(self):
        '''e.g.:
        There are 43 <pages> in a <photo album>. Each <page> has 8 <photos>. How many <photos> are there in the <photo album>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ11"
        self.CheckAnswerType = 1
        
        self.items = [['pages','photo album','page','photos'],
                      ['sheets of stickers','sticker book','sheet','stickers'],
                      ['boxes of crayons','carton','box','crayons'],
                      ['bundles of paper','box','bundle','sheets'],
                      ['stacks of sheets','box','stack','sheets'],
                      ['packs of files','carton','pack','files'],
                      ['packets of cookies','tin','packet','cookies'],
                      ['bags of marbles','jar','bag','marbles'],
                      ['bags of fruit','basket','bag','fruits'],
                      ['bags of candies','jar','bag','candies']]
               
        self.item = random.choice(self.items)

        self.number1 = randint(3,9)
        self.number2 = randint(30,80)

        self.problem = "There are %d %s in a %s. Each %s has %d %s. How many %s are there in the %s?"%(self.number2,self.item[0],self.item[1],self.item[2],
                                                                                                       self.number1,self.item[3],self.item[3],self.item[1])
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[3]
        self.dollar_unit = ""
  
        self.template = "MCQTypeProblems.html"          
        
        self.wrongAnswers = [self.number1*(self.number2-1),self.number1*(self.number2+1),self.number1*(self.number2-2),self.number1*(self.number2+2)]
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.number1,self.number2,self.item[1],self.item[2],self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ12(self):
        '''e.g.:
        [Person.Auntyname] <bought> 5 <boxes> of <muffins> <for a party>. If there were 6 <muffins> in each <box>, how many <muffins> did she <buy>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ12"
        self.CheckAnswerType = 1
        
        self.items = [['bought','boxes','muffins','for a Christmas party at work','box','buy'],
                      ['baked','boxes','tarts','for her class','box','bake'],
                      ['sold','bags','curry puffs','to a customer','bag','sell'],
                      ['bought','plates','nuggets','at a food court','plate','buy'],
                      ['sold','boxes','nuggets','to a customer','box','sell'],
                      ["fried","bags","nuggets","for her son's birthday party","bag","fry"],
                      ['bought','tins','cookies','for a party','tin','buy'],
                      ['baked','trays','cookies','for a birthday party','tray','bake'],
                      ['bought','bunches','bananas','at a supermarket','bunch','buy'],
                      ['made','trays','cupcakes','for her birthday','tray','make'],
                      ['bought','packets','mechanical pencils','for her grandchildren','packet','buy'],
                      ['sold','packets','sticker sheets','at her book store','packet','sell']]
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.AuntyName)
        self.number1 = randint(3,9)
        self.number2 = randint(4,9)

        self.problem = "%s %s %d %s of %s %s. If there were %d %s in each %s, how many %s did she %s altogether?"%(self.name,self.item[0],self.number1,self.item[1],
                                                                                                        self.item[2],self.item[3],self.number2,self.item[2],
                                                                                                        self.item[4],self.item[2],self.item[5])
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[2]
        self.dollar_unit = ""
  
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number1*(self.number2-1),self.number1*(self.number2+1),self.number1*(self.number2-2),self.number1*(self.number2+2)]
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[2],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ13a(self):
        '''e.g.:
        [Person.Name] <gets> $8 <of pocketmoney a day>. How much <pocketmoney> does he/she <get> in a <year>? (There are 365 days in a year.)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ13a"
        self.CheckAnswerType = 1
        
        self.items = [['gets','in pocketmoney a day','pocketmoney','get','year','in pocketmoney in a year'],
                      ['spends','a day on food and drinks','money','spend on food and drinks','year','on food and drinks in a year'],
                      ['saves','a day','money','save','year','in a year'],
                      ['receives','a day for doing odd jobs','money','receive','year for doing odd jobs','in a year for doing odd jobs'],
                      ['gives away','a day to poor children','money','give away to poor children','year','to poor children in a year']]
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.BoyName)
        self.number1 = randint(3,9)
        self.number2 = 365

        self.problem = "%s %s $%d %s. How much %s does he %s in a %s?<br><br>[Hint: There are 365 days in a year.]"%(self.name,self.item[0],self.number1,
                                                                                                        self.item[1],self.item[2],self.item[3],
                                                                                                        self.item[4])
        self.answer = self.number1 * self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
  
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number1*(self.number2-1),self.number1*(self.number2+1),self.number1*(self.number2-2),self.number1*(self.number2+2)]
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.number1,365,self.item[0],self.item[5],1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ13b(self):
        '''e.g.:
        [Person.Name] <earns> $560 <a month>. How much <money> does he/she <earn> in 5 months?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ13b"
        self.CheckAnswerType = 1
        
        self.items = [['earns','a month','money','earn',''],
                      ['gets','in pocketmoney a month','pocketmoney','get','in pocketmoney'],
                      ['spends','a month on groceries','money','spend on groceries','on groceries'],
                      ['saves','a month','money','save',''],
                      ['donates','a month to charity','money','donate to charity','to charity']]
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.GirlName)
        self.number1 = randint(3,9)
        self.number2 = randint(112,800)

        self.problem = "%s %s $%d %s. How much %s does she %s in %d months?"%(self.name,self.item[0],self.number2,self.item[1],self.item[2],
                                                                                self.item[3],self.number1)
        
        self.answer = self.number1 * self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
  
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number1*(self.number2-1),self.number1*(self.number2+1),self.number1*(self.number2-2),self.number1*(self.number2+2)]
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[4],2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ14(self):
        '''e.g.:
        How many <postcards> did [Person.name] <make> in a week if he/she <made> 121 <postcards> each day of the week?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ14"
        self.CheckAnswerType = 1
        
        self.items = [['postcards','make','made'],
                      ['kites','sell','sold'],
                      ['pies','bake','baked'],
                      ['exam papers','correct','corrected'],
                      ['fruits','pick','picked'],
                      ['decorative cards','make','made'],
                      ['math questions','solve','solved'],
                      ['handkerchiefs','stitch','stitched'],
                      ['sea shells','collect','collected'],
                      ['dishes','wash','washed']]
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.GirlName)
        self.number1 = 7
        self.number2 = randint(112,198)

        self.problem = "How many %s did %s %s in a week if she %s %d %s each day of the week?"%(self.item[0],self.name,self.item[1],
                                                                                                self.item[2],self.number2,self.item[0])
        
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[0]
        self.dollar_unit = ""
  
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number1*(self.number2-1),self.number1*(self.number2+1),self.number1*(self.number2-2),self.number1*(self.number2+2)]
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.number2,self.item[0],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ15a(self):
        '''e.g.:
        Person.Name] <had> 4 <jars> <containing> 230 <marbles> each. How many <marbles> did [Person.Name] <have> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ15a"
        self.CheckAnswerType = 1
        
        self.items = [['had','jars','containing','marbles','have','jar'],['had','cases','containing','tacks','have','case'],
                      ['collected','albums','of','stamps','collect','album'],['shared','packets','containing','magnets','share','packet'],
                      ['bought','packs','containing','rubberbands','buy','pack'],['bought','packets','of','beads','buy','packet'],
                      ['sold','packs','with','buttons','sell','pack'],['sold','bags','containing','ice-cream sticks','sell','bag'],
                      ['won','games','with','points','win','game'],['won','game sets','with','stars','win','set'],
                      ['got','cases','containing','push pins','get','case'],['received','cases','with','paper clips','receive','case'],
                      ['made','bags','of','flags','make','bag'],['made','scrapbooks','with','stickers','make','book']]
               
        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.PersonName)
        self.number1 = randint(3,9)
        self.number2 = randint(112,198)

        self.problem = "%s %s %d %s %s %d %s each. How many %s did %s %s altogether?"%(self.name,self.item[0],self.number1,self.item[1],
                                                                                       self.item[2],self.number2,self.item[3],self.item[3],
                                                                                       self.name,self.item[4])
        
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[3]
        self.dollar_unit = ""
  
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number1*(self.number2-1),self.number1*(self.number2+1),self.number1*(self.number2-2),self.number1*(self.number2+2)]
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.name,self.number1,self.number2,self.item[0],self.item[3],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ15b(self):
        '''e.g.:
        A <supplier> <supplied> 4 identical <boxes> <containing> 230 <T-shirts> each. How many <T-shirts> did the <supplier> <supply> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ15b"
        self.CheckAnswerType = 1
        
        self.items = [['supplier','supplied','boxes','containing','T-shirts','supply','box'],
                      ['shopkeeper','bought','cartons','containing','shirts','buy','carton'],
                      ['department store','purchased','bags','of','frocks','purchase','store'],
                      ['tailor','stitched','lots','of','scarves','stitch','lot'],
                      ['tailor','sewed','bundles','of','ties','sew','bundle'],
                      ['factory','produced','batches','of','phones','produce','batch'],
                      ['fruiterer','packed','cartons','with','pears','pack','carton'],
                      ['grocery store','bought','sacks','containing','potatoes','buy','sack'],
                      ['farmer','packed','boxes','with','carrots','pack','box'],
                      ['farmer','planted','fields','with','fruit trees','plant','field'],
                      ['vendor','bought','boxes','of','spoons','buy','box'],
                      ['manufacturer','produced','lots','of','batteries','produce','lot'],
                      ['printer','printed','batches','of','posters','print','batch'],
                      ['bookstore','purchased','boxes','containing','erasers','purchase','box'],
                      ['library','had','shelves','containing','books','have','shelf']]

        self.item = random.choice(self.items)

        self.name = random.choice(PersonName.PersonName)
        self.number1 = randint(3,9)
        self.number2 = randint(112,198)

        self.problem = "A %s %s %d identical %s %s %d %s each. How many %s did the %s %s altogether?"%(self.item[0],self.item[1],self.number1,
                                                                                                       self.item[2],self.item[3],self.number2,
                                                                                                       self.item[4],self.item[4],self.item[0],
                                                                                                       self.item[5])
        
        doer = "The %s"%(self.item[0])
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[4]
        self.dollar_unit = ""
  
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number1*(self.number2-1),self.number1*(self.number2+1),self.number1*(self.number2-2),self.number1*(self.number2+2)]
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,doer,self.number1,self.number2,self.item[1],self.item[4],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ16(self):
        '''e.g.:
        [Person.Girlname 1], [Person.Girlname 2], [Person.Girlname 3], [Person.Girlname 4] and [Person.Girlname 5] each had 224 <photos>. How many <photos> did they have altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ16"
        self.CheckAnswerType = 1
        
        self.items = ['photos','ribbons','sea shells','erasers','crayons','markers','hair clips','gummies','can tabs','hair ties','cards','rings']

        self.item = random.choice(self.items)

        self.names = random.sample(PersonName.GirlName,5)
        
        self.number1 = randint(3,5)
        self.number2 = randint(112,298)


        if self.number1 == 3:
            self.problem = "%s, %s and %s each had %d %s. How many %s did they have altogether?"%(self.names[0],self.names[1],self.names[2],
                                                                                                  self.number2,self.item,self.item)
        elif self.number1 == 4:
            self.problem = "%s, %s, %s and %s each had %d %s. How many %s did they have altogether?"%(self.names[0],self.names[1],self.names[2],
                                                                                                  self.names[3],self.number2,self.item,self.item)
        else:
            self.problem = "%s, %s, %s, %s and %s each had %d %s. How many %s did they have altogether?"%(self.names[0],self.names[1],
                                                                                                          self.names[2],self.names[3],
                                                                                                          self.names[4],self.number2,
                                                                                                          self.item,self.item)
                
        self.answer = self.number1 * self.number2
        
        self.unit = self.item
        self.dollar_unit = ""
  
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number1*(self.number2-1),self.number1*(self.number2+1),self.number1*(self.number2-2),self.number1*(self.number2+2)]
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType16(self.problem,self.answer,self.number1,self.number2,self.item,self.names,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ17(self):
        '''e.g.:
        [Person.Girlname 1] <got> 480 <points in a computer game>. [Person.Girlname 2] <got> twice/thrice as many <points> as [Person.Girlname 1]. How many <points> did [Person.Girlname 2] <get>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ17"
        self.CheckAnswerType = 1
        
        self.items = [['got','points in a computer game','points','get'],['had','plums with her','plums','have'],
                      ['baked','buns in her bakery','buns','bake'],['clicked','photos during her vacation','photos','click'],
                      ['used','beads to make a necklace','beads','use'],['collected','stamps in an album','stamps','collect'],
                      ['collected','books for a book drive','books','collect'],['gave away','marbles','marbles','give away'],
                      ['gave away','sweets to her friends','sweets','give away'],
                      ['solved','questions to prepare for her maths exam','questions','solve']]

        self.item = random.choice(self.items)

        self.names = random.sample(PersonName.GirlName,2)
        
        self.number1s = random.choice([[2,"twice"],
                                       [3,"thrice"],
                                       [4,"4 times"],
                                       [5,"5 times"]
                                       ])
        self.number1 = self.number1s[0]
        self.number2 = randint(112,198)

        self.problem = "%s %s %d %s. %s %s %s as many %s as %s. How many %s did %s %s?"%(self.names[0],self.item[0],self.number2,self.item[1],
                                                                                         self.names[1],self.item[0],self.number1s[1],self.item[2],
                                                                                         self.names[0],self.item[2],self.names[1],self.item[3])
                
        self.answer = self.number1 * self.number2
        
        self.unit = self.item[2]
        self.dollar_unit = ""
  
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number1*(self.number2-1),self.number1*(self.number2+1),self.number1*(self.number2-2),self.number1*(self.number2+2)]
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType17(self.problem,self.answer,self.number1,self.number2,self.names,self.item[0],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
           
    def MultiplicationExplanation(self,number1,number2):
        
        hundreds1,tens1 = divmod(int(number1),100)
        tens1,ones1 = divmod(tens1,10)

        carryOverToTens,prodOnes = divmod(ones1*number2,10)
        carryOverToHundreds,prodTens = divmod(tens1*number2+carryOverToTens,10)
        carryOverToThousands,prodHundreds = divmod(hundreds1*number2+carryOverToHundreds,10)
        
        if carryOverToHundreds>0:
            if len(str(number1))>=3: # making sure it's at least a 3-digit number
                hundreds1_td = "<sup>%d</sup>%d"%(carryOverToHundreds,hundreds1)
            else:
                hundreds1_td = "&nbsp;" #hundreds place digit of number1 is 0           
        else:
            if len(str(number1))>=3:
                hundreds1_td = "%d"%(hundreds1)
            else:
                hundreds1_td = "&nbsp;" #hundreds place digit of number1 is 0           

        if carryOverToTens>0:
            tens1_td = "<sup>%d</sup>%d"%(carryOverToTens,tens1)
        else:
            tens1_td = "%d"%(tens1)

        if int(number1*number2)<100:
            smallTable = 1
        else:
            smallTable = 0
            
        #checks to make sure not to display the leading 0s
        if carryOverToThousands==0:
            thousandsAnswer_td = "&nbsp;"
        else:
            thousandsAnswer_td = "%d"%(carryOverToThousands)
        
        if smallTable==1:
            self.solution_text = "<table class='ExplanationMoneyTable' border=0>"
            self.solution_text = self.solution_text + "<tr><td></td><td>%s</td><td>%d</td></tr>"%(tens1_td,ones1)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td></td><td>%d</td></tr>"%(number2)
            self.solution_text = self.solution_text + "<tr><td colspan=3 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line_3.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td></td><td>%d</td><td>%d</td></tr>"%(prodTens,prodOnes)
            self.solution_text = self.solution_text + "</table><br><br>"
        else:
            self.solution_text = "<table class='ExplanationMoneyTable' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%s</td><td>%s</td><td>%d</td></tr>"%(hundreds1_td,tens1_td,ones1)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:0px;'>&times;</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td></tr>"%(number2)
            self.solution_text = self.solution_text + "<tr><td colspan=5 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line_4.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>%s</td><td>%d</td><td>%d</td><td>%d </td></tr>"%(thousandsAnswer_td,prodHundreds,prodTens,prodOnes)
            self.solution_text = self.solution_text + "</table><br><br>"

        return self.solution_text

    def DivisionExplanation(self,number1,number2):        
        hundreds1,tens1 = divmod(int(number1),100)
        tens1,ones1 = divmod(tens1,10)
        
        quotientHundreds,remTens = divmod(hundreds1,number2)
        quotientTens,remOnes = divmod(tens1+remTens*10,number2)
        quotientOnes,rem = divmod(ones1+remOnes*10,number2)
        
        if number1<100:
            if quotientTens==0:
                self.solution_text = "<table class='ExplanationMoneyTable' border=0>"
                self.solution_text = self.solution_text + "<tr><td></td><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-width:2px;'></td><td style='padding-left:0px;'></td><td style='text-align:left;'>%d</td></tr>"%(quotientOnes)
                self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;max-width:2px;'></td><td rowspan=2 style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'><font style='font-size:1.6em'>)</font></td><td colspan=3 style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;'><img src='/images/explanation/line_2.png' /></td></tr>"
                self.solution_text = self.solution_text + "<tr><td style='vertical-align:top;padding-top:0px;'>%d</td><td style='vertical-align:top;padding-left:0px;padding-top:0px;'>%d</td><td style='vertical-align:top;padding-top:0px;text-align:left;'>%d</td></tr>"%(number2,tens1,ones1)
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td style='padding-left:0px;'>&minus; %d</td><td style='text-align:left;'>%d</td></tr>"%(divmod(quotientOnes*number2,10))
                self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;max-width:2px;'></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td colspan=3 style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;'><img src='/images/explanation/line_2.png' /></td></tr>"
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td></td><td style='text-align:left;'>%d</td></tr>"%(rem)
                self.solution_text = self.solution_text + "</table><br><br>"
            else:
                self.solution_text = "<table class='ExplanationMoneyTable' border=0>"
                self.solution_text = self.solution_text + "<tr><td></td><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-width:2px;'></td><td style='padding-left:0px;'>%d</td><td style='text-align:left;'>%d</td></tr>"%(quotientTens,quotientOnes)
                self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;max-width:2px;'></td><td rowspan=2 style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'><font style='font-size:1.6em'>)</font></td><td colspan=3 style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;'><img src='/images/explanation/line_2.png' /></td></tr>"
                self.solution_text = self.solution_text + "<tr><td style='vertical-align:top;padding-top:0px;'>%d</td><td style='vertical-align:top;padding-left:0px;padding-top:0px;'>%d</td><td style='vertical-align:top;padding-top:0px;text-align:left;'>%d</td></tr>"%(number2,tens1,ones1)
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td style='padding-left:0px;'>&minus; %d</td><td></td></tr>"%(quotientTens*number2)
                self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;max-width:2px;'></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td colspan=3 style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;'><img src='/images/explanation/line_2.png' /></td></tr>"
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td style='padding-left:0px;'>%d</td><td style='text-align:left;'>%d</td></tr>"%(remOnes,ones1)
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td style='padding-left:0px;'>&minus; %d</td><td style='text-align:left;'>%d</td></tr>"%(divmod(quotientOnes*number2,10))
                self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;max-width:2px;'></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td colspan=3 style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;'><img src='/images/explanation/line_2.png' /></td></tr>"
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td></td><td style='text-align:left;'>%d</td></tr>"%(rem)
                self.solution_text = self.solution_text + "</table><br><br>"
        else:
            if quotientHundreds==0:
                self.solution_text = "<table class='ExplanationMoneyTable' border=0>"
                self.solution_text = self.solution_text + "<tr><td></td><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-width:2px;'></td><td style='padding-left:0px;'></td><td>%d</td><td>%d</td></tr>"%(quotientTens,quotientOnes)
                self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;max-width:2px;'></td><td rowspan=2 style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'><font style='font-size:1.6em'>)</font></td><td colspan=3 style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;'><img src='/images/explanation/line_3.png' /></td></tr>"
                self.solution_text = self.solution_text + "<tr><td style='vertical-align:top;padding-top:0px;'>%d</td><td style='vertical-align:top;padding-left:0px;padding-top:0px;'>%d</td><td style='vertical-align:top;padding-top:0px;'>%d</td><td style='vertical-align:top;padding-top:0px;'>%d</td></tr>"%(number2,hundreds1,tens1,ones1)
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td style='padding-left:0px;'>&minus; %d</td><td>%d</td><td></td></tr>"%(divmod(quotientTens*number2,10))
                self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;max-width:2px;'></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td colspan=3 style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;'><img src='/images/explanation/line_3.png' /></td></tr>"
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td></td><td>%d</td><td>%d</td></tr>"%(remOnes,ones1)
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td></td><td style='padding-left:0px;'>&minus; %d</td><td>%d</td></tr>"%(divmod(quotientOnes*number2,10))
                self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;max-width:2px;'></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td colspan=3 style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;'><img src='/images/explanation/line_3.png' /></td></tr>"
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td></td><td></td><td>%d</td></tr>"%(rem)
                self.solution_text = self.solution_text + "</table><br><br>"
            else:
                self.solution_text = "<table class='ExplanationMoneyTable' border=0>"
                self.solution_text = self.solution_text + "<tr><td></td><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-width:2px;'></td><td style='padding-left:0px;'>%d</td><td>%d</td><td>%d</td></tr>"%(quotientHundreds,quotientTens,quotientOnes)
                self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;max-width:2px;'></td><td rowspan=2 style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'><font style='font-size:1.6em'>)</font></td><td colspan=3 style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;'><img src='/images/explanation/line_3.png' /></td></tr>"
                self.solution_text = self.solution_text + "<tr><td style='vertical-align:top;padding-top:0px;'>%d</td><td style='vertical-align:top;padding-left:0px;padding-top:0px;'>%d</td><td style='vertical-align:top;padding-top:0px;'>%d</td><td style='vertical-align:top;padding-top:0px;'>%d</td></tr>"%(number2,hundreds1,tens1,ones1)
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td style='padding-left:0px;'>&minus; %d</td><td></td><td></td></tr>"%(quotientHundreds*number2)
                self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;max-width:2px;'></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td colspan=3 style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;'><img src='/images/explanation/line_3.png' /></td></tr>"
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td style='padding-left:0px;'>%d</td><td>%d</td><td></td></tr>"%(remTens,tens1)
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td style='padding-left:0px;'>&minus; %d</td><td>%d</td><td></td></tr>"%(divmod(quotientTens*number2,10))
                self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;max-width:2px;'></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td colspan=3 style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;'><img src='/images/explanation/line_3.png' /></td></tr>"
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td></td><td>%d</td><td>%d</td></tr>"%(remOnes,ones1)
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td></td><td style='padding-left:0px;'>&minus; %d</td><td>%d</td></tr>"%(divmod(quotientOnes*number2,10))
                self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;max-width:2px;'></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td colspan=3 style='text-align:left;padding:0px;margin:0px;vertical-align:bottom;max-height:3px;'><img src='/images/explanation/line_3.png' /></td></tr>"
                self.solution_text = self.solution_text + "<tr><td></td><td style='padding:0px;margin:0px;vertical-align:top;max-width:2px;'></td><td></td><td></td><td>%d</td></tr>"%(rem)
                self.solution_text = self.solution_text + "</table><br><br>"
        
        return self.solution_text

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                
                return False
        elif CheckAnswer == 2:
            try:
                return str(answer)==str(InputAnswer).lower()
            except ValueError:
                return False            