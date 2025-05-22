'''
Created on Oct 27, 2011

Module: SemiCircleArea
Generates "Finding area of semicircle and quarter circle" problems for Primary 6

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

class SemiCircleArea:
    
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
        #return self.GenerateProblemType3()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            }
        return self.ProblemType[problem_type]
    
    def GenerateProblemType1(self):
        '''e.g: Find the area of the semicircle below.
                Write your answer correct to two decimal places.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius = randint(2,20)
        self.unit = randint(1,2)
        self.FunctionCall = "DrawSemiCircle2("+str(self.radius)+","+str(self.unit)+")"
        self.answer = round(float(self.radius*self.radius) * 22 / 14,2)
        if self.unit == 1:
            self.unit = "cm"
            self.problem1 = random.choice(PersonName.GirlName) +" made a semicircular handkerchief as shown below. What is the area of the handkerchief rounded off to 2 decimal places?<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = random.choice(PersonName.GirlName) +" drew a semicircle as shown below. Find its area. Round off your answer to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = random.choice(PersonName.GirlName) +" has a semicircular decal as shown below. Find the area of the decal. Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "A semicircular sticker has a radius of "+str(self.radius)+" "+self.unit+". Find its area. Write your answer correct to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "The radius of a semicircular piece of paper is "+str(self.radius)+" "+self.unit+". What is its area? Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        else:
            self.unit = "m"
            self.problem1 = random.choice(PersonName.BoyName) +" is building a flower garden on a semicircular piece of land as shown below. What is the area of the garden rounded off to 2 decimal places?<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = "A pool of water shaped like a semicircle has a radius of "+str(self.radius)+" "+self.unit+". What is the area covered by the pool rounded off to the nearest hundredth?<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = "A children's play area shaped like a semicircle has a radius of "+str(self.radius)+" "+self.unit+". Find the area of the play area. Give your answer correct to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "The radius of a semicircular sheet of iron is "+str(self.radius)+" "+self.unit+". Find its area correct to the hundredths place.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "A semicircular piece of land has a radius of "+str(self.radius)+" "+self.unit+". What is the area of the land? Round off your answer to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6 = "What is the area of the semicircle below? Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem7 = "Find the area of the semicircle below correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</font></td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem8 = "The radius of a semicircle is "+str(self.radius)+" "+self.unit+". What is its area? Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem9 = "A semicircle has a radius of "+str(self.radius)+" "+self.unit+". Find the area of the semicircle. Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6,self.problem7,self.problem8,self.problem9])
        
        oldUnit = self.unit
        self.unit = self.unit+"<sup>2</sup>"

        self.template = "DrawCircles.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.radius,oldUnit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType1(self,problem,answer,radius,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit+"<sup>2</sup>"
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of a semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius &divide; 2</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>22</u><br>&nbsp;7</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Area of the semicircle</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>22</u><br>7</td><td style='padding-left:0px; vertical-align:middle'>&nbsp;&times; "+str(radius)+" &times; " +str(radius)+" &divide; 2</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(answer)+" "+unit+"<sup>2</sup></td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Area-of-Circle" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType2(self):
        '''e.g: Find the area of the semicircle below.
                Write your answer correct to two decimal places.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius = randint(2,20)
        self.diameter = 2 * self.radius
        self.unit = randint(1,2)
        self.FunctionCall = "DrawSemiCircle1("+str(self.diameter)+","+str(self.unit)+")"
        self.answer = round(float(self.radius*self.radius) * 22 / 14,2)
        if self.unit == 1:
            self.unit = "cm"
            self.problem1 = random.choice(PersonName.GirlName) +" made a semicircular handkerchief as shown below. What is the area of the handkerchief rounded off to 2 decimal places?<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = random.choice(PersonName.GirlName) +" drew a semicircle as shown below. Find its area. Round off your answer to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = random.choice(PersonName.GirlName) +" has a semicircular decal as shown below. Find the area of the decal. Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "A semicircular sticker has a diameter of "+str(self.diameter)+" "+self.unit+". Find its area. Write your answer correct to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "The diameter of a semicircular piece of paper is "+str(self.diameter)+" "+self.unit+". What is its area? Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        else:
            self.unit = "m"
            self.problem1 = random.choice(PersonName.BoyName) +" is building a flower garden on a semicircular piece of land as shown below. What is the area of the garden rounded off to 2 decimal places?<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = "A pool of water shaped like a semicircle has a diameter of "+str(self.diameter)+" "+self.unit+". What is the area covered by the pool rounded off to the nearest hundredth?<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = "A children's play area shaped like a semicircle has a diameter of "+str(self.diameter)+" "+self.unit+". Find the area of the play area. Give your answer correct to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "The diameter of a semicircular sheet of iron is "+str(self.diameter)+" "+self.unit+". Find its area correct to the hundredths place.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "A semicircular piece of land has a diameter of "+str(self.diameter)+" "+self.unit+". What is the area of the land? Round off your answer to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6 = "What is the area of the semicircle below? Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem7 = "Find the area of the semicircle below correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Diameter = "+str(self.diameter)+" "+self.unit+", &nbsp;&pi; =&nbsp;</font></td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem8 = "The diameter of a semicircle is "+str(self.diameter)+" "+self.unit+". What is its area? Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem9 = "A semicircle has a diameter of "+str(self.diameter)+" "+self.unit+". Find the area of the semicircle. Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6,self.problem7,self.problem8,self.problem9])
        
        oldUnit = self.unit
        self.unit = self.unit + "<sup>2</sup>"
        self.template = "DrawCircles.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.diameter,self.radius,oldUnit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType2(self,problem,answer,diameter,radius,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit+"<sup>2</sup>"
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of a semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius &divide; 2</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Diameter</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Diameter &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter/2)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>22</u><br>&nbsp;7</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Area of the semicircle</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>22</u><br>7</td><td style='padding-left:0px; vertical-align:middle'>&nbsp;&times; "+str(diameter/2)+" &times; " +str(diameter/2)+" &divide; 2</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(answer)+" "+unit+"<sup>2</sup></td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Area-of-Circle" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType3(self):
        '''e.g: Find the area of the quarter circle below.
                Write your answer correct to two decimal places.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius = randint(2,20)
        self.unit = randint(1,2)
        self.FunctionCall = "DrawQuarterCircle1("+str(self.radius)+","+str(self.unit)+")"
        self.answer = round(float(self.radius*self.radius) * 22 / 28,2)
        if self.unit == 1:
            self.unit = "cm"
            self.problem1 = random.choice(PersonName.GirlName) +" cut a piece of cloth into a quarter circle as shown below. What is its area rounded off to 2 decimal places?<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = random.choice(PersonName.GirlName) +" drew a quarter circle as shown below. Find its area. Round off your answer to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = random.choice(PersonName.GirlName) +" has a decal shaped like a quarter circle as shown below. Find the area of the decal. Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "A dish shaped like a quarter circle has a radius of "+str(self.radius)+" "+self.unit+". Find its area. Write your answer correct to the nearest hundredth.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "The radius of a quarter circle piece of paper is "+str(self.radius)+" "+self.unit+". What is its area? Round off your answer to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        else:
            self.unit = "m"
            self.problem1 = random.choice(PersonName.BoyName) +" is tiling a floor that is the shape of a quarter circle as shown below. What is the area of the floor to be tiled rounded off to 2 decimal places?<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem2 = "A fish pond shaped like a quarter circle has a radius of "+str(self.radius)+" "+self.unit+". What is the area covered by the fish pond rounded off to the nearest hundredth?<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem3 = "An animal pen shaped like a quarter circle has a radius of "+str(self.radius)+" "+self.unit+". Find the area of the animal pen. Give your answer correct to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem4 = "The radius of a quarter circle sheet of steel is "+str(self.radius)+" "+self.unit+". Find its area correct to the hundredths place.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
            self.problem5 = "A quarter circle piece of land has a radius of "+str(self.radius)+" "+self.unit+". What is the area of the land? Round off your answer to 2 decimal places.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem6 = "What is the area of the quarter circle below? Give your answer correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem7 = "Find the area of the quarter circle below correct to 2 decimal places.<br><table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;Radius = "+str(self.radius)+" "+self.unit+", &nbsp;&pi; =&nbsp;</font></td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem8 = "The radius of a quarter circle is "+str(self.radius)+" "+self.unit+". What is its area? Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem9 = "A quarter circle has a radius of "+str(self.radius)+" "+self.unit+". Find the area of the quarter circle. Round off your answer to the nearest hundredth.<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>(&nbsp;&pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></tr></table>"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6,self.problem7,self.problem8,self.problem9])
        
        oldUnit = self.unit
        self.unit = self.unit + "<sup>2</sup>"
        self.template = "DrawCircles.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.radius,oldUnit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType3(self,problem,answer,radius,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit+"<sup>2</sup>"
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of a quarter circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius &divide; 4</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>22</u><br>&nbsp;7</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Area of the quarter circle</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>22</u><br>7</td><td style='padding-left:0px; vertical-align:middle'>&nbsp;&times; "+str(radius)+" &times; " +str(radius)+" &divide; 4</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(answer)+" "+unit+"<sup>2</sup></td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Area-of-Circle" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
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