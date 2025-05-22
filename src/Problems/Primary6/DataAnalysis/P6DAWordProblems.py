'''
Created on Apr 21, 2012
Module: P6DAWordProblems
Generates the "Pie Chart Word Problems" problems for Primary 6

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
from Utils import LcmGcf
import string

class P6DAWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1a",],2:["ProblemType1b",],3:["ProblemType1c",],
                            4:["ProblemType2a",],5:["ProblemType2b",],6:["ProblemType2c",],
                            7:["ProblemType3a",],8:["ProblemType3b",],9:["ProblemType3c",],
                            10:["ProblemType1d",],11:["ProblemType1e",],
                            12:["ProblemType2d",],13:["ProblemType2e",],14:["ProblemType2f",],
                            }
        
        self.GenerateProblemType = {1:[self.GenerateProblemType1a(),],2:[self.GenerateProblemType1b(),],3:[self.GenerateProblemType1c(),],
                                    4:[self.GenerateProblemType2a(),],5:[self.GenerateProblemType2b(),],6:[self.GenerateProblemType2c(),],
                                    7:[self.GenerateProblemType3a(),],8:[self.GenerateProblemType3b(),],9:[self.GenerateProblemType3c(),],
                                    10:[self.GenerateProblemType1d(),],11:[self.GenerateProblemType1e(),],
                                    12:[self.GenerateProblemType2d(),],13:[self.GenerateProblemType2e(),],14:[self.GenerateProblemType2f(),],
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
        #return self.GenerateProblemType2a()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1a":self.GenerateProblemType1a(),
                            "ProblemType1b":self.GenerateProblemType1b(),
                            "ProblemType1c":self.GenerateProblemType1c(),
                            "ProblemType1d":self.GenerateProblemType1d(),
                            "ProblemType1e":self.GenerateProblemType1e(),
                            "ProblemType2a":self.GenerateProblemType2a(),
                            "ProblemType2b":self.GenerateProblemType2b(),
                            "ProblemType2c":self.GenerateProblemType2c(),
                            "ProblemType2d":self.GenerateProblemType2d(),
                            "ProblemType2e":self.GenerateProblemType2e(),
                            "ProblemType2f":self.GenerateProblemType2f(),
                            "ProblemType3a":self.GenerateProblemType3a(),
                            "ProblemType3b":self.GenerateProblemType3b(),
                            "ProblemType3c":self.GenerateProblemType3c(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1a(self):
        '''e.g: A community centre organized a racial harmony fair through which it collected a sum of $5880. 
        The pie chart below shows the amount of money collected by the various stalls.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.stalls = ['Souvenir','Games','Food','Drinks']
        random.shuffle(self.stalls)
        
        self.multiplier = randint(60,200)
        self.total = 20 * self.multiplier
        self.MoneyStall0 = 5 * self.multiplier
        self.MoneyStall1 = randint(3,5) * self.multiplier
        self.MoneyStall2 = randint(4,7) * self.multiplier
        self.MoneyStall3 = self.total - self.MoneyStall0 - self.MoneyStall1 - self.MoneyStall2
        
        self.data = [self.MoneyStall0,self.MoneyStall1,self.MoneyStall2,self.MoneyStall3]
        self.FunctionCall = "DrawPieChart1("+str(self.data)+","+str(self.stalls)+")"
        
        self.problem = "A community centre organized a racial harmony fair through which it collected a sum of $"+str(self.total)+"."
        self.problem = self.problem+" The pie chart below shows the amount of money collected by the various stalls.<br><br>"
        self.problem = self.problem + "Find the sum of money collected by the "+self.stalls[0]+" stall."

        self.answer = self.MoneyStall0
        self.unit = ""
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1a",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"$",
                'FunctionCall':self.FunctionCall}            
        
    def GenerateProblemType1b(self):
        '''e.g: What percentage of the total money was collected by the souvenir stall?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.stalls = ['Souvenir','Games','Food','Drinks']
        random.shuffle(self.stalls)
        
        self.multiplier = randint(60,200)
        self.total = 20 * self.multiplier
        self.MoneyStall0 = 5 * self.multiplier
        self.MoneyStall1 = randint(3,5) * self.multiplier
        self.MoneyStall2 = randint(4,7) * self.multiplier
        self.MoneyStall3 = self.total - self.MoneyStall0 - self.MoneyStall1 - self.MoneyStall2
        
        self.data = [self.MoneyStall0,self.MoneyStall1,self.MoneyStall2,self.MoneyStall3]
        self.FunctionCall = "DrawPieChart1("+str(self.data)+","+str(self.stalls)+")"
        
        self.problem = "A community centre organized a racial harmony fair through which it collected a sum of $"+str(self.total)+"."
        self.problem = self.problem+" The pie chart below shows the amount of money collected by the various stalls.<br><br>"
        self.problem = self.problem + "What percentage of the total money was collected by the "+self.stalls[1]+" stall?"

        self.answer = self.MoneyStall1 * 100 / self.total
        self.unit = "%" 
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1b",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':"%"}
        
    def GenerateProblemType1c(self):
        '''e.g: What fraction of the total money was collected by the foods stall?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.stalls = ['Souvenir','Games','Food','Drinks']
        random.shuffle(self.stalls)
        
        self.multiplier = randint(60,200)
        self.total = 20 * self.multiplier
        self.MoneyStall0 = 5 * self.multiplier
        self.MoneyStall1 = randint(3,5) * self.multiplier
        self.MoneyStall2 = randint(4,7) * self.multiplier
        self.MoneyStall3 = self.total - self.MoneyStall0 - self.MoneyStall1 - self.MoneyStall2
        
        self.data = [self.MoneyStall0,self.MoneyStall1,self.MoneyStall2,self.MoneyStall3]
        self.FunctionCall = "DrawPieChart1("+str(self.data)+","+str(self.stalls)+")"
        
        self.problem = "A community centre organized a racial harmony fair through which it collected a sum of $"+str(self.total)+"."
        self.problem = self.problem+" The pie chart below shows the amount of money collected by the various stalls.<br><br>"
        self.problem = self.problem + "What fraction of the total money was collected by the "+self.stalls[3]+" stall?"

        self.numerator = self.MoneyStall3
        self.denominator = self.total
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        self.answer = str(self.numerator/self.gcf)+"/"+str(self.denominator/self.gcf)
        
        self.unit = "" 
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1c",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':self.unit}
        
    def GenerateProblemType1d(self):
        '''e.g: What percentage of the total money was collected by the food and drinks stalls?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.stalls = ['Souvenir','Games','Food','Drinks']
        random.shuffle(self.stalls)
        
        self.multiplier = randint(60,200)
        self.total = 20 * self.multiplier
        self.MoneyStall0 = 5 * self.multiplier
        self.MoneyStall1 = randint(3,5) * self.multiplier
        self.MoneyStall2 = randint(4,7) * self.multiplier
        self.MoneyStall3 = self.total - self.MoneyStall0 - self.MoneyStall1 - self.MoneyStall2
        
        self.data = [self.MoneyStall0,self.MoneyStall1,self.MoneyStall2,self.MoneyStall3]
        self.FunctionCall = "DrawPieChart1("+str(self.data)+","+str(self.stalls)+")"
        
        self.problem = "A community centre organized a racial harmony fair through which it collected a sum of $"+str(self.total)+"."
        self.problem = self.problem+" The pie chart below shows the amount of money collected by the various stalls.<br><br>"
        self.problem = self.problem + "What percentage of the total money was collected by the "+self.stalls[2]+" and "+self.stalls[3]+" stalls?"

        self.answer = (self.MoneyStall2+self.MoneyStall3)*100/self.total
        
        self.unit = "%" 
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1d",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':self.unit}
        
    def GenerateProblemType1e(self):
        '''e.g: What was the ratio of the sum of money collected by the food and drinks stalls to the sum of money collected by the games stall?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.stalls = ['Souvenir','Games','Food','Drinks']
        random.shuffle(self.stalls)
        
        self.multiplier = randint(60,200)
        self.total = 20 * self.multiplier
        self.MoneyStall0 = 5 * self.multiplier
        self.MoneyStall1 = randint(3,5) * self.multiplier
        self.MoneyStall2 = randint(4,7) * self.multiplier
        self.MoneyStall3 = self.total - self.MoneyStall0 - self.MoneyStall1 - self.MoneyStall2
        
        self.data = [self.MoneyStall0,self.MoneyStall1,self.MoneyStall2,self.MoneyStall3]
        self.FunctionCall = "DrawPieChart1("+str(self.data)+","+str(self.stalls)+")"
        
        self.problem = "A community centre organized a racial harmony fair through which it collected a sum of $"+str(self.total)+"."
        self.problem = self.problem+" The pie chart below shows the amount of money collected by the various stalls.<br><br>"
        self.problem = self.problem + "What was the ratio of the sum of money collected by the "+self.stalls[2]+" and "+self.stalls[3]+" stalls to the sum of money collected by the "+self.stalls[0]+" stall?"

        self.numerator = self.MoneyStall2+self.MoneyStall3
        self.denominator = self.MoneyStall0
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        self.answer = str(self.numerator/self.gcf)+":"+str(self.denominator/self.gcf)
        
        self.unit = "" 
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1e",'CheckAnswerType':3,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':self.unit}
                                
    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Data-Analysis/Pie-Chart-Word-Problems#WP1' target='_blank'><u>Pie Charts Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2a(self):
        '''e.g: A clothing merchant has 3840 pieces of clothing of 5 types. The pie chart below represents what fraction of the clothing are of each type. 
            PQ is the diameter of the circle on the pie chart.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.clothes = ['Pants','Skirts','Dresses','T-shirts','Shirts']
        random.shuffle(self.clothes)
        
        self.multiplier = randint(60,200)
        self.total = 20 * self.multiplier
        self.cloth0 = 5 * self.multiplier
        self.cloth1 = randint(2,4) * self.multiplier
        self.cloth2 = 5 * self.multiplier - self.cloth1
        self.cloth3 = randint(3,8) * self.multiplier
        self.cloth4 = 10 * self.multiplier - self.cloth3
        
        self.gcf1 = LcmGcf.LcmGcf().find_gcf(self.cloth1,self.total)
        self.numerator1 = self.cloth1/self.gcf1
        self.denominator1 = self.total/self.gcf1
        
        self.gcf2 = LcmGcf.LcmGcf().find_gcf(self.cloth3,self.total)
        self.numerator2 = self.cloth3/self.gcf2
        self.denominator2 = self.total/self.gcf2
        
        '''order of the data is to give the pie chart same look as pie chart in notes'''
        self.data = [self.cloth0,self.cloth1,self.cloth2,self.cloth3,self.cloth4]
        self.FunctionCall = "DrawPieChart2("+str(self.data)+","+str(self.clothes)+","+str(self.numerator1)+","+str(self.denominator1)+","+str(self.numerator2)+","+str(self.denominator2)+")"
        
        self.problem = "A clothing merchant has "+str(self.total)+" pieces of clothing of 5 types. The pie chart below represents what fraction of the clothing are of each type. "
        self.problem = self.problem + "PQ is the diameter of the circle on the pie chart.<br><br>"
        self.problem = self.problem + "How many "+self.clothes[4]+" does the clothing merchant have?"

        self.answer = self.cloth4
        
        self.unit = self.clothes[4] 
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2a",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':self.unit}
        
    def GenerateProblemType2b(self):
        '''e.g: What fraction of the clothing are dresses?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.clothes = ['Pants','Skirts','Dresses','T-shirts','Shirts']
        random.shuffle(self.clothes)
        
        self.multiplier = randint(60,200)
        self.total = 20 * self.multiplier
        self.cloth0 = 5 * self.multiplier
        self.cloth1 = randint(2,4) * self.multiplier
        self.cloth2 = 5 * self.multiplier - self.cloth1
        self.cloth3 = randint(3,8) * self.multiplier
        self.cloth4 = 10 * self.multiplier - self.cloth3
        
        self.gcf1 = LcmGcf.LcmGcf().find_gcf(self.cloth1,self.total)
        self.numerator1 = self.cloth1/self.gcf1
        self.denominator1 = self.total/self.gcf1
        
        self.gcf2 = LcmGcf.LcmGcf().find_gcf(self.cloth3,self.total)
        self.numerator2 = self.cloth3/self.gcf2
        self.denominator2 = self.total/self.gcf2
        
        '''order of the data is to give the pie chart same look as pie chart in notes'''
        self.data = [self.cloth0,self.cloth1,self.cloth2,self.cloth3,self.cloth4]
        self.FunctionCall = "DrawPieChart2("+str(self.data)+","+str(self.clothes)+","+str(self.numerator1)+","+str(self.denominator1)+","+str(self.numerator2)+","+str(self.denominator2)+")"
        
        self.problem = "A clothing merchant has "+str(self.total)+" pieces of clothing of 5 types. The pie chart below represents what fraction of the clothing are of each type. "
        self.problem = self.problem + "PQ is the diameter of the circle on the pie chart.<br><br>"
        self.problem = self.problem + "What fraction of the clothing are "+self.clothes[2]+"?"

        self.numerator = self.cloth2
        self.denominator = self.total
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        
        self.answer = str(self.numerator/self.gcf)+"/"+str(self.denominator/self.gcf)
        
        self.unit = ""
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2b",'CheckAnswerType':2,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':self.unit}
        
    def GenerateProblemType2c(self):
        '''e.g: How many dresses are there?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.clothes = ['Pants','Skirts','Dresses','T-shirts','Shirts']
        random.shuffle(self.clothes)
        
        self.multiplier = randint(60,200)
        self.total = 20 * self.multiplier
        self.cloth0 = 5 * self.multiplier
        self.cloth1 = randint(2,4) * self.multiplier
        self.cloth2 = 5 * self.multiplier - self.cloth1
        self.cloth3 = randint(3,8) * self.multiplier
        self.cloth4 = 10 * self.multiplier - self.cloth3
        
        self.gcf1 = LcmGcf.LcmGcf().find_gcf(self.cloth1,self.total)
        self.numerator1 = self.cloth1/self.gcf1
        self.denominator1 = self.total/self.gcf1
        
        self.gcf2 = LcmGcf.LcmGcf().find_gcf(self.cloth3,self.total)
        self.numerator2 = self.cloth3/self.gcf2
        self.denominator2 = self.total/self.gcf2
        
        '''order of the data is to give the pie chart same look as pie chart in notes'''
        self.data = [self.cloth0,self.cloth1,self.cloth2,self.cloth3,self.cloth4]
        self.FunctionCall = "DrawPieChart2("+str(self.data)+","+str(self.clothes)+","+str(self.numerator1)+","+str(self.denominator1)+","+str(self.numerator2)+","+str(self.denominator2)+")"
        
        self.problem = "A clothing merchant has "+str(self.total)+" pieces of clothing of 5 types. The pie chart below represents what fraction of the clothing are of each type. "
        self.problem = self.problem + "PQ is the diameter of the circle on the pie chart.<br><br>"
        self.problem = self.problem + "How many "+self.clothes[2]+" are there?"

        self.answer = self.cloth2
        
        self.unit = self.clothes[2]
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2c",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':self.unit}
        
    def GenerateProblemType2d(self):
        '''e.g: How many more dresses are there than skirts?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.clothes = ['Pants','Skirts','Dresses','T-shirts','Shirts']
        random.shuffle(self.clothes)
        
        self.multiplier = randint(60,200)
        self.total = 20 * self.multiplier
        self.cloth0 = 5 * self.multiplier
        self.cloth1 = randint(2,4) * self.multiplier
        self.cloth2 = 5 * self.multiplier - self.cloth1
        self.cloth3 = randint(3,8) * self.multiplier
        self.cloth4 = 10 * self.multiplier - self.cloth3
        
        self.gcf1 = LcmGcf.LcmGcf().find_gcf(self.cloth1,self.total)
        self.numerator1 = self.cloth1/self.gcf1
        self.denominator1 = self.total/self.gcf1
        
        self.gcf2 = LcmGcf.LcmGcf().find_gcf(self.cloth3,self.total)
        self.numerator2 = self.cloth3/self.gcf2
        self.denominator2 = self.total/self.gcf2
        
        '''order of the data is to give the pie chart same look as pie chart in notes'''
        self.data = [self.cloth0,self.cloth1,self.cloth2,self.cloth3,self.cloth4]
        self.FunctionCall = "DrawPieChart2("+str(self.data)+","+str(self.clothes)+","+str(self.numerator1)+","+str(self.denominator1)+","+str(self.numerator2)+","+str(self.denominator2)+")"
        
        self.problem = "A clothing merchant has "+str(self.total)+" pieces of clothing of 5 types. The pie chart below represents what fraction of the clothing are of each type. "
        self.problem = self.problem + "PQ is the diameter of the circle on the pie chart.<br><br>"
        if self.cloth1 > self.cloth2:
            self.problem = self.problem + "How many more "+self.clothes[1]+" are there than "+self.clothes[2]+"?"
            self.answer = self.cloth1 - self.cloth2
        else:
            self.problem = self.problem + "How many more "+self.clothes[2]+" are there than "+self.clothes[1]+"?"
            self.answer = self.cloth2 - self.cloth1
        
        self.unit = ""
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2d",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':self.unit}
        
    def GenerateProblemType2e(self):
        '''e.g: What is the ratio of the number of T-shirts to the number of shirts?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.clothes = ['Pants','Skirts','Dresses','T-shirts','Shirts']
        random.shuffle(self.clothes)
        
        self.multiplier = randint(60,200)
        self.total = 20 * self.multiplier
        self.cloth0 = 5 * self.multiplier
        self.cloth1 = randint(2,4) * self.multiplier
        self.cloth2 = 5 * self.multiplier - self.cloth1
        self.cloth3 = randint(3,8) * self.multiplier
        self.cloth4 = 10 * self.multiplier - self.cloth3
        
        self.gcf1 = LcmGcf.LcmGcf().find_gcf(self.cloth1,self.total)
        self.numerator1 = self.cloth1/self.gcf1
        self.denominator1 = self.total/self.gcf1
        
        self.gcf2 = LcmGcf.LcmGcf().find_gcf(self.cloth3,self.total)
        self.numerator2 = self.cloth3/self.gcf2
        self.denominator2 = self.total/self.gcf2
        
        '''order of the data is to give the pie chart same look as pie chart in notes'''
        self.data = [self.cloth0,self.cloth1,self.cloth2,self.cloth3,self.cloth4]
        self.FunctionCall = "DrawPieChart2("+str(self.data)+","+str(self.clothes)+","+str(self.numerator1)+","+str(self.denominator1)+","+str(self.numerator2)+","+str(self.denominator2)+")"
        
        self.problem = "A clothing merchant has "+str(self.total)+" pieces of clothing of 5 types. The pie chart below represents what fraction of the clothing are of each type. "
        self.problem = self.problem + "PQ is the diameter of the circle on the pie chart.<br><br>"
        self.problem = self.problem + "What is the ratio of the number of "+self.clothes[3]+" to the number of "+self.clothes[4]+"?"
        
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.cloth3, self.cloth4)
        self.answer = str(self.cloth3/self.gcf)+":"+str(self.cloth4/self.gcf)
        self.unit = ""
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2e",'CheckAnswerType':3,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':self.unit}
        
    def GenerateProblemType2f(self):
        '''e.g: How many percent of the clothing are pants and skirts?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.clothes = ['Pants','Skirts','Dresses','T-shirts','Shirts']
        random.shuffle(self.clothes)
        
        self.multiplier = randint(60,200)
        self.total = 20 * self.multiplier
        self.cloth0 = 5 * self.multiplier
        self.cloth1 = randint(2,4) * self.multiplier
        self.cloth2 = 5 * self.multiplier - self.cloth1
        self.cloth3 = randint(3,8) * self.multiplier
        self.cloth4 = 10 * self.multiplier - self.cloth3
        
        self.gcf1 = LcmGcf.LcmGcf().find_gcf(self.cloth1,self.total)
        self.numerator1 = self.cloth1/self.gcf1
        self.denominator1 = self.total/self.gcf1
        
        self.gcf2 = LcmGcf.LcmGcf().find_gcf(self.cloth3,self.total)
        self.numerator2 = self.cloth3/self.gcf2
        self.denominator2 = self.total/self.gcf2
        
        '''order of the data is to give the pie chart same look as pie chart in notes'''
        self.data = [self.cloth0,self.cloth1,self.cloth2,self.cloth3,self.cloth4]
        self.FunctionCall = "DrawPieChart2("+str(self.data)+","+str(self.clothes)+","+str(self.numerator1)+","+str(self.denominator1)+","+str(self.numerator2)+","+str(self.denominator2)+")"
        
        self.problem = "A clothing merchant has "+str(self.total)+" pieces of clothing of 5 types. The pie chart below represents what fraction of the clothing are of each type. "
        self.problem = self.problem + "PQ is the diameter of the circle on the pie chart.<br><br>"
        self.problem = self.problem + "How many percent of the clothing are "+self.clothes[0]+" and "+self.clothes[1]+"?"
        
        self.answer = (self.cloth0+self.cloth1)*100/self.total
        
        self.unit = "%"
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2f",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':self.unit}
                                
    def ExplainType2(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Data-Analysis/Pie-Chart-Word-Problems#WP2' target='_blank'><u>Pie Charts Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3a(self):
        '''e.g: A florist has some roses in 5 different colours. 
        The pie chart below shows what percentage of the roses are in each colour. AB is a diameter of the circle on the pie chart.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
               
        self.multiplier = randint(6,20)
        self.total = 20 * self.multiplier
        self.colours = ["orange","yellow","pink","red","white"]
        random.shuffle(self.colours)
        
        self.colour0 = randint(3,5) * self.multiplier
        self.colour1 = randint(3,4) * self.multiplier
        self.colour2 = 10 * self.multiplier - self.colour0 - self.colour1
        self.colour3 = randint(3,8) * self.multiplier
        self.colour4 = 10 * self.multiplier - self.colour3
        
        self.percent1 = self.colour1*100/self.total
        self.percent2 = self.colour2*100/self.total
        self.percent3 = self.colour3*100/self.total
        
        self.data = [self.colour0,self.colour1,self.colour2,self.colour3,self.colour4]
        self.FunctionCall = "DrawPieChart3("+str(self.data)+","+str(self.colours)+","+str(self.percent1)+","+str(self.percent2)+","+str(self.percent3)+")"
        
        self.problem = "A florist has some roses in 5 different colours. "
        self.problem = self.problem + "The pie chart below shows what percentage of the roses are in each colour. AB is a diameter of the circle on the pie chart.<br><br>"
        self.problem = self.problem + "How many percent of the roses are "+self.colours[0]+"?"
        
        self.answer = self.colour0*100/self.total
        
        self.unit = "%"
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3a",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':self.unit}
        
    def GenerateProblemType3b(self):
        '''e.g: Given that there are 36 yellow roses, how many roses are there altogether?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
               
        self.multiplier = randint(6,20)
        self.total = 20 * self.multiplier
        self.colours = ["orange","yellow","pink","red","white"]
        random.shuffle(self.colours)
        
        self.colour0 = randint(3,5) * self.multiplier
        self.colour1 = randint(3,4) * self.multiplier
        self.colour2 = 10 * self.multiplier - self.colour0 - self.colour1
        self.colour3 = randint(3,8) * self.multiplier
        self.colour4 = 10 * self.multiplier - self.colour3
        
        self.percent1 = self.colour1*100/self.total
        self.percent2 = self.colour2*100/self.total
        self.percent3 = self.colour3*100/self.total
        
        self.data = [self.colour0,self.colour1,self.colour2,self.colour3,self.colour4]
        self.FunctionCall = "DrawPieChart3("+str(self.data)+","+str(self.colours)+","+str(self.percent1)+","+str(self.percent2)+","+str(self.percent3)+")"
        
        self.problem = "A florist has some roses in 5 different colours. "
        self.problem = self.problem + "The pie chart below shows what percentage of the roses are in each colour. AB is a diameter of the circle on the pie chart.<br><br>"
        self.problem = self.problem + "Given that there are "+str(self.colour1)+" "+self.colours[1]+" roses, how many roses are there altogether?"
        
        self.answer = self.total
        
        self.unit = "roses"
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3b",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':self.unit}
        
    def GenerateProblemType3c(self):
        '''e.g: What is the ratio of the number of white roses to the number of red roses?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
               
        self.multiplier = randint(6,20)
        self.total = 20 * self.multiplier
        self.colours = ["orange","yellow","pink","red","white"]
        random.shuffle(self.colours)
        
        self.colour0 = randint(3,5) * self.multiplier
        self.colour1 = randint(3,4) * self.multiplier
        self.colour2 = 10 * self.multiplier - self.colour0 - self.colour1
        self.colour3 = randint(3,8) * self.multiplier
        self.colour4 = 10 * self.multiplier - self.colour3
        
        self.percent1 = self.colour1*100/self.total
        self.percent2 = self.colour2*100/self.total
        self.percent3 = self.colour3*100/self.total
        
        self.data = [self.colour0,self.colour1,self.colour2,self.colour3,self.colour4]
        self.FunctionCall = "DrawPieChart3("+str(self.data)+","+str(self.colours)+","+str(self.percent1)+","+str(self.percent2)+","+str(self.percent3)+")"
        
        self.problem = "A florist has some roses in 5 different colours. "
        self.problem = self.problem + "The pie chart below shows what percentage of the roses are in each colour. AB is a diameter of the circle on the pie chart.<br><br>"
        self.problem = self.problem + "What is the ratio of the number of "+self.colours[4]+" roses to the number of "+self.colours[3]+" roses?"
        
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.colour4, self.colour3)
        
        self.answer = str(self.colour4/self.gcf)+":"+str(self.colour3/self.gcf)
        
        self.unit = "roses"
        self.template = "DrawPieCharts.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3c",'CheckAnswerType':3,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'dollar_unit':"",
                'FunctionCall':self.FunctionCall,'unit':self.unit}
                                
    def ExplainType3(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Data-Analysis/Pie-Chart-Word-Problems#WP3' target='_blank'><u>Pie Charts Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False
        elif CheckAnswer==2:
            try:
                AnswerNumerator = str(answer).partition("/")[0]
                AnswerDenominator = str(answer).partition("/")[2]
                InputAnswer = string.join(InputAnswer.split(),"")
                InputNumerator = str(InputAnswer).partition("/")[0]
                InputDenominator = str(InputAnswer).partition("/")[2]
                return float(AnswerNumerator)/float(AnswerDenominator) == float(InputNumerator)/float(InputDenominator)
            except ValueError:
                return False
        elif CheckAnswer==3:
            try:
                AnswerNumerator = str(answer).partition(":")[0]
                AnswerDenominator = str(answer).partition(":")[2]
                InputAnswer = string.join(InputAnswer.split(),"")
                InputNumerator = str(InputAnswer).partition(":")[0]
                InputDenominator = str(InputAnswer).partition(":")[2]
                return float(AnswerNumerator)/float(AnswerDenominator) == float(InputNumerator)/float(InputDenominator)
            except ValueError:
                return False                               