'''
Created on Oct 12, 2011

Module: PercentIncDec
Generates "Finding percentage increase decrease" problems for Primary 6

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

class PercentIncDec:
    
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
        #return self.GenerateProblemType3()
        
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
        '''e.g: Initial number = 100
                Final number = 110
                Find the percentage increase?'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.InitialNumber = 100
        self.diff = randint(2,98)
        
        thing = random.choice(["caps","hats","toy cars","toys","children","paper clips","books","bottles","pencils","erasers","crayons","rubber bands","ice cream sticks","bottles","sharpeners","chairs","beads","marbles","t-shirts","shirts","bows","ties","books","cups","mugs","spoons","forks"])
            
        if randint(1,2) == 1:
            self.FinalNumber = self.InitialNumber + self.diff
            self.flag = 1
            self.problem1 = "The number of "+thing+" changed from "+str(self.InitialNumber)+" to "+str(self.FinalNumber)+". What is the percentage increase in the number of "+thing+"?"
            self.problem2 = "There were "+str(self.InitialNumber)+" "+thing+" at first. There are "+str(self.FinalNumber)+" "+thing+" now. Find the percentage increase in the number of "+thing+"."
            self.problem3 = "Initial number = "+str(self.InitialNumber)+"<br>Final number = "+str(self.FinalNumber)+"<br>Find the percentage increase."        
            self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        else:
            self.FinalNumber = self.InitialNumber - self.diff
            self.flag = 2
            self.problem1 = "The number of "+thing+" changed from "+str(self.InitialNumber)+" to "+str(self.FinalNumber)+". What is the percentage decrease in the number of "+thing+"?"
            self.problem2 = "There were "+str(self.InitialNumber)+" "+thing+" at first. There are "+str(self.FinalNumber)+" "+thing+" left now. Find the percentage decrease in the number of "+thing+"."
            self.problem3 = "Initial number = "+str(self.InitialNumber)+"<br>Final number = "+str(self.FinalNumber)+"<br>Find the percentage decrease."        
            self.problem = random.choice([self.problem1,self.problem2])

        self.answer = str(self.diff*100/self.InitialNumber)

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.InitialNumber,self.FinalNumber,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':"%"}

    def ExplainType1(self,problem,answer,InitialNumber,FinalNumber,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+"%"
        if flag == 1:
            self.solution_text = "<table>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Initial quantity</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(InitialNumber)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>New quantity</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(FinalNumber)+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Then,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Amount increased</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(FinalNumber)+" &minus; "+str(InitialNumber)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(FinalNumber-InitialNumber)+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Percentage increase</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td colspan='2' style='padding-top:7px;'><u>&nbsp;amount increased&nbsp;</u><br>initial quantity</td><td style='vertical-align:middle; text-align:left; padding-left:0px'>&times; 100%</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left; padding-left:0px; padding-right:0px'><table><tr><td style='padding-top:7px;'><u>&nbsp;"+str(FinalNumber-InitialNumber)+" &nbsp;</u><br>"+str(InitialNumber)+"</td><td style='vertical-align:middle; text-align:left; padding-left:0px'>&times; 100%</td></tr></table></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+"%</td></tr>"
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Percentage/Finding-Percentage-Increase-Decrease" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        elif flag == 2:
            self.solution_text = "<table>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Initial quantity</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(InitialNumber)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>New quantity</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(FinalNumber)+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Then,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Amount decreased</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(InitialNumber)+" &minus; "+str(FinalNumber)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(InitialNumber-FinalNumber)+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Percentage decrease</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td colspan='2' style='padding-top:7px;'><u>&nbsp;amount decreased&nbsp;</u><br>initial quantity</td><td style='vertical-align:middle; text-align:left; padding-left:0px'>&times; 100%</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left; padding-left:0px; padding-right:0px'><table><tr><td style='padding-top:7px;'><u>&nbsp;"+str(InitialNumber-FinalNumber)+" &nbsp;</u><br>"+str(InitialNumber)+"</td><td style='vertical-align:middle; text-align:left; padding-left:0px'>&times; 100%</td></tr></table></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+"%</td></tr>"
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Percentage/Finding-Percentage-Increase-Decrease" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):
        '''e.g: Initial number = 110
                Final number = 121
                Find the percentage change?'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.diff = randint(2,98)
        self.mutlitplier = random.choice([2,4,5,10,20,50])
        self.InitialNumber = self.diff * self.mutlitplier
        
        thing = random.choice(["caps","hats","toy cars","toys","children","paper clips","books","bottles","pencils","erasers","crayons","rubber bands","ice cream sticks","bottles","sharpeners","chairs","beads","marbles","t-shirts","shirts","bows","ties","books","cups","mugs","spoons","forks"])
            
        if randint(1,2) == 1:
            self.FinalNumber = self.InitialNumber + self.diff
            self.flag = 1
            self.problem1 = "The number of "+thing+" changed from "+str(self.InitialNumber)+" to "+str(self.FinalNumber)+". What is the percentage change in the number of "+thing+"?"
            self.problem2 = "There were "+str(self.InitialNumber)+" "+thing+" at first. There are "+str(self.FinalNumber)+" "+thing+" now. Find the percentage increase in the number of "+thing+"."
            self.problem3 = "Initial number = "+str(self.InitialNumber)+"<br>Final number = "+str(self.FinalNumber)+"<br>Find the percentage change."        
            self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        else:
            self.FinalNumber = self.InitialNumber - self.diff
            self.flag = 2
            self.problem1 = "The number of "+thing+" changed from "+str(self.InitialNumber)+" to "+str(self.FinalNumber)+". What is the percentage decrease in the number of "+thing+"?"
            self.problem2 = "There were "+str(self.InitialNumber)+" "+thing+" at first. There are "+str(self.FinalNumber)+" "+thing+" left now. Find the percentage change in the number of "+thing+"."
            self.problem3 = "Initial number = "+str(self.InitialNumber)+"<br>Final number = "+str(self.FinalNumber)+"<br>Find the percentage change."        
            self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = str(self.diff*100/self.InitialNumber)

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.InitialNumber,self.FinalNumber,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':"%"}

    def ExplainType2(self,problem,answer,InitialNumber,FinalNumber,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+"%"
        if flag == 1:
            self.solution_text = "<table>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Initial quantity</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(InitialNumber)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>New quantity</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(FinalNumber)+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Then,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Amount increased</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(FinalNumber)+" &minus; "+str(InitialNumber)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(FinalNumber-InitialNumber)+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Percentage increase</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td colspan='2' style='padding-top:7px;'><u>&nbsp;amount increased&nbsp;</u><br>initial quantity</td><td style='vertical-align:middle; text-align:left; padding-left:0px'>&times; 100%</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left; padding-left:0px; padding-right:0px'><table><tr><td style='padding-top:7px;'><u>&nbsp;"+str(FinalNumber-InitialNumber)+" &nbsp;</u><br>"+str(InitialNumber)+"</td><td style='vertical-align:middle; text-align:left; padding-left:0px'>&times; 100%</td></tr></table></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+"%</td></tr>"
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Percentage/Finding-Percentage-Increase-Decrease" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        elif flag == 2:
            self.solution_text = "<table>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Initial quantity</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(InitialNumber)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>New quantity</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(FinalNumber)+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Then,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Amount decreased</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(InitialNumber)+" &minus; "+str(FinalNumber)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(InitialNumber-FinalNumber)+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Percentage decrease</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td colspan='2' style='padding-top:7px;'><u>&nbsp;amount decreased&nbsp;</u><br>initial quantity</td><td style='vertical-align:middle; text-align:left; padding-left:0px'>&times; 100%</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left; padding-left:0px; padding-right:0px'><table><tr><td style='padding-top:7px;'><u>&nbsp;"+str(InitialNumber-FinalNumber)+" &nbsp;</u><br>"+str(InitialNumber)+"</td><td style='vertical-align:middle; text-align:left; padding-left:0px'>&times; 100%</td></tr></table></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+"%</td></tr>"
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Percentage/Finding-Percentage-Increase-Decrease" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain


    def GenerateProblemType3(self):
        '''e.g: Initial number = 48
                Final number = 56
                Find the percentage change?
                (Write your answer correct to 2 decimal places)'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.InitialNumber = randint(5,100)
        self.diff = randint(2,self.InitialNumber-1)        
            
        thing = random.choice(["caps","hats","toy cars","toys","children","paper clips","books","bottles","pencils","erasers","crayons","rubber bands","ice cream sticks","bottles","sharpeners","chairs","beads","marbles","t-shirts","shirts","bows","ties","books","cups","mugs","spoons","forks"])
            
        if randint(1,2) == 1:
            self.FinalNumber = self.InitialNumber + self.diff
            self.flag = 1
            self.problem1 = "The number of "+thing+" changed from "+str(self.InitialNumber)+" to "+str(self.FinalNumber)+". What is the percentage increase in the number of "+thing+"?"
            self.problem2 = "There were "+str(self.InitialNumber)+" "+thing+" at first. There are "+str(self.FinalNumber)+" "+thing+" now. Find the percentage increase in the number of "+thing+"."
            self.problem3 = "Initial number = "+str(self.InitialNumber)+"<br>Final number = "+str(self.FinalNumber)+"<br>Find the percentage increase."        
            self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        else:
            self.FinalNumber = self.InitialNumber - self.diff
            self.flag = 2
            self.problem1 = "The number of "+thing+" changed from "+str(self.InitialNumber)+" to "+str(self.FinalNumber)+". What is the percentage decrease in the number of "+thing+"?"
            self.problem2 = "There were "+str(self.InitialNumber)+" "+thing+" at first. There are "+str(self.FinalNumber)+" "+thing+" left now. Find the percentage decrease in the number of "+thing+"."
            self.problem3 = "Initial number = "+str(self.InitialNumber)+"<br>Final number = "+str(self.FinalNumber)+"<br>Find the percentage decrease."        
            self.problem = random.choice([self.problem1,self.problem2])
        self.problem = self.problem + "<br><br><font style='font-size:0.8em'>(Write your answer correct to two decimal places.)</font>"

        self.answer = str(round(float(self.diff)*100/self.InitialNumber,2))

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.InitialNumber,self.FinalNumber,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':"%"}

    def ExplainType3(self,problem,answer,InitialNumber,FinalNumber,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+"%"
        if flag == 1:
            self.solution_text = "<table>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Initial quantity</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(InitialNumber)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>New quantity</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(FinalNumber)+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Then,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Amount increased</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(FinalNumber)+" &minus; "+str(InitialNumber)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(FinalNumber-InitialNumber)+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Percentage increase</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td colspan='2' style='padding-top:7px;'><u>&nbsp;amount increased&nbsp;</u><br>initial quantity</td><td style='vertical-align:middle; text-align:left; padding-left:0px'>&times; 100%</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left; padding-left:0px; padding-right:0px'><table><tr><td style='padding-top:7px;'><u>&nbsp;"+str(FinalNumber-InitialNumber)+" &nbsp;</u><br>"+str(InitialNumber)+"</td><td style='vertical-align:middle; text-align:left; padding-left:0px'>&times; 100%</td></tr></table></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+"%</td></tr>"
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Percentage/Finding-Percentage-Increase-Decrease" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        elif flag == 2:
            self.solution_text = "<table>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Initial quantity</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(InitialNumber)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>New quantity</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(FinalNumber)+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Then,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Amount decreased</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(InitialNumber)+" &minus; "+str(FinalNumber)+"</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(InitialNumber-FinalNumber)+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left; vertical-align:middle'>Percentage decrease</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td colspan='2' style='padding-top:7px;'><u>&nbsp;amount decreased&nbsp;</u><br>initial quantity</td><td style='vertical-align:middle; text-align:left; padding-left:0px'>&times; 100%</td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px; vertical-align:middle'>=</td><td style='text-align:left; padding-left:0px; padding-right:0px'><table><tr><td style='padding-top:7px;'><u>&nbsp;"+str(InitialNumber-FinalNumber)+" &nbsp;</u><br>"+str(InitialNumber)+"</td><td style='vertical-align:middle; text-align:left; padding-left:0px'>&times; 100%</td></tr></table></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+"%</td></tr>"
            self.solution_text = self.solution_text + "</table>"
            self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Percentage/Finding-Percentage-Increase-Decrease" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        
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
        '''e.g: Initial number = 100
                Final number = 110
                Find the percentage increase?'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.InitialNumber = 100
        self.diff = randint(2,98)
        
        thing = random.choice(["caps","hats","toy cars","toys","children","paper clips","books","bottles","pencils","erasers","crayons","rubber bands","ice cream sticks","bottles","sharpeners","chairs","beads","marbles","t-shirts","shirts","bows","ties","books","cups","mugs","spoons","forks"])
            
        if randint(1,2) == 1:
            self.FinalNumber = self.InitialNumber + self.diff
            self.flag = 1
            self.problem1 = "The number of "+thing+" changed from "+str(self.InitialNumber)+" to "+str(self.FinalNumber)+". What is the percentage increase in the number of "+thing+"?"
            self.problem2 = "There were "+str(self.InitialNumber)+" "+thing+" at first. There are "+str(self.FinalNumber)+" "+thing+" now. Find the percentage increase in the number of "+thing+"."
            self.problem3 = "Initial number = "+str(self.InitialNumber)+"<br>Final number = "+str(self.FinalNumber)+"<br>Find the percentage increase."        
            self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        else:
            self.FinalNumber = self.InitialNumber - self.diff
            self.flag = 2
            self.problem1 = "The number of "+thing+" changed from "+str(self.InitialNumber)+" to "+str(self.FinalNumber)+". What is the percentage decrease in the number of "+thing+"?"
            self.problem2 = "There were "+str(self.InitialNumber)+" "+thing+" at first. There are "+str(self.FinalNumber)+" "+thing+" left now. Find the percentage decrease in the number of "+thing+"."
            self.problem3 = "Initial number = "+str(self.InitialNumber)+"<br>Final number = "+str(self.FinalNumber)+"<br>Find the percentage decrease."        
            self.problem = random.choice([self.problem1,self.problem2])
            
        self.answer = self.diff*100/self.InitialNumber
                
        self.problem_type = "ProblemTypeMCQ1"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))

        self.answer = str(self.answer)          
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.InitialNumber,self.FinalNumber,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def GenerateProblemTypeMCQ2(self):
        '''e.g: Initial number = 110
                Final number = 121
                Find the percentage change?'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.diff = randint(2,98)
        self.mutlitplier = random.choice([2,4,5,10,20,50])
        self.InitialNumber = self.diff * self.mutlitplier

        thing = random.choice(["caps","hats","toy cars","toys","children","paper clips","books","bottles","pencils","erasers","crayons","rubber bands","ice cream sticks","bottles","sharpeners","chairs","beads","marbles","t-shirts","shirts","bows","ties","books","cups","mugs","spoons","forks"])
            
        if randint(1,2) == 1:
            self.FinalNumber = self.InitialNumber + self.diff
            self.flag = 1
            self.problem1 = "The number of "+thing+" changed from "+str(self.InitialNumber)+" to "+str(self.FinalNumber)+". What is the percentage change in the number of "+thing+"?"
            self.problem2 = "There were "+str(self.InitialNumber)+" "+thing+" at first. There are "+str(self.FinalNumber)+" "+thing+" now. Find the percentage increase in the number of "+thing+"."
            self.problem3 = "Initial number = "+str(self.InitialNumber)+"<br>Final number = "+str(self.FinalNumber)+"<br>Find the percentage change."        
            self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        else:
            self.FinalNumber = self.InitialNumber - self.diff
            self.flag = 2
            self.problem1 = "The number of "+thing+" changed from "+str(self.InitialNumber)+" to "+str(self.FinalNumber)+". What is the percentage decrease in the number of "+thing+"?"
            self.problem2 = "There were "+str(self.InitialNumber)+" "+thing+" at first. There are "+str(self.FinalNumber)+" "+thing+" left now. Find the percentage change in the number of "+thing+"."
            self.problem3 = "Initial number = "+str(self.InitialNumber)+"<br>Final number = "+str(self.FinalNumber)+"<br>Find the percentage change."        
            self.problem = random.choice([self.problem1,self.problem2])

        self.answer = self.diff*100/self.InitialNumber
                
        self.problem_type = "ProblemTypeMCQ2"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.InitialNumber,self.FinalNumber,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def GenerateProblemTypeMCQ3(self):
        '''e.g: Initial number = 48
                Final number = 56
                Find the percentage change?
                (Write your answer correct to 2 decimal places)'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.InitialNumber = randint(5,100)
        self.diff = randint(2,self.InitialNumber-1)        
            
        thing = random.choice(["caps","hats","toy cars","toys","children","paper clips","books","bottles","pencils","erasers","crayons","rubber bands","ice cream sticks","bottles","sharpeners","chairs","beads","marbles","t-shirts","shirts","bows","ties","books","cups","mugs","spoons","forks"])
            
        if randint(1,2) == 1:
            self.FinalNumber = self.InitialNumber + self.diff
            self.flag = 1
            self.problem1 = "The number of "+thing+" changed from "+str(self.InitialNumber)+" to "+str(self.FinalNumber)+". What is the percentage increase in the number of "+thing+"?"
            self.problem2 = "There were "+str(self.InitialNumber)+" "+thing+" at first. There are "+str(self.FinalNumber)+" "+thing+" now. Find the percentage increase in the number of "+thing+"."
            self.problem3 = "Initial number = "+str(self.InitialNumber)+"<br>Final number = "+str(self.FinalNumber)+"<br>Find the percentage increase."        
            self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        else:
            self.FinalNumber = self.InitialNumber - self.diff
            self.flag = 2
            self.problem1 = "The number of "+thing+" changed from "+str(self.InitialNumber)+" to "+str(self.FinalNumber)+". What is the percentage decrease in the number of "+thing+"?"
            self.problem2 = "There were "+str(self.InitialNumber)+" "+thing+" at first. There are "+str(self.FinalNumber)+" "+thing+" left now. Find the percentage decrease in the number of "+thing+"."
            self.problem3 = "Initial number = "+str(self.InitialNumber)+"<br>Final number = "+str(self.FinalNumber)+"<br>Find the percentage decrease."        
            self.problem = random.choice([self.problem1,self.problem2])
        self.problem = self.problem + "<br><br><font style='font-size:0.8em'>(Write your answer correct to two decimal places.)</font>"
        
        self.answer = round(float(self.diff)*100/self.InitialNumber,2)
                
        self.problem_type = "ProblemTypeMCQ3"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+.01))
        self.wrongAnswers.append(str(self.answer+.05))
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1.01))
        self.wrongAnswers.append(str(self.answer-2.05))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.InitialNumber,self.FinalNumber,self.flag)
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
        if CheckType==2:
            try:
                return (float(answer)==float(AnswerInput))
            except ValueError:
                return False               