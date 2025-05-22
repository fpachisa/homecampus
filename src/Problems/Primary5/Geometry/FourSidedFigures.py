'''
Created on Nov 17, 2011

Module: FourSidedFigures
Generates "Finding unknown angles of a four sided figure" problems for Primary 5

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

class FourSidedFigures:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"easy":[self.GenerateProblemType1(),self.GenerateProblemType2(),self.GenerateProblemType3(),],
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
        #return self.GenerateProblemType3()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            }
        return self.ProblemType[problem_type]
            
    def GenerateProblemType1(self):
        '''e.g: Find the unknown marked angle in the below parallelograms.'''
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.angle1 = randint(35,75)
        self.flag = randint(1,3)
        self.FunctionCall = "DrawParallelogram("+str(self.angle1)+","+str(self.flag)+")"
        if self.flag==2:
            self.answer = self.angle1
        else:
            self.answer = 180 - self.angle1

        self.problem = "Find the unknown marked angle in the parallelogram below.<br><br>"
        self.problem = self.problem + "(&ang;ABC = "+str(self.angle1)+"&deg;)"
        self.unit = "&deg;"
        self.template = "Geometry.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.angle1,self.unit,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType1(self,problem,answer,angle1,unit,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+unit
        if flag == 2:
            self.solution_text = "The opposite angles of a parallelogram are equal.<br><br>"
            self.solution_text = self.solution_text + "Therefore, &ang;x = &ang;ABC = "+str(angle1)+unit
        else:
            self.solution_text = "The sum of a pair of angles between two parallel sides is 180&deg;<br><br>"
            self.solution_text = self.solution_text + "&ang;ABC + &ang;x = 180&deg;<br><br>"
            self.solution_text = self.solution_text + "&ang;x = 180&deg; - "+str(angle1)+unit+" = "+str(answer)+unit
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+str(answer)+unit+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                      
        return self.explain
            
    def GenerateProblemType2(self):
        '''e.g: Find the unknown marked angle in the below rhombus.'''
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.angle1 = randint(35,75)
        self.flag = randint(1,3)
        self.FunctionCall = "DrawRhombus("+str(self.angle1)+","+str(self.flag)+")"
        if self.flag==2:
            self.answer = self.angle1
        else:
            self.answer = 180 - self.angle1

        self.problem = "Find the unknown marked angle in the rhombus below.<br><br>"
        self.problem = self.problem + "(&ang;ABC = "+str(self.angle1)+"&deg;)"
        self.unit = "&deg;"
        self.template = "Geometry.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.angle1,self.unit,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType2(self,problem,answer,angle1,unit,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+unit
        if flag == 2:
            self.solution_text = "The opposite angles of a rhombus are equal.<br><br>"
            self.solution_text = self.solution_text + "Therefore, &ang;x = &ang;ABC = "+str(angle1)+unit
        else:
            self.solution_text = "The sum of a pair of angles between two parallel sides is 180&deg;<br><br>"
            self.solution_text = self.solution_text + "&ang;ABC + &ang;x = 180&deg;<br><br>"
            self.solution_text = self.solution_text + "&ang;x = 180&deg; - "+str(angle1)+unit+" = "+str(answer)+unit
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+str(answer)+unit+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                      
        return self.explain
            
    def GenerateProblemType3(self):
        '''e.g: Find the unknown marked angle in the trapezium below.'''
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.angle1 = randint(35,75)

        self.FunctionCall = "DrawTrapezium("+str(self.angle1)+")"

        self.answer = 180 - self.angle1

        self.problem = "Find the unknown marked angle in the trapezium below.<br><br>"
        self.problem = self.problem + "(&ang;ABC = "+str(self.angle1)+"&deg;)"
        self.unit = "&deg;"
        self.template = "Geometry.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.angle1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType3(self,problem,answer,angle1,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+unit
        self.solution_text = "The sum of a pair of angles between two parallel sides is 180&deg;<br><br>"
        self.solution_text = self.solution_text + "&ang;ABC + &ang;x = 180&deg;<br><br>"
        self.solution_text = self.solution_text + "&ang;x = 180&deg; - "+str(angle1)+unit+" = "+str(answer)+unit
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+str(answer)+unit+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                      
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckType):
        if CheckType==1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False               