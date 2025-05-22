'''
Created on Oct 29, 2011

Module: CompositeFigures
Generates "Finding area/perimeter of a composite figure" problems for Primary 6

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

class CompositeFigures:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"medium":[self.GenerateProblemType1(),self.GenerateProblemType1a(),self.GenerateProblemType3(),
                                         self.GenerateProblemType3a(),self.GenerateProblemType5(),self.GenerateProblemType7(),
                                         self.GenerateProblemType9()],
                            "difficult":[self.GenerateProblemType2(),self.GenerateProblemType2a(),self.GenerateProblemType4(),self.GenerateProblemType4a(),
                                         self.GenerateProblemType5a(),self.GenerateProblemType6(),self.GenerateProblemType8(),
                                         self.GenerateProblemType9a(),self.GenerateProblemType10(),self.GenerateProblemType10a()],
                            }
        try:
            return random.choice(self.ProblemType[level])
        except KeyError:
            return random.choice(random.choice(self.ProblemType.values()))
        #return self.GenerateProblemType7()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''                
                      
        self.ProblemType = {1:["ProblemType1","ProblemType1a"],
                            2:["ProblemType3","ProblemType3a",],
                            3:["ProblemType5","ProblemType5a",],
                            4:["ProblemType6",],
                            5:["ProblemType8",],
                            6:["ProblemType10","ProblemType10a",],
                            7:["ProblemType2","ProblemType2a",],
                            8:["ProblemType4","ProblemType4a",],
                            9:["ProblemType7",],
                            10:["ProblemType9","ProblemType9a",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemType1a()],
                                    2:[self.GenerateProblemType3(),self.GenerateProblemType3a(),],
                                    3:[self.GenerateProblemType5(),self.GenerateProblemType5a()],
                                    4:[self.GenerateProblemType6(),],
                                    5:[self.GenerateProblemType8()],
                                    6:[self.GenerateProblemType10(),self.GenerateProblemType10a()],
                                    7:[self.GenerateProblemType2(),self.GenerateProblemType2a(),],
                                    8:[self.GenerateProblemType4(),self.GenerateProblemType4a()],
                                    9:[self.GenerateProblemType7(),],
                                    10:[self.GenerateProblemType9(),self.GenerateProblemType9a()],                                    
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
        #return self.GenerateProblemType22()
        
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(self.GenerateProblemType.values())
        else:
            if LastProblemID in self.ProblemType.values():
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if v == LastProblemID][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return self.GenerateProblemType[NextProblemKey]
            else:
                return random.choice(self.GenerateProblemType.values())
        #return self.GenerateProblemType10a()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType1a":self.GenerateProblemType1a(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType2a":self.GenerateProblemType2a(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType3a":self.GenerateProblemType3a(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType4a":self.GenerateProblemType4a(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType5a":self.GenerateProblemType5a(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemType9a":self.GenerateProblemType9a(),
                            "ProblemType10":self.GenerateProblemType10(),
                            "ProblemType10a":self.GenerateProblemType10a(),
                            }
        return self.ProblemType[problem_type]
            
    def GenerateProblemType1(self):
        '''e.g: Find the area of the shaded circle enclosed in a square of side 5 cm.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius = randint(2,20)
        self.diameter = self.radius * 2
        self.unit = randint(1,2)
        self.FunctionCall = "DrawCircleSquare1("+str(self.diameter)+","+str(self.unit)+")"
        self.answer = round(float(self.radius*self.radius) * 22 / 7,2)
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"     
        self.problem = "Find the area of the shaded circle below enclosed in a square of side "+str(self.diameter)+" "+self.unit+". Write your answer correct to 2 decimal places.<br>"
        self.problem = self.problem + "<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>( Given, &pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></font></tr></table>"
        oldUnit = self.unit
        self.unit = self.unit + "<sup>2</sup>"
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.radius,self.diameter,oldUnit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType1(self,problem,answer,radius,diameter,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit+"<sup>2</sup>"
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of a circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>22</u><br>&nbsp;7</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Diameter of the shaded circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Side of the enclosing square</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of the shaded circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Diameter &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+unit+"</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Area of the shaded circle</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>22</u><br>7</td><td style='padding-left:0px; vertical-align:middle'>&nbsp;&times; "+str(radius)+" &times; " +str(radius)+"</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(answer)+" "+unit+"<sup>2</sup></td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType1a(self):
        '''e.g: Find the perimeter of the shaded circle enclosed in a square of side 5 cm.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius = randint(2,20)
        self.diameter = self.radius * 2
        self.unit = randint(1,2)
        self.FunctionCall = "DrawCircleSquare1("+str(self.diameter)+","+str(self.unit)+")"
        self.answer = round(2 * float(self.radius) * 3.14,2)
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"     
        self.problem = "Find the perimeter of the shaded circle below enclosed in a square of side "+str(self.diameter)+" "+self.unit+". Write your answer correct to 2 decimal places.<br><br>"
        self.problem = self.problem + "( Given, &pi; = 3.14 )"

        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1a(self.problem,self.answer,self.radius,self.diameter,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1a",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType1a(self,problem,answer,radius,diameter,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter or circumference of a circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Diameter</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>&pi;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Diameter of the shaded circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Side of the enclosing square</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit+"</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter of the shaded circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14 &times; "+str(diameter)+"</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType2(self):
        '''e.g: Find the area of the shaded circle enclosed in a square of area 25 cm2.'''
        self.complexity_level = "difficult"
        self.HCScore = 7
        self.radius = randint(2,20)
        self.diameter = self.radius * 2
        self.area = self.diameter * self.diameter
        self.unit = randint(1,2)
        self.FunctionCall = "DrawCircleSquare2("+str(self.diameter)+","+str(self.unit)+")"
        self.answer = round(float(self.radius*self.radius) * 22 / 7,2)
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.unit1 = self.unit
        self.unit = self.unit + "<sup>2</sup>"
        self.problem = "Find the area of the shaded circle below enclosed in a square of area "+str(self.area)+" "+self.unit+". Write your answer correct to 2 decimal places.<br>"
        self.problem = self.problem + "<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>( Given, &pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></font></tr></table>"
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.radius,self.diameter,self.area,self.unit,self.unit1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType2(self,problem,answer,radius,diameter,area,unit,unit1):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of a circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>22</u><br>&nbsp;7</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the square</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(area)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Side of the square</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&radic;"+str(area)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit1+"</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Diameter of the shaded circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Side of the square</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit1+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of the shaded circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Diameter &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit1+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+unit1+"</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Area of the shaded circle</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>22</u><br>7</td><td style='padding-left:0px; vertical-align:middle'>&nbsp;&times; "+str(radius)+" &times; " +str(radius)+"</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(answer)+" "+unit+"</td></tr></table>"
        
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType2a(self):
        '''e.g: Find the circumference of the shaded circle enclosed in a square of area 25 cm2.'''
        self.complexity_level = "difficult"
        self.HCScore = 7
        self.radius = randint(2,10)
        self.diameter = self.radius * 2
        self.area = self.diameter * self.diameter
        self.unit = randint(1,2)
        self.FunctionCall = "DrawCircleSquare2("+str(self.diameter)+","+str(self.unit)+")"
        self.answer = round(2 * 3.14 * float(self.radius),2)
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.unit1 = self.unit
        self.problem = "Find the circumference of the shaded circle below enclosed in a square of area "+str(self.area)+" "+self.unit+"<sup>2</sup>. Write your answer correct to 2 decimal places.<br><br>"
        self.problem = self.problem + "( Given, &pi; = 3.14 )"
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2a(self.problem,self.answer,self.radius,self.diameter,self.area,self.unit,self.unit1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2a",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType2a(self,problem,answer,radius,diameter,area,unit,unit1):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Circumference of a circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Diameter</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>&pi;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the square</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(area)+" "+unit+"<sup>2</sup></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Side of the square</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&radic;"+str(area)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit1+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Diameter of the shaded circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Side of the square</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit1+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;'>Circumference of the shaded circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14 &times; "+str(diameter)+"</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit1+"</td></tr></table>"
        
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain  
    
    def GenerateProblemType3(self):
        '''e.g: Find the area of the shaded figure comprises of 3 identical quadrants of radius 5 cm.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius = randint(2,20)
        self.diameter = self.radius * 2
        self.unit = randint(1,2)
        self.FunctionCall = "DrawThreeFourthCircle("+str(self.radius)+","+str(self.unit)+")"
        self.answer = round(float(self.radius*self.radius) * 22 * 3 /(7*4),2)
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.problem = "Find the area of the shaded figure below that comprises of a semicircle and a quadrant, each of radius "+str(self.radius)+" "+self.unit+". Round off your answer to two decimal places.<br>"
        self.problem = self.problem + "<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>( Given, &pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></font></tr></table>"
        radiusUnit = self.unit
        self.unit = self.unit + "<sup>2</sup>"
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.radius,self.diameter,self.unit,radiusUnit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType3(self,problem,answer,radius,diameter,areaUnit,radiusUnit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+areaUnit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Area of the semicircle + Area of the quadrant</td></tr></table>"    

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+radiusUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>22</u><br>&nbsp;7</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of a semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>Area of the circle &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>&pi; &times; Radius &times; Radius &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>22</u><br>7</td><td style='padding-left:0px; vertical-align:middle;text-align:left'>&nbsp;&times; "+str(radius)+" &times; " +str(radius)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(round(22*float(radius*radius)/14,2))+" "+areaUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of a quadrant</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>Area of the circle &divide; 4</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>&pi; &times; Radius &times; Radius &divide; 4</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-right:0px; padding-top:7px;'><u>22</u><br>7</td><td style='padding-left:0px; vertical-align:middle;text-align:left'>&nbsp;&times; "+str(radius)+" &times; " +str(radius)+" &divide; 4</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(round(22*float(radius*radius)/28,2))+" "+areaUnit+"</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(round(22*float(radius*radius)/14,2))+" + "+str(round(22*float(radius*radius)/28,2))+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(answer)+" "+areaUnit+"</td></tr></table>"
        
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType3a(self):
        '''e.g: Find the perimeter of the shaded figure comprises of 3 identical quadrants of radius 5 cm.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius = randint(2,20)
        self.diameter = self.radius * 2
        self.unit = randint(1,2)
        self.FunctionCall = "DrawThreeFourthCircle("+str(self.radius)+","+str(self.unit)+")"
        self.answer = round(3.14*float(self.radius)+2*float(self.radius)+3.14*float(self.radius)/2+2*float(self.radius),2)
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.problem = "Find the perimeter of the shaded figure that comprises of a semicircle and a quadrant, each of radius "+str(self.radius)+" "+self.unit+". Give your answer correct to the hundredths place.<br><br>"
        self.problem = self.problem + "( Given, &pi; = 3.14 )</font>"
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3a(self.problem,self.answer,self.radius,self.diameter,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3a",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType3a(self,problem,answer,radius,diameter,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Perimeter of the semicircle + Perimeter of the quadrant</td></tr></table>"    
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>&pi;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter of semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left;padding-right:0px' colspan='3'>Half the circumference of circle + ( 2 &times; Radius )</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>(</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>1</u><br>2</td><td style='text-align:left;vertical-align:middle;padding-left:0px'>&nbsp;&times; 2 &times; &pi; &times; Radius ) + ( 2 &times; Radius )</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>(&nbsp;</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>1</u><br>2</td><td style='text-align:left;padding-right:0px;padding-left:0px;vertical-align:middle'>&nbsp;&times; 2 &times; 3.14 &times; "+str(radius)+" ) + ( 2 &times; "+str(radius)+" )</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='3'>"+str(3.14*float(radius)+2*float(radius))+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter of quadrant</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left;padding-right:0px' colspan='3'>Quarter the circumference of circle + ( 2 &times; Radius )</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>(</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>1</u><br>4</td><td style='text-align:left;vertical-align:middle;padding-left:0px'>&nbsp;&times; 2 &times; &pi; &times; Radius ) + ( 2 &times; Radius )</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>(&nbsp;</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>1</u><br>4</td><td style='text-align:left;padding-right:0px;padding-left:0px;vertical-align:middle'>&nbsp;&times; 2 &times; 3.14 &times; "+str(radius)+" ) + ( 2 &times; "+str(radius)+" )</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='3'>"+str(3.14*float(radius)/2+2*float(radius))+" "+unit+"</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(3.14*float(radius)+2*float(radius))+" + "+str(3.14*float(radius)/2+2*float(radius))+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType4(self):
        '''e.g: Find the area of the shaded figure made up of 3 identical quadrants of radius 5 cm each.'''
        self.complexity_level = "difficult"
        self.HCScore = 7
        self.radius = randint(2,20)
        self.unit = randint(1,2)
        self.flag = randint(2,4)
        self.FunctionCall = "DrawQuadrants1("+str(self.radius)+","+str(self.unit)+","+str(self.flag)+")"
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.problem = "Find the area of the shaded figure below made up of "
        self.answer = 1
        if self.flag == 2:
            self.problem = self.problem + "2 identical quadrants of radius "+str(self.radius)+" "+self.unit+" each. Write your answer correct to two decimal places.<br>"
            self.answer = round(22*float(self.radius*self.radius)*2/28,2)
        if self.flag == 3:
            self.problem = self.problem + "3 identical quadrants of radius "+str(self.radius)+" "+self.unit+" each. Give your answer correct to two decimal places.<br>"
            self.answer = round(22*float(self.radius*self.radius)*3/28,2)            
        if self.flag == 4:
            self.problem = self.problem + "4 identical quadrants of radius "+str(self.radius)+" "+self.unit+" each. Write your answer correct to the hundredths place.<br>"
            self.answer = round(22*float(self.radius*self.radius)*4/28,2)            
        self.problem = self.problem + "<table><tr><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>( Given, &pi; =&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle; padding-top:11px'><u>22</u><br>7</td><td style='padding-left:0px;padding-right:0px; vertical-align:middle'>&nbsp;)</td></font></tr></table>"
        radiusUnit = self.unit
        self.unit = self.unit + "<sup>2</sup>"
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.radius,self.unit,radiusUnit,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType4(self,problem,answer,radius,unit,radiusUnit,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Area of "+str(flag)+" quadrants</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(flag)+" &times; area of 1 quadrant</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of a quadrant</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Area of the circle &divide; 4</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius &divide; 4</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+radiusUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>22</u><br>&nbsp;7</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>"+str(flag)+" &times;</td><td style='padding-top:7px;padding-left:0px;padding-right:0px; text-align:left'><u>22</u><br>&nbsp;7</td><td style='text-align:left;padding-left:0px;vertical-align:middle'>&nbsp;&times; "+str(radius)+" &times; "+str(radius)+" &divide; 4</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left' colspan='3'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType4a(self):
        '''e.g: Find the perimeter of the shaded figure made up of 3 identical quadrants of radius 5 cm each.'''
        self.complexity_level = "difficult"
        self.HCScore = 7
        self.radius = randint(2,20)
        self.unit = randint(1,2)
        self.flag = randint(2,4)
        self.FunctionCall = "DrawQuadrants1("+str(self.radius)+","+str(self.unit)+","+str(self.flag)+")"
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.answer = 1
        self.answer = round(self.flag*(3.14*float(self.radius)/2+2*float(self.radius)),2)
        self.problem = "The figure below is made up of "+str(self.flag)+" identical quadrants of radius "+str(self.radius)+" "+self.unit+" each. Find its perimeter correct to 2 decimal places.<br><br>"
        self.problem = self.problem + "(Given, &pi; = 3.14 )"
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4a(self.problem,self.answer,self.radius,self.unit,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4a",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType4a(self,problem,answer,radius,unit,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Perimeter of "+str(flag)+" quadrants</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(flag)+" &times; perimeter of 1 quadrant</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&pi;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>3.14</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter of a quadrant</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left;padding-right:0px' colspan='3'>Quarter the circumference of circle + ( 2 &times; Radius )</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>(</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>1</u><br>4</td><td style='text-align:left;vertical-align:middle;padding-left:0px'>&nbsp;&times; 2 &times; &pi; &times; Radius ) + ( 2 &times; Radius )</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>(</td><td style='padding-left:0px; padding-right:0px; padding-top:7px;'><u>1</u><br>4</td><td style='text-align:left;vertical-align:middle;padding-left:0px'>&nbsp;&times; 2 &times; 3.14 &times; "+str(radius)+" ) + ( 2 &times; "+str(radius)+" )</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='3'>"+str(2*3.14*float(radius)/4+2*float(radius))+" "+unit+"</td></tr></table>"
                
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>Perimeter of the shaded figure</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>"+str(flag)+" &times; "+str(2*3.14*float(radius)/4+2*float(radius))+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left' colspan='3'>"+str(answer)+" "+unit+"</td></tr></table>"
                                                
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType5(self):
        '''e.g: Find the area of the below shaded figure made up of a rectangle and two semicircles.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius1 = randint(2,10)
        self.radius2 = randint(2,6) + self.radius1
        self.unit = randint(1,2)

        self.FunctionCall = "DrawRectangleSemiCircles1("+str(self.radius1)+","+str(self.radius2)+","+str(self.unit)+")"
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.problem = "Find the area of the shaded figure below made up of a rectangle measuring "+str(2*self.radius1)+" "+self.unit+" by "+str(2*self.radius2)+" "+self.unit+" and two semicircles. Give your answer correct to two decimal places.<br><br>"
        self.problem = self.problem + "(Given, &pi; = 3.14)"
        radiusUnit = self.unit
        self.unit = self.unit + "<sup>2</sup>"
        self.answer = (self.radius1*self.radius2)*4 + round((3.14*float(self.radius1*self.radius1)/2),2) + round((3.14*float(self.radius2*self.radius2)/2),2)
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.radius1,self.radius2,self.unit,radiusUnit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType5(self,problem,answer,radius1,radius2,unit,radiusUnit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Area of the rectangle + Area of small semicircle + Area of big semicircle</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>&pi;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Breadth of rectangle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius1)+" "+radiusUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Length of rectangle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius2)+" "+radiusUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of small semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Breadth of rectangle &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius1)+" "+radiusUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of big semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length of rectangle &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius2)+" "+radiusUnit+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of rectangle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left;padding-right:0px'>Length &times; Breadth</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left;padding-right:0px'>"+str(2*radius2)+" &times; "+str(2*radius1)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left;padding-right:0px'>"+str(4*radius2*radius1)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of small semicircle</td><td style='padding-left:0px; padding-right:0px;vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>&pi; &times; Radius &times; Radius &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>3.14 &times; "+str(radius1)+" &times; "+str(radius1)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>"+str(round((3.14*float(self.radius1*self.radius1)/2),2))+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of big semicircle</td><td style='padding-left:0px; padding-right:0px;vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>&pi; &times; Radius &times; Radius &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>3.14 &times; "+str(radius2)+" &times; "+str(radius2)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:middle'>=</td><td style='text-align:left;vertical-align:middle;padding-right:0px'>"+str(round((3.14*float(self.radius2*self.radius2)/2),2))+" "+unit+"</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(4*radius2*radius1)+" + "+str(round((3.14*float(self.radius1*self.radius1)/2),2))+" + "+str(round((3.14*float(self.radius2*self.radius2)/2),2))+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemType5a(self):
        '''e.g: Find the perimeter of the below shaded figure made up of a rectangle and two semicircles.'''
        self.complexity_level = "difficult"
        self.HCScore = 7
        self.radius1 = randint(2,10)
        self.radius2 = randint(2,6) + self.radius1
        self.unit = randint(1,2)

        self.FunctionCall = "DrawRectangleSemiCircles1("+str(self.radius1)+","+str(self.radius2)+","+str(self.unit)+")"
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.problem = "Find the perimeter of the shaded figure below made up of a rectangle measuring "+str(2*self.radius1)+" "+self.unit+" by "+str(2*self.radius2)+" "+self.unit+" and two semicircles. Give your answer correct to two decimal places.<br><br>"
        self.problem = self.problem + "(Given, &pi; = 3.14)"
        
        self.answer = (self.radius1+self.radius2)*2 + round(3.14*float(self.radius1),2) + round(3.14*float(self.radius2),2)
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5a(self.problem,self.answer,self.radius1,self.radius2,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5a",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType5a(self,problem,answer,radius1,radius2,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length of rectangle + Breadth of rectangle + Half the circumference of small circle + Half the circumference of big circle</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length of rectangle + Breadth of rectangle + (&pi; &times; Radius of small semicircle) + (&pi; &times; Radius of big semicircle)</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>&pi;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Breadth of rectangle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius1)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Length of rectangle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius2)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of small semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Breadth of rectangle &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius1)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of big semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length of rectangle &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius2)+" "+unit+"</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>Perimeter of the shaded figure</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(2*radius2)+" + "+str(2*radius1)+" + (3.14 &times; "+str(radius1)+") + (3.14 &times; "+str(radius2)+")</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(2*radius2)+" + "+str(2*radius1)+" + "+str(3.14*float(radius1))+" + "+str(3.14*float(radius2))+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType6(self):
        '''e.g: Find the area of the below shaded figure made up of a triangle and two semicircles.'''
        self.complexity_level = "difficult"
        self.HCScore = 7
        self.radius1 = randint(2,10)
        self.radius2 = randint(2,6) + self.radius1
        self.unit = randint(1,2)

        self.FunctionCall = "DrawTriangleSemiCircles1("+str(self.radius1)+","+str(self.radius2)+","+str(self.unit)+")"
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.problem = "Find the area of the shaded figure below made up of a triangle and two semicircles. Give your answer correct to the hundredths place.<br><br>"
        self.problem = self.problem + "(Given, height of the triangle = "+str(2*self.radius1)+" "+self.unit+", base of the triangle = "+str(2*self.radius2)+" "+self.unit+", and &pi; = 3.14)</font>"
        radiusUnit = self.unit
        self.unit = self.unit + "<sup>2</sup>"
        self.answer = (self.radius1*self.radius2*4)/2 + round((3.14*float(self.radius1*self.radius1)/2),2) + round((3.14*float(self.radius2*self.radius2)/2),2)
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.radius1,self.radius2,self.unit,radiusUnit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType6(self,problem,answer,radius1,radius2,unit,radiusUnit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Area of triangle + Area of small semicircle + Area of big semicircle</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>&pi;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Height of triangle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius1)+" "+radiusUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Base of triangle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius2)+" "+radiusUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of small semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Height of triangle &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius1)+" "+radiusUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of big semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Base of triangle &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius2)+" "+radiusUnit+"</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of triangle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Base &times; Height &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius2*2)+" &times; "+str(radius1*2)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius1*radius2*4/2)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of small semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14 &times; "+str(radius1)+" &times; "+str(radius1)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(round((3.14*float(radius1*radius1)/2),2))+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of big semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14 &times; "+str(radius2)+" &times; "+str(radius2)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(round((3.14*float(radius2*radius2)/2),2))+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(radius1*radius2*4/2)+" + "+str(round((3.14*float(radius1*radius1)/2),2))+" + "+str(round((3.14*float(radius2*radius2)/2),2))+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7(self):
        '''e.g: Find the area of the below shaded figure made up of two semicircles.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.radius1 = randint(2,10)
        self.diff = randint(0,5)
        self.radius2 = randint(2,6) + self.radius1 + self.diff
        
        self.unit = randint(1,2)

        self.FunctionCall = "DrawTwoSemiCircles1("+str(self.radius1)+","+str(self.radius2)+","+str(self.diff)+","+str(self.unit)+")"
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.problem = "What is the area of the shaded figure below made up of two semicircles? Give your answer correct to 2 decimal places.<br><br>"
        self.problem = self.problem + "(Given, diameter of big semicircle = "+str(2*self.radius2)+" "+self.unit+", diameter of small semicircle = "+str(2*self.radius1)+" "+self.unit+", and &pi; = 3.14)"
        radiusUnit = self.unit
        self.unit = self.unit + "<sup>2</sup>"
        self.answer = round((3.14*float(self.radius2*self.radius2)/2),2) - round((3.14*float(self.radius1*self.radius1)/2),2)
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.radius1,self.radius2,self.unit,radiusUnit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType7(self,problem,answer,radius1,radius2,unit,radiusUnit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Area of big semicircle &minus; Area of small semicircle</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>&pi;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of big semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius2)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius2)+" "+radiusUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of small semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius1)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius1)+" "+radiusUnit+"</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of big semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14 &times; "+str(radius2)+" &times; "+str(radius2)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(round((3.14*float(radius2*radius2)/2),2))+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of small semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14 &times; "+str(radius1)+" &times; "+str(radius1)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(round((3.14*float(radius1*radius1)/2),2))+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(round((3.14*float(radius2*radius2)/2),2))+" &minus; "+str(round((3.14*float(radius1*radius1)/2),2))+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8(self):
        '''e.g: Find the area of the below shaded figure made up of two semicircles.'''
        self.complexity_level = "difficult"
        self.HCScore = 7
        
        self.radius1 = randint(7,15)
        self.diff = randint(0,5)
        self.radius2 = randint(2,6) + self.radius1 + self.diff

        self.unit = randint(1,2)

        self.FunctionCall = "DrawTwoSemiCircles2("+str(self.radius1)+","+str(self.radius2)+","+str(self.diff)+","+str(self.unit)+")"
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.problem = "Find the area of the following shaded figure made up of two semicircles. Write your answer correct to the hundredths place.<br><br>"
        self.problem = self.problem + "(Given, &pi; = 3.14)"
        radiusUnit = self.unit
        self.unit = self.unit + "<sup>2</sup>"
        self.answer = round((3.14*float(self.radius2*self.radius2)/2),2) - round((3.14*float(self.radius1*self.radius1)/2),2)
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.radius1,self.radius2,self.diff,self.unit,radiusUnit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType8(self,problem,answer,radius1,radius2,diff,unit,radiusUnit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Area of big semicircle &minus; Area of small semicircle</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>&pi;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of big semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>("+str(radius2-diff-radius1)+" + "+str(2*radius1)+" + "+str(radius2+diff-radius1)+") &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius2)+" "+radiusUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of small semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius1)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius1)+" "+radiusUnit+"</td></tr></table>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of big semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14 &times; "+str(radius2)+" &times; "+str(radius2)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(round((3.14*float(radius2*radius2)/2),2))+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of small semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14 &times; "+str(radius1)+" &times; "+str(radius1)+" &divide; 2</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(round((3.14*float(radius1*radius1)/2),2))+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(round((3.14*float(radius2*radius2)/2),2))+" &minus; "+str(round((3.14*float(radius1*radius1)/2),2))+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType9(self):
        '''e.g: Find the area of the below shaded figure made up of two quadrant and a square.'''
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.radius1 = randint(7,15)

        self.unit = randint(1,2)

        self.FunctionCall = "DrawTwoSemiCirclesSquare1("+str(self.radius1)+","+str(self.unit)+")"
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.problem = "Find the area of the shaded figure below made up of two quadrants and a square. Write your answer correct to two decimal places.<br><br>"
        self.problem = self.problem + "(Given, &pi; = 3.14)"
        radiusUnit = self.unit
        self.unit = self.unit + "<sup>2</sup>"
        self.answer = round(2*(self.radius1*self.radius1 - 3.14*float(self.radius1*self.radius1)/4),2) 
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.radius1,self.unit,radiusUnit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType9",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType9(self,problem,answer,radius1,unit,radiusUnit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>2 &times; (Area of smaller square &minus; Area of quadrant)</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>&pi;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Side of smaller square</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius1)+" "+radiusUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of quadrant</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Side of smaller square</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius1)+" "+radiusUnit+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of smaller square</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Side &times; Side</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius1)+" &times; "+str(radius1)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius1*radius1)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of quadrant</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius &divide; 4</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14 &times; "+str(radius1)+" &times; "+str(radius1)+" &divide; 4</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(3.14*float(self.radius1*self.radius1)/4)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>2 &times; ("+str(radius1*radius1)+" &minus; "+str(3.14*float(self.radius1*self.radius1)/4)+")</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType9a(self):
        '''e.g: Find the perimeter of the below shaded figure made up of two quadrant and a square.'''
        self.complexity_level = "difficult"
        self.HCScore = 7
        
        self.radius1 = randint(7,15)

        self.unit = randint(1,2)

        self.FunctionCall = "DrawTwoSemiCirclesSquare1("+str(self.radius1)+","+str(self.unit)+")"
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.problem = "Find the perimeter of the shaded figure made up of two quadrants and a square. Write your answer correct to two decimal places.<br><br>"
        self.problem = self.problem + "(Given, &pi; = 3.14)"

        self.answer = round(2*(2*self.radius1 + 2*3.14*float(self.radius1)/4),2) 
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9a(self.problem,self.answer,self.radius1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType9a",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType9a(self,problem,answer,radius1,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>2 &times; (sum of 2 sides of "+str(radius1)+" "+unit+" each + quarter the circumference of circle of radius "+str(radius1)+" "+unit+")</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Circumference of circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>2 &times; &pi; &times; Radius</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>2 &times; 3.14 &times; "+str(radius1)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*3.14*float(self.radius1))+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Quarter the circumference</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*3.14*float(self.radius1))+" &divide; 4</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*3.14*float(self.radius1)/4)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>Perimeter of the shaded figure</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>2 &times; ("+str(radius1)+" + "+str(radius1)+" + "+str(2*3.14*float(self.radius1)/4)+")</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType10(self):
        '''e.g: Find the area of the below shaded figure made up of two quadrant and a square.'''
        self.complexity_level = "difficult"
        self.HCScore = 7
        
        self.radius1 = randint(7,15)

        self.unit = randint(1,2)

        self.FunctionCall = "DrawTwoSemiCirclesSquare2("+str(self.radius1)+","+str(self.unit)+")"
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.problem = "Find the area of the shaded figure made up of two quadrants and a square. Write your answer correct to two decimal places.<br><br>"
        self.problem = self.problem + "(Given, &pi; = 3.14)"
        radiusUnit= self.unit
        self.unit = self.unit + "<sup>2</sup>"
        self.side = 2 * self.radius1
        self.answer = round(3.14*float(self.side*self.side)/2 - float(self.side*self.side),2) 
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.radius1,self.unit,radiusUnit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType10",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType10(self,problem,answer,radius1,unit,radiusUnit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Area of the square &minus; Area of the unshaded figure</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of half the unshaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Area of the square &minus; Area of 1 quadrant</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>&pi;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Side of square</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius1)+" "+radiusUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of quadrant</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Side of square</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius1)+" "+radiusUnit+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of square</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Side &times; Side</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius1)+" &times; "+str(2*radius1)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(4*radius1*radius1)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of quadrant</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&pi; &times; Radius &times; Radius &divide; 4</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14 &times; "+str(2*radius1)+" &times; "+str(2*radius1)+" &divide; 4</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(3.14*float(radius1*radius1*4)/4)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of the unshaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>2 &times; ("+str(4*radius1*radius1)+" &minus;"+str(3.14*float(radius1*radius1*4)/4)+")</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*(radius1*radius1*4-3.14*float(radius1*radius1*4)/4))+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>Area of the shaded figure</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(4*radius1*radius1)+" &minus; "+str(2*(radius1*radius1*4-3.14*float(radius1*radius1*4)/4))+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType10a(self):
        '''e.g: Find the perimeter of the below shaded figure made up of two quadrant and a square.'''
        self.complexity_level = "difficult"
        self.HCScore = 7
        
        self.radius1 = randint(7,15)

        self.unit = randint(1,2)

        self.FunctionCall = "DrawTwoSemiCirclesSquare2("+str(self.radius1)+","+str(self.unit)+")"
        if self.unit == 1:
            self.unit = "cm"
        else:
            self.unit = "m"
        self.problem = "Find the perimeter of the shaded figure made up of two quadrants and a square. Give your answer correct to the hundredths place.<br><br>"
        self.problem = self.problem + "(Given, &pi; = 3.14)"
        self.side = 2 * self.radius1
        self.answer = round(2*2*3.14*float(self.side)/4,2) 
        
        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10a(self.problem,self.answer,self.radius1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType10a",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType10a(self,problem,answer,radius1,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "Perimeter of the shaded figure = 2 &times; quarter the perimeter of a circle<br><br>"  
        self.solution_text = self.solution_text + "side of the square = radius of the circle = "+str(2*radius1)+"<br><br>"
        self.solution_text = self.solution_text + "quarter the perimeter of a circle = 2 &times; 3.14 &times; "+str(2*radius1)+" &divide; 4 = "+str(2*3.14*float(self.radius1*2)/4)+"<br><br>"
        self.solution_text = self.solution_text + "Therefore, perimeter of the shaded figure = 2 &times; "+str(2*3.14*float(self.radius1*2)/4)+" = "+str(answer)+" "+unit+"<br><br>"

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>From the figure,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Perimeter of the shaded figure</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>2 &times; Perimeter contributed by one quadrant</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>2 &times; Quarter the circumference of the circle</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>&pi;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>3.14</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of quadrant</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Side of square</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*radius1)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Circumference of the circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>2 &times; &pi; &times; Radius</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>2 &times; 3.14 &times; "+str(2*radius1)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*3.14*float(radius1*2))+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Quarter the circumference</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*3.14*float(radius1*2))+" &divide; 4</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(2*3.14*float(radius1*2)/4)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>Perimeter of the shaded figure</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>2 &times; "+str(2*3.14*float(radius1*2)/4)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckType):
        if CheckType==1:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False               