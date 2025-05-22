'''
Created on Aug 03, 2012
Module: P4DALineGraphs
Generates the "Interpreting data in line graphs" problems for Primary 4

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
import simplejson as json
from Problems import PersonName
import logging

class P4DALineGraphs:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemTypeMCQ1a",],2:["ProblemTypeMCQ1b",],3:["ProblemType1c",],
                            4:["ProblemType2a",],5:["ProblemType2b",],6:["ProblemType2c",],7:["ProblemType2d",],
                            8:["ProblemTypeMCQ3a",],9:["ProblemTypeMCQ3b",],10:["ProblemTypeMCQ3c",],11:["ProblemTypeMCQ3d",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemTypeMCQ1a(),],2:[self.GenerateProblemTypeMCQ1b(),],3:[self.GenerateProblemType1c(),],
                                    4:[self.GenerateProblemType2a(),],5:[self.GenerateProblemType2b(),],6:[self.GenerateProblemType2c(),],7:[self.GenerateProblemType2d(),],
                                    8:[self.GenerateProblemTypeMCQ3a(),],9:[self.GenerateProblemTypeMCQ3b(),],10:[self.GenerateProblemTypeMCQ3c(),],11:[self.GenerateProblemTypeMCQ3d(),],
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
        #return self.GenerateProblemTypeMCQ3d()

    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemTypeMCQ1a":self.GenerateProblemTypeMCQ1a(),"ProblemTypeMCQ1b":self.GenerateProblemTypeMCQ1b(),
                            "ProblemType1c":self.GenerateProblemType1c(),"ProblemType2a":self.GenerateProblemType2a(),
                            "ProblemType2b":self.GenerateProblemType2b(),"ProblemType2c":self.GenerateProblemType2c(),
                            "ProblemType2d":self.GenerateProblemType2d(),"ProblemTypeMCQ3a":self.GenerateProblemTypeMCQ3a(),
                            "ProblemTypeMCQ3b":self.GenerateProblemTypeMCQ3b(),"ProblemTypeMCQ3c":self.GenerateProblemTypeMCQ3c(),
                            "ProblemTypeMCQ3d":self.GenerateProblemTypeMCQ3d(),
                            }
        return self.ProblemType[problem_type]
            
    def GenerateProblemTypeMCQ1a(self):
        '''e.g.:
        '''
              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemTypeMCQ1a'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        self.xAxisMax = 24
        self.yAxisMax = 180
        self.xAxisInterval = 4
        self.yAxisInterval = 20
        self.xAxisLabel = "Age(year)"
        self.yAxisLabel = "Height(cm)"
        self.ChartName = self.name+"'s growth in height over time"
        
        self.HeightBirth = random.randrange(40,60,5)
        
        self.Height4 = self.HeightBirth + random.randrange(20,40,5)
        if self.Height4 <=70:
            self.Height4 = 75

        self.Height8 = self.Height4 + random.randrange(20,40,5)
        if self.Height8 <=100:
            self.Height8 = 110
            
        self.Height12 = self.Height8 + random.randrange(10,20,5)
        if self.Height12 <=120:
            self.Height12 = 130
            
        self.Height16 = self.Height12 + 5
        self.Height20 = self.Height16 + 5
        self.Height24 = self.Height20 + random.choice([0,5])
        
        self.heights = [self.HeightBirth,self.Height4,self.Height8,self.Height12,self.Height16,self.Height20,self.Height24]
        
        self.DataPoints = [[0,self.HeightBirth],
                           [4,self.Height4],
                           [8,self.Height8],
                           [12,self.Height12],
                           [16,self.Height16],
                           [20,self.Height20],
                           [24,self.Height24]
                           ]
        
        self.QuestionYear = random.randrange(4,24,4)
        self.answer = self.heights[self.QuestionYear/4]
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+5)
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer-5)
        self.wrongAnswers.append(self.answer-10)
        
        '''json used to pass the list to javascript function'''
        self.DataPoints = json.dumps(self.DataPoints)
        self.xAxisLabel = json.dumps(self.xAxisLabel)
        self.yAxisLabel = json.dumps(self.yAxisLabel)
        self.ChartName = json.dumps(self.ChartName)
        
        self.FunctionCall = "P4DrawLineChart1("+str(self.xAxisMax)+","+str(self.yAxisMax)+","+str(self.xAxisInterval)+","+str(self.yAxisInterval)+","+self.xAxisLabel+","+self.yAxisLabel+","+self.ChartName+","+self.DataPoints+")"
        self.problem = "The following graph shows "+self.name + "'s height from birth to 24 years of age. "
        self.problem = self.problem + "What was "+self.name+"'s height when she was "+str(self.QuestionYear)+" years old?"
               
        self.unit = 'cm'
        
        self.template = "DrawLineGraphs.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def GenerateProblemTypeMCQ1b(self):
        '''e.g.:
        '''
              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemTypeMCQ1b'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        self.xAxisMax = 24
        self.yAxisMax = 180
        self.xAxisInterval = 4
        self.yAxisInterval = 20
        self.xAxisLabel = "Age(year)"
        self.yAxisLabel = "Height(cm)"
        self.ChartName = self.name+"'s growth in height over time"
        
        self.HeightBirth = random.randrange(40,60,10)
        
        self.Height4 = self.HeightBirth + random.randrange(20,40,10)
        if self.Height4 <=70:
            self.Height4 = 80

        self.Height8 = self.Height4 + random.randrange(20,40,10)
        if self.Height8 <=100:
            self.Height8 = 110
            
        self.Height12 = self.Height8 + random.randrange(10,20,10)
        if self.Height12 <=120:
            self.Height12 = 130
            
        self.Height16 = self.Height12 + 10
        self.Height20 = self.Height16 + 10
        self.Height24 = self.Height20
        
        self.heights = [self.HeightBirth,self.Height4,self.Height8,self.Height12,self.Height16,self.Height20,self.Height24]
        
        self.DataPoints = [[0,self.HeightBirth],
                           [4,self.Height4],
                           [8,self.Height8],
                           [12,self.Height12],
                           [16,self.Height16],
                           [20,self.Height20],
                           [24,self.Height24]
                           ]
        
        self.QuestionYear = random.randrange(2,22,4)
        self.answer = (self.heights[self.QuestionYear/4] + self.heights[self.QuestionYear/4+1]) / 2
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+5)
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer-5)
        self.wrongAnswers.append(self.answer-10)
        
        '''json used to pass the list to javascript function'''
        self.DataPoints = json.dumps(self.DataPoints)
        self.xAxisLabel = json.dumps(self.xAxisLabel)
        self.yAxisLabel = json.dumps(self.yAxisLabel)
        self.ChartName = json.dumps(self.ChartName)
        
        self.FunctionCall = "P4DrawLineChart1("+str(self.xAxisMax)+","+str(self.yAxisMax)+","+str(self.xAxisInterval)+","+str(self.yAxisInterval)+","+self.xAxisLabel+","+self.yAxisLabel+","+self.ChartName+","+self.DataPoints+")"
        self.problem = "The following graph shows "+self.name + "'s height from birth to 24 years of age. "
        self.problem = self.problem + "What was "+self.name+"'s height when she was "+str(self.QuestionYear)+" years old?"
               
        self.unit = 'cm'
        
        self.template = "DrawLineGraphs.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def GenerateProblemType1c(self):
        '''e.g.:
        '''
              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemType1c'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        self.xAxisMax = 24
        self.yAxisMax = 180
        self.xAxisInterval = 4
        self.yAxisInterval = 20
        self.xAxisLabel = "Age(year)"
        self.yAxisLabel = "Height(cm)"
        self.ChartName = self.name+"'s growth in height over time"
        
        self.HeightBirth = random.randrange(40,60,10)
        
        self.Height4 = self.HeightBirth + random.randrange(20,40,10)
        if self.Height4 <=70:
            self.Height4 = 80

        self.Height8 = self.Height4 + random.randrange(20,40,10)
        if self.Height8 <=100:
            self.Height8 = 110
            
        self.Height12 = self.Height8 + random.randrange(10,20,10)
        if self.Height12 <=120:
            self.Height12 = 130
            
        self.Height16 = self.Height12 + 10
        self.Height20 = self.Height16 + 10
        self.Height24 = self.Height20
        
        self.heights = [self.HeightBirth,self.Height4,self.Height8,self.Height12,self.Height16,self.Height20,self.Height24]
        
        self.DataPoints = [[0,self.HeightBirth],
                           [4,self.Height4],
                           [8,self.Height8],
                           [12,self.Height12],
                           [16,self.Height16],
                           [20,self.Height20],
                           [24,self.Height24]
                           ]
        
        self.Year1 = random.randrange(2,24,2)
        self.Year2 = random.randrange(2,24,2)
        
        while self.Year1 == self.Year2:
            self.Year2 = random.randrange(2,24,2)
        
        if self.Year1%4==0:
            self.HeightYear1 = self.heights[self.Year1/4]
        else:
            self.HeightYear1 = (self.heights[self.Year1/4] + self.heights[self.Year1/4+1]) / 2
        
        if self.Year2%4==0:
            self.HeightYear2 = self.heights[self.Year2/4]
        else:
            self.HeightYear2 = (self.heights[self.Year2/4] + self.heights[self.Year2/4+1]) / 2
        
        self.answer = abs(self.HeightYear1-self.HeightYear2)
               
        '''json used to pass the list to javascript function'''
        self.DataPoints = json.dumps(self.DataPoints)
        self.xAxisLabel = json.dumps(self.xAxisLabel)
        self.yAxisLabel = json.dumps(self.yAxisLabel)
        self.ChartName = json.dumps(self.ChartName)
        
        self.FunctionCall = "P4DrawLineChart1("+str(self.xAxisMax)+","+str(self.yAxisMax)+","+str(self.xAxisInterval)+","+str(self.yAxisInterval)+","+self.xAxisLabel+","+self.yAxisLabel+","+self.ChartName+","+self.DataPoints+")"
        self.problem = "The following graph shows "+self.name + "'s height from birth to 24 years of age. "
        if self.Year1 > self.Year2:
            self.problem = self.problem + "How many centimeters did she gain from the age of "+str(self.Year2)+" to the age of "+str(self.Year1)+"?"
        else:
            self.problem = self.problem + "How many centimeters did she gain from the age of "+str(self.Year1)+" to the age of "+str(self.Year2)+"?"
               
        self.unit = 'cm'
        
        self.template = "DrawLineGraphsEnterType.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':self.problem_type,
                'grade':self.grade,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,"unit":self.unit,
                'FunctionCall':self.FunctionCall}            

    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation please refer to Problem 1 at <a href='/Learn/Primary-Grade-4/Data-Analysis/Line-Graphs#WP1' target='_blank'><u>Line Graphs</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemType2a(self):
        '''e.g.:
        '''
              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemType2a'
        self.CheckAnswerType = 2
        
        self.xAxis = random.choice([[300,50],[200,20],[600,100],[400,80],[500,100]])
        self.xAxisMax = self.xAxis[0]
        self.xAxisInterval = self.xAxis[1]
        self.yAxisInterval = random.choice([2,4,6,8,10])
        self.yAxisMax = self.yAxisInterval * self.xAxisMax / self.xAxisInterval
        self.xAxisLabel = "Length(cm)"
        self.yAxisLabel = "Price($)"
        self.ChartName = "Price of lace"
              
        self.DataPoints = [[0,0],
                           [self.xAxisMax,self.yAxisMax]
                           ]
               
        '''json used to pass the list to javascript function'''
        self.DataPoints = json.dumps(self.DataPoints)
        self.xAxisLabel = json.dumps(self.xAxisLabel)
        self.yAxisLabel = json.dumps(self.yAxisLabel)
        self.ChartName = json.dumps(self.ChartName)
        
        self.length = random.randrange(self.xAxisInterval/2,self.xAxisMax,self.xAxisInterval/2)
        
        self.FunctionCall = "P4DrawLineChart1("+str(self.xAxisMax)+","+str(self.yAxisMax)+","+str(self.xAxisInterval)+","+str(self.yAxisInterval)+","+self.xAxisLabel+","+self.yAxisLabel+","+self.ChartName+","+self.DataPoints+")"
        self.problem = "The graph below shows the price of different lengths of lace at a shop. "
        self.problem = self.problem + "Find the price of "+str(self.length)+" cm of lace."
        
        self.answer = self.length * self.yAxisInterval / self.xAxisInterval
        
        self.unit = ''
        self.dollar = '$'
        
        self.template = "DrawLineGraphsEnterType.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':self.problem_type,
                'grade':self.grade,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,"unit":self.unit,
                'dollar_unit':self.dollar,'FunctionCall':self.FunctionCall}            
            
    def GenerateProblemType2b(self):
        '''e.g.:
        '''
              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemType2b'
        self.CheckAnswerType = 2
        
        self.name = random.choice(PersonName.GirlName)
        self.xAxis = random.choice([[300,50],[200,20],[600,100],[400,80],[500,100]])
        self.xAxisMax = self.xAxis[0]
        self.xAxisInterval = self.xAxis[1]
        self.yAxisInterval = random.choice([2,4,6,8,10])
        self.yAxisMax = self.yAxisInterval * self.xAxisMax / self.xAxisInterval
        self.xAxisLabel = "Length(cm)"
        self.yAxisLabel = "Price($)"
        self.ChartName = "Price of lace"
              
        self.DataPoints = [[0,0],
                           [self.xAxisMax,self.yAxisMax]
                           ]
               
        '''json used to pass the list to javascript function'''
        self.DataPoints = json.dumps(self.DataPoints)
        self.xAxisLabel = json.dumps(self.xAxisLabel)
        self.yAxisLabel = json.dumps(self.yAxisLabel)
        self.ChartName = json.dumps(self.ChartName)
        
        self.money = random.randrange(self.yAxisInterval/2,self.yAxisMax,self.yAxisInterval/2)
        
        self.FunctionCall = "P4DrawLineChart1("+str(self.xAxisMax)+","+str(self.yAxisMax)+","+str(self.xAxisInterval)+","+str(self.yAxisInterval)+","+self.xAxisLabel+","+self.yAxisLabel+","+self.ChartName+","+self.DataPoints+")"
        self.problem = "The graph below shows the price of different lengths of lace at a shop. "
        self.problem = self.problem + self.name+" paid $"+str(self.money)+" for some lace. How many centimeters of lace did she buy?"
        
        self.answer = self.money * self.xAxisInterval / self.yAxisInterval
        
        self.unit = 'cm'
        self.dollar = ''
        
        self.template = "DrawLineGraphsEnterType.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':self.problem_type,
                'grade':self.grade,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,"unit":self.unit,
                'dollar_unit':self.dollar,'FunctionCall':self.FunctionCall}            
            
    def GenerateProblemType2c(self):
        '''e.g.:
        '''
              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemType2c'
        self.CheckAnswerType = 2
        
        self.names = random.sample(PersonName.PersonName,2)
        self.xAxis = random.choice([[300,50],[200,20],[600,100],[400,80],[500,100]])
        self.xAxisMax = self.xAxis[0]
        self.xAxisInterval = self.xAxis[1]
        self.yAxisInterval = random.choice([2,4,6,8,10])
        self.yAxisMax = self.yAxisInterval * self.xAxisMax / self.xAxisInterval
        self.xAxisLabel = "Length(cm)"
        self.yAxisLabel = "Price($)"
        self.ChartName = "Price of lace"
              
        self.DataPoints = [[0,0],
                           [self.xAxisMax,self.yAxisMax]
                           ]
               
        '''json used to pass the list to javascript function'''
        self.DataPoints = json.dumps(self.DataPoints)
        self.xAxisLabel = json.dumps(self.xAxisLabel)
        self.yAxisLabel = json.dumps(self.yAxisLabel)
        self.ChartName = json.dumps(self.ChartName)
        
        self.length1 = random.randrange(self.xAxisInterval/2,self.xAxisMax,self.xAxisInterval/2)
        self.length2 = random.randrange(self.xAxisInterval/2,self.xAxisMax,self.xAxisInterval/2)
        
        while self.length1==self.length2:
            self.length1 = random.randrange(self.xAxisInterval/2,self.xAxisMax,self.xAxisInterval/2)
        
        self.FunctionCall = "P4DrawLineChart1("+str(self.xAxisMax)+","+str(self.yAxisMax)+","+str(self.xAxisInterval)+","+str(self.yAxisInterval)+","+self.xAxisLabel+","+self.yAxisLabel+","+self.ChartName+","+self.DataPoints+")"
        self.problem = "The graph below shows the price of different lengths of lace at a shop. "
        self.problem = self.problem + self.names[0]+" bought "+str(self.length1)+" cm of lace. "+self.names[1]+" bought "+str(self.length2)+" cm of lace. "
        self.problem = self.problem + "How much did they pay for the lace altogether?"
        
        self.answer = (self.length1+self.length2) * self.yAxisInterval / self.xAxisInterval
        
        self.unit = ''
        self.dollar = '$'
        
        self.template = "DrawLineGraphsEnterType.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':self.problem_type,
                'grade':self.grade,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,"unit":self.unit,
                'dollar_unit':self.dollar,'FunctionCall':self.FunctionCall}            
            
    def GenerateProblemType2d(self):
        '''e.g.:
        '''
              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemType2d'
        self.CheckAnswerType = 2
        
        self.names = random.sample(PersonName.PersonName,2)
        self.xAxis = random.choice([[300,50],[200,20],[600,100],[400,80],[500,100]])
        self.xAxisMax = self.xAxis[0]
        self.xAxisInterval = self.xAxis[1]
        self.yAxisInterval = random.choice([2,4,6,8,10])
        self.yAxisMax = self.yAxisInterval * self.xAxisMax / self.xAxisInterval
        self.xAxisLabel = "Length(cm)"
        self.yAxisLabel = "Price($)"
        self.ChartName = "Price of lace"
              
        self.DataPoints = [[0,0],
                           [self.xAxisMax,self.yAxisMax]
                           ]
               
        '''json used to pass the list to javascript function'''
        self.DataPoints = json.dumps(self.DataPoints)
        self.xAxisLabel = json.dumps(self.xAxisLabel)
        self.yAxisLabel = json.dumps(self.yAxisLabel)
        self.ChartName = json.dumps(self.ChartName)
        
        self.length1 = random.randrange(self.xAxisInterval/2,self.xAxisMax,self.xAxisInterval/2)
        self.cost = self.length1 * self.yAxisInterval / self.xAxisInterval
        if self.cost < 50:
            self.paid = 50
        elif self.cost < 100:
            self.paid = 100
        else:
            self.paid = 500
        
        self.FunctionCall = "P4DrawLineChart1("+str(self.xAxisMax)+","+str(self.yAxisMax)+","+str(self.xAxisInterval)+","+str(self.yAxisInterval)+","+self.xAxisLabel+","+self.yAxisLabel+","+self.ChartName+","+self.DataPoints+")"
        self.problem = "The graph below shows the price of different lengths of lace at a shop. "
        self.problem = self.problem + self.names[0]+" bought "+str(self.length1)+" cm of lace and gave $"+str(self.paid)+" to the cashier. "
        self.problem = self.problem + "How much change must the cashier return to "+self.names[0]+"?"
        
        self.answer = self.paid - self.cost
        
        self.unit = ''
        self.dollar = '$'
        
        self.template = "DrawLineGraphsEnterType.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':self.problem_type,
                'grade':self.grade,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType,"unit":self.unit,
                'dollar_unit':self.dollar,'FunctionCall':self.FunctionCall}            

    def ExplainType2(self,problem,answer,unit,dollar):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "For detailed explanation please refer to Problem 2 at <a href='/Learn/Primary-Grade-4/Data-Analysis/Line-Graphs#WP2' target='_blank'><u>Line Graphs</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemTypeMCQ3a(self):
        '''e.g.:
        '''
              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemTypeMCQ3a'
        self.CheckAnswerType = 1

        self.xAxisInterval = 1
        self.xAxisMax = 7
        self.yAxisInterval = random.randrange(2,20,2)
        self.yAxisMax = randint(8,12) * self.yAxisInterval
        
        
        self.xAxisLabel = "Day"
        self.yAxisLabel = "Cakes sold"
        self.ChartName = "Cakes sold by the bakery"
        self.DayNames = ["","Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        
        self.CakesSold = []
        self.DataPoints = [0,0]
        
        for i in range(7):
            self.cake = random.randrange(self.yAxisInterval/2,self.yAxisMax,self.yAxisInterval/2)
            try:
                if self.cake == min(self.CakesSold) and self.cake!= self.yAxisMax:
                    self.cake = self.cake + self.yAxisInterval/2
            except ValueError:
                pass     
            self.CakesSold.append(self.cake)
            self.DataPoints.append([i+1,self.cake])
       
        
        '''json used to pass the list to javascript function'''
        self.DataPoints = json.dumps(self.DataPoints)
        self.xAxisLabel = json.dumps(self.xAxisLabel)
        self.yAxisLabel = json.dumps(self.yAxisLabel)
        self.ChartName = json.dumps(self.ChartName)
        self.DayNames = json.dumps(self.DayNames)
        
        self.FunctionCall = "P4DrawLineChart2("+str(self.xAxisMax)+","+str(self.yAxisMax)+","+str(self.xAxisInterval)+","+str(self.yAxisInterval)+","+self.xAxisLabel+","+self.yAxisLabel+","+self.ChartName+","+self.DataPoints+","+self.DayNames+")"
        self.problem = "The line graph below shows the number of cakes that a bakery sold last week. "
        self.problem = self.problem + " On which day did it sell least number of cakes?"
        
        self.Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.wrongAnswers = []
                                
        self.answer = self.Days[self.CakesSold.index(min(self.CakesSold))]

        i = 0
        while i < 3:
            self.WrongDay = random.choice(self.Days)
            if self.WrongDay not in self.wrongAnswers and self.WrongDay != self.answer:
                self.wrongAnswers.append(self.WrongDay)
                i = i + 1
        
        self.unit = ''
        self.dollar = ''
        
        self.template = "DrawLineGraphs.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def GenerateProblemTypeMCQ3b(self):
        '''e.g.:
        '''
              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemTypeMCQ3b'
        self.CheckAnswerType = 1

        self.xAxisInterval = 1
        self.xAxisMax = 7
        self.yAxisInterval = random.randrange(2,20,2)
        self.yAxisMax = randint(8,12) * self.yAxisInterval
        
        
        self.xAxisLabel = "Day"
        self.yAxisLabel = "Cakes sold"
        self.ChartName = "Cakes sold by the bakery"
        self.DayNames = ["","Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        
        self.CakesSold = []
        self.DataPoints = [0,0]
        
        for i in range(7):
            self.cake = random.randrange(self.yAxisInterval/2,self.yAxisMax,self.yAxisInterval/2)
            try:
                if self.cake == max(self.CakesSold) and self.cake > self.yAxisInterval/2:
                    self.cake = self.cake - self.yAxisInterval/2
            except ValueError:
                pass     
            self.CakesSold.append(self.cake)
            self.DataPoints.append([i+1,self.cake])
       
        
        '''json used to pass the list to javascript function'''
        self.DataPoints = json.dumps(self.DataPoints)
        self.xAxisLabel = json.dumps(self.xAxisLabel)
        self.yAxisLabel = json.dumps(self.yAxisLabel)
        self.ChartName = json.dumps(self.ChartName)
        self.DayNames = json.dumps(self.DayNames)
        
        self.FunctionCall = "P4DrawLineChart2("+str(self.xAxisMax)+","+str(self.yAxisMax)+","+str(self.xAxisInterval)+","+str(self.yAxisInterval)+","+self.xAxisLabel+","+self.yAxisLabel+","+self.ChartName+","+self.DataPoints+","+self.DayNames+")"
        self.problem = "The line graph below shows the number of cakes that a bakery sold last week. "
        self.problem = self.problem + " On which day did it sell most number of cakes?"
        
        self.Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.wrongAnswers = []
                                
        self.answer = self.Days[self.CakesSold.index(max(self.CakesSold))]

        i = 0
        while i < 3:
            self.WrongDay = random.choice(self.Days)
            if self.WrongDay not in self.wrongAnswers and self.WrongDay != self.answer:
                self.wrongAnswers.append(self.WrongDay)
                i = i + 1
        
        self.unit = ''
        self.dollar = ''
        
        self.template = "DrawLineGraphs.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def GenerateProblemTypeMCQ3c(self):
        '''e.g.:
        '''
              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemTypeMCQ3c'
        self.CheckAnswerType = 1

        self.xAxisInterval = 1
        self.xAxisMax = 7
        self.yAxisInterval = random.randrange(2,20,2)
        self.yAxisMax = randint(8,12) * self.yAxisInterval
        
        
        self.xAxisLabel = "Day"
        self.yAxisLabel = "Cakes sold"
        self.ChartName = "Cakes sold by the bakery"
        self.DayNames = ["","Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        
        self.CakesSold = []
        self.DataPoints = [0,0]
        
        for i in range(7):
            self.cake = random.randrange(self.yAxisInterval/2,self.yAxisMax,self.yAxisInterval/2)  
            self.CakesSold.append(self.cake)
            self.DataPoints.append([i+1,self.cake])
       
        
        '''json used to pass the list to javascript function'''
        self.DataPoints = json.dumps(self.DataPoints)
        self.xAxisLabel = json.dumps(self.xAxisLabel)
        self.yAxisLabel = json.dumps(self.yAxisLabel)
        self.ChartName = json.dumps(self.ChartName)
        self.DayNames = json.dumps(self.DayNames)
        
        self.Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.SellDay = random.choice(self.Days) 
        
        self.FunctionCall = "P4DrawLineChart2("+str(self.xAxisMax)+","+str(self.yAxisMax)+","+str(self.xAxisInterval)+","+str(self.yAxisInterval)+","+self.xAxisLabel+","+self.yAxisLabel+","+self.ChartName+","+self.DataPoints+","+self.DayNames+")"
        self.problem = "The line graph below shows the number of cakes that a bakery sold last week. "
        self.problem = self.problem + " How many cakes did the bakery sell on "+self.SellDay+"?"
        
        self.answer = self.CakesSold[self.Days.index(self.SellDay)]
        self.wrongAnswers = []

        i = 1
        while i < 4:
            self.WrongSell = self.answer + random.choice([-1,1]) * i * self.yAxisInterval/2
            if self.WrongSell not in self.wrongAnswers and self.WrongSell > 0 and self.WrongSell < self.yAxisMax:
                self.wrongAnswers.append(self.WrongSell)
                i = i + 1
        
        self.unit = 'cakes'
        self.dollar = ''
        
        self.template = "DrawLineGraphs.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def GenerateProblemTypeMCQ3d(self):
        '''e.g.:
        '''
              
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemTypeMCQ3d'
        self.CheckAnswerType = 1

        self.xAxisInterval = 1
        self.xAxisMax = 7
        self.yAxisInterval = random.randrange(2,20,2)
        self.yAxisMax = randint(8,12) * self.yAxisInterval
        
        
        self.xAxisLabel = "Day"
        self.yAxisLabel = "Cakes sold"
        self.ChartName = "Cakes sold by the bakery"
        self.DayNames = ["","Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        
        self.CakesSold = []
        self.DataPoints = [0,0]
        
        i = 0
        while i < 7:
            self.cake = random.randrange(self.yAxisInterval/2,self.yAxisMax,self.yAxisInterval/2)
            if self.cake not in self.CakesSold:
                self.CakesSold.append(self.cake)
                self.DataPoints.append([i+1,self.cake])
                i = i + 1       
        
        '''json used to pass the list to javascript function'''
        self.DataPoints = json.dumps(self.DataPoints)
        self.xAxisLabel = json.dumps(self.xAxisLabel)
        self.yAxisLabel = json.dumps(self.yAxisLabel)
        self.ChartName = json.dumps(self.ChartName)
        self.DayNames = json.dumps(self.DayNames)
        
        self.Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.SellNumber = random.choice(self.CakesSold) 
        
        self.FunctionCall = "P4DrawLineChart2("+str(self.xAxisMax)+","+str(self.yAxisMax)+","+str(self.xAxisInterval)+","+str(self.yAxisInterval)+","+self.xAxisLabel+","+self.yAxisLabel+","+self.ChartName+","+self.DataPoints+","+self.DayNames+")"
        self.problem = "The line graph below shows the number of cakes that a bakery sold last week. "
        self.problem = self.problem + " On which day did the bakery sell "+str(self.SellNumber)+" cakes?"
        
        self.answer = self.Days[self.CakesSold.index(self.SellNumber)]
        self.wrongAnswers = []

        i = 0
        while i < 3:
            self.WrongDay = random.choice(self.Days)
            if self.WrongDay not in self.wrongAnswers and self.WrongDay != self.answer:
                self.wrongAnswers.append(self.WrongDay)
                i = i + 1
        
        self.unit = ''
        self.dollar = ''
        
        self.template = "DrawLineGraphs.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType3(self,problem,answer,unit,dollar):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "For detailed explanation please refer to notes at <a href='/Learn/Primary-Grade-4/Data-Analysis/Line-Graphs' target='_blank'><u>Line Graphs</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore,grade,CheckAnswerType,FunctionCall):
        
        self.answer1=''
        self.answer2=''
        self.answer3=''
        self.answer4=''

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
                'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType,
                'FunctionCall':FunctionCall}
                                                                                                                                           
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return str(answer) == str(InputAnswer)
            except ValueError:
                return False
        elif CheckAnswer==2:
            try:
                return float(answer) == float(InputAnswer)
            except ValueError:
                return False            