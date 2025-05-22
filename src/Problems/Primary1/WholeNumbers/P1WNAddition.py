'''
Created on Jan 26, 2013

Module: Addition
Generates the Addition problems for Primary 1 (Created exclusively for Rayan..not for public yet)

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

class P1WNAddition:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
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
        #return self.GenerateProblemTypeMCQ4()

    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            }
        return self.ProblemType[problem_type]
    
    def GenerateProblemType1(self):
        '''e.g.
        2 + 3 = 
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemType1"
        self.grade = 1
        self.CheckAnswerType = 1

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.answer = self.number1 + self.number2
        while self.answer >= 10:
            self.number1 = randint(1,9)
            self.number2 = randint(1,9)
            self.answer = self.number1 + self.number2
        
        self.problem = str(self.number1)+" + "+str(self.number2)+" ="
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':self.problem_type,
                'grade':self.grade,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType}

    def ExplainType1(self,problem,answer,number1,number2):

        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  ""
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType2(self):
        '''e.g.
        12 + 3 = 
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemType2"
        self.grade = 1
        self.CheckAnswerType = 1

        self.number1 = randint(1,19)
        self.number2 = randint(1,19)
        self.answer = self.number1 + self.number2
        while self.answer<10 or self.answer >= 20:
            self.number1 = randint(1,19)
            self.number2 = randint(1,19)
            self.answer = self.number1 + self.number2
        
        self.problem = str(self.number1)+" + "+str(self.number2)+" ="
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,str(self.answer),self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':self.problem_type,
                'grade':self.grade,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType}

    def ExplainType2(self,problem,answer,number1,number2):

        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  ""
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType3(self):
        '''e.g.
        Find the missing number: 
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemType3"
        self.grade = 1
        self.CheckAnswerType = 1

        self.StartingNumber = randint(1,5)
        self.Skip = randint(1,5)
        self.MissingNumberIndex = randint(0,4)
        self.numbers = []
        
        for i in range(5):
            self.numbers.append(self.StartingNumber+i*self.Skip)
        
        self.answer = self.numbers[self.MissingNumberIndex]
        
        self.problem = "Find the missing number:<br><br>"
        for i in range(5):
            if i!=self.MissingNumberIndex:
                self.problem = self.problem + str(self.numbers[i])+"&nbsp;&nbsp;&nbsp;&nbsp;"
            else: 
                self.problem = self.problem + "?&nbsp;&nbsp;&nbsp;&nbsp;"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':self.problem_type,
                'grade':self.grade,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType}

    def ExplainType3(self,problem,answer,numbers):

        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  ""
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType4(self):
        '''e.g.
        Find the missing number: 
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemType4"
        self.grade = 1
        self.CheckAnswerType = 1

        self.StartingNumber = randint(1,5)
        self.Skip = randint(1,5)
        self.MissingNumberIndex = randint(0,4)
        self.numbers = []
        
        for i in range(5):
            self.numbers.append(self.StartingNumber+i*self.Skip)
        
        self.numbers.reverse()
        
        self.answer = self.numbers[self.MissingNumberIndex]        
        
        self.problem = "Find the missing number:<br><br>"
        for i in range(5):
            if i!=self.MissingNumberIndex:
                self.problem = self.problem + str(self.numbers[i])+"&nbsp;&nbsp;&nbsp;&nbsp;"
            else: 
                self.problem = self.problem + "?&nbsp;&nbsp;&nbsp;&nbsp;"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':self.problem_type,
                'grade':self.grade,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType}

    def ExplainType4(self,problem,answer,numbers):

        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  ""
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
        '''e.g.
        2 + 3 = 
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemType1"
        self.grade = 1
        self.CheckAnswerType = 1

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.answer = self.number1 + self.number2
        while self.answer >= 10:
            self.number1 = randint(1,9)
            self.number2 = randint(1,9)
            self.answer = self.number1 + self.number2
        
        self.problem = str(self.number1)+" + "+str(self.number2)+" ="
        
        self.template = "MCQTypeProblems.html"
        
        '''List of wrong answers is same as the list of numbers displayed'''
        self.wrongAnswers = []
        
        self.wrongAnswers.append(self.answer+1)
        self.wrongAnswers.append(self.answer+2)
        self.wrongAnswers.append(self.answer-1)
        self.wrongAnswers.append(self.answer-2)    
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ2(self):
        '''e.g.
        12 + 3 = 
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemType2"
        self.grade = 1
        self.CheckAnswerType = 1

        self.number1 = randint(1,19)
        self.number2 = randint(1,19)
        self.answer = self.number1 + self.number2
        while self.answer<10 or self.answer >= 20:
            self.number1 = randint(1,19)
            self.number2 = randint(1,19)
            self.answer = self.number1 + self.number2
        
        self.problem = str(self.number1)+" + "+str(self.number2)+" ="
        
        self.template = "MCQTypeProblems.html"
        
        '''List of wrong answers is same as the list of numbers displayed'''
        self.wrongAnswers = []
        
        self.wrongAnswers.append(self.answer+1)
        self.wrongAnswers.append(self.answer+2)
        self.wrongAnswers.append(self.answer-1)
        self.wrongAnswers.append(self.answer-2)    
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,str(self.answer),self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ3(self):
        '''e.g.
        Find the missing number: 
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemType3"
        self.grade = 1
        self.CheckAnswerType = 1

        self.StartingNumber = randint(1,5)
        self.Skip = randint(1,5)
        self.MissingNumberIndex = randint(0,4)
        self.numbers = []
        
        for i in range(5):
            self.numbers.append(self.StartingNumber+i*self.Skip)
        
        self.answer = self.numbers[self.MissingNumberIndex]
        
        self.problem = "Find the missing number:<br><br>"
        for i in range(5):
            if i!=self.MissingNumberIndex:
                self.problem = self.problem + str(self.numbers[i])+"&nbsp;&nbsp;&nbsp;&nbsp;"
            else: 
                self.problem = self.problem + "?&nbsp;&nbsp;&nbsp;&nbsp;"
        
        self.template = "MCQTypeProblems.html"
        
        '''List of wrong answers is same as the list of numbers displayed'''
        self.wrongAnswers = []
        
        self.wrongAnswers.append(self.answer+1)
        self.wrongAnswers.append(self.answer+2)
        self.wrongAnswers.append(self.answer-1)
        self.wrongAnswers.append(self.answer-2)
        for i in range(len(self.numbers)):
            if self.numbers[i] not in self.wrongAnswers:
                self.wrongAnswers.append(self.numbers[i])    
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ4(self):
        '''e.g.
        Find the missing number: 
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemType4"
        self.grade = 1
        self.CheckAnswerType = 1

        self.StartingNumber = randint(1,5)
        self.Skip = randint(1,5)
        self.MissingNumberIndex = randint(0,4)
        self.numbers = []
        
        for i in range(5):
            self.numbers.append(self.StartingNumber+i*self.Skip)
        
        self.numbers.reverse()
        
        self.answer = self.numbers[self.MissingNumberIndex]        
        
        self.problem = "Find the missing number:<br><br>"
        for i in range(5):
            if i!=self.MissingNumberIndex:
                self.problem = self.problem + str(self.numbers[i])+"&nbsp;&nbsp;&nbsp;&nbsp;"
            else: 
                self.problem = self.problem + "?&nbsp;&nbsp;&nbsp;&nbsp;"
        
        self.template = "MCQTypeProblems.html"
        
        '''List of wrong answers is same as the list of numbers displayed'''
        self.wrongAnswers = []
        
        self.wrongAnswers.append(self.answer+1)
        self.wrongAnswers.append(self.answer+2)
        if self.answer-1>0:
            self.wrongAnswers.append(self.answer-1)
        if self.answer-2>0:
            self.wrongAnswers.append(self.answer-2)
        for i in range(len(self.numbers)):
            if self.numbers[i] not in self.wrongAnswers:
                self.wrongAnswers.append(self.numbers[i])    
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)
       
    def checkAnswer(self,template,answer,Input,CheckAnswerType):
        if CheckAnswerType == 1:
            try:
                return int(answer)==int(Input)
            except ValueError:
                return False        