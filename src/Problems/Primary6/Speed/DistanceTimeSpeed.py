'''
Created on Oct 23, 2011

Module: DistanceTimeSpeed
Generates "relationship between distance, time and speed" problems for Primary 6

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
import string

class DistanceTimeSpeed:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"easy":[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),
                                    self.GenerateProblemType2(),self.GenerateProblemType3(),
                                    self.GenerateProblemTypeMCQ2(),self.GenerateProblemTypeMCQ3(),],
                            }
        try:
            return random.choice(self.ProblemType[level])
        except KeyError:
            return random.choice(random.choice(self.ProblemType.values()))
        #return self.GenerateProblemTypeMCQ3()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1"],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1()],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3()],
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
        #return self.GenerateProblemTypeMCQ3()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g: Speed of an object = 10 Km/hr
                Time taken = 2hr
                Find the distance travelled by the object?'''
        self.complexity_level = "easy"
        self.HCScore = 3
        #self.UnitTranslation={"h":"hours","min":"minutes","s":"seconds"}
        self.UnitTranslation={"h":"h","min":"min","s":"s"}
        self.SpeedUnit = random.choice(["km/h","m/min","m/s","cm/s"])
        self.DistanceUnit = self.SpeedUnit.partition("/")[0]
        self.TimeUnit = self.UnitTranslation[self.SpeedUnit.partition("/")[2]]
        self.speed = randint(2,100)
        self.time = randint(2,10)
        self.distance = self.speed * self.time
        
        self.problem1 = "The speed of an object is "+str(self.speed)+" "+self.SpeedUnit+".&nbsp;"
        self.problem1 = self.problem1 + "What is the distance travelled by it in "+str(self.time)+" "+self.TimeUnit+"?<br>"
        
        self.problem2 = "An object travels for "+str(self.time)+" "+self.TimeUnit+" at a speed of "+str(self.speed)+" "+self.SpeedUnit+".&nbsp;"
        self.problem2 = self.problem2+"How far does it go?"
        
        self.problem3 = "Speed of an object = "+str(self.speed)+" "+self.SpeedUnit+"<br><br>"
        self.problem3 = self.problem3+"Time taken = "+str(self.time)+" "+self.TimeUnit+"<br><br>"
        self.problem3 = self.problem3+"Find the total distance travelled by the object.<br>"
        
        self.problem = random.choice([self.problem1, self.problem2, self.problem3])
        
        self.answer = self.distance
        self.unit = self.DistanceUnit
                                                                                            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.distance,self.speed,self.time,self.SpeedUnit,
                                              self.DistanceUnit,self.TimeUnit,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}

    def ExplainType1(self,problem,answer,distance,speed,time,SpeedUnit,DistanceUnit,TimeUnit,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Speed</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(speed)+" "+SpeedUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Time taken</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(time)+" "+TimeUnit+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Distance travelled</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Speed &nbsp;&times;&nbsp; Time taken</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Distance travelled</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(speed)+" "+SpeedUnit+" &nbsp;&times;&nbsp; "+str(time)+" "+TimeUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td><tr>"
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Speed/Distance-Time-Speed" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):
        '''e.g: Speed of an object = 10 Km/hr
                Distance travelled = 20 km
                Find the time taken to travel the distance.'''
        self.complexity_level = "easy"
        self.HCScore = 3
        #self.UnitTranslation={"h":"hours","min":"minutes","s":"seconds"}
        self.UnitTranslation={"h":"h","min":"min","s":"s"}
        self.SpeedUnit = random.choice(["km/h","m/min","m/s","cm/s"])
        self.DistanceUnit = self.SpeedUnit.partition("/")[0]
        self.TimeUnit = self.UnitTranslation[self.SpeedUnit.partition("/")[2]]
        self.speed = randint(2,100)
        self.time = randint(2,10)
        self.distance = self.speed * self.time
        
        self.problem1 = "An object travels "+str(self.distance)+" "+self.DistanceUnit+" at a speed of "+str(self.speed)+" "+self.SpeedUnit+". Find the time taken to cover this distance."
        
        self.problem2 = "How long does an object take to travel a distance of "+str(self.distance)+" "+self.DistanceUnit+" at a speed of "+str(self.speed)+" "+str(self.SpeedUnit)+"."
        
        self.problem3 = "Speed of an object = "+str(self.speed)+" "+self.SpeedUnit+"<br><br>"
        self.problem3 = self.problem3+"Distance travelled = "+str(self.distance)+" "+self.DistanceUnit+"<br><br>"
        self.problem3 = self.problem3+"Find the time taken by the object to travel this distance.<br>"
        
        self.problem = random.choice([self.problem1, self.problem2, self.problem3])

        self.answer = self.time
        self.unit = self.TimeUnit
                                                                                            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.distance,self.speed,self.time,self.SpeedUnit,
                                              self.DistanceUnit,self.TimeUnit,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}

    def ExplainType2(self,problem,answer,distance,speed,time,SpeedUnit,DistanceUnit,TimeUnit,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Distance travelled</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(distance)+" "+DistanceUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Speed</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(speed)+" "+SpeedUnit+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Time taken</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='padding-top:0px'><u>Distance travelled</u><br/>Speed</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Time taken</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='padding-top:0px'><u>&nbsp;&nbsp;"+str(distance)+" "+DistanceUnit+"&nbsp;&nbsp;</u><br>"+str(speed)+" "+SpeedUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td><tr>"
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Speed/Distance-Time-Speed" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):
        '''e.g: Distance travelled = 20 km
                Time taken = 2 hr
                Find the speed of the object.'''
        self.complexity_level = "easy"
        self.HCScore = 3
        #self.UnitTranslation={"h":"hours","min":"minutes","s":"seconds"}
        self.UnitTranslation={"h":"h","min":"min","s":"s"}
        self.SpeedUnit = random.choice(["km/h","m/min","m/s","cm/s"])
        self.DistanceUnit = self.SpeedUnit.partition("/")[0]
        self.TimeUnit = self.UnitTranslation[self.SpeedUnit.partition("/")[2]]
        self.speed = randint(2,100)
        self.time = randint(2,10)
        self.distance = self.speed * self.time
        self.problem1 = "An object takes "+str(self.time)+" "+self.TimeUnit+" to travel a distance of "+str(self.distance)+" "+self.DistanceUnit+".&nbsp;"
        self.problem1 = self.problem1 + "Find the average speed of the object."
        
        self.problem2 = "An object travels "+str(self.distance)+" "+self.DistanceUnit+" in "+str(self.time)+" "+str(self.TimeUnit)+". What is its average speed for the journey?"
        
        self.problem3 = "Distance travelled by an object = "+str(self.distance)+" "+self.DistanceUnit+"<br><br>"
        self.problem3 = self.problem3+"Time taken = "+str(self.time)+" "+self.TimeUnit+"<br><br>"
        self.problem3 = self.problem3+"Find the speed of the object.<br>"
        
        self.problem = random.choice([self.problem1, self.problem2, self.problem3])
        
        self.answer = self.speed
        self.unit = self.SpeedUnit
                                                                                            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.distance,self.speed,self.time,self.SpeedUnit,
                                              self.DistanceUnit,self.TimeUnit,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}

    def ExplainType3(self,problem,answer,distance,speed,time,SpeedUnit,DistanceUnit,TimeUnit,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Distance travelled</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(distance)+" "+DistanceUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Time taken</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(time)+" "+TimeUnit+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Speed</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='padding-top:0px'><u>Distance travelled</u><br/>Time taken</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Speed</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='padding-top:0px'><u>&nbsp;"+str(distance)+" "+DistanceUnit+"&nbsp;</u><br>"+str(time)+" "+TimeUnit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" "+unit+"</td><tr>"
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Speed/Distance-Time-Speed" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
                                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,
                    CheckAnswerType,grade,complexity_level,HCScore):
        
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
            self.value1 = string.join(self.answer1.split(),"")
            self.value2 = string.join(self.answer2.split(),"")
            self.value3 = string.join(self.answer3.split(),"")
            self.value4 = string.join(self.answer4.split(),"")
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'answer4':self.answer4,'value1':self.value1,'value2':self.value2
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type,
                'CheckAnswerType':CheckAnswerType,'grade':6,"complexity_level":complexity_level,"HCScore":HCScore}      

    def GenerateProblemTypeMCQ1(self):
        '''e.g: Speed of an object = 10 Km/hr
                Time taken = 2hr
                Find the distance travelled by the object?'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.ProblemSelector = 1
        #self.UnitTranslation={"h":"hours","min":"minutes","s":"seconds"}
        self.UnitTranslation={"h":"h","min":"min","s":"s"}
        if self.ProblemSelector == 1:
            self.flag = 1
            self.SpeedUnit = random.choice(["km/h","m/min","m/s","cm/s"])
            self.DistanceUnit = self.SpeedUnit.partition("/")[0]
            self.TimeUnit = self.UnitTranslation[self.SpeedUnit.partition("/")[2]]
            self.speed = randint(2,100)
            self.time = randint(2,10)
            self.distance = self.speed * self.time
            
            self.problem1 = "What is the distance travelled by an object in "+str(self.time)+" "+self.TimeUnit+" if it is moving at a speed of "+str(self.speed)+" "+self.SpeedUnit+"?<br>"

            self.problem2 = "An object is travelling at an average speed of "+str(self.speed)+" "+self.SpeedUnit+". What is the distance covered by it in "+str(self.time)+" "+self.TimeUnit+"?"

            self.problem3 = "Speed of an object = "+str(self.speed)+" "+self.SpeedUnit+"<br><br>"
            self.problem3 = self.problem3+"Time taken = "+str(self.time)+" "+self.TimeUnit+"<br><br>"
            self.problem3 = self.problem3+"Find the total distance travelled by the object.<br>"
        
            self.problem = random.choice([self.problem1, self.problem2, self.problem3])

            self.answer = self.distance
            self.unit = self.DistanceUnit
                                                           
        self.problem_type = "ProblemTypeMCQ1"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.speed * (self.time-1))+" "+self.unit)
        self.wrongAnswers.append(str(self.speed * (self.time+1))+" "+self.unit)
        self.wrongAnswers.append(str(self.answer+2)+" "+self.unit)
        self.wrongAnswers.append(str(self.answer-2)+" "+self.unit)                 
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.distance,self.speed,self.time,self.SpeedUnit,
                                              self.DistanceUnit,self.TimeUnit,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        self.answer = str(self.answer)+" "+self.unit
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def GenerateProblemTypeMCQ2(self):
        '''e.g: Speed of an object = 10 Km/hr
                Distance travelled = 20 km
                Find the time taken to travel the distance.'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.ProblemSelector = 1
        #self.UnitTranslation={"h":"hours","min":"minutes","s":"seconds"}
        self.UnitTranslation={"h":"h","min":"min","s":"s"}
        if self.ProblemSelector == 1:
            self.flag = 1
            self.SpeedUnit = random.choice(["km/h","m/min","m/s","cm/s"])
            self.DistanceUnit = self.SpeedUnit.partition("/")[0]
            self.TimeUnit = self.UnitTranslation[self.SpeedUnit.partition("/")[2]]
            self.speed = randint(2,100)
            self.time = randint(2,10)
            self.distance = self.speed * self.time
            
            self.problem1 = "An object is moving at an average speed of "+str(self.speed)+" "+self.SpeedUnit+". &nbsp;"
            self.problem1 = self.problem1 + "How long does it take to travel "+str(self.distance)+" "+self.DistanceUnit+"?<br>"
            
            self.problem2 = "How much time does an object take to travel "+str(self.distance)+" "+self.DistanceUnit+" at a speed of "+str(self.speed)+" "+self.SpeedUnit+"?"
            
            self.problem3 = "Speed of an object = "+str(self.speed)+" "+self.SpeedUnit+"<br><br>"
            self.problem3 = self.problem3+"Distance travelled = "+str(self.distance)+" "+self.DistanceUnit+"<br><br>"
            self.problem3 = self.problem3+"Find the time taken by the object to travel this distance.<br>"
            
            self.problem = random.choice([self.problem1, self.problem2, self.problem3])
            
            self.answer = self.time
            self.unit = self.TimeUnit

        self.problem_type = "ProblemTypeMCQ2"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1)+" "+self.unit)
        self.wrongAnswers.append(str(self.answer-1)+" "+self.unit)
        self.wrongAnswers.append(str(self.answer+2)+" "+self.unit)
        self.wrongAnswers.append(str(self.answer-2)+" "+self.unit)                 
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.distance,self.speed,self.time,self.SpeedUnit,
                                              self.DistanceUnit,self.TimeUnit,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        self.answer = str(self.answer)+" "+self.unit
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def GenerateProblemTypeMCQ3(self):
        '''e.g: Distance travelled = 20 km
                Time taken = 2 hr
                Find the speed of the object.'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.ProblemSelector = 1
        #self.UnitTranslation={"h":"hours","min":"minutes","s":"seconds"}
        self.UnitTranslation={"h":"h","min":"min","s":"s"}
        if self.ProblemSelector == 1:
            self.flag = 1
            self.SpeedUnit = random.choice(["km/h","m/min","m/s","cm/s"])
            self.DistanceUnit = self.SpeedUnit.partition("/")[0]
            self.TimeUnit = self.UnitTranslation[self.SpeedUnit.partition("/")[2]]
            self.speed = randint(2,100)
            self.time = randint(2,10)
            self.distance = self.speed * self.time

            self.problem1 = "An object takes "+str(self.time)+" "+self.TimeUnit+" to travel a distance of "+str(self.distance)+" "+self.DistanceUnit+".&nbsp;"
            self.problem1 = self.problem1 + "Find the average speed of the object."
            
            self.problem2 = "An object covers "+str(self.distance)+" "+self.DistanceUnit+" in "+str(self.time)+" "+str(self.TimeUnit)+". What is its average speed?"
            
            self.problem3 = "Distance travelled by an object = "+str(self.distance)+" "+self.DistanceUnit+"<br><br>"
            self.problem3 = self.problem3+"Time taken = "+str(self.time)+" "+self.TimeUnit+"<br><br>"
            self.problem3 = self.problem3+"Find the speed of the object.<br>"
            
            self.problem = random.choice([self.problem1, self.problem2, self.problem3])

            self.answer = self.speed
            self.unit = self.SpeedUnit

        self.problem_type = "ProblemTypeMCQ3"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1)+" "+self.unit)
        self.wrongAnswers.append(str(self.answer-1)+" "+self.unit)
        self.wrongAnswers.append(str(self.answer+2)+" "+self.unit)
        self.wrongAnswers.append(str(self.answer-2)+" "+self.unit)                 
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.distance,self.speed,self.time,self.SpeedUnit,
                                              self.DistanceUnit,self.TimeUnit,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        self.answer = str(self.answer)+" "+self.unit
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def checkAnswer(self,template,answer,InputAnswer,CheckType):
        if CheckType==1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        if CheckType==2:
            try:
                answer = string.join(answer.split(),"")
                InputAnswer = string.join(InputAnswer.split(),"")
                return (answer == InputAnswer)
            except ValueError:
                return False               