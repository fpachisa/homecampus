'''
Created on Apr 30, 2012
Module: P6FRWordProblems
Generates the "Fractions Word Problems" problems for Primary 6

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
from Problems import PersonName
from Utils import LcmGcf
import logging

class P6FRWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2a",],3:["ProblemTypeMCQ3b",],
                            4:["ProblemType4",],5:["ProblemTypeMCQ5b","ProblemType5a"],6:["ProblemTypeMCQ6",],
                            7:["ProblemType2b",],8:["ProblemType3a",],9:["ProblemTypeMCQ5c",],
                            }
        
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2a(),],3:[self.GenerateProblemTypeMCQ3b(),],
                                    4:[self.GenerateProblemType4(),],5:[self.GenerateProblemTypeMCQ5b(),self.GenerateProblemType5a(),],6:[self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemType2b(),],8:[self.GenerateProblemType3a(),],9:[self.GenerateProblemTypeMCQ5c(),],
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
        #return self.GenerateProblemTypeMCQ6()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2a":self.GenerateProblemType2a(),
                            "ProblemType2b":self.GenerateProblemType2b(),
                            "ProblemType3a":self.GenerateProblemType3a(),
                            "ProblemTypeMCQ3b":self.GenerateProblemTypeMCQ3b(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5a":self.GenerateProblemType5a(),
                            "ProblemTypeMCQ5b":self.GenerateProblemTypeMCQ5b(),
                            "ProblemTypeMCQ5c":self.GenerateProblemTypeMCQ5c(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g: Nina had 2 m of lace that she used for making bows.
                If she needed 2/7 m of lace for each bow, how many bows did she make?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.numerator = randint(2,7)
        self.denominator = randint(self.numerator+1,9)
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        self.numerator = self.numerator / self.gcf
        self.denominator = self.denominator / self.gcf
        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.name+" had "+str(self.numerator)+" m of lace that she used for making bows.</td></tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'><tr><td>If she needed &nbsp;</td><td><u>"+str(self.numerator)+"</u><br />"+str(self.denominator)+"</td><td>&nbsp; m of lace for each bow, how many bows did she make?</td></tr></table>"
        
        self.answer = self.denominator
        self.unit = "bows"
        self.template = "EnterTypeProblems.html"
        self.CheckAnswerType = 1
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}            

    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Fractions/Dividing-Whole-Number-by-Proper-Fraction#WP1' target='_blank'><u>Dividing Whole Numbers by Proper Fractions</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2a(self):
        '''e.g: Mr. Lee buys 25 kg of decorative shells from a wholesale market.
                He then repacks the shells into small bags of 1/4 kg each.
                a) How many bags does he get?
        '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.numerator = randint(2,7)
        self.denominator = randint(self.numerator+1,9)
        self.number = random.randrange(6*self.numerator,20*self.numerator,self.numerator)
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        self.numerator = self.numerator / self.gcf
        self.denominator = self.denominator / self.gcf
        self.cost = float(random.randrange(150,400,50)) / 100
        
        self.problem = "<table class='FractionsTable'><tr><td>"+self.name+" buys "+str(self.number)+" kg of decorative shells from a wholesale market.</td></tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'><tr><td>He then repacks the shells into small bags of &nbsp;</td><td><u>"+str(self.numerator)+"</u><br />"+str(self.denominator)+"</td><td>&nbsp; kg each.</td></tr></table>"

        self.problem = self.problem + "How many bags does he get?"
        self.answer = self.denominator * self.number / self.numerator
        self.unit = "bags"
        self.dollar = ""
        self.CheckAnswerType = 1
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2a",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":self.dollar}            
        
    def GenerateProblemType2b(self):
        '''e.g: Mr. Lee buys 25 kg of decorative shells from a wholesale market.
                He then repacks the shells into small bags of 1/4 kg each.
                If he sells each bag at $3.50, how much money does he collect from the sale of all bags?
        '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.numerator = randint(2,7)
        self.denominator = randint(self.numerator+1,9)
        self.number = random.randrange(6*self.numerator,20*self.numerator,self.numerator)
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        self.numerator = self.numerator / self.gcf
        self.denominator = self.denominator / self.gcf
        self.cost = float(random.randrange(150,400,50)) / 100
        
        self.problem = "<table class='FractionsTable'><tr><td>"+self.name+" buys "+str(self.number)+" kg of decorative shells from a wholesale market.</td></tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'><tr><td>He then repacks the shells into small bags of &nbsp;</td><td><u>"+str(self.numerator)+"</u><br />"+str(self.denominator)+"</td><td>&nbsp; kg each.</td></tr></table>"
        
        self.problem = self.problem + "If he sells each bag at $"+str(self.cost)+", how much money does he collect from the sale of all bags?"
        self.answer = float(self.denominator * self.number * self.cost)/ self.numerator
        self.unit = ""
        self.dollar = "$"
        self.CheckAnswerType = 2
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2b",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":self.dollar}            

    def ExplainType2(self,problem,answer,unit,dollar):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Fractions/Dividing-Whole-Number-by-Proper-Fraction#WP2' target='_blank'><u>Dividing Whole Numbers by Proper Fractions</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3a(self):
        '''e.g: A chemist fills 5 litres of perfume into bottles that have a capacity of 2/11 litre each.
                a) What is the greatest number of bottles that he can fill completely?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.numerator = randint(2,7)
        self.denominator = randint(self.numerator+1,11)
        self.number = randint(2,10)
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        self.numerator = self.numerator / self.gcf
        self.denominator = self.denominator / self.gcf

        while self.numerator == 1:
            self.numerator = randint(2,7)
            self.denominator = randint(self.numerator+1,11)
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
            self.numerator = self.numerator / self.gcf
            self.denominator = self.denominator / self.gcf
            
        while (self.number*self.denominator)%self.numerator==0:
            self.number = self.number + 1
            logging.info("number = "+str(self.number))
        
        self.problem = "<table class='FractionsTable'><tr><td>A chemist fills "+str(self.number)+" litres of perfume into bottles that have a capacity of &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br />"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td></tr></table>"
        self.problem = self.problem + "litre each. What is the greatest number of bottles that he can fill completely?"

        self.answer = int(self.denominator * self.number / self.numerator)
        self.unit = "bottles"
        self.dollar = ""
        self.CheckAnswerType = 1
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3a(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3a",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":self.dollar}            

    def ExplainType3a(self,problem,answer,unit,dollar):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Fractions/Dividing-Whole-Number-by-Proper-Fraction#WP3' target='_blank'><u>Dividing Whole Numbers by Proper Fractions</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ3b(self):
        '''e.g: A chemist fills 5 litres of perfume into bottles that have a capacity of 2/11 litre each.
                In the end, there is one bottle that is not completely filled. How much perfume does that bottle contain?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.numerator = randint(2,7)
        self.denominator = randint(self.numerator+1,11)
        self.number = randint(2,10)
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        self.numerator = self.numerator / self.gcf
        self.denominator = self.denominator / self.gcf

        while self.numerator == 1:
            self.numerator = randint(2,7)
            self.denominator = randint(self.numerator+1,11)
            self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
            self.numerator = self.numerator / self.gcf
            self.denominator = self.denominator / self.gcf
            
        while (self.number*self.denominator)%self.numerator==0:
            self.number = self.number + 1
        
        self.problem = "<table class='FractionsTable'><tr><td>A chemist fills "+str(self.number)+" litres of perfume into bottles that have a capacity of &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br />"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td></tr></table>"
        self.problem = self.problem + "In the end, there is one bottle that is not completely filled. How much perfume does that bottle contain?<br><br>"
                    
        self.numerator2 = int(self.denominator * self.number / self.numerator) * self.numerator
        
        self.AnswerNumerator = self.number*self.denominator - self.numerator2
        self.AnswerDenominator = self.denominator
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
        self.AnswerNumerator = self.AnswerNumerator/self.gcf
        self.AnswerDenominator = self.AnswerDenominator/self.gcf
        
        self.answer = [0,self.AnswerNumerator,self.AnswerDenominator]
        
        self.problem_type = "ProblemTypeMCQ3b"
        self.template = "FractionMCQTypeProblems.html"
        self.CheckAnswerType = 3
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append([0,self.AnswerNumerator+2,self.AnswerDenominator])
        self.wrongAnswers.append([0,self.AnswerNumerator+1,self.AnswerDenominator])
        self.wrongAnswers.append([0,self.AnswerNumerator+3,self.AnswerDenominator])
        self.wrongAnswers.append([0,self.AnswerNumerator+4,self.AnswerDenominator])
                                      
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ3b(self.problem,self.AnswerNumerator,self.AnswerDenominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def ExplainTypeMCQ3b(self,problem,answer1,answer2):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*(len(str(answer2))/2)+str(answer1)+"&nbsp;"*(len(str(answer2))/2)+"</u><br>"+"&nbsp;"*(len(str(answer1))/2)+str(answer2)+"</td>"            
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Fractions/Dividing-Whole-Number-by-Proper-Fraction#WP3' target='_blank'><u>Dividing Whole Numbers by Proper Fractions</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g: Ray has 5/6 litre of tea in a kettle. He pours 1/12 litre of tea into each of some teacups. How many teacups does he use?s
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.name = random.choice(PersonName.BoyName)
        self.numerator1 = randint(2,7)
        self.denominator1 = randint(self.numerator1+1,11)
        self.numerator2 = 1
        self.denominator2 = randint(2,4) * self.denominator1
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator1, self.denominator1)
        self.numerator1 = self.numerator1 / self.gcf
        self.denominator1 = self.denominator1 / self.gcf
        
        self.problem = "<table class='FractionsTable'><tr><td>"+self.name+" has &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator1))+"</u><br />"+"&nbsp;"*len(str(self.numerator1))+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp; litre of tea in a kettle. He pours &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator2))+"</u><br />"+"&nbsp;"*len(str(self.numerator2))+str(self.denominator2)+"</td><td>&nbsp; litre of tea </td></tr></table>"
        self.problem = self.problem + "into each of some teacups. How many teacups does he use?"

        self.answer = self.numerator1 * self.denominator2 / (self.numerator2 * self.denominator1)
        self.unit = "teacups"
        self.dollar = ""
        self.CheckAnswerType = 1
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":self.dollar}            

    def ExplainType4(self,problem,answer,unit,dollar):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction#WP1' target='_blank'><u>Dividing Proper Fraction by Proper Fraction</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType5a(self):
        '''e.g: Maya had 3/4 kg of rice. She packed the rice into bags of 1/10 kg each.
                a) How many bags did she make?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.name = random.choice(PersonName.GirlName)
        self.numerator1 = randint(4,7)
        self.denominator1 = randint(self.numerator1+1,11)
        self.numerator2 = 1
        self.denominator2 = randint(7,10)
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator1, self.denominator1)
        self.numerator1 = self.numerator1 / self.gcf
        self.denominator1 = self.denominator1 / self.gcf
            
        while (self.numerator1*self.denominator2)%(self.denominator1)==0:
            self.denominator2 = self.denominator2 + 1
        
        self.problem = "<table class='FractionsTable'><tr><td>"+self.name+" had &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator1))+"</u><br />"+"&nbsp;"*len(str(self.numerator1))+str(self.denominator1)+"</td><td>&nbsp; kg of rice." 
        self.problem = self.problem + " She packed the rice into bags of &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator2))+"</u><br />"+"&nbsp;"*len(str(self.numerator2))+str(self.denominator2)+"</td><td>&nbsp; kg each.</td></tr></table>"
        self.problem = self.problem + "How many bags did she make?"

        self.answer = int(self.numerator1*self.denominator2/self.denominator1)
        self.unit = "bags"
        self.dollar = ""
        self.CheckAnswerType = 1
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5a(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5a",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":self.dollar}            

    def ExplainType5a(self,problem,answer,unit,dollar):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction#WP2' target='_blank'><u>Dividing Proper Fraction by Proper Fraction</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ5b(self):
        '''e.g: Maya had 3/4 kg of rice. She packed the rice into bags of 1/10 kg each.
                b) How much rice was left unpacked?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.name = random.choice(PersonName.GirlName)
        self.numerator1 = randint(4,7)
        self.denominator1 = randint(self.numerator1+1,11)
        self.numerator2 = 1
        self.denominator2 = randint(7,10)
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator1, self.denominator1)
        self.numerator1 = self.numerator1 / self.gcf
        self.denominator1 = self.denominator1 / self.gcf
            
        while (self.numerator1*self.denominator2)%(self.denominator1)==0:
            self.denominator2 = self.denominator2 + 1
        
        self.problem = "<table class='FractionsTable'><tr><td>"+self.name+" had &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator1))+"</u><br />"+"&nbsp;"*len(str(self.numerator1))+str(self.denominator1)+"</td><td>&nbsp; kg of rice." 
        self.problem = self.problem + " She packed the rice into bags of &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator2))+"</u><br />"+"&nbsp;"*len(str(self.numerator2))+str(self.denominator2)+"</td><td>&nbsp; kg each.</td></tr></table>"
        self.problem = self.problem + "How much rice was left unpacked?"
                    
        self.numerator3 = int(self.numerator1*self.denominator2/self.denominator1) * self.numerator2
        self.denominator3 = self.denominator2
        
        self.AnswerNumerator = (self.numerator1*self.denominator3-self.numerator3*self.denominator1)
        self.AnswerDenominator = self.denominator1*self.denominator3
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
        self.AnswerNumerator = self.AnswerNumerator/self.gcf
        self.AnswerDenominator = self.AnswerDenominator/self.gcf
        
        self.answer = [0,self.AnswerNumerator,self.AnswerDenominator]
        
        self.problem_type = "ProblemTypeMCQ5b"
        self.template = "FractionMCQTypeProblems.html"
        self.CheckAnswerType = 3
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append([0,self.AnswerNumerator+2,self.AnswerDenominator])
        self.wrongAnswers.append([0,self.AnswerNumerator+1,self.AnswerDenominator])
        self.wrongAnswers.append([0,self.AnswerNumerator+3,self.AnswerDenominator])
        self.wrongAnswers.append([0,self.AnswerNumerator+4,self.AnswerDenominator])
                                      
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ5(self.problem,self.AnswerNumerator,self.AnswerDenominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def GenerateProblemTypeMCQ5c(self):
        '''e.g: Maya had 3/4 kg of rice. She packed the rice into bags of 1/10 kg each.
                How much more rice does she need to make another bag of 1/10 kg?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.name = random.choice(PersonName.GirlName)
        self.numerator1 = randint(4,7)
        self.denominator1 = randint(self.numerator1+1,11)
        self.numerator2 = 1
        self.denominator2 = randint(7,10)
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator1, self.denominator1)
        self.numerator1 = self.numerator1 / self.gcf
        self.denominator1 = self.denominator1 / self.gcf
            
        while (self.numerator1*self.denominator2)%(self.denominator1)==0:
            self.denominator2 = self.denominator2 + 1
        
        self.problem = "<table class='FractionsTable'><tr><td>"+self.name+" had &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator1))+"</u><br />"+"&nbsp;"*len(str(self.numerator1))+str(self.denominator1)+"</td><td>&nbsp; kg of rice." 
        self.problem = self.problem + " She packed the rice into bags of &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator2))+"</u><br />"+"&nbsp;"*len(str(self.numerator2))+str(self.denominator2)+"</td><td>&nbsp; kg each.</td></tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'><tr><td> How much more rice does she need to make another bag of &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator2))+str(self.numerator2)+"&nbsp;"*len(str(self.denominator2))+"</u><br />"+"&nbsp;"*len(str(self.numerator2))+str(self.denominator2)+"</td><td>&nbsp; kg?</td></tr></table>"
                    
        self.numerator3 = int(self.numerator1*self.denominator2/self.denominator1) * self.numerator2
        self.denominator3 = self.denominator2

        self.numerator4 = (self.numerator1*self.denominator3-self.numerator3*self.denominator1)
        self.denominator4 =  self.denominator1*self.denominator3
               
        self.AnswerNumerator = (self.numerator2*self.denominator4-self.numerator4*self.denominator2)
        self.AnswerDenominator = self.denominator2*self.denominator4
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
        self.AnswerNumerator = self.AnswerNumerator/self.gcf
        self.AnswerDenominator = self.AnswerDenominator/self.gcf
        
        self.answer = [0,self.AnswerNumerator,self.AnswerDenominator]
        
        self.problem_type = "ProblemTypeMCQ5c"
        self.template = "FractionMCQTypeProblems.html"
        self.CheckAnswerType = 3
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append([0,self.AnswerNumerator+2,self.AnswerDenominator])
        self.wrongAnswers.append([0,self.AnswerNumerator+1,self.AnswerDenominator])
        self.wrongAnswers.append([0,self.AnswerNumerator+3,self.AnswerDenominator])
        self.wrongAnswers.append([0,self.AnswerNumerator+4,self.AnswerDenominator])         
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ5(self.problem,self.AnswerNumerator,self.AnswerDenominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def ExplainTypeMCQ5(self,problem,answer1,answer2):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*(len(str(answer2))/2)+str(answer1)+"&nbsp;"*(len(str(answer2))/2)+"</u><br>"+"&nbsp;"*(len(str(answer1))/2)+str(answer2)+"</td>"            
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction#WP2' target='_blank'><u>Dividing Proper Fraction by Proper Fraction</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ6(self):
        '''e.g: A rectangular piece of land 1/3 km long has an area of 1/12 km2.
                Find the length of fence needed to border the land.
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.numerator1 = randint(1,5)
        self.denominator1 = randint(self.numerator1+1,9)
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator1,self.denominator1)
        self.numerator1 = self.numerator1 / self.gcf
        self.denominator1 = self.denominator1 / self.gcf
             
        self.numerator2 = randint(1,5)
        self.denominator2 = randint(self.numerator2+1,9)
        
        self.numerator3 = self.numerator1*self.numerator2
        self.denominator3 = self.denominator1*self.denominator2
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator3,self.denominator3)
        self.numerator3 = self.numerator3 / self.gcf
        self.denominator3 = self.denominator3 / self.gcf

        
        self.problem = "<table class='FractionsTable'><tr><td>A rectangular piece of land &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator1))+str(self.numerator1)+"&nbsp;"*len(str(self.denominator1))+"</u><br />"+"&nbsp;"*len(str(self.numerator1))+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp; km long has an area of &nbsp;</td><td><u>"+"&nbsp;"*len(str(self.denominator3))+str(self.numerator3)+"&nbsp;"*len(str(self.denominator3))+"</u><br />"+"&nbsp;"*len(str(self.numerator3))+str(self.denominator3)+"</td><td>&nbsp; km<sup>2</sup>.</td></tr></table>" 
        self.problem = self.problem + "Find the length of fence needed to border the land."
                                   
        self.AnswerNumerator = 2*(self.numerator1*self.denominator2+self.numerator2*self.denominator1)
        self.AnswerDenominator = self.denominator1*self.denominator2
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
        self.AnswerNumerator = self.AnswerNumerator/self.gcf
        self.AnswerDenominator = self.AnswerDenominator/self.gcf
        
        self.answer = [0,self.AnswerNumerator,self.AnswerDenominator]
        
        self.problem_type = "ProblemTypeMCQ6"
        self.template = "FractionMCQTypeProblems.html"
        self.CheckAnswerType = 3
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append([0,self.AnswerNumerator+2,self.AnswerDenominator])
        self.wrongAnswers.append([0,self.AnswerNumerator+1,self.AnswerDenominator])
        if self.AnswerNumerator > 1 and self.AnswerNumerator<=2:
            self.wrongAnswers.append([0,self.AnswerNumerator-1,self.AnswerDenominator])
            self.wrongAnswers.append([0,self.AnswerNumerator+3,self.AnswerDenominator])
        elif self.AnswerNumerator >2:
            self.wrongAnswers.append([0,self.AnswerNumerator-2,self.AnswerDenominator])
            self.wrongAnswers.append([0,self.AnswerNumerator-1,self.AnswerDenominator])
        else:
            self.wrongAnswers.append([0,self.AnswerNumerator+4,self.AnswerDenominator])
            self.wrongAnswers.append([0,self.AnswerNumerator+3,self.AnswerDenominator])            
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ6(self.problem,self.AnswerNumerator,self.AnswerDenominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def ExplainTypeMCQ6(self,problem,answer1,answer2):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        if answer2!=1:
            self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*(len(str(answer2))/2)+str(answer1)+"&nbsp;"*(len(str(answer2))/2)+"</u><br>"+"&nbsp;"*(len(str(answer1))/2)+str(answer2)+"</td>"            
        else:
            self.answer_text = self.answer_text +"<td>"+str(answer1)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction#WP3' target='_blank'><u>Dividing Proper Fraction by Proper Fraction</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,
                    CheckAnswerType,grade,complexity_level,HCScore):
        
        
        '''Removing correct answers from the wrongAnswers list'''
        wrongAnswers = filter(self.removeCorrectAnswer,wrongAnswers)
                             
        '''Randomly selecting 3 wrong answers and adding the correct answer as well'''
        try:
            wrongAnswers = random.sample(wrongAnswers,3)
        except ValueError:
            pass
            
        wrongAnswers.append(answer)
        random.shuffle(wrongAnswers)
        try:
            self.answer1 = wrongAnswers[0]
            self.answer2 = wrongAnswers[1]
            self.answer3 = wrongAnswers[2]
            self.answer4 = wrongAnswers[3]         
        except IndexError:
            pass
        try:
            '''self.value1 = str(self.answer1[0])+"/"+str(self.answer1[1])
            self.value2 = str(self.answer2[0])+"/"+str(self.answer2[1])
            self.value3 = str(self.answer3[0])+"/"+str(self.answer3[1])
            self.value4 = str(self.answer4[0])+"/"+str(self.answer4[1])'''
            self.value1 = self.answer1
            self.value2 = self.answer2
            self.value3 = self.answer3
            self.value4 = self.answer4              
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answerM1':self.answer1[0],'answerN1':self.answer1[1],'answerD1':self.answer1[2],
                'answerM2':self.answer2[0],'answerN2':self.answer2[1],'answerD2':self.answer2[2],
                'answerM3':self.answer3[0],'answerN3':self.answer3[1],'answerD3':self.answer3[2],
                'answerM4':self.answer4[0],'answerN4':self.answer4[1],'answerD4':self.answer4[2],
                'value1':self.value1,'value2':self.value2,'value3':self.value3,'value4':self.value4,
                'explain':explain,'problem_type':problem_type,'CheckAnswerType':CheckAnswerType,'grade':6,
                "complexity_level":complexity_level,"HCScore":HCScore}       

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False
        elif CheckAnswer==2:
            try:
                return float(answer)==float(InputAnswer)
            except ValueError:
                return False
        elif CheckAnswer==3:
            try:
                answer=str(answer)
                return answer==InputAnswer
            except ValueError:
                return False
        elif CheckAnswer==5:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False            