'''
Created on Feb 19, 2012

Module: MultiplyProperImproperFractions
Generates "Multiplying proper and improper fractions" problems for Primary 4

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

class MultiplyProperImproperFractions:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        self.RandomQ = randint(1,10)
        #70% of the time it will generate MCQs
        if self.RandomQ > 3:
            self.ProblemType = random.choice([self.GenerateProblemTypeMCQ1(),self.GenerateProblemTypeMCQ2()])
        else:
            self.ProblemType = random.choice([self.GenerateProblemType1(),self.GenerateProblemType2()])
        return self.ProblemType
        #return self.GenerateProblemTypeMCQ2()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
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
        #return self.GenerateProblemTypeMCQ2()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = randint(3,12)
        self.numerator = randint(1,self.denominator-1)        
        self.multiplier = randint(2,8)
        self.number = self.multiplier * self.denominator

        self.problem = "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td>Find the value of&nbsp;</td>"
        self.problem = self.problem + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td> &nbsp;of&nbsp;"+str(self.number)+"<td>"
        self.problem = self.problem + "</tr></table>"
        
        self.answer = self.numerator*self.multiplier
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.numerator,self.denominator,self.multiplier,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,}            
    
    def ExplainType1(self,problem,answer,numerator,denominator,multiplier,number):
        self.answer_text = "The correct answer is:&nbsp;"+str(answer)
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator))+str(numerator)+"&nbsp;"*len(str(denominator))+"</u><br>&nbsp;"+str(denominator)+"</td>"
        self.solution_text = self.solution_text + "<td> &nbsp;of&nbsp;"+str(self.number)+"<td>"
        self.solution_text = self.solution_text + "<td> &nbsp;=&nbsp; <td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator))+str(numerator)+"&nbsp;"*len(str(denominator))+"</u><br>&nbsp;<del>"+str(denominator)+"</del>1</td>"
        self.solution_text = self.solution_text + "<td> &nbsp;&times;&nbsp;<del>"+str(self.number)+"</del>"+str(multiplier)+"<td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        self.solution_text = self.solution_text + "= "+str(numerator)+" &times; "+str(multiplier)+"<br><br>"
        self.solution_text = self.solution_text + "= "+str(answer)+"<br><br>"
        self.solution_text = self.solution_text + "Hence the correct answer is &nbsp;<i><b>"+str(answer)+"</b></i>"        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType2(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = randint(3,12)
        self.numerator = randint(self.denominator+1,24)        
        self.multiplier = randint(2,8)
        self.number = self.multiplier * self.denominator

        self.problem = "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td>Find the value of&nbsp;</td>"
        self.problem = self.problem + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td> &nbsp;of&nbsp;"+str(self.number)+"<td>"
        self.problem = self.problem + "</tr></table>"
        
        self.answer = self.numerator*self.multiplier
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.numerator,self.denominator,self.multiplier,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,}            
    
    def ExplainType2(self,problem,answer,numerator,denominator,multiplier,number):
        self.answer_text = "The correct answer is:&nbsp;"+str(answer)
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator))+str(numerator)+"&nbsp;"*len(str(denominator))+"</u><br>"+"&nbsp;"*len(str(numerator))+str(denominator)+"</td>"
        self.solution_text = self.solution_text + "<td> &nbsp;of&nbsp;"+str(self.number)+"<td>"
        self.solution_text = self.solution_text + "<td> &nbsp;=&nbsp; <td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(denominator))+str(numerator)+"&nbsp;"*len(str(denominator))+"</u><br>&nbsp;<del>"+str(denominator)+"</del>1</td>"
        self.solution_text = self.solution_text + "<td> &nbsp;&times;&nbsp;<del>"+str(self.number)+"</del>"+str(multiplier)+"<td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        self.solution_text = self.solution_text + "= "+str(numerator)+" &times; "+str(multiplier)+"<br><br>"
        self.solution_text = self.solution_text + "= "+str(answer)+"<br><br>"
        self.solution_text = self.solution_text + "Hence the correct answer is &nbsp;<i><b>"+str(answer)+"</b></i>"        
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
                ,'value3':self.value3,'value4':self.value4,'explain':explain
                ,'problem_type':problem_type,'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}       

    def GenerateProblemTypeMCQ1(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.CheckAnswerType = 1            
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = randint(3,12)
        self.numerator = randint(1,self.denominator-1)        
        self.multiplier = randint(2,8)
        self.number = self.multiplier * self.denominator

        self.problem = "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td>Find the value of&nbsp;</td>"
        self.problem = self.problem + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td> &nbsp;of&nbsp;"+str(self.number)+"<td>"
        self.problem = self.problem + "</tr></table>"
        
        self.answer = self.numerator*self.multiplier

        self.wrongAnswers = []    
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer+4))
        self.wrongAnswers.append(str(self.answer-2))
        self.wrongAnswers.append(str(self.answer+10))
        self.wrongAnswers.append(str(self.answer+5))
                                   
        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ1"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.numerator,self.denominator,self.multiplier,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ2(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.CheckAnswerType = 1            
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = randint(3,12)
        self.numerator = randint(self.denominator+1,24)        
        self.multiplier = randint(2,8)
        self.number = self.multiplier * self.denominator

        self.problem = "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td>Find the value of&nbsp;</td>"
        self.problem = self.problem + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td> &nbsp;of&nbsp;"+str(self.number)+"<td>"
        self.problem = self.problem + "</tr></table>"
        
        self.answer = self.numerator*self.multiplier

        self.wrongAnswers = []    
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer+4))
        self.wrongAnswers.append(str(self.answer-2))
        self.wrongAnswers.append(str(self.answer+10))
        self.wrongAnswers.append(str(self.answer+5))
                                   
        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ2"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.numerator,self.denominator,self.multiplier,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)
                  
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
        if CheckAnswerType == 1:
                try:
                    return int(answer)==int(InputAnswer)
                except ValueError:
                    return False