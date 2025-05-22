'''
Created on Oct 25, 2011

Module: CircleCircumference
Generates "Finding circumference of a circle" problems for Primary 6

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

class CircleCircumference:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"medium":[self.GenerateProblemType1(),self.GenerateProblemType2(),],
                            }
        try:
            return random.choice(self.ProblemType[level])
        except KeyError:
            return random.choice(random.choice(self.ProblemType.values()))
        #return self.GenerateProblemType4()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
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
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g: Find the circumference of the circle below.
                Write your answer correct to two decimal places.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius = randint(2,20)
        self.unit = randint(1,2)
        self.FunctionCall = "DrawCircle2("+str(self.radius)+","+str(self.unit)+")"
        self.answer = round(float(self.radius) * 2 * 22 / 7,2)
        if self.unit == 1:
            self.unit = "cm"
            self.problem1 = random.choice(PersonName.GirlName) +" bent a piece of wire into a ring as shown below. What is the circumference of the ring rounded off to 2 decimal places?<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = random.choice(PersonName.GirlName) +" used a piece of string to form a circle as shown below. Find the length of the string she used rounded off to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = random.choice(PersonName.GirlName) +" cut a piece of paper into a round disc as shown below. Find the circumference of the disc. Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "A round bowl has a radius of "+str(self.radius)+" "+self.unit+". Find the circumference of the bowl. Write your answer correct to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "The radius of a circular mirror is "+str(self.radius)+" "+self.unit+". What is the circumference of the mirror? Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        else:
            self.unit = "m"
            self.problem1 = random.choice(PersonName.BoyName) +" is using a circular piece of land as shown below to build a garden. What is the circumference of the garden rounded off to 2 decimal places?<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = "A circular pool of water has a radius of "+str(self.radius)+" "+self.unit+". What is the circumference of the pool rounded off to the nearest hundredth?<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = "A round pond has a radius of "+str(self.radius)+" "+self.unit+". Find the circumference of the pond. Give your answer correct to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "The radius of a circular sheet of plastic is "+str(self.radius)+" "+self.unit+". Find its circumference correct to the hundredths place.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "A round stage has a radius of "+str(self.radius)+" "+self.unit+". What is the circumference of the stage? Round off your answer to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6 = "What is the circumference of the circle below? Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem7 = "Find the circumference of the circle below correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</font></td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem8 = "The radius of a circle is "+str(self.radius)+" "+self.unit+". What is its circumference? Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem9 = "A circle has a radius of "+str(self.radius)+" "+self.unit+". Find the circumference of the circle. Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6,self.problem7,self.problem8,self.problem9])

        self.template = "DrawCircles.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.radius,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType1(self,problem,answer,radius,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Circumference of a circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>2 &times; &pi; &times; Radius</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>22</u><br>&nbsp;7</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Circumference</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left; padding-right:0px; vertical-align:middle'>2 &times;&nbsp;</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>22</u><br>7</td><td style='padding-left:0px; vertical-align:middle'>&nbsp;&times; "+str(radius)+" " +unit+"</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='3'>"+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Circumference-of-Circle" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType2(self):
        '''e.g: Find the circumference of the circle below.
                Write your answer correct to two decimal places.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.diameter = random.randrange(2,30,2)
        self.unit = randint(1,2)
        self.FunctionCall = "DrawCircle1("+str(self.diameter)+","+str(self.unit)+")"
        self.answer = round(float(self.diameter) * 22/7,2)
        if self.unit == 1:
            self.unit = "cm"
            self.problem1 = random.choice(PersonName.GirlName) +" bent a piece of wire into a ring as shown below. What is the circumference of the ring rounded off to 2 decimal places?<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = random.choice(PersonName.GirlName) +" used a piece of rope to form a circle as shown below. Find the length of the rope she used rounded off to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = random.choice(PersonName.GirlName) +" cut a piece of paper into a circular disc as shown below. Find the circumference of the disc. Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "A round lid has a diameter of "+str(self.diameter)+" "+self.unit+". Find the circumference of the lid. Write your answer correct to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "The diameter of a circular box is "+str(self.diameter)+" "+self.unit+". What is the circumference of the box? Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        else:
            self.unit = "m"
            self.problem1 = random.choice(PersonName.BoyName) +" is tiling a circular piece of land. What is the circumference of the land rounded off to 2 decimal places?<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = "A circular pool of water has a diameter of "+str(self.diameter)+" "+self.unit+". What is the circumference of the pool rounded off to the nearest hundredth?<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = "A round pond has a diameter of "+str(self.diameter)+" "+self.unit+". Find the circumference of the pond. Give your answer correct to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "The diameter of a circular sheet of metal is "+str(self.diameter)+" "+self.unit+". Find its circumference correct to the hundredths place.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "A round stage has a diameter of "+str(self.diameter)+" "+self.unit+". What is the circumference of the stage? Round off your answer to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6 = "What is the circumference of the circle below? Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem7 = "Find the circumference of the circle below correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</font></td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem8 = "The diameter of a circle is "+str(self.diameter)+" "+self.unit+". What is its circumference? Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem9 = "A circle has a diameter of "+str(self.diameter)+" "+self.unit+". Find the circumference of the circle. Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6,self.problem7,self.problem8,self.problem9])

        self.template = "DrawCircles.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.diameter,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType2(self,problem,answer,diameter,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Circumference of a circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Diameter</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Diameter</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>22</u><br>&nbsp;7</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Circumference</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>22</u><br>7</td><td style='padding-left:0px; vertical-align:middle'>&nbsp;&times; "+str(diameter)+" " +unit+"</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Circumference-of-Circle" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckType):
        if CheckType==1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        if CheckType==2:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False               