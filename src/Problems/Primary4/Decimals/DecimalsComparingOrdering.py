'''
Created on Feb 28, 2012
Module: DecimalsComparingOrdering
Generates the "Decimals Comparing and Ordering" problems for Primary 4

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
import string

class DecimalsComparingOrdering:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            3:["ProblemTypeMCQ1",],
                            4:["ProblemType4",],
                            5:["ProblemTypeMCQ3",],
                            6:["ProblemType6",],
                            7:["ProblemTypeMCQ4",],
                            8:["ProblemType5",],
                            9:["ProblemType9",],
                            10:["ProblemType8",],
                            11:["ProblemTypeMCQ2",],
                            12:["ProblemType3",],
                            13:["ProblemType7",],
                            14:["ProblemTypeMCQ5",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemTypeMCQ1(),],
                                    4:[self.GenerateProblemType4(),],
                                    5:[self.GenerateProblemTypeMCQ3(),],
                                    6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemTypeMCQ4(),],
                                    8:[self.GenerateProblemType5(),],
                                    9:[self.GenerateProblemType9(),],
                                    10:[self.GenerateProblemType8(),],
                                    11:[self.GenerateProblemTypeMCQ2(),],
                                    12:[self.GenerateProblemType3(),],
                                    13:[self.GenerateProblemType7(),],
                                    14:[self.GenerateProblemTypeMCQ5(),],
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
        #return self.GenerateProblemTypeMCQ5()

    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            }
        return self.ProblemType[problem_type]
            
    def GenerateProblemType1(self):
        '''e.g.:
        0.1 more than 3.2 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(1,89)
        self.number2 = randint(1,9)
        
        self.FloatNumber1 = float(self.number1) / 10
        self.FloatNumber2 = float(self.number2) / 10
             
        self.problem = str(self.FloatNumber2)+" more than "+str(self.FloatNumber1)+" = "        
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1 + self.number2) / 10

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.FloatNumber1,self.FloatNumber2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType1(self,problem,answer,number1,number2,float1,float2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the below place value tables with the given numbers:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(float1)[0]+"</td><td>"+str(float1)[2]+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(float2)[0]+"</td><td>"+str(float2)[2]+"</td></tr></table><br>"

        self.solution_text = self.solution_text + "Now simply add the two numbers "
        self.solution_text = self.solution_text + "and fill the place value table with as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(answer)[0]+"</td><td>"+str(answer)[2]+"</td></tr></table><br>"
        
        self.solution_text = self.solution_text + "Hence, "+problem +"<i><b>"+str(answer)+"</i></b>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g.:
        0.1 less than 3.2 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(10,89)
        self.number2 = randint(1,9)
        
        self.FloatNumber1 = float(self.number1) / 10
        self.FloatNumber2 = float(self.number2) / 10
             
        self.problem = str(self.FloatNumber2)+" less than "+str(self.FloatNumber1)+" = "        
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1 - self.number2) / 10

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.FloatNumber1,self.FloatNumber2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType2(self,problem,answer,number1,number2,float1,float2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the below place value tables with the given numbers:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(float1)[0]+"</td><td>"+str(float1)[2]+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(float2)[0]+"</td><td>"+str(float2)[2]+"</td></tr></table><br>"

        self.solution_text = self.solution_text + "Now simply subtract the two numbers "
        self.solution_text = self.solution_text + "and fill the place value table with as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+str(answer)[0]+"</td><td>"+str(answer)[2]+"</td></tr></table><br>"
        
        self.solution_text = self.solution_text + "Hence, "+problem +"<i><b>"+str(answer)+"</i></b>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g.:
        0.01 more than 3.21 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(10,890)
        self.number2 = randint(1,9)

        self.FloatNumber1 = float(self.number1) / 100
        self.FloatNumber2 = float(self.number2) / 100
             
        self.problem = str(self.FloatNumber2)+" more than "+str(self.FloatNumber1)+" = "        
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1 + self.number2) / 100

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.FloatNumber1,self.FloatNumber2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType3(self,problem,answer,number1,number2,float1,float2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the below place value tables with the given numbers:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td><td>Hundredths</td></tr><tr>"
        for i in range(len(str(float1))):
            if i!=1:
                self.solution_text = self.solution_text + "<td>"+str(float1)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr><tr>"
        for i in range(len(str(float2))):
            if i!=1:
                self.solution_text = self.solution_text + "<td>"+str(float2)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"

        self.solution_text = self.solution_text + "Now simply add the two numbers "
        self.solution_text = self.solution_text + "and fill the place value table with as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td><td>Hundredths</td></tr><tr>"
        for i in range(len(str(answer))):
            if i!=1:
                self.solution_text = self.solution_text + "<td>"+str(answer)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "Hence, "+problem +"<i><b>"+str(answer)+"</i></b>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g.:
        0.1 less than 3.2 = '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(10,890)
        self.number2 = randint(1,9)

        self.FloatNumber1 = float(self.number1) / 100
        self.FloatNumber2 = float(self.number2) / 100
                     
        self.problem = str(self.FloatNumber2)+" less than "+str(self.FloatNumber1)+" = "        
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1 - self.number2) / 100

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.FloatNumber1,self.FloatNumber2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType4(self,problem,answer,number1,number2,float1,float2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the below place value tables with the given numbers:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td><td>Hundredths</td></tr><tr>"
        for i in range(len(str(float1))):
            if i!=1:
                self.solution_text = self.solution_text + "<td>"+str(float1)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr><tr>"
        for i in range(len(str(float2))):
            if i!=1:
                self.solution_text = self.solution_text + "<td>"+str(float2)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"

        self.solution_text = self.solution_text + "Now simply subtract the two numbers "
        self.solution_text = self.solution_text + "and fill the place value table with as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td><td>Hundredths</td></tr><tr>"
        for i in range(len(str(answer))):
            if i!=1:
                self.solution_text = self.solution_text + "<td>"+str(answer)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "Hence, "+problem +"<i><b>"+str(answer)+"</i></b>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType5(self):
        '''e.g.:
        0.001 more than 3.214 = '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(100,8900)
        self.number2 = randint(1,9)

        self.FloatNumber1 = float(self.number1) / 1000
        self.FloatNumber2 = float(self.number2) / 1000
             
        self.problem = str(self.FloatNumber2)+" more than "+str(self.FloatNumber1)+" = "        
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1 + self.number2) / 1000

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.FloatNumber1,self.FloatNumber2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType5(self,problem,answer,number1,number2,float1,float2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the below place value tables with the given numbers:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td><td>Hundredths</td><td>Thousandths</td></tr><tr>"
        for i in range(len(str(float1))):
            if i!=1:
                self.solution_text = self.solution_text + "<td>"+str(float1)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr><tr>"
        for i in range(len(str(float2))):
            if i!=1:
                self.solution_text = self.solution_text + "<td>"+str(float2)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"

        self.solution_text = self.solution_text + "Now simply add the two numbers "
        self.solution_text = self.solution_text + "and fill the place value table with as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td><td>Hundredths</td><td>Thousandths</td></tr><tr>"
        for i in range(len(str(answer))):
            if i!=1:
                self.solution_text = self.solution_text + "<td>"+str(answer)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "Hence, "+problem +"<i><b>"+str(answer)+"</i></b>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType6(self):
        '''e.g.:
        0.001 less than 3.214 = '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(100,8900)
        self.number2 = randint(1,9)

        self.FloatNumber1 = float(self.number1) / 1000
        self.FloatNumber2 = float(self.number2) / 1000
                             
        self.problem = str(self.FloatNumber2)+" less than "+str(self.FloatNumber1)+" = "        
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1 - self.number2) / 1000

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.FloatNumber1,self.FloatNumber2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType6(self,problem,answer,number1,number2,float1,float2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the below place value tables with the given numbers:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td><td>Hundredths</td><td>Thousandths</td></tr><tr>"
        for i in range(len(str(float1))):
            if i!=1:
                self.solution_text = self.solution_text + "<td>"+str(float1)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr><tr>"
        for i in range(len(str(float2))):
            if i!=1:
                self.solution_text = self.solution_text + "<td>"+str(float2)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"

        self.solution_text = self.solution_text + "Now simply subtract the two numbers "
        self.solution_text = self.solution_text + "and fill the place value table with as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td><td>Hundredths</td><td>Thousandths</td></tr><tr>"
        for i in range(len(str(answer))):
            if i!=1:
                self.solution_text = self.solution_text + "<td>"+str(answer)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "Hence, "+problem +"<i><b>"+str(answer)+"</i></b>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7(self):
        '''e.g.:
        Complete the number pattern:
        6.4,6.5,___,6.7,6.8'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.numbers=[]
        self.number1 = randint(41,80)
        self.number2 = randint(1,5)
        
        self.number = float(self.number1) / 10
        '''Adding the first number to the numbers list'''       
        self.numbers.append(str(self.number))
        
        self.pattern = float(self.number2) / 10
        
        '''50% of the time the pattern will be added and 50% of the time it will be subtracted'''
        if(randint(1,2)==1):
            for _i in range(4):
                self.number = self.number + self.pattern
                self.numbers.append(str(self.number))
            self.flag = "add"
        else:
            for _i in range(4):
                self.number = self.number - self.pattern
                self.numbers.append(str(self.number))
            self.flag = "sub"
                 
        missingNumber = randint(0,len(self.numbers)-1)
       
        self.answer = self.numbers[missingNumber]
        self.numbers[missingNumber] = "___"
        
        self.problem = "Complete the number pattern:<br><br>%s, %s, %s, %s, %s "%(self.numbers[0],self.numbers[1],
                                                                    self.numbers[2],self.numbers[3],self.numbers[4])
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,str(self.answer),self.numbers,missingNumber,self.flag,self.pattern)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def GenerateProblemType8(self):
        '''e.g.:
        Complete the number pattern:
        6.41,6.51,___,6.71,6.81'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.numbers=[]
        self.number1 = randint(441,800)
        self.number2 = randint(1,5)
        
        self.number = float(self.number1) / 100
        '''Adding the first number to the numbers list'''       
        self.numbers.append(str(self.number))
        
        self.pattern = float(self.number2) / 100
        
        '''50% of the time the pattern will be added and 50% of the time it will be subtracted'''
        if(randint(1,2)==1):
            for _i in range(4):
                self.number = self.number + self.pattern
                self.numbers.append(str(self.number))
            self.flag = "add"
        else:
            for _i in range(4):
                self.number = self.number - self.pattern
                self.numbers.append(str(self.number))
            self.flag = "sub"
                 
        missingNumber = randint(0,len(self.numbers)-1)
       
        self.answer = self.numbers[missingNumber]
        self.numbers[missingNumber] = "___"
        
        self.problem = "Complete the number pattern:<br><br>%s, %s, %s, %s, %s "%(self.numbers[0],self.numbers[1],
                                                                    self.numbers[2],self.numbers[3],self.numbers[4])
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        '''Explanation same as Problem Type 7'''
        self.explain_text = self.ExplainType7(self.problem,str(self.answer),self.numbers,missingNumber,self.flag,self.pattern)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def GenerateProblemType9(self):
        '''e.g.:
        Complete the number pattern:
        6.41,6.51,___,6.71,6.81'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.numbers=[]
        self.number1 = randint(4011,8000)
        self.number2 = randint(1,5)
        
        self.number = float(self.number1) / 1000
        '''Adding the first number to the numbers list'''       
        self.numbers.append(str(self.number))
        
        self.pattern = float(self.number2) / 1000
        
        '''50% of the time the pattern will be added and 50% of the time it will be subtracted'''
        if(randint(1,2)==1):
            for _i in range(4):
                self.number = self.number + self.pattern
                self.numbers.append(str(self.number))
            self.flag = "add"
        else:
            for _i in range(4):
                self.number = self.number - self.pattern
                self.numbers.append(str(self.number))
            self.flag = "sub"
                 
        missingNumber = randint(0,len(self.numbers)-1)
       
        self.answer = self.numbers[missingNumber]
        self.numbers[missingNumber] = "___"
        
        self.problem = "Complete the number pattern:<br><br>%s, %s, %s, %s, %s "%(self.numbers[0],self.numbers[1],
                                                                    self.numbers[2],self.numbers[3],self.numbers[4])
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        '''Explanation same as Problem Type 7'''
        self.explain_text = self.ExplainType7(self.problem,str(self.answer),self.numbers,missingNumber,self.flag,self.pattern)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}
        
    def ExplainType7(self,problem,answer,numbers,missingNumber,flag,pattern):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        if missingNumber == 0:
            self.solution_text = self.solution_text + "Since the first number is blank, lets compare numbers 2 and 3<br>"
            if flag == "add":
                self.solution_text = self.solution_text + "Number 3 is greater than number 2. The difference between the two numbers is ("+numbers[2]+" - "+numbers[1]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 3 by adding "+str(pattern)+" to "+numbers[1]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 3 and number 4. Difference between these two numbers is ("+numbers[3]+" - "+numbers[2]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by adding "+str(pattern)+" to the previous number."
                self.solution_text = self.solution_text + "So the pattern is to add "+str(pattern)+" to the previous number which means the number 2 ("+str(numbers[1])+ " ) in the series came by adding "+str(pattern)+" to the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to subtract "+str(pattern)+" from "+str(numbers[1])+"<br>"
                self.solution_text = self.solution_text + str(numbers[1])+" - "+str(pattern)+" = "+str(answer)
            elif flag == "sub":
                self.solution_text = self.solution_text + "Number 3 is less than number 2. The difference between the two numbers is ("+numbers[1]+" - "+numbers[2]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 3 by subtracting "+str(pattern)+" from "+numbers[1]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 3 and number 4. Difference between these two numbers is ("+numbers[2]+" - "+numbers[3]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by subtracting "+str(pattern)+" from the previous number."
                self.solution_text = self.solution_text + "So the pattern is to subtract "+str(pattern)+" from the previous number which means the number 2 ("+str(numbers[1])+ " ) in the series came by subtracting "+str(pattern)+" from the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to add "+str(pattern)+" to "+str(numbers[1])+"<br>"
                self.solution_text = self.solution_text + str(numbers[1])+" + "+str(pattern)+" = "+str(answer)
        elif missingNumber == 1:
            self.solution_text = self.solution_text + "Since the second number is blank, lets compare numbers 3 and 4<br>"
            if flag == "add":
                self.solution_text = self.solution_text + "Number 4 is greater than number 3. The difference between the two numbers is ("+numbers[3]+" - "+numbers[2]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 4 by adding "+str(pattern)+" to "+numbers[2]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 4 and number 5. Difference between these two numbers is ("+numbers[4]+" - "+numbers[3]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by adding "+str(pattern)+" to the previous number."
                self.solution_text = self.solution_text + "So the pattern is to add "+str(pattern)+" to the previous number which means the number 3 ("+str(numbers[2])+ " ) in the series came by adding "+str(pattern)+" to the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to add "+str(pattern)+" to "+str(numbers[0])+"<br>"
                self.solution_text = self.solution_text + str(numbers[0])+" + "+str(pattern)+" = "+str(answer)
            elif flag == "sub":
                self.solution_text = self.solution_text + "Number 4 is less than number 3. The difference between the two numbers is ("+numbers[2]+" - "+numbers[3]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 4 by subtracting "+str(pattern)+" from "+numbers[2]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 4 and number 5. Difference between these two numbers is ("+numbers[3]+" - "+numbers[4]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by subtracting "+str(pattern)+" from the previous number."
                self.solution_text = self.solution_text + "So the pattern is to subtract "+str(pattern)+ " from the previous number which means the number 3 ("+str(numbers[2])+ " ) in the series came by subtracting "+str(pattern)+" from the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to subtract "+str(pattern)+" from "+str(numbers[0])+"<br>"
                self.solution_text = self.solution_text + str(numbers[0])+" - "+str(pattern)+" = "+str(answer)
        elif missingNumber == 2:
            self.solution_text = self.solution_text + "First compare numbers 1 and 2<br>"
            if flag == "add":
                self.solution_text = self.solution_text + "Number 2 is greater than number 1. The difference between the two numbers is ("+numbers[1]+" - "+numbers[0]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 2 by adding "+str(pattern)+" to "+numbers[0]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 4 and number 5. Difference between these two numbers is ("+numbers[4]+" - "+numbers[3]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by adding "+str(pattern)+" to the previous number."
                self.solution_text = self.solution_text + "So the pattern is to add "+str(pattern)+" to the previous number which means the number 4 ("+str(numbers[3])+ " ) in the series came by adding "+str(pattern)+" to the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to add "+str(pattern)+" to "+str(numbers[1])+"<br>"
                self.solution_text = self.solution_text + str(numbers[1])+" + "+str(pattern)+" = "+str(answer)
            elif flag == "sub":
                self.solution_text = self.solution_text + "Number 1 is greater than number 2. The difference between the two numbers is ("+numbers[0]+" - "+numbers[1]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 2 by subtracting "+str(pattern)+" from "+numbers[0]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 4 and number 5. Difference between these two numbers is ("+numbers[3]+" - "+numbers[4]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by subtracting "+str(pattern)+" from the previous number."
                self.solution_text = self.solution_text + "So the pattern is to subtract "+str(pattern)+" from the previous number which means the number 4 ("+str(numbers[3])+ " ) in the series came by subtracting "+str(pattern)+" from the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to subtract "+str(pattern)+" from "+str(numbers[1])+"<br>"
                self.solution_text = self.solution_text + str(numbers[1])+" - "+str(pattern)+" = "+str(answer)
        elif missingNumber == 3:
            self.solution_text = self.solution_text + "First compare numbers 1 and 2<br>"
            if flag == "add":
                self.solution_text = self.solution_text + "Number 2 is greater than number 1. The difference between the two numbers is ("+numbers[1]+" - "+numbers[0]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 2 by adding "+str(pattern)+" to "+numbers[0]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 2 and number 3. Difference between these two numbers is ("+numbers[2]+" - "+numbers[1]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by adding "+str(pattern)+" to the previous number."
                self.solution_text = self.solution_text + "So the pattern is to add "+str(pattern)+" to the previous number which means the number 5 ("+str(numbers[4])+ " ) in the series came by adding "+str(pattern)+" to the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to add "+str(pattern)+" to "+str(numbers[2])+"<br>"
                self.solution_text = self.solution_text + str(numbers[2])+" + "+str(pattern)+" = "+str(answer)
            elif flag == "sub":
                self.solution_text = self.solution_text + "Number 1 is greater than number 2. The difference between the two numbers is ("+numbers[0]+" - "+numbers[1]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 2 by subtracting "+str(pattern)+" from "+numbers[0]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 2 and number 3. Difference between these two numbers is ("+numbers[1]+" - "+numbers[2]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by subtracting "+str(pattern)+" from the previous number."
                self.solution_text = self.solution_text + "So the pattern is to subtract "+str(pattern)+" from the previous number which means the number 5 ("+str(numbers[4])+ " ) in the series came by subtracting "+str(pattern)+" from the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to subtract "+str(pattern)+" from "+str(numbers[2])+"<br>"
                self.solution_text = self.solution_text + str(numbers[2])+" - "+str(pattern)+" = "+str(answer)
        elif missingNumber == 4:
            self.solution_text = self.solution_text + "First compare numbers 1 and 2<br>"
            if flag == "add":
                self.solution_text = self.solution_text + "Number 2 is greater than number 1. The difference between the two numbers is ("+numbers[1]+" - "+numbers[0]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 2 by adding "+str(pattern)+" to "+numbers[0]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 2 and number 3. Difference between these two numbers is ("+numbers[2]+" - "+numbers[1]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by adding "+str(pattern)+" to the previous number.<br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to add "+str(pattern)+" to "+str(numbers[3])+"<br><br>"
                self.solution_text = self.solution_text + str(numbers[3])+" + "+str(pattern)+" = "+str(answer)
            elif flag == "sub":
                self.solution_text = self.solution_text + "Number 1 is greater than number 2. The difference between the two numbers is ("+numbers[0]+" - "+numbers[1]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 2 by subtracting "+str(pattern)+" from "+numbers[0]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 2 and number 3. Difference between these two numbers is ("+numbers[1]+" - "+numbers[2]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by subtracting "+str(pattern)+" from the previous number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to subtract "+str(pattern)+" from "+str(numbers[3])+"<br>"
                self.solution_text = self.solution_text + str(numbers[3])+" - "+str(pattern)+" = "+str(answer)       
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the missing number in the pattern is "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain   

    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore,grade,CheckAnswerType):
        
        self.answer1=''
        self.answer2=''
        self.answer3=''
        self.answer4=''
                             
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
        

    def GenerateMCQ1(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore,grade,CheckAnswerType):
        
        '''Removing correct answers from the wrongAnswers list'''
        #wrongAnswers = filter(self.removeCorrectAnswer,wrongAnswers)
        
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
                'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}
                     
    def GenerateProblemTypeMCQ1(self):
        '''e.g.
        Which number is the greatest:
        7.8
        6.9
        6.6
        7.5
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.CheckAnswerType = 1
        
        self.problem_type = "ProblemTypeMCQ1"
        i=0
        self.numbers=[]
        while i!=4:
            number = randint(10,99)
            FloatNumber = float(number)/10   
            if(FloatNumber not in self.numbers):
                self.numbers.append(FloatNumber)
                i=i+1
        self.problem = "Which number is the greatest:"
        
        self.answer = max(self.numbers)
        
        self.template = "MCQTypeProblems.html"
        
        '''List of wrong answers is same as the list of numbers displayed'''
        self.wrongAnswers = list(self.numbers)    
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ1(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def ExplainTypeMCQ1(self,problem,answer,numbers):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "First fill the place value table with the numbers as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenth</td></tr>"
        self.ones = []
        self.tenths = []
        NumbersCopy = list(numbers)
        StringNumbers = []
        j = 0
        for i in range(4):
            self.ones.append(int(str(NumbersCopy[i])[0]))
            StringNumbers.append(str(NumbersCopy[i]))
            
        for i in range(len(NumbersCopy)):
            self.solution_text = self.solution_text + "<tr><td>"+str(NumbersCopy[i])[0]+"</td><td>"+str(NumbersCopy[i])[2]+"</td></tr>"
            if float(str(NumbersCopy[i])[0]) != max(self.ones):
                del StringNumbers[i-j]
                j = j + 1
            else:
                self.tenths.append(int(str(NumbersCopy[i])[2]))

        self.solution_text = self.solution_text + "</table><br>"
        self.solution_text = self.solution_text + "Now compare the digits from left to right<br><br>"
        self.solution_text = self.solution_text + "First compare the ones<br><br>"
        self.solution_text = self.solution_text + str(max(self.ones))+" is the greatest digit in ones place and it belongs to "+str(StringNumbers)+"<br><br>"
        if len(StringNumbers)>1:
            self.solution_text = self.solution_text + "Since the ones digit is same for these numbers, let's compare tenths digit<br><br>"
            self.solution_text = self.solution_text + str(max(self.tenths))+" is the greatest digit in tenths place and it belongs to "+str(answer)+"<br><br>"
        self.solution_text = self.solution_text + "Hence the greatest number is: <i><b>"+str(answer)+"</b></i>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ2(self):
        '''e.g.
        Which number is the greatest:
        7.8
        6.9
        6.6
        7.5
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.grade = 4
        self.CheckAnswerType = 1
        
        self.problem_type = "ProblemTypeMCQ2"
        i=0
        self.numbers=[]
        self.digit1 = randint(1,9)
        while i!=4:
            number = randint(10,99)
            FloatNumber = self.digit1 + float(number)/100           
            if(FloatNumber not in self.numbers):
                self.numbers.append(FloatNumber)
                i=i+1
       
        self.problem = "Which number is the smallest:"
        
        self.answer = min(self.numbers)
        
        self.template = "MCQTypeProblems.html"
        
        '''List of wrong answers is same as the list of numbers displayed'''
        self.wrongAnswers = list(self.numbers)    
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ2(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def ExplainTypeMCQ2(self,problem,answer,numbers):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "First fill the place value table with the numbers as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td><td>Hundredths</td></tr>"
        for i in range(len(numbers)):
            if len(str(numbers[i]))==3:
                numbers[i] = str(numbers[i])+"0"
            self.solution_text = self.solution_text + "<tr><td>"+str(numbers[i])[0]+"</td><td>"+str(numbers[i])[2]+"</td><td>"+str(numbers[i])[3]+"</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        self.solution_text = self.solution_text + "Now compare the numbers from left to right. The number which has the smallest digit is the smallest.<br><br>"
        self.solution_text = self.solution_text + "If two digits are same then move on to the next digit."
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the smallest number is "+answer+"</b></i>"        
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ3(self):
        '''e.g.
        Which number is the greatest:
        7.8
        6.9
        6.6
        7.5
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.grade = 4
        self.CheckAnswerType = 1
        
        self.problem_type = "ProblemTypeMCQ3"
        i=0
        self.numbers=[]
        self.digit12 = float(randint(10,99)/10)
        while i!=4:
            number = randint(10,99)
            FloatNumber = self.digit12 + float(number) / 1000                       
            if(FloatNumber not in self.numbers):
                self.numbers.append(FloatNumber)
                i=i+1
        self.problem = "Which number is the greatest:"
        
        self.answer = max(self.numbers)
        
        self.template = "MCQTypeProblems.html"
        
        '''List of wrong answers is same as the list of numbers displayed'''
        self.wrongAnswers = list(self.numbers)    
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ3(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def ExplainTypeMCQ3(self,problem,answer,numbers):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "First fill the place value table with the numbers as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td><td>Hundredths</td><td>Thousandths</td></tr>"
        for i in range(len(numbers)):
            if len(str(numbers[i]))==3:
                numbers[i] = str(numbers[i])+"00"
            elif len(str(numbers[i]))==4:
                numbers[i] = str(numbers[i])+"0"
            self.solution_text = self.solution_text + "<tr><td>"+str(numbers[i])[0]+"</td><td>"+str(numbers[i])[2]+"</td><td>"+str(numbers[i])[3]+"</td><td>"+str(numbers[i])[4]+"</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        self.solution_text = self.solution_text + "Now compare the numbers from left to right. The number which has the greatest digit is the greatest.<br><br>"
        self.solution_text = self.solution_text + "If two digits are same then move on to the next digit."
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the greatest number is "+answer+"</b></i>"        
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        return self.explain

    def GenerateProblemTypeMCQ4(self):
        '''e.g.
        Arrange the numbers in increasing order:
        2.3, 4.5, 6.5, 4.3
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.grade = 4
        self.CheckAnswerType = 2
        
        self.problem_type = "ProblemTypeMCQ4"
        i=0
        self.numbers=[]
        while i!=4:
            number = randint(10,99)           
            FloatNumber = float(number)/10           
            if(FloatNumber not in self.numbers):
                self.numbers.append(FloatNumber)
                i=i+1
        self.problem = "Arrange the number in increasing order:<br><br>"
        self.problem = self.problem + str(self.numbers[0])+", "+str(self.numbers[1])+", "+str(self.numbers[2])+", "+str(self.numbers[3])
        
        """Sorting the numbers in increasing order"""
        self.numbers.sort()
                       
        self.answer = str(self.numbers[0])+", "+str(self.numbers[1])+", "+str(self.numbers[2])+", "+str(self.numbers[3])
        
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        self.wrongAnswers.append(str(self.numbers[3])+", "+str(self.numbers[1])+", "+str(self.numbers[2])+", "+str(self.numbers[0]))
        self.wrongAnswers.append(str(self.numbers[0])+", "+str(self.numbers[2])+", "+str(self.numbers[1])+", "+str(self.numbers[3]))
        self.wrongAnswers.append(str(self.numbers[0])+", "+str(self.numbers[1])+", "+str(self.numbers[3])+", "+str(self.numbers[2]))    
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ4(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ1(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def ExplainTypeMCQ4(self,problem,answer,numbers):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "First fill the place value table with the numbers as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td></tr>"
        for i in range(len(numbers)):
            self.solution_text = self.solution_text + "<tr><td>"+str(numbers[i])[0]+"</td><td>"+str(numbers[i])[2]+"</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        self.solution_text = self.solution_text + "Now compare the numbers from left to right. The number which has the smallest digit is the smallest.<br><br>"
        self.solution_text = self.solution_text + "The smallest number will come first. Next, compare the remaining three numbers from left to right.<br><br>"
        self.solution_text = self.solution_text + "Find the next smallest number. Follow the same process until you arrange all the numbers.<br><br>"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the greatest number is "+answer+"</b></i>"        
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        return self.explain

    def GenerateProblemTypeMCQ5(self):
        '''e.g.
        Arrange the numbers in decreasing order:
        2.3, 4.5, 6.5, 4.3
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.grade = 4
        self.CheckAnswerType = 2
        
        self.problem_type = "ProblemTypeMCQ5"
        i=0
        self.numbers=[]
        while i!=4:
            number = randint(10,99)
            FloatNumber = float(number)/10           
            if(FloatNumber not in self.numbers):
                self.numbers.append(FloatNumber)
                i=i+1
        self.problem = "Arrange the number in decreasing order:<br><br>"
        self.problem = self.problem + str(self.numbers[0])+", "+str(self.numbers[1])+", "+str(self.numbers[2])+", "+str(self.numbers[3])
        
        """Sorting the numbers in increasing order"""
        self.numbers.sort(reverse=True)
                       
        self.answer = str(self.numbers[0])+", "+str(self.numbers[1])+", "+str(self.numbers[2])+", "+str(self.numbers[3])
        
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers = []
        
        self.wrongAnswers.append(str(self.numbers[3])+", "+str(self.numbers[1])+", "+str(self.numbers[2])+", "+str(self.numbers[0]))
        self.wrongAnswers.append(str(self.numbers[0])+", "+str(self.numbers[2])+", "+str(self.numbers[1])+", "+str(self.numbers[3]))
        self.wrongAnswers.append(str(self.numbers[0])+", "+str(self.numbers[1])+", "+str(self.numbers[3])+", "+str(self.numbers[2]))    
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ5(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ1(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def ExplainTypeMCQ5(self,problem,answer,numbers):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "First fill the place value table with the numbers as shown below:<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1>"
        self.solution_text = self.solution_text + "<tr><td>Ones</td><td>Tenths</td></tr>"
        for i in range(len(numbers)):
            self.solution_text = self.solution_text + "<tr><td>"+str(numbers[i])[0]+"</td><td>"+str(numbers[i])[2]+"</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        self.solution_text = self.solution_text + "Now compare the numbers from left to right. The number which has the greatest digit is the greatest.<br><br>"
        self.solution_text = self.solution_text + "The greatest number will come first. Next, compare the remaining three numbers from left to right.<br><br>"
        self.solution_text = self.solution_text + "Find the next greatest number. Follow the same process until you arrange all the numbers."
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the greatest number is "+answer+"</b></i>"        
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        return self.explain
                        
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False                           
        elif CheckAnswer==2:
            try:
                return (string.join(answer.split(),"")==str(InputAnswer))
            except ValueError:
                return False                           
    