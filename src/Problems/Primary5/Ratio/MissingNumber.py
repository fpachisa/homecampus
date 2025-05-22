'''
Created on Mar 06, 2011

Module: MissingNumber
Generates "Finding the missing number" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

from random import randint
from Utils import LcmGcf

class MissingNumber:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        return self.GenerateProblemType1()                    
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g.:
        Express the following ratio in its simplest form:
        18:24 = _:_'''
        
        self.multiplier = randint(2,5)
        self.number1 = randint(2,9)*self.multiplier
        self.number2 = randint(2,9)*self.multiplier
        while self.number1 == self.number2:
            self.number1 = randint(2,9)*self.multiplier
            self.number2 = randint(2,9)*self.multiplier

        gcf = LcmGcf.LcmGcf().find_gcf(self.number1,self.number2)
        self.answer = self.number2/gcf
         
        if randint(1,2)==1:
            self.problem = "Find the missing number: <br><br>"+str(self.number1)+" : "+str(self.number2)+" = "+str(self.number1/gcf)+" : __"
            self.answer = self.number2/gcf
            self.flag = 1      
        else:
            self.problem = "Find the missing number: <br><br>"+str(self.number1)+" : "+str(self.number2)+" = __ : "+str(self.number2/gcf)
            self.answer = self.number1/gcf
            self.flag = 2    
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,gcf,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",'unit':"",
                'CheckAnswerType':1}
    
    def ExplainType1(self,problem,answer,number1,number2,gcf,flag):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "A ratio remains unchanged if its terms are multiplied or divided by the same number.<br><br>"
        if flag==1:
            self.solution_text = self.solution_text + "We get "+str(number1/gcf)+" by dividing "+str(number1)+" by "+str(gcf)+".<br><br>"
            self.solution_text = self.solution_text + "To get the missing number we need to divide "+str(number2)+" by the same number "+str(gcf)+".<br><br>"
            self.solution_text = self.solution_text + "= "+str(number2)+" &divide; "+str(gcf)+" = "+str(number2/gcf)
        elif flag==2:
            self.solution_text = self.solution_text + "We get "+str(number2/gcf)+" by dividing "+str(number2)+" by "+str(gcf)+".<br><br>"
            self.solution_text = self.solution_text + "To get the missing number we need to divide "+str(number1)+" by the same number "+str(gcf)+".<br><br>"
            self.solution_text = self.solution_text + "= "+str(number1)+" &divide; "+str(gcf)+" = "+str(number1/gcf)            
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+str(answer)+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain


    def checkAnswer(self,template,answer,InputAnswer):
        try:
            return (str(answer)==str(InputAnswer))
        except ValueError:
            return False  