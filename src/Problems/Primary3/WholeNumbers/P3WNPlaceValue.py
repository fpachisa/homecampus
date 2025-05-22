'''
Created on Feb 16, 2013
Module: P3WNPlaceValue
Generates the PlaceValue problems for Primary 3

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
import logging

class P3WNPlaceValue:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1a","ProblemType1b","ProblemTypeMCQ1a","ProblemTypeMCQ1b",],
                            2:["ProblemType2a","ProblemType2b","ProblemTypeMCQ2a","ProblemTypeMCQ2b",],
                            3:["ProblemType3a","ProblemType3b","ProblemTypeMCQ3a","ProblemTypeMCQ3b",],
                            4:["ProblemType4a","ProblemType4b","ProblemTypeMCQ4a","ProblemTypeMCQ4b",],
                            5:["ProblemType5a","ProblemType5b","ProblemType5c","ProblemTypeMCQ5a","ProblemTypeMCQ5b","ProblemTypeMCQ5c",],
                            6:["ProblemType6","ProblemTypeMCQ6",],
                            7:["ProblemType7a","ProblemType7b","ProblemTypeMCQ7a","ProblemTypeMCQ7b",],
                            8:["ProblemType8a","ProblemType8b","ProblemType8c","ProblemType8d","ProblemTypeMCQ8a","ProblemTypeMCQ8b","ProblemTypeMCQ8c","ProblemTypeMCQ8d",],
                            9:["ProblemType9","ProblemTypeMCQ9",],
                            10:["ProblemType10","ProblemTypeMCQ10",],
                            11:["ProblemType11","ProblemTypeMCQ11",],
                            12:["ProblemType12a","ProblemType12b","ProblemTypeMCQ12a","ProblemTypeMCQ12b",],
                            13:["ProblemType13a","ProblemType13b","ProblemType13c","ProblemType13d","ProblemTypeMCQ13a","ProblemTypeMCQ13b","ProblemTypeMCQ13c","ProblemTypeMCQ13d",],
                            14:["ProblemType14a","ProblemType14b","ProblemTypeMCQ14a","ProblemTypeMCQ14b",],
                            15:["ProblemType15","ProblemTypeMCQ15",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1a(),self.GenerateProblemType1b(),self.GenerateProblemTypeMCQ1a(),self.GenerateProblemTypeMCQ1b(),],
                                    2:[self.GenerateProblemType2a(),self.GenerateProblemType2b(),self.GenerateProblemTypeMCQ2a(),self.GenerateProblemTypeMCQ2b(),],
                                    3:[self.GenerateProblemType3a(),self.GenerateProblemType3b(),self.GenerateProblemTypeMCQ3a(),self.GenerateProblemTypeMCQ3b(),],
                                    4:[self.GenerateProblemType4a(),self.GenerateProblemType4b(),self.GenerateProblemTypeMCQ4a(),self.GenerateProblemTypeMCQ4b(),],
                                    5:[self.GenerateProblemType5a(),self.GenerateProblemType5b(),self.GenerateProblemType5c(),self.GenerateProblemTypeMCQ5a(),self.GenerateProblemTypeMCQ5b(),self.GenerateProblemTypeMCQ5c(),],
                                    6:[self.GenerateProblemType6(),self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemType7a(),self.GenerateProblemType7b(),self.GenerateProblemTypeMCQ7a(),self.GenerateProblemTypeMCQ7b(),],
                                    8:[self.GenerateProblemType8a(),self.GenerateProblemType8b(),self.GenerateProblemType8c(),self.GenerateProblemType8d(),
                                       self.GenerateProblemTypeMCQ8a(),self.GenerateProblemTypeMCQ8b(),self.GenerateProblemTypeMCQ8c(),self.GenerateProblemTypeMCQ8d(),],
                                    9:[self.GenerateProblemType9(),self.GenerateProblemTypeMCQ9(),],
                                    10:[self.GenerateProblemType10(),self.GenerateProblemTypeMCQ10(),],
                                    11:[self.GenerateProblemType11(),self.GenerateProblemTypeMCQ11(),],
                                    12:[self.GenerateProblemType12a(),self.GenerateProblemType12b(),self.GenerateProblemTypeMCQ12a(),self.GenerateProblemTypeMCQ12b(),],                                    
                                    13:[self.GenerateProblemType13a(),self.GenerateProblemType13b(),self.GenerateProblemType13c(),self.GenerateProblemType13d(),
                                       self.GenerateProblemTypeMCQ13a(),self.GenerateProblemTypeMCQ13b(),self.GenerateProblemTypeMCQ13c(),self.GenerateProblemTypeMCQ13d(),],
                                    14:[self.GenerateProblemType14a(),self.GenerateProblemType14b(),self.GenerateProblemTypeMCQ14a(),self.GenerateProblemTypeMCQ14b(),],
                                    15:[self.GenerateProblemType15(),self.GenerateProblemTypeMCQ15(),],
                                    }        
        
        #Creating one more problem type so it creates a list and not a list of lists
        self.ProblemTypes = []
        
        for i in self.ProblemType.values():
            for k in i:
                self.ProblemTypes.append(k)
        
        
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(self.GenerateProblemType[1])
        else:
            if LastProblemID in self.ProblemTypes:
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if LastProblemID in v][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return random.choice(self.GenerateProblemType[NextProblemKey])
            else:
                return random.choice(self.GenerateProblemType[1])
        #return self.GenerateProblemType1a()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1a":self.GenerateProblemType1a(),"ProblemType1b":self.GenerateProblemType1b(),
                            "ProblemType2a":self.GenerateProblemType2a(),"ProblemType2b":self.GenerateProblemType2b(),
                            "ProblemType3a":self.GenerateProblemType3a(),"ProblemType3b":self.GenerateProblemType3b(),
                            "ProblemType4a":self.GenerateProblemType4a(),"ProblemType4b":self.GenerateProblemType4b(),
                            "ProblemType5a":self.GenerateProblemType5a(),"ProblemType5b":self.GenerateProblemType5b(),"ProblemType5c":self.GenerateProblemType5c(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7a":self.GenerateProblemType7a(),"ProblemType7b":self.GenerateProblemType7b(),
                            "ProblemType8a":self.GenerateProblemType8a(),"ProblemType8b":self.GenerateProblemType8b(),
                            "ProblemType8c":self.GenerateProblemType8c(),"ProblemType8d":self.GenerateProblemType8d(),
                            "ProblemType9":self.GenerateProblemType9(),"ProblemType10":self.GenerateProblemType10(),"ProblemType11":self.GenerateProblemType11(),
                            "ProblemType12a":self.GenerateProblemType12a(),"ProblemType12b":self.GenerateProblemType12b(),
                            "ProblemType13a":self.GenerateProblemType13a(),"ProblemType13b":self.GenerateProblemType13b(),
                            "ProblemType13c":self.GenerateProblemType13c(),"ProblemType13d":self.GenerateProblemType13d(),
                            "ProblemType14a":self.GenerateProblemType14a(),"ProblemType14b":self.GenerateProblemType14b(),
                            "ProblemType15":self.GenerateProblemType15(),
                            "ProblemTypeMCQ1a":self.GenerateProblemTypeMCQ1a(),"ProblemTypeMCQ1b":self.GenerateProblemTypeMCQ1b(),
                            "ProblemTypeMCQ2a":self.GenerateProblemTypeMCQ2a(),"ProblemTypeMCQ2b":self.GenerateProblemTypeMCQ2b(),
                            "ProblemTypeMCQ3a":self.GenerateProblemTypeMCQ3a(),"ProblemTypeMCQ3b":self.GenerateProblemTypeMCQ3b(),
                            "ProblemTypeMCQ4a":self.GenerateProblemTypeMCQ4a(),"ProblemTypeMCQ4b":self.GenerateProblemTypeMCQ4b(),
                            "ProblemTypeMCQ5a":self.GenerateProblemTypeMCQ5a(),"ProblemTypeMCQ5b":self.GenerateProblemTypeMCQ5b(),"ProblemTypeMCQ5c":self.GenerateProblemTypeMCQ5c(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemTypeMCQ7a":self.GenerateProblemTypeMCQ7a(),"ProblemTypeMCQ7b":self.GenerateProblemTypeMCQ7b(),
                            "ProblemTypeMCQ8a":self.GenerateProblemTypeMCQ8a(),"ProblemTypeMCQ8b":self.GenerateProblemTypeMCQ8b(),
                            "ProblemTypeMCQ8c":self.GenerateProblemTypeMCQ8c(),"ProblemTypeMCQ8d":self.GenerateProblemTypeMCQ8d(),
                            "ProblemTypeMCQ9":self.GenerateProblemTypeMCQ9(),"ProblemTypeMCQ10":self.GenerateProblemTypeMCQ10(),
                            "ProblemTypeMCQ11":self.GenerateProblemTypeMCQ11(),
                            "ProblemTypeMCQ12a":self.GenerateProblemTypeMCQ12a(),"ProblemTypeMCQ12b":self.GenerateProblemTypeMCQ12b(),
                            "ProblemTypeMCQ13a":self.GenerateProblemTypeMCQ13a(),"ProblemTypeMCQ13b":self.GenerateProblemTypeMCQ13b(),
                            "ProblemTypeMCQ13c":self.GenerateProblemTypeMCQ13c(),"ProblemTypeMCQ13d":self.GenerateProblemTypeMCQ13d(),
                            "ProblemTypeMCQ14a":self.GenerateProblemTypeMCQ14a(),"ProblemTypeMCQ14b":self.GenerateProblemTypeMCQ14b(),
                            "ProblemTypeMCQ15":self.GenerateProblemTypeMCQ15(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1a(self):       
        '''e.g.:
        In 9824, which digit is in the <ones, tens, hundreds, thousands> place? '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
            
        self.digitPlace = {"ones":3,"tens":2,"hundreds":1,"thousands":0}
        
        self.place = self.digitPlace.keys()[randint(0,len(self.digitPlace)-1)]
        self.digit = self.digits[self.digitPlace[self.place]]
        
        self.answer = self.digits[self.digitPlace[self.place]]
        self.problem = "In %s, which digit is in the %s place?" %(self.number,self.place)
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.number,self.place,self.digit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def GenerateProblemType1b(self):       
        '''e.g.:
        In 9824, the digit 8 is in the __________ place.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
            
        self.digitPlace = {"ones":3,"tens":2,"hundreds":1,"thousands":0}
        
        self.place = self.digitPlace.keys()[randint(0,len(self.digitPlace)-1)]
        
        self.digit = self.digits[self.digitPlace[self.place]]
        self.answer = self.place
        
        self.problem = "In %s, the digit %s is in the ______ place." %(self.number,self.digit)
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.number,self.place,self.digit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}

    def ExplainType1(self,problem,answer,number,place,digit):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        self.solution_text = self.PlaceValueTable1(int(number))
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In %s, the digit %d is in the %s place."%(number,digit,place)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2a(self):
        '''e.g.:
        What does the digit 2 stand for in 9824? '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.digitPlace = randint(0,len(self.digits)-1)      
        self.randomDigit = self.digits[self.digitPlace]
        
        self.problem = "What does the digit %s stand for in %s?" %(self.randomDigit, self.number)
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.randomDigit
        self.multiplier = str(1)
        for _i in range(4-self.digitPlace-1):
            self.multiplier = self.multiplier + '0'
        
        self.answer = str(self.answer*int(self.multiplier))

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.randomDigit,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            
    
    def GenerateProblemType2b(self):
        '''e.g.:
        In 9824, the digit _______ stands for 20. '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.digitPlace = randint(0,len(self.digits)-1)      
        self.randomDigit = self.digits[self.digitPlace]
        
        self.number1 = self.randomDigit
        self.multiplier = str(1)
        for _i in range(4-self.digitPlace-1):
            self.multiplier = self.multiplier + '0'
        
        self.number1 = str(self.number1*int(self.multiplier))

        self.problem = "In %s, the digit ______ stands for %s?" %(self.number,self.number1)
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.randomDigit

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.randomDigit,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType2(self,problem,answer,number,RandomDigit,multiplier):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = self.PlaceValueTable2(int(number))
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In %s, the digit %d stands for %d."%(number,int(RandomDigit),int(RandomDigit)*int(multiplier))
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType3a(self):
        '''e.g.:
        What is the value of the digit 2 in 9824? '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.digitPlace = randint(0,len(self.digits)-1)      
        self.randomDigit = self.digits[self.digitPlace]
        
        self.problem = "What is the value of the digit %s in %s?" %(self.randomDigit, self.number)
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.randomDigit
        self.multiplier = str(1)
        for _i in range(4-self.digitPlace-1):
            self.multiplier = self.multiplier + '0'
        
        self.answer = str(self.answer*int(self.multiplier))

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number,self.randomDigit,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            
    
    def GenerateProblemType3b(self):
        '''e.g.:
        In 9824, the digit _______ stands for 20. '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.digitPlace = randint(0,len(self.digits)-1)      
        self.randomDigit = self.digits[self.digitPlace]
        
        self.number1 = self.randomDigit
        self.multiplier = str(1)
        for _i in range(4-self.digitPlace-1):
            self.multiplier = self.multiplier + '0'
        
        self.number1 = str(self.number1*int(self.multiplier))

        self.problem = "In %s, the value of the digit ______ is %s?" %(self.number,self.number1)
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.randomDigit

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number,self.randomDigit,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType3(self,problem,answer,number,RandomDigit,multiplier):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = self.PlaceValueTable2(int(number))
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In %s, the value of the digit %d is %d."%(number,int(RandomDigit),int(RandomDigit)*int(multiplier))
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType4a(self):
        '''e.g.:
        9000, 20, 4 and 800 make _____. '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        self.numbers = []
        self.numbersInOrder = []
        
        self.digitPlace = 3
        for d in self.digits:
            self.number = self.number + str(d)
            self.numbers.append(d*int('1'+'0'*self.digitPlace))
            self.numbersInOrder.append(d*int('1'+'0'*self.digitPlace))
            self.digitPlace = self.digitPlace - 1

        random.shuffle(self.numbers)
        
        self.problem = "%d, %d, %d and %d make ______." %(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3])
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.number

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4a(self.problem,self.answer,self.number,self.numbers,self.numbersInOrder)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            
    
    def ExplainType4a(self,problem,answer,number,numbers,numbersInOrder):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<br><div class='side'><font style='font-size:0.9em;'>First, arrange the numbers from greatest to smallest. Then, add.</font></div>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s &nbsp;+&nbsp; %s &nbsp;+&nbsp; %s &nbsp;+&nbsp; %s &nbsp;=&nbsp; %s<br><br>"%(numbersInOrder[0],numbersInOrder[1],numbersInOrder[2],numbersInOrder[3],number)
        self.solution_text = self.solution_text + "%s, %s, %s and %s make %s."%(numbers[0],numbers[1],numbers[2],numbers[3],number)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType4b(self):
        '''e.g.:
        9000, 20, 4 and 800 make _____. '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        self.numbers = []
        self.numbersInOrder = []
        
        self.digitPlace = 3
        for d in self.digits:
            self.number = self.number + str(d)
            self.numbers.append(d*int('1'+'0'*self.digitPlace))
            self.numbersInOrder.append(d*int('1'+'0'*self.digitPlace))
            self.digitPlace = self.digitPlace - 1

        random.shuffle(self.numbers)
        
        self.problem = "%s is %d, %d, %d and ______." %(self.number, self.numbers[0],self.numbers[1],self.numbers[2])
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = str(self.numbers[3])

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4b(self.problem,self.answer,self.number,self.numbers,self.numbersInOrder)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType4b(self,problem,answer,number,numbers,numbersInOrder):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s &nbsp;=&nbsp; %s &nbsp;+&nbsp; %s &nbsp;+&nbsp; %s &nbsp;+&nbsp; %s<br><br>"%(number,numbersInOrder[0],numbersInOrder[1],numbersInOrder[2],numbersInOrder[3])
        self.solution_text = self.solution_text + "The missing number is %s."%(str(answer))
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType5a(self):
        '''e.g.:
        How many ones are there in 9824?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        
        '''Randomly select ones, tens, hundreds keyword in the problem'''
        self.problem = "How many ones are there in %s?" %(self.number)
        
        self.answer = self.number
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number,"ones",)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            
    
    def GenerateProblemType5b(self):
        '''e.g.:
        How many tens are there in 9820?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 3)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        
        self.number = self.number + '0'
        
        self.problem = "How many tens are there in %s?" %(self.number)
        
        self.answer = self.number[:-1]
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number,"tens",)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            
    
    def GenerateProblemType5c(self):
        '''e.g.:
        How many hundreds are there in 9820?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 2)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        
        self.number = self.number + '00'
        
        self.problem = "How many hundreds are there in %s?" %(self.number)
        
        self.answer = self.number[:-2]
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number,"hundreds",)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType5(self,problem,answer,number,place):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<br><font class='ExplanationFont'>"
        if place=="ones":
            self.solution_text = self.solution_text + "%s &nbsp;=&nbsp; %s &nbsp;&times;&nbsp; 1<br>"%(number,answer)
        elif place=="tens":
            self.solution_text = self.solution_text + "%s &nbsp;=&nbsp; %s &nbsp;&times;&nbsp; 10<br>"%(number,answer)
        elif place=="hundreds":
            self.solution_text = self.solution_text + "%s &nbsp;=&nbsp; %s &nbsp;&times;&nbsp; 100<br>"%(number,answer)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %s %s<br><br>"%(answer,place)
        
        self.solution_text = self.solution_text + "There are %s %s in %s."%(answer,place,number)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType6(self):
        '''e.g.:
            Find the missing number:
            9000 + 800 + ____ + 4 = 9824'''
        
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''First digit cannot be zero'''
        self.firstDigit = random.sample([1,2,3,4,5,6,7,8,9], 1)
        self.digits = random.sample([0,1,2,3,4,5,6,7,8,9], 3)
        self.digits = self.firstDigit + self.digits
        
        self.number = ''
        self.breakDown = []
        for d in self.digits:
            self.number = self.number + str(d)
        
        i = len(self.digits)
        while i != 0:
            self.breakDownDigit = str(self.digits[len(self.digits)-i])          
            i =i-1
            
            '''If the digit is zero don't generate the breakdown
            e.g.: 350847 = ___+50000+800+40+7'''
            if(self.breakDownDigit!='0'):
                for _j in range(i):
                    self.breakDownDigit = self.breakDownDigit + '0'
                self.breakDown.append(self.breakDownDigit)
        
        self.missingDigit = randint(0,len(self.breakDown)-1)
        rand = randint(1,10)
        '''80% of the time pattern would be 123456 = 100000+____+3000+400+50+6        
        20% of the time pattern would be ______ = 100000+20000+3000+400+50+6'''
        self.flag = 0
        self.actualNumber = int(self.number)
        if (rand<=8):
            self.answer = self.breakDown[self.missingDigit]
            self.breakDown[self.missingDigit]="___"
            self.flag = 1
        else:
            self.answer = self.number
            self.number = "___"
            self.flag = 2
        '''80% of the time pattern would be 123456 = 100000+____+3000+400+50+6        
        20% of the time pattern would be 123456 = 6+3000+100000+400+_____'''        
        if(rand<=8):       
            self.problem = "Find the missing number:<br> %s = %s" %(self.number," + ".join(self.breakDown))
        else:
            ''' copying to another list as don't want to shuffle the original list'''
            self.breakDown1 = list(self.breakDown)
            random.shuffle(self.breakDown1)
            self.problem = "Write the missing number:<br> %s = %s" %(self.number," + ".join(self.breakDown1))
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.actualNumber,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType6(self,problem,answer,actualNumber,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        thousands,remHundreds = divmod(actualNumber,1000)
        hundreds,remTens = divmod(remHundreds,100)
        tens,ones = divmod(remTens,10)
         
        self.solution_text = "<br><font class='ExplanationFont'>"
        if flag==1:
            self.solution_text = self.solution_text + "%s &nbsp;=&nbsp; %s"%(actualNumber,thousands*1000)
            if hundreds*100>0:
                self.solution_text = self.solution_text + " &nbsp;+&nbsp; %s"%(hundreds*100)
            if tens*10>0:
                self.solution_text = self.solution_text + " &nbsp;+&nbsp; %s"%(tens*10)
            if ones>0:
                self.solution_text = self.solution_text + " &nbsp;+&nbsp; %s<br><br>"%(ones)
        else:
            self.solution_text = self.solution_text + "%s"%(thousands*1000)
            if hundreds*100>0:
                self.solution_text = self.solution_text + " &nbsp;+&nbsp; %s"%(hundreds*100)
            if tens*10>0:
                self.solution_text = self.solution_text + " &nbsp;+&nbsp; %s"%(tens*10)
            if ones>0:
                self.solution_text = self.solution_text + " &nbsp;+&nbsp; %s"%(ones)
            self.solution_text = self.solution_text + " &nbsp;=&nbsp; %s<br><br>"%(actualNumber) 
        self.solution_text = self.solution_text + "The missing number is %s."%(str(answer))
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType7a(self):
        '''e.g.:
            How many <tens / hundreds> must be added to 7824 to get 8124?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.digits = random.sample([1,2,3,4,5], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
            
        self.digitPlace = {"tens":10,"hundreds":100}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.answer = randint(3,40)
        self.finalNumber = self.digitPlace[self.digitPlace.keys()[self.randPlace]]*self.answer + int(self.number)        
        self.problem = "How many %s must be added to %s to make %d?" %(self.digitPlace.keys()[self.randPlace],self.number,self.finalNumber)
        self.unit = self.digitPlace.keys()[self.randPlace]
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number,self.finalNumber,self.unit,1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit}            
    
    def GenerateProblemType7b(self):
        '''e.g.:
            How many <tens / hundreds> must be subtracted 8124 to get 7824?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.digits = random.sample([1,2,3,4,5], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
            
        self.digitPlace = {"tens":10,"hundreds":100}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.answer = randint(3,40)
        self.finalNumber = self.digitPlace[self.digitPlace.keys()[self.randPlace]]*self.answer + int(self.number)        
        self.problem = "How many %s must be subtracted from %d to get %s?" %(self.digitPlace.keys()[self.randPlace],self.finalNumber,self.number)
        self.unit = self.digitPlace.keys()[self.randPlace]
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number,self.finalNumber,self.unit,2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit}            

    def ExplainType7(self,problem,answer,number,finalNumber,unit,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<br><table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding-left:0px;padding-right:8px;'>%s &nbsp;&minus;&nbsp; %s</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%s</td></tr>"%(finalNumber,number,int(finalNumber)-int(number))
        if unit=="tens":
            self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding-left:0px;padding-right:8px;'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d &nbsp;&times;&nbsp; 10</td></tr>"%((int(finalNumber)-int(number))/10)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d %s</td></tr>"%((int(finalNumber)-int(number))/10,unit)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
            if flag==1:
                self.solution_text = self.solution_text + "%s tens must be added to %s to make %s.<br>"%(answer,number,finalNumber)
            elif flag==2:
                self.solution_text = self.solution_text + "%s tens must be subtracted from %s to get %s.<br>"%(answer,finalNumber,number)
            self.solution_text = self.solution_text + "</font>"
        elif unit=="hundreds":
            self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding-left:0px;padding-right:8px;'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d &nbsp;&times;&nbsp; 100</td></tr>"%((int(finalNumber)-int(number))/100)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d %s</td></tr>"%((int(finalNumber)-int(number))/100,unit)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
            if flag==1:
                self.solution_text = self.solution_text + "%s hundreds must be added to %s to make %s.<br>"%(answer,number,finalNumber)
            elif flag==2:
                self.solution_text = self.solution_text + "%s hundreds must be subtracted from %s to get %s.<br>"%(answer,finalNumber,number)
            self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType8a(self):
        '''e.g.:
            25 <tens / hundreds> more than 8590 is:'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        '''Generating a random number'''
        self.number = randint(1000,6000)
            
        self.digitPlace = {"tens":10,"hundreds":100,}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.multiplier = randint(10,25)
        
        self.problem = "%d %s more than %d is:" %(self.multiplier,self.digitPlace.keys()[self.randPlace],self.number)
        self.answer = (self.digitPlace[self.digitPlace.keys()[self.randPlace]])*self.multiplier + self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8a(self.problem,self.answer,self.number,self.multiplier,self.digitPlace.keys()[self.randPlace])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            
    
    def ExplainType8a(self,problem,answer,number,multiplier,digitPlace):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<br><table class='ExplanationTable'>"
        if digitPlace=="tens":
            self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding-left:0px;padding-right:8px;'>%d tens</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d &nbsp;&times;&nbsp; 10</td></tr>"%(multiplier,multiplier)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d</td></tr>"%(multiplier*10)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding-left:0px;padding-right:8px;'>%d &nbsp;+&nbsp; %d tens</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d &nbsp;+&nbsp; %d</td></tr>"%(number,multiplier,number,multiplier*10)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d</td></tr>"%(number+multiplier*10)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "%d tens more than %d is %d.<br>"%(multiplier,number,answer)
            self.solution_text = self.solution_text + "</font>"
        elif digitPlace=="hundreds":
            self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding-left:0px;padding-right:8px;'>%d hundreds</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d &nbsp;&times;&nbsp; 100</td></tr>"%(multiplier,multiplier)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d</td></tr>"%(multiplier*100)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding-left:0px;padding-right:8px;'>%d &nbsp;+&nbsp; %d hundreds</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d &nbsp;+&nbsp; %d</td></tr>"%(number,multiplier,number,multiplier*100)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d</td></tr>"%(number+multiplier*100)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "%d hundreds more than %d is %d.<br>"%(multiplier,number,answer)
            self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8b(self):
        '''e.g.:
            25 <tens / hundreds> less than 8590 is:'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        '''Generating a random number'''
        self.number = randint(3000,8000)
            
        self.digitPlace = {"tens":10,"hundreds":100,}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.multiplier = randint(10,25)
        
        self.problem = "%d %s less than %d is:" %(self.multiplier,self.digitPlace.keys()[self.randPlace],self.number)
        self.answer = self.number - (self.digitPlace[self.digitPlace.keys()[self.randPlace]])*self.multiplier
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8b(self.problem,self.answer,self.number,self.multiplier,self.digitPlace.keys()[self.randPlace])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            
    
    def ExplainType8b(self,problem,answer,number,multiplier,digitPlace):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<br><table class='ExplanationTable'>"
        if digitPlace=="tens":
            self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding-left:0px;padding-right:8px;'>%d tens</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d &nbsp;&times;&nbsp; 10</td></tr>"%(multiplier,multiplier)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d</td></tr>"%(multiplier*10)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding-left:0px;padding-right:8px;'>%d &nbsp;&minus;&nbsp; %d tens</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d &nbsp;&minus;&nbsp; %d</td></tr>"%(number,multiplier,number,multiplier*10)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d</td></tr>"%(number-multiplier*10)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "%d tens less than %d is %d.<br>"%(multiplier,number,answer)
            self.solution_text = self.solution_text + "</font>"
        elif digitPlace=="hundreds":
            self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding-left:0px;padding-right:8px;'>%d hundreds</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d &nbsp;&times;&nbsp; 100</td></tr>"%(multiplier,multiplier)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d</td></tr>"%(multiplier*100)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding-left:0px;padding-right:8px;'>%d &nbsp;&minus;&nbsp; %d hundreds</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d &nbsp;&minus;&nbsp; %d</td></tr>"%(number,multiplier,number,multiplier*100)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d</td></tr>"%(number-multiplier*100)
            self.solution_text = self.solution_text + "</table><br>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "%d hundreds less than %d is %d.<br>"%(multiplier,number,answer)
            self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8c(self):
        '''e.g.:
            1000 more than 7824 is __________.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        '''Generating a random number'''
        self.number = randint(1000,6000)
            
        self.digitPlace = {"tens":10,"hundreds":100,}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.multiplier = randint(1,25)
        
        self.number2 = (self.digitPlace[self.digitPlace.keys()[self.randPlace]])*self.multiplier
        
        self.problem = "%d more than %d is ______." %(self.number2,self.number)
        self.answer = self.number2 + self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8c(self.problem,self.answer,self.number,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType8c(self,problem,answer,number,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(number,number2,answer)
        self.solution_text = self.solution_text + "%d more than %d is %d.<br>"%(number2,number,answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType8d(self):
        '''e.g.:
            10 less than 5005 is _________.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        '''Generating a random number'''
        self.number = randint(3000,8000)
            
        self.digitPlace = {"tens":10,"hundreds":100,}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.multiplier = randint(1,25)
        
        self.number2 = (self.digitPlace[self.digitPlace.keys()[self.randPlace]])*self.multiplier
        
        self.problem = "%d less than %d is ______." %(self.number2,self.number)
        self.answer = self.number - self.number2
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8d(self.problem,self.answer,self.number,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8d",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType8d(self,problem,answer,number,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(number,number2,answer)
        self.solution_text = self.solution_text + "%d less than %d is %d.<br>"%(number2,number,answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType9(self):
        '''e.g.:
            6 thousands 95 tens 93 ones=______(in figures)'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.thousandDigit = randint(2,9)
        self.hundredDigit = randint(10,99)
        self.onesDigit = randint(10,99)
        
        self.numbers = [self.thousandDigit,self.hundredDigit,self.onesDigit]
        
        self.problem = "%d thousands %d tens %d ones &nbsp;=&nbsp; ______ (in figures)" % (self.thousandDigit,
                                                                                 self.hundredDigit,self.onesDigit)
        
        self.answer = self.thousandDigit*1000+self.hundredDigit*10+self.onesDigit
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType9(self,problem,answer,numbers):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<br><table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left;padding-left:0px;padding-right:8px;'>%d thousands %d tens %d ones</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d thousands &nbsp;+&nbsp; %d tens &nbsp;+&nbsp; %d ones</td></tr>"%(numbers[0],numbers[1],numbers[2],numbers[0],numbers[1],numbers[2])
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d &times; 1000 &nbsp;+&nbsp; %d &times; 10 &nbsp;+&nbsp; %d &times; 1</td></tr>"%(numbers[0],numbers[1],numbers[2])
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d</td></tr>"%(numbers[0]*1000,numbers[1]*10,numbers[2])
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px; padding-right:0px;'>=</td><td style='text-align:left;padding-left:8px;'>%d</td></tr>"%(numbers[0]*1000+numbers[1]*10+numbers[2])
        self.solution_text = self.solution_text + "</table><br>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType10(self):
        '''e.g.:
            What number is 400 more than 6782?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        '''Generating a random number'''
        self.number = randint(1000,6000)
            
        self.digitPlace = {"tens":10,"hundreds":100,}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.multiplier = randint(1,25)
        
        self.number2 = (self.digitPlace[self.digitPlace.keys()[self.randPlace]])*self.multiplier
        
        self.problem = "What number is %d more than %d?" %(self.number2,self.number)
        self.answer = self.number2 + self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.number,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType10(self,problem,answer,number,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(number,number2,answer)
        self.solution_text = self.solution_text + "%d is %d more than %d.<br>"%(answer,number2,number)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType11(self):
        '''e.g.:
        What does the digit 6 in the sum of 237 and 421 stand for? '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.digits = random.sample([4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
            
        self.digitPlace = randint(0,len(self.digits)-1)      
        self.randomDigit = self.digits[self.digitPlace]
        
        self.number1 = randint(400,2000)
        self.number2 = int(self.number) - self.number1
                
        self.problem = "What does the digit %s in the sum of %d and %d stand for?" %(self.randomDigit, self.number1, self.number2)
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.randomDigit
        self.multiplier = str(1) + '0'*(4-self.digitPlace-1)
        
        self.answer = str(self.answer*int(self.multiplier))

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.number1,self.number2,self.randomDigit,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType11(self,problem,answer,number1,number2,RandomDigit,multiplier):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "The sum of %d and %d is %d.<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + self.PlaceValueTable2(int(number1+number2))
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In %s, the digit %d stands for %d."%(number1+number2,int(RandomDigit),int(RandomDigit)*int(multiplier))
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType12a(self):
        '''e.g.:
        Use all the digits 1, 2, 3 to make the smallest 3-digit number. '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.digits = random.sample([4,5,6,7,8,9], 3)
        
        self.digits1 = list(self.digits)
        self.digits.sort()
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
                
        self.problem = "Use all the digits %d, %d, %d to make the smallest 3-digit number." %(self.digits1[0],self.digits1[1],self.digits1[2])
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.number

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12a(self.problem,self.answer,self.digits1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            
    
    def ExplainType12a(self,problem,answer,digits):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        digits.sort()
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Arrange the digits from smallest to greatest to make the smallest 3-digit number.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d<br><br>"%(digits[0],digits[1],digits[2])
        self.solution_text = self.solution_text + "The smallest 3-digit number is %s.<br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType12b(self):
        '''e.g.:
        Use all the digits 1, 2, 3 to make the greatest 3-digit number. '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.digits = random.sample([4,5,6,7,8,9], 3)
        
        self.digits1 = list(self.digits)
        self.digits.sort(reverse=True)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
                
        self.problem = "Use all the digits %d, %d, %d to make the greatest 3-digit number." %(self.digits1[0],self.digits1[1],self.digits1[2])
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.number

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12b(self.problem,self.answer,self.digits1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType12b(self,problem,answer,digits):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        digits.sort()
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Arrange the digits from greatest to smallest to make the greatest 3-digit number.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d<br><br>"%(digits[2],digits[1],digits[0])
        self.solution_text = self.solution_text + "The greatest 3-digit number is %s.<br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType13a(self):
        '''e.g.:
        Use all the digits 1, 2, 3 to make the smallest  3-digit  odd number.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.flag = randint(1,2)
        if self.flag == 1:
            '''generating 1 odd digit which will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],2)
            self.OddDigits = random.sample([1,3,5,7,9],1)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.EvenDigits.sort()
            self.number = ''
            for d in self.EvenDigits:
                self.number = self.number + str(d)
                    
            self.problem = "Use all the digits %d, %d, %d to make the smallest 3-digit odd number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number+str(self.OddDigits[0])
        else:
            '''generating 2 odd digits, the greater of these will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],1)
            self.OddDigits = random.sample([1,3,5,7,9],2)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.OddDigits.sort()
            if self.OddDigits[0] < self.EvenDigits[0]:
                self.number = str(self.OddDigits[0])+str(self.EvenDigits[0])+str(self.OddDigits[1])
            else:
                self.number = str(self.EvenDigits[0])+str(self.OddDigits[0])+str(self.OddDigits[1])
            
            self.problem = "Use all the digits %d, %d, %d to make the smallest 3-digit odd number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13a(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            
    
    def ExplainType13a(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "First, pick out the greatest odd digit from the given digits.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[2])
        self.solution_text = self.solution_text + "Next, arrange the remaining digits from smallest to greatest.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1])
        self.solution_text = self.solution_text + "Finally, attach the greatest odd digit that we picked out to the end of this list.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1],answer[2])
        self.solution_text = self.solution_text + "The smallest 3-digit odd number is %s.<br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType13b(self):
        '''e.g.:
        Use all the digits 1, 2, 3 to make the greatest  3-digit  odd number.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.flag = randint(1,2)
        if self.flag == 1:
            '''generating 1 odd digit which will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],2)
            self.OddDigits = random.sample([1,3,5,7,9],1)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.EvenDigits.sort(reverse=True)
            self.number = ''
            for d in self.EvenDigits:
                self.number = self.number + str(d)
                    
            self.problem = "Use all the digits %d, %d, %d to make the greatest 3-digit odd number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number+str(self.OddDigits[0])
        else:
            '''generating 2 odd digits, the smaller of these will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],1)
            self.OddDigits = random.sample([1,3,5,7,9],2)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.OddDigits.sort(reverse=True)
            if self.OddDigits[0] > self.EvenDigits[0]:
                self.number = str(self.OddDigits[0])+str(self.EvenDigits[0])+str(self.OddDigits[1])
            else:
                self.number = str(self.EvenDigits[0])+str(self.OddDigits[0])+str(self.OddDigits[1])
            
            self.problem = "Use all the digits %d, %d, %d to make the greatest 3-digit odd number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13b(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            
    
    def ExplainType13b(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "First, pick out the smallest odd digit from the given digits.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[2])
        self.solution_text = self.solution_text + "Next, arrange the remaining digits from greatest to smallest.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1])
        self.solution_text = self.solution_text + "Finally, attach the smallest odd digit that we picked out to the end of this list.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1],answer[2])
        self.solution_text = self.solution_text + "The greatest 3-digit odd number is %s.<br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType13c(self):
        '''e.g.:
        Use all the digits 1, 2, 3 to make the smallest  3-digit even number.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.flag = randint(1,2)
        if self.flag == 1:
            '''generating 1 even digit which will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],1)
            self.OddDigits = random.sample([1,3,5,7,9],2)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.OddDigits.sort()
            self.number = ''
            for d in self.OddDigits:
                self.number = self.number + str(d)
                    
            self.problem = "Use all the digits %d, %d, %d to make the smallest 3-digit even number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number+str(self.EvenDigits[0])
        else:
            '''generating 2 odd digits, the greater of these will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],2)
            self.OddDigits = random.sample([1,3,5,7,9],1)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.EvenDigits.sort()
            if self.EvenDigits[0] < self.OddDigits[0]:
                self.number = str(self.EvenDigits[0])+str(self.OddDigits[0])+str(self.EvenDigits[1])
            else:
                self.number = str(self.OddDigits[0])+str(self.EvenDigits[0])+str(self.EvenDigits[1])
                
            self.problem = "Use all the digits %d, %d, %d to make the smallest 3-digit even number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13c(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            
    
    def ExplainType13c(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "First, pick out the greatest even digit from the given digits.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[2])
        self.solution_text = self.solution_text + "Next, arrange the remaining digits from smallest to greatest.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1])
        self.solution_text = self.solution_text + "Finally, attach the greatest even digit that we picked out to the end of this list.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1],answer[2])
        self.solution_text = self.solution_text + "The smallest 3-digit even number is %s.<br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType13d(self):
        '''e.g.:
        Use all the digits 1, 2, 3 to make the greatest 3-digit even number.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.flag = randint(1,2)
        if self.flag == 1:
            '''generating 1 even digit which will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],1)
            self.OddDigits = random.sample([1,3,5,7,9],2)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.OddDigits.sort(reverse=True)
            self.number = ''
            for d in self.OddDigits:
                self.number = self.number + str(d)
                    
            self.problem = "Use all the digits %d, %d, %d to make the greatest 3-digit even number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number+str(self.EvenDigits[0])
        else:
            '''generating 2 odd digits, the smaller of these will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],2)
            self.OddDigits = random.sample([1,3,5,7,9],1)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.EvenDigits.sort(reverse=True)
            if self.EvenDigits[0] > self.OddDigits[0]:
                self.number = str(self.EvenDigits[0])+str(self.OddDigits[0])+str(self.EvenDigits[1])
            else:
                self.number = str(self.OddDigits[0])+str(self.EvenDigits[0])+str(self.EvenDigits[1])
            
            self.problem = "Use all the digits %d, %d, %d to make the greatest 3-digit even number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13d(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13d",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType13d(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "First, pick out the smallest even digit from the given digits.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[2])
        self.solution_text = self.solution_text + "Next, arrange the remaining digits from greatest to smallest.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1])
        self.solution_text = self.solution_text + "Finally, attach the smallest even digit that we picked out to the end of this list.<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1],answer[2])
        self.solution_text = self.solution_text + "The greatest 3-digit even number is %s.<br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType14a(self):
        '''e.g.:
        I am a 3-digit odd number. I am smaller than 500 but greater than 400. The digit in my tens place is 2 more/less than the digit in my hundreds place. You will find me if you count by fives. What number am I?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.flag = randint(1,3)
        if self.flag == 1:
            self.SmallerThan = random.randrange(200,500,100)
            self.GreaterThan = self.SmallerThan - 100
            self.hundredDigit = self.GreaterThan / 100
            
            self.TensDigit = randint(5,9)
            self.MoreLessThan = self.TensDigit - self.hundredDigit
                    
            self.problem = "I am a 3-digit odd number. I am smaller than %d but greater than %d. "%(self.SmallerThan, self.GreaterThan)
            self.problem = self.problem + "The digit in my tens place is %d more than the digit in my hundreds place. "%(self.MoreLessThan)
            self.problem = self.problem + "You will find me if you count by fives. What number am I?"
            self.answer = "%d%d5"%(self.hundredDigit,self.TensDigit)
        elif self.flag == 2:
            self.SmallerThan = random.randrange(600,900,100)
            self.GreaterThan = self.SmallerThan - 100
            self.hundredDigit = self.GreaterThan / 100
            
            self.TensDigit = randint(1,4)
            self.MoreLessThan = self.hundredDigit - self.TensDigit
                    
            self.problem = "I am a 3-digit odd number. I am smaller than %d but greater than %d. "%(self.SmallerThan, self.GreaterThan)
            self.problem = self.problem + "The digit in my tens place is %d less than the digit in my hundreds place. "%(self.MoreLessThan)
            self.problem = self.problem + "You will find me if you count by fives. What number am I?"
            self.answer = "%d%d5"%(self.hundredDigit,self.TensDigit)
        elif self.flag == 3:
            self.SmallerThan = random.randrange(200,900,100)
            self.GreaterThan = self.SmallerThan - 100
            self.hundredDigit = self.GreaterThan / 100
            
            self.TensDigit = self.hundredDigit
            self.MoreLessThan = self.hundredDigit - self.TensDigit
                    
            self.problem = "I am a 3-digit odd number. I am smaller than %d but greater than %d. "%(self.SmallerThan, self.GreaterThan)
            self.problem = self.problem + "The digit in my tens place is the same as the digit in my hundreds place. "
            self.problem = self.problem + "You will find me if you count by fives. What number am I?"
            self.answer = "%d%d5"%(self.hundredDigit,self.TensDigit)
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14a(self.problem,self.answer,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            
    
    def ExplainType14a(self,problem,answer,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The digit in the hundreds place is %s.<br><br>"%(answer[0])
        if flag==1:
            self.solution_text = self.solution_text + "The digit in the tens place is %d more than %s, so it is %s.<br><br>"%(int(answer[1])-int(answer[0]),answer[0],answer[1])
        elif flag==2:
            self.solution_text = self.solution_text + "The digit in the tens place is %d less than %s, so it is %s.<br><br>"%(int(answer[0])-int(answer[1]),answer[0],answer[1])
        else:
            self.solution_text = self.solution_text + "The digit in the tens place is the same as the digit in the hundreds place, so it is %d.<br><br>"%(int(answer[1]))
        self.solution_text = self.solution_text + "The digit in the ones place is 5.<br><br>"
        self.solution_text = self.solution_text + "So, the 3-digit odd number is %s.<br><br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType14b(self):
        '''e.g.:
        I am a 3-digit even number. I am smaller than 500 but greater than 400. The digit in my tens place is 2 more/less than the digit in my hundreds place. You will find me if you count by threes. What number am I?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.flag = randint(1,3)
        if self.flag == 1:
            self.SmallerThan = random.randrange(200,500,100)
            self.GreaterThan = self.SmallerThan - 100
            self.hundredDigit = self.GreaterThan / 100
            
            self.TensDigit = randint(5,9)
            self.MoreLessThan = self.TensDigit - self.hundredDigit
                    
            self.problem = "I am a 3-digit even number. I am smaller than %d but greater than %d. "%(self.SmallerThan, self.GreaterThan)
            self.problem = self.problem + "The digit in my tens place is %d more than the digit in my hundreds place. "%(self.MoreLessThan)
            self.problem = self.problem + "You will find me if you count by threes. What number am I?"
            self.answer = "%d%d6"%(self.hundredDigit,self.TensDigit)
        elif self.flag == 2:
            self.SmallerThan = random.randrange(600,900,100)
            self.GreaterThan = self.SmallerThan - 100
            self.hundredDigit = self.GreaterThan / 100
            
            self.TensDigit = randint(1,4)
            self.MoreLessThan = self.hundredDigit - self.TensDigit
                    
            self.problem = "I am a 3-digit even number. I am smaller than %d but greater than %d. "%(self.SmallerThan, self.GreaterThan)
            self.problem = self.problem + "The digit in my tens place is %d less than the digit in my hundreds place. "%(self.MoreLessThan)
            self.problem = self.problem + "You will find me if you count by threes. What number am I?"
            self.answer = "%d%d6"%(self.hundredDigit,self.TensDigit)
        elif self.flag == 3:
            self.SmallerThan = random.randrange(200,900,100)
            self.GreaterThan = self.SmallerThan - 100
            self.hundredDigit = self.GreaterThan / 100
            
            self.TensDigit = self.hundredDigit
            self.MoreLessThan = self.hundredDigit - self.TensDigit
                    
            self.problem = "I am a 3-digit even number. I am smaller than %d but greater than %d. "%(self.SmallerThan, self.GreaterThan)
            self.problem = self.problem + "The digit in my tens place is the same as the digit in my hundreds place. "
            self.problem = self.problem + "You will find me if you count by threes. What number am I?"
            self.answer = "%d%d6"%(self.hundredDigit,self.TensDigit)
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14b(self.problem,self.answer,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType14b(self,problem,answer,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The digit in the hundreds place is %s.<br><br>"%(answer[0])
        if flag==1:
            self.solution_text = self.solution_text + "The digit in the tens place is %d more than %s, so it is %s.<br><br>"%(int(answer[1])-int(answer[0]),answer[0],answer[1])
        elif flag==2:
            self.solution_text = self.solution_text + "The digit in the tens place is %d less than %s, so it is %s.<br><br>"%(int(answer[0])-int(answer[1]),answer[0],answer[1])
        else:
            self.solution_text = self.solution_text + "The digit in the tens place is the same as the digit in the hundreds place, so it is %d.<br><br>"%(int(answer[1]))
        self.solution_text = self.solution_text + "The digit in the ones place is 6.<br><br>"
        self.solution_text = self.solution_text + "So, the 3-digit even number is %s.<br><br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType15(self):
        '''e.g.:
        I am a 3-digit even number. I am smaller than 500 but greater than 400. The digit in my tens place is 2 more/less than the digit in my hundreds place. You will find me if you count by threes. What number am I?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                          
        self.number = randint(2001,8999)

        self.GreaterThan = (self.number / 1000)*1000
        self.SmallerThan = self.GreaterThan + 1000

        
        self.thousandDigit = self.number / 1000
        self.hundredDigit = self.number / 100 - 10*(self.number/1000)
        self.TensDigit = self.number / 10 - 10*(self.number/100)
        self.onesDigit = self.number - 10*(self.number/10)
        
        if self.onesDigit%2 == 0:
            self.EvenOdd = "even"
        else:
            self.EvenOdd = "odd"
                
        self.HundredsPlaceMoreLessThan = self.hundredDigit - self.thousandDigit
        if self.HundredsPlaceMoreLessThan > 0:
            self.HundredsPlaceMoreLessThanFlag = "more than"
        elif self.HundredsPlaceMoreLessThan < 0:
            self.HundredsPlaceMoreLessThanFlag = "less than"
        else:
            self.HundredsPlaceMoreLessThanFlag = "same as"
                
        self.TensPlaceMoreLessThan = self.TensDigit - self.hundredDigit
        if self.TensPlaceMoreLessThan > 0:
            self.TensPlaceMoreLessThanFlag = "more than"
        elif self.TensPlaceMoreLessThan < 0:
            self.TensPlaceMoreLessThanFlag = "less than"
        else:
            self.TensPlaceMoreLessThanFlag = "same as"
                
        self.OnesPlaceMoreLessThan = self.onesDigit - self.TensDigit
        if self.OnesPlaceMoreLessThan > 0:
            self.OnesPlaceMoreLessThanFlag = "more than"
        elif self.OnesPlaceMoreLessThan < 0:
            self.OnesPlaceMoreLessThanFlag = "less than"
        else:
            self.OnesPlaceMoreLessThanFlag = "same as"
            
        self.problem = "I am a 4-digit %s number. I am smaller than %d but greater than %d.<br>"%(self.EvenOdd,self.SmallerThan, self.GreaterThan)
        if self.HundredsPlaceMoreLessThanFlag != "same as":
            self.problem = self.problem + "The digit in my hundreds place is %d %s the digit in my thousands place.<br>"%(abs(self.HundredsPlaceMoreLessThan),self.HundredsPlaceMoreLessThanFlag)
        else:
            self.problem = self.problem + "The digit in my hundreds place is the same as the digit in my thousands place.<br>"
        if self.TensPlaceMoreLessThanFlag != "same as":
            self.problem = self.problem + "The digit in my tens place is %d %s the digit in my hundreds place.<br>"%(abs(self.TensPlaceMoreLessThan),self.TensPlaceMoreLessThanFlag)
        else:
            self.problem = self.problem + "The digit in my tens place is the same as the digit in my hundreds place.<br>"
        if self.HundredsPlaceMoreLessThanFlag != "same as":
            self.problem = self.problem + "The digit in my ones place is %d %s the digit in my tens place.<br>"%(abs(self.OnesPlaceMoreLessThan),self.OnesPlaceMoreLessThanFlag)
        else:
            self.problem = self.problem + "The digit in my ones place is the same as the digit in my tens place.<br>"

        self.problem = self.problem + "<br>What number am I?"
        self.answer = self.number
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.HundredsPlaceMoreLessThan,self.TensPlaceMoreLessThan,self.OnesPlaceMoreLessThan,self.EvenOdd)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType15",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType15(self,problem,answer,hundredsFlag,tensFlag,onesFlag,evenOdd):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        thousands,remHundreds = divmod(answer,1000)
        hundreds,remTens = divmod(remHundreds,100)
        tens,ones = divmod(remTens,10)
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The digit in the thousands place is %d.<br><br>"%(thousands)
        if hundredsFlag>0:        
            self.solution_text = self.solution_text + "The digit in the hundreds place is %d more than %d, so it is %d + %d or %d.<br><br>"%(hundreds-thousands,thousands,thousands,hundreds-thousands,hundreds)
        elif hundredsFlag<0:        
            self.solution_text = self.solution_text + "The digit in the hundreds place is %d less than %d, so it is %d &minus; %d or %d.<br><br>"%(thousands-hundreds,thousands,thousands,thousands-hundreds,hundreds)
        else:
            self.solution_text = self.solution_text + "The digit in the hundreds place is the same as the digit in the thousands place, so it is %d.<br><br>"%(hundreds)

        if tensFlag>0:        
            self.solution_text = self.solution_text + "The digit in the tens place is %d more than %d, so it is %d + %d or %d.<br><br>"%(tens-hundreds,hundreds,hundreds,tens-hundreds,tens)
        elif hundredsFlag<0:        
            self.solution_text = self.solution_text + "The digit in the tens place is %d less than %d, so it is %d &minus; %d or %d.<br><br>"%(hundreds-tens,hundreds,hundreds,hundreds-tens,tens)
        else:
            self.solution_text = self.solution_text + "The digit in the tens place is the same as the digit in the hundreds place, so it is %d.<br><br>"%(tens)

        if onesFlag>0:        
            self.solution_text = self.solution_text + "The digit in the ones place is %d more than %d, so it is %d + %d or %d.<br><br>"%(ones-tens,tens,tens,ones-tens,ones)
        elif hundredsFlag<0:        
            self.solution_text = self.solution_text + "The digit in the ones place is %d less than %d, so it is %d &minus; %d or %d.<br><br>"%(tens-ones,tens,tens,tens-ones,ones)
        else:
            self.solution_text = self.solution_text + "The digit in the ones place is the same as the digit in the tens place, so it is %d.<br><br>"%(ones)

        self.solution_text = self.solution_text + "So, the 4-digit %s number is %s.<br><br>"%(evenOdd,answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore,CheckAnswerType):
        
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
                'grade':3,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}
        

    def GenerateProblemTypeMCQ1a(self):
        '''e.g.:
        In 9824, which digit is in the <ones, tens, hundreds, thousands> place? '''
        
        self.problem_type = "ProblemTypeMCQ1a"
        self.complexity_level = "medium"
        self.HCScore = 5
        self.CheckAnswerType = 1

        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
            
        self.digitPlace = {"ones":3,"tens":2,"hundreds":1,"thousands":0}
        
        self.place = self.digitPlace.keys()[randint(0,len(self.digitPlace)-1)]
        self.digit = self.digits[self.digitPlace[self.place]]
        
        self.answer = self.digits[self.digitPlace[self.place]]
        self.problem = "In %s, which digit is in the %s place?" %(self.number,self.place)
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = self.digits    
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.number,self.place,self.digit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ1b(self):
        '''e.g.:
        In 9824, the digit 8 is in the __________ place.'''
        
        self.problem_type = "ProblemTypeMCQ1b"
        self.CheckAnswerType = 2
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
            
        self.digitPlace = {"ones":3,"tens":2,"hundreds":1,"thousands":0}
        
        self.place = self.digitPlace.keys()[randint(0,len(self.digitPlace)-1)]
        
        self.digit = self.digits[self.digitPlace[self.place]]
        self.answer = self.place
        
        self.problem = "In %s, the digit %s is in the ______ place." %(self.number,self.digit)
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = ["ones","tens","hundreds","thousands"]    
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.number,self.place,self.digit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ2a(self):
        '''e.g.:
        What does the digit 2 stand for in 9824? '''

        self.problem_type = "ProblemTypeMCQ2a"
        self.CheckAnswerType = 1
        self.complexity_level = "easy"
        self.HCScore = 3

        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.digitPlace = randint(0,len(self.digits)-1)      
        self.randomDigit = self.digits[self.digitPlace]
        
        self.problem = "What does the digit %s stand for in %s?" %(self.randomDigit, self.number)
        
        self.answer = self.randomDigit
        self.multiplier = str(1)
        for _i in range(4-self.digitPlace-1):
            self.multiplier = self.multiplier + '0'
        
        self.answer = self.answer*int(self.multiplier)
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.randomDigit,self.randomDigit*10,self.randomDigit*100,self.randomDigit*1000]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.randomDigit,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ2b(self):
        '''e.g.:
        In 9824, the digit _______ stands for 20. '''

        self.problem_type = "ProblemTypeMCQ2b"
        self.CheckAnswerType = 1

        self.complexity_level = "easy"
        self.HCScore = 3
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.digitPlace = randint(0,len(self.digits)-1)      
        self.randomDigit = self.digits[self.digitPlace]
        
        self.number1 = self.randomDigit
        self.multiplier = str(1)
        for _i in range(4-self.digitPlace-1):
            self.multiplier = self.multiplier + '0'
        
        self.number1 = str(self.number1*int(self.multiplier))

        self.problem = "In %s, the digit ______ stands for %s?" %(self.number,self.number1)

        self.answer = self.randomDigit
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = self.digits
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.randomDigit,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ3a(self):
        '''e.g.:
        What is the value of the digit 2 in 9824? '''

        self.problem_type = "ProblemTypeMCQ3a"
        self.CheckAnswerType = 1
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.digitPlace = randint(0,len(self.digits)-1)      
        self.randomDigit = self.digits[self.digitPlace]
        
        self.problem = "What is the value of the digit %s in %s?" %(self.randomDigit, self.number)
        
        self.answer = self.randomDigit
        self.multiplier = str(1)
        for _i in range(4-self.digitPlace-1):
            self.multiplier = self.multiplier + '0'
        
        self.answer = self.answer*int(self.multiplier)
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.randomDigit,self.randomDigit*10,self.randomDigit*100,self.randomDigit*1000]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number,self.randomDigit,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ3b(self):
        '''e.g.:
        In 9824, the digit _______ stands for 20. '''
        
        self.problem_type = "ProblemTypeMCQ3b"
        self.CheckAnswerType = 1
        self.complexity_level = "easy"
        self.HCScore = 3

        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.digitPlace = randint(0,len(self.digits)-1)      
        self.randomDigit = self.digits[self.digitPlace]
        
        self.number1 = self.randomDigit
        self.multiplier = str(1)
        for _i in range(4-self.digitPlace-1):
            self.multiplier = self.multiplier + '0'
        
        self.number1 = str(self.number1*int(self.multiplier))

        self.problem = "In %s, the value of the digit ______ is %s?" %(self.number,self.number1)

        self.answer = self.randomDigit
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = self.digits
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number,self.randomDigit,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ4a(self):
        '''e.g.:
        9000, 20, 4 and 800 make _____. '''
        
        self.problem_type = "ProblemTypeMCQ4a"
        self.CheckAnswerType = 1
        self.complexity_level = "medium"
        self.HCScore = 5

        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        self.numbers = []
        self.numbersInOrder = []
        
        self.digitPlace = 3
        for d in self.digits:
            self.number = self.number + str(d)
            self.numbers.append(d*int('1'+'0'*self.digitPlace))
            self.numbersInOrder.append(d*int('1'+'0'*self.digitPlace))
            self.digitPlace = self.digitPlace - 1

        random.shuffle(self.numbers)
        
        self.problem = "%d, %d, %d and %d make ______." %(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3])
        
        self.answer = self.number
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append("%d%d%d%d"%(self.digits[1],self.digits[2],self.digits[3],self.digits[0]))
        self.wrongAnswers.append("%d%d%d%d"%(self.digits[1],self.digits[3],self.digits[2],self.digits[0]))
        self.wrongAnswers.append("%d%d%d%d"%(self.digits[0],self.digits[2],self.digits[3],self.digits[1]))
        self.wrongAnswers.append("%d%d%d%d"%(self.digits[0],self.digits[3],self.digits[1],self.digits[2]))
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4a(self.problem,self.answer,self.number,self.numbers,self.numbersInOrder)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ4b(self):
        '''e.g.:
        9000, 20, 4 and 800 make _____. '''
        
        self.problem_type = "ProblemTypeMCQ4b"
        self.CheckAnswerType = 1
        self.complexity_level = "medium"
        self.HCScore = 5

        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        self.numbers = []
        self.numbersInOrder = []
        
        self.digitPlace = 3
        for d in self.digits:
            self.number = self.number + str(d)
            self.numbers.append(d*int('1'+'0'*self.digitPlace))
            self.numbersInOrder.append(d*int('1'+'0'*self.digitPlace))
            self.digitPlace = self.digitPlace - 1

        random.shuffle(self.numbers)
        
        self.problem = "%s is %d, %d, %d and ______." %(self.number, self.numbers[0],self.numbers[1],self.numbers[2])
                       
        self.answer = self.numbers[3]
                
        self.template = "MCQTypeProblems.html"
        
        self.firstDigit = int(str(self.numbers[3])[:1])
        self.wrongAnswers = [self.firstDigit,self.firstDigit*10,self.firstDigit*100,self.firstDigit*1000]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4b(self.problem,self.answer,self.number,self.numbers,self.numbersInOrder)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ5a(self):
        '''e.g.:
        How many ones are there in 9824?'''
        
        self.problem_type = "ProblemTypeMCQ5a"
        self.CheckAnswerType = 1
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        
        self.problem = "How many ones are there in %s?" %(self.number)
        
        self.answer = self.number
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number[:1],self.number[:2],self.number[:3]]
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number,"ones",)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ5b(self):
        '''e.g.:
        How many tens are there in 9820?'''
        
        self.problem_type = "ProblemTypeMCQ5b"
        self.CheckAnswerType = 1
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 3)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        
        self.number = self.number + '0'
        
        self.problem = "How many tens are there in %s?" %(self.number)
        
        self.answer = self.number[:-1]
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number[:1],self.number[:2],self.number[:4]]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number,"tens")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ5c(self):
        '''e.g.:
        How many hundreds are there in 9820?'''
        
        self.problem_type = "ProblemTypeMCQ5c"
        self.CheckAnswerType = 1

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 2)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        
        self.number = self.number + '00'
        
        self.problem = "How many hundreds are there in %s?" %(self.number)
        
        self.answer = self.number[:-2]
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number[:1],self.number[:3],self.number[:4]]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number,"hundreds")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ6(self):
        '''e.g.:
            Find the missing number:
            9000 + 800 + ____ + 4 = 9824'''
        
        self.problem_type = "ProblemTypeMCQ6"
        self.CheckAnswerType = 1
        self.complexity_level = "medium"
        self.HCScore = 5        

        '''First digit cannot be zero'''
        self.firstDigit = random.sample([1,2,3,4,5,6,7,8,9], 1)
        self.digits = random.sample([0,1,2,3,4,5,6,7,8,9], 3)
        self.digits = self.firstDigit + self.digits
        
        self.number = ''
        self.breakDown = []
        for d in self.digits:
            self.number = self.number + str(d)
            
        i = len(self.digits)
        while i != 0:
            self.breakDownDigit = str(self.digits[len(self.digits)-i])          
            i =i-1
            
            '''If the digit is zero don't generate the breakdown
            e.g.: 350847 = ___+50000+800+40+7'''
            if(self.breakDownDigit!='0'):
                for _j in range(i):
                    self.breakDownDigit = self.breakDownDigit + '0'
                self.breakDown.append(self.breakDownDigit)
        
        self.wrongAnswers = []
        '''Generating wrong answers'''            
        for i in range(len(self.breakDown)):
            self.wrongAnswers.append(self.breakDown[i]) 
                    
        self.missingDigit = randint(0,len(self.breakDown)-1)
        rand = randint(1,10)
        '''80% of the time pattern would be 123456 = 100000+____+3000+400+50+6        
        20% of the time pattern would be ______ = 100000+20000+3000+400+50+6'''
        self.flag = 0
        self.actualNumber = int(self.number)
        if (rand<=8):
            self.answer = self.breakDown[self.missingDigit]
            self.breakDown[self.missingDigit]="___"
            self.flag = 1
        else:
            self.answer = self.number
            self.number = "___"
            self.flag = 2
        '''80% of the time pattern would be 123456 = 100000+____+3000+400+50+6        
        20% of the time pattern would be 123456 = 6+3000+100000+400+_____'''        
        if(rand<=8):       
            self.problem = "Find the missing number:<br> %s = %s" %(self.number," + ".join(self.breakDown))
        else:
            ''' copying to another list as don't want to shuffle the original list'''
            self.breakDown1 = list(self.breakDown)
            random.shuffle(self.breakDown1)
            self.problem = "Write the missing number:<br> %s = %s" %(self.number," + ".join(self.breakDown1))
                
        self.template = "MCQTypeProblems.html"
        
        '''This problem type is not using generic method GenerateMCQ because only 2 wrong answers are 
        randomly selected in this problem unlike 3 in rest'''
        
        '''Removing correct answers from the wrongAnswers list'''
        self.wrongAnswers = filter(self.removeCorrectAnswer,self.wrongAnswers)
        
        '''Randomly selecting 2 wrong answer and 1 wrong answer and 1 correct answer is always included
        in this example the wrong answer which is always included is 7815'''                     
        self.wrongAnswers = random.sample(self.wrongAnswers,2)
        self.wrongAnswer =''
        for i in range(self.missingDigit,len(self.digits)):
            self.wrongAnswer = self.wrongAnswer + str(self.digits[i])
            
        '''If the correct answer is the last digit of the number then the wrong answer would be same as
        correct answer so checking for that. 
        for e.g.: 247815 = 200000+40000+7000+800+10+___. In this case wrong answer is changed to 55'''
        if (self.wrongAnswer==self.answer):
            self.wrongAnswer = self.wrongAnswer * 2
            
        self.wrongAnswers.append(self.wrongAnswer)
        self.wrongAnswers.append(self.answer)
        random.shuffle(self.wrongAnswers)
        self.answer1 = str(self.wrongAnswers[0])
        self.answer2 = str(self.wrongAnswers[1])
        self.answer3 = str(self.wrongAnswers[2])
        self.answer4 = str(self.wrongAnswers[3])        

        self.value1 = self.answer1
        self.value2 = self.answer2
        self.value3 = self.answer3
        self.value4 = self.answer4
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.actualNumber,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'answer4':self.answer4,'value1':self.value1,'value2':self.value2
                ,'value3':self.value3,'value4':self.value4,'explain':self.explain,'problem_type':self.problem_type,
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType}

    def GenerateProblemTypeMCQ7a(self):
        '''e.g.:
            How many <tens / hundreds> must be added to 7824 to get 8124?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.problem_type = "ProblemTypeMCQ7a"
        self.CheckAnswerType = 1       
        self.digits = random.sample([1,2,3,4,5], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
            
        self.digitPlace = {"tens":10,"hundreds":100}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.answer = randint(3,40)
        self.finalNumber = self.digitPlace[self.digitPlace.keys()[self.randPlace]]*self.answer + int(self.number)        
        self.problem = "How many %s must be added to %s to make %d?" %(self.digitPlace.keys()[self.randPlace],self.number,self.finalNumber)
        self.unit = self.digitPlace.keys()[self.randPlace]
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        while len(self.wrongAnswers)<3:
            self.wrongAnswer = randint(3,40)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer)
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number,self.finalNumber,self.unit,1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ7b(self):
        '''e.g.:
            How many <tens / hundreds> must be subtracted 8124 to get 7824?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ7b"
        self.CheckAnswerType = 1

        self.digits = random.sample([1,2,3,4,5], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
            
        self.digitPlace = {"tens":10,"hundreds":100}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.answer = randint(3,40)
        self.finalNumber = self.digitPlace[self.digitPlace.keys()[self.randPlace]]*self.answer + int(self.number)        
        self.problem = "How many %s must be subtracted from %d to get %s?" %(self.digitPlace.keys()[self.randPlace],self.finalNumber,self.number)
        self.unit = self.digitPlace.keys()[self.randPlace]
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        while len(self.wrongAnswers)<3:
            self.wrongAnswer = randint(3,40)
            if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                self.wrongAnswers.append(self.wrongAnswer)
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number,self.finalNumber,self.unit,2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ8a(self):
        '''e.g.:
            25 <tens / hundreds> more than 8590 is:'''
        
        self.complexity_level = "medium"
        self.HCScore = 5     
        self.problem_type = "ProblemTypeMCQ8a"
        self.CheckAnswerType = 1       

        '''Generating a random number'''
        self.number = randint(1000,6000)
            
        self.digitPlace = {"tens":10,"hundreds":100,}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.multiplier = randint(10,25)
        
        self.problem = "%d %s more than %d is:" %(self.multiplier,self.digitPlace.keys()[self.randPlace],self.number)
        self.answer = (self.digitPlace[self.digitPlace.keys()[self.randPlace]])*self.multiplier + self.number
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.multiplier*10+self.number,self.multiplier*100+self.number,self.multiplier+self.number,self.answer+10,self.answer+100]
        
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8a(self.problem,self.answer,self.number,self.multiplier,self.digitPlace.keys()[self.randPlace])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ8b(self):
        '''e.g.:
            25 <tens / hundreds> less than 8590 is:'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ8b"
        self.CheckAnswerType = 1       

        '''Generating a random number'''
        self.number = randint(3000,8000)
            
        self.digitPlace = {"tens":10,"hundreds":100,}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.multiplier = randint(10,25)
        
        self.problem = "%d %s less than %d is:" %(self.multiplier,self.digitPlace.keys()[self.randPlace],self.number)
        self.answer = self.number - (self.digitPlace[self.digitPlace.keys()[self.randPlace]])*self.multiplier
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number-self.multiplier*10,self.number-self.multiplier,self.answer-10,self.answer-100,self.answer+10,self.answer+100]
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8b(self.problem,self.answer,self.number,self.multiplier,self.digitPlace.keys()[self.randPlace])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ8c(self):
        '''e.g.:
            1000 more than 7824 is __________.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ8c"
        self.CheckAnswerType = 1       

        '''Generating a random number'''
        self.number = randint(1000,6000)
            
        self.digitPlace = {"tens":10,"hundreds":100,}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.multiplier = randint(1,25)
        
        self.number2 = (self.digitPlace[self.digitPlace.keys()[self.randPlace]])*self.multiplier
        
        self.problem = "%d more than %d is ______." %(self.number2,self.number)
        self.answer = self.number2 + self.number
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.multiplier*10+self.number,self.multiplier*100+self.number,self.multiplier+self.number,self.answer+10,self.answer+100]
        
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8c(self.problem,self.answer,self.number,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ8d(self):
        '''e.g.:
            10 less than 5005 is _________.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ8d"
        self.CheckAnswerType = 1       

        '''Generating a random number'''
        self.number = randint(3000,8000)
            
        self.digitPlace = {"tens":10,"hundreds":100,}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.multiplier = randint(1,25)
        
        self.number2 = (self.digitPlace[self.digitPlace.keys()[self.randPlace]])*self.multiplier
        
        self.problem = "%d less than %d is ______." %(self.number2,self.number)
        self.answer = self.number - self.number2

        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number-self.multiplier*10,self.number-self.multiplier,self.answer-10,self.answer-100,self.answer+10,self.answer+100]
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8d(self.problem,self.answer,self.number,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ9(self):
        '''e.g.:
            6 thousands 95 tens 93 ones=______(in figures)'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ9"
        self.CheckAnswerType = 1       
        
        self.thousandDigit = randint(2,9)
        self.hundredDigit = randint(10,99)
        self.onesDigit = randint(10,99)
        
        self.numbers = [self.thousandDigit,self.hundredDigit,self.onesDigit]
        
        self.problem = "%d thousands %d tens %d ones=______(in figures)" % (self.thousandDigit,
                                                                                 self.hundredDigit,self.onesDigit)
        
        self.answer = self.thousandDigit*1000+self.hundredDigit*10+self.onesDigit

        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(int("%d%d%d"%(self.thousandDigit,self.hundredDigit,self.onesDigit)))
        self.wrongAnswers.append(self.thousandDigit*1000+self.hundredDigit+self.onesDigit)
        self.wrongAnswers.append(self.thousandDigit*1000+self.hundredDigit*10+self.onesDigit*10)
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ10(self):
        '''e.g.:
            What number is 400 more than 6782?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ10"
        self.CheckAnswerType = 1       
        
        '''Generating a random number'''
        self.number = randint(1000,6000)
            
        self.digitPlace = {"tens":10,"hundreds":100,}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.multiplier = randint(1,25)
        
        self.number2 = (self.digitPlace[self.digitPlace.keys()[self.randPlace]])*self.multiplier
        
        self.problem = "What number is %d more than %d?" %(self.number2,self.number)
        self.answer = self.number2 + self.number

        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.multiplier*10+self.number,self.multiplier*100+self.number,self.multiplier+self.number,self.answer+10,self.answer+100]
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.number,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ11(self):
        '''e.g.:
        What does the digit 6 in the sum of 237 and 421 stand for? '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ11"
        self.CheckAnswerType = 1       
        
        self.digits = random.sample([4,5,6,7,8,9], 4)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
            
        self.digitPlace = randint(0,len(self.digits)-1)      
        self.randomDigit = self.digits[self.digitPlace]
        
        self.number1 = randint(400,2000)
        self.number2 = int(self.number) - self.number1
                
        self.problem = "What does the digit %s in the sum of %d and %d stand for?" %(self.randomDigit, self.number1, self.number2)
        self.answer = self.randomDigit
        self.multiplier = str(1) + '0'*(4-self.digitPlace-1)
        
        self.answer = self.answer*int(self.multiplier)
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.randomDigit,self.randomDigit*10,self.randomDigit*100,self.randomDigit*1000]
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.number1,self.number2,self.randomDigit,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ12a(self):
        '''e.g.:
        Use all the digits 1, 2, 3 to make the smallest 3-digit number. '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ12a"
        self.CheckAnswerType = 1       
        
        self.digits = random.sample([4,5,6,7,8,9], 3)
        
        self.digits1 = list(self.digits)
        self.digits.sort()
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
                
        self.problem = "Use all the digits %d, %d, %d to make the smallest 3-digit number." %(self.digits1[0],self.digits1[1],self.digits1[2])
        
        self.answer = self.number
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        while len(self.wrongAnswers)<4:
            random.shuffle(self.digits)
            self.wrongAnswer = ''
            for d in self.digits:
                self.wrongAnswer = self.wrongAnswer + str(d)
            if self.wrongAnswer not in self.wrongAnswers:
                self.wrongAnswers.append(self.wrongAnswer)
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12a(self.problem,self.answer,self.digits1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ12b(self):
        '''e.g.:
        Use all the digits 1, 2, 3 to make the greatest 3-digit number. '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ12b"
        self.CheckAnswerType = 1       
        
        self.digits = random.sample([4,5,6,7,8,9], 3)
        
        self.digits1 = list(self.digits)
        self.digits.sort(reverse=True)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
                
        self.problem = "Use all the digits %d, %d, %d to make the greatest 3-digit number." %(self.digits1[0],self.digits1[1],self.digits1[2])
                       
        self.answer = self.number
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        while len(self.wrongAnswers)<4:
            random.shuffle(self.digits)
            self.wrongAnswer = ''
            for d in self.digits:
                self.wrongAnswer = self.wrongAnswer + str(d)
            if self.wrongAnswer not in self.wrongAnswers:
                self.wrongAnswers.append(self.wrongAnswer)
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12b(self.problem,self.answer,self.digits1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ13a(self):
        '''e.g.:
        Use all the digits 1, 2, 3 to make the smallest  3-digit  odd number.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ13a"
        self.CheckAnswerType = 1              
        
        self.flag = randint(1,2)
        if self.flag == 1:
            '''generating 1 odd digit which will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],2)
            self.OddDigits = random.sample([1,3,5,7,9],1)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.EvenDigits.sort()
            self.number = ''
            for d in self.EvenDigits:
                self.number = self.number + str(d)
                    
            self.problem = "Use all the digits %d, %d, %d to make the smallest 3-digit odd number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number+str(self.OddDigits[0])
            
            self.wrongAnswers = []
            while len(self.wrongAnswers)<4:
                random.shuffle(self.digits)
                self.wrongAnswer = ''
                for d in self.digits:
                    self.wrongAnswer = self.wrongAnswer + str(d)
                if self.wrongAnswer not in self.wrongAnswers:
                    self.wrongAnswers.append(self.wrongAnswer)
        else:
            '''generating 2 odd digits, the greater of these will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],1)
            self.OddDigits = random.sample([1,3,5,7,9],2)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.OddDigits.sort()
            if self.OddDigits[0] < self.EvenDigits[0]:
                self.number = str(self.OddDigits[0])+str(self.EvenDigits[0])+str(self.OddDigits[1])
            else:
                self.number = str(self.EvenDigits[0])+str(self.OddDigits[0])+str(self.OddDigits[1])
            
            self.wrongAnswers = []
            while len(self.wrongAnswers)<4:
                random.shuffle(self.digits)
                self.wrongAnswer = ''
                for d in self.digits:
                    self.wrongAnswer = self.wrongAnswer + str(d)
                if self.wrongAnswer not in self.wrongAnswers:
                    self.wrongAnswers.append(self.wrongAnswer)
            
            self.problem = "Use all the digits %d, %d, %d to make the smallest 3-digit odd number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number
        
        self.template = "MCQTypeProblems.html"
               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13a(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ13b(self):
        '''e.g.:
        Use all the digits 1, 2, 3 to make the greatest  3-digit  odd number.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ13b"
        self.CheckAnswerType = 1              
        
        self.flag = randint(1,2)
        if self.flag == 1:
            '''generating 1 odd digit which will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],2)
            self.OddDigits = random.sample([1,3,5,7,9],1)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.EvenDigits.sort(reverse=True)
            self.number = ''
            for d in self.EvenDigits:
                self.number = self.number + str(d)
                    
            self.problem = "Use all the digits %d, %d, %d to make the greatest 3-digit odd number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number+str(self.OddDigits[0])
        else:
            '''generating 2 odd digits, the smaller of these will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],1)
            self.OddDigits = random.sample([1,3,5,7,9],2)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.OddDigits.sort(reverse=True)
            if self.OddDigits[0] > self.EvenDigits[0]:
                self.number = str(self.OddDigits[0])+str(self.EvenDigits[0])+str(self.OddDigits[1])
            else:
                self.number = str(self.EvenDigits[0])+str(self.OddDigits[0])+str(self.OddDigits[1])
            
            self.problem = "Use all the digits %d, %d, %d to make the greatest 3-digit odd number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number

        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        while len(self.wrongAnswers)<4:
            random.shuffle(self.digits)
            self.wrongAnswer = ''
            for d in self.digits:
                self.wrongAnswer = self.wrongAnswer + str(d)
            if self.wrongAnswer not in self.wrongAnswers:
                self.wrongAnswers.append(self.wrongAnswer)
               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13b(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ13c(self):
        '''e.g.:
        Use all the digits 1, 2, 3 to make the smallest  3-digit even number.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ13c"
        self.CheckAnswerType = 1              
        
        self.flag = randint(1,2)
        if self.flag == 1:
            '''generating 1 even digit which will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],1)
            self.OddDigits = random.sample([1,3,5,7,9],2)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.OddDigits.sort()
            self.number = ''
            for d in self.OddDigits:
                self.number = self.number + str(d)
                    
            self.problem = "Use all the digits %d, %d, %d to make the smallest 3-digit even number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number+str(self.EvenDigits[0])
        else:
            '''generating 2 odd digits, the greater of these will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],2)
            self.OddDigits = random.sample([1,3,5,7,9],1)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.EvenDigits.sort()
            if self.EvenDigits[0] < self.OddDigits[0]:
                self.number = str(self.EvenDigits[0])+str(self.OddDigits[0])+str(self.EvenDigits[1])
            else:
                self.number = str(self.OddDigits[0])+str(self.EvenDigits[0])+str(self.EvenDigits[1])
                
            self.problem = "Use all the digits %d, %d, %d to make the smallest 3-digit even number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number

        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        while len(self.wrongAnswers)<4:
            random.shuffle(self.digits)
            self.wrongAnswer = ''
            for d in self.digits:
                self.wrongAnswer = self.wrongAnswer + str(d)
            if self.wrongAnswer not in self.wrongAnswers:
                self.wrongAnswers.append(self.wrongAnswer)
               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13c(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ13d(self):
        '''e.g.:
        Use all the digits 1, 2, 3 to make the greatest 3-digit even number.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ13d"
        self.CheckAnswerType = 1              
        
        self.flag = randint(1,2)
        if self.flag == 1:
            '''generating 1 even digit which will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],1)
            self.OddDigits = random.sample([1,3,5,7,9],2)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.OddDigits.sort(reverse=True)
            self.number = ''
            for d in self.OddDigits:
                self.number = self.number + str(d)
                    
            self.problem = "Use all the digits %d, %d, %d to make the greatest 3-digit even number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number+str(self.EvenDigits[0])
        else:
            '''generating 2 odd digits, the smaller of these will be the last digit'''
            self.EvenDigits = random.sample([2,4,6,8],2)
            self.OddDigits = random.sample([1,3,5,7,9],1)
            
            self.digits = self.EvenDigits + self.OddDigits
            random.shuffle(self.digits)
            
            self.EvenDigits.sort(reverse=True)
            if self.EvenDigits[0] > self.OddDigits[0]:
                self.number = str(self.EvenDigits[0])+str(self.OddDigits[0])+str(self.EvenDigits[1])
            else:
                self.number = str(self.OddDigits[0])+str(self.EvenDigits[0])+str(self.EvenDigits[1])
            
            self.problem = "Use all the digits %d, %d, %d to make the greatest 3-digit even number." %(self.digits[0],self.digits[1],self.digits[2])
            self.answer = self.number

        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        while len(self.wrongAnswers)<4:
            random.shuffle(self.digits)
            self.wrongAnswer = ''
            for d in self.digits:
                self.wrongAnswer = self.wrongAnswer + str(d)
            if self.wrongAnswer not in self.wrongAnswers:
                self.wrongAnswers.append(self.wrongAnswer)
               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13d(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ14a(self):
        '''e.g.:
        I am a 3-digit odd number. I am smaller than 500 but greater than 400. The digit in my tens place is 2 more/less than the digit in my hundreds place. You will find me if you count by fives. What number am I?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ14a"
        self.CheckAnswerType = 1              
        
        self.flag = randint(1,3)
        if self.flag == 1:
            self.SmallerThan = random.randrange(200,500,100)
            self.GreaterThan = self.SmallerThan - 100
            self.hundredDigit = self.GreaterThan / 100
            
            self.TensDigit = randint(5,9)
            self.MoreLessThan = self.TensDigit - self.hundredDigit
                    
            self.problem = "I am a 3-digit odd number. I am smaller than %d but greater than %d. "%(self.SmallerThan, self.GreaterThan)
            self.problem = self.problem + "The digit in my tens place is %d more than the digit in my hundreds place. "%(self.MoreLessThan)
            self.problem = self.problem + "You will find me if you count by fives. What number am I?"
            self.answer = "%d%d5"%(self.hundredDigit,self.TensDigit)
        elif self.flag == 2:
            self.SmallerThan = random.randrange(600,900,100)
            self.GreaterThan = self.SmallerThan - 100
            self.hundredDigit = self.GreaterThan / 100
            
            self.TensDigit = randint(1,4)
            self.MoreLessThan = self.hundredDigit - self.TensDigit
                    
            self.problem = "I am a 3-digit odd number. I am smaller than %d but greater than %d. "%(self.SmallerThan, self.GreaterThan)
            self.problem = self.problem + "The digit in my tens place is %d less than the digit in my hundreds place. "%(self.MoreLessThan)
            self.problem = self.problem + "You will find me if you count by fives. What number am I?"
            self.answer = "%d%d5"%(self.hundredDigit,self.TensDigit)
        elif self.flag == 3:
            self.SmallerThan = random.randrange(200,900,100)
            self.GreaterThan = self.SmallerThan - 100
            self.hundredDigit = self.GreaterThan / 100
            
            self.TensDigit = self.hundredDigit
            self.MoreLessThan = self.hundredDigit - self.TensDigit
                    
            self.problem = "I am a 3-digit odd number. I am smaller than %d but greater than %d. "%(self.SmallerThan, self.GreaterThan)
            self.problem = self.problem + "The digit in my tens place is the same as the digit in my hundreds place. "
            self.problem = self.problem + "You will find me if you count by fives. What number am I?"
            self.answer = "%d%d5"%(self.hundredDigit,self.TensDigit)

        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append("%d%d0"%(self.hundredDigit,self.TensDigit))
        if self.hundredDigit+1<10:
            self.wrongAnswers.append("%d%d5"%(self.hundredDigit+1,self.TensDigit))
        else:
            self.wrongAnswers.append("%d%d5"%(self.hundredDigit-1,self.TensDigit))
        if self.TensDigit+1<10:
            self.wrongAnswers.append("%d%d0"%(self.hundredDigit,self.TensDigit+1))
        else:
            self.wrongAnswers.append("%d%d0"%(self.hundredDigit,self.TensDigit-1))
               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14a(self.problem,self.answer,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ14b(self):
        '''e.g.:
        I am a 3-digit even number. I am smaller than 500 but greater than 400. The digit in my tens place is 2 more/less than the digit in my hundreds place. You will find me if you count by threes. What number am I?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ14b"
        self.CheckAnswerType = 1              
        
        self.flag = randint(1,3)
        if self.flag == 1:
            self.SmallerThan = random.randrange(200,500,100)
            self.GreaterThan = self.SmallerThan - 100
            self.hundredDigit = self.GreaterThan / 100
            
            self.TensDigit = randint(5,9)
            self.MoreLessThan = self.TensDigit - self.hundredDigit
                    
            self.problem = "I am a 3-digit even number. I am smaller than %d but greater than %d. "%(self.SmallerThan, self.GreaterThan)
            self.problem = self.problem + "The digit in my tens place is %d more than the digit in my hundreds place. "%(self.MoreLessThan)
            self.problem = self.problem + "You will find me if you count by threes. What number am I?"
            self.answer = "%d%d6"%(self.hundredDigit,self.TensDigit)
        elif self.flag == 2:
            self.SmallerThan = random.randrange(600,900,100)
            self.GreaterThan = self.SmallerThan - 100
            self.hundredDigit = self.GreaterThan / 100
            
            self.TensDigit = randint(1,4)
            self.MoreLessThan = self.hundredDigit - self.TensDigit
                    
            self.problem = "I am a 3-digit even number. I am smaller than %d but greater than %d. "%(self.SmallerThan, self.GreaterThan)
            self.problem = self.problem + "The digit in my tens place is %d less than the digit in my hundreds place. "%(self.MoreLessThan)
            self.problem = self.problem + "You will find me if you count by threes. What number am I?"
            self.answer = "%d%d6"%(self.hundredDigit,self.TensDigit)
        elif self.flag == 3:
            self.SmallerThan = random.randrange(200,900,100)
            self.GreaterThan = self.SmallerThan - 100
            self.hundredDigit = self.GreaterThan / 100
            
            self.TensDigit = self.hundredDigit
            self.MoreLessThan = self.hundredDigit - self.TensDigit
                    
            self.problem = "I am a 3-digit even number. I am smaller than %d but greater than %d. "%(self.SmallerThan, self.GreaterThan)
            self.problem = self.problem + "The digit in my tens place is the same as the digit in my hundreds place. "
            self.problem = self.problem + "You will find me if you count by threes. What number am I?"
            self.answer = "%d%d6"%(self.hundredDigit,self.TensDigit)

        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append("%d%d3"%(self.hundredDigit,self.TensDigit))
        if self.hundredDigit+1<10:
            self.wrongAnswers.append("%d%d6"%(self.hundredDigit+1,self.TensDigit))
        else:
            self.wrongAnswers.append("%d%d6"%(self.hundredDigit-1,self.TensDigit))
        if self.TensDigit+1<10:
            self.wrongAnswers.append("%d%d8"%(self.hundredDigit,self.TensDigit+1))
        else:
            self.wrongAnswers.append("%d%d8"%(self.hundredDigit,self.TensDigit-1))
               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14b(self.problem,self.answer,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)

    def GenerateProblemTypeMCQ15(self):
        '''e.g.:
        I am a 3-digit even number. I am smaller than 500 but greater than 400. The digit in my tens place is 2 more/less than the digit in my hundreds place. You will find me if you count by threes. What number am I?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.problem_type = "ProblemTypeMCQ15"
        self.CheckAnswerType = 1              
                          
        self.number = randint(2001,8999)

        self.GreaterThan = (self.number / 1000)*1000
        self.SmallerThan = self.GreaterThan + 1000

        
        self.thousandDigit = self.number / 1000
        self.hundredDigit = self.number / 100 - 10*(self.number/1000)
        self.TensDigit = self.number / 10 - 10*(self.number/100)
        self.onesDigit = self.number - 10*(self.number/10)
        
        if self.onesDigit%2 == 0:
            self.EvenOdd = "even"
        else:
            self.EvenOdd = "odd"
                
        self.HundredsPlaceMoreLessThan = self.hundredDigit - self.thousandDigit
        if self.HundredsPlaceMoreLessThan > 0:
            self.HundredsPlaceMoreLessThanFlag = "more than"
        elif self.HundredsPlaceMoreLessThan < 0:
            self.HundredsPlaceMoreLessThanFlag = "less than"
        else:
            self.HundredsPlaceMoreLessThanFlag = "same as"
                
        self.TensPlaceMoreLessThan = self.TensDigit - self.hundredDigit
        if self.TensPlaceMoreLessThan > 0:
            self.TensPlaceMoreLessThanFlag = "more than"
        elif self.TensPlaceMoreLessThan < 0:
            self.TensPlaceMoreLessThanFlag = "less than"
        else:
            self.TensPlaceMoreLessThanFlag = "same as"
                
        self.OnesPlaceMoreLessThan = self.onesDigit - self.TensDigit
        if self.OnesPlaceMoreLessThan > 0:
            self.OnesPlaceMoreLessThanFlag = "more than"
        elif self.OnesPlaceMoreLessThan < 0:
            self.OnesPlaceMoreLessThanFlag = "less than"
        else:
            self.OnesPlaceMoreLessThanFlag = "same as"
            
        self.problem = "I am a 4-digit %s number. I am smaller than %d but greater than %d.<br>"%(self.EvenOdd,self.SmallerThan, self.GreaterThan)
        if self.HundredsPlaceMoreLessThanFlag != "same as":
            self.problem = self.problem + "The digit in my hundreds place is %d %s the digit in my thousands place.<br>"%(abs(self.HundredsPlaceMoreLessThan),self.HundredsPlaceMoreLessThanFlag)
        else:
            self.problem = self.problem + "The digit in my hundreds place is the same as the digit in my thousands place.<br>"
        if self.TensPlaceMoreLessThanFlag != "same as":
            self.problem = self.problem + "The digit in my tens place is %d %s the digit in my hundreds place.<br>"%(abs(self.TensPlaceMoreLessThan),self.TensPlaceMoreLessThanFlag)
        else:
            self.problem = self.problem + "The digit in my tens place is the same as the digit in my hundreds place.<br>"
        if self.HundredsPlaceMoreLessThanFlag != "same as":
            self.problem = self.problem + "The digit in my ones place is %d %s the digit in my tens place.<br>"%(abs(self.OnesPlaceMoreLessThan),self.OnesPlaceMoreLessThanFlag)
        else:
            self.problem = self.problem + "The digit in my ones place is the same as the digit in my tens place.<br>"

        self.problem = self.problem + "<br>What number am I?"
        self.answer = self.number

        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number+10,self.number+100,self.number+100,self.number+1]
               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.HundredsPlaceMoreLessThan,self.TensPlaceMoreLessThan,self.OnesPlaceMoreLessThan,self.EvenOdd)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False                           
        elif CheckAnswer == 2:
            try:
                return str(answer).upper()==str(InputAnswer).upper() or str(answer)[:-1].upper()==str(InputAnswer).upper()
            except ValueError:
                return False                           
            
    def PlaceValueTable1(self,number):
        colorOnes = 'purple'
        colorTens = 'dodgerblue'
        colorHundreds = 'hotpink'
        colorThousands = 'darkorange'
        
        thousands,remHundreds  = divmod(number,1000)
        hundreds,remTens = divmod(remHundreds,100)
        tens,ones = divmod(remTens,10)
        
        placeValueTable = "<br><br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        placeValueTable = placeValueTable + "<tr><td style='background-color:%s;height:35px;width:150px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Thousands</font></td><td style='background-color:%s;height:35px;width:150px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Hundreds</font></td><td style='background-color:%s;height:35px;width:100px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Tens</font></td><td style='background-color:%s;height:35px;width:100px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Ones</font></td></tr>"%(colorThousands,colorHundreds,colorTens,colorOnes)
        placeValueTable = placeValueTable + "<tr><td style='height:40px;border:white solid 1px;'>%d</td><td style='height:40px;border:white solid 1px;'>%d</td><td style='height:40px;border:white solid 1px;'>%d</td><td style='height:40px;border:white solid 1px;'>%d</td></tr>"%(thousands,hundreds,tens,ones)
        placeValueTable = placeValueTable + "</table><br><br>"
        
        return placeValueTable 
    
    def PlaceValueTable2(self,number):
        colorOnes = 'purple'
        colorTens = 'dodgerblue'
        colorHundreds = 'hotpink'
        colorThousands = 'darkorange'
        
        thousands,remHundreds  = divmod(number,1000)
        hundreds,remTens = divmod(remHundreds,100)
        tens,ones = divmod(remTens,10)
        
        placeValueTable = "<br><br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        placeValueTable = placeValueTable + "<tr><td style='background-color:%s;height:35px;width:150px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Thousands</font></td><td style='background-color:%s;height:35px;width:150px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Hundreds</font></td><td style='background-color:%s;height:35px;width:100px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Tens</font></td><td style='background-color:%s;height:35px;width:100px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Ones</font></td></tr>"%(colorThousands,colorHundreds,colorTens,colorOnes)
        placeValueTable = placeValueTable + "<tr><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td></tr>"%(thousands,hundreds,tens,ones)
        placeValueTable = placeValueTable + "<tr><td style='padding:0'><img src='/images/explanation/P3_model_arrow_thousands.png' /></td><td style='padding:0'><img src='/images/explanation/P3_model_arrow_hundreds.png' /></td><td style='padding:0'><img src='/images/explanation/P3_model_arrow_tens.png' /></td><td style='padding:0'><img src='/images/explanation/P3_model_arrow_ones.png' /></td></tr>"
        
        placeValueTable = placeValueTable + "<tr>"
        placeValueTable = placeValueTable + "<td style='height:35px;white-space:nowrap;'>%d thousands<br>or %d</td>"%(thousands,thousands*1000)
        placeValueTable = placeValueTable + "<td style='height:35px;white-space:nowrap;'>%d hundreds<br>or %d</td>"%(hundreds,hundreds*100)
        placeValueTable = placeValueTable + "<td style='height:35px;white-space:nowrap;'>%d tens<br>or %d</td>"%(tens,tens*10)
        placeValueTable = placeValueTable + "<td style='height:35px;white-space:nowrap;'>%d ones<br>or %d</td>"%(ones,ones)
        placeValueTable = placeValueTable + "</tr>"
        placeValueTable = placeValueTable + "</table><br><br>"
        
        return placeValueTable 
