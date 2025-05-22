'''
Created on Jul 29, 2013
Module: P3ANRightAngle
Generates the Right Angles problems for Primary 3

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
  

History:
  
'''
import random
from random import randint
import simplejson as json
import string

class P3ANRightAngle:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemTypeMCQ1",],2:["ProblemTypeMCQ2",],3:["ProblemTypeMCQ3",],4:["ProblemTypeMCQ4",],
                            5:["ProblemTypeMCQ5",],6:["ProblemTypeMCQ6",],7:["ProblemType7",],8:["ProblemTypeMCQ8",],
                            9:["ProblemTypeMCQ9",],10:["ProblemTypeMCQ10",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemTypeMCQ1(),],2:[self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemTypeMCQ3(),],4:[self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemTypeMCQ5(),],6:[self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemTypeMCQ8(),],
                                    9:[self.GenerateProblemTypeMCQ9(),],10:[self.GenerateProblemTypeMCQ10(),],
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
        #return self.GenerateProblemTypeMCQ10()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            "ProblemTypeMCQ9":self.GenerateProblemTypeMCQ9(),
                            "ProblemTypeMCQ10":self.GenerateProblemTypeMCQ10(),
                            }
        return self.ProblemType[problem_type]
            
    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        '''              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemTypeMCQ1'
        self.CheckAnswerType = 1
        
        self.colours = random.choice(["red","blue","green"])
        self.JSONColours = json.dumps([self.colours])
        self.labels = random.choice(string.ascii_uppercase)
        self.JSONAngleLabels = json.dumps([self.labels])
        
        self.flag = randint(1,3)
        if self.flag == 1:
            self.angle1 = randint(30,70)
            self.FunctionCall = "P3ANRightAngleQ1a("+str(self.angle1)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "False"
        elif self.flag == 2:
            self.angle1 = 90
            self.FunctionCall = "P3ANRightAngleQ1b("+str(self.angle1)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "True"
        else:
            self.angle1 = randint(110,140)
            self.FunctionCall = "P3ANRightAngleQ1c("+str(self.angle1)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "False"
        
        self.problem = "The below pair of lines form a right angle."
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':"True",'answer2':"False",'value1':"True",'value2':"False",
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType1(self,problem,answer,unit,flag):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Right angle is an angle of 90&deg;, as in a corner of a square.<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "The angle given is smaller than right angle."
        elif flag == 3:
            self.solution_text = self.solution_text + "The angle given is greater than right angle."
        else:
            self.solution_text = self.solution_text + "The angle given is a right angle."
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
            
    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        '''              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemTypeMCQ2'
        self.CheckAnswerType = 1
        
        self.colours = ["red","blue","green"]
        random.shuffle(self.colours)
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        ''' using this i to take any two consecutive alphabets'''
        i = randint(0,23)
        self.AngleLabels = [self.characters[i],self.characters[i+1],self.characters[i+2]]
        self.JSONAngleLabels = json.dumps([self.characters[i],self.characters[i+1],self.characters[i+2]])
        self.flag = randint(1,2)
        self.flag = 1
        if self.flag == 1:
            self.angle1 = randint(70,80)
            self.angle2 = randint(30,40)
            self.angle3 = randint(30,40)
            self.angle4 = 90
            self.angle5 = randint(120,150)
            self.FunctionCall = "P3ANRightAngleQ2a("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[1])
        else:
            self.angle1 = randint(50,70)
            self.angle2 = randint(70,85)
            self.angle3 = randint(25,35)
            self.angle4 = randint(35,55)
            self.angle5 = 90
            self.FunctionCall = "P3ANRightAngleQ2b("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[2])
            
        self.answers = ["&angle;%s"%(self.AngleLabels[0]),"&angle;%s"%(self.AngleLabels[1]),"&angle;%s"%(self.AngleLabels[2])]
        random.shuffle(self.answers)          
        
        self.problem = "Which of the below angles form a right angle?"
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles_3Choices.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answers[0],'answer2':self.answers[1],'answer3':self.answers[2],
                'value1':self.answers[0],'value2':self.answers[1],'value3':self.answers[2],
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType2(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Right angle is an angle of 90&deg;, as in a corner of a square.<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "Hence, &angle;%s is a right angle."%(AngleLabels[1])
        else:
            self.solution_text = self.solution_text + "Hence, &angle;%s is a right angle."%(AngleLabels[2])
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
        '''              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemTypeMCQ3'
        self.CheckAnswerType = 1
        
        self.colours = random.choice(["red","blue","green"])
        self.JSONColours = json.dumps([self.colours])
        self.labels = random.choice(string.ascii_uppercase)
        self.JSONAngleLabels = json.dumps([self.labels])
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.angle1 = randint(30,70)
            self.FunctionCall = "P3ANRightAngleQ1a("+str(self.angle1)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "False"
        else:
            self.angle1 = randint(110,140)
            self.FunctionCall = "P3ANRightAngleQ1c("+str(self.angle1)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "True"
        
        self.problem = "The &angle;%s is greater than right angle."%(self.labels)
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':"True",'answer2':"False",'value1':"True",'value2':"False",
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType3(self,problem,answer,unit,flag):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Right angle is an angle of 90&deg;, as in a corner of a square.<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "The angle given is smaller than right angle."
        else:
            self.solution_text = self.solution_text + "The angle given is greater than right angle."
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
            
    def GenerateProblemTypeMCQ4(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemTypeMCQ4'
        self.CheckAnswerType = 1

        self.colours = random.sample(["red","blue","green"],2)
        random.shuffle(self.colours)
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        ''' using this i to take any two consecutive alphabets'''
        i = randint(0,24)
        self.AngleLabels = [self.characters[i],self.characters[i+1]]
        self.JSONAngleLabels = json.dumps([self.characters[i],self.characters[i+1]])
        self.flag = randint(1,3)
        if self.flag == 1:
            self.angle1 = randint(40,60)
            self.angle2 = randint(80,100)
            self.angle3 = randint(10,25)
            self.angle4 = randint(120,150)
            self.FunctionCall = "P3ANRightAngleQ4a("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[0])           
        elif self.flag == 2:
            self.angle1 = randint(70,80)
            self.angle2 = randint(30,40)
            self.angle3 = randint(120,150)
            self.FunctionCall = "P3ANRightAngleQ4c("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[0])
        else:
            self.angle1 = randint(50,70)
            self.angle2 = randint(40,60)
            self.angle3 = randint(25,35)
            self.angle4 = randint(100,120)
            self.FunctionCall = "P3ANRightAngleQ4b("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[0])           

        self.answers = ["&angle;%s"%(self.AngleLabels[0]),"&angle;%s"%(self.AngleLabels[1])]
        random.shuffle(self.answers)

        self.problem = "Which of the below angle is smaller than a right angle?"
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answers[0],'answer2':self.answers[1],
                'value1':self.answers[0],'value2':self.answers[1],
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType4(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Right angle is an angle of 90&deg;, as in a corner of a square.<br><br>"
        self.solution_text = self.solution_text + "&angle;%s is smaller than right angle."%(AngleLabels[0])
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemTypeMCQ5(self):
        '''e.g.:
        '''              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemTypeMCQ5'
        self.CheckAnswerType = 1
        
        self.colours = random.choice(["red","blue","green"])
        self.JSONColours = json.dumps([self.colours])
        self.labels = random.choice(string.ascii_uppercase)
        self.JSONAngleLabels = json.dumps([self.labels])
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.angle1 = randint(30,70)
            self.FunctionCall = "P3ANRightAngleQ1a("+str(self.angle1)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "smaller"
        else:
            self.angle1 = randint(110,140)
            self.FunctionCall = "P3ANRightAngleQ1c("+str(self.angle1)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "greater"
        
        self.answers = ['smaller','greater']
        random.shuffle(self.answers)
        
        self.problem = "&angle;%s is _____ than right angle."%(self.labels)
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answers[0],'answer2':self.answers[1],'value1':self.answers[0],'value2':self.answers[1],
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType5(self,problem,answer,unit,flag):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Right angle is an angle of 90&deg;, as in a corner of a square.<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "The angle given is smaller than right angle."
        else:
            self.solution_text = self.solution_text + "The angle given is greater than right angle."
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
            
    def GenerateProblemTypeMCQ6(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemTypeMCQ6'
        self.CheckAnswerType = 1

        self.colours = random.sample(["red","blue","green"],2)
        random.shuffle(self.colours)
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        ''' using this i to take any two consecutive alphabets'''
        i = randint(0,24)
        self.AngleLabels = [self.characters[i],self.characters[i+1]]
        self.JSONAngleLabels = json.dumps([self.characters[i],self.characters[i+1]])
        self.flag = randint(1,3)
        if self.flag == 1:
            self.angle1 = randint(40,60)
            self.angle2 = randint(80,100)
            self.angle3 = randint(10,25)
            self.angle4 = randint(120,150)
            self.FunctionCall = "P3ANRightAngleQ4a("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[1])           
        elif self.flag == 2:
            self.angle1 = randint(70,80)
            self.angle2 = randint(30,40)
            self.angle3 = randint(120,150)
            self.FunctionCall = "P3ANRightAngleQ4c("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[1])
        else:
            self.angle1 = randint(50,70)
            self.angle2 = randint(40,60)
            self.angle3 = randint(25,35)
            self.angle4 = randint(100,120)
            self.FunctionCall = "P3ANRightAngleQ4b("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[1])           

        self.answers = ["&angle;%s"%(self.AngleLabels[0]),"&angle;%s"%(self.AngleLabels[1])]
        random.shuffle(self.answers)

        self.problem = "Which of the below angle is greater than a right angle?"
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answers[0],'answer2':self.answers[1],
                'value1':self.answers[0],'value2':self.answers[1],
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType6(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Right angle is an angle of 90&deg;, as in a corner of a square.<br><br>"
        self.solution_text = self.solution_text + "&angle;%s is greater than right angle."%(AngleLabels[1])        
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
            
    def GenerateProblemType7(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemType7'
        self.CheckAnswerType = 2

        self.colours = ["red","blue","green"]
        random.shuffle(self.colours)
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        self.AngleLabels = [self.characters[0],self.characters[1],self.characters[2],self.characters[3],self.characters[4],
                            self.characters[5],self.characters[6],self.characters[7],self.characters[8],self.characters[9],self.characters[10],]
        self.JSONAngleLabels = json.dumps(self.AngleLabels)
        self.flag = randint(1,7)
        if self.flag == 1:
            self.angle = random.choice([20,30,180,190,200])
            self.FunctionCall = "P3ANRightAngleQ7a("+self.JSONColours+","+str(self.angle)+")"
            self.answer = 2
        elif self.flag == 2:
            self.angle = random.choice([20,30,180,190,200])
            self.FunctionCall = "P3ANRightAngleQ7b("+self.JSONColours+","+str(self.angle)+")"
            self.answer = 4
        elif self.flag == 3:
            self.FunctionCall = "P3ANRightAngleQ7c("+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = 5
        elif self.flag == 4:
            self.FunctionCall = "P3ANRightAngleQ7d("+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = 6
        elif self.flag == 5:
            self.FunctionCall = "P3ANRightAngleQ7e("+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = 7
        elif self.flag == 6:
            self.FunctionCall = "P3ANRightAngleQ7f("+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = 8
        elif self.flag == 7:
            self.FunctionCall = "P3ANRightAngleQ7g("+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = 9
            
        self.problem = "How many right angles are there in below figure?"
               
        self.unit = 'right angles'
        self.template = "P3ANDrawAnglesEnterType.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall,'unit':self.unit}            

    def ExplainType7(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>%s %s."%(str(answer), unit)
        self.solution_text = "<font class='ExplanationFont'>"
        if flag == 1:
            self.solution_text = self.solution_text + "The figure has two right angles."
        elif flag == 2:
            self.solution_text = self.solution_text + "The figure is a square.<br><br>A square has 4 right angles."
        elif flag == 3:
            self.solution_text = self.solution_text + "The figure has 5 right angles.<br><br>"
            self.solution_text = self.solution_text + "&angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s and &angle;%s%s%s are right angles."%(AngleLabels[0],AngleLabels[1],AngleLabels[2],
                                                                                                                                AngleLabels[1],AngleLabels[2],AngleLabels[3],
                                                                                                                                AngleLabels[2],AngleLabels[3],AngleLabels[4],
                                                                                                                                AngleLabels[3],AngleLabels[4],AngleLabels[5],
                                                                                                                                AngleLabels[4],AngleLabels[5],AngleLabels[6],)
        elif flag == 4:
            self.solution_text = self.solution_text + "The figure has 6 right angles.<br><br>"
            self.solution_text = self.solution_text + "&angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s and &angle;%s%s%s are right angles."%(AngleLabels[0],AngleLabels[1],AngleLabels[2],
                                                                                                                                AngleLabels[1],AngleLabels[2],AngleLabels[3],
                                                                                                                                AngleLabels[2],AngleLabels[3],AngleLabels[4],
                                                                                                                                AngleLabels[3],AngleLabels[4],AngleLabels[5],
                                                                                                                                AngleLabels[4],AngleLabels[5],AngleLabels[6],
                                                                                                                                AngleLabels[5],AngleLabels[6],AngleLabels[7])
        elif flag == 5:
            self.solution_text = self.solution_text + "The figure has 7 right angles.<br><br>"
            self.solution_text = self.solution_text + "&angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s and &angle;%s%s%s are right angles."%(AngleLabels[0],AngleLabels[1],AngleLabels[2],
                                                                                                                                AngleLabels[1],AngleLabels[2],AngleLabels[3],
                                                                                                                                AngleLabels[2],AngleLabels[3],AngleLabels[4],
                                                                                                                                AngleLabels[3],AngleLabels[4],AngleLabels[5],
                                                                                                                                AngleLabels[4],AngleLabels[5],AngleLabels[6],
                                                                                                                                AngleLabels[5],AngleLabels[6],AngleLabels[7],
                                                                                                                                AngleLabels[6],AngleLabels[7],AngleLabels[8])
        elif flag == 6:
            self.solution_text = self.solution_text + "The figure has 8 right angles.<br><br>"
            self.solution_text = self.solution_text + "&angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s and &angle;%s%s%s are right angles."%(AngleLabels[0],AngleLabels[1],AngleLabels[2],
                                                                                                                                AngleLabels[1],AngleLabels[2],AngleLabels[3],
                                                                                                                                AngleLabels[2],AngleLabels[3],AngleLabels[4],
                                                                                                                                AngleLabels[3],AngleLabels[4],AngleLabels[5],
                                                                                                                                AngleLabels[4],AngleLabels[5],AngleLabels[6],
                                                                                                                                AngleLabels[5],AngleLabels[6],AngleLabels[7],
                                                                                                                                AngleLabels[6],AngleLabels[7],AngleLabels[8],
                                                                                                                                AngleLabels[7],AngleLabels[8],AngleLabels[9])
        elif flag == 7:
            self.solution_text = self.solution_text + "The figure has 9 right angles.<br><br>"
            self.solution_text = self.solution_text + "&angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s, &angle;%s%s%s and &angle;%s%s%s are right angles."%(AngleLabels[0],AngleLabels[1],AngleLabels[2],
                                                                                                                                AngleLabels[1],AngleLabels[2],AngleLabels[3],
                                                                                                                                AngleLabels[2],AngleLabels[3],AngleLabels[4],
                                                                                                                                AngleLabels[3],AngleLabels[4],AngleLabels[5],
                                                                                                                                AngleLabels[4],AngleLabels[5],AngleLabels[6],
                                                                                                                                AngleLabels[5],AngleLabels[6],AngleLabels[7],
                                                                                                                                AngleLabels[6],AngleLabels[7],AngleLabels[8],
                                                                                                                                AngleLabels[7],AngleLabels[8],AngleLabels[9],
                                                                                                                                AngleLabels[8],AngleLabels[9],AngleLabels[10])

        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
            
    def GenerateProblemTypeMCQ8(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemTypeMCQ8'
        self.CheckAnswerType = 1

        self.colours = random.sample(["red","blue","green"],2)
        random.shuffle(self.colours)
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        ''' using this i to take any two consecutive alphabets'''
        i = randint(0,22)
        self.AngleLabels = [self.characters[i],self.characters[i+1],self.characters[i+2],self.characters[i+3]]
        self.JSONAngleLabels = json.dumps([self.characters[i],self.characters[i+1],self.characters[i+2],self.characters[i+3]])
        self.flag = randint(1,3)
        if self.flag == 1:
            self.angle1 = randint(10,30)
            self.angle2 = randint(100,130)
            self.FunctionCall = "P3ANRightAngleQ9a("+str(self.angle1)+","+str(self.angle2)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "2"
            self.answers = ["1","2","3"]                       
        elif self.flag == 2:
            self.FunctionCall = "P3ANRightAngleQ9b("+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "0"
            self.answers = ["0","4","2"]                       
        elif self.flag == 3:
            self.FunctionCall = "P3ANRightAngleQ9c("+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "1"
            self.answers = ["1","3","2"]                       

        random.shuffle(self.answers)

        self.problem = "How many angles are smaller than right angle in below figure?"
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles_3Choices.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answers[0],'answer2':self.answers[1],'answer3':self.answers[2],
                'value1':self.answers[0],'value2':self.answers[1],'value3':self.answers[2],
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType8(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        if flag == 1:
            self.solution_text = self.solution_text + "In the given figure, there are 2 angles smaller than right angle.<br><br>"
            self.solution_text = self.solution_text + "&angle;%s%s%s & &angle;%s%s%s are smaller than right angle."%(AngleLabels[0],AngleLabels[1],AngleLabels[2],AngleLabels[0],AngleLabels[2],AngleLabels[1])        
        elif flag == 2:
            self.solution_text = self.solution_text + "Given shape is a rectangle. All the angles of a rectangle are 90&deg;<br><br>"
            self.solution_text = self.solution_text + "Hence, in a rectangle there is no angle which is smaller than a right angle."
        elif flag == 3:
            self.solution_text = self.solution_text + "In the given figure, there is 1 angle smaller than right angle.<br><br>"
            self.solution_text = self.solution_text + "&angle;%s%s%s is smaller than right angle."%(AngleLabels[0],AngleLabels[1],AngleLabels[3])        
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
           
    def GenerateProblemTypeMCQ9(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemTypeMCQ9'
        self.CheckAnswerType = 1

        self.colours = random.sample(["red","blue","green"],2)
        random.shuffle(self.colours)
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        ''' using this i to take any two consecutive alphabets'''
        i = randint(0,23)
        self.AngleLabels = [self.characters[i],self.characters[i+1],self.characters[i+2]]
        self.JSONAngleLabels = json.dumps([self.characters[i],self.characters[i+1],self.characters[i+2]])
        self.flag = randint(1,4)
        if self.flag == 1:
            self.FunctionCall = "P3ANRightAngleQ8a("+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = " %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[0],self.AngleLabels[1],self.AngleLabels[2])
            self.answers = [" %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[0],self.AngleLabels[1],self.AngleLabels[2]),
                            " %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[1],self.AngleLabels[0],self.AngleLabels[2]),
                            " %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[0],self.AngleLabels[2],self.AngleLabels[1])]                       
        elif self.flag == 2:
            self.FunctionCall = "P3ANRightAngleQ8b("+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = " %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[0],self.AngleLabels[1],self.AngleLabels[2])           
            self.answers = [" %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[0],self.AngleLabels[1],self.AngleLabels[2]),
                            " %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[1],self.AngleLabels[0],self.AngleLabels[2]),
                            " %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[0],self.AngleLabels[2],self.AngleLabels[1])]                       
        elif self.flag == 3:
            self.FunctionCall = "P3ANRightAngleQ8c("+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = " %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[1],self.AngleLabels[2],self.AngleLabels[0])           
            self.answers = [" %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[1],self.AngleLabels[2],self.AngleLabels[0]),
                            " %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[0],self.AngleLabels[1],self.AngleLabels[2]),
                            " %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[2],self.AngleLabels[0],self.AngleLabels[1])]                       
        elif self.flag == 4:
            self.FunctionCall = "P3ANRightAngleQ8d("+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = " %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[1],self.AngleLabels[0],self.AngleLabels[2])           
            self.answers = [" %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[1],self.AngleLabels[0],self.AngleLabels[2]),
                            " %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[1],self.AngleLabels[2],self.AngleLabels[0]),
                            " %s &minus;&gt; %s &minus;&gt; %s"%(self.AngleLabels[2],self.AngleLabels[1],self.AngleLabels[0])]                       

        random.shuffle(self.answers)

        self.problem = "Which points will you connect to form a right angle?"
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles_3Choices.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answers[0],'answer2':self.answers[1],'answer3':self.answers[2],
                'value1':self.answers[0],'value2':self.answers[1],'value3':self.answers[2],
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType9(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Right angle is an angle of 90&deg;, as in a corner of a square.<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "If you join points %s &minus;&gt; %s &minus;&gt; %s, it will make a right angle."%(AngleLabels[0],AngleLabels[1],AngleLabels[2])        
        elif flag == 2:
            self.solution_text = self.solution_text + "If you join points %s &minus;&gt; %s &minus;&gt; %s, it will make a right angle."%(AngleLabels[0],AngleLabels[1],AngleLabels[2])        
        elif flag == 3:
            self.solution_text = self.solution_text + "If you join points %s &minus;&gt; %s &minus;&gt; %s, it will make a right angle."%(AngleLabels[1],AngleLabels[2],AngleLabels[0])        
        elif flag == 4:
            self.solution_text = self.solution_text + "If you join points %s &minus;&gt; %s &minus;&gt; %s, it will make a right angle."%(AngleLabels[1],AngleLabels[0],AngleLabels[2])        
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
            
    def GenerateProblemTypeMCQ10(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemTypeMCQ10'
        self.CheckAnswerType = 1

        self.colours = random.sample(["red","blue","green"],2)
        random.shuffle(self.colours)
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        ''' using this i to take any two consecutive alphabets'''
        i = randint(0,22)
        self.AngleLabels = [self.characters[i],self.characters[i+1],self.characters[i+2],self.characters[i+3]]
        self.JSONAngleLabels = json.dumps([self.characters[i],self.characters[i+1],self.characters[i+2],self.characters[i+3]])
        self.flag = randint(1,2)
        if self.flag == 1:
            self.angle1 = randint(10,30)
            self.angle2 = randint(100,130)
            self.FunctionCall = "P3ANRightAngleQ9a("+str(self.angle1)+","+str(self.angle2)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s%s%s"%(self.AngleLabels[1],self.AngleLabels[0],self.AngleLabels[2])
            self.answers = ["&angle;%s%s%s"%(self.AngleLabels[1],self.AngleLabels[0],self.AngleLabels[2]),
                            "&angle;%s%s%s"%(self.AngleLabels[0],self.AngleLabels[1],self.AngleLabels[2]),
                            "&angle;%s%s%s"%(self.AngleLabels[1],self.AngleLabels[2],self.AngleLabels[0])]                                          
        elif self.flag == 2:
            self.FunctionCall = "P3ANRightAngleQ9c("+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s%s%s"%(self.AngleLabels[2],self.AngleLabels[3],self.AngleLabels[1])
            self.answers = ["&angle;%s%s%s"%(self.AngleLabels[2],self.AngleLabels[3],self.AngleLabels[1]),
                            "&angle;%s%s%s"%(self.AngleLabels[0],self.AngleLabels[1],self.AngleLabels[3]),
                            "&angle;%s%s%s"%(self.AngleLabels[0],self.AngleLabels[2],self.AngleLabels[3])]                                          

        random.shuffle(self.answers)

        self.problem = "Which angle is greater than right angle in below figure?"
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles_3Choices.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answers[0],'answer2':self.answers[1],'answer3':self.answers[2],
                'value1':self.answers[0],'value2':self.answers[1],'value3':self.answers[2],
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType10(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Right angle is an angle of 90&deg;, as in a corner of a square.<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "&angle;%s%s%s is greater than right angle."%(AngleLabels[1],AngleLabels[0],AngleLabels[2])        
        elif flag == 2:
            self.solution_text = self.solution_text + "&angle;%s%s%s is greater than right angle."%(AngleLabels[2],AngleLabels[3],AngleLabels[1])        
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return str(answer)==str(InputAnswer)
            except ValueError:
                return False
        elif CheckAnswer == 2:
            numbers = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
            try:
                # if user types two instead of 2 then also it should be correct
                InputAnswer = numbers[string.join(str(InputAnswer).split(),"").lower()]
            except KeyError:
                pass
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False                                          