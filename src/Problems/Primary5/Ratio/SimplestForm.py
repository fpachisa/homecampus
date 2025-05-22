'''
Created on Mar 06, 2011

Module: SimplestForm
Generates "Expressing a ratio in simplest form" problems for Primary 5

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
import string

class SimplestForm:
    
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
        self.answer = str(self.number1/gcf)+":"+str(self.number2/gcf)
         
        self.problem = "Express the following ratio in its simplest form (Express your answer as a:b)<br><br>"+str(self.number1)+":"+str(self.number2)      
                 
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,gcf)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",'unit':"",
                'CheckAnswerType':1}
    
    def ExplainType1(self,problem,answer,number1,number2,gcf):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "A ratio remains unchanged if its terms are multiplied or divided by the same number.<br><br>"
        self.solution_text = self.solution_text + "To express a ratio in its simplest form, we divide both the numbers by its common factor.<br><br>"
        self.solution_text = self.solution_text + str(gcf)+" is a common factor of "+str(number1)+" and "+str(number2)+". Divide "+str(number1)+" and "+str(number2)+" by "+str(gcf)+"."
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+str(answer)+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer):
        try:
            InputAnswer= string.join(InputAnswer.split(),"")
            return (str(answer)==str(InputAnswer))
        except ValueError:
            return False  