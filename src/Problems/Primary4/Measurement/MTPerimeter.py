'''
Created on Mar 22, 2012
Module: MTPerimeter
Generates the "Calculating Perimeter of Rectangles and Squares" problems for Primary 4

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

class MTPerimeter:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemTypeMCQ2",],
                            3:["ProblemType3",],
                            4:["ProblemTypeMCQ1",],
                            5:["ProblemType2",],
                            6:["ProblemTypeMCQ3",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemTypeMCQ1(),],
                                    5:[self.GenerateProblemType2(),],
                                    6:[self.GenerateProblemTypeMCQ3(),],
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
        '''e.g.:
        The perimeter of a rectangle is 18 cm and lenght is 6 cm. Find its breadth.'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.breadth = randint(3,30)
        self.length = randint(self.breadth+5,35)       
        
        self.perimeter = 2 * (self.length + self.breadth)
        self.problem = "The perimeter of a rectangle is "+str(self.perimeter)+" cm and length is "+str(self.length)+" cm.<br><br>"
        self.problem = self.problem + "Find its breadth."
        
        self.answer = self.breadth
        
        self.template = "EnterTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.length,self.breadth,self.perimeter)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":"cm"}            

    def ExplainType1(self,problem,answer,length,breath,perimeter):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" cm"
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Perimeter = length + breadth + length + breadth<br><br>"
        self.solution_text = self.solution_text + "Perimeter &divide; 2 = length + breadth<br><br>"
        self.solution_text = self.solution_text + "Given perimeter = "+str(perimeter)+" cm and length = "+str(length)+" cm<br><br>"
        self.solution_text = self.solution_text + "length + breadth = "+str(perimeter)+" &divide; 2<br><br>"
        self.solution_text = self.solution_text + "length + breadth = "+str(perimeter/2)+"<br><br>"
        self.solution_text = self.solution_text + "Therefore, breadth = "+str(perimeter/2)+" - "+str(length)+" cm = <b><i>"+str(answer)+" cm</b></i><br><br>"        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g.:
        The perimeter of a rectangle is 18 cm and breadth is 6 cm. Find its length.'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.breadth = randint(3,30)
        self.length = randint(self.breadth+5,35)

        self.perimeter = 2 * (self.length + self.breadth)
        self.problem = "The perimeter of a rectangle is "+str(self.perimeter)+" cm and breadth is "+str(self.breadth)+" cm.<br><br>"
        self.problem = self.problem + "Find its length."
        
        self.answer = self.length
        
        self.template = "EnterTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.length,self.breadth,self.perimeter)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":"cm"}            

    def ExplainType2(self,problem,answer,length,breadth,perimeter):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" cm"
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Perimeter = length + breadth + length + breadth<br><br>"
        self.solution_text = self.solution_text + "Perimeter &divide; 2 = length + breadth<br><br>"
        self.solution_text = self.solution_text + "Given perimeter = "+str(perimeter)+" cm and breadth = "+str(breadth)+" cm<br><br>"
        self.solution_text = self.solution_text + "length + breadth = "+str(perimeter)+" &divide; 2<br><br>"
        self.solution_text = self.solution_text + "length + breadth = "+str(perimeter/2)+"<br><br>"
        self.solution_text = self.solution_text + "Therefore, length = "+str(perimeter/2)+" - "+str(breadth)+" cm = <b><i>"+str(answer)+" cm</b></i><br><br>"        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g.:
        The perimeter of a square is 16 cm. Find length of a side.'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.length = randint(3,30)

        self.perimeter = 4 * self.length
        self.problem = "The perimeter of a square is "+str(self.perimeter)+" cm. Find length of a side."
        
        self.answer = self.length
        
        self.template = "EnterTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.length,self.perimeter)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":"cm"}            

    def ExplainType3(self,problem,answer,length,perimeter):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" cm"
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Perimeter of a square = 4 &times; length<br><br>"
        self.solution_text = self.solution_text + "Therefore, length = perimeter &divide; 4<br><br>"
        self.solution_text = self.solution_text + "length = "+str(perimeter)+" &divide; 4 = <b><i>"+str(answer)+" cm</b></i><br><br>"       
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
            self.answer1 = str(wrongAnswers[0])+" cm"
            self.answer2 = str(wrongAnswers[1])+" cm"
            self.answer3 = str(wrongAnswers[2])+" cm"
            self.answer4 = str(wrongAnswers[3])+" cm"  
        except IndexError:
            pass
        try:
            self.value1 = str(wrongAnswers[0])
            self.value2 = str(wrongAnswers[1])
            self.value3 = str(wrongAnswers[2])
            self.value4 = str(wrongAnswers[3])
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'answer4':self.answer4,'value1':self.value1,'value2':self.value2
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type,
                'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}      

    def GenerateProblemTypeMCQ1(self):        
        '''e.g.:
        The perimeter of a rectangle is 18 cm and lenght is 6 cm. Find its breadth.'''
                
        self.problem_type = "ProblemTypeMCQ1"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.breadth = randint(3,30)
        self.length = randint(self.breadth+5,35)       
        
        self.perimeter = 2 * (self.length + self.breadth)
        self.problem = "The perimeter of a rectangle is "+str(self.perimeter)+" cm and length is "+str(self.length)+" cm.<br><br>"
        self.problem = self.problem + "Find its breadth."
        
        self.answer = self.breadth       
        
        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        for i in range(2):
            self.wrongAnswers.append(self.answer+i+1)
            self.wrongAnswers.append(self.answer-i-1)
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.length,self.breadth,self.perimeter)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ2(self):        
        '''e.g.:
        The perimeter of a rectangle is 18 cm and breadth is 6 cm. Find its length.'''
                
        self.problem_type = "ProblemTypeMCQ2"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4

        self.breadth = randint(3,30)
        self.length = randint(self.breadth+5,35)

        self.perimeter = 2 * (self.length + self.breadth)
        self.problem = "The perimeter of a rectangle is "+str(self.perimeter)+" cm and breadth is "+str(self.breadth)+" cm.<br><br>"
        self.problem = self.problem + "Find its length."
        
        self.answer = self.length
               
        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        for i in range(3):
            self.wrongAnswers.append(self.answer+i+1)
            self.wrongAnswers.append(self.answer-i-1)
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.length,self.breadth,self.perimeter)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ3(self):        
        '''e.g.:
        The perimeter of a square is 16 cm. Find length of a side.'''
                
        self.problem_type = "ProblemTypeMCQ3"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.length = randint(3,30)

        self.perimeter = 4 * self.length
        self.problem = "The perimeter of a square is "+str(self.perimeter)+" cm. Find length of a side."
        
        self.answer = self.length
               
        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        for i in range(2):
            self.wrongAnswers.append(self.answer+i+1)
            self.wrongAnswers.append(self.answer-i-1)
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.length,self.perimeter)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)
                                                                                                                                                           
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False