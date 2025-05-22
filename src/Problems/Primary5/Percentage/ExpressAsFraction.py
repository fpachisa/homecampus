'''
Created on Mar 06, 2011

Module: ExpressAsFraction
Generates "Expressing a percentage as fraction" problems for Primary 5

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
from decimal import Decimal
from Utils import LcmGcf

class ExpressAsFraction:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        return self.GenerateProblemType1()                    
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            }
        return self.ProblemType[problem_type]
   
    def ExplainType1(self,problem,answer,number,number1,number2,gcf):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "To express "+str(number)+" as fraction, divide it by 100 and remove the &#37; sign.<br><br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(number)+"&nbsp;</u><br>100</td>"
        self.solution_text = self.solution_text + "<td align='center'>=</td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.number1)+"&nbsp;</u><br>"+str(self.number2)+"</td></tr></table>"
        if gcf!=1:
            self.solution_text = self.solution_text + "It can be further simplified to:<br><br>"
            self.solution_text = self.solution_text + "<table class='FractionsTable'><tr>"
            self.solution_text = self.solution_text + "<td></td><td align='center'>=</td><td>"+str(answer)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br><i><b>Hence the correct answer is "+str(answer)+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType1(self):
        '''e.g.:
        Express the following percentage as a fraction:
        78 / 100'''
             
        self.number2 = random.choice([5,10,20,25,50,100])     
        self.number1 = randint(1,self.number2-1)
        self.number = self.number1*100/self.number2
        
        self.problem = "Express the following percentage as fraction:"
        self.problem = self.problem + "<table class='FractionsTable'><tr>"     
        self.problem = self.problem + "<td>(Express your answer as a/b. For e.g. write&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;1&nbsp;</u><br>&nbsp;2&nbsp;</td>"
        self.problem = self.problem + "<td>&nbsp;as 1/2)&nbsp;</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + str(self.number)+"&#37;"

        gcf = LcmGcf.LcmGcf().find_gcf(self.number1,self.number2)        
        self.answer = str(self.number1/gcf)+"/"+str(self.number2/gcf)      
                
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number,self.number1,self.number2,gcf)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",'unit':""}

    def checkAnswer(self,template,answer,InputAnswer):
        try:
            AnswerNumerator = int(str(answer).partition("/")[0])
            AnswerDenominator = int(str(answer).partition("/")[2])

            InputNumerator = int(str(InputAnswer).partition("/")[0])
            InputDenominator = int(str(InputAnswer).partition("/")[2])

            return Decimal(AnswerNumerator)/Decimal(AnswerDenominator)==Decimal(InputNumerator)/Decimal(InputDenominator)
        except ValueError:
            return False 