'''
Created on Mar 12, 2012
Module: DecimalsAddSub
Generates the "Decimals Addition and Subtraction" problems for Primary 4

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

class DecimalsAddSub:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType5","ProblemTypeMCQ5",],
                            6:["ProblemType6","ProblemTypeMCQ6",],
                            7:["ProblemType7","ProblemTypeMCQ7",],
                            8:["ProblemType8","ProblemTypeMCQ8",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemType5(),self.GenerateProblemTypeMCQ5(),],
                                    6:[self.GenerateProblemType6(),self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemType7(),self.GenerateProblemTypeMCQ7(),],
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
        #return self.GenerateProblemTypeMCQ4()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),
                            "ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            }
        return self.ProblemType[problem_type]
        
        
    def GenerateProblemType1(self):
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.FloatNumber1 = float(self.number1) / 10
        self.FloatNumber2 = float(self.number2) / 10
        
        self.problem = str(self.FloatNumber1)+" + "+str(self.FloatNumber2)+" = "
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1+self.number2) / 10

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType1(self,problem,answer,FloatNumber1,FloatNumber2,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the place value table with the given numbers as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1><tr>"
        self.solution_text = self.solution_text + "<td>Ones</td><td>Tenths</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(FloatNumber1)[0]+"</td><td>"+str(FloatNumber1)[2]+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(FloatNumber2)[0]+"</td><td>"+str(FloatNumber2)[2]+"</td></tr></table><br>"
        self.solution_text = self.solution_text + "Now, first add the digits at Tenths<br><br>"
        if int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]) >=10:
            if int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]) > 11:
                self.solution_text = self.solution_text + str(FloatNumber1)[2]+" + "+str(FloatNumber2)[2]+" = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" = 1 one "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenths<br><br>"
            else:
                self.solution_text = self.solution_text + str(FloatNumber1)[2]+" + "+str(FloatNumber2)[2]+" = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" = 1 one "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenth<br><br>"
            self.solution_text = self.solution_text + "Digit 1 will be carried forward to Ones<br><br>"
            self.solution_text = self.solution_text + "Now add the ones:<br><br>"
            self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" + 1 = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" ones"+"<br><br>"
            self.solution_text = self.solution_text + "Hence the answer is "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenths = "+str(answer)
        else:
            self.solution_text = self.solution_text + str(int(str(FloatNumber1)[2]))+" + "+str(int(str(FloatNumber2)[2]))+" = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" tenths<br><br>"
            self.solution_text = self.solution_text + "Now add the ones:<br><br>"
            self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" ones"+"<br><br>"
            self.solution_text = self.solution_text + "Hence the answer is "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" tenths = "+str(answer)
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(11,99)
        self.number2 = randint(11,99)
        self.FloatNumber1 = float(self.number1) / 10
        self.FloatNumber2 = float(self.number2) / 10
        
        self.problem = str(self.FloatNumber1)+" + "+str(self.FloatNumber2)+" = "
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1+self.number2) / 10

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType2(self,problem,answer,FloatNumber1,FloatNumber2,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the place value table with the given numbers as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1><tr>"
        self.solution_text = self.solution_text + "<td>Ones</td><td>Tenths</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(FloatNumber1)[0]+"</td><td>"+str(FloatNumber1)[2]+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(FloatNumber2)[0]+"</td><td>"+str(FloatNumber2)[2]+"</td></tr></table><br>"
        self.solution_text = self.solution_text + "Now, first add the digits at Tenths<br><br>"
        if int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]) >=10:
            if int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]) > 11:
                self.solution_text = self.solution_text + str(FloatNumber1)[2]+" + "+str(FloatNumber2)[2]+" = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" = 1 one "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenths<br><br>"
            else:
                self.solution_text = self.solution_text + str(FloatNumber1)[2]+" + "+str(FloatNumber2)[2]+" = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" = 1 one "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenth<br><br>"
            self.solution_text = self.solution_text + "Digit 1 will be carried forward to Ones<br><br>"
            self.CarryForward = 1
        else:
            self.solution_text = self.solution_text + str(int(str(FloatNumber1)[2]))+" + "+str(int(str(FloatNumber2)[2]))+" = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" tenths<br><br>"
            self.CarryForward = 0
            
        self.solution_text = self.solution_text + "Now add the ones:<br><br>"
        if self.CarryForward == 1:
            if int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1>9: 
                self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" + 1 = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" = 1 ten "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)[1]+" ones"+"<br><br>"
                self.solution_text = self.solution_text + "Hence the answer is: 1 ten "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)[1]+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenths = <i><b>"+str(answer)+"</b></i>"
            else:
                self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" + 1 = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" ones"+"<br><br>"
                self.solution_text = self.solution_text + "Hence the answer is: "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenths = <i><b>"+str(answer)+"</b></i>"
        else:
            if int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])>9:
                self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" = 1 ten "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))[1]+" ones"+"<br><br>"
                self.solution_text = self.solution_text + "Hence the answer is: 1 ten "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))[1]+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" tenths = <i><b>"+str(answer)+"</b></i>"
            else:
                self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" ones"+"<br><br>"
                self.solution_text = self.solution_text + "Hence the answer is: "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" tenths = <i><b>"+str(answer)+"</b></i>"        
        self.solution_text = self.solution_text + "<br><br><i>(Remember the decimal point is added after ones digit)</i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g.:
        0.11 + 0.77 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(11,99)
        self.number2 = randint(11,99)
        while self.number1%10==0:
            self.number1 = randint(11,99)
        while self.number2%10==0:
            self.number2 = randint(11,99)

        self.FloatNumber1 = float(self.number1) / 100
        self.FloatNumber2 = float(self.number2) / 100
        
        self.problem = str(self.FloatNumber1)+" + "+str(self.FloatNumber2)+" = "
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1+self.number2) / 100

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType3(self,problem,answer,FloatNumber1,FloatNumber2,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the place value table with the given numbers as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1><tr>"
        self.solution_text = self.solution_text + "<td>Ones</td><td>Tenths</td><td>Hundredths</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(FloatNumber1)[0]+"</td><td>"+str(FloatNumber1)[2]+"</td><td>"+str(FloatNumber1)[3]+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(FloatNumber2)[0]+"</td><td>"+str(FloatNumber2)[2]+"</td><td>"+str(FloatNumber2)[3]+"</td></tr></table><br>"
        self.solution_text = self.solution_text + "Now, first add the digits at Hundredths<br><br>"
        if int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]) >=10:
            if int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]) > 11:
                self.solution_text = self.solution_text + str(FloatNumber1)[3]+" + "+str(FloatNumber2)[3]+" = "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))+" = 1 tenths <b>"+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))[1]+" hundredths</b><br><br>"
            else:
                self.solution_text = self.solution_text + str(FloatNumber1)[3]+" + "+str(FloatNumber2)[3]+" = "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))+" = 1 tenths <b>"+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))[1]+" hundredth</b><br><br>"
            self.solution_text = self.solution_text + "Digit 1 will be carried forward to Tenths<br><br>"
            self.CarryForward = 1
        else:
            self.solution_text = self.solution_text + str(int(str(FloatNumber1)[3]))+" + "+str(int(str(FloatNumber2)[3]))+" = <b>"+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))+" hundredths<br><br></b>"
            self.CarryForward = 0
        self.solution_text = self.solution_text + "Now add the digit at tenths<br><br>"
        if self.CarryForward == 0:
            if int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]) >=10:
                if int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]) > 11:
                    self.solution_text = self.solution_text + str(FloatNumber1)[2]+" + "+str(FloatNumber2)[2]+" = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" = 1 one <b>"+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenths</b><br><br>"
                else:
                    self.solution_text = self.solution_text + str(FloatNumber1)[2]+" + "+str(FloatNumber2)[2]+" = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" = 1 one <b>"+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenth</b><br><br>"
                self.solution_text = self.solution_text + "Digit 1 will be carried forward to Ones<br><br>"
                self.solution_text = self.solution_text + "Now add the ones:<br><br>"
                self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" + 1 = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" = <b>"+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" ones</b><br><br>"
                self.solution_text = self.solution_text + "Hence the answer is "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenths "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))+" hundredths = <i><b>"+str(answer)+"</b></i>"
            else:
                self.solution_text = self.solution_text + str(int(str(FloatNumber1)[2]))+" + "+str(int(str(FloatNumber2)[2]))+" = <b>"+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" tenths</b><br><br>"
                self.solution_text = self.solution_text + "Now add the ones:<br><br>"
                self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" = <b>"+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" ones</b><br><br>"
                self.solution_text = self.solution_text + "Hence the answer is "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" tenths "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))+" hundredths = <i><b>"+str(answer)+"</b></i>"
        else:
            if int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1 >=10:
                if int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1 > 11:
                    self.solution_text = self.solution_text + str(FloatNumber1)[2]+" + "+str(FloatNumber2)[2]+" + 1 = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)+" = 1 one <b>"+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)[1]+" tenths</b><br><br>"
                else:
                    self.solution_text = self.solution_text + str(FloatNumber1)[2]+" + "+str(FloatNumber2)[2]+" + 1 = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)+" = 1 one <b>"+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)[1]+" tenth</b><br><br>"
                self.solution_text = self.solution_text + "Digit 1 will be carried forward to Ones<br><br>"
                self.solution_text = self.solution_text + "Now add the ones:<br><br>"
                self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" + 1 = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" = <b>"+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" ones</b><br><br>"
                self.solution_text = self.solution_text + "Hence the answer is "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)[1]+" tenths "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))[1]+" hundredths = <i><b>"+str(answer)+"</b></i>"
            else:
                self.solution_text = self.solution_text + str(int(str(FloatNumber1)[2]))+" + "+str(int(str(FloatNumber2)[2]))+" + 1 = <b>"+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)+" tenths</b><br><br>"
                self.solution_text = self.solution_text + "Now add the ones:<br><br>"
                self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" = <b>"+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" ones</b><br><br>"
                self.solution_text = self.solution_text + "Hence the answer is "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)+" tenths "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))[1]+" hundredths = <i><b>"+str(answer)+"</b></i>"
        self.solution_text = self.solution_text + "<br><br><i>(Remember the decimal point is added after ones digit)</i>"    
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g.:
        0.11 + 0.77 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(101,999)
        self.number2 = randint(101,999)
        while self.number1%10==0 or self.number1%100==0:
            self.number1 = randint(101,999)
        while self.number2%10==0 or self.number2%100==0:
            self.number2 = randint(101,999)
        self.FloatNumber1 = float(self.number1) / 100
        self.FloatNumber2 = float(self.number2) / 100
        
        self.problem = str(self.FloatNumber1)+" + "+str(self.FloatNumber2)+" = "
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1+self.number2) / 100

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType4(self,problem,answer,FloatNumber1,FloatNumber2,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the place value table with the given numbers as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1><tr>"
        self.solution_text = self.solution_text + "<td>Ones</td><td>Tenths</td><td>Hundredths</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(FloatNumber1)[0]+"</td><td>"+str(FloatNumber1)[2]+"</td><td>"+str(FloatNumber1)[3]+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(FloatNumber2)[0]+"</td><td>"+str(FloatNumber2)[2]+"</td><td>"+str(FloatNumber2)[3]+"</td></tr></table><br>"
        self.solution_text = self.solution_text + "Now, first add the digits at Hundredths<br><br>"
        if int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]) >=10:
            if int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]) > 11:
                self.solution_text = self.solution_text + str(FloatNumber1)[3]+" + "+str(FloatNumber2)[3]+" = "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))+" = 1 tenths <b>"+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))[1]+" hundredths</b><br><br>"
            else:
                self.solution_text = self.solution_text + str(FloatNumber1)[3]+" + "+str(FloatNumber2)[3]+" = "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))+" = 1 tenths <b>"+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))[1]+" hundredth</b><br><br>"
            self.solution_text = self.solution_text + "Digit 1 will be carried forward to Tenths<br><br>"
            self.CarryForwardT = 1
        else:
            self.solution_text = self.solution_text + str(int(str(FloatNumber1)[3]))+" + "+str(int(str(FloatNumber2)[3]))+" = <b>"+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))+" hundredths<br><br></b>"
            self.CarryForwardT = 0
        self.solution_text = self.solution_text + "Next add the digits at Tenths<br><br>"
        if self.CarryForwardT==1:
            if int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1 >=10:
                if int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1 > 11:
                    self.solution_text = self.solution_text + str(FloatNumber1)[2]+" + "+str(FloatNumber2)[2]+" + 1 = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)+" = 1 one <b>"+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)[1]+" tenths</b><br><br>"
                else:
                    self.solution_text = self.solution_text + str(FloatNumber1)[2]+" + "+str(FloatNumber2)[2]+" + 1 = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)+" = 1 one <b>"+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)[1]+" tenth</b><br><br>"
                self.solution_text = self.solution_text + "Digit 1 will be carried forward to Ones<br><br>"
                self.CarryForwardO = 1
            else:
                self.solution_text = self.solution_text + str(int(str(FloatNumber1)[2]))+" + "+str(int(str(FloatNumber2)[2]))+" + 1 = <b>"+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)+" tenths</b><br><br>"
                self.CarryForwardO = 0
        else:
            if int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]) >=10:
                if int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]) > 11:
                    self.solution_text = self.solution_text + str(FloatNumber1)[2]+" + "+str(FloatNumber2)[2]+" = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" = 1 one <b>"+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenths</b><br><br>"
                else:
                    self.solution_text = self.solution_text + str(FloatNumber1)[2]+" + "+str(FloatNumber2)[2]+" = "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" = 1 one <b>"+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenth</b><br><br>"
                self.solution_text = self.solution_text + "Digit 1 will be carried forward to Ones<br><br>"
                self.CarryForwardO = 1
            else:
                self.solution_text = self.solution_text + str(int(str(FloatNumber1)[2]))+" + "+str(int(str(FloatNumber2)[2]))+" = <b>"+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" tenths</b><br><br>"
                self.CarryForwardO = 0
            
            
        self.solution_text = self.solution_text + "Now add the ones:<br><br>"
        if self.CarryForwardO == 1:
            if int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1>9: 
                self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" + 1 = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" = 1 ten <b>"+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)[1]+" ones</b><br><br>"
                if self.CarryForwardT == 1:
                    self.solution_text = self.solution_text + "Hence the answer is: 1 ten "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)[1]+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)[1]+" tenths "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))[1]+" hundredths = <i><b>"+str(answer)+"</b></i>"
                else:
                    self.solution_text = self.solution_text + "Hence the answer is: 1 ten "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)[1]+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenths "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))+" hundredths = <i><b>"+str(answer)+"</b></i>"
            else:
                self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" + 1 = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" = <b>"+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" ones</b><br><br>"
                if self.CarryForwardT == 1:
                    self.solution_text = self.solution_text + "Hence the answer is: "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)[1]+" tenths "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))[1]+" hundredths = <i><b>"+str(answer)+"</b></i>"
                else:
                    self.solution_text = self.solution_text + "Hence the answer is: "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])+1)+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))[1]+" tenths "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))+" hundredths = <i><b>"+str(answer)+"</b></i>"
        else:
            if int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0])>9:
                self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" = 1 ten <b>"+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))[1]+" ones</b><br><br>"
                if self.CarryForwardT == 1:
                    self.solution_text = self.solution_text + "Hence the answer is: 1 ten "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))[1]+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)+" tenths "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))[1]+" hundredths = <i><b>"+str(answer)+"</b></i>"
                else:
                    self.solution_text = self.solution_text + "Hence the answer is: 1 ten "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))[1]+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" tenths "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))+" hundredths = <i><b>"+str(answer)+"</b></i>"
            else:
                self.solution_text = self.solution_text + str(FloatNumber1)[0]+" + "+str(FloatNumber2)[0]+" = "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" = <b>"+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" ones</b><br><br>"
                if self.CarryForwardT == 1:
                    self.solution_text = self.solution_text + "Hence the answer is: "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2])+1)+" tenths "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))[1]+" hundredths = <i><b>"+str(answer)+"</b></i>"
                else:
                    self.solution_text = self.solution_text + "Hence the answer is: "+str(int(str(FloatNumber1)[0])+int(str(FloatNumber2)[0]))+" ones "+str(int(str(FloatNumber1)[2])+int(str(FloatNumber2)[2]))+" tenths "+str(int(str(FloatNumber1)[3])+int(str(FloatNumber2)[3]))+" hundredths = <i><b>"+str(answer)+"</b></i>"
        self.solution_text = self.solution_text + "<br><br><i>(Remember the decimal point is added after ones digit)</i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType5(self):
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        
        self.answer = float(self.number1) / 10
        self.FloatNumber2 = float(self.number2) / 10
        self.FloatNumber1 = float(self.number1+self.number2) / 10 

        self.problem = str(self.FloatNumber1)+" - "+str(self.FloatNumber2)+" = "
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType5(self,problem,answer,FloatNumber1,FloatNumber2,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"

        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType6(self):
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(11,99)
        self.number2 = randint(11,99)
        
        self.answer = float(self.number1) / 10
        self.FloatNumber2 = float(self.number2) / 10
        self.FloatNumber1 = float(self.number1+self.number2) / 10 
        
        self.problem = str(self.FloatNumber1)+" - "+str(self.FloatNumber2)+" = "
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType6(self,problem,answer,FloatNumber1,FloatNumber2,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType7(self):
        '''e.g.:
        0.11 + 0.77 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(11,99)
        self.number2 = randint(11,99)

        self.answer = float(self.number1) / 100
        self.FloatNumber2 = float(self.number2) / 100
        self.FloatNumber1 = float(self.number1+self.number2) / 100
        
        self.problem = str(self.FloatNumber1)+" - "+str(self.FloatNumber2)+" = "
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType7(self,problem,answer,FloatNumber1,FloatNumber2,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"

        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType8(self):
        '''e.g.:
        0.11 + 0.77 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(101,999)
        self.number2 = randint(101,999)

        self.answer = float(self.number1) / 100
        self.FloatNumber2 = float(self.number2) / 100
        self.FloatNumber1 = float(self.number1+self.number2) / 100 
        
        self.problem = str(self.FloatNumber1)+" - "+str(self.FloatNumber2)+" = "
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType8(self,problem,answer,FloatNumber1,FloatNumber2,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"

        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore,grade,CheckAnswerType):
        
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
                'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}      

    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        What does the digit 7 stand for in 71453? '''
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.problem_type = "ProblemTypeMCQ1"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.FloatNumber1 = float(self.number1) / 10
        self.FloatNumber2 = float(self.number2) / 10
        
        self.problem = str(self.FloatNumber1)+" + "+str(self.FloatNumber2)+" = "

        self.answer = float(self.number1+self.number2) / 10

        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        self.wrongAnswers.append(self.answer + 0.1)
        self.wrongAnswers.append(self.answer + 0.2)        
        if self.answer > 0.2:
            self.wrongAnswers.append(self.answer - 0.1)
            self.wrongAnswers.append(self.answer - 0.2)
        elif self.answer > 0.1 and self.answer < 0.2:
            self.wrongAnswers.append(self.answer - 0.1)
            self.wrongAnswers.append(self.answer + 0.3)
        else:
            self.wrongAnswers.append(self.answer + 0.3)
            self.wrongAnswers.append(self.answer + 0.4)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        What does the digit 7 stand for in 71453? '''
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.problem_type = "ProblemTypeMCQ2"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        
        self.number1 = randint(11,99)
        self.number2 = randint(11,99)
        self.FloatNumber1 = float(self.number1) / 10
        self.FloatNumber2 = float(self.number2) / 10
        
        self.problem = str(self.FloatNumber1)+" + "+str(self.FloatNumber2)+" = "
       
        self.answer = float(self.number1+self.number2) / 10

        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        self.wrongAnswers.append(self.answer + 0.1)
        self.wrongAnswers.append(self.answer + 0.2)        
        if self.answer > 0.2:
            self.wrongAnswers.append(self.answer - 0.1)
            self.wrongAnswers.append(self.answer - 0.2)
        elif self.answer > 0.1 and self.answer < 0.2:
            self.wrongAnswers.append(self.answer - 0.1)
            self.wrongAnswers.append(self.answer + 0.3)
        else:
            self.wrongAnswers.append(self.answer + 0.3)
            self.wrongAnswers.append(self.answer + 0.4)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
        What does the digit 7 stand for in 71453? '''
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.problem_type = "ProblemTypeMCQ3"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.number1 = randint(11,99)
        self.number2 = randint(11,99)
        while self.number1%10==0:
            self.number1 = randint(11,99)
        while self.number2%10==0:
            self.number2 = randint(11,99)
        self.FloatNumber1 = float(self.number1) / 100
        self.FloatNumber2 = float(self.number2) / 100
        
        self.problem = str(self.FloatNumber1)+" + "+str(self.FloatNumber2)+" = "

        self.answer = float(self.number1+self.number2) / 100

        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        self.wrongAnswers.append(self.answer + 0.01)
        self.wrongAnswers.append(self.answer + 0.02)        
        if self.answer > 0.02:
            self.wrongAnswers.append(self.answer - 0.01)
            self.wrongAnswers.append(self.answer - 0.02)
        elif self.answer > 0.01 and self.answer < 0.02:
            self.wrongAnswers.append(self.answer - 0.01)
            self.wrongAnswers.append(self.answer + 0.03)
        else:
            self.wrongAnswers.append(self.answer + 0.03)
            self.wrongAnswers.append(self.answer + 0.04)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ4(self):
        '''e.g.:
        What does the digit 7 stand for in 71453? '''
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.problem_type = "ProblemTypeMCQ4"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.number1 = randint(101,999)
        self.number2 = randint(101,999)
        while self.number1%10==0 or self.number1%100==0:
            self.number1 = randint(101,999)
        while self.number2%10==0 or self.number2%100==0:
            self.number2 = randint(101,999)

        self.FloatNumber1 = float(self.number1) / 100
        self.FloatNumber2 = float(self.number2) / 100
        
        self.problem = str(self.FloatNumber1)+" + "+str(self.FloatNumber2)+" = "
        
        self.answer = float(self.number1+self.number2) / 100

        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        self.wrongAnswers.append(self.answer + 0.01)
        self.wrongAnswers.append(self.answer + 0.02)        
        if self.answer > 0.02:
            self.wrongAnswers.append(self.answer - 0.01)
            self.wrongAnswers.append(self.answer - 0.02)
        elif self.answer > 0.01 and self.answer < 0.02:
            self.wrongAnswers.append(self.answer - 0.01)
            self.wrongAnswers.append(self.answer + 0.03)
        else:
            self.wrongAnswers.append(self.answer + 0.03)
            self.wrongAnswers.append(self.answer + 0.04)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ5(self):
        '''e.g.:
        What does the digit 7 stand for in 71453? '''
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.problem_type = "ProblemTypeMCQ5"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        
        self.answer = float(self.number1) / 10
        self.FloatNumber2 = float(self.number2) / 10
        self.FloatNumber1 = float(self.number1+self.number2) / 10 

        self.problem = str(self.FloatNumber1)+" - "+str(self.FloatNumber2)+" = "

        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        self.wrongAnswers.append(self.answer + 0.1)
        self.wrongAnswers.append(self.answer + 0.2)        
        if self.answer > 0.2:
            self.wrongAnswers.append(self.answer - 0.1)
            self.wrongAnswers.append(self.answer - 0.2)
        elif self.answer > 0.1 and self.answer < 0.2:
            self.wrongAnswers.append(self.answer - 0.1)
            self.wrongAnswers.append(self.answer + 0.3)
        else:
            self.wrongAnswers.append(self.answer + 0.3)
            self.wrongAnswers.append(self.answer + 0.4)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ6(self):
        '''e.g.:
        What does the digit 7 stand for in 71453? '''
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.problem_type = "ProblemTypeMCQ6"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.number1 = randint(11,99)
        self.number2 = randint(11,99)
        
        self.answer = float(self.number1) / 10
        self.FloatNumber2 = float(self.number2) / 10
        self.FloatNumber1 = float(self.number1+self.number2) / 10 
        
        self.problem = str(self.FloatNumber1)+" - "+str(self.FloatNumber2)+" = "

        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        self.wrongAnswers.append(self.answer + 0.1)
        self.wrongAnswers.append(self.answer + 0.2)        
        if self.answer > 0.2:
            self.wrongAnswers.append(self.answer - 0.1)
            self.wrongAnswers.append(self.answer - 0.2)
        elif self.answer > 0.1 and self.answer < 0.2:
            self.wrongAnswers.append(self.answer - 0.1)
            self.wrongAnswers.append(self.answer + 0.3)
        else:
            self.wrongAnswers.append(self.answer + 0.3)
            self.wrongAnswers.append(self.answer + 0.4)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ7(self):
        '''e.g.:
        What does the digit 7 stand for in 71453? '''
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.problem_type = "ProblemTypeMCQ7"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.number1 = randint(11,99)
        self.number2 = randint(11,99)

        self.answer = float(self.number1) / 100
        self.FloatNumber2 = float(self.number2) / 100
        self.FloatNumber1 = float(self.number1+self.number2) / 100
        
        self.problem = str(self.FloatNumber1)+" - "+str(self.FloatNumber2)+" = "

        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        self.wrongAnswers.append(self.answer + 0.01)
        self.wrongAnswers.append(self.answer + 0.02)        
        if self.answer > 0.02:
            self.wrongAnswers.append(self.answer - 0.01)
            self.wrongAnswers.append(self.answer - 0.02)
        elif self.answer > 0.01 and self.answer < 0.02:
            self.wrongAnswers.append(self.answer - 0.01)
            self.wrongAnswers.append(self.answer + 0.03)
        else:
            self.wrongAnswers.append(self.answer + 0.03)
            self.wrongAnswers.append(self.answer + 0.04)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ8(self):
        '''e.g.:
        What does the digit 7 stand for in 71453? '''
        '''e.g.:
        0.1 + 0.7 = '''
        
        self.problem_type = "ProblemTypeMCQ8"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.number1 = randint(101,999)
        self.number2 = randint(101,999)

        self.answer = float(self.number1) / 100
        self.FloatNumber2 = float(self.number2) / 100
        self.FloatNumber1 = float(self.number1+self.number2) / 100 
        
        self.problem = str(self.FloatNumber1)+" - "+str(self.FloatNumber2)+" = "

        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        self.wrongAnswers.append(self.answer + 0.01)
        self.wrongAnswers.append(self.answer + 0.02)        
        if self.answer > 0.02:
            self.wrongAnswers.append(self.answer - 0.01)
            self.wrongAnswers.append(self.answer - 0.02)
        elif self.answer > 0.01 and self.answer < 0.02:
            self.wrongAnswers.append(self.answer - 0.01)
            self.wrongAnswers.append(self.answer + 0.03)
        else:
            self.wrongAnswers.append(self.answer + 0.03)
            self.wrongAnswers.append(self.answer + 0.04)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.FloatNumber1,self.FloatNumber2,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)
                                                                                                                                                               
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False