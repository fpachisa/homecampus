'''
Created on Jan 18, 2011

Module: ExpressAsPercent
Generates "Expressing as percentage" problems for Primary 5

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

class ExpressAsPercent:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        self.ProblemType = random.choice([self.GenerateProblemType1(),self.GenerateProblemType2(),self.GenerateProblemType3()])
        return self.ProblemType
        #return self.GenerateProblemType3()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:"ProblemType1",2:"ProblemType2",3:"ProblemType3",}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemType2(),3:self.GenerateProblemType3(),
                                    }
        
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(self.GenerateProblemType.values())
        else:
            if LastProblemID in self.ProblemType.values():
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if v == LastProblemID][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return self.GenerateProblemType[NextProblemKey]
            else:
                return random.choice(self.GenerateProblemType.values())
        #return self.GenerateProblemType1()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g.:
        Express the following as a percentage:
        78 out of 100'''
        
        self.number2 = random.choice([5,10,20,25,50,100])     
        self.number1 = randint(1,self.number2-1)
        self.problem="Express the following as a percentage:<br><br>%d out of %d"%(self.number1,self.number2)
        
        self.answer = self.number1*100/self.number2         
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2)       
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",'unit':"&#37;"}
    
    def ExplainType1(self,problem,answer,number1,number2):
        self.answer_text = "The correct answer is:<br>"+str(answer)+"&#37;"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        if number2!=100:
            self.solution_text = self.solution_text + str(number1)+" out of "+str(number2)+" is same as "+str(answer)+" out of 100<br><br>"
        self.solution_text = self.solution_text + str(answer)+" out of 100 means "+str(answer)+"&#37;"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+str(answer)+"&#37;</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.:
        Express the following fraction as a percentage:
        78 / 100'''
             
        self.number2 = random.choice([5,10,20,25,50,100])     
        self.number1 = randint(1,self.number2-1)
        self.problem="Express the following fraction as a percentage:<br><br>"
        self.problem = self.problem + "<table cellspacing=0 cellpadding=1><tr>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.number1)+"&nbsp;</u><br>"+str(self.number2)+"</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.answer = self.number1*100/self.number2        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",'unit':"&#37;"}
    
    def ExplainType2(self,problem,answer,number1,number2):
        self.answer_text = "The correct answer is:<br>"+str(answer)+"&#37;"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Multiply the fraction by 100 &#37; to convert it to percentage:<br><br>"
        self.solution_text = self.solution_text + "<table cellspacing=0 cellpadding=1><tr>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.number1)+"&nbsp;</u><br>"+str(self.number2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'>=</td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.number1)+"&nbsp;</u><br>"+str(self.number2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'>&times; 100 &#37;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td></td><td align='center'>=</td><td>"+str(answer)+"&#37;</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br><i><b>Hence the correct answer is "+str(answer)+"&#37;</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):
        '''e.g.:
        Express the following decimal as percentage:
        0.30'''
             
        self.number1 = "0."+random.choice(["0"+str(randint(1,9)),str(randint(11,99))])
        self.problem = "Express the following decimal as percentage:<br><br>"+self.number1
        
        self.answer = int(float(self.number1)*100)          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",'unit':"&#37;"}
    
    def ExplainType3(self,problem,answer,number1):
        self.answer_text = "The correct answer is:<br>"+str(answer)+"&#37;"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Multiply "+str(number1)+" by 100 to convert it to percentage:<br><br>"
        self.solution_text = self.solution_text + "Multiplying by 100 is equal to shifting decimal places to the right by 2 digits<br><br>"
        self.solution_text = self.solution_text + "<br><i><b>Hence the correct answer is "+str(answer)+"&#37;</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):
        '''e.g.:
        What percentage of the whole figure is coloured?'''
             
        self.number1 = randint(1,10)
        self.number2 = randint(1,10)
        
        self.problem = "<table border=1>"
        for _i in range(10):
            self.problem = self.problem + "<tr>"
            self.problem = self.problem + "<td "+random.choice(["bgcolor = yellow",""])+" width=10 height=10></td>"
            self.problem = self.problem + "<td "+random.choice(["bgcolor = yellow",""])+" width=10 height=10></td>"
            self.problem = self.problem + "<td "+random.choice(["bgcolor = yellow",""])+" width=10 height=10></td>"
            self.problem = self.problem + "<td "+random.choice(["bgcolor = yellow",""])+" width=10 height=10></td>"
            self.problem = self.problem + "</tr>"
        self.problem = self.problem + "</table>"
        
        self.answer = ""          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",'unit':"&#37;"}

    def checkAnswer(self,template,answer,InputAnswer):
        try:
            return (str(answer)==str(InputAnswer))
        except ValueError:
            return False  