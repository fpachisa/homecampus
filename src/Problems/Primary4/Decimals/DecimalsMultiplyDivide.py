'''
Created on Mar 14, 2012
Module: DecimalsMultiplyDivide
Generates the "Decimals Multiplication and Division" problems for Primary 4

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
import logging

class DecimalsMultiplyDivide:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            3:["ProblemType3",],
                            4:["ProblemType4",],
                            5:["ProblemType5",],
                            6:["ProblemType6",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],
                                    5:[self.GenerateProblemType5(),],
                                    6:[self.GenerateProblemType6(),],
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
        #return self.GenerateProblemType6()

    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(2,9)
        self.number2 = randint(2,9)
        self.FloatNumber1 = float(self.number1) / 10
        
        self.problem = str(self.FloatNumber1)+" &times; "+str(self.number2)+" = "
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1*self.number2) / 10

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.FloatNumber1,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType1(self,problem,answer,FloatNumber1,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"

        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(22,99)
        self.number2 = randint(2,9)
        self.FloatNumber1 = float(self.number1) / 100
        
        self.problem = str(self.FloatNumber1)+" &times; "+str(self.number2)+" = "
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1*self.number2) / 100

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.FloatNumber1,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType2(self,problem,answer,FloatNumber1,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"

        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(2,9)
        self.number2 = randint(2,9)
        self.FloatNumber1 = float(self.number1*self.number2) / 10
        
        self.problem = str(self.FloatNumber1)+" &divide; "+str(self.number2)+" = "
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1) / 10

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.FloatNumber1,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType3(self,problem,answer,FloatNumber1,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"

        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g.:
        0.42 / 7 = '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(22,99)
        self.number2 = randint(2,9)
        self.FloatNumber1 = float(self.number1*self.number2) / 100
        
        self.problem = str(self.FloatNumber1)+" &divide; "+str(self.number2)+" = "
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1) / 100

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.FloatNumber1,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType4(self,problem,answer,FloatNumber1,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"

        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType5(self):
        '''e.g.:
        4 / 8 = '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(2,9)
        self.number2 = randint(self.number1+1,self.number1+10)
        
        self.problem = str(self.number1)+" &divide; "+str(self.number2)+" = <br><br>"
        self.problem = self.problem + "<font style='font-size:0.7em'>"
        self.problem = self.problem + random.choice(["(Round off the answer to the nearest tenth)","(Round off the answer to 1 decimal place)"])+"</font>" 
        self.template = "EnterTypeProblems.html"
        
        self.answer = round(float(self.number1)/self.number2,1) 

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType5(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"

        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType6(self):
        '''e.g.:
        4 / 8 = '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(2,9)
        self.number2 = randint(self.number1+1,self.number1+10)
        
        self.problem = str(self.number1)+" &divide; "+str(self.number2)+" = <br><br>"
        self.problem = self.problem + "<font style='font-size:0.7em'>"
        self.problem = self.problem + random.choice(["(Round off the answer to the nearest hundredth)","(Round off the answer to 2 decimal places)"])+"</font>" 
        self.template = "EnterTypeProblems.html"
        
        self.answer = round(float(self.number1)/self.number2,2) 

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType6(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"

        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore,grade,CheckAnswerType):
        
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
            self.value1 = self.answer1
            self.value2 = self.answer2
            self.value3 = self.answer3
            self.value4 = self.answer4
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'answer4':self.answer4,'value1':self.value1,'value2':self.value2
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type,
                'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}      

    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        What does the digit 7 stand for in 71453? '''
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.problem_type = "ProblemTypeMCQ1"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.number1 = randint(2,9)
        self.number2 = randint(2,9)
        self.FloatNumber1 = float(self.number1) / 10
        self.FloatNumber2 = float(self.number2) / 10
        
        self.problem = str(self.FloatNumber1)+" + "+str(self.FloatNumber2)+" = "

        self.answer = float(self.number1+self.number2) / 10

        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        self.wrongAnswers.append(self.answer + 0.1)
        self.wrongAnswers.append(self.answer + 0.2)        
        if self.answer > 0.2:
            self.wrongAnswers.append(self.answer - 0.1)
            self.wrongAnswers.append(self.answer - 0.2)
        elif self.answer > 0.1 and self.answer < 0.2:
            self.wrongAnswers.append(self.answer - 0.1)
            self.wrongAnswers.append(self.answer + 0.3)
        else:
            self.wrongAnswers.append(self.answer + 0.3)
            self.wrongAnswers.append(self.answer + 0.4)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)
                                                                
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False