'''
Created on Jan 18, 2011

Module: UnitConversion
Generates "Conversion of unit" problems for Primary 5

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

class UnitConversion:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        self.ProblemList = [self.GenerateProblemType1(),self.GenerateProblemType2()]
        return random.choice(self.ProblemList)
        #return self.GenerateProblemType2()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:"ProblemType1",2:"ProblemType2",}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemType2(),}
        
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
        #return self.GenerateProblemType2()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g.:
        Express 1.043 km in metres'''
        
        #self.number = str(randint(1,99))+"."+str(randint(0,9))+str(randint(0,9))+str(randint(1,8))
        self.number = randint(1234,99123)
        self.number1 = randint(123,9982)

        self.problem1 = "Express "+str(float(self.number)/1000)+" km in metres:"
        self.problem2 = "Express "+str(float(self.number)/1000)+" kg in grams:"
        self.problem3 = "Express "+str(float(self.number)/1000)+" litres in millilitres:"
        self.problem4 = "Express "+str(float(self.number1)/100)+" m in centimetres:"
              
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
        
        self.answer = self.number

        if self.problem == self.problem1:
            self.unit = "metres"
            self.flag = 1
        elif self.problem == self.problem2:
            self.unit = "grams"
            self.flag = 2
        elif self.problem == self.problem3:
            self.unit = "millilitres"
            self.flag = 3
        elif self.problem == self.problem4:
            self.unit = "centimetres"
            self.answer = self.number1
            self.flag = 4
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number,self.number1,self.flag,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",'unit':self.unit}

    def ExplainType1(self,problem,answer,number,number1,flag,unit):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+" "+unit
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "1 km = 1000 m<br><br>"
            self.solution_text = self.solution_text + "When converting from km to m, you are converting to a smaller unit, hence you need to multiply by the conversion factor.<br><br>"
            self.solution_text = self.solution_text + "When a number is multiplied by 1000, its decimal point shifts 3 places to the right.<br><br>"
            self.solution_text = self.solution_text + "= "+str(float(number)/1000)+" &times; 1000 = "+str(answer)
        elif flag == 2:
            self.solution_text = self.solution_text + "1 kg = 1000 g<br><br>"
            self.solution_text = self.solution_text + "When converting from kg to g, you are converting to a smaller unit, hence you need to multiply by the conversion factor.<br><br>"
            self.solution_text = self.solution_text + "When a number is multiplied by 1000, its decimal point shifts 3 places to the right.<br><br>"
            self.solution_text = self.solution_text + "= "+str(float(number)/1000)+" &times; 1000 = "+str(answer)
        elif flag == 3:
            self.solution_text = self.solution_text + "1 l = 1000 ml<br><br>"
            self.solution_text = self.solution_text + "When converting from l to ml, you are converting to a smaller unit, hence you need to multiply by the conversion factor.<br><br>"
            self.solution_text = self.solution_text + "When a number is multiplied by 1000, its decimal point shifts 3 places to the right.<br><br>"
            self.solution_text = self.solution_text + "= "+str(float(number)/1000)+" &times; 1000 = "+str(answer)
        elif flag == 4:
            self.solution_text = self.solution_text + "1 m = 100 cm<br><br>"
            self.solution_text = self.solution_text + "When converting from m to cm, you are converting to a smaller unit, hence you need to multiply by the conversion factor.<br><br>"
            self.solution_text = self.solution_text + "When a number is multiplied by 100, its decimal point shifts 2 places to the right.<br><br>"
            self.solution_text = self.solution_text + "= "+str(float(number1)/100)+" &times; 100 = "+str(answer)
        
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+str(answer)+" "+unit+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.:
        Express 1043 m in km'''

        self.number = randint(1234,99123)
        self.number1 = randint(123,9982)
                        
        self.problem1 = "Express "+str(self.number)+" m in km:"
        self.problem2 = "Express "+str(self.number)+" g in kg:"
        self.problem3 = "Express "+str(self.number)+" ml in litres:"
        self.problem4 = "Express "+str(self.number1)+" cm in m:"
              
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])

        self.answer = float(self.number) / 1000
        
        if self.problem == self.problem1:
            self.unit = "km"
            self.flag = 1
        elif self.problem == self.problem2:
            self.unit = "kg"
            self.flag = 2
        elif self.problem == self.problem3:
            self.unit = "litres"
            self.flag = 3
        elif self.problem == self.problem4:
            self.unit = "m"
            self.answer = float(self.number1) / 100
            self.flag = 4
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.number1,self.flag,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",'unit':self.unit}

    def ExplainType2(self,problem,answer,number,number1,flag,unit):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+" "+unit
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "1 km = 1000 m<br><br>"
            self.solution_text = self.solution_text + "When converting from m to km, you are converting to a bigger unit, hence you need to divide by the conversion factor.<br><br>"
            self.solution_text = self.solution_text + "When a number is divided by 1000, its decimal point shifts 3 places to the left.<br><br>"
            self.solution_text = self.solution_text + "= "+str(self.number)+" &divide; 1000 = "+str(answer)
        elif flag == 2:
            self.solution_text = self.solution_text + "1 kg = 1000 g<br><br>"
            self.solution_text = self.solution_text + "When converting from g to kg, you are converting to a bigger unit, hence you need to divide by the conversion factor.<br><br>"
            self.solution_text = self.solution_text + "When a number is divided by 1000, its decimal point shifts 3 places to the left.<br><br>"
            self.solution_text = self.solution_text + "= "+str(self.number)+" &divide; 1000 = "+str(answer)
        elif flag == 3:
            self.solution_text = self.solution_text + "1 l = 1000 ml<br><br>"
            self.solution_text = self.solution_text + "When converting from ml to l, you are converting to a bigger unit, hence you need to divide by the conversion factor.<br><br>"
            self.solution_text = self.solution_text + "When a number is divided by 1000, its decimal point shifts 3 places to the left.<br><br>"
            self.solution_text = self.solution_text + "= "+str(self.number)+" &divide; 1000 = "+str(answer)
        elif flag == 4:
            self.solution_text = self.solution_text + "1 m = 100 cm<br><br>"
            self.solution_text = self.solution_text + "When converting from cm to m, you are converting to a bigger unit, hence you need to divide by the conversion factor.<br><br>"
            self.solution_text = self.solution_text + "When a number is divided by 100, its decimal point shifts 2 places to the left.<br><br>"
            self.solution_text = self.solution_text + "= "+str(self.number1)+" &divide; 100 = "+str(answer)
        
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+str(answer)+" "+unit+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer):
        try:
            #20-08-2011 changed the int(answer)==int(InputAnswer) to float(answer)==float(InputAnswer). As you cannot make int when there is a decimal place in the answer
            return (float(answer)==float(InputAnswer))
        except ValueError:
            return False  