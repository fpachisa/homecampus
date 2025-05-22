'''
Created on Oct 12, 2011

Module: WholePart
Generates "Finding whole given part and percentage" problems for Primary 6

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

class WholePart:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"easy":[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                            "medium":[self.GenerateProblemType2(),self.GenerateProblemType3(),
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
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g: Find the number:
                If 5% of it is 20. '''
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.numbers = random.choice([(2,50),(4,25),(5,20),(10,10)])
        self.number1 = self.numbers[1] * randint(1,10)
        self.number2 = self.numbers[0] * randint(1,10)
        self.number3 = random.randrange(200,900,100)
        self.number4 = randint(2,99)
        
        if randint(1,2) == 1:
            self.whole = self.number1
            self.percent = self.number2
        else:
            self.whole = self.number3
            self.percent = self.number4
        self.part = self.whole * self.percent / 100
        
        self.problem1 = "Find the number if "+str(self.percent)+"% of that number is "+str(self.part)+"."
        self.problem2 = str(self.percent)+"% of a number is "+str(self.part)+". What is the number?"
        self.problem = random.choice([self.problem1, self.problem2])
        
        self.answer = self.whole
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.part,self.percent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType1(self,problem,answer,part,percent):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<table>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>"+str(percent)+"%</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(part)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1%</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(part)+" &divide; "+str(percent)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>100%</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(part)+" &divide; "+str(percent)+" &times; 100</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='text-align:right'>=</td><td style='text-align:left'>"+str(answer)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td colspan='3' style='text-align:left'><br>The number is "+str(answer)+".</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Percentage/Finding-Whole-Given-Part-and-Percentage" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):
        '''e.g: Find the number:
                If 5% of it is 20. '''
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.percent = randint(2,99)
        self.part = randint(5,100)
        self.whole = float(self.part) * 100 / float(self.percent)
        
        self.problem1 = "Find the number if "+str(self.percent)+"% of that number is "+str(self.part)+".<br><br><font style='font-size:0.8em'>(Write your answer correct to two decimal places.)</font><br>"
        self.problem2 = str(self.percent)+"% of a number is "+str(self.part)+". What is the number?<br><br><font style='font-size:0.8em'>(Round off your answer to two decimal places.)</font><br>"
        self.problem = random.choice([self.problem1, self.problem2])
        
        self.answer = round(self.whole,2)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.part,self.percent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType2(self,problem,answer,part,percent):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        self.solution_text = "<table>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>"+str(percent)+"%</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(part)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1%</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(part)+" &divide; "+str(percent)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>100%</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(part)+" &divide; "+str(percent)+" &times; 100</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='text-align:right'>=</td><td style='text-align:left'>"+str(answer)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td colspan='3' style='text-align:left'><br>The number is "+str(answer)+".</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Percentage/Finding-Whole-Given-Part-and-Percentage" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):
        '''e.g: 5% of x is 200. Find x. '''
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.percent = randint(2,99)
        self.part = randint(5,100)
        self.whole = float(self.part) * 100 / float(self.percent)
        self.variable = random.choice(['b','c','d','f','g','h','j','k','m','n','p','q','r','s','t','v','w','x','y','z'])

        self.problem1 = str(self.percent)+"% of <i>"+self.variable+"</i> is "+str(self.part)+". Find the value of <i>"+str(self.variable)+"</i>.<br><br>"
        self.problem1 = self.problem1 + "<font style='font-size:0.8em'>(Write your answer correct to two decimal places.)</font>"

        self.problem2 = "Find the value of <i>"+str(self.variable)+"</i> if "+str(self.percent)+"% of <i>"+self.variable+"</i> is "+str(self.part)+".<br><br>"
        self.problem2 = self.problem2 + "<font style='font-size:0.8em'>(Round off your answer to two decimal places.)</font>"
        
        self.problem = random.choice([self.problem1, self.problem2])

        self.answer = round(self.whole,2)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.part,self.percent,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType3(self,problem,answer,part,percent,variable):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<table>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>"+str(percent)+"% of <i>"+variable+"</i></td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(part)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1% of <i>"+variable+"</i></td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(part)+" &divide; "+str(percent)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>100% of <i>"+variable+"</i></td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(part)+" &divide; "+str(percent)+" &times; 100</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='text-align:right'>=</td><td style='text-align:left'>"+str(answer)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td colspan='3' style='text-align:left'>Hence, <i>"+variable+"</i> is "+str(answer)+".</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Percentage/Finding-Whole-Given-Part-and-Percentage" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

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
        '''e.g: Find the number:
                If 5% of it is 20. '''
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.numbers = random.choice([(2,50),(4,25),(5,20),(10,10)])
        self.number1 = self.numbers[1] * randint(1,10)
        self.number2 = self.numbers[0] * randint(1,10)
        self.number3 = random.randrange(200,900,100)
        self.number4 = randint(2,99)
        
        if randint(1,2) == 1:
            self.whole = self.number1
            self.percent = self.number2
        else:
            self.whole = self.number3
            self.percent = self.number4
        self.part = self.whole * self.percent / 100
        
        self.problem1 = "Find the number if "+str(self.percent)+"% of that number is "+str(self.part)+"."
        self.problem2 = str(self.percent)+"% of a number is "+str(self.part)+". What is the number?"
        self.problem = random.choice([self.problem1, self.problem2])
        
        self.answer = self.whole
        
        self.problem_type = "ProblemTypeMCQ1"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.part,self.percent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def GenerateProblemTypeMCQ2(self):
        '''e.g: Find the number:
                If 5% of it is 20. '''
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.percent = randint(2,99)
        self.part = randint(5,100)
        self.whole = float(self.part) * 100 / float(self.percent)
        
        '''self.problem = "Find the number:<br><br>"
        self.problem = self.problem + "If "+str(self.percent)+"% of that number is "+str(self.part)+".<br><br>"'''
        
        self.problem1 = "Find the number if "+str(self.percent)+"% of that number is "+str(self.part)+".<br><br><font style='font-size:0.8em'>(Round off your answer correct to two decimal places.)</font><br>"
        self.problem2 = str(self.percent)+"% of a number is "+str(self.part)+". What is the number?<br><br><font style='font-size:0.8em'>(Find your answer correct to two decimal places.)</font><br>"
        self.problem = random.choice([self.problem1, self.problem2])
        
        self.answer = round(self.whole,2)
        
        self.problem_type = "ProblemTypeMCQ2"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+.10))
        self.wrongAnswers.append(str(self.answer+.01))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.part,self.percent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def GenerateProblemTypeMCQ3(self):
        '''e.g: 5% of x is 200. Find x. '''
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.percent = randint(2,99)
        self.part = randint(5,100)
        self.whole = float(self.part) * 100 / float(self.percent)
        self.variable = random.choice(['b','c','d','f','g','h','j','k','m','n','p','q','r','s','t','v','w','x','y','z'])
                
        self.problem1 = str(self.percent)+"% of <i>"+self.variable+"</i> is "+str(self.part)+". Find the value of <i>"+str(self.variable)+"</i>.<br><br>"
        self.problem1 = self.problem1 + "<font style='font-size:0.8em'>(Give your answer correct to two decimal places.)</font>"

        self.problem2 = "Find the value of <i>"+str(self.variable)+"</i> if "+str(self.percent)+"% of <i>"+self.variable+"</i> is "+str(self.part)+".<br><br>"
        self.problem2 = self.problem2 + "<font style='font-size:0.8em'>(Round off your answer to two decimal places.)</font>"
        
        self.problem = random.choice([self.problem1, self.problem2])

        self.answer = round(self.whole,2)
        
        self.problem_type = "ProblemTypeMCQ3"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+.10))
        self.wrongAnswers.append(str(self.answer+.01))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.part,self.percent,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def checkAnswer(self,template,answer,AnswerInput,CheckType):
        if CheckType==1:
            try:
                return (int(answer)==int(AnswerInput))
            except ValueError:
                return False
        elif CheckType==2:
            try:
                return (float(answer)==float(AnswerInput))
            except ValueError:
                return False                          