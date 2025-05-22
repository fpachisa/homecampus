'''
Created on Sep 26, 2011

Module: SimplifyingAlgebra
Generates "Simplifying algebraic expressions" problems for Primary 6

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random
from random import randint
import string
import logging

class SimplifyingAlgebra:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"easy":[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),
                                    self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4()],
                            "medium":[self.GenerateProblemTypeMCQ5()],
                            }
        try:
            return random.choice(self.ProblemType[level])
        except KeyError:
            return random.choice(random.choice(self.ProblemType.values()))
        #return self.GenerateProblemTypeMCQ5()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1"],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemTypeMCQ5",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1()],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3()],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4()],
                                    5:[self.GenerateProblemTypeMCQ5()],
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
        #return self.GenerateProblemTypeMCQ5()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g: 3k + 2k = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z'])
        self.problem = "Simplify the following algebraic expression:<br><br>"
        self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i> + "+str(self.number2)+"<i>"+self.variable+"</i> = "
        
        self.answer = str(self.number1+self.number2)+self.variable

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType1(self,problem,answer,number1,number2,variable):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  str(number1)+"<i>"+variable+"</i> + "+str(number2)+"<i>"+variable+"</i> = "
        self.solution_text = self.solution_text +"("+str(number1)+" + "+str(number2)+")<i>"+variable+"</i><br><br>"
        self.solution_text = self.solution_text + " = "+str(answer)
        self.solution_text = self.solution_text + '<br><br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):
        '''e.g: 3k - 2k = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z'])
        
        self.answer = str(self.number1)+self.variable
        self.number1 = self.number1 + self.number2
        self.problem = "Simplify the following algebraic expression:<br><br>"
        self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i>"+" &minus; "+str(self.number2)+"<i>"+self.variable+"</i>"+" = "       
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType2(self,problem,answer,number1,number2,variable):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  str(number1)+"<i>"+variable+"</i> &minus; "+str(number2)+"<i>"+variable+"</i> = "
        self.solution_text = self.solution_text +"("+str(number1)+" &minus; "+str(number2)+")<i>"+variable+"</i><br><br>"
        self.solution_text = self.solution_text + " = "+str(answer)
        self.solution_text = self.solution_text + '<br><br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):
        '''e.g: 3k + 2k - 4k = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z'])
        
        self.answer = str(self.number1)+self.variable
        self.number1 = self.number1 + self.number2
        self.number3 = randint(2,self.number1-1)
        self.number1 = self.number1 - self.number3
        self.problem = "Simplify the following algebraic expression:<br><br>"
        self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i>"+" + "+str(self.number3)+"<i>"+self.variable+"</i>"+" &minus; "+str(self.number2)+"<i>"+self.variable+"</i>"+" = "      
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.number3,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType3(self,problem,answer,number1,number2,number3,variable):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "Using the rule of order of operations, do all addition and/or subtraction from left to right.<br><br>"
        self.solution_text = self.solution_text +"<font style=color:red>" +str(number1)+"<i>"+variable+"</i>"+" + "+str(number3)+"<i>"+variable+"</i></font>"+" &minus; "+str(number2)+"<i>"+variable+"</i><br><br>"
        self.solution_text = self.solution_text + " = <font style=color:red>" +str(number1+number3)+"<i>"+variable+"</i></font> &minus; "+str(number2)+"<i>"+variable+"</i><br><br>"
        self.solution_text = self.solution_text + " = "+str(answer)
        self.solution_text = self.solution_text + '<br><br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'         
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4(self):
        '''e.g: 3k - 2k + 4k = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(3,10)
        self.number2 = randint(2,self.number1-1)
        self.number3 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z'])

        self.problem = "Simplify the following algebraic expression:<br><br>"
        self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i>"+" &minus; "+str(self.number2)+"<i>"+self.variable+"</i>"+" + "+str(self.number3)+"<i>"+self.variable+"</i>"+" = "
        
        self.answer = str(self.number1-self.number2+self.number3)+self.variable        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.number3,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType4(self,problem,answer,number1,number2,number3,variable):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "Using the rule of order of operations, do all addition and/or subtraction from left to right.<br><br>"
        self.solution_text = self.solution_text +"<font style=color:red>" +str(number1)+"<i>"+variable+"</i>"+" &minus; "+str(number2)+"<i>"+variable+"</i></font>"+" + "+str(number3)+"<i>"+variable+"</i><br><br>"
        self.solution_text = self.solution_text + " = <font style=color:red>"+str(number1-number2)+"<i>"+variable+"</i></font> + "+str(number3)+"<i>"+variable+"</i><br><br>"
        self.solution_text = self.solution_text + " = "+str(answer)
        self.solution_text = self.solution_text + '<br><br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
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
        '''e.g: 3k + 2k = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z'])
        self.problem = "Simplify the following algebraic expression:<br><br>"
        self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i> + "+str(self.number2)+"<i>"+self.variable+"</i> = "
        
        self.answer = str(self.number1+self.number2)+"<i>"+self.variable+"</i>"
        
        self.problem_type = "ProblemTypeMCQ1"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.number1+self.number2+1)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number1+self.number2-1)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number1+self.number2+2)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number1+self.number2-2)+"<i>"+self.variable+"</i>")

        self.answer1 = self.answer
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def GenerateProblemTypeMCQ2(self):
        '''e.g: 3k - 2k = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z'])
        
        self.answer = str(self.number1)+"<i>"+self.variable+"</i>"
        self.number1 = self.number1 + self.number2
        self.problem = "Simplify the following algebraic expression:<br><br>"
        self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i>"+" &minus; "+str(self.number2)+"<i>"+self.variable+"</i>"+" = "
        
        self.problem_type = "ProblemTypeMCQ2"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.number1-self.number2+1)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number1-self.number2-1)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number1-self.number2+2)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number1-self.number2-2)+"<i>"+self.variable+"</i>")

        self.answer1 = self.answer
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ3(self):
        '''e.g: 3k + 2k - 4k = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z'])
        
        self.answer = str(self.number1)+"<i>"+self.variable+"</i>"
        self.number1 = self.number1 + self.number2
        self.number3 = randint(2,self.number1-1)
        self.number1 = self.number1 - self.number3
        self.problem = "Simplify the following algebraic expression:<br><br>"
        self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i>"+" + "+str(self.number3)+"<i>"+self.variable+"</i>"+" &minus; "+str(self.number2)+"<i>"+self.variable+"</i>"+" = "      
        
        self.problem_type = "ProblemTypeMCQ3"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.number1+self.number3-self.number2+1)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number1+self.number3-self.number2-1)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number1+self.number3-self.number2+2)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number1+self.number3+self.number2)+"<i>"+self.variable+"</i>")

        self.answer1 = self.answer
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.number3,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ4(self):
        '''e.g: 3k - 2k + 4k = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(3,10)
        self.number2 = randint(2,self.number1-1)
        self.number3 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z'])

        self.problem = "Simplify the following algebraic expression:<br><br>"
        self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i>"+" &minus; "+str(self.number2)+"<i>"+self.variable+"</i>"+" + "+str(self.number3)+"<i>"+self.variable+"</i>"+" = "
        
        self.answer = str(self.number1-self.number2+self.number3)+"<i>"+self.variable+"</i>"
                
        self.problem_type = "ProblemTypeMCQ4"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.number1+self.number3-self.number2+1)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number1+self.number3-self.number2-1)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number1+self.number3-self.number2+2)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number1+self.number3+self.number2)+"<i>"+self.variable+"</i>")

        self.answer1 = self.answer
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.number3,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ5(self):
        '''e.g: 3k + 4 - k - 1 = '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.number1 = randint(3,10)
        self.number2 = randint(1,self.number1-2)
        self.number3 = randint(3,10)
        self.number4 = randint(1,self.number3-2)
        self.variable = random.choice(['a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z'])

        if self.number2 == 1:
            self.problem = "Simplify the following algebraic expression:<br><br>"
            self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i> + "+str(self.number3)+" &minus; <i>"+self.variable+"</i> &minus; "+str(self.number4)+" = "
            self.flag = 1
        else:
            self.problem = "Simplify the following algebraic expression:<br><br>"
            self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i> + "+str(self.number3)+" &minus; "+str(self.number2)+"<i>"+self.variable+"</i> &minus; "+str(self.number4)+" = "
            self.flag = 2
        
        if self.number1-self.number2 == 1:           
            self.answer1 = "<i>"+self.variable+"</i> + "+ str(self.number3-self.number4)        
            self.answer2 = str(self.number3-self.number4) +" + <i>"+self.variable+"</i>"
        else:
            self.answer1 = str(self.number1-self.number2)+"<i>"+self.variable+"</i> + "+ str(self.number3-self.number4)        
            self.answer2 = str(self.number3-self.number4) +" + "+ str(self.number1-self.number2)+"<i>"+self.variable+"</i>"

        
        self.answer = random.choice([self.answer1,self.answer2])
        self.problem_type = "ProblemTypeMCQ5"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.number1-self.number2-1)+"<i>"+self.variable +"</i> + "+ str(self.number3-self.number4))
        self.wrongAnswers.append(str(self.number1-self.number2)+"<i>"+self.variable +"</i> + "+ str(self.number3-self.number4+1))
        self.wrongAnswers.append(str(self.number3-self.number4-1) +" + "+ str(self.number1-self.number2)+"<i>"+self.variable+"</i>")
        self.wrongAnswers.append(str(self.number3-self.number4) +" + "+ str(self.number1-self.number2+1)+"<i>"+self.variable+"</i>")    
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.variable,self.flag,self.answer1,self.answer2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)

    def ExplainType5(self,problem,answer,number1,number2,number3,number4,variable,flag,answer1,answer2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "Rearrange the known and unknown numbers in the algebraic expression.<br><br>"
        if flag==1:
            self.solution_text = self.solution_text +"<font style=color:red>"+ str(number1)+"<i>"+variable+"</i></font> + "+str(number3)+" <font style=color:red>&minus; <i>"+variable+"</i></font> &minus; "+str(number4)+"<br><br>"
            self.solution_text = self.solution_text +" = "+"<font style=color:red>"+ str(number1)+"<i>"+variable+"</i> &minus; "+"<i>"+variable+"</i></font> + "+str(number3)+" &minus; "+str(number4)+"<br><br>"            
        elif flag ==2:
            self.solution_text = self.solution_text +"<font style=color:red>"+ str(number1)+"<i>"+variable+"</i></font> + "+str(number3)+" <font style=color:red>&minus; "+str(number2)+"<i>"+variable+"</i></font> &minus; "+str(number4)+"<br><br>"
            self.solution_text = self.solution_text +" = "+"<font style=color:red>"+ str(number1)+"<i>"+variable+"</i> &minus; "+str(number2)+"<i>"+variable+"</i></font> + "+str(number3)+" &minus; "+str(number4)+"<br><br>"
        self.solution_text = self.solution_text + " = "+str(answer1)+" &nbsp;&nbsp;or&nbsp;&nbsp; "+str(answer2)
        self.solution_text = self.solution_text + '<br><br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckType):
        if CheckType==1:
            try:
                InputAnswer= string.join(InputAnswer.split(),"")
                logging.info("answer = "+str(answer))
                logging.info("input = "+str(InputAnswer))
                return (str(answer)==str(InputAnswer))
            except ValueError:
                return False
        if CheckType==2:
            try:
                answer= string.join(answer.split(),"")
                return (str(answer)==str(InputAnswer))
            except ValueError:
                return False               