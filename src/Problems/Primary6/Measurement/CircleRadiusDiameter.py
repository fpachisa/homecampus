'''
Created on Oct 25, 2011

Module: CircleRadiusDiameter
Generates "Radius diameter relationship of a circle" problems for Primary 6

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

class CircleRadiusDiameter:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"easy":[self.GenerateProblemType1(),self.GenerateProblemType2(),
                                    self.GenerateProblemType3(),self.GenerateProblemType4(),],
                            }
        try:
            return random.choice(self.ProblemType[level])
        except KeyError:
            return random.choice(random.choice(self.ProblemType.values()))
        #return self.GenerateProblemType1()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            3:["ProblemType3",],
                            4:["ProblemType4",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],
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
        #return self.GenerateProblemType4()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g: What is the radius of the below circle?'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.diameter = random.randrange(2,30,2)
        self.unit = randint(1,2)
        self.FunctionCall = "DrawCircle1("+str(self.diameter)+","+str(self.unit)+")"
        self.answer = self.diameter / 2
        if self.unit == 1:
            self.unit = "cm"
            self.problem1 = random.choice(PersonName.GirlName) +" bent a piece of wire into a circle as shown below. What is the radius of the circle?<br><br>"+"(Diameter = "+str(self.diameter)+" "+self.unit+")"
            self.problem2 = random.choice(PersonName.GirlName) +" formed a circle as shown below with a piece of string. Find the radius of the circle formed.<br><br>"+"(Diameter = "+str(self.diameter)+" "+self.unit+")"
            self.problem3 = random.choice(PersonName.GirlName) +" cut a piece of paper into a disc as shown below. Find the radius of the disc.<br><br>"+"(Diameter = "+str(self.diameter)+" "+self.unit+")"
            self.problem4 = "A round plate has a diameter of "+str(self.diameter)+" "+self.unit+". Find the radius of the plate."
            self.problem5 = "The diameter of a circular mirror is "+str(self.diameter)+" "+self.unit+". Find the radius of the mirror."
        else:
            self.unit = "m"
            self.problem1 = random.choice(PersonName.BoyName) +" is using a circular piece of land as shown below to build a garden. What is the radius of the garden?<br><br>"+"(Diameter = "+str(self.diameter)+" "+self.unit+")"
            self.problem2 = "A circular pool of water has a diameter of "+str(self.diameter)+" "+self.unit+". What is the radius of the pool?"
            self.problem3 = "A round mirror has a diameter of "+str(self.diameter)+" "+self.unit+". Find the radius of the mirror."
            self.problem4 = "The diameter of a circular sheet of tin is "+str(self.diameter)+" "+self.unit+". Find its radius."
            self.problem5 = "A round stage has a diameter of "+str(self.diameter)+" "+self.unit+". What is the radius of the stage?"

        self.problem6 = "What is the radius of the circle below?<br><br>"+"(Diameter = "+str(self.diameter)+" "+self.unit+")"
        self.problem7 = "Find the radius of the circle below.<br><br>"+"(Diameter = "+str(self.diameter)+" "+self.unit+")"
        self.problem8 = "The diameter of a circle is "+str(self.diameter)+" "+self.unit+". What is its radius?"
        self.problem9 = "A circle has a diameter of "+str(self.diameter)+" "+self.unit+". Find the radius of the circle."
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6,self.problem7,self.problem8,self.problem9])

        self.template = "DrawCircles.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.diameter,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType1(self,problem,answer,diameter,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Diameter of the circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Diameter &divide; 2</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Radius</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(diameter)+" " +unit+" &divide; 2</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Radius-and-Diameter-of-Circle" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):
        '''e.g: What is the diameter of the circle below?'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.radius = randint(2,20)
        self.unit = randint(1,2)
        self.FunctionCall = "DrawCircle2("+str(self.radius)+","+str(self.unit)+")"
        self.answer = self.radius * 2
        if self.unit == 1:
            self.unit = "cm"
            self.problem1 = random.choice(PersonName.GirlName) +" bent a piece of wire into a circle as shown below. What is the diameter of the circle?<br><br>"+"(Radius = "+str(self.radius)+" "+self.unit+")"
            self.problem2 = random.choice(PersonName.GirlName) +" formed a circle as shown below with a piece of string. Find the diameter of the circle formed.<br><br>"+"(Radius = "+str(self.radius)+" "+self.unit+")"
            self.problem3 = random.choice(PersonName.GirlName) +" cut a piece of paper into a disc as shown below. Find the diameter of the disc.<br><br>"+"(Radius = "+str(self.radius)+" "+self.unit+")"
            self.problem4 = "A round plate has a radius of "+str(self.radius)+" "+self.unit+". Find the diameter of the plate."
            self.problem5 = "The radius of a circular mirror is "+str(self.radius)+" "+self.unit+". Find the diameter of the mirror."
        else:
            self.unit = "m"
            self.problem1 = random.choice(PersonName.BoyName) +" is using a circular piece of land as shown below to build a garden. What is the diameter of the garden?<br><br>"+"(Radius = "+str(self.radius)+" "+self.unit+")"
            self.problem2 = "A circular pool of water has a radius of "+str(self.radius)+" "+self.unit+". What is the diameter of the pool?"
            self.problem3 = "A round mirror has a radius of "+str(self.radius)+" "+self.unit+". Find the diameter of the mirror."
            self.problem4 = "The radius of a circular sheet of tin is "+str(self.radius)+" "+self.unit+". Find its diameter."
            self.problem5 = "A round stage has a radius of "+str(self.radius)+" "+self.unit+". What is the diameter of the stage?"
        self.problem6 = "What is the diameter of the circle below?<br><br>"+"(Radius = "+str(self.radius)+" "+self.unit+")"
        self.problem7 = "Find the diameter of the circle below.<br><br>"+"(Radius = "+str(self.radius)+" "+self.unit+")"
        self.problem8 = "The radius of a circle is "+str(self.radius)+" "+self.unit+". What is its diameter?"
        self.problem9 = "A circle has a radius of "+str(self.radius)+" "+self.unit+". Find the diameter of the circle."
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6,self.problem7,self.problem8,self.problem9])
        
        self.template = "DrawCircles.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.radius,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType2(self,problem,answer,radius,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of the circle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Diameter</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Radius &times; 2</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Diameter</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(radius)+" " +unit+" &times; 2</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Radius-and-Diameter-of-Circle" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):
        '''e.g: What is the radius of the below semicircle?'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.diameter = random.randrange(2,30,2)
        self.unit = randint(1,2)
        self.FunctionCall = "DrawSemiCircle1("+str(self.diameter)+","+str(self.unit)+")"
        self.answer = self.diameter / 2
        if self.unit == 1:
            self.unit = "cm"
            self.problem1 = random.choice(PersonName.GirlName) +" bent a piece of wire into a semicircle as shown below. What is the radius of the semicircle?<br><br>"+"(Diameter = "+str(self.diameter)+" "+self.unit+")"
            self.problem2 = random.choice(PersonName.GirlName) +" formed a semicircle as shown below with a piece of string. Find the radius of the semicircle formed.<br><br>"+"(Diameter = "+str(self.diameter)+" "+self.unit+")"
            self.problem3 = random.choice(PersonName.GirlName) +" cut a piece of paper into a semicircular disc as shown below. Find the radius of the disc.<br><br>"+"(Diameter = "+str(self.diameter)+" "+self.unit+")"
            self.problem4 = "A semicircular plate has a diameter of "+str(self.diameter)+" "+self.unit+". Find the radius of the plate."
            self.problem5 = "The diameter of a semicircular mirror is "+str(self.diameter)+" "+self.unit+". Find the radius of the mirror."
        else:
            self.unit = "m"
            self.problem1 = random.choice(PersonName.BoyName) +" is using a semicircular piece of land as shown below to build a garden. What is the radius of the garden?<br><br>"+"(Diameter = "+str(self.diameter)+" "+self.unit+")"
            self.problem2 = "A semicircular pool of water has a diameter of "+str(self.diameter)+" "+self.unit+". What is the radius of the pool?"
            self.problem3 = "A mirror shaped like a semicircle has a diameter of "+str(self.diameter)+" "+self.unit+". Find the radius of the mirror."
            self.problem4 = "The diameter of a semicircular sheet of tin is "+str(self.diameter)+" "+self.unit+". Find its radius."
            self.problem5 = "A stage shaped like a semicircle has a diameter of "+str(self.diameter)+" "+self.unit+". What is the radius of the stage?"
        self.problem6 = "What is the radius of the semicircle below?<br><br>"+"(Diameter = "+str(self.diameter)+" "+self.unit+")"
        self.problem7 = "Find the radius of the semicircle below.<br><br>"+"(Diameter = "+str(self.diameter)+" "+self.unit+")"
        self.problem8 = "The diameter of a semicircle is "+str(self.diameter)+" "+self.unit+". What is its radius?"
        self.problem9 = "A semicircle has a diameter of "+str(self.diameter)+" "+self.unit+". Find the radius of the circle."
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6,self.problem7,self.problem8,self.problem9])
        
        self.template = "DrawCircles.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.diameter,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType3(self,problem,answer,diameter,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Diameter of the semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(diameter)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Diameter &divide; 2</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Radius</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(diameter)+" " +unit+" &divide; 2</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Radius-and-Diameter-of-Circle" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4(self):
        '''e.g: What is the diameter of the semicircle below?'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.radius = randint(2,20)
        self.unit = randint(1,2)
        self.FunctionCall = "DrawSemiCircle2("+str(self.radius)+","+str(self.unit)+")"
        self.answer = self.radius * 2
        if self.unit == 1:
            self.unit = "cm"
            self.problem1 = random.choice(PersonName.GirlName) +" bent a piece of wire into a semicircle as shown below. What is the diameter of the semicircle?<br><br>"+"(Radius = "+str(self.radius)+" "+self.unit+")"
            self.problem2 = random.choice(PersonName.GirlName) +" formed a semicircle as shown below with a piece of string. Find the diameter of the semicircle formed.<br><br>"+"(Radius = "+str(self.radius)+" "+self.unit+")"
            self.problem3 = random.choice(PersonName.GirlName) +" cut a piece of paper into a semicircular disc as shown below. Find the diameter of the disc.<br><br>"+"(Radius = "+str(self.radius)+" "+self.unit+")"
            self.problem4 = "A semicircular plate has a radius of "+str(self.radius)+" "+self.unit+". Find the diameter of the plate."
            self.problem5 = "The radius of a semicircular mirror is "+str(self.radius)+" "+self.unit+". Find the diameter of the mirror."
        else:
            self.unit = "m"
            self.problem1 = random.choice(PersonName.BoyName) +" is using a semicircular piece of land as shown below to build a garden. What is the diameter of the garden?<br><br>"+"(Radius = "+str(self.radius)+" "+self.unit+")"
            self.problem2 = "A semicircular pool of water has a radius of "+str(self.radius)+" "+self.unit+". What is the diameter of the pool?"
            self.problem3 = "A mirror shaped like a semicircle has a radius of "+str(self.radius)+" "+self.unit+". Find the diameter of the mirror."
            self.problem4 = "The radius of a semicircular sheet of tin is "+str(self.radius)+" "+self.unit+". Find its diameter."
            self.problem5 = "A stage shaped like a semicircle has a radius of "+str(self.radius)+" "+self.unit+". What is the diameter of the stage?"
        self.problem6 = "What is the diameter of the semicircle below?<br><br>"+"(Radius = "+str(self.radius)+" "+self.unit+")"
        self.problem7 = "Find the diameter of the semicircle below.<br><br>"+"(Radius = "+str(self.radius)+" "+self.unit+")"
        self.problem8 = "The radius of a semicircle is "+str(self.radius)+" "+self.unit+". What is its diameter?"
        self.problem9 = "A semicircle has a radius of "+str(self.radius)+" "+self.unit+". Find the diameter of the circle."
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6,self.problem7,self.problem8,self.problem9])
        
        self.template = "DrawCircles.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.radius,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType4(self,problem,answer,radius,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Radius of the semicircle</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(radius)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Diameter</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Radius &times; 2</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Diameter</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>"+str(radius)+" " +unit+" &times; 2</td></tr>"    
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Radius-and-Diameter-of-Circle" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
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