'''
Created on Jan 20, 2012

Module: FactorMultiple
Generates "Factors and multiples of whole numbers" problems for Primary 4

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
from Utils import Factors
from Utils import LcmGcf
import string

class FactorMultiple:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        random = randint(1,3)
        if random==1:
            if randint(1,2)==1:
                return self.GenerateProblemType1()
            else:
                return self.GenerateProblemTypeMCQ1()
        elif random==2:
            if randint(1,2)==1:
                return self.GenerateProblemType2()
            else:
                return self.GenerateProblemTypeMCQ2()
        else:
            if randint(1,2)==1:
                return self.GenerateProblemType3()
            else:
                return self.GenerateProblemTypeMCQ3()
        #return self.GenerateProblemTypeMCQ3()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemType4",],
                            5:["ProblemType5",],6:["ProblemType6",],7:["ProblemType7",],8:["ProblemType8",],}
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],}
        
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
        #return self.GenerateProblemType4()

    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''Is 4 a factor of 16?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.multiplier = randint(2,10)
        self.number = randint(2,9)
        self.product = self.number * self.multiplier
        self.problem = "Is %d a factor of %d?"%(self.number,self.product)
        
        self.answer = "Yes"
        self.answer1 = "Yes"
        self.answer2 = "No"
        
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number,self.product)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'value1':self.answer1,'value2':self.answer2,'answer1':self.answer1,'answer2':self.answer2}

    def ExplainType1(self,problem,answer,number,product):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + str(product)+" &divide; "+str(number)+" = "+str(product/number)+"<br><br>"
        self.solution_text = self.solution_text + "Since, "+str(product)+" can be divided exactly by "+str(number)+"."
        self.solution_text = self.solution_text + "<br><br><i><b>"+str(number)+" is a factor of "+str(product)+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain 

    def GenerateProblemType2(self):
        '''Is 5 a factor of 37?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.number = randint(2,9)
        self.product = randint(15,99)
        self.problem = "Is %d a factor of %d?"%(self.number,self.product)
        
        if self.product % self.number == 0:
            self.answer = "Yes"
        else:
            self.answer = "No"
        self.answer1 = "Yes"
        self.answer2 = "No"
        
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.product)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'value1':self.answer1,'value2':self.answer2,'answer1':self.answer1,'answer2':self.answer2}

    def ExplainType2(self,problem,answer,number,product):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        div,mod = divmod(product,number)
        if mod == 0:
            self.solution_text = self.solution_text + str(product)+" &divide; "+str(number)+" = "+str(product/number)+"<br><br>"
            self.solution_text = self.solution_text + "Since, "+str(product)+" can be divided exactly by "+str(number)+"."
            self.solution_text = self.solution_text + "<br><br><i><b>"+str(number)+" is a factor of "+str(product)+"<b></i>"
        else:
            self.solution_text = self.solution_text + str(product)+" &divide; "+str(number)+" = "+str(div)+" R"+str(mod)+"<br><br>"
            self.solution_text = self.solution_text + "Since, "+str(product)+" cannot be divided exactly by "+str(number)+"."
            self.solution_text = self.solution_text + "<br><br><i><b>"+str(number)+" is not a factor of "+str(product)+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):
        '''Write all factors of 48.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.number = randint(10,99)
        self.problem = "Write all factors of %d."%(self.number)
        self.problem = self.problem + "<br>(Write all numbers separated by commas. For e.g. Write all factors of 8 as 1,2,4,8)"
        
        self.answer = Factors.Factors().find_factors(self.number)                
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,}

    def ExplainType3(self,problem,answer,number):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        for i in range(len(answer)/2):
            self.solution_text = self.solution_text + str(number)+" = "+str(answer[i])+" &times; "+str(answer[len(answer)-i-1])+"<br>"
        self.solution_text = self.solution_text + "<br>Therefore, the factors of "+str(number)+" are "+str(answer)
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4(self):
        '''What are the common factors of 48 and 64?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.numbers = [[random.randrange(8,96,4),random.randrange(8,96,4)],[random.randrange(10,100,2),random.randrange(10,100,2)],
                        [random.randrange(8,96,8),random.randrange(8,96,8),],[random.randrange(12,96,6),random.randrange(12,96,6)],
                        [random.randrange(10,100,5),random.randrange(10,100,5),],]
        self.NumberSet = random.choice(self.numbers)
        
        self.number1 = self.NumberSet[0]
        self.number2 = self.NumberSet[1]
        
        while self.number1 == self.number2:
            self.NumberSet = random.choice(self.numbers)
            self.number1 = self.NumberSet[0]
            self.number2 = self.NumberSet[1] 
                   
        self.problem = "What are the common factors of %d and %d."%(self.number1,self.number2)
        self.problem = self.problem + "<br>(Write all numbers separated by commas. For e.g. Common factors of 8 and 10 are 1,2)"
        
        self.answer = Factors.Factors().find_common_factors(self.number1, self.number2)                
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,}

    def ExplainType4(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        factor1 = Factors.Factors().find_factors(number1)
        factor2 = Factors.Factors().find_factors(number2)
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        for i in range(len(factor1)/2):
            self.solution_text = self.solution_text + str(number1)+" = "+str(factor1[i])+" &times; "+str(factor1[len(factor1)-i-1])+"<br>"
        self.solution_text = self.solution_text + "<br>The factors of "+str(number1)+" are "+str(factor1)+"<br><br>"
        for i in range(len(factor2)/2):
            self.solution_text = self.solution_text + str(number2)+" = "+str(factor2[i])+" &times; "+str(factor2[len(factor2)-i-1])+"<br>"
        self.solution_text = self.solution_text + "<br>The factors of "+str(number2)+" are "+str(factor2)+"<br><br>"
        self.solution_text = self.solution_text + "Therefore, the common factors of "+str(number1)+" and "+str(number2)+" are "+str(answer)
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain


    def GenerateProblemType5(self):
        '''Is 16 a multiple of 4?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.multiplier = randint(2,10)
        self.number = randint(2,9)
        self.product = self.number * self.multiplier
        self.problem = "Is %d a multiple of %d?"%(self.product,self.number)
        
        self.answer = "Yes"
        self.answer1 = "Yes"
        self.answer2 = "No"
        
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number,self.product)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'value1':self.answer1,'value2':self.answer2,'answer1':self.answer1,'answer2':self.answer2}

    def ExplainType5(self,problem,answer,number,product):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + str(product)+" &divide; "+str(number)+" = "+str(product/number)+"<br><br>"
        self.solution_text = self.solution_text + "Since, "+str(product)+" can be divided exactly by "+str(number)+"."
        self.solution_text = self.solution_text + "<br><br><i><b>"+str(product)+" is a multiple of "+str(number)+" or "+str(number)+" is a factor of "+str(product)+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain 

    def GenerateProblemType6(self):
        '''Is 37 a multiple of 5?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.number = randint(2,9)
        self.product = randint(15,99)
        self.problem = "Is %d a multiple of %d?"%(self.product,self.number)
        
        if self.product % self.number == 0:
            self.answer = "Yes"
        else:
            self.answer = "No"
        self.answer1 = "Yes"
        self.answer2 = "No"
        
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number,self.product)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'value1':self.answer1,'value2':self.answer2,'answer1':self.answer1,'answer2':self.answer2}

    def ExplainType6(self,problem,answer,number,product):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        div,mod = divmod(product,number)
        if mod == 0:
            self.solution_text = self.solution_text + str(product)+" &divide; "+str(number)+" = "+str(product/number)+"<br><br>"
            self.solution_text = self.solution_text + "Since, "+str(product)+" can be divided exactly by "+str(number)+"."
            self.solution_text = self.solution_text + "<br><br><i><b>"+str(product)+" is a multiple of "+str(number)+" or "+str(number)+" is a factor of "+str(product)+"</b></i>"
        else:
            self.solution_text = self.solution_text + str(product)+" &divide; "+str(number)+" = "+str(div)+" R"+str(mod)+"<br><br>"
            self.solution_text = self.solution_text + "Since, "+str(product)+" cannot be divided exactly by "+str(number)+"."
            self.solution_text = self.solution_text + "<br><br><i><b>"+str(product)+" is not a multiple of "+str(number)+" or "+str(number)+" is not a factor of "+str(product)+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.number = randint(2,9)
        self.multiple = randint(2,12)
        
        self.problem = "First 12 multiples of "+str(self.number)+" are listed below. Find the missing number:<br><br>"
        for i in range (6):
            i = i + 1
            if i == self.multiple:
                self.problem = self.problem + str(self.number)+" &times; "+str(i)+"  = __&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
            else:
                self.problem = self.problem + str(self.number)+" &times; "+str(i)+"  = "+str(self.number*i)+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
            if i+6 == self.multiple:
                self.problem = self.problem + str(self.number)+" &times; "+str(i+6)+"  = __<br>"
            else:    
                self.problem = self.problem + str(self.number)+" &times; "+str(i+6)+"  = "+str(self.number*(i+6))+"<br>"
            
        self.answer = self.number * self.multiple
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number,self.multiple)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType7(self,problem,answer,number,multiple):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "The missing number is = "+str(number)+" &times; "+str(multiple)
        self.solution_text = self.solution_text + "<br><br><i><b> = "+str(answer)+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType8(self):
        '''Find a common multiple of 3 and 9.'''
        self.complexity_level = "medium"
        self.HCScore = 5

        self.numbers = random.sample([2,3,4,5,6,7,8,9],2)
        self.numbers.sort()
        self.number1 = self.numbers[0]
        self.number2 = self.numbers[1]
        
        self.problem = "Find a common multiple of %d and %d."%(self.number1,self.number2)
            
        self.answer = LcmGcf.LcmGcf().find_lcm(self.number1,self.number2)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3}

    def ExplainType8(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "The multiples of "+str(number1)+" and "+str(number2)+" are as given below:<br><br>"
        i=0
        while(number1*i!=answer):
            i=i+1
            if (number1*i==answer):
                self.solution_text = self.solution_text + str(number1)+" &times; "+str(i)+" = <font style='color:red'>"+str(number1*i)+"</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
            else:
                self.solution_text = self.solution_text + str(number1)+" &times; "+str(i)+" = "+str(number1*i)+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
            if (number2*i==answer):
                self.solution_text = self.solution_text + str(number2)+" &times; "+str(i)+" = <font style='color:red'>"+str(number2*i)+"</font><br>"
            else:
                self.solution_text = self.solution_text + str(number2)+" &times; "+str(i)+" = "+str(number2*i)+"<br>"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the common multiple is "+str(answer)+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
                
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):  
        if CheckAnswerType == 1:
            try:
                return str(answer)==str(InputAnswer)
            except ValueError:
                return False
        
        elif CheckAnswerType == 2:
            try:
                '''converting list to string as Test module can only store string as answer'''
                answer = str(answer)[1:-1]
                answer = string.join(answer.split(),"")
                AnswerList = []
                while  answer.partition(",")[1]!="":
                    AnswerList.append(int(answer.partition(",")[0]))
                    answer = answer.partition(",")[2]
                AnswerList.append(int(answer))
                AnswerList.sort()
                                
                InputAnswer = str(InputAnswer)
                InputAnswerList = []
                while  InputAnswer.partition(",")[1]!="":
                    InputAnswerList.append(int(InputAnswer.partition(",")[0]))
                    InputAnswer = InputAnswer.partition(",")[2]
                InputAnswerList.append(int(InputAnswer))
                InputAnswerList.sort()
                
                return AnswerList == InputAnswerList
            except ValueError:
                return False
        
        elif CheckAnswerType == 3:
            try:
                return int(InputAnswer)%int(answer)==0
            except ValueError:
                return False            