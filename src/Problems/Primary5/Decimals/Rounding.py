'''
Created on Jan 18, 2011

Module: Rounding
Generates "Rounding Decimals to nearest whole numbers, 1 decimal or 2 decimal places" problems for Primary 5

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
from Problems import PersonName

class Rounding:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        self.ProblemType = random.choice([self.GenerateProblemType1(),self.GenerateProblemType2()
                                          ,self.GenerateProblemType3(),self.GenerateProblemType4()
                                          ,self.GenerateProblemTypeMCQ1(),self.GenerateProblemTypeMCQ2()
                                          ,self.GenerateProblemTypeMCQ3(),self.GenerateProblemTypeMCQ4()])
        return self.ProblemType
        #return self.GenerateProblemTypeMCQ4()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType5","ProblemTypeMCQ5",],
                            6:["ProblemType6","ProblemTypeMCQ6",],
                            7:["ProblemType7a","ProblemType7b","ProblemType7c","ProblemType7d","ProblemTypeMCQ7a","ProblemTypeMCQ7b","ProblemTypeMCQ7c","ProblemTypeMCQ7d",],
                            8:["ProblemType8","ProblemTypeMCQ8",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemType5(),self.GenerateProblemTypeMCQ5(),],
                                    6:[self.GenerateProblemType6(),self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemType7a(),self.GenerateProblemTypeMCQ7a(),self.GenerateProblemType7b(),self.GenerateProblemTypeMCQ7b(),self.GenerateProblemType7c(),self.GenerateProblemTypeMCQ7c(),self.GenerateProblemType7d(),self.GenerateProblemTypeMCQ7d(),],
                                    8:[self.GenerateProblemType8(),self.GenerateProblemTypeMCQ8(),],
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
        #return self.GenerateProblemTypeMCQ8()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7a":self.GenerateProblemType7a(),
                            "ProblemType7b":self.GenerateProblemType7b(),
                            "ProblemType7c":self.GenerateProblemType7c(),
                            "ProblemType7d":self.GenerateProblemType7d(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemTypeMCQ7a":self.GenerateProblemTypeMCQ7a(),
                            "ProblemTypeMCQ7b":self.GenerateProblemTypeMCQ7b(),
                            "ProblemTypeMCQ7c":self.GenerateProblemTypeMCQ7c(),
                            "ProblemTypeMCQ7d":self.GenerateProblemTypeMCQ7d(),
                            "ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g.:
        Add the numbers and round off the answer to 1 decimal place.'''
        self.complexity_level = "easy"
        self.HCScore = 3        
             
        self.number1 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number = float(self.number1)+float(self.number2)
        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.number = float(self.number1)+float(self.number2)
        #making sure that there are 2 digits after decimal
        if len(str(self.number).partition(".")[2]) == 1:
            self.number1 = str(float(self.number1) + 0.01)
            self.number = float(self.number1)+float(self.number2)
            
        self.round = randint(1,len(str(self.number).partition(".")[2])-1)
        if self.round==3:
            self.round = 2
        
        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(self.number,1)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(self.number,2)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        
        self.problem1 = "Add the following numbers and round off your answer to %s:<br><br>&nbsp;&nbsp;&nbsp; %s + %s"%(self.places[0],self.number1,self.number2)
        self.problem2 = "Find the sum of %s and %s, correct to %s."%(self.number1,self.number2,self.places[0])
        self.problem3 = "What is the sum of %s and %s? Give your answer correct to %s."%(self.number1,self.number2,self.places[0])
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.places[0],self.places[1],self.round,self.numberLine1,self.numberLine2,self.numberLine3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}
        
    def ExplainType1(self,problem,answer,number1,number2,place1,place2,round,numberLine1,numberLine2,numberLine3):

        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        number = float(number1)+float(number2)
        self.WholeNumber = str(number).partition(".")[0]
        self.decimal = str(number).partition(".")[2]
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Getting the answer,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'><b>"+number1+" + " +number2+"</b></td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(float(number1)+float(number2))+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Rounding off the answer to "+place1+",</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(float(number1)+float(number2))+" is between "+str(numberLine1)+"0"+" and "+str(numberLine2)+"0.</td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(float(number1)+float(number2))+" is closer to "+str(answer)+"0"+" than to "+str(numberLine3)+"0"+".</td></tr>"
        if (int(self.decimal[round])>=5):
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(float(number1)+float(number2))+" is "+self.WholeNumber+"."+self.decimal[:round-1]+"<span style='color:yellow'>"+str(int(self.decimal[round-1])+1)+"</span> when rounded off to "+place1+".</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(float(number1)+float(number2))+" is "+self.WholeNumber+"."+self.decimal[:round-1]+"<span style='color:yellow'>"+str(int(self.decimal[round-1]))+"</span> when rounded off to "+place1+".</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='5'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:top'>"+str(float(number1)+float(number2))+"</b></td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>&asymp;</td><td style='text-align:left;vertical-align:top'><b>"+str(answer)+"</b></td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:300px;font-size:.8em;'>When rounding off a decimal to <b>"+place1+"</b>, consider the digit in the <b>"+place2+"</b> only.</div></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.:
        Add the numbers and round off the answer to the nearest whole number.'''
        self.complexity_level = "easy"
        self.HCScore = 3        
             
        self.number1 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number = float(self.number1)+float(self.number2)
        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.number = float(self.number1)+float(self.number2)
            
        #Choose which phrase to use in the problem statement: ones place or nearest whole number
        self.onesPlace = ["the ones place","tenths place"]
        self.wholeNumberPlace = ["the nearest whole number","1st decimal place"]
        self.places = random.choice([self.onesPlace,self.wholeNumberPlace])
        
        self.problem1 = "Add the following numbers and round off your answer to %s:<br><br>&nbsp;&nbsp;&nbsp; %s + %s"%(self.places[0],self.number1,self.number2)
        self.problem2 = "Find the sum of %s and %s, correct to %s."%(self.number1,self.number2,self.places[0])
        self.problem3 = "What is the sum of %s and %s? Give your answer correct to %s."%(self.number1,self.number2,self.places[0])
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.answer = int(round(float(self.number1)+float(self.number2),0))
        if self.answer > self.number:
            self.numberLine1 = self.answer - 1
            self.numberLine2 = self.answer
            self.numberLine3 = self.numberLine1
        else:
            self.numberLine2 = self.answer + 1
            self.numberLine1 = self.answer
            self.numberLine3 = self.numberLine2
                      
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.places[0],self.places[1],0,self.numberLine1,self.numberLine2,self.numberLine3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}
        
    def ExplainType2(self,problem,answer,number1,number2,place1,place2,round,numberLine1,numberLine2,numberLine3):

        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        number = float(number1)+float(number2)
        self.WholeNumber = str(number).partition(".")[0]
        self.decimal = str(number).partition(".")[2]
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Getting the answer,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'><b>"+number1+" + " +number2+"</b></td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(float(number1)+float(number2))+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Rounding off the answer to "+place1+",</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(float(number1)+float(number2))+" is between "+str(numberLine1)+"."+"0"*len(self.decimal)+" and "+str(numberLine2)+"."+"0"*len(self.decimal)+".</td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(float(number1)+float(number2))+" is closer to "+str(answer)+"."+"0"*len(self.decimal)+" than to "+str(numberLine3)+"."+"0"*len(self.decimal)+".</td></tr>"
        if (int(self.decimal[round])>=5):
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(float(number1)+float(number2))+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(float(number1)+float(number2))+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='5'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:top'>"+str(float(number1)+float(number2))+"</b></td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>&asymp;</td><td style='text-align:left;vertical-align:top'><b>"+str(answer)+"</b></td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:300px;font-size:.8em;'>When rounding off a decimal to <b>"+place1+"</b>, consider the digit in the <b>"+place2+"</b> only.</div></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):
        '''e.g.:
        Subtract the numbers and round off the answer to 1 decimal place.'''
        self.complexity_level = "easy"
        self.HCScore = 3        
             
        self.number1 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number = abs(float(self.number1)-float(self.number2))
        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.number = abs(float(self.number1)-float(self.number2))
        #making sure that there are 2 digits after decimal
        if len(str(self.number).partition(".")[2]) == 1:
            self.number1 = str(float(self.number1) + 0.01)
            self.number = abs(float(self.number1)-float(self.number2))        
            
        self.round = randint(1,len(str(self.number).partition(".")[2])-1)
        if self.round==3:
            self.round = 2

        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(self.number,1)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(self.number,2)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                

        if float(self.number2) > float(self.number1):
            self.number2, self.number1 = self.number1, self.number2

        self.problem1 = "Subtract the following numbers and round off your answer to %s:<br><br>&nbsp;&nbsp;&nbsp; %s &nbsp;&minus;&nbsp; %s"%(self.places[0],self.number1,self.number2)
        self.problem2 = "Find the difference of %s and %s, correct to %s."%(self.number1,self.number2,self.places[0])
        self.problem3 = "What is the difference of %s and %s? Give your answer correct to %s."%(self.number1,self.number2,self.places[0])
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.places[0],self.places[1],self.round,self.numberLine1,self.numberLine2,self.numberLine3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType3(self,problem,answer,number1,number2,place1,place2,round,numberLine1,numberLine2,numberLine3):

        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        number = float(number1)-float(number2)
        self.WholeNumber = str(number).partition(".")[0]
        self.decimal = str(number).partition(".")[2]
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Getting the answer,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'><b>"+number1+" - " +number2+"</b></td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Rounding off the answer to "+place1+",</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is between "+str(numberLine1)+"0"+" and "+str(numberLine2)+"0.</td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is closer to "+str(answer)+"0"+" than to "+str(numberLine3)+"0"+".</td></tr>"
        if (int(self.decimal[round])>=5):
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+self.WholeNumber+"."+self.decimal[:round-1]+"<span style='color:yellow'>"+str(int(self.decimal[round-1])+1)+"</span> when rounded off to "+place1+".</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+self.WholeNumber+"."+self.decimal[:round-1]+"<span style='color:yellow'>"+str(int(self.decimal[round-1]))+"</span> when rounded off to "+place1+".</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='5'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:top'>"+str(number)+"</b></td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>&asymp;</td><td style='text-align:left;vertical-align:top'><b>"+str(answer)+"</b></td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:300px;font-size:.8em;'>When rounding off a decimal to <b>"+place1+"</b>, consider the digit in the <b>"+place2+"</b> only.</div></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4(self):
        '''e.g.:
        Add the numbers and round off the answer to the nearest whole number.'''
        self.complexity_level = "easy"
        self.HCScore = 3        
             
        self.number1 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number = abs(float(self.number1)-float(self.number2))
        if self.number<1:
            self.number1 = str(float(self.number1) + 1)
        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.number = abs(float(self.number1)-float(self.number2))

        #Choose which phrase to use in the problem statement: ones place or nearest whole number
        self.onesPlace = ["the ones place","tenths place"]
        self.wholeNumberPlace = ["the nearest whole number","1st decimal place"]
        self.places = random.choice([self.onesPlace,self.wholeNumberPlace])
        
        if float(self.number2) > float(self.number1):
            self.number2,self.number1 = self.number1,self.number2

        self.problem1 = "Subtract the following numbers and round off your answer to the %s:<br><br>&nbsp;&nbsp;&nbsp; %s &nbsp;&minus;&nbsp; %s"%(self.places[0],self.number1,self.number2)
        self.problem2 = "Find the difference of %s and %s, correct to the %s."%(self.number1,self.number2,self.places[0])
        self.problem3 = "What is the difference of %s and %s? Give your answer correct to the %s."%(self.number1,self.number2,self.places[0])
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.answer = int(round(abs(float(self.number1)-float(self.number2)),0))          
        if self.answer > self.number:
            self.numberLine1 = self.answer - 1
            self.numberLine2 = self.answer
            self.numberLine3 = self.numberLine1
        else:
            self.numberLine2 = self.answer + 1
            self.numberLine1 = self.answer
            self.numberLine3 = self.numberLine2

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.places[0],self.places[1],0,self.numberLine1,self.numberLine2,self.numberLine3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}
        
    def ExplainType4(self,problem,answer,number1,number2,place1,place2,round,numberLine1,numberLine2,numberLine3):

        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        number = float(number1)-float(number2)
        self.WholeNumber = str(number).partition(".")[0]
        self.decimal = str(number).partition(".")[2]
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Getting the answer,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'><b>"+number1+" - " +number2+"</b></td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Rounding off the answer to "+place1+",</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is between "+str(numberLine1)+"."+"0"*len(self.decimal)+" and "+str(numberLine2)+"."+"0"*len(self.decimal)+".</td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is closer to "+str(answer)+"."+"0"*len(self.decimal)+" than to "+str(numberLine3)+"."+"0"*len(self.decimal)+".</td></tr>"
        if (int(self.decimal[round])>=5):
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='5'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:top'>"+str(number)+"</b></td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>&asymp;</td><td style='text-align:left;vertical-align:top'><b>"+str(answer)+"</b></td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:300px;font-size:.8em;'>When rounding off a decimal to <b>"+place1+"</b>, consider the digit in the <b>"+place2+"</b> only.</div></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5(self):
        '''e.g.:
        Add the numbers and round off the answer to the nearest whole number.'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        
        self.items = random.choice(['packages','bags of plain flour','packets of coarse sugar','bags of seeds','packets of basmati rice',
                      'boxes of chocolate chip cookies','cans of evaporated milk','blocks of wood','books','boxes','bricks','boxes','bags of apples',])
             
        self.number1 = str(randint(1,2))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(1,2))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number3 = str(randint(1,2))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number4 = str(randint(1,2))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        
        self.numbers = [self.number1,self.number2,self.number3,self.number4]
        self.TotalNumbers = randint(2,4)
        
        self.number = 0
        for i in range(self.TotalNumbers):
            self.number = self.number + float(self.numbers[i])
            
        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.numbers[0] = str(float(self.number1) + 0.55)
            self.number = 0
            for i in range(self.TotalNumbers):
                self.number = self.number + float(self.numbers[i])
            
        #Choose which phrase to use in the problem statement: ones place or nearest whole number
        self.onesPlace = ["the ones place","tenths place"]
        self.wholeNumberPlace = ["the nearest whole number","1st decimal place"]
        self.places = random.choice([self.onesPlace,self.wholeNumberPlace])
        
        self.problem1 = "The masses of "+str(self.TotalNumbers)+" "+self.items+" are "+str(self.numbers[0])+" kg"
        if self.TotalNumbers == 2:
            self.problem1 = self.problem1 + " and "+str(self.numbers[1])+" kg."
        elif self.TotalNumbers ==3:
            self.problem1 = self.problem1 + ", "+str(self.numbers[1])+" kg and "+str(self.numbers[2])+" kg."
        else:
            self.problem1 = self.problem1 + ", "+str(self.numbers[1])+" kg, "+str(self.numbers[2])+" kg and "+str(self.numbers[3])+" kg."
        
        self.problem1 = self.problem1 +  " Find the total mass of the "+str(self.TotalNumbers)+" "+self.items+". Give your answer correct to the nearest kilogram." 

        self.problem2 = "What is the total mass of "+str(self.TotalNumbers)+" "+self.items+" that have individual masses of "+str(self.numbers[0])+" kg"
        
        if self.TotalNumbers == 2:
            self.problem2 = self.problem2 + " and "+str(self.numbers[1])+" kg."
        elif self.TotalNumbers ==3:
            self.problem2 = self.problem2 + ", "+str(self.numbers[1])+" kg and "+str(self.numbers[2])+" kg."
        else:
            self.problem2 = self.problem2 + ", "+str(self.numbers[1])+" kg, "+str(self.numbers[2])+" kg and "+str(self.numbers[3])+" kg."

        self.problem2 = self.problem2 + " Round off your answer to the nearest kilogram."

        self.problem = random.choice([self.problem1,self.problem2])

        self.answer = int(round(self.number,0))
        if self.answer > self.number:
            self.numberLine1 = self.answer - 1
            self.numberLine2 = self.answer
            self.numberLine3 = self.numberLine1
        else:
            self.numberLine2 = self.answer + 1
            self.numberLine1 = self.answer
            self.numberLine3 = self.numberLine2
                      
        self.unit = "kg"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number,self.numbers,self.places[0],self.places[1],0,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.TotalNumbers,self.items,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}
        
    def ExplainType5(self,problem,answer,number,numbers,place1,place2,round,numberLine1,numberLine2,numberLine3,TotalNumbers,item,unit):

        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.WholeNumber = str(number).partition(".")[0]
        self.decimal = str(number).partition(".")[2]
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Getting the answer,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>Total mass of "+str(TotalNumbers)+" "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td>"
        if TotalNumbers == 2:
            self.solution_text = self.solution_text + "<td style='text-align:left'>"+numbers[0]+" + " +numbers[1]+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+"</td></tr></table>"
        elif TotalNumbers == 3:
            self.solution_text = self.solution_text + "<td style='text-align:left'>"+numbers[0]+" + " +numbers[1]+" + " +numbers[2]+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+"</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<td style='text-align:left'>"+numbers[0]+" + " +numbers[1]+" + " +numbers[2]+" + " +numbers[3]+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+"</td></tr></table>"
            
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Rounding off the answer to "+place1+",</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is between "+str(numberLine1)+"."+"0"*len(self.decimal)+" and "+str(numberLine2)+"."+"0"*len(self.decimal)+".</td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is closer to "+str(answer)+"."+"0"*len(self.decimal)+" than to "+str(numberLine3)+"."+"0"*len(self.decimal)+".</td></tr>"
        if (int(self.decimal[round])>=5):
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='5'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:top'>"+str(number)+"</b></td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>&asymp;</td><td style='text-align:left;vertical-align:top'><b>"+str(answer)+"</b></td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:300px;font-size:.8em;'>When rounding off a decimal to <b>"+place1+"</b>, consider the digit in the <b>"+place2+"</b> only.</div></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6(self):
        '''e.g.:
        A [can] had <decimal1> litre(s) of [juice]. [Person.name] poured out <decimal2> litre(s) of [juice] from it.How much [juice] is left in the [can]. Round off your 
        answer to the hundredths place. (Or the tenths place)'''
        
        self.complexity_level = "medium"
        self.HCScore = 5        
        
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice([['tomato ketchup','bottle'],['sparkling water','bottle'],['mango juice','cup'],['strawberry milk','mug'],['chocolate milk','carton'],
                                    ['oil paint','can'],['soda','cup'],['cooking oil','can'],['liquid','container'],['green tea','cup']])
             
        self.number1 = str(1)+"."+random.choice([str(randint(100,200)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(0)+"."+random.choice([str(randint(100,800)),str(randint(1,99)),str(0)+str(randint(1,99))])
        
        self.number = float(self.number1)-float(self.number2)
        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.number = float(self.number1)-float(self.number2)
        #making sure that there are 2 digits after decimal
        if len(str(self.number).partition(".")[2]) == 1:
            self.number1 = str(float(self.number1) + 0.01)
            self.number = float(self.number1)-float(self.number2)        
            
        self.round = randint(1,len(str(self.number).partition(".")[2])-1)
        if self.round==3:
            self.round = 2

        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(self.number,1)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(self.number,2)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        
        self.problem1 = "A "+self.items[1]+" had "+self.number1+" litres of "+self.items[0]+". "
        self.problem1 = self.problem1 + self.name+ " poured out "+self.number2+" litre of "+self.items[0]+" from it. "
        self.problem1 = self.problem1 + "How much "+self.items[0]+" is left in the "+self.items[1]+". Round off your answer to "+self.places[0]+"." 

        self.problem2 = self.name+" pours out "+self.number2+" litre of "+self.items[0]+" from a "+self.items[1]+" that had "+self.number1+" litres of "+self.items[0]+" at first. "
        self.problem2 = self.problem2 + "Find the volume of "+self.items[0]+" left in the "+self.items[1]+" rounded off to "+self.places[0]+"."

        self.problem = random.choice([self.problem1,self.problem2])

                      
        if self.answer>1:
            self.unit = "litres"
        else:
            self.unit = "litre"
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.places[0],self.places[1],self.round,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.unit,self.items[0],self.items[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6",'grade':5,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType6(self,problem,answer,number1,number2,place1,place2,round,numberLine1,numberLine2,numberLine3,unit,item1,item2):

        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        number = float(number1)-float(number2)
        self.WholeNumber = str(number).partition(".")[0]
        self.decimal = str(number).partition(".")[2]
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Getting the answer,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>"+item1+" left in the "+item2+"</td><td style='padding-left:0px; padding-right:0px'>=</td>"
        self.solution_text = self.solution_text + "<td style='text-align:left'><b>"+number1+" - " +number2+"</b></td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+"</td></tr></table>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Rounding off the answer to "+place1+",</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is between "+str(numberLine1)+"0"+" and "+str(numberLine2)+"0.</td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is closer to "+str(answer)+"0"+" than to "+str(numberLine3)+"0"+".</td></tr>"
        if (int(self.decimal[round])>=5):
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+self.WholeNumber+"."+self.decimal[:round-1]+"<span style='color:yellow'>"+str(int(self.decimal[round-1])+1)+"</span> when rounded off to "+place1+".</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+self.WholeNumber+"."+self.decimal[:round-1]+"<span style='color:yellow'>"+str(int(self.decimal[round-1]))+"</span> when rounded off to "+place1+".</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='5'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:top'>"+str(number)+"</b></td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>&asymp;</td><td style='text-align:left;vertical-align:top'><b>"+str(answer)+"</b></td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:300px;font-size:.8em;'>When rounding off a decimal to <b>"+place1+"</b>, consider the digit in the <b>"+place2+"</b> only.</div></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7a(self):
        '''e.g.:
        [Person.Boyname1] [bicycled] <decimal1> km while [Person.Boyname2] [bicycled] <decimal2> km. What is the total distance the two boys [bicycled] rounded off to 1 decimal place?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        
        self.items = random.choice(['bicycled','cycled','ran','skated','jogged','walked'])
        
        self.names = random.sample(PersonName.BoyName,2)
             
        self.number1 = str(randint(3,10))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(3,10))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        
        self.numbers = [self.number1,self.number2]
        
        self.number = float(self.number1) + float(self.number2)            

        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.numbers[0] = self.number1
            self.number = float(self.number1)+float(self.number2)
        #making sure that there are 2 digits after decimal
        if len(str(self.number).partition(".")[2]) == 1:
            self.number1 = str(float(self.number1) + 0.01)
            self.numbers[0] = self.number1
            self.number = float(self.number1)+float(self.number2)        
            
        self.round = randint(1,len(str(self.number).partition(".")[2])-1)
        if self.round==3:
            self.round = 2

        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(self.number,1)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(self.number,2)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        
        self.problem = self.names[0]+" "+self.items+" "+self.number1+" km while "+self.names[1]+" "+self.items+" "+self.number2+" km. What is the total distance the two boys "+self.items+" rounded off to "+self.places[0]+"?"

        self.unit = "km"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7a(self.problem,self.answer,self.number,self.numbers,self.places[0],self.places[1],0,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.items,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7a",'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}
        
    def ExplainType7a(self,problem,answer,number,numbers,place1,place2,round,numberLine1,numberLine2,numberLine3,item,unit):

        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.WholeNumber = str(number).partition(".")[0]
        self.decimal = str(number).partition(".")[2]
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Getting the answer,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>Total distance "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td>"
        self.solution_text = self.solution_text + "<td style='text-align:left'>"+numbers[0]+" + " +numbers[1]+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+" "+unit+"</td></tr></table>"
            
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Rounding off the answer to "+place1+",</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is between "+str(numberLine1)+"0 and "+str(numberLine2)+"0.</td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is closer to "+str(answer)+"0 than to "+str(numberLine3)+"0.</td></tr>"
        if (int(self.decimal[round])>=5):
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='5'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:top'>"+str(number)+"</b></td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>&asymp;</td><td style='text-align:left;vertical-align:top'><b>"+str(answer)+"</b></td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:300px;font-size:.8em;'>When rounding off a decimal to <b>"+place1+"</b>, consider the digit in the <b>"+place2+"</b> only.</div></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7b(self):
        '''e.g.:
        [Person.Boyname1] [bicycled] <decimal1> km while [Person.Boyname2] [bicycled] <decimal2> km. What is the total distance the two boys [bicycled] rounded off to 1 decimal place?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        
        self.items = random.choice(['bicycled','cycled','ran','skated','jogged','walked'])
        
        self.names = random.sample(PersonName.BoyName,2)
             
        self.number1 = str(randint(3,10))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(3,10))+"."+str(randint(100,999))
        
        self.numbers = [self.number1,self.number2]
        
        self.number = float(self.number1) + float(self.number2)            

        self.round = randint(1,2)
        
        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(float(self.number2),1)
            self.answer = float(self.answer)
            if self.answer > float(self.number2):
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(float(self.number2),2)
            self.answer = float(self.answer)
            if self.answer > float(self.number2):
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        
        self.problem = self.names[0]+" and "+self.names[1]+" "+self.items+" a total distance of "+str(self.number)+" km. If "+self.names[0]+" "+self.items+" "+self.number1+" km, find the distance that "+self.names[1]+" "+self.items+", correct to "+self.places[0]+"."

        self.unit = "km"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7b(self.problem,self.answer,self.number,self.numbers,self.places[0],self.places[1],0,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.items,self.unit,self.names)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7b",'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}
        
    def ExplainType7b(self,problem,answer,number,numbers,place1,place2,round,numberLine1,numberLine2,numberLine3,item,unit,names):

        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.WholeNumber = numbers[1].partition(".")[0]
        self.decimal = numbers[1].partition(".")[2]
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Getting the answer,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>Distance "+item+" by "+names[1]+"</td><td style='padding-left:0px; padding-right:0px'>=</td>"
        self.solution_text = self.solution_text + "<td style='text-align:left'>"+str(number)+" - " +numbers[0]+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(numbers[1])+" "+unit+"</td></tr></table>"
            
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Rounding off the answer to "+place1+",</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(numbers[1])+" is between "+str(numberLine1)+"0 and "+str(numberLine2)+"0.</td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(numbers[1])+" is closer to "+str(answer)+"0 than to "+str(numberLine3)+"0.</td></tr>"
        if (int(self.decimal[round])>=5):
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(numbers[1])+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(numbers[1])+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='5'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:top'>"+str(numbers[1])+"</b></td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>&asymp;</td><td style='text-align:left;vertical-align:top'><b>"+str(answer)+"</b></td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:300px;font-size:.8em;'>When rounding off a decimal to <b>"+place1+"</b>, consider the digit in the <b>"+place2+"</b> only.</div></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7c(self):
        '''e.g.:
        In a certain relay race, each of the <four> members in a team [bicycled] an equal distance. What distance did each member [bicycle] if the total distance covered by the team was <decimal1>? Round off your answer to 2 decimal places.'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        
        self.items = random.choice([['bicycled','bicycle'],['cycled','cycle'],['ran','run'],['skated','skate'],['walked','walk']])        
             
        self.number1 = str(randint(3,10))+"."+str(randint(1,9))+str(randint(1,9))+str(randint(1,9))
        
        self.TotalNumbers = randint(2,4)
        
        self.number = float(self.number1) * self.TotalNumbers            

        self.round = randint(1,2)
        
        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(float(self.number1),1)
            self.answer = float(self.answer)
            if self.answer > float(self.number1):
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(float(self.number1),2)
            self.answer = float(self.answer)
            if self.answer > float(self.number1):
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        
        self.problem = "In a certain relay race, each of the "+str(self.TotalNumbers)+" members in a team "+self.items[0]+" an equal distance. "
        self.problem = self.problem + "What distance did each member "+self.items[1]+" if the total distance covered by the team was "+str(self.number)+" km? Round off your answer to "+self.places[0]+"."

        self.unit = "km"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7c(self.problem,self.answer,self.number1,self.number,self.TotalNumbers,self.places[0],self.places[1],0,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.items,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7c",'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}
        
    def ExplainType7c(self,problem,answer,number1,number,TotalNumber,place1,place2,round,numberLine1,numberLine2,numberLine3,item,unit):

        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.WholeNumber = number1.partition(".")[0]
        self.decimal = number1.partition(".")[2]
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Getting the answer,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>Distance each member "+item[0]+"</td><td style='padding-left:0px; padding-right:0px'>=</td>"
        self.solution_text = self.solution_text + "<td style='text-align:left'>"+str(number)+" &divide; " +str(TotalNumber)+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number1)+"</td></tr></table>"
            
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Rounding off the answer to "+place1+",</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number1)+" is between "+str(numberLine1)+"0 and "+str(numberLine2)+"0.</td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number1)+" is closer to "+str(answer)+"0 than to "+str(numberLine3)+"0.</td></tr>"
        if (int(self.decimal[round])>=5):
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number1)+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number1)+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='5'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:top'>"+str(number1)+"</b></td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>&asymp;</td><td style='text-align:left;vertical-align:top'><b>"+str(answer)+"</b></td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:300px;font-size:.8em;'>When rounding off a decimal to <b>"+place1+"</b>, consider the digit in the <b>"+place2+"</b> only.</div></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7d(self):
        '''e.g.:
        Each member in a <4>-member team in a relay race [bicycled] a distance of <decimal1>. What was the total distance covered by the team, correct to 2 distance places?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        
        self.items = random.choice(['bicycled','cycled','ran','swam','skated','walked'])        
             
        self.number1 = str(randint(3,10))+"."+str(randint(1,9))+str(randint(6,9))+str(randint(6,9))
        
        self.TotalNumbers = randint(2,4)
        
        self.number = float(self.number1) * self.TotalNumbers            

        self.round = randint(1,2)
        
        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(self.number,1)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(self.number,2)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        
        self.problem = "Each member in a "+str(self.TotalNumbers)+"-member team in a relay race "+self.items+" a distance of "+self.number1+" km. What was the total distance covered by the team, correct to "+self.places[0]+"?"

        self.unit = "km"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7d(self.problem,self.answer,self.number1,self.number,self.TotalNumbers,self.places[0],self.places[1],0,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.items,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7d",'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}
        
    def ExplainType7d(self,problem,answer,number1,number,TotalNumber,place1,place2,round,numberLine1,numberLine2,numberLine3,item,unit):

        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.WholeNumber = str(number).partition(".")[0]
        self.decimal = str(number).partition(".")[2]
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Getting the answer,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>Total distance "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td>"
        self.solution_text = self.solution_text + "<td style='text-align:left'>"+str(number1)+" &times; " +str(TotalNumber)+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+"</td></tr></table>"
            
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Rounding off the answer to "+place1+",</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is between "+str(numberLine1)+"0 and "+str(numberLine2)+"0.</td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is closer to "+str(answer)+"0 than to "+str(numberLine3)+"0.</td></tr>"
        if (int(self.decimal[round])>=5):
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='5'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:top'>"+str(number)+"</b></td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>&asymp;</td><td style='text-align:left;vertical-align:top'><b>"+str(answer)+"</b></td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:300px;font-size:.8em;'>When rounding off a decimal to <b>"+place1+"</b>, consider the digit in the <b>"+place2+"</b> only.</div></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8(self):
        '''e.g.:
        [Person.Girlname] bought [a pencil case] for $<decimal1>, [a sharpener] for $<decimal2> and [some art paper] for $<decimal3> at a [bookshop]. Find the total amount she spent at the [bookshop], correct to the nearest dollar.'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        
        self.items = random.choice([['a pencil case','a sharpener','some art paper','bookshop'],['some apples','some berries','some mangoes','fruit shop'],
                                    ['some bananas','some carrots','some bread','grocery store'],['some curry puffs','some muffins','some cupcakes','bakery'],
                                    ['a kite','a spool of kitestring','a kite lantern','kite shop'],['a burger','a drink','a dessert','canteen'],
                                    ['some fresh tomatoes','some oranges','some coffee beans','wet market'],['a hair clip','some rubber bands','some beads','hair accessories store'],
                                    ['some nails','some nuts','a hammer','hardware store'],['some stamps','some envelopes','a bubble wrap','post office'],
                                    ['a pot','some seeds','some plant food','plant nursery']])
        
        self.name = random.choice(PersonName.GirlName)
             
        self.number1 = str(randint(1,3))+"."+random.choice([str(randint(10,99)),str(0)+str(randint(1,9))])
        self.number2 = str(randint(1,3))+"."+random.choice([str(randint(10,99)),str(0)+str(randint(1,9))])
        self.number3 = str(randint(1,3))+"."+random.choice([str(randint(10,99)),str(0)+str(randint(1,9))])
        
        self.numbers = [self.number1,self.number2,self.number3]
        
        for i in range(len(self.numbers)):
            if len(self.numbers[i].partition(".")[2])==1:
                self.numbers[i] = self.numbers[i]+"0"
        
        self.number = float(self.number1) + float(self.number2) + float(self.number3)            

        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.numbers[0] = self.number1
            self.number = float(self.number1) + float(self.number2) + float(self.number3)
        #making sure that there are 2 digits after decimal
        if len(str(self.number).partition(".")[2]) == 1:
            self.number1 = str(float(self.number1) + 0.01)
            self.numbers[0] = self.number1
            self.number = float(self.number1) + float(self.number2) + float(self.number3)        
            
        #Choose which phrase to use in the problem statement: ones place or nearest whole number
        self.onesPlace = ["the ones place","tenths place"]
        self.wholeNumberPlace = ["the nearest whole number","1st decimal place"]
        self.places = random.choice([self.onesPlace,self.wholeNumberPlace])
        
        self.answer = int(round(self.number,0))
        if self.answer > self.number:
            self.numberLine1 = self.answer - 1
            self.numberLine2 = self.answer
            self.numberLine3 = self.numberLine1
        else:
            self.numberLine2 = self.answer + 1
            self.numberLine1 = self.answer
            self.numberLine3 = self.numberLine2
        
        self.problem1 = self.name+" bought "+self.items[0]+" for $"+self.number1+", "+self.items[1]+" for $"+self.number2+" and "
        self.problem1 = self.problem1 + self.items[2]+" for $"+self.number3+" at a "+self.items[3]+". Find the total amount she spent at the "+self.items[3]+", correct to "+self.places[0]+"."
        
        self.problem2 = self.name+" went to a "+self.items[3]+". She spent $"+self.number1+" on "+self.items[0]+", $"+self.number2+" on "+self.items[1]+" and $"+self.number3+" on "+self.items[2]+"."
        self.problem2 = self.problem2 + " How much did she spend at the "+self.items[3]+"? Give your answer rounded off to "+self.places[0]+"."
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.unit = ""
        self.dollar = "$"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number,self.numbers,self.places[0],self.places[1],0,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.name,self.items[3],self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8",'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":self.dollar}
        
    def ExplainType8(self,problem,answer,number,numbers,place1,place2,round,numberLine1,numberLine2,numberLine3,name,item,unit,dollar):

        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit

        self.WholeNumber = str(number).partition(".")[0]
        self.decimal = str(number).partition(".")[2]
        
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Getting the answer,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>Total amount spent by "+name+" at "+item+"</td><td style='padding-left:0px; padding-right:0px'>=</td>"
        self.solution_text = self.solution_text + "<td style='text-align:left'>"+numbers[0]+" + " +numbers[1]+" + " +numbers[2]+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(number)+" "+unit+"</td></tr></table>"
            
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Rounding off the answer to "+place1+",</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is between "+str(numberLine1)+".0 and "+str(numberLine2)+".0.</td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is closer to "+str(answer)+".0 than to "+str(numberLine3)+".0.</td></tr>"
        if (int(self.decimal[round])>=5):
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>"+str(number)+" is "+str(answer)+" when rounded off to "+place1+".</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='5'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left;vertical-align:top'>"+dollar+str(number)+"</b></td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>&asymp;</td><td style='text-align:left;vertical-align:top'><b>"+dollar+str(answer)+"</b></td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:300px;font-size:.8em;'>When rounding off a decimal to <b>"+place1+"</b>, consider the digit in the <b>"+place2+"</b> only.</div></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore):
        
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
            self.value1 = self.answer1
            self.value2 = self.answer2
            self.value3 = self.answer3
            self.value4 = self.answer4
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'answer4':self.answer4,'value1':self.value1,'value2':self.value2
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type,
                'grade':5,"complexity_level":complexity_level,"HCScore":HCScore}       
        

    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        Add the numbers and round off the answer to 1 decimal place.'''
        self.complexity_level = "easy"
        self.HCScore = 3        
             
        self.number1 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number = float(self.number1)+float(self.number2)
        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.number = float(self.number1)+float(self.number2)
        #making sure that there are 2 digits after decimal
        if len(str(self.number).partition(".")[2]) == 1:
            self.number1 = str(float(self.number1) + 0.01)
            self.number = float(self.number1)+float(self.number2)
            
        self.round = randint(1,len(str(self.number).partition(".")[2])-1)
        if self.round==3:
            self.round = 2
        
        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(self.number,1)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(self.number,2)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        
        self.problem1 = "Add the following numbers and round off your answer to %s:<br><br>&nbsp;&nbsp;&nbsp; %s + %s"%(self.places[0],self.number1,self.number2)
        self.problem2 = "Find the sum of %s and %s, correct to %s."%(self.number1,self.number2,self.places[0])
        self.problem3 = "What is the sum of %s and %s? Give your answer correct to %s."%(self.number1,self.number2,self.places[0])
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ1"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+0.1)
        self.wrongAnswers.append(self.answer+0.2)
        self.wrongAnswers.append(self.answer+0.3)
        self.wrongAnswers.append(self.answer-0.1)

        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                             
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.places[0],self.places[1],self.round,self.numberLine1,self.numberLine2,self.numberLine3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        Add the numbers and round off the answer to the nearest whole number.'''
        self.complexity_level = "easy"
        self.HCScore = 3        
             
        self.number1 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number = float(self.number1)+float(self.number2)
        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.number = float(self.number1)+float(self.number2)
            
        #Choose which phrase to use in the problem statement: ones place or nearest whole number
        self.onesPlace = ["the ones place","tenths place"]
        self.wholeNumberPlace = ["the nearest whole number","1st decimal place"]
        self.places = random.choice([self.onesPlace,self.wholeNumberPlace])
        
        self.problem1 = "Add the following numbers and round off your answer to %s:<br><br>&nbsp;&nbsp;&nbsp; %s + %s"%(self.places[0],self.number1,self.number2)
        self.problem2 = "Find the sum of %s and %s, correct to %s."%(self.number1,self.number2,self.places[0])
        self.problem3 = "What is the sum of %s and %s? Give your answer correct to %s."%(self.number1,self.number2,self.places[0])
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.answer = int(round(float(self.number1)+float(self.number2),0))
        if self.answer > self.number:
            self.numberLine1 = self.answer - 1
            self.numberLine2 = self.answer
            self.numberLine3 = self.numberLine1
        else:
            self.numberLine2 = self.answer + 1
            self.numberLine1 = self.answer
            self.numberLine3 = self.numberLine2
        
        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ2"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+1)
        self.wrongAnswers.append(self.answer+2)
        self.wrongAnswers.append(self.answer-2)
        self.wrongAnswers.append(self.answer-1)
          
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.places[0],self.places[1],0,self.numberLine1,self.numberLine2,self.numberLine3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
        Subtract the numbers and round off the answer to 1 decimal place.'''
        self.complexity_level = "easy"
        self.HCScore = 3        
        self.problem_type = "ProblemTypeMCQ3"             
             
        self.number1 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number = abs(float(self.number1)-float(self.number2))
        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.number = abs(float(self.number1)-float(self.number2))
        #making sure that there are 2 digits after decimal
        if len(str(self.number).partition(".")[2]) == 1:
            self.number1 = str(float(self.number1) + 0.01)
            self.number = abs(float(self.number1)-float(self.number2))        
            
        self.round = randint(1,len(str(self.number).partition(".")[2])-1)
        if self.round==3:
            self.round = 2

        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(self.number,1)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(self.number,2)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                

        if float(self.number2) > float(self.number1):
            self.number2, self.number1 = self.number1, self.number2

        self.problem1 = "Subtract the following numbers and round off your answer to %s:<br><br>&nbsp;&nbsp;&nbsp; %s &nbsp;&minus;&nbsp; %s"%(self.places[0],self.number1,self.number2)
        self.problem2 = "Find the difference of %s and %s, correct to %s."%(self.number1,self.number2,self.places[0])
        self.problem3 = "What is the difference of %s and %s? Give your answer correct to %s."%(self.number1,self.number2,self.places[0])
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+0.1)
        self.wrongAnswers.append(self.answer+0.2)
        self.wrongAnswers.append(self.answer-0.1)
        self.wrongAnswers.append(self.answer-0.2)
          
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.places[0],self.places[1],self.round,self.numberLine1,self.numberLine2,self.numberLine3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ4(self):
        '''e.g.:
        Add the numbers and round off the answer to the nearest whole number.'''
        self.complexity_level = "easy"
        self.HCScore = 3        
        self.problem_type = "ProblemTypeMCQ4" 
             
        self.number1 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(1,20))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number = abs(float(self.number1)-float(self.number2))
        if self.number<1:
            self.number1 = str(float(self.number1) + 1)
        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.number = abs(float(self.number1)-float(self.number2))

        #Choose which phrase to use in the problem statement: ones place or nearest whole number
        self.onesPlace = ["the ones place","tenths place"]
        self.wholeNumberPlace = ["the nearest whole number","1st decimal place"]
        self.places = random.choice([self.onesPlace,self.wholeNumberPlace])
        
        if float(self.number2) > float(self.number1):
            self.number2,self.number1 = self.number1,self.number2

        self.problem1 = "Subtract the following numbers and round off your answer to the %s:<br><br>&nbsp;&nbsp;&nbsp; %s &nbsp;&minus;&nbsp; %s"%(self.places[0],self.number1,self.number2)
        self.problem2 = "Find the difference of %s and %s, correct to the %s."%(self.number1,self.number2,self.places[0])
        self.problem3 = "What is the difference of %s and %s? Give your answer correct to the %s."%(self.number1,self.number2,self.places[0])
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.answer = int(round(abs(float(self.number1)-float(self.number2)),0))          
        if self.answer > self.number:
            self.numberLine1 = self.answer - 1
            self.numberLine2 = self.answer
            self.numberLine3 = self.numberLine1
        else:
            self.numberLine2 = self.answer + 1
            self.numberLine1 = self.answer
            self.numberLine3 = self.numberLine2
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+1)
        self.wrongAnswers.append(self.answer+2)
        self.wrongAnswers.append(self.answer-1)
        self.wrongAnswers.append(self.answer+3)
          
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.places[0],self.places[1],0,self.numberLine1,self.numberLine2,self.numberLine3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ5(self):
        '''e.g.:
        Add the numbers and round off the answer to the nearest whole number.'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        self.problem_type = "ProblemTypeMCQ5"
        self.items = random.choice(['packages','bags of plain flour','packets of coarse sugar','bags of seeds','packets of basmati rice',
                      'boxes of chocolate chip cookies','cans of evaporated milk','blocks of wood','books','boxes','bricks','boxes','bags of apples',])
             
        self.number1 = str(randint(1,2))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(1,2))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number3 = str(randint(1,2))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number4 = str(randint(1,2))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        
        self.numbers = [self.number1,self.number2,self.number3,self.number4]
        self.TotalNumbers = randint(2,4)
        
        self.number = 0
        for i in range(self.TotalNumbers):
            self.number = self.number + float(self.numbers[i])
            
        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.numbers[0] = str(float(self.number1) + 0.55)
            self.number = 0
            for i in range(self.TotalNumbers):
                self.number = self.number + float(self.numbers[i])
            
        #Choose which phrase to use in the problem statement: ones place or nearest whole number
        self.onesPlace = ["the ones place","tenths place"]
        self.wholeNumberPlace = ["the nearest whole number","1st decimal place"]
        self.places = random.choice([self.onesPlace,self.wholeNumberPlace])
        
        self.problem1 = "The masses of "+str(self.TotalNumbers)+" "+self.items+" are "+str(self.numbers[0])+" kg"
        if self.TotalNumbers == 2:
            self.problem1 = self.problem1 + " and "+str(self.numbers[1])+" kg."
        elif self.TotalNumbers ==3:
            self.problem1 = self.problem1 + ", "+str(self.numbers[1])+" kg and "+str(self.numbers[2])+" kg."
        else:
            self.problem1 = self.problem1 + ", "+str(self.numbers[1])+" kg, "+str(self.numbers[2])+" kg and "+str(self.numbers[3])+" kg."
        
        self.problem1 = self.problem1 +  " Find the total mass of the "+str(self.TotalNumbers)+" "+self.items+". Give your answer correct to the nearest kilogram." 

        self.problem2 = "What is the total mass of "+str(self.TotalNumbers)+" "+self.items+" that have individual masses of "+str(self.numbers[0])+" kg"
        
        if self.TotalNumbers == 2:
            self.problem2 = self.problem2 + " and "+str(self.numbers[1])+" kg."
        elif self.TotalNumbers ==3:
            self.problem2 = self.problem2 + ", "+str(self.numbers[1])+" kg and "+str(self.numbers[2])+" kg."
        else:
            self.problem2 = self.problem2 + ", "+str(self.numbers[1])+" kg, "+str(self.numbers[2])+" kg and "+str(self.numbers[3])+" kg."

        self.problem2 = self.problem2 + " Round off your answer to the nearest kilogram."

        self.problem = random.choice([self.problem1,self.problem2])

        self.answer = int(round(self.number,0))
        if self.answer > self.number:
            self.numberLine1 = self.answer - 1
            self.numberLine2 = self.answer
            self.numberLine3 = self.numberLine1
        else:
            self.numberLine2 = self.answer + 1
            self.numberLine1 = self.answer
            self.numberLine3 = self.numberLine2
                      
        self.unit = "kg"
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+1)
        self.wrongAnswers.append(self.answer+float(0.5))
        self.wrongAnswers.append(self.answer-1)
        self.wrongAnswers.append(self.number)
          
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number,self.numbers,self.places[0],self.places[1],0,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.TotalNumbers,self.items,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ6(self):
        '''e.g.:
        A [can] had <decimal1> litre(s) of [juice]. [Person.name] poured out <decimal2> litre(s) of [juice] from it.How much [juice] is left in the [can]. Round off your 
        answer to the hundredths place. (Or the tenths place)'''
        
        self.complexity_level = "medium"
        self.HCScore = 5        
        self.problem_type = "ProblemTypeMCQ6"
        
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice([['tomato ketchup','bottle'],['sparkling water','bottle'],['mango juice','cup'],['strawberry milk','mug'],['chocolate milk','carton'],
                                    ['oil paint','can'],['soda','cup'],['cooking oil','can'],['liquid','container'],['green tea','cup']])
             
        self.number1 = str(1)+"."+random.choice([str(randint(100,200)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(0)+"."+random.choice([str(randint(100,800)),str(randint(1,99)),str(0)+str(randint(1,99))])
        
        self.number = float(self.number1)-float(self.number2)
        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.number = float(self.number1)-float(self.number2)
        #making sure that there are 2 digits after decimal
        if len(str(self.number).partition(".")[2]) == 1:
            self.number1 = str(float(self.number1) + 0.01)
            self.number = float(self.number1)-float(self.number2)        
            
        self.round = randint(1,len(str(self.number).partition(".")[2])-1)
        if self.round==3:
            self.round = 2

        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(self.number,1)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(self.number,2)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        
        self.problem1 = "A "+self.items[1]+" had "+self.number1+" litres of "+self.items[0]+". "
        self.problem1 = self.problem1 + self.name+ " poured out "+self.number2+" litre of "+self.items[0]+" from it. "
        self.problem1 = self.problem1 + "How much "+self.items[0]+" is left in the "+self.items[1]+". Round off your answer to "+self.places[0]+"." 

        self.problem2 = self.name+" pours out "+self.number2+" litre of "+self.items[0]+" from a "+self.items[1]+" that had "+self.number1+" litres of "+self.items[0]+" at first. "
        self.problem2 = self.problem2 + "Find the volume of "+self.items[0]+" left in the "+self.items[1]+" rounded off to "+self.places[0]+"."

        self.problem = random.choice([self.problem1,self.problem2])

                      
        if self.answer>1:
            self.unit = "litres"
        else:
            self.unit = "litre"
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+0.05)
        self.wrongAnswers.append(self.answer+0.5)
        self.wrongAnswers.append(self.answer-0.05)
        self.wrongAnswers.append(self.number)
          
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.places[0],self.places[1],self.round,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.unit,self.items[0],self.items[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ7a(self):
        '''e.g.:
        [Person.Boyname1] [bicycled] <decimal1> km while [Person.Boyname2] [bicycled] <decimal2> km. What is the total distance the two boys [bicycled] rounded off to 1 decimal place?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        self.problem_type = "ProblemTypeMCQ7a"
        
        self.items = random.choice(['bicycled','cycled','ran','skated','jogged','walked'])
        
        self.names = random.sample(PersonName.BoyName,2)
             
        self.number1 = str(randint(3,10))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(3,10))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        
        self.numbers = [self.number1,self.number2]
        
        self.number = float(self.number1) + float(self.number2)            

        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.numbers[0] = self.number1
            self.number = float(self.number1)+float(self.number2)
        #making sure that there are 2 digits after decimal
        if len(str(self.number).partition(".")[2]) == 1:
            self.number1 = str(float(self.number1) + 0.01)
            self.numbers[0] = self.number1
            self.number = float(self.number1)+float(self.number2)        
            
        self.round = randint(1,len(str(self.number).partition(".")[2])-1)
        if self.round==3:
            self.round = 2

        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(self.number,1)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(self.number,2)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        
        self.problem = self.names[0]+" "+self.items+" "+self.number1+" km while "+self.names[1]+" "+self.items+" "+self.number2+" km. What is the total distance the two boys "+self.items+" rounded off to "+self.places[0]+"?"

        self.unit = "km"
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+0.05)
        self.wrongAnswers.append(self.answer+0.5)
        self.wrongAnswers.append(self.answer-0.05)
        self.wrongAnswers.append(self.number)
          
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7a(self.problem,self.answer,self.number,self.numbers,self.places[0],self.places[1],0,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.items,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ7b(self):
        '''e.g.:
        [Person.Boyname1] [bicycled] <decimal1> km while [Person.Boyname2] [bicycled] <decimal2> km. What is the total distance the two boys [bicycled] rounded off to 1 decimal place?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        self.problem_type = "ProblemTypeMCQ7b"
        
        self.items = random.choice(['bicycled','cycled','ran','skated','jogged','walked'])
        
        self.names = random.sample(PersonName.BoyName,2)
             
        self.number1 = str(randint(3,10))+"."+random.choice([str(randint(100,999)),str(randint(1,99)),str(0)+str(randint(1,99))])
        self.number2 = str(randint(3,10))+"."+str(randint(100,999))
        
        self.numbers = [self.number1,self.number2]
        
        self.number = float(self.number1) + float(self.number2)            

        self.round = randint(1,2)
        
        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(float(self.number2),1)
            self.answer = float(self.answer)
            if self.answer > float(self.number2):
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(float(self.number2),2)
            self.answer = float(self.answer)
            if self.answer > float(self.number2):
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        
        self.problem = self.names[0]+" and "+self.names[1]+" "+self.items+" a total distance of "+str(self.number)+" km. If "+self.names[0]+" "+self.items+" "+self.number1+" km, find the distance that "+self.names[1]+" "+self.items+", correct to "+self.places[0]+"."

        self.unit = "km"

        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+0.05)
        self.wrongAnswers.append(self.answer+0.5)
        self.wrongAnswers.append(self.answer-0.05)
        self.wrongAnswers.append(self.number2)
          
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7b(self.problem,self.answer,self.number,self.numbers,self.places[0],self.places[1],0,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.items,self.unit,self.names)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ7c(self):
        '''e.g.:
        In a certain relay race, each of the <four> members in a team [bicycled] an equal distance. What distance did each member [bicycle] if the total distance covered by the team was <decimal1>? Round off your answer to 2 decimal places.'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        self.problem_type = "ProblemTypeMCQ7c"
        
        self.items = random.choice([['bicycled','bicycle'],['cycled','cycle'],['ran','run'],['skated','skate'],['walked','walk']])        
             
        self.number1 = str(randint(3,10))+"."+str(randint(1,9))+str(randint(1,9))+str(randint(1,9))
        
        self.TotalNumbers = randint(2,4)
        
        self.number = float(self.number1) * self.TotalNumbers            

        self.round = randint(1,2)
        
        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(float(self.number1),1)
            self.answer = float(self.answer)
            if self.answer > float(self.number1):
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(float(self.number1),2)
            self.answer = float(self.answer)
            if self.answer > float(self.number1):
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        
        self.problem = "In a certain relay race, each of the "+str(self.TotalNumbers)+" members in a team "+self.items[0]+" an equal distance. "
        self.problem = self.problem + "What distance did each member "+self.items[1]+" if the total distance covered by the team was "+str(self.number)+" km? Round off your answer to "+self.places[0]+"."

        self.unit = "km"

        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+0.05)
        self.wrongAnswers.append(self.answer+0.5)
        self.wrongAnswers.append(self.answer-0.05)
        self.wrongAnswers.append(self.number1)
          
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7c(self.problem,self.answer,self.number1,self.number,self.TotalNumbers,self.places[0],self.places[1],0,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.items,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ7d(self):
        '''e.g.:
        Each member in a <4>-member team in a relay race [bicycled] a distance of <decimal1>. What was the total distance covered by the team, correct to 2 distance places?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        self.problem_type = "ProblemTypeMCQ7d"
        
        self.items = random.choice(['bicycled','cycled','ran','swam','skated','walked'])        
             
        self.number1 = str(randint(3,10))+"."+str(randint(1,9))+str(randint(6,9))+str(randint(6,9))
        
        self.TotalNumbers = randint(2,4)
        
        self.number = float(self.number1) * self.TotalNumbers            

        self.round = randint(1,2)
        
        #Choose which phrase to use in the problem statement: the tenths place or 1 decimal place; or the hundredths place or 2 decimal places
        if self.round==1:
            self.tenthsPlace = ["the tenths place","the hundredths place"]
            self.decimalPlace = ["1 decimal place","2nd decimal place"]
            self.places = random.choice([self.tenthsPlace,self.decimalPlace])
            self.answer = '%.1f' %round(self.number,1)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.1
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.1
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        else:
            self.hundredthsPlace = ["the hundredths place","the thousandths place"]
            self.decimalPlace = ["2 decimal places","3rd decimal place"]
            self.places = random.choice([self.hundredthsPlace,self.decimalPlace])
            self.answer = '%.2f' %round(self.number,2)
            self.answer = float(self.answer)
            if self.answer > self.number:
                self.numberLine1 = self.answer - 0.01
                self.numberLine2 = self.answer
                self.numberLine3 = self.numberLine1
            else:
                self.numberLine2 = self.answer + 0.01
                self.numberLine1 = self.answer
                self.numberLine3 = self.numberLine2                
        
        self.problem = "Each member in a "+str(self.TotalNumbers)+"-member team in a relay race "+self.items+" a distance of "+self.number1+" km. What was the total distance covered by the team, correct to "+self.places[0]+"?"

        self.unit = "km"
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+0.05)
        self.wrongAnswers.append(self.answer+0.5)
        self.wrongAnswers.append(self.answer-0.05)
        self.wrongAnswers.append(self.number)
          
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7d(self.problem,self.answer,self.number1,self.number,self.TotalNumbers,self.places[0],self.places[1],0,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.items,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)

    def GenerateProblemTypeMCQ8(self):
        '''e.g.:
        [Person.Girlname] bought [a pencil case] for $<decimal1>, [a sharpener] for $<decimal2> and [some art paper] for $<decimal3> at a [bookshop]. Find the total amount she spent at the [bookshop], correct to the nearest dollar.'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        self.problem_type = "ProblemTypeMCQ7d"
        
        self.items = random.choice([['a pencil case','a sharpener','some art paper','bookshop'],['some apples','some berries','some mangoes','fruit shop'],
                                    ['some bananas','some carrots','some bread','grocery store'],['some curry puffs','some muffins','some cupcakes','bakery'],
                                    ['a kite','a spool of kitestring','a kite lantern','kite shop'],['a burger','a drink','a dessert','canteen'],
                                    ['some fresh tomatoes','some oranges','some coffee beans','wet market'],['a hair clip','some rubber bands','some beads','hair accessories store'],
                                    ['some nails','some nuts','a hammer','hardware store'],['some stamps','some envelopes','a bubble wrap','post office'],
                                    ['a pot','some seeds','some plant food','plant nursery']])
        
        self.name = random.choice(PersonName.GirlName)
             
        self.number1 = str(randint(1,3))+"."+random.choice([str(randint(10,99)),str(0)+str(randint(1,9))])
        self.number2 = str(randint(1,3))+"."+random.choice([str(randint(10,99)),str(0)+str(randint(1,9))])
        self.number3 = str(randint(1,3))+"."+random.choice([str(randint(10,99)),str(0)+str(randint(1,9))])
        
        self.numbers = [self.number1,self.number2,self.number3]
        
        for i in range(len(self.numbers)):
            if len(self.numbers[i].partition(".")[2])==1:
                self.numbers[i] = self.numbers[i]+"0"
        
        self.number = float(self.number1) + float(self.number2) + float(self.number3)            

        #making sure the decimal is not .0
        if str(self.number).partition(".")[2]==str(0):
            self.number1 = str(float(self.number1) + 0.55)
            self.numbers[0] = self.number1
            self.number = float(self.number1) + float(self.number2) + float(self.number3)
        #making sure that there are 2 digits after decimal
        if len(str(self.number).partition(".")[2]) == 1:
            self.number1 = str(float(self.number1) + 0.01)
            self.numbers[0] = self.number1
            self.number = float(self.number1) + float(self.number2) + float(self.number3)        
            
        #Choose which phrase to use in the problem statement: ones place or nearest whole number
        self.onesPlace = ["the ones place","tenths place"]
        self.wholeNumberPlace = ["the nearest whole number","1st decimal place"]
        self.places = random.choice([self.onesPlace,self.wholeNumberPlace])
        
        self.answer = int(round(self.number,0))
        if self.answer > self.number:
            self.numberLine1 = self.answer - 1
            self.numberLine2 = self.answer
            self.numberLine3 = self.numberLine1
        else:
            self.numberLine2 = self.answer + 1
            self.numberLine1 = self.answer
            self.numberLine3 = self.numberLine2
        
        self.problem1 = self.name+" bought "+self.items[0]+" for $"+self.number1+", "+self.items[1]+" for $"+self.number2+" and "
        self.problem1 = self.problem1 + self.items[2]+" for $"+self.number3+" at a "+self.items[3]+". Find the total amount she spent at the "+self.items[3]+", correct to "+self.places[0]+"."
        
        self.problem2 = self.name+" went to a "+self.items[3]+". She spent $"+self.number1+" on "+self.items[0]+", $"+self.number2+" on "+self.items[1]+" and $"+self.number3+" on "+self.items[2]+"."
        self.problem2 = self.problem2 + " How much did she spend at the "+self.items[3]+"? Give your answer rounded off to "+self.places[0]+"."
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.unit = ""
        self.dollar = "$"
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+1)
        self.wrongAnswers.append(self.answer-1)
        self.wrongAnswers.append(self.number)
          
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number,self.numbers,self.places[0],self.places[1],0,
                                              self.numberLine1,self.numberLine2,self.numberLine3,self.name,self.items[3],self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)

    def checkAnswer(self,template,answer,InputAnswer):
        try:
            return (float(answer)==float(InputAnswer))
        except ValueError:
            return False  