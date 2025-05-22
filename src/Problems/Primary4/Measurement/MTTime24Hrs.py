'''
Created on Mar 18, 2012
Module: MTTime24Hrs
Generates the "24 Hrs Time" problems for Primary 4

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
import string

class MTTime24Hrs:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
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
        #return self.GenerateProblemType2()

    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g.:
        Express the time using 24-Hour clock:'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(1,12)
        self.number2 = randint(0,59)
        
        self.time = random.choice(["a.m.","p.m."])
        
        if self.number2 < 10:
            self.number2 = '0'+str(self.number2)
        self.problem = "Express the time using 24-Hour clock:<br><br>"
        self.problem = self.problem + str(self.number1)+"."+str(self.number2)+" "+self.time
        
        if self.time == "a.m.":
            if self.number1 < 10:
                self.number1 = '0'+str(self.number1)
            if self.number1 == 12:
                self.number1 = '00'
            self.answer = str(self.number1)+" "+str(self.number2)
        else:
            if self.number1 == 12:
                self.answer = str(self.number1)+" "+str(self.number2)
            else:
                self.answer = str(self.number1+12)+" "+str(self.number2)
        
        
        self.template = "EnterTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.time)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType1(self,problem,answer,number1,number2,time):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g.:
        Express the time using 12-Hour clock:'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(0,23)
        self.number2 = randint(0,59)
        
        if self.number1 < 10:
            self.number1 = '0'+str(self.number1)
        if self.number2 < 10:
            self.number2 = '0'+str(self.number2)
        self.problem = "Express the time using 12-Hour clock:<br><br>"
        self.problem = self.problem + str(self.number1)+" "+str(self.number2)
        
        if int(self.number1) < 12:
            self.time = "a.m."
        else:
            self.time = "p.m."
        
        self.number1 = int(self.number1)

        if self.number1 == 0:
            self.number1 = 12
        
        if self.number1 > 12:
            self.number1 = self.number1 - 12
            
        self.answer = str(self.number1)+"."+str(self.number2)+" "+self.time 

        self.template = "EnterTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.time)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}            

    def ExplainType2(self,problem,answer,number1,number2,time):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                if " " in InputAnswer:
                    InputAnswer = string.join(InputAnswer.split(),"")[0:4]
                    answer = string.join(answer.split(),"")[0:4]
                    return answer==InputAnswer
            except ValueError:
                return False
        elif CheckAnswer==2:
            try:
                if " " in InputAnswer:
                    InputAnswer = string.join(InputAnswer.split(),"")
                    answer = string.join(answer.split(),"")
                    '''Two different logic for 1:29am and 11:29am because of the length of the string'''
                    if len(answer)==9:
                        if "." in InputAnswer[3:]:
                            InputAnswer = string.upper(InputAnswer[:2]+string.split(InputAnswer[3:],".")[0]+string.split(InputAnswer[3:],".")[1])
                        else:
                            InputAnswer = string.upper(InputAnswer[:2]+InputAnswer[3:])
                        answer = string.upper(answer[:2]+string.split(answer[3:],".")[0]+string.split(answer[3:],".")[1])
                    else:
                        if "." in InputAnswer[3:]:
                            InputAnswer = string.upper(InputAnswer[:1]+string.split(InputAnswer[2:],".")[0]+string.split(InputAnswer[2:],".")[1])
                        else:
                            InputAnswer = string.upper(InputAnswer[:1]+InputAnswer[2:])
                        answer = string.upper(answer[:1]+string.split(answer[2:],".")[0]+string.split(answer[2:],".")[1])
                    return answer==InputAnswer
            except ValueError:
                return False            