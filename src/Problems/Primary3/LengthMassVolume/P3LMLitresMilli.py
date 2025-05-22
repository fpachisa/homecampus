'''
Created on May 01, 2013
Module: P3LMLitresMilli
Generates the litres and millitres problems on Length Mass Volume for Primary 3

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
import string

class P3LMLitresMilli:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType5a","ProblemType5b",],
                            6:["ProblemType6a","ProblemType6b",],
                            7:["ProblemType7",],
                            8:["ProblemType8",],9:["ProblemType9",],10:["ProblemType10",],
                            11:["ProblemType11",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemType5a(),self.GenerateProblemType5b(),],
                                    6:[self.GenerateProblemType6a(),self.GenerateProblemType6b(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],
                                    9:[self.GenerateProblemType9(),],10:[self.GenerateProblemType10(),],
                                    11:[self.GenerateProblemType11(),],
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
        #return self.GenerateProblemType11()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),"ProblemType2":self.GenerateProblemType2(),"ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),"ProblemType5a":self.GenerateProblemType5a(),"ProblemType5b":self.GenerateProblemType5b(),
                            "ProblemType6a":self.GenerateProblemType6a(),"ProblemType6b":self.GenerateProblemType6b(),
                            "ProblemType7":self.GenerateProblemType7(),"ProblemType8":self.GenerateProblemType8(),"ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10":self.GenerateProblemType10(),"ProblemType11":self.GenerateProblemType11(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),"ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),"ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        Write in millilitres.
         5 l 243 ml = _________ ml'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(100,999)

        self.problem = "Write in millilitres.<br><br>%d <font class='litreFont'>l</font> &nbsp;%d <font class='litreFont'>ml = ____ ml</font>"%(self.number1,self.number2)
        
        self.answer = self.number1*1000+self.number2
                   
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <font class='litreFont'>l</font> = 1000 <font class='litreFont'>ml</font><br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>l</font> = %d <font class='litreFont'>ml</font></font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <font class='litreFont'>l</font> = 1000 <font class='litreFont'>ml</font></font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>l</font> &nbsp;%d <font class='litreFont'>ml</font></td><td>=</td><td>%d <font class='litreFont'>l</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        Write in millilitres.
         5 l 24 ml = _________ ml'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(1,99)

        self.problem = "Write in millilitres.<br><br>%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml = ____ ml</font>"%(self.number1,self.number2)
        
        self.answer = self.number1*1000+self.number2
                   
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <font class='litreFont'>l</font> = 1000 <font class='litreFont'>ml</font><br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>l</font> = %d <font class='litreFont'>ml</font></font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <font class='litreFont'>l</font> = 1000 <font class='litreFont'>ml</font></font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font></td><td>=</td><td>%d <font class='litreFont'>l</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        Write in litres and millilitres.
         3456 ml = _____ l _____ ml
        (Write your answer as in the example below.
        Example: 5 l 678 ml)'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.number3 = randint(1,9)
        self.number4 = randint(1,9)

        self.number = int(str(self.number1)+str(self.number2)+str(self.number3)+str(self.number4))
        self.problem = "Write in litres and millilitres.<br><br>"
        self.problem = self.problem + "%d <font class='litreFont'>ml = ___ l  ___ ml</font><br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 <font class='litreFont'>l</font>&nbsp; 293 <font class='litreFont'>ml</font>)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d l %d ml"%(div,mod)
        self.answer1 = "%d <font class='litreFont'>l</font> &nbsp;%d <font class='litreFont'>ml</font>"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.answer1,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,answer1,number,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer1),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 <font class='litreFont'>ml</font> = 1 <font class='litreFont'>l</font><br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>ml</font> = %d <font class='litreFont'>l</font></font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 <font class='litreFont'>ml</font> = 1 <font class='litreFont'>l</font></font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>ml</font></td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>l</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer1)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        Write in litres and millilitres.
         3456 ml = _____ l _____ ml
        (Write your answer as in the example below.
        Example: 5 l 678 ml)'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(0,9)
        self.number3 = randint(1,9)
        self.number = int(str(self.number1)+'0'+str(self.number2)+str(self.number3))
        
        self.problem = "Write in litres and millilitres.<br><br>"
        self.problem = self.problem + "%d <font class='litreFont'>ml = ___ l  ___ ml</font><br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 <font class='litreFont'>l</font>&nbsp; 293 <font class='litreFont'>ml</font>)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d l %d ml"%(div,mod)
        self.answer1 = "%d <font class='litreFont'>l</font> &nbsp;%d <font class='litreFont'>ml</font>"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.answer1,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,answer1,number,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer1),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 <font class='litreFont'>ml</font> = 1 <font class='litreFont'>l</font><br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>ml</font> = %d <font class='litreFont'>l</font></font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 <font class='litreFont'>ml</font> = 1 <font class='litreFont'>l</font></font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>ml</font></td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>l</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer1)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5a(self):       
        '''e.g.:
        Find the total volume of water in the following set of measuring cups in millilitres.
        <Put an image.>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [[630,500,100,30,0],
                        [1160,500,500,100,60],
                        [1170,1000,100,70,0],
                        [1520,1000,500,20,0],
                        [1540,500,500,500,40],
                        [1850,500,500,500,350],
                        [2050,1000,500,500,50],
                        [2080,1000,1000,80,0],
                        [2510,1000,1000,500,10],
                        [3350,1000,1000,1000,350]]
        self.item = random.choice(self.items)
        self.number = self.item[0]
        
        self.problem = "Find the total volume of water in the following set of measuring cups in millilitres.<br><br>"
        self.problem = self.problem + "<img src='/images/P3ProblemImages/P3LMLitresMilli_"+str(self.number)+".png'>"
        
        self.answer = self.number
        
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5a(self.problem,self.answer,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5a(self,problem,answer,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of water in the first cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[1])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of water in the second cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[2])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of water in the third cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[3])
        if item[4] == 0:
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
            self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Total volume of water in the 3 cups</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(item[1],item[2],item[3])
        else:
            self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of water in the fourth cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[4])
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
            self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Total volume of water in the 4 cups</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(item[1],item[2],item[3],item[4])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5b(self):       
        '''e.g.:
        Find the total volume of water in the following set of measuring cups in litres and millilitres.
        <Put an image.>'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.items = [[630,500,100,30,0],
                        [1160,500,500,100,60],
                        [1170,1000,100,70,0],
                        [1520,1000,500,20,0],
                        [1540,500,500,500,40],
                        [1850,500,500,500,350],
                        [2050,1000,500,500,50],
                        [2080,1000,1000,80,0],
                        [2510,1000,1000,500,10],
                        [3350,1000,1000,1000,350]]
        self.item = random.choice(self.items)
        self.number = self.item[0]
        
        self.problem = "Find the total volume of water in the following set of measuring cups in litres and millilitres.<br><br>"
        self.problem = self.problem + "<img src='/images/P3ProblemImages/P3LMLitresMilli_"+str(self.number)+".png'><br>"
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 <font class='litreFont'>l</font>&nbsp; 293 <font class='litreFont'>ml</font>)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d l %d ml"%(div,mod)
        self.answer1 = "%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5b(self.problem,self.answer,self.answer1,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5b(self,problem,answer,answer1,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer1),unit)

        self.solution_text = "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of water in the first cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[1])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of water in the second cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[2])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of water in the third cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[3])
        if item[4] == 0:
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
            self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Total volume of water in the 3 cups</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(item[1],item[2],item[3])
        else:
            self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of water in the fourth cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[4])
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
            self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Total volume of water in the 4 cups</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(item[1],item[2],item[3],item[4])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[0])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%s</td></tr>"%(answer1)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6a(self):       
        '''e.g.:
        [Person.Girlname] has a <pail filled with water to the brim.>
        She empties the <pail> into the following measuring cups.
        Find the capacity of the <pail> in millilitres.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                      ['pail filled with water to the brim','pail',random.choice([['P3LMLitresMilli_water_1230',1230,1000,100,100,30],['P3LMLitresMilli_water_1520',1520,500,500,500,20],
                                                                                  ['P3LMLitresMilli_water_1610',1610,1000,500,100,10],['P3LMLitresMilli_water_2050',2050,1000,1000,50,0],
                                                                                  ['P3LMLitresMilli_water_3040',3040,1000,1000,1000,40]]),'water'],
                      ['jug filled with iced tea to the top','jug',random.choice([['P3LMLitresMilli_icedtea_720',720,500,100,100,20],['P3LMLitresMilli_icedtea_1170',1170,1000,100,70,0],
                                                                                 ['P3LMLitresMilli_icedtea_1690',1690,1000,500,100,90],['P3LMLitresMilli_icedtea_1800',1800,1000,500,300,0],
                                                                                 ['P3LMLitresMilli_icedtea_2560',2560,1000,1000,500,60]]),'tea'],
                      ['bottle filled with milk to the brim','bottle',random.choice([['P3LMLitresMilli_milk_390',390,100,100,100,90],['P3LMLitresMilli_milk_1280',1280,1000,100,100,80],
                                                                                    ['P3LMLitresMilli_milk_2010',2010,1000,1000,10,0],['P3LMLitresMilli_milk_2800',2800,1000,1000,500,300],
                                                                                    ['P3LMLitresMilli_milk_3800',3800,1000,1000,1000,800]]),'milk'],
                      ['dispenser completely filled with orange juice','dispenser',random.choice([['P3LMLitresMilli_juice_310',310,100,100,100,10],['P3LMLitresMilli_juice_1640',1640,1000,500,100,40],
                                                                                                  ['P3LMLitresMilli_juice_1950',1950,500,500,500,450],['P3LMLitresMilli_juice_2120',2120,1000,1000,100,20],
                                                                                                  ['P3LMLitresMilli_juice_3250',3250,1000,1000,1000,250]]),'juice'],
                       ['can filled with oil to the top','can',random.choice([['P3LMLitresMilli_oil_770',770,500,100,100,70],['P3LMLitresMilli_oil_1190',1190,1000,100,90,0],
                                                                             ['P3LMLitresMilli_oil_1240',1240,1000,100,100,40],['P3LMLitresMilli_oil_1750',1750,1000,500,250,0],
                                                                             ['P3LMLitresMilli_oil_2060',2060,1000,1000,60,0]]),'oil']
                      ]
        self.item = random.choice(self.items)
        self.number = self.item[2][1]
        
        self.problem = "%s has a %s.<br><br>"%(self.name,self.item[0])
        self.problem = self.problem + "She empties the %s into the following measuring cups.<br><br>"%(self.item[1])
        self.problem = self.problem + "Find the capacity of the %s in millilitres.<br><br>"%(self.item[1])
        self.problem = self.problem + "<img src='/images/P3ProblemImages/"+self.item[2][0]+".png'>"
        
        self.answer = self.number
        
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6a(self.problem,self.answer,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6a(self,problem,answer,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of %s in the first cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[3],item[2][2])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of %s in the second cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[3],item[2][3])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of %s in the third cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[3],item[2][4])
        if item[2][5] == 0:
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
            self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Total volume of %s in the 3 cups</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(item[3],item[2][2],item[2][3],item[2][4])
        else:
            self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of %s in the fourth cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[3],item[2][5])
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
            self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Total volume of %s in the 4 cups</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(item[3],item[2][2],item[2][3],item[2][4],item[2][5])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(answer)
        self.solution_text = self.solution_text + "<tr><td colspan=3 style='padding:0px'><br>The capacity of the %s is %d <font class='litreFont'>ml</font> .</td></tr>"%(item[1],answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6b(self):       
        '''e.g.:
        [Person.Girlname] has a <pail filled with water to the brim.>
        She empties the <pail> into the following measuring cups.
        Find the capacity of the <pail> in litres and millilitres.
        (Write your answer as in the example below.
        Example: 5 l 678 ml)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                      ['pail filled with water to the brim','pail',random.choice([['P3LMLitresMilli_water_1230',1230,1000,100,100,30],['P3LMLitresMilli_water_1520',1520,500,500,500,20],
                                                                                  ['P3LMLitresMilli_water_1610',1610,1000,500,100,10],['P3LMLitresMilli_water_2050',2050,1000,1000,50,0],
                                                                                  ['P3LMLitresMilli_water_3040',3040,1000,1000,1000,40]]),'water'],
                      ['jug filled with iced tea to the top','jug',random.choice([['P3LMLitresMilli_icedtea_720',720,500,100,100,20],['P3LMLitresMilli_icedtea_1170',1170,1000,100,70,0],
                                                                                 ['P3LMLitresMilli_icedtea_1690',1690,1000,500,100,90],['P3LMLitresMilli_icedtea_1800',1800,1000,500,300,0],
                                                                                 ['P3LMLitresMilli_icedtea_2560',2560,1000,1000,500,60]]),'tea'],
                      ['bottle filled with milk to the brim','bottle',random.choice([['P3LMLitresMilli_milk_390',390,100,100,100,90],['P3LMLitresMilli_milk_1280',1280,1000,100,100,80],
                                                                                    ['P3LMLitresMilli_milk_2010',2010,1000,1000,10,0],['P3LMLitresMilli_milk_2800',2800,1000,1000,500,300],
                                                                                    ['P3LMLitresMilli_milk_3800',3800,1000,1000,1000,800]]),'milk'],
                      ['dispenser completely filled with orange juice','dispenser',random.choice([['P3LMLitresMilli_juice_310',310,100,100,100,10],['P3LMLitresMilli_juice_1640',1640,1000,500,100,40],
                                                                                                  ['P3LMLitresMilli_juice_1950',1950,500,500,500,450],['P3LMLitresMilli_juice_2120',2120,1000,1000,100,20],
                                                                                                  ['P3LMLitresMilli_juice_3250',3250,1000,1000,1000,250]]),'juice'],
                       ['can filled with oil to the top','can',random.choice([['P3LMLitresMilli_oil_770',770,500,100,100,70],['P3LMLitresMilli_oil_1190',1190,1000,100,90,0],
                                                                             ['P3LMLitresMilli_oil_1240',1240,1000,100,100,40],['P3LMLitresMilli_oil_1750',1750,1000,500,250,0],
                                                                             ['P3LMLitresMilli_oil_2060',2060,1000,1000,60,0]]),'oil']
                      ]
        self.item = random.choice(self.items)
        self.number = self.item[2][1]
        
        self.problem = "%s has a %s.<br><br>"%(self.name,self.item[0])
        self.problem = self.problem + "She empties the %s into the following measuring cups.<br><br>"%(self.item[1])
        self.problem = self.problem + "Find the capacity of the %s in litres and millilitres.<br><br>"%(self.item[1])
        self.problem = self.problem + "<img src='/images/P3ProblemImages/"+self.item[2][0]+".png'><br>"
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 <font class='litreFont'>l</font> 293 <font class='litreFont'>ml</font>)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d l %d ml"%(div,mod)
        self.answer1 = "%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""       
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6b(self.problem,self.answer,self.answer1,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6b(self,problem,answer,answer1,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer1),unit)

        self.solution_text = "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of %s in the first cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[3],item[2][2])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of %s in the second cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[3],item[2][3])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of %s in the third cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[3],item[2][4])
        if item[2][5] == 0:
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
            self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Total volume of %s in the 3 cups</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(item[3],item[2][2],item[2][3],item[2][4])
        else:
            self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Volume of %s in the fourth cup</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[3],item[2][5])
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
            self.solution_text = self.solution_text + "<tr><td style='padding:0px'>Total volume of %s in the 4 cups</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(item[3],item[2][2],item[2][3],item[2][4],item[2][5])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(item[2][1])
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:center'>&nbsp; =</td><td>%s</td></tr>"%(answer1)
        self.solution_text = self.solution_text + "<tr><td colspan=3 style='padding:0px'><br>The capacity of the %s is %s .</td></tr>"%(item[1],answer1)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        A <container> can hold 1 l 230 ml of <juice when filled to the brim>.
        What is the <capacity> of the container in millilitres?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['container','juice when filled to the brim',randint(1000,9999)],
                      ['pail','water when filled completely',randint(1000,9999)],
                      ['bottle','ketchup when filled completely',randint(1000,2000)],
                      ['kettle','tea when filled to the brim',randint(1000,2000)],
                      ['pot','sauce when filled to the top',randint(1000,3000)],
                      ['thermos flask','milk when filled completely',randint(2000,4000)],
                      ['can','oil when filled to the top',randint(2000,4000)],
                      ['jar','rose drink when filled to the top',randint(4000,7000)],
                      ['coffee dispenser','coffee when filled to the brim',randint(4000,7000)],
                      ['barrel','beverage when filled completely',randint(6000,9999)]]
        
        self.item = random.choice(self.items)
        
        self.number = self.item[2]
        self.number1,self.number2 = divmod(self.number,1000)

        self.problem = "A %s can hold %d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>&nbsp; of %s.<br><br>"%(self.item[0],self.number1,self.number2,self.item[1])
        self.problem = self.problem + "What is the capacity of the %s in millilitres?"%(self.item[0])
        
        self.answer = self.number
                   
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,number1,number2,item0,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <font class='litreFont'>l</font> = 1000 <font class='litreFont'>ml</font><br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>l</font> = %d <font class='litreFont'>ml</font></font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <font class='litreFont'>l</font> = 1000 <font class='litreFont'>ml</font></font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>l</font> &nbsp;%d <font class='litreFont'>ml</font></td><td>=</td><td>%d <font class='litreFont'>l</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The capacity of the %s is %d <font class='litreFont'>ml</font></font> ."%(item0,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        A <can> has 1230 ml of <milk>.
        What is the volume of <milk> in the <can> in litres and millilitres?
        (Write your answer as in the example below.
        Example: 5 l 678 ml)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['can','milk'],['container','chocolate drink'],['tank','oil'],['tub','water'],['bottle','ink'],['flask','chemical fluid'],['jar','honey'],['dispenser','pomegranate juice'],['cooler','beverage'],['pot','coffee']]
        self.item = random.choice(self.items)
        
        self.number = random.randrange(1000,5000,10)
        
        self.problem = "A %s has %d <font class='litreFont'>ml</font> of %s.<br><br>"%(self.item[0],self.number,self.item[1])
        self.problem = self.problem + "What is the volume of %s in the %s in litres and millilitres?<br><br>"%(self.item[1],self.item[0])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 <font class='litreFont'>l</font>&nbsp; 293 <font class='litreFont'>ml</font>)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d l %d ml"%(div,mod)
        self.answer1 = "%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.answer1,self.number,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,answer1,number,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer1),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 <font class='litreFont'>ml</font> = 1 <font class='litreFont'>l</font><br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>ml</font> = %d <font class='litreFont'>l</font></font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 <font class='litreFont'>ml</font> = 1 <font class='litreFont'>l</font></font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>ml</font></td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>l</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer1)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The volume of %s in the %s is %s </font> ."%(item1,item0,answer1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        [Person.Auntyname] <bought> 2 l 300 ml <milk>.
        How much milk did she <buy> in millilitres?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [['bought','milk','buy','milk',random.randrange(2000,4000,100)],
                      ['bought','ice cream for her family','buy','ice cream',random.randrange(1000,2000,100)],
                      ['made','soup for a party','make','soup',random.randrange(2000,3000,100)],
                      ['made','tomato puree','make','tomato puree',random.randrange(2000,3000,100)],
                      ['sold','vinegar','sell','vinegar',random.randrange(5000,9900,100)],
                      ['sold','coconut water at her drinks stall','sell','coconut water',random.randrange(1000,9900,100)],
                      ['had','mango juice','have','mango juice',random.randrange(4000,6000,100)],
                      ['had','soy sauce','have','soy sauce',random.randrange(3000,4000,100)],
                      ['used','water to wash her clothes','use','water',random.randrange(1000,9900,100)],
                      ['used','sugar syrup to make a dessert','use','sugar syrup',random.randrange(1000,3000,100)]]
        
        self.item = random.choice(self.items)
        
        self.number = self.item[4]
        self.number1,self.number2 = divmod(self.number,1000)

        self.problem = "%s %s %d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>&nbsp; of %s.<br><br>"%(self.name,self.item[0],self.number1,self.number2,self.item[1])
        self.problem = self.problem + "How much %s did she %s in millilitres?"%(self.item[3],self.item[2])
        
        self.answer = self.number
                   
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,number1,number2,item0,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <font class='litreFont'>l</font> = 1000 <font class='litreFont'>ml</font><br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>l</font> = %d <font class='litreFont'>ml</font></font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <font class='litreFont'>l</font> = 1000 <font class='litreFont'>ml</font></font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>l</font> &nbsp;%d <font class='litreFont'>ml</font></td><td>=</td><td>%d <font class='litreFont'>l</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>She %s %d <font class='litreFont'>ml</font>&nbsp; of %s.</font>"%(item0,answer,item3)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:
        [Person.Unclename] <bought> 2300 ml <orange juice>.
        Find the volume of <orange juice he bought> in litres and millilitres?
        (Write your answer as in the example below.
        Example: 5 l 678 ml)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['bought','yogurt','yogurt he bought',random.randrange(1000,2000,100),'He bought','yogurt'],
                      ['bought','flavoured milk','flavoured milk he bought',random.randrange(2000,4000,100),'He bought','flavoured milk'],
                      ['made','chicken soup','chicken soup he made',random.randrange(2000,3000,100),'He made','chicken soup'],
                      ['made','milkshake','milkshake he made',random.randrange(2000,3000,100),'He made','milkshake'],
                      ['sold','mayonnaise','mayonnaise he sold',random.randrange(3000,5000,100),'He sold','mayonnaise'],
                      ['sold','cough syrup at his pharmacy','cough syrup he sold',random.randrange(1000,9900,100),'He sold','cough syrup'],
                      ['packed','fruit pulp into bottles','fruit pulp he packed',random.randrange(3000,4000,100),'He packed','fruit pulp'],
                      ['had','olive oil at his grocery store','olive oil he had',random.randrange(4000,6000,100),'He had','olive oil'],
                      ['used','water for his plants','water he used',random.randrange(1000,9900,100),'He used','water'],
                      ['used','chilli sauce','chilli sauce he used',random.randrange(1000,3000,100),'He used','chilli sauce'],
                      ['and his friends donated','blood during a blood donation drive','blood they donated',random.randrange(1000,3000,100),'They donated','blood']]
        
        self.item = random.choice(self.items)
        
        self.number = self.item[3]
        
        self.problem = "%s %s %d <font class='litreFont'>ml</font>&nbsp; of %s.<br><br>"%(self.name,self.item[0],self.number,self.item[1])
        self.problem = self.problem + "Find the volume of %s in litres and millilitres?<br><br>"%(self.item[2])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 <font class='litreFont'>l</font>&nbsp; 293 <font class='litreFont'>ml</font> )"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d l %d ml"%(div,mod)
        self.answer1 = "%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(div,mod)

        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.answer1,self.number,self.item[4],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,answer1,number,item4,item5,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer1),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 <font class='litreFont'>ml</font> = 1 <font class='litreFont'>l</font><br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>ml</font> = %d <font class='litreFont'>l</font></font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 <font class='litreFont'>ml</font> = 1 <font class='litreFont'>l</font></font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>ml</font></td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>l</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer1)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>%s &nbsp;%s of %s</font>."%(item4,answer1,item5)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:
        Fill in the blank with 'l' or 'ml'.
         <A fountain pen has about> 2 ____ <of ink.>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['A fountain pen can hold about','of ink.','ml',randint(2,4),'A fountain pen is a small object.<br>It can normally hold about&nbsp;',"<font class='litreFont'>ml</font>&nbsp; of ink.<br>A fountain pen that could hold&nbsp;","<font class='litreFont'>l</font>&nbsp; of ink would be too huge to write with!"],
                      ['A cup holds about','of liquid.','ml',random.choice([230,240,250]),'A cup holds one serving of a liquid.<br>A standard cup holds about&nbsp;',"<font class='litreFont'>ml</font>&nbsp; of liquid.<br>A cup that could hold&nbsp;","<font class='litreFont'>l</font>&nbsp; of liquid would be too huge to drink from!"],
                      ['I had a bowl of soup for lunch. It had about','of soup in it.','ml',random.randrange(200,1000,10),'A bowl holds one serving of soup.<br>A regular bowl holds about&nbsp;',"<font class='litreFont'>ml</font>&nbsp; of soup.<br>A bowl that could hold&nbsp;","<font class='litreFont'>l</font>&nbsp; of soup would be used to serve a giant!"],
                      ['In some countries, a can of soda has about','of beverage.','ml',random.choice([200,245,250,300,330,350,355,375,440,500]),'The amount of beverage that a can of soda holds varies among countries.<br>It is normal for a can to have about&nbsp;',"<font class='litreFont'>ml</font>&nbsp; of beverage.<br>A container that could hold&nbsp;","<font class='litreFont'>l</font>&nbsp; of beverage would be a tank and not a can!"],
                      ["My friend's baby sister drinks about",'of milk each day.','ml',random.randrange(500,900,10),'The amount of milk babies drink varies from one baby to another.<br>However, a baby would drink more or less about&nbsp;',"<font class='litreFont'>ml</font>&nbsp; of milk.<br>A baby that could drink&nbsp;","<font class='litreFont'>l</font>&nbsp; of milk would be out of this world!"],
                      ['A glass of water has about','of water.','ml',random.choice([200,210,220,230,240,250]),'A glass holds one serving of water.<br>A standard glass holds about&nbsp;',"<font class='litreFont'>ml</font>&nbsp; of water.<br>A serving of&nbsp;","<font class='litreFont'>l</font>&nbsp; of water would be too much to drink!"],
                      ['My family uses about','of milk each day.','l',random.choice([1,2,3,4,5]),'The amount of milk used by a family depends upon the size of the family.<br>However, that amount is always measured in litres, and in this case it is about&nbsp;',"<font class='litreFont'>l</font>&nbsp;.<br>If a family uses only&nbsp;","<font class='litreFont'>ml</font>&nbsp; of milk each day, that means it uses no milk at all, which would not be considered normal!"],
                      ['My family drinks about','of water each day.','l',randint(8,20),'A normal person drinks about 2 litres of water a day.<br>The amount of water that a family drinks each day depends upon the size of the family.<br>However, that amount is always measured in litres, and in this case it is about&nbsp;',"<font class='litreFont'>l</font>&nbsp;.<br>If a family drinks only&nbsp;","<font class='litreFont'>ml</font>&nbsp; of water a day, it means it drinks no water at all, which is impossible!"],
                      ['Milk bottles in the supermarket contain about','of milk each.','l',random.choice([1,2,4]),'Milk bottles come in different sizes.<br>One standard size you can get in the supermarket contains about&nbsp;',"<font class='litreFont'>l</font>&nbsp; of milk.<br>If the bottle contains only&nbsp;","<font class='litreFont'>ml</font>&nbsp; of milk, that bottle would be a toy bottle!"],
                      ['I use about','of water to take a shower.','l',random.choice([20,30,40,50]),'The amount of water a person uses to take a shower varies among individuals.<br>However, that amount is always measured in litres, in this case it is about&nbsp;',"<font class='litreFont'>l</font>&nbsp;.<br>It is impossible to take a shower with as little as&nbsp;","<font class='litreFont'>ml</font>&nbsp; of water, which is even less than what a glass can hold!"]]
        
        self.item = random.choice(self.items)
        
        self.number = self.item[3]
        
        self.problem = "Fill in the blank with &nbsp;<font class='litreFont'>l</font>&nbsp; or &nbsp;<font class='litreFont'>ml</font> .<br><br>"
        self.problem = self.problem + "%s %d ____ %s"%(self.item[0],self.number,self.item[1])
        
        self.answer = self.item[2]
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.number,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,number,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s<font class='litreFont'>%s</font> %s"%(dollar_unit,str(answer),unit)
        self.solution_text =  "<font class='ExplanationFont'>%s %d %s %d %s</font>"%(item[4],number,item[5],number,item[6])
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
        Write in millilitres.
         5 l 243 ml = _________ ml'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1"
        self.CheckAnswerType = 1

        self.number1 = randint(1,9)
        self.number2 = randint(100,999)

        self.problem = "Write in millilitres.<br><br>%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml = ____ ml</font>"%(self.number1,self.number2)
        
        self.answer = self.number1*1000+self.number2
                   
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [float(self.answer)/100,
                             str(self.number1)+"."+str(self.number2),float(self.answer)/10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        Write in millilitres.
         5 l 24 ml = _________ ml'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ2"
        self.CheckAnswerType = 1

        self.number1 = randint(1,9)
        self.number2 = randint(1,99)

        self.problem = "Write in millilitres.<br><br>%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml = ____ ml</font>"%(self.number1,self.number2)
        
        self.answer = self.number1*1000+self.number2
                   
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [float(self.answer)/100,
                             str(self.number1)+"."+str(self.number2),float(self.answer)/10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
        Write in litres and millilitres.
         3456 ml = _____ l _____ ml
        (Write your answer as in the example below.
        Example: 5 l 678 ml)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ3"
        self.CheckAnswerType = 2

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.number3 = randint(1,9)
        self.number4 = randint(1,9)

        self.number = int(str(self.number1)+str(self.number2)+str(self.number3)+str(self.number4))
        self.problem = "Write in litres and millilitres.<br><br>"
        self.problem = self.problem + "%d <font class='litreFont'>l = ___ l  ___ ml</font><br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 <font class='litreFont'>l</font>&nbsp; 293 <font class='litreFont'>ml</font>)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d l %d ml"%(div,mod)
        self.answer1 = "%d <font class='litreFont'>l</font> &nbsp;%d <font class='litreFont'>ml</font>"%(div,mod)
                
        self.unit = ""
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = ["%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(divmod(self.number,10)),
                             "%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(divmod(self.number,100)),
                             "%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(divmod(self.number,1)),
                             str(self.number1)+str(self.number2)+" <font class='litreFont'>l</font> &nbsp;"+str(self.number3)+" <font class='litreFont'>ml</font>"]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.answer1,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer1,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ4(self):
        '''e.g.:
        Write in litres and millilitres.
         3456 ml = _____ l _____ ml
        (Write your answer as in the example below.
        Example: 5 l 678 ml)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ4"
        self.CheckAnswerType = 2

        self.number1 = randint(1,9)
        self.number2 = randint(0,9)
        self.number3 = randint(1,9)
        self.number = int(str(self.number1)+'0'+str(self.number2)+str(self.number3))
        
        self.problem = "Write in litres and millilitres.<br><br>"
        self.problem = self.problem + "%d <font class='litreFont'>l = ___ l  ___ ml</font><br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 <font class='litreFont'>l</font>&nbsp; 293 <font class='litreFont'>ml</font>)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d l %d ml"%(div,mod)
        self.answer1 = "%d <font class='litreFont'>l</font> &nbsp;%d <font class='litreFont'>ml</font>"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = ["%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(divmod(self.number,10)),
                             "%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(divmod(self.number,100)),
                             "%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(divmod(self.number,1)),
                             str(self.number1)+str(self.number2)+" <font class='litreFont'>l</font>&nbsp; "+str(self.number3)+" <font class='litreFont'>ml</font>"]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.answer1,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer1,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswer == 2:
            try:
                answer1 = string.join(str(answer).split(),"")
                '''If user enter answer as 1l 007 ml that should also be correct'''
                if len(answer1.partition("l")[2])==4:
                    answer2 = answer1.partition("l")[0]+"l0"+answer1.partition("l")[2]
                elif len(answer1.partition("l")[2])==3:
                    answer2 = answer1.partition("l")[0]+"l00"+answer1.partition("l")[2]
                else:
                    answer2 = answer1
                InputAnswer = string.join(str(InputAnswer).split(),"")
                return answer1.capitalize() == InputAnswer.capitalize() or answer2.capitalize() == InputAnswer.capitalize()
            except ValueError:
                return False
        elif CheckAnswer == 3:
            try:
                return str(answer).capitalize() == str(InputAnswer).capitalize()
            except ValueError:
                return False