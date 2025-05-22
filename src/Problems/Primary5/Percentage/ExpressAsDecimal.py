'''
Created on Mar 06, 2011

Module: ExpressAsDecimal
Generates "Expressing a percentage as decimal" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

from random import randint

class ExpressAsDecimal:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        return self.GenerateProblemType1()                    
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            }
        return self.ProblemType[problem_type]
    
    def ExplainType1(self,problem,answer,number):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Divide "+str(number)+" by 100 to convert it to decimal.<br><br>"
        self.solution_text = self.solution_text + "Dividing by 100 is equal to shifting decimal places to the left by 2 digits."
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+str(answer)+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType1(self):
        '''e.g.:
        Express the following percentage as decimal:
        0.30'''

        self.number = randint(10,99)
        self.answer = float(self.number)/100
        self.problem = "Express the following percentage as decimal<br><br>"+str(self.number)+"&#37;"       
                 
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'unit':""}

    def checkAnswer(self,template,answer,InputAnswer):
        try:
            return (float(answer)==float(InputAnswer))
        except ValueError:
            return False  