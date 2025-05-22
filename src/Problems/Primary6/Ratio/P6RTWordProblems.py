'''
Created on Apr 10, 2012

Module: P6RTWordProblems
Generates "Word Problems on Ratio" for Primary 6

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
from Problems import PersonName
from Utils import LcmGcf
import math
import logging

class P6RTWordProblems:
    
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
                      
        self.ProblemType = {1:["ProblemType1","ProblemType2"],2:["ProblemType3",],3:["ProblemType4",],4:["ProblemType5",],
                            5:["ProblemType6",],6:["ProblemType7",],7:["ProblemType8",],8:["ProblemType9",],
                            9:["ProblemType10",],10:["ProblemType11",],11:["ProblemType12",],12:["ProblemType13",],
                            13:["ProblemType14",],14:["ProblemType15",],15:["ProblemType16",],16:["ProblemType17",],
                            17:["ProblemType18",],18:["ProblemType19",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemType2()],
                                    2:[self.GenerateProblemType3(),],3:[self.GenerateProblemType4(),],4:[self.GenerateProblemType5(),],
                                    5:[self.GenerateProblemType6(),],6:[self.GenerateProblemType7(),],7:[self.GenerateProblemType8(),],
                                    8:[self.GenerateProblemType9(),],9:[self.GenerateProblemType10(),],10:[self.GenerateProblemType11(),],
                                    11:[self.GenerateProblemType12(),],12:[self.GenerateProblemType13(),],13:[self.GenerateProblemType14(),],
                                    14:[self.GenerateProblemType15(),],15:[self.GenerateProblemType16(),],16:[self.GenerateProblemType17(),],
                                    17:[self.GenerateProblemType18(),],18:[self.GenerateProblemType19(),],
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
        #return self.GenerateProblemType19()
        
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
                            "ProblemType10":self.GenerateProblemType10(),
                            "ProblemType11":self.GenerateProblemType11(),
                            "ProblemType12":self.GenerateProblemType12(),
                            "ProblemType13":self.GenerateProblemType13(),
                            "ProblemType14":self.GenerateProblemType14(),
                            "ProblemType15":self.GenerateProblemType15(),
                            "ProblemType16":self.GenerateProblemType16(),
                            "ProblemType17":self.GenerateProblemType17(),
                            "ProblemType18":self.GenerateProblemType18(),
                            "ProblemType19":self.GenerateProblemType19(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.NameGender = [[random.choice(PersonName.BoyName),"his"],[random.choice(PersonName.GirlName),"her"]]
        self.animals = random.sample(["chickens","ducks","turkeys","pigs","cows","sheep","horses"],3)
        self.multiplier = randint(3,7)
        
        self.number1 = random.randrange(self.multiplier,100,self.multiplier)
        self.number2 = random.randrange(self.multiplier,100,self.multiplier)
        self.number3 = random.randrange(self.multiplier,100,self.multiplier)
        
        self.NameFlag = randint(0,1)
        
        self.problem = self.NameGender[self.NameFlag][0] + " has "+str(self.number1)+" "+self.animals[0]+", "
        self.problem = self.problem + str(self.number2)+" "+self.animals[1]+" and "
        self.problem = self.problem + str(self.number3)+" "+self.animals[2]+" on "+self.NameGender[self.NameFlag][1]+" farm.<br><br>"
        
        self.flag = randint(1,6)

        if self.flag == 1:
            self.problem = self.problem + "What is the ratio between the number of "+self.animals[0]+" to the number of "+self.animals[1]+"?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.number1, self.number2)
            self.answer = str(self.number1/self.gcf)+":"+str(self.number2/self.gcf)
        elif self.flag == 2:
            self.problem = self.problem + "What is the ratio between the number of "+self.animals[0]+" to the number of "+self.animals[2]+"?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.number1, self.number3)
            self.answer = str(self.number1/self.gcf)+":"+str(self.number3/self.gcf)
        elif self.flag == 3:
            self.problem = self.problem + "What is the ratio between the number of "+self.animals[1]+" to the number of "+self.animals[2]+"?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.number2, self.number3)
            self.answer = str(self.number2/self.gcf)+":"+str(self.number3/self.gcf)
        elif self.flag == 4:
            self.problem = self.problem + "What is the ratio between the number of "+self.animals[1]+" to the number of "+self.animals[0]+"?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.number2, self.number1)
            self.answer = str(self.number2/self.gcf)+":"+str(self.number1/self.gcf)
        elif self.flag == 5:
            self.problem = self.problem + "What is the ratio between the number of "+self.animals[2]+" to the number of "+self.animals[0]+"?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.number3, self.number1)
            self.answer = str(self.number3/self.gcf)+":"+str(self.number1/self.gcf)
        elif self.flag == 6:
            self.problem = self.problem + "What is the ratio between the number of "+self.animals[2]+" to the number of "+self.animals[1]+"?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.number3, self.number2)
            self.answer = str(self.number3/self.gcf)+":"+str(self.number2/self.gcf)

        self.problem = self.problem + "<br><br>(Express the ratio in simplest form)"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType1(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "For detailed explanation read the notes on <a href='/Learn/Primary6/Ratio/Ratio-and-Fraction' target='_blank'>Ratio and Fractions</a>"
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.NameGender = [[random.choice(PersonName.BoyName),"his"],[random.choice(PersonName.GirlName),"her"]]
        self.animals = random.sample(["chickens","ducks","turkeys","pigs","cows","sheep","horses"],3)
        self.multiplier = randint(3,6)
        
        self.number1 = random.randrange(self.multiplier,30,self.multiplier)
        self.number2 = random.randrange(self.multiplier,30,self.multiplier)
        self.number3 = random.randrange(self.multiplier,30,self.multiplier)
        self.total = self.number1 + self.number2 + self.number3
        
        self.NameFlag = randint(0,1)
        
        self.problem = self.NameGender[self.NameFlag][0] + " has "+str(self.number1)+" "+self.animals[0]+", "
        self.problem = self.problem + str(self.number2)+" "+self.animals[1]+" and "
        self.problem = self.problem + str(self.number3)+" "+self.animals[2]+" on "+self.NameGender[self.NameFlag][1]+" farm.<br><br>"
        
        self.flag = randint(1,3)

        if self.flag == 1:
            self.problem = self.problem + "What is the ratio between the number of "+self.animals[0]+" to the total number of animals in the farm?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.number1, self.total)
            self.answer = str(self.number1/self.gcf)+":"+str(self.total/self.gcf)
        elif self.flag == 2:
            self.problem = self.problem + "What is the ratio between the number of "+self.animals[1]+" to the total number of animals in the farm?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.number2, self.total)
            self.answer = str(self.number2/self.gcf)+":"+str(self.total/self.gcf)
        elif self.flag == 3:
            self.problem = self.problem + "What is the ratio between the number of "+self.animals[2]+" to the total number of animals in the farm?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.number3, self.total)
            self.answer = str(self.number3/self.gcf)+":"+str(self.total/self.gcf)
        
        self.problem = self.problem + "<br><br>(Express the ratio in simplest form)"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType2(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "For detailed explanation read the notes on <a href='/Learn/Primary6/Ratio/Ratio-and-Fraction' target='_blank'>Ratio and Fractions</a>"
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.NameGender = [[random.choice(PersonName.BoyName),"his"],[random.choice(PersonName.GirlName),"her"]]
        self.animals = random.sample(["chickens","ducks","turkeys","pigs","cows","sheep","horses"],3)
        self.multiplier = randint(3,6)
        
        self.number1 = random.randrange(self.multiplier,30,self.multiplier)
        self.number2 = random.randrange(self.multiplier,30,self.multiplier)
        self.number3 = random.randrange(self.multiplier,30,self.multiplier)
        self.total = self.number1 + self.number2 + self.number3
        
        self.NameFlag = randint(0,1)
        
        self.problem = self.NameGender[self.NameFlag][0] + " has "+str(self.number1)+" "+self.animals[0]+", "
        self.problem = self.problem + str(self.number2)+" "+self.animals[1]+" and "
        self.problem = self.problem + str(self.number3)+" "+self.animals[2]+" on "+self.NameGender[self.NameFlag][1]+" farm.<br><br>"
        
        self.flag = randint(1,3)

        if self.flag == 1:
            self.problem = self.problem + "What fraction of the animals on the farm are "+self.animals[0]+"?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.number1, self.total)
            self.answer = str(self.number1/self.gcf)+"/"+str(self.total/self.gcf)
        elif self.flag == 2:
            self.problem = self.problem + "What fraction of the animals on the farm are "+self.animals[1]+"?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.number2, self.total)
            self.answer = str(self.number2/self.gcf)+"/"+str(self.total/self.gcf)
        elif self.flag == 3:
            self.problem = self.problem + "What fraction of the animals on the farm are "+self.animals[2]+"?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.number3, self.total)
            self.answer = str(self.number3/self.gcf)+"/"+str(self.total/self.gcf)
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Express the fraction in simplest form and type answer as: If&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType3(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "For detailed explanation read the notes on <a href='/Learn/Primary6/Ratio/Ratio-and-Fraction' target='_blank'>Ratio and Fractions</a>"
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.names = random.sample(PersonName.PersonName,2)
        
        self.mixed = randint(1,2)
        self.numerator = randint(1,7)
        self.denominator = randint(self.numerator+1,8)
        
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        self.numerator = self.numerator/self.gcf 
        self.denominator = self.denominator/self.gcf
                
        self.problem = "A certain departmental store rewards shoppers with points for shopping."
        
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.names[0]+" has </td>"
        self.problem = self.problem + "<td>"+str(self.mixed)+"</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator)+"&nbsp;</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp;as many points as "+self.names[1]+".</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.unit = ""
        self.flag = randint(1,6)
        if self.flag == 1:
            self.problem = self.problem + "What is the ratio of "+self.names[0]+"'s points to "+self.names[1]+"'s points?"
            self.AnswerNumerator = self.mixed * self.denominator + self.numerator
            self.AnswerDenominator = self.denominator
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
            self.answer = str(self.AnswerNumerator/self.gcf)+":"+str(self.AnswerDenominator/self.gcf)
            self.type = "ratio"
        elif self.flag == 2:
            self.problem = self.problem + "What is the ratio of "+self.names[1]+"'s points to "+self.names[0]+"'s points?"
            self.AnswerNumerator = self.denominator
            self.AnswerDenominator = self.mixed * self.denominator + self.numerator
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
            self.answer = str(self.AnswerNumerator/self.gcf)+":"+str(self.AnswerDenominator/self.gcf)
            self.type = "ratio"
        elif self.flag == 3:
            self.problem = self.problem + "What is the ratio of "+self.names[0]+"'s points to their total points?"
            self.AnswerNumerator = self.mixed * self.denominator + self.numerator
            self.AnswerDenominator = self.denominator + self.AnswerNumerator
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
            self.answer = str(self.AnswerNumerator/self.gcf)+":"+str(self.AnswerDenominator/self.gcf)
            self.type = "ratio"
        elif self.flag == 4:
            self.problem = self.problem + "Express "+self.names[1]+"'s points as a fraction of their total points."
            self.AnswerNumerator = self.denominator
            self.AnswerDenominator = self.mixed * self.denominator + self.numerator + self.denominator
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
            self.answer = str(self.AnswerNumerator/self.gcf)+"/"+str(self.AnswerDenominator/self.gcf)
            self.type = "fraction"
        elif self.flag == 5:
            self.problem = self.problem + "Express "+self.names[1]+"'s points as a fraction of "+self.names[0]+"'s points."
            self.AnswerNumerator = self.denominator
            self.AnswerDenominator = self.mixed * self.denominator + self.numerator
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
            self.answer = str(self.AnswerNumerator/self.gcf)+"/"+str(self.AnswerDenominator/self.gcf)
            self.type = "fraction"
        elif self.flag == 6:
            self.total = random.randrange(self.mixed * self.denominator + self.numerator + self.denominator,100,self.mixed * self.denominator + self.numerator + self.denominator)
            self.problem = self.problem + "If they have a total of "+str(self.total)+" points, how many points has "+self.names[0]+"?"
            self.answer = str(self.total*(self.denominator*self.mixed+self.numerator)/(self.denominator*self.mixed+self.numerator+self.denominator))
            self.type = "whole"
            self.unit = "points"
                                            
        if self.type == "ratio":
            self.problem = self.problem + "<br><br><font style='font-size:0.8em;color:black'>(Express the ratio in simplest form)</font>"
        elif self.type == "fraction":
            self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
            self.problem = self.problem + "<tr><td>(Express the fraction in simplest form and type answer as: If&nbsp;</td>"
            self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
            self.problem = self.problem + "<td>&nbsp;then type as 1/2)</td>"
            self.problem = self.problem + "</tr></table>"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType4(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Ratio/Ratio-and-Fraction#WP1' target='_blank'><u>Ratio and Fractions</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.NameGender = [[random.choice(PersonName.BoyName),"he"],[random.choice(PersonName.GirlName),"she"]]
        self.NameFlag = randint(0,1)
        self.name = self.NameGender[self.NameFlag][0]
        self.gender = self.NameGender[self.NameFlag][1]
        self.drinks = random.sample(["lemonade","cider","apple juice","orange juice",],2)
        
        self.mixed = randint(1,2)
        self.numerator1 = randint(1,4)
        self.denominator1 = randint(self.numerator1+1,5)
        
        self.denominator2 = self.denominator1
        self.numerator2 = randint(1,self.denominator2-1)
        
        self.gcf1 = LcmGcf.LcmGcf().find_gcf(self.numerator1, self.denominator1)
        self.numerator1 = self.numerator1/self.gcf1 
        self.denominator1 = self.denominator1/self.gcf1

        self.gcf2 = LcmGcf.LcmGcf().find_gcf(self.numerator2, self.denominator2)
        self.numerator2 = self.numerator2/self.gcf2 
        self.denominator2 = self.denominator2/self.gcf2
                               
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.name+" has </td>"
        self.problem = self.problem + "<td>"+str(self.mixed)+"</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp;litres of "+self.drinks[0]+" and </td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td>&nbsp;litre of "+self.drinks[1]+".</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.unit = ""
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = self.problem + "Express the quantity of "+self.drinks[1]+" as a fraction of the quantity of "+self.drinks[0]+"."
            self.AnswerNumerator = self.numerator2 * self.denominator1
            self.AnswerDenominator = (self.mixed * self.denominator1 + self.numerator1) * self.denominator2
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
            self.answer = str(self.AnswerNumerator/self.gcf)+"/"+str(self.AnswerDenominator/self.gcf)
            self.type = "fraction"
        elif self.flag == 2:
            self.problem = self.problem + "What is the ratio of the quantity of "+self.drinks[0]+" to the total quantity of beverages that "+self.name+" has?"
            self.AnswerNumerator = (self.mixed * self.denominator1 + self.numerator1) * self.denominator2
            self.AnswerDenominator = self.numerator2 * self.denominator1
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
            self.answer = str(self.AnswerNumerator/self.gcf)+":"+str(self.AnswerDenominator/self.gcf)
            self.type = "ratio"
                                            
        if self.type == "ratio":
            self.problem = self.problem + "<br><br><font style='font-size:0.8em;color:black'>(Express the ratio in simplest form)</font>"
        elif self.type == "fraction":
            self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
            self.problem = self.problem + "<tr><td>(Express the fraction in simplest form and type answer as: If&nbsp;</td>"
            self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
            self.problem = self.problem + "<td>&nbsp;then type as 1/2)</td>"
            self.problem = self.problem + "</tr></table>"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType5(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Ratio/Ratio-and-Fraction#WP2' target='_blank'><u>Ratio and Fractions</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.NameGender = [[random.choice(PersonName.BoyName),"his","he"],[random.choice(PersonName.GirlName),"her","she"]]
        self.NameFlag = randint(0,1)
        self.name = self.NameGender[self.NameFlag][0]
        self.gender1 = self.NameGender[self.NameFlag][1]
        self.gender2 = self.NameGender[self.NameFlag][2]
        
        self.numerator = randint(2,5)
        self.denominator = randint(self.numerator+1,10)        

        self.problem = self.name+" adds fertilizer to "+self.gender1+" flower pots which are all of the same size. "+self.gender2.capitalize()+" uses "+str(self.numerator)+" tablespoons of fertilizer for every "+str(self.denominator)+" flower pots.<br><br>"        
        self.unit = ""
        self.flag = randint(1,3)
        if self.flag == 1:
            self.problem = self.problem + "Express the number of tablepoons of fertilizer as a fraction of the number of flower pots in the simplest form."
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
            self.AnswerNumerator = self.numerator / self.gcf
            self.AnswerDenominator = self.denominator / self.gcf
            self.answer = str(self.AnswerNumerator)+"/"+str(self.AnswerDenominator)
            self.type = "fraction"
        elif self.flag == 2:
            self.TotalPots = random.randrange(self.denominator,30,self.denominator)
            self.problem = self.problem + "If "+self.gender2+" has "+str(self.TotalPots)+" flower pots, how many tablespoons of fertilizer does "+self.gender2+" need?"
            self.answer = str(self.numerator*self.TotalPots/self.denominator)
            self.type = "whole"
            self.unit = "tablespoons of fertilizer"
        elif self.flag == 3:
            self.TotalPots = random.randrange(self.denominator,30,self.denominator)
            self.fertilizer = self.numerator*self.TotalPots/self.denominator
            while self.numerator == self.fertilizer:
                self.TotalPots = random.randrange(self.denominator,30,self.denominator)
                self.fertilizer = self.numerator*self.TotalPots/self.denominator
            self.problem = self.problem + "How many flower pots are needed if "+str(self.fertilizer)+" tablespoons of fertilizer is used?"
            self.answer = str(self.TotalPots)
            self.type = "whole"
            self.unit = "flower pots"
                                                        
        if self.type == "ratio":
            self.problem = self.problem + "<br><br><font style='font-size:0.8em;color:black'>(Express the ratio in simplest form)</font>"
        elif self.type == "fraction":
            self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
            self.problem = self.problem + "<tr><td>(Express the fraction in simplest form and type answer as: If&nbsp;</td>"
            self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
            self.problem = self.problem + "<td>&nbsp;then type as 1/2)</td>"
            self.problem = self.problem + "</tr></table>"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType6(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Ratio/Equivalent-Fraction-and-Ratio#WP1' target='_blank'><u>Ratio and Fractions</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.NameGender = [[random.choice(PersonName.BoyName),"he"],[random.choice(PersonName.GirlName),"she"]]
        self.NameFlag = randint(0,1)
        self.name = self.NameGender[self.NameFlag][0]
        self.gender1 = self.NameGender[self.NameFlag][1]
        
        self.numerator = randint(2,14)
        self.denominator = randint(3,7) * self.numerator        

        self.problem = self.name+" is making a pattern with "+str(self.numerator)+" green tiles for every "+str(self.denominator)+" blue tiles.<br><br>"        
        self.unit = ""
        self.flag = randint(1,5)
        if self.flag == 1:
            self.problem = self.problem + "Find the ratio of the number of green tiles to the number of blue tiles in the simplest form."
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
            self.AnswerNumerator = self.numerator / self.gcf
            self.AnswerDenominator = self.denominator / self.gcf
            self.answer = str(self.AnswerNumerator)+":"+str(self.AnswerDenominator)
            self.type = ""
        elif self.flag == 2:
            self.problem = self.problem + "Find the ratio of the number of blue tiles to the number of green tiles."
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
            self.AnswerNumerator = self.denominator / self.gcf
            self.AnswerDenominator = self.numerator / self.gcf
            self.answer = str(self.AnswerNumerator)+":"+str(self.AnswerDenominator)
            self.type = "ratio"
        elif self.flag == 3:
            self.GreenTiles = randint(3,7) * self.numerator
            self.problem = self.problem + "If "+self.gender1+" uses "+str(self.GreenTiles)+" green tiles, how many blue tiles does "+self.gender1+" use?"
            self.answer = str(self.denominator*self.GreenTiles/self.numerator)
            self.type = ""
            self.unit = "blue tiles"   
        elif self.flag == 4:
            self.GreenTiles = randint(3,7) * self.numerator
            self.BlueTiles = self.GreenTiles * self.denominator / self.numerator
            self.TotalTiles = self.GreenTiles + self.BlueTiles
            self.problem = self.problem + "If "+self.gender1+" uses a total of "+str(self.TotalTiles)+" tiles, how many of them are blue?"
            self.answer = str(self.BlueTiles)
            self.type = ""
            self.unit = "blue tiles"            
        elif self.flag == 5:
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
            self.SimpleRatio1 = self.numerator / self.gcf
            self.SimpleRatio2 = self.denominator / self.gcf
            self.SimpleRatio3 = randint(2,4)
            self.GreenTiles = randint(3,7) * self.numerator
            self.BlueTiles = self.GreenTiles * self.denominator / self.numerator
            self.RedTiles = self.SimpleRatio3 * self.GreenTiles
            self.TotalTiles = self.GreenTiles + self.BlueTiles + self.RedTiles
            self.problem = self.problem + self.gender1.capitalize()+" adds red tiles to the pattern so the ratio of the number of green tiles to the number of blue tiles to the number of red tiles is "+str(self.SimpleRatio1)+":"+str(self.SimpleRatio2)+":"+str(self.SimpleRatio3)+"."
            self.problem = self.problem + " If "+self.gender1+" uses "+str(self.TotalTiles)+" tiles altogether, how many of them are red?"
            self.answer = str(self.RedTiles)
            self.type = ""
            self.unit = "red tiles"
                                                                    
        if self.type == "ratio":
            self.problem = self.problem + "<br><br><font style='font-size:0.8em;color:black'>(Express the ratio in simplest form)</font>"
        elif self.type == "fraction":
            self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
            self.problem = self.problem + "<tr><td>(Express the fraction in simplest form and type answer as: If&nbsp;</td>"
            self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
            self.problem = self.problem + "<td>&nbsp;then type as 1/2)</td>"
            self.problem = self.problem + "</tr></table>"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType7(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Ratio/Equivalent-Fraction-and-Ratio#WP2' target='_blank'><u>Ratio and Fractions</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8(self):
        '''The difference between the capacities of a jar and a bottle is 300 ml. 
            If the capacities of the bottle and the jar are in the ratio 3 : 5, what is the maximum volume of water in ml that they can hold together?
        '''
        self.complexity_level = "medium"
        self.HCScore = 5        
                
        self.numerator = randint(2,4)
        self.diff = randint(2,4)
        self.denominator = self.numerator + self.diff        
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        
        self.numerator = self.numerator/self.gcf
        self.denominator = self.denominator/self.gcf
        self.SimpleDiff = self.denominator - self.numerator
        
        self.CapacityDiff = self.SimpleDiff * random.randrange(10,100,10)
        
        self.problem = "The difference between the capacities of a jar and a bottle is "+str(self.CapacityDiff)+" ml. "
        self.problem = self.problem + "If the capacities of the bottle and the jar are in the ratio "+str(self.numerator)+" : "+str(self.denominator)
        self.problem = self.problem + ", what is the maximum volume of water in ml that they can hold together?"         
        self.unit = "ml"
        
        self.answer = str((self.numerator+self.denominator)*self.CapacityDiff/self.SimpleDiff)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType8(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Ratio/Word-Problems#WP1' target='_blank'><u>Ratio -- Word Problems</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType9(self):
        '''The ratio of the breadth of a rectangle to its perimeter is 1 : 8. Find the area of the rectangle if its length is 45 cm.
        '''
        self.complexity_level = "medium"
        self.HCScore = 5        
                
        self.LengthUnit = randint(2,5)
        self.perimeter = 2*(1+self.LengthUnit)
        
        self.length = random.randrange(self.LengthUnit*5,50,self.LengthUnit)
        
        self.problem = "The ratio of the breadth of a rectangle to its perimeter is 1 : "+str(self.perimeter)+".<br><br>"
        self.problem = self.problem + "Find the area of the rectangle if its length is "+str(self.length)+" cm."
        self.unit = "cm<sup>2</sup>"
        
        self.answer = str(self.length*self.length/self.LengthUnit)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType9",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType9(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Ratio/Word-Problems#WP2' target='_blank'><u>Ratio -- Word Problems</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType10(self):
        '''Sally had $200 at first. She spent a sum of money on a dress, a necklace and a ring in the ratio 7 : 4 : 5. 
        If she spent $108 on the jewellery, how much money had she left?
        '''
        self.complexity_level = "medium"
        self.HCScore = 5        
                
        self.name = random.choice(PersonName.GirlName)
        
        self.ratios = random.sample([1,2,3,4,5,6,7,8,9],3)
        
        self.dress = self.ratios[0]
        self.necklace = self.ratios[1]
        self.ring = self.ratios[2]
        
        self.multiplier = randint(10,20)
        self.initial = int(math.ceil((float(self.dress+self.necklace+self.ring)*self.multiplier)/100)*100)
        
        self.problem = self.name+" had $"+str(self.initial)+" at first. She spent a sum of money on a dress, a necklace and a ring in the ratio "+str(self.dress)+" : "+str(self.necklace)+" : "+str(self.ring)+"."
        self.problem = self.problem + " If she spent $"+str((self.necklace+self.ring)*self.multiplier)+" on the jewellery, how much money had she left?"
        
        self.dollar_unit = "$"
        
        self.answer = str(self.initial-(self.necklace+self.ring+self.dress)*self.multiplier)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType10",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"dollar_unit":self.dollar_unit}

    def ExplainType10(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>$"+str(answer)
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Ratio/Word-Problems#WP3' target='_blank'><u>Ratio -- Word Problems</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType11(self):
        '''The lengths of 3 poles are in the ratio 4 : 5 : 10. The shortest pole is 48 cm shorter than the longest pole. 
        What is the length of the poles altogether?
        '''
        self.complexity_level = "medium"
        self.HCScore = 5        
                       
        self.ratios = random.sample([1,2,3,4,5,6,7,8,9],3)
        
        self.ratios.sort()
        
        self.multiplier = randint(10,20)
        
        self.problem = "The lengths of 3 poles are in the ratio "+str(self.ratios[0])+" : "+str(self.ratios[1])+" : "+str(self.ratios[2])+". "
        self.problem = self.problem + "The shortest pole is "+str((self.ratios[2]-self.ratios[0])*self.multiplier)+" cm shorter than the longest pole. "
        self.problem = self.problem + "What is the length of the poles altogether?"
        
        self.unit = "cm"
        
        self.answer = str((self.ratios[0]+self.ratios[1]+self.ratios[2])*self.multiplier)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType11",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType11(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 4 at <a href='/Learn/Primary6/Ratio/Word-Problems#WP4' target='_blank'><u>Ratio -- Word Problems</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType12(self):
        '''Pam travelled 1/11 of the distance of her journey by car while the rest by bus and train in the ratio 1 : 4. 
            If she travelled 532 km more by train than by car, how far did she travel?
        '''
        self.complexity_level = "difficult"
        self.HCScore = 7        

        self.NameGender = [[random.choice(PersonName.BoyName),"his","he"],[random.choice(PersonName.GirlName),"her","she"]]
        self.NameFlag = randint(0,1)
        self.name = self.NameGender[self.NameFlag][0]
        self.gender1 = self.NameGender[self.NameFlag][1]
        self.gender2 = self.NameGender[self.NameFlag][2]
        
        self.ratios = [[11,1,4,random.randrange(7*20,600,7)],[9,1,3,random.randrange(5*30,600,5)],[7,1,2,random.randrange(3*40,600,3)]]
        self.ratios = random.choice(self.ratios)

        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.name+" travelled &nbsp;</td><td style='text-align:center'><u>&nbsp;1&nbsp;</u><br />"+str(self.ratios[0])+"</td><td>&nbsp; of the distance of "+self.gender1+" journey by car while the rest</td></tr></table>"
        self.problem = self.problem + "by bus and train in the ratio "
        self.problem = self.problem + str(self.ratios[1])+" : "+str(self.ratios[2])+". "
        self.problem = self.problem + "If "+self.gender2+" travelled "+str(self.ratios[3])+" km more by train than by car, how far did "+self.gender2+" travel?"
        
        self.unit = "km"
        
        self.answer = str(self.ratios[3]*self.ratios[0]/(self.ratios[2]*2-1))
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType12",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType12(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 5 at <a href='/Learn/Primary6/Ratio/Word-Problems#WP5' target='_blank'><u>Ratio -- Word Problems</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType13(self):
        '''A pet parrot shop has 322 parrots that are coloured either green or blue or yellow. 
        The ratio of the number of green parrots to the number of blue parrots is 13 : 4.
        The ratio of the number of blue parrots to the number of yellow parrots is 2 : 3.
        '''
        self.complexity_level = "medium"
        self.HCScore = 5


        self.green = random.choice([5,7,9,11,13])
        self.ratios = random.sample([2,3,4],2)
        self.multiplier = randint(2,3)
        self.blue = self.ratios[0] * self.multiplier
        self.yellow = self.ratios[1] * self.multiplier
        self.TotalUnit = self.green + self.blue + self.yellow
        self.total = random.randrange(self.TotalUnit*10,400,self.TotalUnit)

        self.problem = "A pet parrot shop has "+str(self.total)+" parrots that are coloured either green or blue or yellow.<br>"
        self.problem = self.problem + "The ratio of the number of green parrots to the number of blue parrots is "+str(self.green)+" : "+str(self.blue)+".<br>"
        self.problem = self.problem + "The ratio of the number of blue parrots to the number of yellow parrots is "+str(self.blue/self.multiplier)+" : "+str(self.yellow/self.multiplier)+".<br><br>"
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.unit = ""
            self.problem = self.problem + "Find the ratio of the number of green parrots to the number of blue parrots to the number of yellow parrots."
            self.answer = str(self.green)+":"+str(self.blue)+":"+str(self.yellow)
        else:
            self.colour = random.choice(["green","blue","yellow"])
            self.unit = self.colour+" parrots"
            self.problem = self.problem + "Find the number of "+self.colour+" parrots."
            if self.colour == "green":
                self.answer = str(self.green*self.total/(self.TotalUnit))
            elif self.colour == "blue":
                self.answer = str(self.blue*self.total/(self.TotalUnit))
            if self.colour == "yellow":
                self.answer = str(self.yellow*self.total/(self.TotalUnit))
                    
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType13",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType13(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 6 at <a href='/Learn/Primary6/Ratio/Word-Problems#WP6' target='_blank'><u>Ratio -- Word Problems</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType14(self):
        '''In a school, for every 5 children born in January there were 3 born in February and for every 2 children born in February there were 5 born in March.
        '''
        self.complexity_level = "medium"
        self.HCScore = 5

        self.ratios = random.sample([2,3,5],2)
        self.jan = self.ratios[0]
        self.feb1 = self.ratios[1]
        self.ratios = random.sample([2,3,5],2)
        self.feb2 = self.ratios[0]
        self.march = self.ratios[1]
        
        self.lcm = LcmGcf.LcmGcf().find_lcm(self.feb1, self.feb2)
        
        self.TotalUnit = self.jan*self.lcm/self.feb1 + self.lcm + self.march*self.lcm/self.feb2
        
        self.total = random.randrange(self.TotalUnit*10,1000,self.TotalUnit)

        self.problem = "In a school, for every "+str(self.jan)+" children born in January there were "+str(self.feb1)+" born in February and for every "+str(self.feb2)+" children born in February there were "+str(self.march)+" born in March.<br><br>"
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.unit = ""
            self.problem = self.problem + "What is the ratio of the number of children born in January to the number of children born in March?(in simplest form)"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.jan*self.lcm/self.feb1,self.march*self.lcm/self.feb2)
            self.answer = str(self.jan*self.lcm/(self.feb1*self.gcf))+":"+str(self.march*self.lcm/(self.feb2*self.gcf))
        else:
            self.unit = ""
            self.month = random.choice(["January","February","March"])            
            if self.month == "January":
                self.problem = self.problem + "How many children were born in the three months altogether if "+str(self.total*(self.jan*self.lcm/self.feb1)/self.TotalUnit)+" of them were born in January?"
            elif self.month == "February":
                self.problem = self.problem + "How many children were born in the three months altogether if "+str(self.total*(self.lcm)/self.TotalUnit)+" of them were born in February?"
            if self.month == "March":
                self.problem = self.problem + "How many children were born in the three months altogether if "+str(self.total*(self.march*self.lcm/self.feb2)/self.TotalUnit)+" of them were born in March?"
            self.answer = self.total
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType14",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType14(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 7 at <a href='/Learn/Primary6/Ratio/Word-Problems#WP7' target='_blank'><u>Ratio -- Word Problems</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType15(self):
        '''Rayan received twice as much pocket money as Falaq. 
        After Rayan spent $5 on animal cards, the ratio of Rayan's amount to that of Falaq's became 3 : 2. 
        Find the amount of pocket money that Falaq received.
        '''
        self.complexity_level = "medium"
        self.HCScore = 5

        self.names = random.sample(PersonName.PersonName,2)
        
        self.amount1 = random.randrange(10,100,10)
        self.flag = randint(1,2)
        if self.flag == 1:
            self.times = "twice"
            self.amount2 = 2*self.amount1
            self.spent = self.amount2 / 10
        else:
            self.times = "thrice"
            self.amount2 = 3*self.amount1
            self.spent = self.amount2 / 2        
        
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.amount1,self.amount2-self.spent)
        self.ratio1 = (self.amount2-self.spent)/self.gcf
        self.ratio2 = self.amount1/self.gcf

        self.problem = self.names[0]+" received "+self.times+" as much pocket money as "+self.names[1]+".<br><br>"
        self.problem = self.problem + "After "+self.names[0]+" spent $"+str(self.spent)+" on animal cards, the ratio of "+self.names[0]+"'s amount to that of "+self.names[1]+"'s became "+str(self.ratio1)+" : "+str(self.ratio2)+".<br><br>"
        self.problem = self.problem + "Find the amount of pocket money that "+self.names[1]+" received." 
        
        self.answer = self.amount1
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType15",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"dollar_unit":"$"}

    def ExplainType15(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>$"+str(answer)
        self.solution_text = "For detailed explanation refer to Word Problem 8 at <a href='/Learn/Primary6/Ratio/Word-Problems#WP8' target='_blank'><u>Ratio -- Word Problems</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType16(self):
        '''The ratio of Grace's mass to Laura's mass was 7 : 5 at first. 
        Then, Laura fell sick and lost 1/10 of her mass. The new differnce between their body masses was 25 kg.
        '''
        self.complexity_level = "medium"
        self.HCScore = 5

        self.names = random.sample(PersonName.GirlName,2)

        self.ratios = random.sample([3,4,5,6,7,8,9],2)
        self.ratios.sort()        
        self.heavy = self.ratios[1]
        self.light = self.ratios[0]
        self.multiplier = randint(2,5)       
        self.HeavyWeight = 2 * self.heavy * self.multiplier
        self.LightWeight = 2 * self.light * self.multiplier
        self.loss = 2 * self.light
        self.diff = self.HeavyWeight - self.LightWeight * (self.loss-1)/self.loss
        
        self.problem = "The ratio of "+self.names[0]+"'s mass to "+self.names[1]+"'s mass was "+str(self.heavy)+" : "+str(self.light)+" at first. Then, "+self.names[1]
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td> fell sick and lost &nbsp;</td><td style='text-align=center'><u>"+"&nbsp;"*len(str(self.loss))+"1"+"&nbsp;"*len(str(self.loss))+"</u><br />&nbsp;"+str(self.loss)+"</td><td>&nbsp; of her mass. The new difference between their body</td></tr></table>"
        self.problem = self.problem + "masses was "+str(self.diff)+" kg.<br><br>" 
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = self.problem + "Find "+self.names[0]+"'s mass."
            self.answer = str(self.HeavyWeight)
            self.unit = "kg"
        elif self.flag == 2:
            self.problem = self.problem + "What is the new ratio of "+self.names[0]+"'s mass to "+self.names[1]+"'s mass?"
            self.FinalLightWeight = self.LightWeight * (self.loss-1)/self.loss
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.FinalLightWeight, self.HeavyWeight)
            self.answer = str(self.HeavyWeight/self.gcf)+":"+str(self.FinalLightWeight/self.gcf)
            self.unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType16(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType16",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType16(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 9 at <a href='/Learn/Primary6/Ratio/Word-Problems#WP9' target='_blank'><u>Ratio -- Word Problems</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType17(self):
        '''Abby and Nina share a sum of money in the ratio 2 : 3. Then, Nina gives a sixth of her share to Abby.
        '''
        self.complexity_level = "medium"
        self.HCScore = 5

        self.name1 = random.choice(PersonName.GirlName)
        self.name2 = random.choice(PersonName.BoyName)
        
        self.ratios = random.sample([3,4,5,6,7,8,9],2)
        self.ratios.sort()
        
        self.more = self.ratios[1]
        self.less = self.ratios[0]
        self.multiplier = randint(10,100)
        
        self.MoreMoney = 2 * self.more * self.multiplier
        self.LessMoney = 2 * self.less * self.multiplier
        
        self.gave = self.more * 2
        
        self.FinalLessMoney = self.LessMoney + self.MoreMoney/self.gave
        
        self.problem = self.name2+" and "+self.name1+" share a sum of money in the ratio "+str(self.less)+" : "+str(self.more)+"."
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td> Then, "+self.name1+" gives &nbsp;</td><td style='text-align=center'><u>"+"&nbsp;"*len(str(self.gave))+"1"+"&nbsp;"*len(str(self.gave))+"</u><br />&nbsp;"+str(self.gave)+"</td><td>&nbsp; of her share to "+self.name2+".</td></tr></table>"
        self.problem = self.problem + "If "+self.name2+" now has $"+str(self.FinalLessMoney)+", how much money had he at first?" 
        
        self.answer = str(self.LessMoney)
        
        self.unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType17(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType17",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":"$"}

    def ExplainType17(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>$"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 10 at <a href='/Learn/Primary6/Ratio/Word-Problems#WP10' target='_blank'><u>Ratio -- Word Problems</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType18(self):
        '''The ratio of the number of laptops to the number of printers in an electronics store was 2 : 5 at first. 
        After a shipment of 240 new laptops arrived at the store, there were twice as many laptops as printers.
        '''
        self.complexity_level = "medium"
        self.HCScore = 5

        self.ratios = random.sample([2,3,4,5,6,7],2)
        self.ratios.sort()
        self.LaptopRatio = self.ratios[0]
        self.PrinterRatio = self.ratios[1]

        self.multiplier = random.randrange(10,40,10)
        self.InitialLaptop = self.LaptopRatio * self.multiplier
        self.InitialPrinter = self.PrinterRatio * self.multiplier
        
        self.TimesFlag = randint(0,1)
        self.times = [[2,"twice"],[3,"thrice"]]
        self.NewLaptop = self.InitialPrinter*self.times[self.TimesFlag][0] - self.InitialLaptop
        
        self.problem = "The ratio of the number of laptops to the number of printers in an electronics store was "+str(self.LaptopRatio)+" : "+str(self.PrinterRatio)+" at first.<br><br>"
        self.problem = self.problem + "After a shipment of "+str(self.NewLaptop)+" new laptops arrived at the store, there were "+self.times[self.TimesFlag][1]+" as many laptops as printers.<br><br>"

        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = self.problem + "Find the number of printers in the electronics store?"
            self.answer = str(self.InitialPrinter)
            self.unit = "Printers"
        elif self.flag == 2:
            self.NewPrinter = random.randrange(30,200,10)
            self.problem = self.problem + "If a shipment of "+str(self.NewPrinter)+" new printers arrived at the store, what would the ratio of the number of laptops to the number of printers now be?"
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.InitialLaptop+self.NewLaptop, self.InitialPrinter+self.NewPrinter)
            self.answer = str((self.InitialLaptop+self.NewLaptop)/self.gcf)+":"+str((self.InitialPrinter+self.NewPrinter)/self.gcf)
            self.unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType18(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType18",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType18(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 11 at <a href='/Learn/Primary6/Ratio/Word-Problems#WP11' target='_blank'><u>Ratio -- Word Problems</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType19(self):
        '''Roy, Danny and Henry had a collection of hats. 
        The ratio of the number of hats that Roy had to the number of hats that Danny had to the number of hats that Henry had was 4 : 5 : 6. Then, Henry gave 1/4 of his hats to Roy.
        '''
        self.complexity_level = "difficult"
        self.HCScore = 7

        self.names = random.sample(PersonName.BoyName,3)
        self.ratios = random.sample([2,3,4,6],2)
        self.ratio1 = self.ratios[0]
        self.ratio2 = random.choice([5,7])
        self.ratio3 = self.ratios[1]
        
        self.lcm = LcmGcf.LcmGcf().find_lcm(self.ratio1,self.ratio3)
        
        self.NewRatio1 = self.ratio1*self.lcm/self.ratio3 + self.lcm/self.ratio1
        self.NewRatio2 = self.ratio2*self.lcm/self.ratio3
        self.NewRatio3 = self.ratio3*self.lcm/self.ratio3 - self.lcm/self.ratio1
        
        self.hats1 = random.randrange(self.NewRatio1*3,self.NewRatio1*10,self.NewRatio1)
        self.hats2 = (self.hats1/self.NewRatio1) * self.NewRatio2
        
        self.problem = self.names[0]+ ", "+self.names[1]+" and "+self.names[2]+" had a collection of hats. The ratio of the number of hats that "+self.names[0]+" had to the number of hats that "+self.names[1]+" had to the number of" 
        self.problem = self.problem + " hats that "+self.names[2]+" had was "+str(self.ratio1)+" : "+str(self.ratio2)+" : "+str(self.ratio3)+"."
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td> Then, "+self.names[2]+" gave &nbsp;</td><td><u>1</u><br />"+str(self.ratio1)+"</td><td>&nbsp; of his hats to "+self.names[0]+".</td></tr></table>"

        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = self.problem + "What is the new ratio of the number of "+self.names[0]+"'s hats to that of "+self.names[1]+"'s to that of "+self.names[2]+"'s?"
            self.answer = str(self.NewRatio1)+":"+str(self.NewRatio2)+":"+str(self.NewRatio3)
            self.unit = ""
        elif self.flag == 2:
            self.problem = self.problem + "If "+self.names[0]+" now has "+str(self.hats1)+" hats, how many hats has "+self.names[1]+"?"
            self.answer = self.hats2
            self.unit = "hats"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType19(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType19",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def ExplainType19(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 12 at <a href='/Learn/Primary6/Ratio/Word-Problems#WP12' target='_blank'><u>Ratio -- Word Problems</u></a> page."
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
                                                              
    def checkAnswer(self,template,answer,AnswerInput,CheckType):
        if CheckType==1:
            try:
                logging.info("input = "+str(AnswerInput))
                return (str(answer)==string.join(AnswerInput.split(),""))
            except ValueError:
                return False
        elif CheckType==2:
            try:
                return (float(answer)==float(AnswerInput))
            except ValueError:
                return False                          