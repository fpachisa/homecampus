'''
Created on Nov 15, 2011

Module: Triangles
Generates "Finding unknown angles of a triangle" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''
import random
import math
from random import randint

class Triangles:
    
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
        self.ProblemType = {1:"ProblemType1",2:"ProblemType2",3:"ProblemType3",}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemType2(),3:self.GenerateProblemType3(),}
        
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
        #return self.GenerateProblemType2()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            }
        return self.ProblemType[problem_type]
            
    def GenerateProblemType1(self):
        '''e.g: Find the unknown marked angle.'''
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.angle1 = randint(35,85)
        '''create triangle based on angle1. To find out angle2 using the below formula'''
        self.angle2 = int(math.degrees(math.atan(100/(150-100/math.tan(math.radians(self.angle1))))))
        self.FunctionCall = "DrawRandomTriangles("+str(self.angle1)+","+str(self.angle2)+")"
        self.answer = 180 - self.angle1 - self.angle2

        self.problem = "Find the unknown marked angle.<br><br>"
        self.problem = self.problem + "(&ang;BAC = "+str(self.angle1)+"&deg;, &ang;BCA = "+str(self.angle2)+"&deg;)"
        self.unit = "&deg;"
        self.template = "Geometry.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.angle1,self.angle2,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType1(self,problem,answer,angle1,angle2,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+unit
        self.solution_text = "Sum of all three angles of a triangle = 180&deg;<br><br>"
        self.solution_text = self.solution_text + "Two given angles are "+str(angle1)+"&deg; and "+str(angle2)+"&deg;<br><br>"
        self.solution_text = self.solution_text + "Therefore, the missing angle = 180&deg; - "+str(angle1)+"&deg; - "+str(angle2)+"&deg;<br><br>"

        self.solution_text = self.solution_text + "Hence the correct answer is "+str(answer)+unit
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemType2(self):
        '''e.g: Find the unknown marked angle.'''
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.height = randint(80,130)
        self.base = randint(100,150)
        self.angle1 = 90
        '''creating a right angle triangle. To find out angle2 using the below formula'''
        self.angle2 = int(math.degrees(math.atan(float(self.height)/float(self.base))))
        self.FunctionCall = "DrawRightAngleTriangle("+str(self.height)+","+str(self.base)+","+str(self.angle1)+","+str(self.angle2)+")"
        self.answer = 180 - self.angle1 - self.angle2

        self.problem = "Find the unknown marked angle.<br><br>"
        self.problem = self.problem + "(&ang;BCA = "+str(self.angle2)+"&deg;)"
        self.unit = "&deg;"
        self.template = "Geometry.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.angle1,self.angle2,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType2(self,problem,answer,angle1,angle2,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+unit
        self.solution_text = "Sum of all three angles of a triangle = 180&deg;<br><br>"
        self.solution_text = self.solution_text + "Since its a right angled triangle one of the angle is 90&deg;. The other angle is "+str(angle2)+"&deg;<br><br>"
        self.solution_text = self.solution_text + "Therefore, the missing angle = 180&deg; - "+str(angle1)+"&deg; - "+str(angle2)+"&deg;<br><br>"

        self.solution_text = self.solution_text + "Hence the correct answer is "+str(answer)+unit
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemType3(self):
        '''e.g: Find the unknown marked angle.'''
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.angle1 = randint(95,120)
        '''create triangle based on angle1. To find out angle2 using the below formula'''
        self.angle2 = int(math.degrees(math.atan(100/(150-100/math.tan(math.radians(self.angle1))))))
        self.FunctionCall = "DrawRandomTriangles("+str(self.angle1)+","+str(self.angle2)+")"
        self.answer = 180 - self.angle1 - self.angle2

        self.problem = "Find the unknown marked angle.<br><br>"
        self.problem = self.problem + "(&ang;BAC = "+str(self.angle1)+"&deg;, &ang;BCA = "+str(self.angle2)+"&deg;)"
        self.unit = "&deg;"
        self.template = "Geometry.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.angle1,self.angle2,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType3(self,problem,answer,angle1,angle2,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+unit
        self.solution_text = "Sum of all three angles of a triangle = 180&deg;<br><br>"
        self.solution_text = self.solution_text + "Two given angles are "+str(angle1)+"&deg; and "+str(angle2)+"&deg;<br><br>"
        self.solution_text = self.solution_text + "Therefore, the missing angle = 180&deg; - "+str(angle1)+"&deg; - "+str(angle2)+"&deg;<br><br>"

        self.solution_text = self.solution_text + "Hence the correct answer is "+str(answer)+unit
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckType):
        if CheckType==1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False               