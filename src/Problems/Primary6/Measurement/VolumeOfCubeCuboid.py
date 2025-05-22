'''
Created on Nov 15, 2011

Module: VolumeOfCubeCuboid
Generates "Finding volume/side of a cuboid or a cube" problems for Primary 6

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

class VolumeOfCubeCuboid:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"easy":[self.GenerateProblemType1(),self.GenerateProblemType3(),],
                            "medium":[self.GenerateProblemType2(),],
                            }
        try:
            return random.choice(self.ProblemType[level])
        except KeyError:
            return random.choice(random.choice(self.ProblemType.values()))
        #return self.GenerateProblemType7()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''                
        self.ProblemType = {1:"ProblemType1",2:"ProblemType2",3:"ProblemType3"}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemType2(),3:self.GenerateProblemType3()
                                    }
                      
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
        '''e.g: The volume of a cuboid is 150 cm<sup>3</sup>. The height is 10cm and length is 5cm. Find its breadth.'''
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.height = randint(2,10)
        self.length = randint(2,10)
        self.breadth = randint(2,10)
        
        if self.length==self.breadth:
            self.length = self.length + 1
            
        self.volume = self.length * self.breadth * self.height
        self.ProblemSelector = randint(1,4)
        if self.ProblemSelector == 1:
            self.problem1 = "A cuboid has a volume of %d cm<sup>3</sup>. It has a height of %d cm and a length of %d cm. What is its breadth?"%(self.volume,self.height,self.length)
            self.problem2 = random.choice(PersonName.BoyName)+" made a rectangular box that was %d cm high and %d cm long. Find the breadth of the box if its volume was %d cm<sup>3</sup>."%(self.height,self.length,self.volume)
            self.problem3 = random.choice(PersonName.GirlName)+" has a jewelry box that is %d cm long and %d cm high. How broad is the rectangular jewelry box if its volume is %d cm<sup>3</sup>?"%(self.length,self.height,self.volume) 
            self.problem4 = "A rectangular block of wood has a length of %d cm and a height of %d cm. If the block has a volume of %d cm<sup>3</sup>, find its breadth."%(self.length,self.height,self.volume)
            self.problem5 = "A rectangular glass container is %d cm long and %d cm high. What is the breadth of the container if its volume is %d cm<sup>3</sup>?"%(self.length,self.height,self.volume)
            self.answer = self.breadth
            self.flag = 1
        elif self.ProblemSelector == 2:
            self.problem1 = "The volume of a cuboid is %d cm<sup>3</sup>. It is %d cm high and %d cm wide. How long is the cuboid?"%(self.volume,self.height,self.breadth)
            self.problem2 = random.choice(PersonName.BoyName)+" made a rectangular box that was %d cm high and %d cm wide. What is the length of the box if its volume was %d cm<sup>3</sup>?"%(self.height,self.breadth,self.volume)
            self.problem3 = random.choice(PersonName.GirlName)+" has a jewelry box that is %d cm wide and %d cm high. Find the length of the rectangular jewelry box if its volume is %d cm<sup>3</sup>."%(self.breadth,self.height,self.volume)
            self.problem4 = random.choice(PersonName.BoyName)+" is polishing a rectangular block of wood that is %d cm wide and %d cm high. What is the length of the block of wood if its volume is %d cm<sup>3</sup>."%(self.breadth,self.height,self.volume)
            self.problem5 = "The volume of a rectangular plastic container is %d cm<sup>3</sup>. How long is the container if it is %d cm wide and %d cm high?"%(self.volume,self.breadth,self.height)
            self.answer = self.length
            self.flag = 2
        elif self.ProblemSelector == 3:
            self.problem1 = "The volume of a cuboid is %d cm<sup>3</sup>. Its breadth is %d cm and length is %d cm. Find its height."%(self.volume,self.breadth,self.length)
            self.problem2 = random.choice(PersonName.BoyName)+" made a rectangular box that was %d cm wide and %d cm long. How high was the box if its volume was %d cm<sup>3</sup>?"%(self.breadth,self.length,self.volume)
            self.problem3 = random.choice(PersonName.GirlName)+" has a jewelry box that is %d cm long and %d cm wide. What is the height of the rectangular jewelry box if its volume is %d cm<sup>3</sup>?"%(self.length,self.breadth,self.volume)
            self.problem4 = random.choice(PersonName.GirlName)+" has a rectangular block of wood that has a length of %d cm and a width of %d cm. Find the height of the block if it has a volume of %d cm<sup>3</sup>."%(self.length,self.breadth,self.volume)
            self.problem5 = "The volume of a rectangular steel container is %d cm<sup>3</sup>. Find the height of the container if its width is %d cm and its length is %d cm."%(self.volume,self.breadth,self.length)
            self.answer = self.height
            self.flag = 3
        else:
            self.breadth = self.length
            self.height = self.length
            self.volume = self.length * self.length * self.length
            self.problem1 = "The volume of a cube is %d cm<sup>3</sup>. What is the length of one edge of the cube?"%(self.volume)
            self.problem2 = random.choice(PersonName.BoyName)+" made a cube. Find the length of one side of the cube if the volume of the cube is %d cm<sup>3</sup>."%(self.volume)
            self.problem3 = random.choice(PersonName.GirlName)+" has a jewelry box that is shaped like a cube. How long is one edge of the jewelry box if its volume is %d cm<sup>3</sup>?"%(self.volume) 
            self.problem4 = "A cubical block of wood has a volume of %d cm<sup>3</sup>. Find the length of the side of the base of the cube."%(self.volume)
            self.problem5 = "The volume of a cubical plastic container is %d cm<sup>3</sup>. Find the length of one side of the container."%(self.volume)        
            self.answer = self.length
            self.flag = 4

        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])
        self.unit = "cm"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.length,self.breadth,self.height,self.volume,self.flag,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}

    def ExplainType1(self,problem,answer,length,breadth,height,volume,flag,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        if flag == 1:
            self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a cuboid</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length &times; Breadth &times; Height</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>So, Breadth</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Volume&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;Length &times; Height</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(volume)+" "+unit+"<sup>3</sup></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Length</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(length)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Height</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(height)+" "+unit+"</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Breadth</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:center'><u>&nbsp;&nbsp;&nbsp;"+str(volume)+"&nbsp;&nbsp;&nbsp;</u><br>"+str(length)+" &times; "+str(height)+"</td></tr>"    
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 2:
            self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a cuboid</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length &times; Breadth &times; Height</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>So, Length</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Volume&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;Breadth &times; Height</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(volume)+" "+unit+"<sup>3</sup></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Breadth</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(breadth)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Height</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(height)+" "+unit+"</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Length</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:center'><u>&nbsp;&nbsp;&nbsp;"+str(volume)+"&nbsp;&nbsp;&nbsp;</u><br>"+str(breadth)+" &times; "+str(height)+"</td></tr>"    
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 3:
            self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a cuboid</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length &times; Breadth &times; Height</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>So, Height</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Volume&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;Length &times; Breadth</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(volume)+" "+unit+"<sup>3</sup></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Length</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(length)+" "+unit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Breadth</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(breadth)+" "+unit+"</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Height</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:center'><u>&nbsp;&nbsp;&nbsp;"+str(volume)+"&nbsp;&nbsp;&nbsp;</u><br>"+str(length)+" &times; "+str(breadth)+"</td></tr>"    
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 4:
            self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a cube</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length &times; Length &times; Length</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>So, Length</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left'>&#8731;Volume</td></tr></table>"
        
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(volume)+" "+unit+"<sup>3</sup></td></tr></table>"
        
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Length of one edge of the cube</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left'>&#8731;"+str(volume)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
            
    def GenerateProblemType2(self):
        '''e.g: The volume of a cuboid is 150 cm<sup>3</sup> and its base area is 15 cm<sup>2</sup>. Find the height of the cuboid.'''
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.height = randint(2,10)
        self.length = randint(2,10)
        self.breadth = randint(2,10)
        
        if self.length==self.breadth:
            self.length = self.length + 1
            
        self.volume = self.length * self.breadth * self.height
        self.area = self.length * self.breadth
        
        self.ProblemSelector = randint(1,3)
        if self.ProblemSelector == 1:
            self.area = self.length * self.height
            self.problem1 = "A cuboid has a volume of %d cm<sup>3</sup>. Its face made up of the height and the length has an area of %d cm<sup>2</sup>. What is the breadth of the cuboid?"%(self.volume,self.area)
            self.problem2 = random.choice(PersonName.BoyName)+" made a rectangular box. Its face made up of the length and the height has an area of %d cm<sup>2</sup>. Find the breadth of the box if its volume is %d cm<sup>3</sup>."%(self.area,self.volume)
            self.problem3 = random.choice(PersonName.GirlName)+" has a rectangular jewelry box that has a volume of %d cm<sup>3</sup>. How broad is the jewelry box if the area of its face made up of the length and the height is %d cm<sup>2</sup>?"%(self.volume,self.area) 
            self.problem4 = "A rectangular block of wood has a volume of %d cm<sup>3</sup>. Find the breadth of the block if its face made up of the length and the height has an area of %d cm<sup>2</sup>."%(self.volume,self.area)
            self.problem5 = "A glass container has a volume of %d cm<sup>3</sup>. What is the breadth of the rectangular container if the face of the container made up of the length and the height has an area of %d cm<sup>2</sup>?"%(self.volume,self.area)
            self.answer = self.breadth
            self.flag = 1
        elif self.ProblemSelector == 2:
            self.area = self.breadth * self.height
            self.problem1 = "The volume of a cuboid is %d cm<sup>3</sup>. Its face made up of the breadth and the height has an area of %d cm<sup>2</sup>. What is the length of the cuboid?"%(self.volume,self.area)
            self.problem2 = random.choice(PersonName.BoyName)+" builds a rectangular box that has a volume of %d cm<sup>3</sup>. What is the length of the box if its face made up of the height and the breadth has an area of %d cm<sup>2</sup>?"%(self.volume,self.area)
            self.problem3 = random.choice(PersonName.GirlName)+" has a rectangular jewelry box that has a volume of %d cm<sup>3</sup>. Find the length of the jewelry box if the area of its face made up of the breadth and the height is %d cm<sup>2</sup>."%(self.volume,self.area)
            self.problem4 = random.choice(PersonName.BoyName)+" is polishing a rectangular block of wood. What is the length of the block of wood if its volume is %d cm<sup>3</sup> and the area of its face made up of the height and the breadth is %d cm<sup>2</sup>?"%(self.volume,self.area)
            self.problem5 = "The volume of a rectangular plastic container is %d cm<sup>3</sup>. How long is the container if the area of its face made up of the height and the breadth is %d cm<sup>2</sup>?"%(self.volume,self.area)
            self.answer = self.length 
            self.flag = 2
        else:
            self.area = self.length * self.breadth
            self.problem1 = "The volume of a cuboid is %d cm<sup>3</sup>. The area of its base is %d cm<sup>2</sup>. Find its height."%(self.volume,self.area)
            self.problem2 = random.choice(PersonName.BoyName)+" built a rectangular box with a base area of %d cm<sup>2</sup>. What is the height of the box if its volume is %d cm<sup>3</sup>?"%(self.area,self.volume)
            self.problem3 = random.choice(PersonName.GirlName)+" has a jewelry box that has a volume of %d cm<sup>3</sup>. What is the height of the jewelry box if its base area is %d cm<sup>2</sup>?"%(self.volume,self.area)
            self.problem4 = "Find the height of a rectangular block of wood that has a base area of %d cm<sup>2</sup> and a volume of %d cm<sup>3</sup>."%(self.area,self.volume)
            self.problem5 = "The base area of a rectangular steel container is %d cm<sup>2</sup>. Find the height of the container if its volume is %d cm<sup>3</sup>."%(self.area,self.volume)
            self.answer = self.height
            self.flag = 3

        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])

        self.unit = "cm"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.volume,self.area,self.flag,self.unit)

        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}

    def ExplainType2(self,problem,answer,volume,area,flag,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        if flag == 1:
            self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a cuboid</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Breadth &times; Length &times; Height</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Breadth &times; Area of face</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>So, Breadth</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Volume&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;Area of face</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(volume)+" "+unit+"<sup>3</sup></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of face</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(area)+" "+unit+"<sup>2</sup></td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Breadth</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:center'><u>&nbsp;"+str(volume)+"&nbsp;</u><br>" +str(area)+"</td></tr>"    
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 2:
            self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a cuboid</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length &times; Breadth &times; Height</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length &times; Area of face</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>So, Length</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Volume&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;Area of face</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(volume)+" "+unit+"<sup>3</sup></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of face</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(area)+" "+unit+"<sup>2</sup></td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Length</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:center'><u>&nbsp;"+str(volume)+"&nbsp;</u><br>" +str(area)+"</td></tr>"    
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 3:
            self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a cuboid</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Height &times; Length &times; Breadth</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Height &times; Area of base</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>So, Height</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Volume&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;Area of base</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(volume)+" "+unit+"<sup>3</sup></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Area of base</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(area)+" "+unit+"<sup>2</sup></td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Height</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:center'><u>&nbsp;"+str(volume)+"&nbsp;</u><br>" +str(area)+"</td></tr>"    
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemType3(self):
        '''e.g: The volume of a cuboid is 150 cm<sup>3</sup> and its length is 15 cm. Find the area of the face.'''
        self.complexity_level = "medium"
        self.HCScore = 3
        
        self.height = randint(2,10)
        self.length = randint(2,10)
        self.breadth = randint(2,10)
        
        if self.length==self.breadth:
            self.length = self.length + 1
            
        self.volume = self.length * self.breadth * self.height
        
        self.ProblemSelector = randint(1,4)
        if self.ProblemSelector == 1:
            self.problem1 = "A cuboid has a volume of %d cm<sup>3</sup> and a breadth of %d cm. Find the area of its face made up of the height and the length."%(self.volume,self.breadth)
            self.problem2 = random.choice(PersonName.BoyName)+" made a rectangular box that was %d cm in breadth and had a volume of %d cm<sup>3</sup>. Find the area of its face made up of the length and the height."%(self.breadth,self.volume)
            self.problem3 = random.choice(PersonName.GirlName)+" built a rectangular jewelry box that was %d cm wide and had a volume of %d cm<sup>3</sup>. What was the area of its face made up of the length and the height?"%(self.breadth,self.volume) 
            self.problem4 = "A rectangular block of wood has a volume of %d cm<sup>3</sup>. Find the area of its face made up of the length and the height if the block has a width of %d cm."%(self.volume,self.breadth)
            self.problem5 = "A glass container has a volume of %d cm<sup>3</sup>. What is the area of its face made up of the length and the height if the breadth of the rectangular container is %d cm?"%(self.volume,self.breadth)
            self.answer = self.length * self.height
            self.flag = 1
        elif self.ProblemSelector == 2:
            self.area = self.breadth * self.height
            self.problem1 = "The volume of a cuboid is %d cm<sup>3</sup>. Its length is %d cm. What is the area of its face made up of the breadth and the height?"%(self.volume,self.length)
            self.problem2 = "A rectangular box has a volume of %d cm<sup>3</sup>. Find the area of its face made up of the breadth and the height if the length of the box is %d cm."%(self.volume,self.length)
            self.problem3 = random.choice(PersonName.GirlName)+" has a rectangular jewelry box that has a length of %d cm and a volume of %d cm<sup>3</sup>. Find the area of its face made up of the breadth and the height."%(self.length,self.volume)
            self.problem4 = random.choice(PersonName.BoyName)+" is polishing a rectangular block of wood. What is the area of its face made up of the height and the breadth if the length of the block of wood is %d cm and its volume is %d cm<sup>3</sup>?"%(self.length,self.volume)
            self.problem5 = "The volume of a container is %d cm<sup>3</sup>. What is the area of its face made up of the breadth and the height if the length of the rectangular container is %d cm?"%(self.volume,self.length)
            self.answer = self.breadth * self.height 
            self.flag = 2
        elif self.ProblemSelector == 3:
            self.area = self.length * self.breadth
            self.problem1 = "The height of a cuboid is %d cm. What is the area of its base if its volume is %d cm<sup>3</sup>?"%(self.height,self.volume)
            self.problem2 = random.choice(PersonName.BoyName)+" built a rectangular box %d cm high. Find the base area of the box if its volume is %d cm<sup>3</sup>?"%(self.height,self.volume)
            self.problem3 = random.choice(PersonName.GirlName)+" has a jewelry box that has a volume of %d cm<sup>3</sup>. What is the area of its base if the height of the jewelry box is %d cm?"%(self.volume,self.height)
            self.problem4 = "Find the base area of a rectangular block of wood that has a height of %d cm and a volume of %d cm<sup>3</sup>."%(self.height,self.volume)
            self.problem5 = "The volume of a rectangular steel container is %d cm<sup>3</sup>. Find the base area of the container if its height is %d cm."%(self.volume,self.height)
            self.answer = self.length * self.breadth
            self.flag = 3
        else:
            self.breadth = self.length
            self.height = self.length
            self.volume = self.length * self.length * self.length
            self.area = self.length * self.length
            self.problem1 = "What is the area of the base of a cube if its volume is %d cm<sup>3</sup>?"%(self.volume)
            self.problem2 = random.choice(PersonName.BoyName)+" built a cubical box. Find the base area of the box if its volume is %d cm<sup>3</sup>?"%(self.volume)
            self.problem3 = random.choice(PersonName.GirlName)+" has a cubical jewelry box that has a volume of %d cm<sup>3</sup>. What is the area of the base of the box?"%(self.volume)
            self.problem4 = "Find the base area of a cubical block of wood that has a volume of %d cm<sup>3</sup>."%(self.volume)
            self.problem5 = "The volume of a cubical container is %d cm<sup>3</sup>. Find the base area of the container."%(self.volume)
            self.answer = self.length * self.length
            self.flag = 4

        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])

        self.unit = "cm"
        self.oldUnit = self.unit
        self.unit = self.unit+"<sup>2</sup>"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.length,self.breadth,self.height,self.volume,self.flag,self.oldUnit,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}

    def ExplainType3(self,problem,answer,length,breadth,height,volume,flag,oldUnit,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        if flag == 1:
            self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a cuboid</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length &times; Height &times; Breadth</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Area of face &times; Breadth</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>So, Area of face</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>&nbsp;&nbsp;Volume&nbsp;&nbsp;</u><br>&nbsp;&nbsp;Breadth</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(volume)+" "+oldUnit+"<sup>3</sup></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Breadth</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(breadth)+" "+oldUnit+"</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Area of face</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:center'><u>&nbsp;"+str(volume)+"&nbsp;</u><br>" +str(breadth)+"</td></tr>"    
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 2:
            self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a cuboid</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Breadth &times; Height &times; Length</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Area of face &times; Length</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>So, Area of face</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>&nbsp;&nbsp;Volume&nbsp;&nbsp;</u><br>&nbsp;&nbsp;Length</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(volume)+" "+oldUnit+"<sup>3</sup></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Length</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(length)+" "+oldUnit+"</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Area of face</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:center'><u>&nbsp;"+str(volume)+"&nbsp;</u><br>" +str(length)+"</td></tr>"    
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 3:
            self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a cuboid</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Breadth &times; Length &times; Height</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Area of base &times; Height</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right; vertical-align:middle'>So, Area of base</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:left'><u>&nbsp;&nbsp;Volume&nbsp;&nbsp;</u><br>&nbsp;&nbsp;Height</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(volume)+" "+oldUnit+"<sup>3</sup></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Height</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(height)+" "+oldUnit+"</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Area of base</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='padding-top:7px; text-align:center'><u>&nbsp;"+str(volume)+"&nbsp;</u><br>" +str(height)+"</td></tr>"    
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"
        elif flag == 4:
            self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a cube</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length &times; Length &times; Length</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>So, Length</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>&#8731;Volume</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>And, Area of base</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Length &times; Length</td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(volume)+" "+oldUnit+"<sup>3</sup></td></tr></table>"
    
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;'>Length of one edge of the cube</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left'>&#8731;"+str(volume)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left'>"+str(length)+" "+oldUnit+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;'>Area of base</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left'>"+str(length)+" &times; "+str(length)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td></tr></table>"

        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckType):
        if CheckType==1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False               