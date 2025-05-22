'''
Created on Oct 26, 2011

Module: SemiCirclePerimeter
Generates "Finding perimeter of semicircle and quarter circle" problems for Primary 6

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

class SemiCirclePerimeter:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"medium":[self.GenerateProblemType1(),self.GenerateProblemType2(),self.GenerateProblemType3(),],
                            }
        try:
            return random.choice(self.ProblemType[level])
        except KeyError:
            return random.choice(random.choice(self.ProblemType.values()))
        #return self.GenerateProblemType3()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            3:["ProblemType3",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],
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
                            "ProblemType3":self.GenerateProblemType3(),
                            }
        return self.ProblemType[problem_type]
    
    def GenerateProblemType1(self):
        '''e.g: Find the perimeter of the semicircle below.
                Write your answer correct to two decimal places.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius = randint(2,20)
        self.unit = randint(1,2)
        self.FunctionCall = "DrawSemiCircle2("+str(self.radius)+","+str(self.unit)+")"
        self.answer = round(float(self.radius) * 22 / 7+2*float(self.radius),2)
        if self.unit == 1:
            self.unit = "cm"
            self.problem1 = random.choice(PersonName.GirlName) +" has a decal shaped like a semicircle as shown below. What is the perimeter of the decal? Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = random.choice(PersonName.GirlName) +" used a piece of string to form a semicircle as shown below. Find the length of the string she used rounded off to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = random.choice(PersonName.GirlName) +" cut a round disc into 2 halves, one of which is shown below. Find the perimeter of each half. Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = random.choice(PersonName.GirlName) +" had some fabric. She cut out a semicircular piece with a radius of "+str(self.radius)+" "+self.unit+" from it as shown below. Find the perimeter of the cut-out. Write your answer correct to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "The radius of a semicircular piece of paper is "+str(self.radius)+" "+self.unit+". What is its perimeter? Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        else:
            self.unit = "m"
            self.problem1 = random.choice(PersonName.BoyName) +" is fencing a piece of land shaped like a half circle as shown below. Find the length of the fence he will need. Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = "A semicircular fish pond has a radius of "+str(self.radius)+" "+self.unit+". What is the perimeter of the pond rounded off to the nearest hundredth?<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = "A hole in the ground is shaped like a half circle with a radius of "+str(self.radius)+" "+self.unit+". Find the perimeter of the hole. Give your answer correct to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "The radius of a semicircular sheet of steel is "+str(self.radius)+" "+self.unit+". Find its perimeter correct to the hundredths place.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "An animal pen shaped like a half circle has a radius of "+str(self.radius)+" "+self.unit+". What is its perimeter? Round off your answer to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6a = "What is the perimeter of the semicircle below? Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6b = "Find the perimeter of the half circle below correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</font></td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem7a = "The radius of a semicircle is "+str(self.radius)+" "+self.unit+". What is its perimeter? Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem7b = "A half circle has a radius of "+str(self.radius)+" "+self.unit+". Find its perimeter. Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6 = random.choice([self.problem6a,self.problem6b])
        self.problem7 = random.choice([self.problem7a,self.problem7b])
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6,self.problem7])
        
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
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter of a semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Half the circumference of the circle + Diameter</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>(&pi; &times; Radius) + (2 &times; Radius)</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of the semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>22</u><br>&nbsp;7</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Perimeter of the semicircle</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left; padding-right:0px; vertical-align:middle'>(</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>22</u><br>7</td><td style='padding-left:0px; vertical-align:middle'>&nbsp;&times; "+str(radius)+") + (2 &times; "+str(radius)+")</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>&asymp;</td><td style='text-align:left' colspan='3'>"+str(round(float(radius)*22/7,3))+" + "+str(2*radius)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='3'>"+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Circumference-of-Circle" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType2(self):
        '''e.g: Find the perimeter of the semicircle below.
                Write your answer correct to two decimal places.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius = randint(2,20)
        self.diameter = 2 * self.radius
        self.unit = randint(1,2)
        self.FunctionCall = "DrawSemiCircle1("+str(self.diameter)+","+str(self.unit)+")"
        self.answer = round(float(self.radius) * 22 / 7+2*float(self.radius),2)
        if self.unit == 1:
            self.unit = "cm"
            self.problem1 = random.choice(PersonName.GirlName) +" has a sticker shaped like a semicircle as shown below. What is the perimeter of the sticker? Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = random.choice(PersonName.GirlName) +" bent a piece of wire into a semicircle as shown below. Find the length of the wire she used rounded off to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = random.choice(PersonName.GirlName) +" drew a semicircle as shown below. Find the perimeter of the semicircle. Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = random.choice(PersonName.GirlName) +" had a sheet of paper. She cut out a semicircular piece with a diameter of "+str(self.diameter)+" "+self.unit+" from it as shown below. Find the perimeter of the cut-out. Write your answer correct to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "The diameter of a semicircular piece of cloth is "+str(self.diameter)+" "+self.unit+". What is its perimeter? Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        else:
            self.unit = "m"
            self.problem1 = random.choice(PersonName.BoyName) +" is building a boundary wall around a piece of land shaped like a half circle as shown below. Find the length of the boundary wall. Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = "A semicircular lagoon has a diameter of "+str(self.diameter)+" "+self.unit+". What is the perimeter of the lagoon rounded off to the nearest hundredth?<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = "A ditch in the ground is shaped like a half circle with a diameter of "+str(self.diameter)+" "+self.unit+". Find the perimeter of the ditch. Give your answer correct to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "The diameter of a semicircular sheet of plastic is "+str(self.diameter)+" "+self.unit+". Find its perimeter correct to the hundredths place.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "A children's play area shaped like a half circle has a diameter of "+str(self.diameter)+" "+self.unit+". What is its perimeter? Round off your answer to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6a = "What is the perimeter of the semicircle below? Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6b = "Find the perimeter of the half circle below correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</font></td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem7a = "The diameter of a semicircle is "+str(self.diameter)+" "+self.unit+". What is its perimeter? Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem7b = "A half circle has a diameter of "+str(self.diameter)+" "+self.unit+". Find its perimeter. Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6 = random.choice([self.problem6a,self.problem6b])
        self.problem7 = random.choice([self.problem7a,self.problem7b])
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6,self.problem7])

        self.template = "DrawCircles.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.diameter,self.radius,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType2(self,problem,answer,diameter,radius,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter of a semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left;padding-right:0px' colspan='4'>Half the circumference of the circle + Diameter</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>(</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>1</u><br>2</td><td style='text-align:left;vertical-align:middle;padding-left:0px'>&nbsp;&times; &pi; &times; Diameter ) + Diameter</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Diameter of the semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>22</u><br>&nbsp;7</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Perimeter of the semicircle</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>(&nbsp;</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>1</u><br>2</td><td style='text-align:left;padding-right:0px;padding-left:0px;vertical-align:middle'>&nbsp;&times;&nbsp;</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>22</u><br>7</td><td style='padding-left:0px; vertical-align:middle'>&nbsp;&times; "+str(diameter)+" ) + "+str(diameter)+"</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>&asymp;</td><td style='text-align:left' colspan='6'>"+str(round(float(radius)*22/7,3))+" + "+str(2*radius)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='6'>"+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Circumference-of-Circle" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType3(self):
        '''e.g: Find the perimeter of the quarter circle below.
                Write your answer correct to two decimal places.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius = randint(2,20)
        self.unit = randint(1,2)
        self.FunctionCall = "DrawQuarterCircle1("+str(self.radius)+","+str(self.unit)+")"
        self.answer = round(float(self.radius) * 22 / 14+2*float(self.radius),2)
        if self.unit == 1:
            self.unit = "cm"
            self.problem1 = random.choice(PersonName.GirlName) +" bent a piece of wire into a quadrant as shown below. What is the length of the wire used? Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = random.choice(PersonName.GirlName) +" used a piece of string to form a quarter circle as shown below. Find the perimeter of the quadrant formed rounded off to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = random.choice(PersonName.GirlName) +" cut a round disc into 4 quadrants, one of which is shown below. Find the perimeter of each quandrant. Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = random.choice(PersonName.GirlName) +" had some fabric. She cut out a quarter circle piece with a radius of "+str(self.radius)+" "+self.unit+" from it as shown below. Find the perimeter of the cut-out. Write your answer correct to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "The radius of a mirror shaped like a quadrant is "+str(self.radius)+" "+self.unit+". What is the perimeter of the mirror? Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        else:
            self.unit = "m"
            self.problem1 = random.choice(PersonName.BoyName) +" is building a fence around a piece of land shaped like a quadrant as shown below. Find the length of the fence he will need. Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = "A pool of water shaped like a quadrant has a radius of "+str(self.radius)+" "+self.unit+". What is the perimeter of the pool rounded off to the nearest hundredth?<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = "A hole in the ground is shaped like a quarter circle with a radius of "+str(self.radius)+" "+self.unit+". Find the perimeter of the hole. Give your answer correct to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "The radius of a quarter circle sheet of aluminium is "+str(self.radius)+" "+self.unit+". Find its perimeter correct to the hundredths place.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "An animal pen shaped like a quadrant has a radius of "+str(self.radius)+" "+self.unit+". What is the perimeter of the animal pen? Round off your answer to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6a = "What is the perimeter of the quadrant below? Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6b = "Find the perimeter of the quarter circle below correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</font></td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem7a = "The radius of a quarter circle is "+str(self.radius)+" "+self.unit+". What is its perimeter? Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem7b = "A quadrant has a radius of "+str(self.radius)+" "+self.unit+". Find its perimeter. Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6 = random.choice([self.problem6a,self.problem6b])
        self.problem7 = random.choice([self.problem7a,self.problem7b])
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6,self.problem7])
        
        self.template = "DrawCircles.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.radius,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType3(self,problem,answer,radius,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter of a quadrant</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left;padding-right:0px' colspan='4'>A quarter of the circumference of circle + ( 2 &times; Radius )</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>(</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>1</u><br>4</td><td style='text-align:left;vertical-align:middle;padding-left:0px'>&nbsp;&times; 2 &times; &pi; &times; Radius ) + ( 2 &times; Radius )</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of the quadrant</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>22</u><br>&nbsp;7</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Perimeter of the quadrant</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>(&nbsp;</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>1</u><br>4</td><td style='text-align:left;padding-right:0px;padding-left:0px;vertical-align:middle'>&nbsp;&times; 2 &times;&nbsp;</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>22</u><br>7</td><td style='padding-left:0px; vertical-align:middle'>&nbsp;&times; "+str(radius)+" ) + ( 2 &times; "+str(radius)+" )</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>&asymp;</td><td style='text-align:left' colspan='6'>"+str(round(float(radius)*22/14,2))+" + "+str(2*radius)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='6'>"+str(answer)+" "+unit+"</td></tr></table>"
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