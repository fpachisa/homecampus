'''
Created on Mar 08, 2012
Module: DecimalsRoundingOff
Generates the "Decimals Rounding Off" problems for Primary 4

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

class DecimalsRoundingOff:
    
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
        Round off 3.2 to the nearest whole number.'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(11,89)
        
        while self.number1%10==0:
            self.number1 = randint(11,89)
        
        self.FloatNumber1 = float(self.number1) / 10
             
        self.problem = "Round off "+str(self.FloatNumber1)+" to the nearest whole number."        
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = int(round(self.FloatNumber1,0))

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.FloatNumber1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType1(self,problem,answer,number1,float1):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        
        self.solution_text = self.solution_text + "Coming Soon!!"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g.:
        Round off 3.25 to the nearest whole number.'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(101,999)
        
        while self.number1%10==0 or self.number1%100==0:
            self.number1 = randint(101,999)
        
        self.FloatNumber1 = float(self.number1) / 100
             
        self.problem = "Round off "+str(self.FloatNumber1)+" to the nearest whole number."        
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = int(round(self.FloatNumber1,0))

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.FloatNumber1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType2(self,problem,answer,number1,float1):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        
        self.solution_text = self.solution_text + "Coming Soon!!"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g.:
        Round off 3.25 to the nearest whole number.'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(1011,9999)
        while self.number1%10==0 or self.number1%100==0 or self.number1%1000==0:
            self.number1 = randint(1011,9999)
        
        self.FloatNumber1 = float(self.number1) / 1000
             
        self.problem = "Round off "+str(self.FloatNumber1)+" to the nearest whole number."        
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = int(round(self.FloatNumber1,0))

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.FloatNumber1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType3(self,problem,answer,number1,float1):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        
        self.solution_text = self.solution_text + "Coming Soon!!"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g.:
        Round off 3.25 to the nearest tenth.'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(101,999)
        while self.number1%10==0 or self.number1%100==0:
            self.number1 = randint(101,999)
        
        self.FloatNumber1 = float(self.number1) / 100
             
        self.problem1 = "Round off "+str(self.FloatNumber1)+" to the nearest tenth."        
        self.problem2 = "Round off "+str(self.FloatNumber1)+" to 1 decimal place."
        
        self.problem = random.choice([self.problem1,self.problem2])
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = round(self.FloatNumber1,1)

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.FloatNumber1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}            

    def ExplainType4(self,problem,answer,number1,float1):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        
        self.solution_text = self.solution_text + "Coming Soon!!"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType5(self):
        '''e.g.:
        Round off 3.256 to the nearest tenth.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(1011,9919)
        while self.number1%10==0 or self.number1%100==0 or self.number1%1000==0:
            self.number1 = randint(1011,9999)
        
        self.FloatNumber1 = float(self.number1) / 1000
             
        self.problem1 = "Round off "+str(self.FloatNumber1)+" to the nearest tenth."        
        self.problem2 = "Round off "+str(self.FloatNumber1)+" to 1 decimal place."
        
        self.problem = random.choice([self.problem1,self.problem2])
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = round(self.FloatNumber1,1)

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.FloatNumber1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}            

    def ExplainType5(self,problem,answer,number1,float1):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Coming Soon!!"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text        
        return self.explain
                
    def GenerateProblemType6(self):
        '''e.g.:
        Round off 3.258 to the nearest hundredth.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(1011,9999)
        while self.number1%10==0 or self.number1%100==0 or self.number1%1000==0:
            self.number1 = randint(1011,9999)

        self.FloatNumber1 = float(self.number1) / 1000
             
        self.problem1 = "Round off "+str(self.FloatNumber1)+" to the nearest hundredth."        
        self.problem2 = "Round off "+str(self.FloatNumber1)+" to 2 decimal places."
        
        self.problem = random.choice([self.problem1,self.problem2])
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = round(self.FloatNumber1,2)
        if len(str(self.answer).partition(".")[2])!=2:
            self.answer = str(self.answer)+"0"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.FloatNumber1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}            

    def ExplainType6(self,problem,answer,number1,float1):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        
        self.solution_text = self.solution_text + "Coming Soon!!"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
                                
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False                                                   
        elif CheckAnswer==2:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False     