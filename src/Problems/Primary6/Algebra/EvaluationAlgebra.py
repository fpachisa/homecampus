'''
Created on Sep 28, 2011

Module: EvaluationAlgebra
Generates "Evaluation of algebraic expressions" problems for Primary 6

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

class EvaluationAlgebra:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"easy":[self.GenerateProblemType1(),self.GenerateProblemType2(),self.GenerateProblemType3(),
                                       self.GenerateProblemType4(),self.GenerateProblemType5(),self.GenerateProblemType6(),
                                       self.GenerateProblemTypeMCQ1(),self.GenerateProblemTypeMCQ2(),self.GenerateProblemTypeMCQ3(),
                                       self.GenerateProblemTypeMCQ4(),self.GenerateProblemTypeMCQ5(),self.GenerateProblemTypeMCQ6(),],
                            "medium":[self.GenerateProblemType7(),self.GenerateProblemType8(),self.GenerateProblemType9(),
                                    self.GenerateProblemTypeMCQ7(),self.GenerateProblemTypeMCQ8(),self.GenerateProblemTypeMCQ9()],
                            }
        try:
            return random.choice(self.ProblemType[level])
        except KeyError:
            return random.choice(random.choice(self.ProblemType.values()))
        #return self.GenerateProblemTypeMCQ9()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1"],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType5","ProblemTypeMCQ5",],
                            6:["ProblemType6","ProblemTypeMCQ6",],
                            7:["ProblemType7","ProblemTypeMCQ7",],
                            8:["ProblemType8","ProblemTypeMCQ8",],
                            9:["ProblemType9","ProblemTypeMCQ9",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1()],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3()],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4()],
                                    5:[self.GenerateProblemType5(),self.GenerateProblemTypeMCQ5()],
                                    6:[self.GenerateProblemType6(),self.GenerateProblemTypeMCQ6()],
                                    7:[self.GenerateProblemType7(),self.GenerateProblemTypeMCQ7()],
                                    8:[self.GenerateProblemType8(),self.GenerateProblemTypeMCQ8()],
                                    9:[self.GenerateProblemType9(),self.GenerateProblemTypeMCQ9()],
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
        return self.GenerateProblemType()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemTypeMCQ9":self.GenerateProblemTypeMCQ9(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g: n + 4 = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"      
        if randint(1,2)==1:
            self.problem = self.problem + "<i>"+self.variable + "</i> + " + str(self.number2)+" = "
            self.flag = 1
        else:
            self.problem = self.problem + str(self.number2) + " + <i>" + self.variable+"</i> = "
            self.flag = 2
        
        self.answer = str(self.number1+self.number2)

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.variable,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType1(self,problem,answer,number1,number2,variable,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "When <i>"+variable+"</i> = "+str(number1)+",<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:right; padding-right:0px'><i><font color='red'>"+variable + "</font></i> + " + str(number2)+"</td><td>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><font color='red'>"+str(number1)+"</font> + "+str(number2)+"</td></tr>"
        if flag == 2:
            self.solution_text = self.solution_text +"<table><tr><td style='text-align:right; padding-right:0px'>"+str(number2)+" + <i><font color='red'>"+variable + "</font></i></td><td>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'>"+str(number2)+" + <font color='red'>"+str(number1)+"</font></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):
        '''e.g: n - 3 = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number2 = randint(2,10)
        self.answer = randint(2,10)
        self.number1 = self.answer + self.number2
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        if randint(1,2)==1:
            self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"
            self.problem = self.problem +"<i>" +self.variable + "</i> &minus; " + str(self.number2)+" = "
            self.flag = 1
        else:
            self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number2)+":<br><br>"
            self.problem = self.problem + str(self.number1)+" &minus; <i>"+self.variable +"</i> = "
            self.flag = 2
        
        self.answer = str(self.answer)
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.variable,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType2(self,problem,answer,number1,number2,variable,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        if flag == 1:
            self.solution_text =  "When <i>"+variable+"</i> = "+str(number1)+",<br><br>"
            self.solution_text = self.solution_text +  "<table><tr><td style='text-align:right; padding-right:0px'><i><font color='red'>"+variable + "</font></i> &minus; " + str(number2)+"</td><td>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><font color='red'>"+ str(number1)+"</font> &minus; "+str(number2)+"</td></tr>"
        if flag == 2:
            self.solution_text =  "When <i>"+variable+"</i> = "+str(number2)+",<br><br>"
            self.solution_text = self.solution_text +"<table><tr><td style='text-align:right; padding-right:0px'>"+str(number1)+" &minus; <i><font color='red'>"+variable + "</font></i></td><td>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'>"+str(number1)+" &minus; <font color='red'>"+str(number2)+"</font></td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):
        '''e.g: 3n = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"
        self.problem = self.problem +str(self.number2)+"<i>"+ self.variable+"</i> = "
               
        self.answer = str(self.number1 * self.number2)
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType3(self,problem,answer,number1,number2,variable):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "When <i>"+variable+"</i> = "+str(number1)+",<br><br>"
        self.solution_text = self.solution_text + "<table border=0><tr><td style='text-align:right; padding-right:0px'>" + str(number2)+"<i><font color='red'>"+variable +"</font></i><td>=</td><td style='text-align:left; padding-left:0px'>"+str(number2)+" &times; <i><font color='red'>"+variable + "</font></i></td></tr>"
        self.solution_text = self.solution_text +"<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+ str(number2)+" &times; <font color='red'>"+str(number1)+"</font></td></tr>"
        self.solution_text = self.solution_text +"<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+ str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4(self):
        '''e.g: 3n + 6 = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.number3 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"
        
        if randint(1,2)==1:
            self.problem = self.problem +str(self.number2)+"<i>"+ self.variable+"</i> + "+str(self.number3)+" = "
            self.flag = 1
        else:
            self.problem = self.problem +str(self.number3)+" + "+str(self.number2)+"<i>"+ self.variable+"</i> = "
            self.flag = 2
               
        self.answer = str(self.number1 * self.number2 + self.number3)
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.number3,self.variable,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType4(self,problem,answer,number1,number2,number3,variable,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        self.solution_text =  "When <i>"+variable+"</i> = "+str(number1)+",<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "<table border=0><tr><td style='text-align:right; padding-right:0px'>" + str(number2)+"<i><font color='red'>"+variable+"</font></i> + "+str(number3)+"</td><td>=</td><td style='text-align:left; padding-left:0px'>("+str(number2)+" &times; <i> <font color='red'>"+variable + "</font></i>) + " + str(number3) +"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>("+str(number2)+" &times; <font color='red'>"+str(number1)+"</font>) + "+str(number3)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(number2*number1)+" + "+str(number3)+"</td></tr>"
        if flag == 2:
            self.solution_text = self.solution_text + "<table border=0><tr><td style='text-align:right; padding-right:0px'>" + str(number3)+" + " +str(number2)+"<i><font color='red'>"+variable+"</font></i></td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(number3)+" + (" +str(number2)+" &times; <i> <font color='red'>"+variable + "</font></i>)</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(number3)+ " + ("+str(number2)+" &times; <font color='red'>"+str(number1)+"</font>)</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(number3)+" + "+str(number2*number1)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain    

    def GenerateProblemType5(self):
        '''e.g: 3n - 6 = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.number3 = randint(2,self.number1*self.number2-2)
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"
        
        self.problem = self.problem +str(self.number2)+"<i>"+ self.variable+"</i> &nbsp;&minus;&nbsp; "+str(self.number3)+" = "
               
        self.answer = str(self.number1 * self.number2 - self.number3)
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.number3,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType5(self,problem,answer,number1,number2,number3,variable):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "When <i>"+variable+"</i> = "+str(number1)+",<br><br>"
        
        self.solution_text = self.solution_text + "<table border=0><tr><td style='text-align:right; padding-right:0px'>" + str(number2)+"<i><font color='red'>"+variable+"</font></i> &minus; "+str(number3)+"</td><td>=</td><td style='text-align:left; padding-left:0px'>("+str(number2)+" &times; <i><font color='red'>"+variable + "</font></i>) &minus; " + str(number3) +"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>("+str(number2)+" &times; <i><font color='red'>"+str(number1)+"</font></i>) &minus; "+str(number3)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(number1*number2)+" &minus; "+str(number3)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'    
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain    

    def GenerateProblemType6(self):
        '''e.g:  8 - 3n = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.answer = randint(2,20)
        self.number3 = self.answer + self.number1*self.number2
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"        
        self.problem = self.problem +str(self.number3)+" &nbsp;&minus;&nbsp; "+str(self.number2)+"<i>"+ self.variable+"</i> = "
               
        self.answer = str(self.answer)
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.number3,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType6(self,problem,answer,number1,number2,number3,variable):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "When <i>"+variable+"</i> = "+str(number1)+",<br><br>"
        
        self.solution_text = self.solution_text + "<table border=0><tr><td style='text-align:right; padding-right:0px'>"+str(number3)+" &minus; "+ str(number2)+"<i><font color='red'>"+variable+"</font></i></td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(number3)+" &minus; ("+str(number2)+" &times; <i><font color='red'>"+variable + "</font></i>)</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(number3)+" &minus; ("+str(number2)+" &times; <i><font color='red'>"+str(number1)+"</font></i>)</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(number3)+" &minus; "+str(number1*number2)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain    

    def GenerateProblemType7(self):
        '''e.g:  4m + 2 / 5 '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.answer = randint(2,10)
        self.number4 = randint(2,10)
        self.number3 = randint(2,10)
        self.number1 = randint(0,10)
        self.number2 = self.answer*self.number4 - self.number1*self.number3
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])

        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"
        self.problem = self.problem + "<table class='FractionsTable'><tr>"
        if self.number2 > 0:
            self.problem = self.problem + "<td style='text-align:center'><u>"+str(self.number2)+" + "+str(self.number3)+"<i>"+self.variable+"</i></u><br>"+str(self.number4)+"</td>"
            #self.problem = self.problem + "<td><u>"+str(self.number2)+" + "+str(self.number3)+"<i>"+self.variable+"</i></u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+str(self.number4)+"</td>"
            self.flag = 1
        elif self.number2 < 0:
            self.problem = self.problem + "<td style='text-align:center'><u>"+str(self.number3)+"<i>"+self.variable+"</i> &minus; "+str(abs(self.number2))+"</u><br>"+str(self.number4)+"</td>"
            #self.problem = self.problem + "<td><u>"+str(self.number3)+"<i>"+self.variable+"</i> &minus; "+str(abs(self.number2))+"</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+str(self.number4)+"</td>"
            self.flag = 2
        else:
            self.problem = self.problem + "<td style='text-align:center'><u>"+str(self.number3)+"<i>"+self.variable+"</i></u><br>"+str(self.number4)+"</td>"
            #self.problem = self.problem + "<td><u>"+str(self.number3)+"<i>"+self.variable+"</i></u><br>&nbsp;"+str(self.number4)+"</td>"
            self.flag = 3
        self.problem = self.problem + "<td> &nbsp;&nbsp;=</td>"
        self.problem = self.problem + "</tr></table>"
           
        self.answer = str(self.answer)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.variable,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType7(self,problem,answer,number1,number2,number3,number4,variable,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "When <i>"+variable+"</i> = "+str(number1)+",<br><br>"
        self.solution_text = self.solution_text + "<table><tr>"
        #self.solution_text = self.solution_text + "<table class='FractionsTable'><tr>"
        if flag == 1:
            self.solution_text = self.solution_text + "<td style='text-align:right; padding-right:0px'><table><tr><td style='text-align:center'><u>"+str(number2)+" + "+str(number3)+"<i><font color='red'>"+variable+"</font></i></u><br>"+str(number4)+"</td></tr></table></td>"
            self.solution_text = self.solution_text + "<td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>"+str(number2)+" + ("+str(number3)+" &times; <i><font color='red'>"+variable+"</font></i>)</u><br>"+str(number4)+"</td></tr></table></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>"+str(number2)+" + ("+str(number3)+" &times; <font color='red'>"+str(number1)+"</font>)</u><br>"+str(number4)+"</td></tr></table></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>"+str(number2)+" + "+str(number3*number1)+"</u><br>"+str(number4)+"</td></tr></table></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>"+str(number2+(number3*number1))+"</u><br>"+str(number4)+"</td></tr></table></td></tr>"
        elif flag ==2:
            self.solution_text = self.solution_text + "<td style='text-align:right; padding-right:0px'><table><tr><td style='text-align:center'><u>"+str(number3)+"<i><font color='red'>"+variable+"</font></i> &minus; "+str(abs(number2))+"</u><br>"+str(number4)+"</td></tr></table></td>"
            self.solution_text = self.solution_text + "<td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>("+str(number3)+" &times; <i><font color='red'>"+variable+"</font></i>) &minus; "+str(abs(number2))+"</u><br>"+str(number4)+"</td></tr></table></td>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>("+str(number3)+" &times; <font color='red'>"+str(number1)+"</font>) &minus; "+str(abs(number2))+"</u><br>"+str(number4)+"</td></tr></table></td>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>"+str(number3*number1)+" &minus; "+str(abs(number2))+"</u><br>"+str(number4)+"</td></tr></table></td>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>"+str(number3*number1-(abs(number2)))+"</u><br>"+str(number4)+"</td></tr></table></td>"
        elif flag == 3:
            self.solution_text = self.solution_text + "<td style='text-align:right; padding-right:0px'><table><tr><td style='text-align:center'><u>"+str(number3)+"<i><font color='red'>"+variable+"</font></i></u><br>"+str(number4)+"</td></tr></table></td>"
            self.solution_text = self.solution_text + "<td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>("+str(number3)+" &times; <i><font color='red'>"+variable+"</font></i>)</u><br>"+str(number4)+"</td></tr></table></td>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>("+str(number3)+" &times; <font color='red'>"+str(number1)+"</font>)</u><br>"+str(number4)+"</td></tr></table></td>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>"+str(number3*number1)+"</u><br>"+str(number4)+"</td></tr></table></td>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"            
        self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'>"+str(answer)+"</td></tr></table></td></tr>"
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8(self):
        '''e.g:  24 - 3m / 6 '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.answer = randint(2,10)
        self.number4 = randint(2,10)
        self.number3 = randint(2,10)
        self.number1 = randint(0,10)
        self.number2 = self.answer*self.number4 + self.number1*self.number3
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])

        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"
        self.problem = self.problem + "<table class='FractionsTable'><tr>"
        self.problem = self.problem + "<td style='text-align:center'><u>"+str(self.number2)+" &minus; "+str(self.number3)+"<i>"+self.variable+"</i></u><br>"+str(self.number4)+"</td>"
        self.problem = self.problem + "<td> &nbsp;&nbsp;= </td>"
        self.problem = self.problem + "</tr></table>"
           
        self.answer = str(self.answer)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType8(self,problem,answer,number1,number2,number3,number4,variable):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "When <i>"+variable+"</i> = "+str(number1)+",<br><br>"
        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td style='text-align:right; padding-right:0px'><table><tr><td style='text-align:center'><u>"+str(number2)+" &minus; "+str(number3)+"<i><font color='red'>"+variable+"</font></i></u><br>"+str(number4)+"</td></tr></table></td>"
        self.solution_text = self.solution_text + "<td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
        self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>"+str(number2)+" &minus; ("+str(number3)+" &times; <i><font color='red'>"+variable+"</font></i>)</u><br>"+str(number4)+"</td></tr></table></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
        self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>"+str(number2)+" &minus; ("+str(number3)+" &times; <font color='red'>"+str(number1)+"</font>)</u><br>"+str(number4)+"</td></tr></table></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
        self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>"+str(number2)+" &minus; "+str(number3*number1)+"</u><br>"+str(number4)+"</td></tr></table></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"
        self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'><u>"+str(number2-(number3*number1))+"</u><br>"+str(number4)+"</td></tr></table></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:middle; padding-left:0px; padding-right:0px'>=</td>"            
        self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><table><tr><td style='text-align:center'>"+str(answer)+"</td></tr></table></td></tr>"
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType9(self):
        '''e.g: 3k + 4 - k - 1 = '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.number1 = randint(3,10)
        self.number2 = randint(1,self.number1-2)
        self.number3 = randint(3,10)
        self.number4 = randint(1,self.number3-2)
        self.number5 = randint(0,8)
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number5)+":<br><br>"
        if self.number2 == 1:
            self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i> + "+str(self.number3)+" &minus; <i>"+self.variable+"</i> &minus; "+str(self.number4)+" = "
            #self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i> + "+str(self.number3)+" - <i>"+self.variable+"</i> - "+str(self.number4)+" = "
            self.flag = 1
        else:
            self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i> + "+str(self.number3)+" &minus; "+str(self.number2)+"<i>"+self.variable+"</i> &minus; "+str(self.number4)+" = "
            #self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i> + "+str(self.number3)+" - "+str(self.number2)+"<i>"+self.variable+"</i> - "+str(self.number4)+" = "
            self.flag = 2
           
        self.answer = str((self.number1-self.number2)*self.number5+self.number3-self.number4)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.variable,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType9",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}        
  
    def ExplainType9(self,problem,answer,number1,number2,number3,number4,number5,variable,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "When <i>"+variable+"</i> = "+str(number1)+",<br><br>"
        self.solution_text = self.solution_text + "<table>"
        if flag==1:
            self.solution_text = self.solution_text + "<tr><td style='text-align:right; padding-right:0px'><font color='red'>" +str(number1)+"<i>"+variable+"</font></i> + "+str(number3)+"<font color='red'> &minus; <i>"+variable+"</font></i> &minus; "+str(number4)+"</td>"
            self.solution_text = self.solution_text + "<td>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><font color='red'>" +str(number1)+"<i>"+variable+"</i> &minus; <i>"+variable+"</font></i> + "+str(number3)+" &minus; "+str(number4)+"</td></tr>"
        elif flag ==2:
            self.solution_text = self.solution_text + "<tr><td style='text-align:right; padding-right:0px'><font color='red'>"+str(number1)+"<i>"+variable+"</font></i> + "+str(number3)+"<font color='red'> &minus; "+str(number2)+"<i>"+variable+"</font></i> &minus; "+str(number4)+"</td>"
            self.solution_text = self.solution_text + "<td>=</td>"
            self.solution_text = self.solution_text + "<td style='text-align:left; padding-left:0px'><font color='red'>"+str(number1)+"<i>"+variable+"</i> &minus; "+str(number2)+"<i>"+variable+"</i></font> + "+str(number3)+"</i> &minus; "+str(number4)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+ "<font color='red'>"+str(number1-number2)+"<i>"+variable+"</i></font> + "+str(number3-number4)+"</td</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'><font color='red'>"+ str(number1-number2)+" &times; "+str(number5)+"</font> + "+str(number3-number4)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'><font color='red'>"+ str((number1-number2)*number5)+"</font> + "+str(number3-number4)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td style='text-align:left; padding-left:0px'>"+str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
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
        '''e.g: n + 4 = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"      
        if randint(1,2)==1:
            self.problem = self.problem + "<i>"+self.variable + "</i> + " + str(self.number2)+" = "
            self.flag = 1
        else:
            self.problem = self.problem + str(self.number2) + " + <i>" + self.variable+"</i> = "
            self.flag = 2
                    
        self.answer = str(self.number1+self.number2)
        
        self.problem_type = "ProblemTypeMCQ1"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.number1+self.number2+1))
        self.wrongAnswers.append(str(self.number1+self.number2-1))
        self.wrongAnswers.append(str(self.number1+self.number2+2))
        self.wrongAnswers.append(str(self.number1+self.number2-2))

        self.answer1 = self.answer
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.variable,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            
    
    def GenerateProblemTypeMCQ2(self):
        '''e.g: n - 3 = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number2 = randint(2,10)
        self.answer = randint(2,10)
        self.number1 = self.answer + self.number2
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        if randint(1,2)==1:
            self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"
            self.problem = self.problem +"<i>" +self.variable + "</i> &minus; " + str(self.number2)+" = "
            self.flag = 1
        else:
            self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number2)+":<br><br>"
            self.problem = self.problem + str(self.number1)+" &minus; <i>"+self.variable +"</i> = "
            self.flag = 2
               
        self.problem_type = "ProblemTypeMCQ2"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))        
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer-2))
            
        self.answer = str(self.answer)                    
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.variable,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            
    
    def GenerateProblemTypeMCQ3(self):
        '''e.g: 3n = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"
        self.problem = self.problem +str(self.number2)+"<i>"+ self.variable+"</i> = "
               
        self.answer = self.number1 * self.number2
        
        self.problem_type = "ProblemTypeMCQ3"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str((self.number1-1)*self.number2))        
        self.wrongAnswers.append(str((self.number2-1)*self.number1))
        self.wrongAnswers.append(str((self.number1+1)*self.number2))
        self.wrongAnswers.append(str((self.number2+1)*self.number1))
            
        self.answer = str(self.answer)                    
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)
    
    def GenerateProblemTypeMCQ4(self):
        '''e.g: 3n + 6 = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.number3 = randint(2,10)
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"
        
        if randint(1,2)==1:
            self.problem = self.problem +str(self.number2)+"<i>"+ self.variable+"</i> + "+str(self.number3)+" = "
            self.flag = 1
        else:
            self.problem = self.problem +str(self.number3)+" + "+str(self.number2)+"<i>"+ self.variable+"</i> = "
            self.flag = 2
               
        self.answer = self.number1 * self.number2 + self.number3
        
        self.problem_type = "ProblemTypeMCQ4"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))        
        self.wrongAnswers.append(str(self.number1+self.number2+self.number3+1))
        self.wrongAnswers.append(str(self.answer-1))
        if (self.number1==self.number2==self.number3):
            self.wrongAnswers.append(str(self.answer-2))
        else:
            self.wrongAnswers.append(str(self.number1+self.number2+self.number3))
            
            
        self.answer = str(self.answer)                    
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.number3,self.variable,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)
    
    def GenerateProblemTypeMCQ5(self):
        '''e.g: 3n - 6 = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.number3 = randint(2,self.number1*self.number2-2)
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"
        
        self.problem = self.problem +str(self.number2)+"<i>"+ self.variable+"</i> &minus; "+str(self.number3)+" = "
               
        self.answer = self.number1 * self.number2 - self.number3
        
        self.problem_type = "ProblemTypeMCQ5"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))        
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer-2))           
            
        self.answer = str(self.answer)                    
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.number3,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)
    
    def GenerateProblemTypeMCQ6(self):
        '''e.g:  8 - 3n = '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.number1 = randint(2,10)
        self.number2 = randint(2,10)
        self.answer = randint(2,20)
        self.number3 = self.answer + self.number1*self.number2
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"        
        self.problem = self.problem +str(self.number3)+" &minus; "+str(self.number2)+"<i>"+ self.variable+"</i> = "
        
        self.problem_type = "ProblemTypeMCQ6"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))        
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer-2))           
            
        self.answer = str(self.answer)                    
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.number3,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)
    
    def GenerateProblemTypeMCQ7(self):
        '''e.g:  4m + 2 / 5 '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.answer = randint(2,10)
        self.number4 = randint(2,10)
        self.number3 = randint(2,10)
        self.number1 = randint(0,10)
        self.number2 = self.answer*self.number4 - self.number1*self.number3
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])

        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"
        self.problem = self.problem + "<table class='FractionsTable'><tr>"
        if self.number2 > 0:
            self.problem = self.problem + "<td style='text-align:center'><u>"+str(self.number2)+" + "+str(self.number3)+"<i>"+self.variable+"</i></u><br>"+str(self.number4)+"</td>"
            self.flag = 1
        elif self.number2 < 0:
            self.problem = self.problem + "<td style='text-align:center'><u>"+str(self.number3)+"<i>"+self.variable+"</i> &minus; "+str(abs(self.number2))+"</u><br>"+str(self.number4)+"</td>"
            self.flag = 2
        else:
            self.problem = self.problem + "<td style='text-align:center'><u>"+str(self.number3)+"<i>"+self.variable+"</i></u><br>"+str(self.number4)+"</td>"
            self.flag = 3
        self.problem = self.problem + "<td> &nbsp;&nbsp;= </td>"
        self.problem = self.problem + "</tr></table>"
        
        self.problem_type = "ProblemTypeMCQ7"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))        
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer-2))           
            
        self.answer = str(self.answer)                    
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.variable,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)
    
    def GenerateProblemTypeMCQ8(self):
        '''e.g:  24 - 3m / 6 '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.answer = randint(2,10)
        self.number4 = randint(2,10)
        self.number3 = randint(2,10)
        self.number1 = randint(0,10)
        self.number2 = self.answer*self.number4 + self.number1*self.number3
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])

        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number1)+":<br><br>"
        self.problem = self.problem + "<table class='FractionsTable'><tr>"
        self.problem = self.problem + "<td style='text-align:center'><u>"+str(self.number2)+" &minus; "+str(self.number3)+"<i>"+self.variable+"</i></u><br>"+str(self.number4)+"</td>"
        self.problem = self.problem + "<td> &nbsp;&nbsp;= </td>"
        self.problem = self.problem + "</tr></table>"
        
        self.problem_type = "ProblemTypeMCQ8"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))        
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer-2))           
            
        self.answer = str(self.answer)                    
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.variable)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)
    
    def GenerateProblemTypeMCQ9(self):
        '''e.g: 3k + 4 - k - 1 = '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.number1 = randint(3,10)
        self.number2 = randint(1,self.number1-2)
        self.number3 = randint(3,10)
        self.number4 = randint(1,self.number3-2)
        self.number5 = randint(0,8)
        self.variable = random.choice(['a','b','c','d','e','h','i','k','m','n','r','s','t','u','v','w','x','z'])
        
        self.problem = "Find the value of the following algebraic expression where <i>"+ self.variable+"</i> = "+str(self.number5)+":<br><br>"
        if self.number2 == 1:
            self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i> + "+str(self.number3)+" &minus; <i>"+self.variable+"</i> &minus; "+str(self.number4)+" = "
            self.flag = 1
        else:
            self.problem = self.problem + str(self.number1)+"<i>"+self.variable+"</i> + "+str(self.number3)+" &minus; "+str(self.number2)+"<i>"+self.variable+"</i> &minus; "+str(self.number4)+" = "
            self.flag = 2   
                    
        self.answer = (self.number1-self.number2)*self.number5+self.number3-self.number4
        
        self.problem_type = "ProblemTypeMCQ9"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))        
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer-2))           
            
        self.answer = str(self.answer)                    
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.number5,self.variable,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)
        
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
        if CheckAnswerType==1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        if CheckAnswerType==2:
            try:
                answer= string.join(answer.split(),"")
                return (str(answer)==str(InputAnswer))
            except ValueError:
                return False               