'''
Created on Jul 17, 2013
Module: P3ANIdentifying
Generates the Identifying 2-D Angles problems for Primary 3

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

class P3ANIdentifying:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemTypeMCQ1",],2:["ProblemTypeMCQ2",],3:["ProblemTypeMCQ3",],4:["ProblemTypeMCQ4",],
                            5:["ProblemTypeMCQ5",],6:["ProblemType6",],7:["ProblemTypeMCQ7",],8:["ProblemTypeMCQ8",],
                            9:["ProblemTypeMCQ9",],10:["ProblemType10",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemTypeMCQ1(),],2:[self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemTypeMCQ3(),],4:[self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemTypeMCQ5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemTypeMCQ7(),],8:[self.GenerateProblemTypeMCQ8(),],
                                    9:[self.GenerateProblemTypeMCQ9(),],10:[self.GenerateProblemType10(),],                                   
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
        #return self.GenerateProblemTypeMCQ3()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),
                            "ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            "ProblemTypeMCQ9":self.GenerateProblemTypeMCQ9(),
                            "ProblemType10":self.GenerateProblemType10(),
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
        
        self.angle1 = randint(30,120)
        self.flag = randint(1,3)
        if self.flag == 1:
            self.FunctionCall = "P3ANDrawLinesQ1()"
            self.answer = "False"
        elif self.flag == 2:
            self.FunctionCall = "P3ANDrawAngleQ1a("+str(self.angle1)+")"
            self.answer = "True"
        else:
            self.FunctionCall = "P3ANDrawAngleQ1b("+str(self.angle1)+")"
            self.answer = "True"

        self.problem = "The below pair of lines form an angle."
               
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
        self.solution_text = self.solution_text + "Any two lines meeting at a point will form an angle.<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "The two lines don't meet at a point, hence they do not form an angle."
        else:
            self.solution_text = self.solution_text + "The two lines meet at a point, hence they form an angle."
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
        
        self.angle1 = randint(45,90)
        self.colours = random.sample(["red","blue","green","yellow"],2)
        self.JSONColours = json.dumps(self.colours)
        self.FunctionCall = "P3ANDrawAngleQ2("+str(self.angle1)+","+self.JSONColours+")"
        self.answer = "%s lines"%(self.colours[0])
        self.wrongAnswers = [self.colours[0]+" lines",self.colours[1]+" lines"]
        random.shuffle(self.wrongAnswers)
        self.answer1 = self.wrongAnswers[0]
        self.answer2 = self.wrongAnswers[1]

        self.problem = "Which pair of lines form an angle?"
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.colours)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answer1,'answer2':self.answer2,'value1':self.answer1,'value2':self.answer2,
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType2(self,problem,answer,unit,colours):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Any two lines meeting at a point will form an angle.<br><br>"
        self.solution_text = self.solution_text + "The two %s lines meet at a point, hence they form an angle."%(colours[0].capitalize())
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
        
        self.angle1 = randint(70,85)
        self.angle2 = randint(20,40)
        self.angle3 = randint(90,120)
        self.angle4 = randint(30,40)
        self.colours = random.sample(["red","blue","green","yellow"],2)
        self.JSONColours = json.dumps(self.colours)
        self.flag = randint(1,2)
        if self.flag == 1:
            self.FunctionCall = "P3ANDrawAngleQ3a("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+self.JSONColours+")"
            self.answer = "%s lines"%(self.colours[0])
        else:
            self.FunctionCall = "P3ANDrawAngleQ3b("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+self.JSONColours+")"
            self.answer = "%s lines"%(self.colours[1])            
        self.wrongAnswers = [self.colours[0]+" lines",self.colours[1]+" lines"]
        random.shuffle(self.wrongAnswers)
        self.answer1 = self.wrongAnswers[0]
        self.answer2 = self.wrongAnswers[1]

        self.problem = "Which pair of lines form a smaller angle?"
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit,self.flag,self.colours)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answer1,'answer2':self.answer2,'value1':self.answer1,'value2':self.answer2,
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType3(self,problem,answer,unit,flag,colours):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        if flag == 1:
            smallAngle = colours[0]
            bigAngle = colours[1]
        else:
            smallAngle = colours[1]
            bigAngle = colours[0]            
        self.solution_text = self.solution_text + "The amount of turning between the two %s lines is smaller than the amount of turning between the two %s lines.<br><br>"%(smallAngle,bigAngle)
        self.solution_text = self.solution_text + "Hence, the %s lines form a smaller angle."%(smallAngle)
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
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        ''' using this i to take any two consecutive alphabets'''
        i = randint(0,24)
        self.AngleLabels = [self.characters[i],self.characters[i+1]]
        self.JSONAngleLabels = json.dumps([self.characters[i],self.characters[i+1]])
        self.flag = randint(1,2)
        if self.flag == 1:
            self.angle1 = randint(70,90)
            self.angle2 = randint(35,50)
            self.angle3 = randint(20,40)
            self.angle4 = randint(90,120)
            self.FunctionCall = "P3ANDrawAngleQ4a("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[1])
        else:
            self.angle1 = randint(10,20)
            self.angle2 = randint(130,150)
            self.angle3 = randint(20,40)
            self.angle4 = randint(80,110)
            self.FunctionCall = "P3ANDrawAngleQ4b("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[0])           
        self.wrongAnswers = ["&angle;%s"%(self.AngleLabels[0]),"&angle;%s"%(self.AngleLabels[1])]
        random.shuffle(self.wrongAnswers)
        self.answer1 = self.wrongAnswers[0]
        self.answer2 = self.wrongAnswers[1]

        self.problem = "Which angle is greater?"
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answer1,'answer2':self.answer2,'value1':self.answer1,'value2':self.answer2,
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType4(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        if flag == 1:
            smallAngle = AngleLabels[0]
            bigAngle = AngleLabels[1]
        else:
            smallAngle = AngleLabels[1]
            bigAngle = AngleLabels[0]            
        self.solution_text = self.solution_text + "The amount of turning formed by &angle;%s is greater than the amount of turning formed by &angle;%s.<br><br>"%(bigAngle,smallAngle)
        self.solution_text = self.solution_text + "Hence, the &angle;%s form a greater angle."%(bigAngle)
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

        self.colours = ["red","blue","green"]
        random.shuffle(self.colours)
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        ''' using this i to take any two consecutive alphabets'''
        i = randint(0,23)
        self.AngleLabels = [self.characters[i],self.characters[i+1],self.characters[i+2]]
        self.JSONAngleLabels = json.dumps([self.characters[i],self.characters[i+1],self.characters[i+2]])
        self.flag = randint(1,2)
        if self.flag == 1:
            self.angle1 = randint(70,90)
            self.angle2 = randint(10,25)
            self.angle3 = randint(130,150)
            self.angle4 = randint(70,90)
            self.angle5 = randint(20,30)
            self.FunctionCall = "P3ANDrawAngleQ5a("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[1])
        else:
            self.angle1 = randint(70,90)
            self.angle2 = randint(70,90)
            self.angle3 = randint(20,30)
            self.angle4 = randint(10,25)
            self.angle5 = randint(120,150)
            self.FunctionCall = "P3ANDrawAngleQ5b("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[2])           
        self.wrongAnswers = ["&angle;%s"%(self.AngleLabels[1]),"&angle;%s"%(self.AngleLabels[2])]
        random.shuffle(self.wrongAnswers)
        self.answer1 = self.wrongAnswers[0]
        self.answer2 = self.wrongAnswers[1]

        self.problem = "Which angle is greater than &angle;%s?"%(self.AngleLabels[0])
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answer1,'answer2':self.answer2,'value1':self.answer1,'value2':self.answer2,
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType5(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        baseAngle = AngleLabels[0]
        if flag == 1:
            bigAngle = AngleLabels[1]
        else:
            bigAngle = AngleLabels[2]            
        self.solution_text = self.solution_text + "The amount of turning formed by &angle;%s is greater than the amount of turning formed by &angle;%s.<br><br>"%(bigAngle,baseAngle)
        self.solution_text = self.solution_text + "Hence, &angle;%s form an angle which is greater than &angle;%s."%(bigAngle,baseAngle)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
            
    def GenerateProblemType6(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemType6'
        self.CheckAnswerType = 2

        self.colours = ["red","blue","green"]
        random.shuffle(self.colours)
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        ''' using this i to take any two consecutive alphabets'''
        i = randint(0,23)
        self.AngleLabels = [self.characters[i],self.characters[i+1],self.characters[i+2]]
        self.JSONAngleLabels = json.dumps([self.characters[i],self.characters[i+1],self.characters[i+2]])
        self.flag = randint(1,2)
        if self.flag == 1:
            self.angle1 = randint(70,80)
            self.angle2 = randint(30,40)
            self.angle3 = randint(20,30)
            self.angle4 = randint(70,80)
            self.angle5 = randint(120,150)
            self.FunctionCall = "P3ANDrawAngleQ6a("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "%s"%(self.AngleLabels[2])
        else:
            self.angle1 = randint(70,90)
            self.angle2 = randint(70,85)
            self.angle3 = randint(25,35)
            self.angle4 = randint(10,25)
            self.angle5 = randint(120,150)
            self.FunctionCall = "P3ANDrawAngleQ6b("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "%s"%(self.AngleLabels[2])           

        self.problem = "Fill in the blank.<br>Angle ____ is the greatest."
               
        self.unit = 'Angle'
        
        self.template = "P3ANDrawAnglesEnterType.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall,'dollar_unit':self.unit}            

    def ExplainType6(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>&angle;%s"%(str(answer))
        self.solution_text = "<font class='ExplanationFont'>"
        if flag == 1:
            bigAngle = AngleLabels[2]
        else:
            bigAngle = AngleLabels[2]            
        self.solution_text = self.solution_text + "The amount of turning formed by &angle;%s is greater than the amount of turning formed by the other two angles.<br><br>"%(bigAngle)
        self.solution_text = self.solution_text + "Hence, &angle;%s form the greatest angle."%(bigAngle)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
            
    def GenerateProblemTypeMCQ7(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemTypeMCQ7'
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
        if self.flag == 1:
            self.angle1 = randint(40,60)
            self.angle2 = randint(80,100)
            self.angle3 = randint(70,80)
            self.angle4 = randint(25,35)
            self.angle5 = randint(10,25)
            self.angle6 = randint(120,150)
            self.FunctionCall = "P3ANDrawAngleQ7a("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+str(self.angle6)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[2],self.AngleLabels[0],self.AngleLabels[1])           
            self.wrongAnswers = ["&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[1],self.AngleLabels[2],self.AngleLabels[0]),
                                 "&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[0],self.AngleLabels[1],self.AngleLabels[2]),
                                 "&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[2],self.AngleLabels[0],self.AngleLabels[1])
                                 ]
        else:
            self.angle1 = randint(70,90)
            self.angle2 = randint(25,35)
            self.angle3 = randint(25,35)
            self.angle4 = randint(100,120)
            self.angle5 = randint(30,40)
            self.angle6 = randint(70,80)
            self.FunctionCall = "P3ANDrawAngleQ7b("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+str(self.angle6)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[1],self.AngleLabels[2],self.AngleLabels[0])           
        
            self.wrongAnswers = ["&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[1],self.AngleLabels[2],self.AngleLabels[0]),
                                 "&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[0],self.AngleLabels[1],self.AngleLabels[2]),
                                 "&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[2],self.AngleLabels[1],self.AngleLabels[0])
                                 ]
        random.shuffle(self.wrongAnswers)
        self.answer1 = self.wrongAnswers[0]
        self.answer2 = self.wrongAnswers[1]
        self.answer3 = self.wrongAnswers[2]

        self.problem = "Arrange the angles in order, beginning with the greatest."
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles_3Choices.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'value1':self.answer1,'value2':self.answer2,'value3':self.answer3,
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType7(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        if flag == 1:
            smallAngle = AngleLabels[1]
            mediumAngle = AngleLabels[0]
            bigAngle = AngleLabels[2]
        else:
            smallAngle = AngleLabels[0]
            mediumAngle = AngleLabels[2]
            bigAngle = AngleLabels[1]
                        
        self.solution_text = self.solution_text + "The amount of turning formed by &angle;%s is greater than the amount of turning formed by the other two angles.<br><br>"%(bigAngle)
        self.solution_text = self.solution_text + "The amount of turning formed by &angle;%s is greater than the amount of turning formed &angle;%s.<br><br>"%(mediumAngle,smallAngle)
        self.solution_text = self.solution_text + "Hence, the order of angles beginning with the greatest will be &angle;%s, &angle;%s, &angle;%s."%(bigAngle,mediumAngle,smallAngle)
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

        self.colours = ["red","blue","green"]
        random.shuffle(self.colours)
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        ''' using this i to take any two consecutive alphabets'''
        i = randint(0,23)
        self.AngleLabels = [self.characters[i],self.characters[i+1],self.characters[i+2]]
        self.JSONAngleLabels = json.dumps([self.characters[i],self.characters[i+1],self.characters[i+2]])
        self.flag = randint(1,2)
        if self.flag == 1:
            self.angle1 = randint(70,80)
            self.angle2 = randint(30,40)
            self.angle3 = randint(20,30)
            self.angle4 = randint(70,80)
            self.angle5 = randint(100,120)
            self.FunctionCall = "P3ANDrawAngleQ6a("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[0])
        else:
            self.angle1 = randint(70,90)
            self.angle2 = randint(70,85)
            self.angle3 = randint(25,35)
            self.angle4 = randint(10,25)
            self.angle5 = randint(120,150)
            self.FunctionCall = "P3ANDrawAngleQ6b("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s"%(self.AngleLabels[1])           
        self.wrongAnswers = ["&angle;%s"%(self.AngleLabels[0]),"&angle;%s"%(self.AngleLabels[1]),"&angle;%s"%(self.AngleLabels[2])]
        random.shuffle(self.wrongAnswers)
        self.answer1 = self.wrongAnswers[0]
        self.answer2 = self.wrongAnswers[1]
        self.answer3 = self.wrongAnswers[2]

        self.problem = "Which angle is the smallest?"
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles_3Choices.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'value1':self.answer1,'value2':self.answer2,'value3':self.answer3,
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType8(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        if flag == 1:
            smallAngle = AngleLabels[0]
        else:
            smallAngle = AngleLabels[1]            
        self.solution_text = self.solution_text + "The amount of turning formed by &angle;%s is smaller than the amount of turning formed by the other two angles.<br><br>"%(smallAngle)
        self.solution_text = self.solution_text + "Hence, &angle;%s form the smallest angle."%(smallAngle)
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

        self.colours = ["red","blue","green"]
        random.shuffle(self.colours)
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        ''' using this i to take any two consecutive alphabets'''
        i = randint(0,23)
        self.AngleLabels = [self.characters[i],self.characters[i+1],self.characters[i+2]]
        self.JSONAngleLabels = json.dumps([self.characters[i],self.characters[i+1],self.characters[i+2]])
        self.flag = randint(1,2)
        if self.flag == 1:
            self.angle1 = randint(40,60)
            self.angle2 = randint(80,100)
            self.angle3 = randint(70,80)
            self.angle4 = randint(25,35)
            self.angle5 = randint(10,25)
            self.angle6 = randint(120,150)
            self.FunctionCall = "P3ANDrawAngleQ7a("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+str(self.angle6)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[1],self.AngleLabels[0],self.AngleLabels[2])           
            self.wrongAnswers = ["&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[1],self.AngleLabels[0],self.AngleLabels[2]),
                                 "&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[0],self.AngleLabels[1],self.AngleLabels[2]),
                                 "&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[2],self.AngleLabels[0],self.AngleLabels[1])
                                 ]
        else:
            self.angle1 = randint(70,90)
            self.angle2 = randint(25,35)
            self.angle3 = randint(25,35)
            self.angle4 = randint(100,120)
            self.angle5 = randint(30,40)
            self.angle6 = randint(70,80)
            self.FunctionCall = "P3ANDrawAngleQ7b("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+str(self.angle6)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[0],self.AngleLabels[2],self.AngleLabels[1])                   
            self.wrongAnswers = ["&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[0],self.AngleLabels[2],self.AngleLabels[1]),
                                 "&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[0],self.AngleLabels[1],self.AngleLabels[2]),
                                 "&angle;%s, &angle;%s, &angle;%s"%(self.AngleLabels[2],self.AngleLabels[1],self.AngleLabels[0])
                                 ]
        random.shuffle(self.wrongAnswers)
        self.answer1 = self.wrongAnswers[0]
        self.answer2 = self.wrongAnswers[1]
        self.answer3 = self.wrongAnswers[2]

        self.problem = "Arrange the angles in order, beginning with the smallest."
               
        self.unit = ''
        
        self.template = "P3ANDrawAngles_3Choices.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'value1':self.answer1,'value2':self.answer2,'value3':self.answer3,
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall}            

    def ExplainType9(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>%s %s"%(str(answer),unit)
        self.solution_text = "<font class='ExplanationFont'>"
        if flag == 1:
            smallAngle = AngleLabels[1]
            mediumAngle = AngleLabels[0]
            bigAngle = AngleLabels[2]
        else:
            smallAngle = AngleLabels[0]
            mediumAngle = AngleLabels[2]
            bigAngle = AngleLabels[1]
                        
        self.solution_text = self.solution_text + "The amount of turning formed by &angle;%s is smaller than the amount of turning formed by the other two angles.<br><br>"%(smallAngle)
        self.solution_text = self.solution_text + "The amount of turning formed by &angle;%s is smaller than the amount of turning formed &angle;%s.<br><br>"%(mediumAngle,bigAngle)
        self.solution_text = self.solution_text + "Hence, the order of angles beginning with the smallest will be &angle;%s, &angle;%s, &angle;%s."%(smallAngle,mediumAngle,bigAngle)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
            
    def GenerateProblemType10(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.problem_type = 'ProblemType10'
        self.CheckAnswerType = 2

        self.colours = ["red","blue","green"]
        random.shuffle(self.colours)
        self.JSONColours = json.dumps(self.colours)
        self.characters = string.ascii_uppercase
        ''' using this i to take any two consecutive alphabets'''
        i = randint(0,23)
        self.AngleLabels = [self.characters[i],self.characters[i+1],self.characters[i+2]]
        self.JSONAngleLabels = json.dumps([self.characters[i],self.characters[i+1],self.characters[i+2]])
        self.flag = randint(1,2)
        if self.flag == 1:
            self.angle1 = randint(70,90)
            self.angle2 = randint(10,25)
            self.angle3 = randint(130,150)
            self.angle4 = randint(70,90)
            self.angle5 = randint(20,30)
            self.FunctionCall = "P3ANDrawAngleQ5a("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "%s"%(self.AngleLabels[2])
        else:
            self.angle1 = randint(70,90)
            self.angle2 = randint(70,90)
            self.angle3 = randint(20,30)
            self.angle4 = randint(10,25)
            self.angle5 = randint(120,150)
            self.FunctionCall = "P3ANDrawAngleQ5b("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+","+str(self.angle5)+","+self.JSONColours+","+self.JSONAngleLabels+")"
            self.answer = "%s"%(self.AngleLabels[1])           

        self.problem = "Fill in the blank.<br>Angle ____ is smaller than Angle %s"%(self.AngleLabels[0])
               
        self.unit = 'Angle '
        
        self.template = "P3ANDrawAnglesEnterType.html"       

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.unit,self.flag,self.AngleLabels)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,"video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'explain':self.explain,'problem_type':self.problem_type,'grade':self.grade,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,
                'FunctionCall':self.FunctionCall,'dollar_unit':self.unit}            

    def ExplainType10(self,problem,answer,unit,flag,AngleLabels):
        self.answer_text = "<br>The correct answer is:<br>&angle;%s"%(str(answer))
        self.solution_text = "<font class='ExplanationFont'>"
        baseAngle = AngleLabels[0]
        if flag == 1:
            smallAngle = AngleLabels[2]
        else:
            smallAngle = AngleLabels[1]            
        self.solution_text = self.solution_text + "The amount of turning formed by &angle;%s is smaller than the amount of turning formed by &angle;%s.<br><br>"%(smallAngle,baseAngle)
        self.solution_text = self.solution_text + "Hence, &angle;%s form an angle which is smaller than &angle;%s."%(smallAngle,baseAngle)
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
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"")
                return str(answer)==str(InputAnswer).upper()
            except ValueError:
                return False                                          