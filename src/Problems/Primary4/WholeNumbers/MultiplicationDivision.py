'''
Created on Jan 31, 2012

Module: MultiplicationDivision
Generates "Multiplication and division of whole numbers" problems for Primary 4

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

class MultiplicationDivision:
    
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
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],}
        
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
        #return self.GenerateProblemType1()

    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''1234
            X 4
          -----'''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.multiplier = randint(2,9)          
        self.number = randint(1001,9999)
        
        self.problem1 = "Multiply:<br><br>"+str(self.number)+"<br>"
        self.problem1 = self.problem1 + "<u>&nbsp;&nbsp;&times&nbsp;&nbsp;"+str(self.multiplier)+"&nbsp;</u><br>"
        self.problem1 = self.problem1 + "_____"
        
        self.problem2 = "Find the product of %d and %d"%(self.number,self.multiplier)
        
        self.problem = random.choice([self.problem1,self.problem2])
        self.answer = self.number * self.multiplier
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                }

    def ExplainType1(self,problem,answer,number,multiplier):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = str(self.number)+"<br>"
        self.solution_text = self.solution_text + "<u>&nbsp;&nbsp;&times&nbsp;&nbsp;"+str(self.multiplier)+"&nbsp;</u><br>"
        if int(str(number)[3]) == 0:
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 &larr; "+str(number)[3]+" &times; "+str(multiplier)+"<br>"
        else:
            self.solution_text = self.solution_text + "&nbsp;"*(7-len(str(int(str(number)[3])*multiplier)))+str(int(str(number)[3])*multiplier)+" &larr; "+str(number)[3]+" &times; "+str(multiplier)+"<br>"
        if int(str(number)[2]) == 0:
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;00 &larr; "+str(number)[2]+"0 &times; "+str(multiplier)+"<br>"
        else:
            self.solution_text = self.solution_text + "&nbsp;"*(7-len(str(int(str(number)[2])*multiplier*10)))+str(int(str(number)[2])*multiplier*10)+" &larr; "+str(number)[2]+"0 &times; "+str(multiplier)+"<br>"
        if int(str(number)[1]) == 0:
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;000 &larr; "+str(number)[3]+"00 &times; "+str(multiplier)+"<br>"
        else:
            self.solution_text = self.solution_text + "&nbsp;"*(7-len(str(int(str(number)[1])*multiplier*100)))+str(int(str(number)[1])*multiplier*100)+" &larr; "+str(number)[1]+"00 &times; "+str(multiplier)+"<br>"

        self.solution_text = self.solution_text +"<u>"+"&nbsp;"*(6-len(str(int(str(number)[0])*multiplier*1000)))+str(int(str(number)[0])*multiplier*1000)+" &larr; "+str(number)[0]+"000 &times; "+str(multiplier)+"</u><br>"
        self.solution_text = self.solution_text + "<br>Add all the above numbers:<br>"
        self.solution_text = self.solution_text + str(int(str(number)[3])*multiplier)+" + "+str(int(str(number)[2])*multiplier*10)+" + "+str(int(str(number)[1])*multiplier*100)+" + "+str(int(str(number)[0])*multiplier*1000)+" = "+str(answer)+"<br><br>"
        self.solution_text = self.solution_text + "<i><b>Hence the answer is "+str(answer)+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain 

    def GenerateProblemType2(self):
        '''123
            X24
          -----'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.multiplier = randint(10,99)
        self.number = randint(100,999)
        
        self.problem1 = "Multiply:<br><br>"+str(self.number)+"<br>"
        self.problem1 = self.problem1 + "<u>&times;&nbsp;"+str(self.multiplier)+"&nbsp;</u><br>"
        self.problem1 = self.problem1 + "____"
        
        self.problem2 = "Find the product of %d and %d"%(self.number,self.multiplier)
        
        self.problem = random.choice([self.problem1,self.problem2])
        self.answer = self.number * self.multiplier
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                }

    def ExplainType2(self,problem,answer,number,multiplier):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "Explanation coming soon!!"
        self.solution_text = self.solution_text + "<br><br><i><b></b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):
        '''1234 divide 4'''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.divisor = randint(2,9)
        self.number = randint(1010,9999)
        
        div,mod = divmod(self.number,self.divisor)
        self.number = self.number - mod
        
        self.problem = "Calculate:<br><br>"+str(self.number)+" &divide; "+str(self.divisor)

        self.answer = self.number / self.divisor
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number,self.divisor)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                }

    def ExplainType3(self,problem,answer,number,multiplier):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "Explanation coming soon!!"
        self.solution_text = self.solution_text + "<br><br><i><b></b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4(self):
        '''1234 divide 4'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.divisor = randint(2,9)
        self.number = randint(1010,9999)
        
        if self.number%self.divisor == 0:
            self.number = self.number + 1
        
        if randint(1,2) == 1:
            self.problem = "Find the quotient:<br><br>"+str(self.number)+" &divide; "+str(self.divisor)
            self.answer = int(self.number/self.divisor) 
        else:
            self.problem = "Find the remainder:<br><br>"+str(self.number)+" &divide; "+str(self.divisor)
            self.answer = self.number%self.divisor                        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number,self.divisor)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                }

    def ExplainType4(self,problem,answer,number,multiplier):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "Explanation coming soon!!"
        self.solution_text = self.solution_text + "<br><br><i><b></b></i>"
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
                InputAnswer = str(InputAnswer)
                InputAnswerList = []
                while  InputAnswer.partition(",")[1]!="":
                    InputAnswerList.append(int(InputAnswer.partition(",")[0]))
                    InputAnswer = InputAnswer.partition(",")[2]
                InputAnswerList.append(int(InputAnswer))
                return list(answer).sort() == InputAnswerList.sort()
                #return answer==InputAnswer
            except ValueError:
                return False
        elif CheckAnswerType == 3:
            try:
                return int(InputAnswer)%int(answer)==0
            except ValueError:
                return False            