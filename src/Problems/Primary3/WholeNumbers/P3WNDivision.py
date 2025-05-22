'''
Created on Mar 10, 2013
Module: P3WNDivision
Generates the Division problems for Primary 3

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

class P3WNDivision:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1a","ProblemType1b","ProblemType1c","ProblemType1d","ProblemType1e","ProblemType1f",
                               "ProblemType1g","ProblemType1h","ProblemType1i","ProblemTypeMCQ1a","ProblemTypeMCQ1b","ProblemTypeMCQ1c",
                               "ProblemTypeMCQ1d","ProblemTypeMCQ1e","ProblemTypeMCQ1f","ProblemTypeMCQ1g","ProblemTypeMCQ1h","ProblemTypeMCQ1i",],
                            2:["ProblemType2a","ProblemTypeMCQ2a","ProblemTypeMCQ2b",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4a","ProblemTypeMCQ4a","ProblemType4b","ProblemTypeMCQ4b",],
                            5:["ProblemType5a","ProblemTypeMCQ5a","ProblemType5b","ProblemTypeMCQ5b",],
                            6:["ProblemType6","ProblemTypeMCQ6",],
                            7:["ProblemType7","ProblemTypeMCQ7",],
                            8:["ProblemType8","ProblemTypeMCQ8",],
                            9:["ProblemType9","ProblemTypeMCQ9",],
                            10:["ProblemType10","ProblemTypeMCQ10",],
                            11:["ProblemType11","ProblemTypeMCQ11",],
                            12:["ProblemType12a","ProblemTypeMCQ12a","ProblemType12b","ProblemTypeMCQ12b",],
                            13:["ProblemType13","ProblemTypeMCQ13",],
                            14:["ProblemType14a","ProblemTypeMCQ14a","ProblemType14b","ProblemTypeMCQ14b",],
                            15:["ProblemType15a","ProblemTypeMCQ15a","ProblemType15b","ProblemTypeMCQ15b",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1a(),self.GenerateProblemType1b(),self.GenerateProblemType1c(),self.GenerateProblemType1d(),
                                       self.GenerateProblemType1e(),self.GenerateProblemType1f(),self.GenerateProblemType1g(),self.GenerateProblemType1h(),
                                       self.GenerateProblemType1i(),self.GenerateProblemTypeMCQ1a(),self.GenerateProblemTypeMCQ1b(),
                                       self.GenerateProblemTypeMCQ1c(),self.GenerateProblemTypeMCQ1d(),self.GenerateProblemTypeMCQ1e(),
                                       self.GenerateProblemTypeMCQ1f(),self.GenerateProblemTypeMCQ1g(),self.GenerateProblemTypeMCQ1h(),
                                       self.GenerateProblemTypeMCQ1i(),],
                                    2:[self.GenerateProblemType2a(),self.GenerateProblemTypeMCQ2a(),self.GenerateProblemTypeMCQ2b(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4a(),self.GenerateProblemTypeMCQ4a(),self.GenerateProblemType4b(),self.GenerateProblemTypeMCQ4b(),],
                                    5:[self.GenerateProblemType5a(),self.GenerateProblemTypeMCQ5a(),self.GenerateProblemType5b(),self.GenerateProblemTypeMCQ5b(),],
                                    6:[self.GenerateProblemType6(),self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemType7(),self.GenerateProblemTypeMCQ7(),],
                                    8:[self.GenerateProblemType8(),self.GenerateProblemTypeMCQ8(),],
                                    9:[self.GenerateProblemType9(),self.GenerateProblemTypeMCQ9(),],
                                    10:[self.GenerateProblemType10(),self.GenerateProblemTypeMCQ10(),],
                                    11:[self.GenerateProblemType11(),self.GenerateProblemTypeMCQ11(),],
                                    12:[self.GenerateProblemType12a(),self.GenerateProblemTypeMCQ12a(),self.GenerateProblemType12b(),self.GenerateProblemTypeMCQ12b(),],
                                    13:[self.GenerateProblemType13(),self.GenerateProblemTypeMCQ13(),],
                                    14:[self.GenerateProblemType14a(),self.GenerateProblemTypeMCQ14a(),self.GenerateProblemType14b(),self.GenerateProblemTypeMCQ14b(),],
                                    15:[self.GenerateProblemType15a(),self.GenerateProblemTypeMCQ15a(),self.GenerateProblemType15b(),self.GenerateProblemTypeMCQ15b(),],
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
        #return self.GenerateProblemType1e()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1a":self.GenerateProblemType1a(),"ProblemType1b":self.GenerateProblemType1b(),"ProblemType1c":self.GenerateProblemType1c(),
                            "ProblemType1d":self.GenerateProblemType1d(),"ProblemType1e":self.GenerateProblemType1e(),"ProblemType1f":self.GenerateProblemType1f(),
                            "ProblemType1g":self.GenerateProblemType1g(),"ProblemType1h":self.GenerateProblemType1h(),"ProblemType1i":self.GenerateProblemType1i(),
                            "ProblemType2a":self.GenerateProblemType2a(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4a":self.GenerateProblemType4a(),"ProblemType4b":self.GenerateProblemType4b(),
                            "ProblemType5a":self.GenerateProblemType5a(),"ProblemType5b":self.GenerateProblemType5b(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),"ProblemType9":self.GenerateProblemType9(),"ProblemType10":self.GenerateProblemType10(),
                            "ProblemType11":self.GenerateProblemType11(),
                            "ProblemType12a":self.GenerateProblemType12a(),"ProblemType12b":self.GenerateProblemType12b(),
                            "ProblemType13":self.GenerateProblemType13(),
                            "ProblemType14a":self.GenerateProblemType14a(),"ProblemType14b":self.GenerateProblemType14b(),
                            "ProblemType15a":self.GenerateProblemType15a(),"ProblemType15b":self.GenerateProblemType15b(),
                            "ProblemTypeMCQ1a":self.GenerateProblemTypeMCQ1a(),"ProblemTypeMCQ1b":self.GenerateProblemTypeMCQ1b(),"ProblemTypeMCQ1c":self.GenerateProblemTypeMCQ1c(),
                            "ProblemTypeMCQ1d":self.GenerateProblemTypeMCQ1d(),"ProblemTypeMCQ1e":self.GenerateProblemTypeMCQ1e(),"ProblemTypeMCQ1f":self.GenerateProblemTypeMCQ1f(),
                            "ProblemTypeMCQ1g":self.GenerateProblemTypeMCQ1g(),"ProblemTypeMCQ1h":self.GenerateProblemTypeMCQ1h(),"ProblemTypeMCQ1i":self.GenerateProblemTypeMCQ1i(),
                            "ProblemTypeMCQ2a":self.GenerateProblemTypeMCQ2a(),"ProblemTypeMCQ2b":self.GenerateProblemTypeMCQ2b(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4a":self.GenerateProblemTypeMCQ4a(),"ProblemTypeMCQ4b":self.GenerateProblemTypeMCQ4b(),
                            "ProblemTypeMCQ5a":self.GenerateProblemTypeMCQ5a(),"ProblemTypeMCQ5b":self.GenerateProblemTypeMCQ5b(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),"ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),"ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            "ProblemTypeMCQ9":self.GenerateProblemTypeMCQ9(),"ProblemTypeMCQ10":self.GenerateProblemTypeMCQ10(),"ProblemTypeMCQ11":self.GenerateProblemTypeMCQ11(),
                            "ProblemTypeMCQ12a":self.GenerateProblemTypeMCQ12a(),"ProblemTypeMCQ12b":self.GenerateProblemTypeMCQ12b(),
                            "ProblemTypeMCQ13":self.GenerateProblemTypeMCQ13(),
                            "ProblemTypeMCQ14a":self.GenerateProblemTypeMCQ14a(),"ProblemTypeMCQ14b":self.GenerateProblemTypeMCQ14b(),
                            "ProblemTypeMCQ15a":self.GenerateProblemTypeMCQ15a(),"ProblemTypeMCQ15b":self.GenerateProblemTypeMCQ15b(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1a(self):       
        '''e.g.:
        41 &divide; 5 = ____ R 1'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.divisor = randint(3,9)
        self.remainder = randint(0,self.divisor-1)
        self.quotient = randint(2,9)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.problem1 = random.choice(["Find the <b>quotient</b>.<br><br>","Divide and find the <b>quotient</b><br><br>"])
        self.problem1 = self.problem1 + "%d &divide; %d = ___ R %d"%(self.dividend,self.divisor,self.remainder)
        
        self.problem2 = "What is the quotient when %d is divided by %d?"%(self.dividend,self.divisor)
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.quotient
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1a(self.problem,self.answer,self.dividend,self.divisor)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType1a(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        self.solution_text = self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1,number2,answer,number1%number2)
        self.solution_text = self.solution_text + "The quotient is: %d<br></font>"%(answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType1b(self):       
        '''e.g.:
        41 &divide; 5 = 8 R ____'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.divisor = randint(3,9)
        self.remainder = randint(0,self.divisor-1)
        self.quotient = randint(2,9)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.problem1 = random.choice(["Find the <i>remainder</i>.<br><br>","Divide and find the <i>remainder</i><br><br>"])
        self.problem1 = self.problem1 + "%d &divide; %d = %d R ___"%(self.dividend,self.divisor,self.quotient)
        
        self.problem2 = "What is the remainder when %d is divided by %d?"%(self.dividend,self.divisor)
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.remainder
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1b(self.problem,self.answer,self.dividend,self.divisor)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType1b(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        self.solution_text = self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1,number2,(number1-answer)/number2,answer)
        self.solution_text = self.solution_text + "The remainder is: %d<br></font>"%(answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType1c(self):       
        '''e.g.:
        Find the missing number.
        32 &divide; ____ = 8'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        
        self.dividend = self.divisor*self.quotient
               
        self.flag = randint(1,2)
        
        if self.flag == 1:
            self.problem = "Find the missing number.<br><br>%d &divide; ____ = %d"%(self.dividend,self.quotient)
            self.answer = self.divisor
        else:
            self.problem = "Find the missing number.<br><br>____ &divide; %d = %d"%(self.divisor,self.quotient)
            self.answer = self.dividend
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1c(self.problem,self.answer,self.flag,self.dividend,self.divisor,self.quotient)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType1c(self,problem,answer,flag,number1,number2,number3):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        if flag==1:
            self.solution_text = "<table class='ExplanationTable' border=0>"
            self.solution_text = self.solution_text + "<tr><td colspan=2>Given,</td><td></td><td></td></tr>"
            self.solution_text = self.solution_text + "<tr><td></td><td>%d &nbsp;&divide;&nbsp; ?</td><td>=</td><td>%d</td></tr>"%(number1,number3)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0><tr><td colspan=2>Therefore,</td><td></td></tr>"
            self.solution_text = self.solution_text + "<tr><td></td><td style='text-align:right;'>?</td><td>=</td><td>%d &nbsp;&divide;&nbsp; %d</td></tr>"%(number1,number3)
            self.solution_text = self.solution_text + "<tr><td></td><td></td><td>=</td><td>%d</td></tr>"%(answer)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>The missing number is: %d<br></font>"%(answer)
        else:
            self.solution_text = "<table class='ExplanationTable' border=0>"
            self.solution_text = self.solution_text + "<tr><td colspan=2>Given,</td><td></td><td></td></tr>"
            self.solution_text = self.solution_text + "<tr><td></td><td>? &nbsp;&divide;&nbsp; %d</td><td>=</td><td>%d</td></tr>"%(number2,number3)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0><tr><td colspan=2>Therefore,</td><td></td></tr>"
            self.solution_text = self.solution_text + "<tr><td></td><td style='text-align:right;'>?</td><td>=</td><td>%d &nbsp;&times;&nbsp; %d</td></tr>"%(number3,number2)
            self.solution_text = self.solution_text + "<tr><td></td><td></td><td>=</td><td>%d</td></tr>"%(answer)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>The missing number is: %d<br></font>"%(answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType1d(self):       
        '''e.g.:
        5 <friends/cousins/classmates> shared 30 <ribbons> equally among themselves. How many <ribbons> did each <friend> receive?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        
        self.dividend = self.divisor*self.quotient
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','poster colour bottles',
                      'paintbrushes','sharpeners','cards','candies','sweets','marbles','notebooks','clear files',
                      'tape rolls','stamps','clips','darts','ice cream sticks','straws','picture puzzles','candy canes',
                      'rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards',
                      'coins','eggs','dry leaves','balls','beads','crayons','markers','hair clips','gummies','can tabs','hair ties','rings']
        
        self.item1 = random.choice(self.items)
        self.item2 = random.choice(['friend','cousin','classmate'])
               
        self.problem = "%d %ss shared %d %s equally among themselves. How many %s did each %s receive?"%(self.divisor,self.item2,self.dividend,self.item1,
                                                                                                        self.item1,self.item2)
        
        self.answer = self.quotient
        self.unit = self.item1
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1d(self.problem,self.answer,self.dividend,self.divisor,self.item1,self.item2,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1d",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":self.unit}

    def ExplainType1d(self,problem,answer,number1,number2,item1,item2,unit):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item1)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d &nbsp;&divide;&nbsp; %d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-right:0px;text-align:right;'>=</td><td style='text-align:left'>%d</td></tr>"%(number1/number2)
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>Each %s received %d %s.<br></font>"%(item2,answer,item1)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType1e(self):       
        '''e.g.:
        [Person.Girlname] had 30 <ribbons>. She and 4 of her <friends> shared them equally among themselves. How many <ribbons> did each <friend> receive?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        
        self.dividend = self.divisor*self.quotient
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','poster colour bottles',
                      'paintbrushes','sharpeners','cards','candies','sweets','marbles','notebooks','clear files',
                      'tape rolls','stamps','clips','darts','ice cream sticks','straws','picture puzzles','candy canes',
                      'rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards',
                      'coins','eggs','dry leaves','balls','beads','crayons','markers','hair clips','gummies','can tabs','hair ties','rings']
        
        self.item1 = random.choice(self.items)
        self.item2 = random.choice(['friend','cousin','classmate'])
        
        self.name = random.choice(PersonName.GirlName)
        
        self.problem = "%s had %d %s. She and %d of her %ss shared them equally among themselves. How many %s did each person receive?"%(self.name,self.dividend,
                                                                                                                                     self.item1,self.divisor-1,
                                                                                                                                     self.item2,self.item1)
        
        self.answer = self.quotient
        self.unit = self.item1
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1e(self.problem,self.answer,self.dividend,self.divisor,self.item1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1e",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":self.unit}

    def ExplainType1e(self,problem,answer,number1,number2,item1,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),self.unit)

        self.solution_text = "<font class='ExplanationFont'>%d &nbsp;+&nbsp; 1 &nbsp;=&nbsp; %d<br>"%(number2-1,number2)
        self.solution_text = self.solution_text + "The %s were shared among %d persons.<br></font>"%(item1,number2)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item1)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d &nbsp;&divide;&nbsp; %d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-right:0px;text-align:right;'>=</td><td style='text-align:left'>%d</td></tr>"%(number1/number2)
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>Each person received %d %s.<br></font>"%(answer,item1)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType1f(self):       
        '''e.g.:
        [Person.Auntyname] had 30 <ribbons>. She packed them into bags of 5 <ribbons> each. How many bags did she get?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        
        self.dividend = self.divisor*self.quotient
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','poster colour bottles',
                      'paintbrushes','sharpeners','cards','candies','sweets','marbles','notebooks','clear files',
                      'tape rolls','stamps','clips','darts','ice cream sticks','straws','picture puzzles','candy canes',
                      'rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards',
                      'coins','eggs','dry leaves','balls','beads','crayons','markers','hair clips','gummies','can tabs','hair ties','rings']
        
        self.item1 = random.choice(self.items)
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.problem = "%s had %d %s. She packed them into bags of %d %s each. How many bags did she get?"%(self.name,self.dividend,self.item1,
                                                                                                                    self.divisor,self.item1)
        
        self.answer = self.quotient
        self.unit = "bags"
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1f(self.problem,self.answer,self.dividend,self.divisor,self.item1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1f",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":self.unit}

    def ExplainType1f(self,problem,answer,number1,number2,item1,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),self.unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small5.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d</td><td colspan=2 style='height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>. . . . .</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px'>%d</td></tr>"%(item1,self.color1,number2,self.color1,number2,self.color1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5><img src='/images/explanation/P3_model_down_brace_small5.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(number1,number2,answer)
        self.solution_text = self.solution_text + "She got %d bags.<br></font>"%(answer)
        #end of steps
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType1g(self):       
        '''e.g.:
        5 <friends/cousins/classmates> shared 31 <ribbons> equally among themselves. How many <ribbons> were left?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        self.remainder = randint(2,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','poster colour bottles',
                      'paintbrushes','sharpeners','cards','candies','sweets','marbles','notebooks','clear files',
                      'tape rolls','stamps','clips','darts','ice cream sticks','straws','picture puzzles','candy canes',
                      'rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards',
                      'coins','eggs','dry leaves','balls','beads','crayons','markers','hair clips','gummies','can tabs','hair ties','rings']
        
        self.item1 = random.choice(self.items)

        self.item2 = random.choice(['friends','cousins','classmates'])
                
        self.problem = "%d %s shared %d %s equally among themselves. How many %s were left?"%(self.divisor,self.item2,self.dividend,self.item1,self.item1)
        
        self.answer = self.remainder
        self.unit = self.item1 
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1g(self.problem,self.answer,self.dividend,self.divisor,self.item1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1g",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":self.unit}

    def ExplainType1g(self,problem,answer,number1,number2,item1,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),self.unit)

        #beginning of model
        if (number1-answer)/number2 < answer:
            totalCellBrace = 'small1extrasmall%d'%(number2)
            remaiderCellBrace = 'small'
            quotientCellWidth = 24
            remainderCellWidth = 50
        else:
            totalCellBrace = 'small%dextrasmall1'%(number2)
            remaiderCellBrace = 'extrasmall'
            quotientCellWidth = 49
            remainderCellWidth = 25

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d></td><td>?</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number2,remaiderCellBrace)

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item1)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td>"%(self.color1,quotientCellWidth)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;white-space:nowrap;width:%dpx'><font style='font-size:0.8em;'>left</font></td></tr>"%(self.color2,remainderCellWidth)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number2+1,totalCellBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(number2+1,number1)
        self.solution_text = self.solution_text + "</table>"
        #end of model

        #beginning of steps
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1,number2,(number1-answer)/number2,answer)
        self.solution_text = self.solution_text + "%d %s were left.<br></font>"%(answer,item1)
        #end of steps
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType1h(self):       
        '''e.g.:
        [Person.Girlname] had 31 <ribbons>. She and 4 of her <friends> shared them equally among themselves. Find the number of <ribbons> left.'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        self.remainder = randint(2,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','poster colour bottles',
                      'paintbrushes','sharpeners','cards','candies','sweets','marbles','notebooks','clear files',
                      'tape rolls','stamps','clips','darts','ice cream sticks','straws','picture puzzles','candy canes',
                      'rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards',
                      'coins','eggs','dry leaves','balls','beads','crayons','markers','hair clips','gummies','can tabs','hair ties','rings']
        
        self.item1 = random.choice(self.items)

        self.item2 = random.choice(['friends','cousins','classmates'])
        
        self.name = random.choice(PersonName.GirlName)
                
        self.problem = "%s had %d %s. She and %d of her %s shared them equally among themselves. Find the number of %s left."%(self.name,self.dividend,self.item1,
                                                                                                                               self.divisor-1,self.item2,self.item1)
        
        self.answer = self.remainder
        self.unit = self.item1
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1h(self.problem,self.answer,self.dividend,self.divisor,self.item1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1h",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":self.unit}

    def ExplainType1h(self,problem,answer,number1,number2,item1,unit):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),self.unit)

        self.solution_text = "<font class='ExplanationFont'>%d &nbsp;+&nbsp; 1 &nbsp;=&nbsp; %d<br>"%(number2-1,number2)
        self.solution_text = self.solution_text + "The %s were shared by %d persons.<br><br>"%(item1,number2)

        #beginning of model
        if (number1-answer)/number2 < answer:
            totalCellBrace = 'small1extrasmall%d'%(number2)
            remaiderCellBrace = 'small'
            quotientCellWidth = 24
            remainderCellWidth = 50
        else:
            totalCellBrace = 'small%dextrasmall1'%(number2)
            remaiderCellBrace = 'extrasmall'
            quotientCellWidth = 49
            remainderCellWidth = 25

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = self.solution_text + "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d></td><td>?</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number2,remaiderCellBrace)

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item1)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx;'>&nbsp;</td>"%(self.color1,quotientCellWidth)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx;white-space:nowrap;'><font style='font-size:0.8em;'>left</font></td></tr>"%(self.color2,remainderCellWidth)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number2+1,totalCellBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(number2+1,number1)
        self.solution_text = self.solution_text + "</table>"
        #end of model

        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1,number2,(number1-answer)/number2,answer)
        self.solution_text = self.solution_text + "%d %s were left.<br></font>"%(answer,item1)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType1i(self):       
        '''e.g.:
        After packing 31 <ribbons> equally into 5 bags, [Person.Auntyname] had some ribbons <left>. Find the number of <ribbons> left.'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        self.remainder = randint(2,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','poster colour bottles',
                      'paintbrushes','sharpeners','cards','candies','sweets','marbles','notebooks','clear files',
                      'tape rolls','stamps','clips','darts','ice cream sticks','straws','picture puzzles','candy canes',
                      'rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards',
                      'coins','eggs','dry leaves','balls','beads','crayons','markers','hair clips','gummies','can tabs','hair ties','rings']
        
        self.item1 = random.choice(self.items)
        
        self.name = random.choice(PersonName.AuntyName)
                
        self.problem = "After packing %d %s equally into %d bags, %s had some %s left. Find the number of %s left."%(self.dividend,self.item1,self.divisor,
                                                                                                                     self.name,self.item1,self.item1)
        
        self.answer = self.remainder
        self.unit = self.item1
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1g(self.problem,self.answer,self.dividend,self.divisor,self.item1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1i",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":self.unit}


    def GenerateProblemType2a(self):       
        '''e.g.:
        Fill in the blank with <b>odd</b> or <b>even</b>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.number = randint(11,999)
        self.problem = "Fill in the blank with <i>odd</i> or <i>even</i>.<br><br>%d is an ____ number."%(self.number)
        
        if self.number%2==0:
            self.answer = "even"
        else:
            self.answer = "odd"
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2a(self.problem,self.answer,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}

    def ExplainType2a(self,problem,answer,number):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        if number%2==0:
            self.solution_text = "<font class='ExplanationFont'>Even numbers are numbers in which the ones digit is 2, 4, 6, 8 or 0.<br><br>"
            self.solution_text = self.solution_text + "%d is an even number.</font>"%(number)
        else:
            self.solution_text = "<font class='ExplanationFont'>Odd numbers are numbers in which the ones digit is 1, 3, 5, 7 or 9.<br><br>"
            self.solution_text = self.solution_text + "%d is an odd number.</font>"%(number)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def ExplainType2b(self,problem,answer,flag):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        if flag==1:
            self.solution_text = "<font class='ExplanationFont'>Even numbers are numbers in which the ones digit is 2, 4, 6, 8 or 0.<br><br>"
            self.solution_text = self.solution_text + "The even numbers are: %s</font>"%(answer)
        else:
            self.solution_text = "<font class='ExplanationFont'>Odd numbers are numbers in which the ones digit is 1, 3, 5, 7 or 9.<br><br>"
            self.solution_text = self.solution_text + "The odd numbers are: %s</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        39 &divide; 3 = ____'''

        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.numbers = [[3,random.choice([33,36,39,63,66,69,93,96,99])],
                        [4,random.choice([44,48,84,88])],
                        [5,55],[6,66],[7,77],[8,88],[9,99]
                        ]
        
        self.number = random.choice(self.numbers)
        
        self.divisor = self.number[0]
        
        self.dividend = self.number[1]
        
        self.problem1 = "%d &divide; %d = ____"%(self.dividend,self.divisor)
        self.problem2 = "Solve this.<br><br>%d &divide; %d = ____"%(self.dividend,self.divisor)
        self.problem3 = "Divide.<br><br>%d &divide; %d = ____"%(self.dividend,self.divisor)
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.answer = self.dividend/self.divisor
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.dividend,self.divisor)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType3(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),self.unit)

        self.solution_text = self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, %d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d</font>"%(number1,number2,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4a(self):       
        '''e.g.:
        A <bag> contains 52 <red and blue marbles>. There are 3 times as many <red marbles as blue marbles>. How many <blue marbles> are there in the <bag>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.divisor = randint(3,9)
        self.quotient = randint(10,20)
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
       
        self.items = [['bag','red and blue marbles','red marbles as blue marbles','blue marbles','red marbles'],
                      ['bag','hair clips and hair bands','hair clips as hair bands','hair bands','hair clips'],
                      ['basket','apples and oranges','apples as oranges','oranges','apples'],['basket','pears and mangoes','pears as mangoes','mangoes','pears'],
                      ['bouquet','roses and orchids','roses as orchids','orchids','roses'],['pencil case','pencils and pens','pencils as pens','pens','pencils'],
                      ['box','ties and scarves','ties as scarves','scarves','ties'],['box','cookies and candies','cookies as candies','candies','cookies'],
                      ['packet','bowls and cups','bowls as cups','cups','bowls'],['packet','beads and marbles','beads as marbles','marbles','beads']] 
        
        self.item = random.choice(self.items)
        
        self.problem = "A %s contains %d %s. There are %d times as many %s. How many %s are there in the %s?"%(self.item[0],self.dividend,self.item[1],
                                                                                                                  self.divisor-1,self.item[2],self.item[3],
                                                                                                                  self.item[0])
        
        self.answer = self.quotient
        
        self.unit = self.item[3]
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4a(self.problem,self.answer,self.dividend,self.divisor,self.item[0],self.item[3],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":self.unit}

    def ExplainType4a(self,problem,answer,number1,number2,item0,item3,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td><td colspan=%d>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;%d</td></tr>"%(item3,self.color1,number2-1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item4)
        for x in range(0, number2-1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d &nbsp;&divide;&nbsp; %d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "</table><blockquote>"
        self.solution_text = self.solution_text + self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "</blockquote><font class='ExplanationFont'>There are %d %s in the %s.</font>"%(answer,item3,item0)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4b(self):       
        '''e.g.:
        [Person.Boyname] <earned> $56. He <earned> 4 times as much money as [Person.Girlname]. How much money did [Person.Girlname] <earn>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.divisor = randint(3,9)
        self.quotient = randint(10,20)
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.names = [random.choice(PersonName.BoyName),random.choice(PersonName.GirlName)]
       
        self.items = [['earned','earn'],['won','win'],['spent','spend'],['saved','save'],['donated','donate'],['collected','collect'],
                      ['deposited','deposit'],['received','receive'],['gave away','give away']] 
        
        self.item = random.choice(self.items)
        
        self.problem = "%s %s $%d. He %s %d times as much money as %s. How much money did %s %s?"%(self.names[0],self.item[0],self.dividend,self.item[0],
                                                                                             self.divisor,self.names[1],self.names[1],self.item[1])
        
        self.answer = self.quotient
        self.unit = ""
        self.dollar_unit = "$"
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4b(self.problem,self.answer,self.names,self.dividend,self.divisor,self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit}

    def ExplainType4b(self,problem,answer,names,number1,number2,item0,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'>$%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(names[0])
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td></tr>"%(names[1],self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>$%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>$%d &nbsp;&divide;&nbsp; %d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "</table><blockquote>"
        self.solution_text = self.solution_text + self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "</blockquote><font class='ExplanationFont'>%s %s $%d.</font>"%(names[1],item0,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5a(self):       
        '''e.g.:
        Divide and find the <b>quotient</b>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.divisor = randint(3,9)
        self.quotient = randint(10,20)
        self.remainder = randint(1,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.problem1 = "Divide and find the <i>quotient</i>.<br><br>%d &divide; %d"%(self.dividend,self.divisor)
        self.problem2 = "Find the <i>quotient</i>.<br><br>%d &divide; %d = ___ R %d"%(self.dividend,self.divisor,self.remainder)
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.quotient
        self.unit = ""
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.dividend,self.divisor,1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit}

    def GenerateProblemType5b(self):       
        '''e.g.:
        Divide and find the <b>remainder</b>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.divisor = randint(3,9)
        self.quotient = randint(10,20)
        self.remainder = randint(1,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.problem1 = "Divide and find the <i>remainder</i>.<br><br>%d &divide; %d"%(self.dividend,self.divisor)
        self.problem2 = "Do this. Find the <i>remainder</i>.<br><br>%d &divide; %d = %d R ___"%(self.dividend,self.divisor,self.quotient)
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.remainder
        self.unit = ""
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.dividend,self.divisor,2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit}

    def ExplainType5(self,problem,answer,number1,number2,flag):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        self.solution_text = self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        if flag==1:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1,number2,answer,number1%number2)
            self.solution_text = self.solution_text + "The quotient is %d.<br></font>"%(answer)
        else:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1,number2,(number1-answer)/number2,answer)
            self.solution_text = self.solution_text + "The remainder is %d.<br></font>"%(answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        [Person.Unclename] paid $64 for 4 <child tickets to an amusement park>. What was the cost of each <child ticket>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.divisor = randint(3,9)
        self.quotient = randint(10,20)
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['child tickets to an amusement park','child ticket'],['adult tickets to an amusement park','adult ticket'],['entrance tickets to a water park','entrance ticket'],['child tickets to a theme park','child ticket'],['adult tickets to a theme park','adult ticket'],['entrance tickets to an animal safari','entrance ticket'],['tickets to a bird park','ticket'],['adult tickets to a zoo','adult ticket'],['tickets to a musical show','ticket'],['tickets to a science museum','entrance ticket'],['entrance tickets to a coins and stamps museum','entrance ticket'],['coupon booklets at a carnival','coupon booklet']]     
        
        self.item = random.choice(self.items)
        
        self.problem = "%s paid $%d for %d %s. What was the cost of each %s?"%(self.name,self.dividend,self.divisor,self.item[0],self.item[1])
        
        self.answer = self.quotient
        self.unit = ""
        self.dollar_unit = "$"
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.dividend,self.divisor,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit}

    def ExplainType6(self,problem,answer,number1,number2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>$%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2,number2)

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%ss</td>"%(item1)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d &nbsp;&divide;&nbsp; %d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(number1,number2,answer)
        self.solution_text = self.solution_text + "The cost of each %s was $%d.<br></font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        [Person.Girlname 1] collected 4 times as many <pencils> as [Person.Girlname 2]. 
        If [Person.Girlname 1] collected 560 <pencils>, find the number of <pencils> collected by [Person.Girlname 2].'''

        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.divisor = randint(3,9)
        self.quotient = randint(10,20)
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.names = random.sample(PersonName.GirlName,2)
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','paintbrushes','sharpeners','cards','marbles','stamps','clips','darts','ice cream sticks','straws','picture puzzles','rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards','coins','dried leaves','balls','crayons','markers','hair clips','can tabs','hair ties','rings']     
        
        self.item = random.choice(self.items)
        
        self.problem = "%s collected %d times as many %s as %s. If %s collected %d %s, find the number of %s collected by %s."%(self.names[0],self.divisor-1,
                                                                                                                                self.item,self.names[1],self.names[0],
                                                                                                                                self.quotient*(self.divisor-1),self.item,self.item,self.names[1])
        
        temp = self.quotient*(self.divisor-1)
        
        self.answer = self.quotient
        self.unit = self.item
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,temp,self.divisor-1,self.names,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit,
                "unit":self.unit}

    def ExplainType7(self,problem,answer,number1,number2,names,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(names[0])
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td></tr>"%(names[1],self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d &nbsp;&divide;&nbsp; %d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(number1,number2,answer)
        self.solution_text = self.solution_text + "%s collected %d %s.<br></font>"%(names[1],answer,item)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        Divide and find the <b>quotient</b>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.divisor = randint(3,9)
        self.quotient = randint(40,80)
        self.remainder = randint(1,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.problem1 = "Divide and find the <i>quotient</i>.<br><br>%d &divide; %d"%(self.dividend,self.divisor)
        self.problem2 = "Find the <i>quotient</i>.<br><br>%d &divide; %d = ___ R %d"%(self.dividend,self.divisor,self.remainder)
        
        self.problem = random.choice([self.problem1,self.problem2])
        self.answer = self.quotient
        self.unit = ""
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.dividend,self.divisor,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit,
                "unit":self.unit}

    def ExplainType8(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1,number2,answer,number1%number2)
        self.solution_text = self.solution_text + "The quotient is %d.<br></font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        [Person.Auntyname] bought 6 identical <chairs> and paid a total of $630. Find the cost of each <chair>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['chairs','chair',randint(40,80)],['tables','table',randint(40,80)],['couches','couch',randint(40,80)],
                      ['mattresses','mattress',randint(40,80)],['phones','phone',randint(80,100)],['bicycles','bicycle',randint(60,90)],
                      ['coffee tables','coffee table',randint(40,80)],['computer tables','computer table',randint(40,80)],
                      ['office tables','office table',randint(40,80)]]
        
        self.item = random.choice(self.items) 
                       
        self.divisor = randint(3,9)
        self.quotient = self.item[2]
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.name = random.choice(PersonName.AuntyName)
               
        self.problem = "%s bought %d identical %s and paid a total of $%d. Find the cost of each %s."%(self.name,self.divisor,self.item[0],self.dividend,self.item[1])
        self.answer = self.quotient
        self.unit = ""
        self.dollar_unit = "$"
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.dividend,self.divisor,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit,
                "unit":self.unit}

    def ExplainType9(self,problem,answer,number1,number2,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>$%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2,number2)

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item0)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d &nbsp;&divide;&nbsp; %d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(number1,number2,answer)
        self.solution_text = self.solution_text + "The cost of each %s is $%d.<br></font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:
        [Person.name] <painted> 121 <postcards> in 5 days. He/She <painted> the same number of <postcards> each day. 
        How many <postcards> did he/she <paint> each day?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['painted','postcards','paint'],['sold','kites','sell'],['baked','pies','bake'],['corrected','exam papers','correct'],
                      ['picked','fruits','pick'],['made','cards','make'],['solved','math questions','solve'],
                      ['stitched','handkerchiefs','stitch'],['collected','sea shells','collect'],['ironed','shirts','iron']]
        
        self.item = random.choice(self.items) 
                       
        self.divisor = randint(3,9)
        self.quotient = randint(40,80)
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.name = random.choice(PersonName.GirlName)
               
        self.problem = "%s %s %d %s in %d days. She %s the same number of %s each day. How many %s did she %s each day?"%(self.name,self.item[0],self.dividend,
                                                                                                                          self.item[1],self.divisor,self.item[0],self.item[1],self.item[1],self.item[2])
        self.answer = self.quotient
        self.unit = self.item[1]
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.dividend,self.divisor,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit,
                "unit":self.unit}

    def ExplainType10(self,problem,answer,number1,number2,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2,number2)

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item1)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d &nbsp;&divide;&nbsp; %d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(number1,number2,answer)
        self.solution_text = self.solution_text + "She %s %d %s each day.<br></font>"%(item0,answer,item1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:
        A <supplier supplied> 4 similar <boxes> <containing> 230 <T-shirts> altogether. How many <T-shirts> were there in each <box>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['supplier supplied','boxes','containing','T-shirts','box'],['shopkeeper bought','cartons','containing','shirts','carton'],
                      ['department store purchased','bags','containing','frocks','bag'],['tailor stitched','lots','of','scarves','lot'],
                      ['tailor sewed','bundles','of','ties','bundle'],['factory produced','batches','of','phones','batch'],
                      ['fruiterer packed','cartons','with','pears','carton'],['farmer packed','boxes','with','carrots','box'],
                      ['vendor bought','boxes','of','spoons','box'],['manufacturer produced','lots','of','batteries','lot'],
                      ['printer printed','batches','of','posters','batch'],['bookstore purchased','boxes','containing','erasers','box']
                      ]
        
        self.item = random.choice(self.items)
                       
        self.divisor = randint(3,9)
        self.quotient = randint(40,80)
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
               
        self.problem = "A %s %d similar %s %s %d %s altogether. How many %s were there in each %s?"%(self.item[0],self.divisor,self.item[1],self.item[2],
                                                                                                     self.dividend,self.item[3],self.item[3],self.item[4])
        self.answer = self.quotient
        self.unit = self.item[3]
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.dividend,self.divisor,self.item[3],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit,
                "unit":self.unit}

    def ExplainType11(self,problem,answer,number1,number2,item3,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2,number2)

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item3)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d &nbsp;&divide;&nbsp; %d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(number1,number2,answer)
        self.solution_text = self.solution_text + "There were %d %s in each %s.<br></font>"%(answer,item3,item4)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType12a(self):       
        '''e.g.:
        [Person.Auntyname] <divided> 306 <muffins> into <boxes> of 8 <muffins> each <for a Christmas party at work>. How many <boxes> did she get?'''

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.items = [['divided','muffins','boxes','for a Christmas party at work'],['packed','tarts','boxes','for her class'],
                      ['packed','curry puffs','bags','for a customer'],['put','sausages','bags','for her customers'],
                      ['divided','nuggets','boxes','for a customer'],["packed","candies","bags","for her son's birthday party"],
                      ['divided','cookies','tins','for a party'],['put','cookies','trays','for a birthday party'],
                      ['packed','bananas','packets','to sell at a supermarket'],['divided','cupcakes','trays','for her birthday'],
                      ['put','mechanical pencils','packets','for her grandchildren'],['packed','sticker sheets','packets','at her book store']]
        
        self.item = random.choice(self.items)
        
        self.name = random.choice(PersonName.AuntyName)
                       
        self.divisor = randint(3,9)
        self.quotient = randint(40,80)
        self.remainder = randint(1,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
               
        self.problem = "%s %s %d %s into %s of %d %s each %s. How many %s did she get?"%(self.name,self.item[0],self.dividend,self.item[1],
                                                                                         self.item[2],self.divisor,self.item[1],self.item[3],self.item[2])
        self.answer = self.quotient
        self.unit = self.item[2]
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.dividend,self.divisor,self.item[1],self.item[2],1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit,
                "unit":self.unit}

    def GenerateProblemType12b(self):       
        '''e.g.:
        [Person.Auntyname] <divided> 306 <muffins> into <boxes> of 8 <muffins> each <for a Christmas party at work>. How many <muffins> were left?'''

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.items = [['divided','muffins','boxes','for a Christmas party at work'],['packed','tarts','boxes','for her class'],
                      ['packed','curry puffs','bags','for a customer'],['put','sausages','bags','for her customers'],
                      ['divided','nuggets','boxes','for a customer'],["packed","candies","bags","for her son's birthday party"],
                      ['divided','cookies','tins','for a party'],['put','cookies','trays','for a birthday party'],
                      ['packed','bananas','packets','to sell at a supermarket'],['divided','cupcakes','trays','for her birthday'],
                      ['put','mechanical pencils','packets','for her grandchildren'],['packed','sticker sheets','packets','at her book store']]
        
        self.item = random.choice(self.items)
        
        self.name = random.choice(PersonName.AuntyName)
                       
        self.divisor = randint(3,9)
        self.quotient = randint(40,80)
        self.remainder = randint(2,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
               
        self.problem = "%s %s %d %s into %s of %d %s each %s. How many %s were left?"%(self.name,self.item[0],self.dividend,self.item[1],
                                                                                         self.item[2],self.divisor,self.item[1],self.item[3],self.item[1])
        self.answer = self.remainder
        self.unit = self.item[1]
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.dividend,self.divisor,self.item[1],self.item[1],2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit,
                "unit":self.unit}

    def ExplainType12(self,problem,answer,number1,number2,item0,item1,flag,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=6>%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=6 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small5extrasmall1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d</td><td colspan=2 style='height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>. . . . .</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px'>%d</td><td style='background-color:%s;height:20px;border:white solid 1px;width:25px;padding-bottom:5px'><font style='font-size:0.8em'>left</font></td></tr>"%(item0,self.color1,number2,self.color1,number2,self.color1,number2,self.color2)
        if flag==1:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5><img src='/images/explanation/P3_model_down_brace_small5.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>?</td></tr>"
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_extrasmall.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        self.solution_text = self.solution_text + self.DivisionExplanation(number1,number2)
        self.solution_text = self.solution_text + "<br><br>"
        if flag==1:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1,number2,answer,number1%number2)
            self.solution_text = self.solution_text + "She got %d %s.<br></font>"%(answer,item1)
        else:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1,number2,(number1-answer)/number2,answer)
            self.solution_text = self.solution_text + "%d %s were left.<br></font>"%(answer,item1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType13(self):       
        '''e.g.:
        When a number is divided by 6, the remainder is 5 and the quotient is 101. What is the number?'''

        self.complexity_level = "medium"
        self.HCScore = 5
                       
        self.divisor = randint(3,9)
        self.quotient = randint(10,80)
        self.remainder = randint(2,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
               
        self.problem = "When a number is divided by %d, the remainder is %d and the quotient is %d. What is the number?"%(self.divisor,self.remainder,self.quotient)
        
        self.answer = self.dividend
        
        self.unit = ""
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.divisor,self.quotient,self.remainder,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit,
                "unit":self.unit}

    def ExplainType13(self,problem,answer,number1,number2,number3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<table class='ExplanationTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=2>Given,</td><td></td><td></td></tr>"
        self.solution_text = self.solution_text + "<tr><td></td><td>? &nbsp;&divide;&nbsp; %d</td><td>=</td><td>%d R %d</td></tr>"%(number1,number2,number3)
        self.solution_text = self.solution_text + "</table><br>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=2>Therefore,</td><td></td></tr>"
        self.solution_text = self.solution_text + "<tr><td></td><td style='text-align:right;'>?</td><td>=</td><td>(%d &nbsp;&times;&nbsp; %d) &nbsp;+&nbsp; %d</td></tr>"%(number2,number1,number3)
        self.solution_text = self.solution_text + "<tr><td></td><td style='text-align:right;'></td><td>=</td><td>%d &nbsp;+&nbsp; %d</td></tr>"%(number2*number1,number3)
        self.solution_text = self.solution_text + "<tr><td></td><td></td><td>=</td><td>%d</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>The number is: %d<br></font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType14a(self):       
        '''e.g.:
        The sum of 123 and 345 is divided by 5. Find the remainder.'''

        self.complexity_level = "medium"
        self.HCScore = 5
                       
        self.number1 = randint(100,300)
        self.number2 = randint(100,300)
        
        self.divisor = randint(3,9)

        self.quotient,self.remainder = divmod(self.number1+self.number2,self.divisor)
               
        self.problem = "The sum of %d and %d is divided by %d. Find the remainder."%(self.number1,self.number2,self.divisor)
        
        self.answer = self.remainder
        
        self.unit = ""
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.number1,self.number2,self.divisor,2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit,
                "unit":self.unit}

    def GenerateProblemType14b(self):       
        '''e.g.:
        The sum of 123 and 345 is divided by 5. Find the quotient.'''

        self.complexity_level = "medium"
        self.HCScore = 5
                       
        self.number1 = randint(100,300)
        self.number2 = randint(100,300)
        
        self.divisor = randint(3,9)

        self.quotient,self.remainder = divmod(self.number1+self.number2,self.divisor)
               
        self.problem = "The sum of %d and %d is divided by %d. Find the quotient."%(self.number1,self.number2,self.divisor)
        
        self.answer = self.quotient
        
        self.unit = ""
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.number1,self.number2,self.divisor,1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit,
                "unit":self.unit}

    def ExplainType14(self,problem,answer,number1,number2,number3,flag,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<font class='ExplanationFont'>%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d</font><br><br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + self.DivisionExplanation(number1+number2,number3)
        self.solution_text = self.solution_text + "<br><br>"
        if flag==1:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1+number2,number3,answer,(number1+number2)%number3)
            self.solution_text = self.solution_text + "The quotient is %d.<br></font>"%(answer)
        else:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1,number2,(number1+number2-answer)/number3,answer)
            self.solution_text = self.solution_text + "The remainder is %d.<br></font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType15a(self):       
        '''e.g.:
        The difference of 123 and 345 is divided by 5. Find the remainder.'''

        self.complexity_level = "medium"
        self.HCScore = 5
                       
        self.number1 = randint(400,800)
        self.number2 = randint(100,300)
        
        self.divisor = randint(3,9)

        self.quotient,self.remainder = divmod(self.number1-self.number2,self.divisor)
               
        self.problem = "The difference of %d and %d is divided by %d. Find the remainder."%(self.number1,self.number2,self.divisor)
        
        self.answer = self.remainder
        
        self.unit = ""
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.number1,self.number2,self.divisor,2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType15a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit,
                "unit":self.unit}

    def GenerateProblemType15b(self):       
        '''e.g.:
        The difference of 123 and 345 is divided by 5. Find the quotient.'''

        self.complexity_level = "medium"
        self.HCScore = 5
                       
        self.number1 = randint(400,800)
        self.number2 = randint(100,300)
        
        self.divisor = randint(3,9)

        self.quotient,self.remainder = divmod(self.number1-self.number2,self.divisor)
               
        self.problem = "The difference of %d and %d is divided by %d. Find the quotient."%(self.number1,self.number2,self.divisor)
        
        self.answer = self.quotient
        
        self.unit = ""
        self.dollar_unit = ""
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.number1,self.number2,self.divisor,1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType15b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":self.dollar_unit,
                "unit":self.unit}

    def ExplainType15(self,problem,answer,number1,number2,number3,flag,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<font class='ExplanationFont'>%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d</font><br><br>"%(number1,number2,number1-number2)
        self.solution_text = self.solution_text + self.DivisionExplanation(number1-number2,number3)
        self.solution_text = self.solution_text + "<br><br>"
        if flag==1:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1-number2,number3,answer,(number1-number2)%number3)
            self.solution_text = self.solution_text + "The quotient is %d.<br></font>"%(answer)
        else:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;R %d<br><br>"%(number1,number2,(number1-number2-answer)/number3,answer)
            self.solution_text = self.solution_text + "The remainder is %d.<br></font>"%(answer)

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
        41 &divide; 5 = ____ R 1'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1a"
        self.CheckAnswerType = 1

        self.divisor = randint(3,9)
        self.remainder = randint(0,self.divisor-1)
        self.quotient = randint(2,9)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.problem1 = random.choice(["Find the <b>quotient</b>.<br><br>","Divide and find the <b>quotient</b><br><br>"])
        self.problem1 = self.problem1 + "%d &divide; %d = ___ R %d"%(self.dividend,self.divisor,self.remainder)
        
        self.problem2 = "What is the quotient when %d is divided by %d?"%(self.dividend,self.divisor)
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.quotient
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(2,9)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1a(self.problem,self.answer,self.dividend,self.divisor)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ1b(self):
        '''e.g.:
        41 &divide; 5 = 8 R ____'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1b"
        self.CheckAnswerType = 1

        self.divisor = randint(3,9)
        self.remainder = randint(0,self.divisor-1)
        self.quotient = randint(2,9)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.problem1 = random.choice(["Find the <i>remainder</i>.<br><br>","Divide and find the <i>remainder</i><br><br>"])
        self.problem1 = self.problem1 + "%d &divide; %d = %d R ___"%(self.dividend,self.divisor,self.quotient)
        
        self.problem2 = "What is the remainder when %d is divided by %d?"%(self.dividend,self.divisor)
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.remainder
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(0,5)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1b(self.problem,self.answer,self.dividend,self.divisor)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ1c(self):
        '''e.g.:
        Find the missing number.
        32 &divide; ____ = 8'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1c"
        self.CheckAnswerType = 1

        self.divisor = randint(3,9)
        self.quotient = randint(4,9)
        
        self.dividend = self.divisor*self.quotient
               
        self.flag = randint(1,2)
        
        self.wrongAnswers = []
        if self.flag == 1:
            self.problem = "Find the missing number.<br><br>%d &divide; ____ = %d"%(self.dividend,self.quotient)
            self.answer = self.divisor
            while len(self.wrongAnswers)!=3:
                self.wrongAnswer = randint(3,9)
                if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                    self.wrongAnswers.append(self.wrongAnswer)
        else:
            self.problem = "Find the missing number.<br><br>____ &divide; %d = %d"%(self.divisor,self.quotient)
            self.answer = self.dividend
            self.wrongAnswers = [(self.divisor+1)*self.quotient,(self.divisor-1)*self.quotient,self.divisor*(self.quotient-1),self.divisor*(self.quotient+1)]
                                    
        self.template = "MCQTypeProblems.html"
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1c(self.problem,self.answer,self.flag,self.dividend,self.divisor,self.quotient)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ1d(self):
        '''e.g.:
        5 <friends/cousins/classmates> shared 30 <ribbons> equally among themselves. How many <ribbons> did each <friend> receive?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1d"
        self.CheckAnswerType = 1

        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        
        self.dividend = self.divisor*self.quotient
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','poster colour bottles',
                      'paintbrushes','sharpeners','cards','candies','sweets','marbles','notebooks','clear files',
                      'tape rolls','stamps','clips','darts','ice cream sticks','straws','picture puzzles','candy canes',
                      'rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards',
                      'coins','eggs','dry leaves','balls','beads','crayons','markers','hair clips','gummies','can tabs','hair ties','rings']
        
        self.item1 = random.choice(self.items)
        self.item2 = random.choice(['friend','cousin','classmate'])
               
        self.problem = "%d %ss shared %d %s equally among themselves. How many %s did each %s receive?"%(self.divisor,self.item2,self.dividend,self.item1,
                                                                                                        self.item1,self.item2)
        
        self.answer = self.quotient
        self.unit = self.item1
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(2,9)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1d(self.problem,self.answer,self.dividend,self.divisor,self.item1,self.item2,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ1e(self):
        '''e.g.:
        [Person.Girlname] had 30 <ribbons>. She and 4 of her <friends> shared them equally among themselves. How many <ribbons> did each <friend> receive?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1e"
        self.CheckAnswerType = 1

        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        
        self.dividend = self.divisor*self.quotient
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','poster colour bottles',
                      'paintbrushes','sharpeners','cards','candies','sweets','marbles','notebooks','clear files',
                      'tape rolls','stamps','clips','darts','ice cream sticks','straws','picture puzzles','candy canes',
                      'rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards',
                      'coins','eggs','dry leaves','balls','beads','crayons','markers','hair clips','gummies','can tabs','hair ties','rings']
        
        self.item1 = random.choice(self.items)
        self.item2 = random.choice(['friend','cousin','classmate'])
        
        self.name = random.choice(PersonName.GirlName)
        
        self.problem = "%s had %d %s. She and %d of her %ss shared them equally among themselves. How many %s did each person receive?"%(self.name,self.dividend,
                                                                                                                                     self.item1,self.divisor-1,
                                                                                                                                     self.item2,self.item1)
        
        self.answer = self.quotient
        self.unit = self.item1
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(2,9)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1e(self.problem,self.answer,self.dividend,self.divisor,self.item1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ1f(self):
        '''e.g.:
        [Person.Auntyname] had 30 <ribbons>. She packed them into bags of 5 <ribbons> each. How many bags did she get?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1f"
        self.CheckAnswerType = 1

        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        
        self.dividend = self.divisor*self.quotient
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','poster colour bottles',
                      'paintbrushes','sharpeners','cards','candies','sweets','marbles','notebooks','clear files',
                      'tape rolls','stamps','clips','darts','ice cream sticks','straws','picture puzzles','candy canes',
                      'rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards',
                      'coins','eggs','dry leaves','balls','beads','crayons','markers','hair clips','gummies','can tabs','hair ties','rings']
        
        self.item1 = random.choice(self.items)
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.problem = "%s had %d %s. She packed them into bags of %d %s each. How many bags did she get?"%(self.name,self.dividend,self.item1,
                                                                                                                    self.divisor,self.item1)

        self.answer = self.quotient
        self.unit = "bags"
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(2,9)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1f(self.problem,self.answer,self.dividend,self.divisor,self.item1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ1g(self):
        '''e.g.:
        5 <friends/cousins/classmates> shared 31 <ribbons> equally among themseleves. How many <ribbons> were left?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1g"
        self.CheckAnswerType = 1


        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        self.remainder = randint(2,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','poster colour bottles',
                      'paintbrushes','sharpeners','cards','candies','sweets','marbles','notebooks','clear files',
                      'tape rolls','stamps','clips','darts','ice cream sticks','straws','picture puzzles','candy canes',
                      'rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards',
                      'coins','eggs','dry leaves','balls','beads','crayons','markers','hair clips','gummies','can tabs','hair ties','rings']
        
        self.item1 = random.choice(self.items)

        self.item2 = random.choice(['friends','cousins','classmates'])
                
        self.problem = "%d %s shared %d %s equally among themselves. How many %s were left?"%(self.divisor,self.item2,self.dividend,self.item1,self.item1)
        
        self.answer = self.remainder
        self.unit = self.item1
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(0,6)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1g(self.problem,self.answer,self.dividend,self.divisor,self.item1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ1h(self):
        '''e.g.:
        [Person.Girlname] had 31 <ribbons>. She and 4 of her <friends> shared them equally among themselves. Find the number of <ribbons> left.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1h"
        self.CheckAnswerType = 1

        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        self.remainder = randint(2,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','poster colour bottles',
                      'paintbrushes','sharpeners','cards','candies','sweets','marbles','notebooks','clear files',
                      'tape rolls','stamps','clips','darts','ice cream sticks','straws','picture puzzles','candy canes',
                      'rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards',
                      'coins','eggs','dry leaves','balls','beads','crayons','markers','hair clips','gummies','can tabs','hair ties','rings']
        
        self.item1 = random.choice(self.items)

        self.item2 = random.choice(['friends','cousins','classmates'])
        
        self.name = random.choice(PersonName.GirlName)
                
        self.problem = "%s had %d %s. She and %d of her %s shared them equally among themselves. Find the number of %s left."%(self.name,self.dividend,self.item1,
                                                                                                                               self.divisor-1,self.item2,self.item1)
        
        self.answer = self.remainder
        self.unit = self.item1
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(0,6)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1h(self.problem,self.answer,self.dividend,self.divisor,self.item1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ1i(self):
        '''e.g.:
        After packing 31 <ribbons> equally into 5 bags, [Person.Auntyname] had some ribbons <left>. Find the number of <ribbons> left.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1i"
        self.CheckAnswerType = 1

        self.divisor = randint(3,9)
        self.quotient = randint(2,9)
        self.remainder = randint(2,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','poster colour bottles',
                      'paintbrushes','sharpeners','cards','candies','sweets','marbles','notebooks','clear files',
                      'tape rolls','stamps','clips','darts','ice cream sticks','straws','picture puzzles','candy canes',
                      'rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards',
                      'coins','eggs','dry leaves','balls','beads','crayons','markers','hair clips','gummies','can tabs','hair ties','rings']
        
        self.item1 = random.choice(self.items)
        
        self.name = random.choice(PersonName.AuntyName)
                
        self.problem = "After packing %d %s equally into %d bags, %s had some %s left. Find the number of %s left."%(self.dividend,self.item1,self.divisor,
                                                                                                                     self.name,self.item1,self.item1)
        
        self.answer = self.remainder
        self.unit = self.item1
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(0,6)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1g(self.problem,self.answer,self.dividend,self.divisor,self.item1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ2a(self):
        '''e.g.:
        Fill in the blank with <b>odd</b> or <b>even</b>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ2a"
        self.CheckAnswerType = 2
                
        self.number = randint(11,999)
        self.problem = "Fill in the blank.<br><br>%d is an ____ number."%(self.number)
        
        if self.number%2==0:
            self.answer = "even"
        else:
            self.answer = "odd"
                                    
        self.template = "MCQType2Choices.html"
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2a(self.problem,self.answer,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':"even",'answer2':"odd",'value1':"even",'value2':"odd",
                'explain':self.explain,'problem_type':self.problem_type,
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType}
        
    def GenerateProblemTypeMCQ2b(self):
        '''e.g.:
        Study the numbers below and write down all the even / odd numbers.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ2b"
        self.CheckAnswerType = 2

        self.EvenNumbers = []
        
        while len(self.EvenNumbers)!=3:
            self.EvenNumber = randint(11,300) * 2
            if self.EvenNumber not in self.EvenNumbers:
                self.EvenNumbers.append(self.EvenNumber)

        self.OddNumbers = []
        
        while len(self.OddNumbers)!=3:
            self.OddNumber = randint(11,300) * 2 + 1
            if self.OddNumber not in self.OddNumbers:
                self.OddNumbers.append(self.OddNumber)
                
        self.numbers = self.EvenNumbers + self.OddNumbers
        
        random.shuffle(self.numbers)
                
        self.flag = randint(1,2)
        
        self.wrongAnswers = []
        
        if self.flag == 1:
            self.problem = "Study the numbers below and choose all the even numbers.<br><br>%d,  %d,  %d,  %d,  %d,  %d"%(self.numbers[0],self.numbers[1],self.numbers[2],
                                                                                                                      self.numbers[3],self.numbers[4],self.numbers[5])
            self.answer = str(self.EvenNumbers[0])+", "+str(self.EvenNumbers[1])+", "+str(self.EvenNumbers[2])
            self.wrongAnswers.append(str(self.EvenNumbers[0])+", "+str(self.EvenNumbers[1]))
            self.wrongAnswers.append(str(self.EvenNumbers[1])+", "+str(self.EvenNumbers[2]))
            self.wrongAnswers.append(str(self.EvenNumbers[2])+", "+str(self.EvenNumbers[0]))
            self.wrongAnswers.append(str(self.EvenNumbers[0])+", "+str(self.EvenNumbers[1])+", "+str(self.OddNumbers[1]))
            self.wrongAnswers.append(str(self.EvenNumbers[1])+", "+str(self.OddNumbers[1])+", "+str(self.OddNumbers[2]))
        else:
            self.problem = "Study the numbers below and choose all the odd numbers.<br><br>%d,  %d,  %d,  %d,  %d,  %d"%(self.numbers[0],self.numbers[1],self.numbers[2],
                                                                                                                      self.numbers[3],self.numbers[4],self.numbers[5])
            self.answer = str(self.OddNumbers[0])+", "+str(self.OddNumbers[1])+", "+str(self.OddNumbers[2])
            self.wrongAnswers.append(str(self.OddNumbers[0])+", "+str(self.OddNumbers[1]))
            self.wrongAnswers.append(str(self.OddNumbers[1])+", "+str(self.OddNumbers[2]))
            self.wrongAnswers.append(str(self.OddNumbers[2])+", "+str(self.OddNumbers[0]))
            self.wrongAnswers.append(str(self.OddNumbers[0])+", "+str(self.OddNumbers[1])+", "+str(self.EvenNumbers[1]))
            self.wrongAnswers.append(str(self.OddNumbers[1])+", "+str(self.EvenNumbers[1])+", "+str(self.EvenNumbers[2]))
                                                
        self.template = "MCQTypeProblems.html"
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2b(self.problem,self.answer,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
        39 &divide; 3 = ____'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ3"
        self.CheckAnswerType = 1

                
        self.numbers = [[3,random.choice([33,36,39,63,66,69,93,96,99])],
                        [4,random.choice([44,48,84,88])],
                        [5,55],[6,66],[7,77],[8,88],[9,99]
                        ]
        
        self.number = random.choice(self.numbers)
        
        self.divisor = self.number[0]
        
        self.dividend = self.number[1]
        
        self.problem1 = "%d &divide; %d = ____"%(self.dividend,self.divisor)
        self.problem2 = "Do this.<br><br>%d &divide; %d = ____"%(self.dividend,self.divisor)
        self.problem3 = "Divide.<br><br>%d &divide; %d = ____"%(self.dividend,self.divisor)
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.answer = self.dividend/self.divisor
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = [self.answer+1, self.answer-1, self.answer+2]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.dividend,self.divisor)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ4a(self):
        '''e.g.:
        A <bag> contains 52 <red and blue marbles>. There are 3 times as many <red marbles as blue marbles>. How many <blue marbles> are there in the <bag>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ4a"
        self.CheckAnswerType = 1
                
        self.divisor = randint(3,9)
        self.quotient = randint(10,20)
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
       
        self.items = [['bag','red and blue marbles','red marbles as blue marbles','blue marbles','red marbles'],
                      ['bag','hair clips and hair bands','hair clips as hair bands','hair bands','hair clips'],
                      ['basket','apples and oranges','apples as oranges','oranges','apples'],['basket','pears and mangoes','pears as mangoes','mangoes','pears'],
                      ['bouquet','roses and orchids','roses as orchids','orchids','roses'],['pencil case','pencils and pens','pencils as pens','pens','pencils'],
                      ['box','ties and scarves','ties as scarves','scarves','ties'],['box','cookies and candies','cookies as candies','candies','cookies'],
                      ['packet','bowls and cups','bowls as cups','cups','bowls'],['packet','beads and marbles','beads as marbles','marbles','beads']] 
        
        self.item = random.choice(self.items)
        
        self.problem = "A %s contains %d %s. There are %d times as many %s. How many %s are there in the %s?"%(self.item[0],self.dividend,self.item[1],
                                                                                                                  self.divisor-1,self.item[2],self.item[3],
                                                                                                                  self.item[0])
        
        self.answer = self.quotient
        
        self.unit = self.item[3]
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(10,20)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4a(self.problem,self.answer,self.dividend,self.divisor,self.item[0],self.item[3],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ4b(self):
        '''e.g.:
        [Person.Boyname] <earned> $56. He <earned> 4 times as much money as [Person.Girlname]. How much money did [Person.Girlname] <earn>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ4b"
        self.CheckAnswerType = 1
                
        self.divisor = randint(3,9)
        self.quotient = randint(10,20)
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.names = [random.choice(PersonName.BoyName),random.choice(PersonName.GirlName)]
       
        self.items = [['earned','earn'],['won','win'],['spent','spend'],['saved','save'],['donated','donate'],['collected','collect'],
                      ['deposited','deposit'],['received','receive'],['gave away','give away']] 
        
        self.item = random.choice(self.items)
        
        self.problem = "%s %s $%d. He %s %d times as much money as %s. How much money did %s %s?"%(self.names[0],self.item[0],self.dividend,self.item[0],
                                                                                             self.divisor,self.names[1],self.names[1],self.item[1])
        
        self.answer = self.quotient
        self.unit = ""
        self.dollar_unit = "$"
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(10,20)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4b(self.problem,self.answer,self.names,self.dividend,self.divisor,self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ5a(self):
        '''e.g.:
        Divide and find the <b>quotient</b>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ5a"
        self.CheckAnswerType = 1
                
        self.divisor = randint(3,9)
        self.quotient = randint(10,20)
        self.remainder = randint(1,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.problem1 = "Divide and find the <i>quotient</i>.<br><br>%d &divide; %d"%(self.dividend,self.divisor)
        self.problem2 = "Find the <i>quotient</i>.<br><br>%d &divide; %d = ___ R %d"%(self.dividend,self.divisor,self.remainder)
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.quotient
        self.unit = ""
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(10,20)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.dividend,self.divisor,1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ5b(self):
        '''e.g.:
        Divide and find the <b>remainder</b>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ5b"
        self.CheckAnswerType = 1
                
        self.divisor = randint(3,9)
        self.quotient = randint(10,20)
        self.remainder = randint(1,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.problem1 = "Divide and find the <i>remainder</i>.<br><br>%d &divide; %d"%(self.dividend,self.divisor)
        self.problem2 = "Do this. Find the <i>remainder</i>.<br><br>%d &divide; %d = %d R ___"%(self.dividend,self.divisor,self.quotient)
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.remainder
        self.unit = ""
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(1,5)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.dividend,self.divisor,2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ6(self):
        '''e.g.:
        [Person.Unclename] paid $64 for 4 <child tickets to an amusement park>. What was the cost of each <child ticket>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ6"
        self.CheckAnswerType = 1
                
        self.divisor = randint(3,9)
        self.quotient = randint(10,20)
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['child tickets to an amusement park','child ticket'],['adult tickets to an amusement park','adult ticket'],['entrance tickets to a water park','entrance ticket'],['child tickets to a theme park','child ticket'],['adult tickets to a theme park','adult ticket'],['entrance tickets to an animal safari','entrance ticket'],['tickets to a bird park','ticket'],['adult tickets to a zoo','adult ticket'],['tickets to a musical show','ticket'],['tickets to a science museum','entrance ticket'],['entrance tickets to a coins and stamps museum','entrance ticket'],['coupon booklets at a carnival','coupon booklet']]     
        
        self.item = random.choice(self.items)
        
        self.problem = "%s paid $%d for %d %s. What was the cost of each %s?"%(self.name,self.dividend,self.divisor,self.item[0],self.item[1])
        
        self.answer = self.quotient
        self.unit = ""
        self.dollar_unit = "$"
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(10,20)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.dividend,self.divisor,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ7(self):
        '''e.g.:
        [Person.Girlname 1] collected 4 times as many <pencils> as [Person.Girlname 2]. 
        If [Person.Girlname 1] collected 560 <pencils>, find the number of <pencils> collected by [Person.Girlname 2].'''

        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ7"
        self.CheckAnswerType = 1
                
        self.divisor = randint(3,9)
        self.quotient = randint(10,20)
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.names = random.sample(PersonName.GirlName,2)
        
        self.items = ['ribbons','erasers','pens','pencils','stickers','shells','paintbrushes','sharpeners','cards','marbles','stamps','clips','darts','ice cream sticks','straws','picture puzzles','rubber ducks','toy animals','starfishes','shells','postcards','envelopes','picture cards','coins','dried leaves','balls','crayons','markers','hair clips','can tabs','hair ties','rings']     
        
        self.item = random.choice(self.items)
        
        self.problem = "%s collected %d times as many %s as %s. If %s collected %d %s, find the number of %s collected by %s."%(self.names[0],self.divisor-1,
                                                                                                                                self.item,self.names[1],self.names[0],
                                                                                                                                self.quotient*(self.divisor-1),self.item,self.item,self.names[1])
        
        temp = self.quotient*(self.divisor-1)
        
        self.answer = self.quotient
        self.unit = self.item
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(10,20)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,temp,self.divisor-1,self.names,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ8(self):
        '''e.g.:
        Divide and find the <b>quotient</b>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ8"
        self.CheckAnswerType = 1
                
        self.divisor = randint(3,9)
        self.quotient = randint(40,80)
        self.remainder = randint(1,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.problem1 = "Divide and find the <i>quotient</i>.<br><br>%d &divide; %d"%(self.dividend,self.divisor)
        self.problem2 = "Find the <i>quotient</i>.<br><br>%d &divide; %d = ___ R %d"%(self.dividend,self.divisor,self.remainder)
        
        self.problem = random.choice([self.problem1,self.problem2])
        self.answer = self.quotient
        self.unit = ""
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(40,80)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.dividend,self.divisor,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ9(self):
        '''e.g.:
        [Person.Auntyname] bought 6 identical <chairs> and paid a total of $630. Find the cost of each <chair>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ9"
        self.CheckAnswerType = 1
        
        self.items = [['chairs','chair',randint(40,80)],['tables','table',randint(40,80)],['couches','couch',randint(40,80)],
                      ['mattresses','mattress',randint(40,80)],['phones','phone',randint(80,100)],['bicycles','bicycle',randint(60,90)],
                      ['coffee tables','coffee table',randint(40,80)],['computer tables','computer table',randint(40,80)],
                      ['office tables','office table',randint(40,80)]]
        
        self.item = random.choice(self.items) 
                       
        self.divisor = randint(3,9)
        self.quotient = self.item[2]
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.name = random.choice(PersonName.AuntyName)
               
        self.problem = "%s bought %d identical %s and paid a total of $%d. Find the cost of each %s."%(self.name,self.divisor,self.item[0],self.dividend,self.item[1])
        self.answer = self.quotient
        self.unit = ""
        self.dollar_unit = "$"
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = [self.answer+5,self.answer-1,self.answer+1,self.answer-5,self.answer+10,self.answer-10] 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.dividend,self.divisor,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ10(self):
        '''e.g.:
        [Person.name] <painted> 121 <postcards> in 5 days. He/She <painted> the same number of <postcards> each day. 
        How many <postcards> did he/she <paint> each day?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ10"
        self.CheckAnswerType = 1
        
        self.items = [['painted','postcards','paint'],['sold','kites','sell'],['baked','pies','bake'],['corrected','exam papers','correct'],
                      ['picked','fruits','pick'],['made','decorative cards','make'],['solved','math questions','solve'],
                      ['stitched','handkerchiefs','stitch'],['collected','sea shells','collect'],['ironed','shirts','iron']]
        
        self.item = random.choice(self.items) 
                       
        self.divisor = randint(3,9)
        self.quotient = randint(40,80)
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
        
        self.name = random.choice(PersonName.GirlName)
               
        self.problem = "%s %s %d %s in %d days. She %s the same number of %s each day. How many %s did she %s each day?"%(self.name,self.item[0],self.dividend,
                                                                                                                          self.item[1],self.divisor,self.item[0],self.item[1],self.item[1],self.item[2])
        self.answer = self.quotient
        self.unit = self.item[1]
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(40,80)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.dividend,self.divisor,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ11(self):
        '''e.g.:
        A <supplier supplied> 4 similar <boxes> <containing> 230 <T-shirts> altogether. How many <T-shirts> were there in each <box>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ11"
        self.CheckAnswerType = 1
        
        self.items = [['supplier supplied','boxes','containing','T-shirts','box'],['shopkeeper bought','cartons','containing','shirts','carton'],
                      ['department store purchased','bags','containing','frocks','bag'],['tailor stitched','lots','of','scarves','lot'],
                      ['tailor sewed','bundles','of','ties','bundle'],['factory produced','batches','of','phones','batch'],
                      ['fruiterer packed','cartons','with','pears','carton'],['farmer packed','boxes','with','carrots','box'],
                      ['vendor bought','boxes','of','spoons','box'],['manufacturer produced','lots','of','batteries','lot'],
                      ['printer printed','batches','of','posters','batch'],['bookstore purchased','boxes','containing','erasers','box']
                      ]
        
        self.item = random.choice(self.items) 
                       
        self.divisor = randint(3,9)
        self.quotient = randint(40,80)
        self.remainder = 0
        
        self.dividend = self.divisor*self.quotient + self.remainder
               
        self.problem = "A %s %d similar %s %s %d %s altogether. How many %s were there in each %s?"%(self.item[0],self.divisor,self.item[1],self.item[2],
                                                                                                     self.dividend,self.item[3],self.item[3],self.item[4])
        self.answer = self.quotient
        self.unit = self.item[3]
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(40,80)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.dividend,self.divisor,self.item[3],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ12a(self):
        '''e.g.:
        [Person.Auntyname] <divided> 306 <muffins> into <boxes> of 8 <muffins> each <for a Christmas party at work>. How many <boxes> did she get?'''

        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ12a"
        self.CheckAnswerType = 1
        
        self.items = [['divided','muffins','boxes','for a Christmas party at work'],['packed','tarts','boxes','for her class'],
                      ['packed','curry puffs','bags','for a customer'],['put','sausages','bags','for her customers'],
                      ['divided','nuggets','boxes','for a customer'],["packed","candies","bags","for her son's birthday party"],
                      ['divided','cookies','tins','for a party'],['put','cookies','trays','for a birthday party'],
                      ['packed','bananas','packets','to sell at a supermarket'],['divided','cupcakes','trays','for her birthday'],
                      ['put','mechanical pencils','packets','for her grandchildren'],['packed','sticker sheets','packets','at her book store']]
        
        self.item = random.choice(self.items)
        
        self.name = random.choice(PersonName.AuntyName)
                       
        self.divisor = randint(3,9)
        self.quotient = randint(40,80)
        self.remainder = randint(1,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
               
        self.problem = "%s %s %d %s into %s of %d %s each %s. How many %s did she get?"%(self.name,self.item[0],self.dividend,self.item[1],
                                                                                         self.item[2],self.divisor,self.item[1],self.item[3],self.item[2])
        self.answer = self.quotient
        self.unit = self.item[2]
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers)!=3:
            self.wrongAnswer = randint(40,80)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer) 
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.dividend,self.divisor,self.item[1],self.item[2],1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ12b(self):
        '''e.g.:
        [Person.Auntyname] <divided> 306 <muffins> into <boxes> of 8 <muffins> each <for a Christmas party at work>. How many <muffins> were left?'''

        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ12b"
        self.CheckAnswerType = 1
        
        self.items = [['divided','muffins','boxes','for a Christmas party at work'],['packed','tarts','boxes','for her class'],
                      ['packed','curry puffs','bags','for a customer'],['put','sausages','bags','for her customers'],
                      ['divided','nuggets','boxes','for a customer'],["packed","candies","bags","for her son's birthday party"],
                      ['divided','cookies','tins','for a party'],['put','cookies','trays','for a birthday party'],
                      ['packed','bananas','packets','to sell at a supermarket'],['divided','cupcakes','trays','for her birthday'],
                      ['put','mechanical pencils','packets','for her grandchildren'],['packed','sticker sheets','packets','at her book store']]
        
        self.item = random.choice(self.items)
        
        self.name = random.choice(PersonName.AuntyName)
                       
        self.divisor = randint(3,9)
        self.quotient = randint(40,80)
        self.remainder = randint(2,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
               
        self.problem = "%s %s %d %s into %s of %d %s each %s. How many %s were left?"%(self.name,self.item[0],self.dividend,self.item[1],
                                                                                         self.item[2],self.divisor,self.item[1],self.item[3],self.item[1])
        self.answer = self.remainder
        self.unit = self.item[1]
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = [self.answer-1,self.answer+1,self.answer+2]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.dividend,self.divisor,self.item[1],self.item[1],2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ13(self):
        '''e.g.:
        When a number is divided by 6, the remainder is 5 and the quotient is 101. What is the number?'''

        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ13"
        self.CheckAnswerType = 1
                       
        self.divisor = randint(3,9)
        self.quotient = randint(10,80)
        self.remainder = randint(2,self.divisor-1)
        
        self.dividend = self.divisor*self.quotient + self.remainder
               
        self.problem = "When a number is divided by %d, the remainder is %d and the quotient is %d. What is the number?"%(self.divisor,self.remainder,self.quotient)
        
        self.answer = self.dividend
        
        self.unit = ""
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = [self.answer-1,self.answer+1,self.answer+5,self.answer-5,self.answer+10,self.answer-10]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.divisor,self.quotient,self.remainder,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ14a(self):
        '''e.g.:
        The sum of 123 and 345 is divided by 5. Find the remainder.'''

        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ14a"
        self.CheckAnswerType = 1
                       
        self.number1 = randint(100,300)
        self.number2 = randint(100,300)
        
        self.divisor = randint(3,9)

        self.quotient,self.remainder = divmod(self.number1+self.number2,self.divisor)
               
        self.problem = "The sum of %d and %d is divided by %d. Find the remainder."%(self.number1,self.number2,self.divisor)
        
        self.answer = self.remainder
        
        self.unit = ""
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = [self.answer+1,self.answer+2]
        
        if self.answer != 0:
            self.wrongAnswers.append(self.answer-1)
        else:
            self.wrongAnswers.append(self.answer+3)
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.number1,self.number2,self.divisor,2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ14b(self):
        '''e.g.:
        The sum of 123 and 345 is divided by 5. Find the quotient.'''

        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ14b"
        self.CheckAnswerType = 1
                       
        self.number1 = randint(100,300)
        self.number2 = randint(100,300)
        
        self.divisor = randint(3,9)

        self.quotient,self.remainder = divmod(self.number1+self.number2,self.divisor)
               
        self.problem = "The sum of %d and %d is divided by %d. Find the quotient."%(self.number1,self.number2,self.divisor)
        
        self.answer = self.quotient
        
        self.unit = ""
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = [self.answer+1,self.answer-1,self.answer+5,self.answer-5,self.answer-10,self.answer+10]

                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.number1,self.number2,self.divisor,1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ15a(self):
        '''e.g.:
        The difference of 123 and 345 is divided by 5. Find the remainder.'''

        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ15a"
        self.CheckAnswerType = 1
                       
        self.number1 = randint(400,800)
        self.number2 = randint(100,300)
        
        self.divisor = randint(3,9)

        self.quotient,self.remainder = divmod(self.number1-self.number2,self.divisor)
               
        self.problem = "The difference of %d and %d is divided by %d. Find the remainder."%(self.number1,self.number2,self.divisor)
        
        self.answer = self.remainder
        
        self.unit = ""
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = [self.answer+1,self.answer+2]
        
        if self.answer != 0:
            self.wrongAnswers.append(self.answer-1)
        else:
            self.wrongAnswers.append(self.answer+3)

                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.number1,self.number2,self.divisor,2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ15b(self):
        '''e.g.:
        The difference of 123 and 345 is divided by 5. Find the quotient.'''

        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ15b"
        self.CheckAnswerType = 1
                       
        self.number1 = randint(400,800)
        self.number2 = randint(100,300)
        
        self.divisor = randint(3,9)

        self.quotient,self.remainder = divmod(self.number1-self.number2,self.divisor)
               
        self.problem = "The difference of %d and %d is divided by %d. Find the quotient."%(self.number1,self.number2,self.divisor)
        
        self.answer = self.quotient
        
        self.unit = ""
        self.dollar_unit = ""
                                    
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = [self.answer+1,self.answer-1,self.answer+5,self.answer-5]
        
        if self.answer > 10:
            self.wrongAnswers.append(self.answer+10)
            self.wrongAnswers.append(self.answer-10)
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.number1,self.number2,self.divisor,1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

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
                self.solution_text = self.solution_text + "</table>"
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
                self.solution_text = self.solution_text + "</table>"
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
                self.solution_text = self.solution_text + "</table>"
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
                self.solution_text = self.solution_text + "</table>"
        
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