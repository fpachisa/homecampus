'''
Created on Jul 26, 2012
Module: P4DATablesBarGraphs
Generates the "Interpreting data in tables and bar graphs" problems for Primary 4

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

class P4DATablesBarGraphs:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemTypeMCQ1a",],2:["ProblemTypeMCQ1b",],3:["ProblemTypeMCQ1c",],
                            4:["ProblemTypeMCQ2a",],5:["ProblemTypeMCQ2b",],6:["ProblemTypeMCQ2c",],7:["ProblemTypeMCQ2d",],
                            8:["ProblemTypeMCQ3a",],9:["ProblemTypeMCQ3b",],10:["ProblemTypeMCQ3c",],11:["ProblemTypeMCQ3d",],12:["ProblemTypeMCQ3e",],13:["ProblemTypeMCQ3f",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemTypeMCQ1a(),],2:[self.GenerateProblemTypeMCQ1b(),],3:[self.GenerateProblemTypeMCQ1c(),],
                                    4:[self.GenerateProblemTypeMCQ2a(),],5:[self.GenerateProblemTypeMCQ2b(),],6:[self.GenerateProblemTypeMCQ2c(),],7:[self.GenerateProblemTypeMCQ2d(),],
                                    8:[self.GenerateProblemTypeMCQ3a(),],9:[self.GenerateProblemTypeMCQ3b(),],10:[self.GenerateProblemTypeMCQ3c(),],11:[self.GenerateProblemTypeMCQ3d(),],
                                    12:[self.GenerateProblemTypeMCQ3e(),],13:[self.GenerateProblemTypeMCQ3f(),],
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
        #return self.GenerateProblemTypeMCQ2b()

    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemTypeMCQ1a":self.GenerateProblemTypeMCQ1a(),"ProblemTypeMCQ1b":self.GenerateProblemTypeMCQ1b(),
                            "ProblemTypeMCQ1c":self.GenerateProblemTypeMCQ1c(),"ProblemTypeMCQ2a":self.GenerateProblemTypeMCQ2a(),
                            "ProblemTypeMCQ2b":self.GenerateProblemTypeMCQ2b(),"ProblemTypeMCQ2c":self.GenerateProblemTypeMCQ2c(),
                            "ProblemTypeMCQ2d":self.GenerateProblemTypeMCQ2d(),"ProblemTypeMCQ3a":self.GenerateProblemTypeMCQ3a(),
                            "ProblemTypeMCQ3b":self.GenerateProblemTypeMCQ3b(),"ProblemTypeMCQ3c":self.GenerateProblemTypeMCQ3c(),
                            "ProblemTypeMCQ3d":self.GenerateProblemTypeMCQ3d(),"ProblemTypeMCQ3e":self.GenerateProblemTypeMCQ3e(),
                            "ProblemTypeMCQ3f":self.GenerateProblemTypeMCQ3f(),
                            }
        return self.ProblemType[problem_type]
            
    def GenerateProblemTypeMCQ1a(self):
        '''e.g.:
        '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"]
        self.problem_type = 'ProblemTypeMCQ1a'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = random.choice([10,15,20])
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 most common flower'''
        for _i in range(self.Bars):
            self.height = randint(self.Interval,self.MaxNumber)
            try:
                if self.height == max(self.heights):
                    self.height = self.height - 1
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Rose","Tulip","Lily","Orchid","Forget-me-not"]
        random.shuffle(self.BarNames)
        self.YAxisLabel = ["Number of Flowers"]
        self.XAxisLabel = ["Kind of Flowers"]
        
        self.answer = self.BarNames[self.BarHeights.index(max(self.BarHeights))]
        self.wrongAnswers = []
        for i in range(len(self.BarNames)):
            if self.BarNames[i]!=self.answer:
                self.wrongAnswers.append(self.BarNames[i])
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        
        self.FunctionCall = "P4DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+")"
        self.problem = self.name + " made a bouquet using the number and types of flowers as represented in the bar chart below. "
        self.problem = self.problem + "Which was the most common flower in the bouquet?"
        
        
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

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
        self.colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"]
        self.problem_type = 'ProblemTypeMCQ1b'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = random.choice([10,15,20])
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 most common flower'''
        for _i in range(self.Bars):
            self.height = randint(self.Interval,self.MaxNumber)
            try:
                if self.height == min(self.heights) and self.height!= self.MaxNumber:
                    self.height = self.height + 1
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Rose","Tulip","Lily","Orchid","Forget-me-not"]
        random.shuffle(self.BarNames)
        self.YAxisLabel = ["Number of Flowers"]
        self.XAxisLabel = ["Kind of Flowers"]
        
        self.answer = self.BarNames[self.BarHeights.index(min(self.BarHeights))]
        self.wrongAnswers = []
        for i in range(len(self.BarNames)):
            if self.BarNames[i]!=self.answer:
                self.wrongAnswers.append(self.BarNames[i])
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        
        self.FunctionCall = "P4DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+")"
        self.problem = self.name + " made a bouquet using the number and types of flowers as represented in the bar chart below. "
        self.problem = self.problem + "Which was the least common flower in the bouquet?"
        
        
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def GenerateProblemTypeMCQ1c(self):
        '''e.g.:
        '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"]
        self.problem_type = 'ProblemTypeMCQ1c'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = random.choice([10,15,20])
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        self.total = 0
        '''making sure that there is only 1 most common flower'''
        for _i in range(self.Bars):
            self.height = randint(self.Interval,self.MaxNumber)
            try:
                if self.height == max(self.heights):
                    self.height = self.height - 1
            except ValueError:
                pass
            self.total = self.total + self.height
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Rose","Tulip","Lily","Orchid","Forget-me-not"]
        random.shuffle(self.BarNames)
        self.YAxisLabel = ["Number of Flowers"]
        self.XAxisLabel = ["Kind of Flowers"]
        
        self.answer = self.total
        self.wrongAnswers = []

        self.wrongAnswers.append(self.answer + 1)
        self.wrongAnswers.append(self.answer - 1)
        self.wrongAnswers.append(self.answer + 2)
        self.wrongAnswers.append(self.answer - 2)
                
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        
        self.FunctionCall = "P4DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+")"
        self.problem = self.name + " made a bouquet using the number and types of flowers as represented in the bar chart below. "
        self.problem = self.problem + "How many flowers had the bouquet?"       
        
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation please refer to Notes at <a href='/Learn/Primary-Grade-4/Data-Analysis/Tables-and-Bar-Graphs' target='_blank'><u>Tables and Bar Graphs</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemTypeMCQ2a(self):
        '''e.g.:
        '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"]
        self.problem_type = 'ProblemTypeMCQ2a'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = random.choice([10,15,20,25,30])
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        self.total = 0
        '''making sure that there is only 1 most common flower'''
        for _i in range(self.Bars):
            self.height = randint(self.Interval,self.MaxNumber)
            try:
                if self.height == max(self.heights):
                    self.height = self.height - 1
            except ValueError:
                pass
            self.total = self.total + self.height
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Swimming","Soccer","Cricket","Skating","Martial Arts"]
        random.shuffle(self.BarNames)
        self.randomBarIndex = randint(0,len(self.BarNames)-1)
        self.randomBarName = self.BarNames[self.randomBarIndex]
        self.answer = self.heights[self.randomBarIndex]
        
        self.YAxisLabel = ["Number of children"]
        self.XAxisLabel = ["Types of sport"]

        self.wrongAnswers = []

        self.wrongAnswers.append(self.answer + 1)
        self.wrongAnswers.append(self.answer - 1)
        self.wrongAnswers.append(self.answer + 2)
        self.wrongAnswers.append(self.answer - 2)
                
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        
        self.FunctionCall = "P4DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+")"
        self.problem = str(self.total) + " children were asked to name their favourite sport. The following bar graph shows their choice."
        self.problem = self.problem + " How many children chose "+self.randomBarName+" as their favourite sport?"
        
        
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def GenerateProblemTypeMCQ2b(self):
        '''e.g.:
        '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"]
        self.problem_type = 'ProblemTypeMCQ2b'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = random.choice([10,15,20,25,30])
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        self.total = 0
        '''making sure that there is only 1 most common flower'''
        i = 0
        while i!=self.Bars:
            self.height = randint(self.Interval,self.MaxNumber)
            if self.height not in self.heights:
                self.total = self.total + self.height
                self.heights.append(self.height)
                i = i + 1
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Swimming","Soccer","Cricket","Skating","Martial Arts"]
        random.shuffle(self.BarNames)

        self.LargestBar = 0
        self.SecondLargestBar = -1       
        self.LargestBarIndex = -1
        self.SecondLargestBarIndex = -1
        
        for i in range(len(self.heights)):
            if self.heights[i] > self.LargestBar:
                self.SecondLargestBar = self.LargestBar
                self.SecondLargestBarIndex = self.LargestBarIndex
                self.LargestBar = self.heights[i]
                self.LargestBarIndex = i
            elif self.LargestBar > self.heights[i] > self.SecondLargestBar:
                self.SecondLargestBar = self.heights[i]
                self.SecondLargestBarIndex = i
                
        self.answer = self.BarNames[self.LargestBarIndex]+" and "+self.BarNames[self.SecondLargestBarIndex]
        
        self.YAxisLabel = ["Number of children"]
        self.XAxisLabel = ["Types of sport"]

        self.wrongAnswers = []
        
        '''assuming there are only 5 bars'''
        i = 0
        while i!=3:
            self.wrongIndices = random.sample([0,1,2,3,4],2)
            self.wrongIndices.sort()
            if self.wrongIndices != [self.SecondLargestBarIndex,self.LargestBarIndex]:
                self.wrongAnswer = self.BarNames[self.wrongIndices[0]]+" and "+self.BarNames[self.wrongIndices[1]]
                if self.wrongAnswer not in self.wrongAnswers and self.wrongAnswer != self.answer:
                    self.wrongAnswers.append(self.wrongAnswer)
                    i = i + 1
                
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        
        self.FunctionCall = "P4DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+")"
        self.problem = str(self.total) + " children were asked to name their favourite sport. The following bar graph shows their choice."
        self.problem = self.problem + " Which are the 2 most popular sports?"
        
        
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def GenerateProblemTypeMCQ2c(self):
        '''e.g.:
        '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"]
        self.problem_type = 'ProblemTypeMCQ2c'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = random.choice([10,15,20,25,30])
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        self.total = 0
        '''making sure that there is only 1 least popular sport'''
        for _i in range(self.Bars):
            self.height = randint(self.Interval,self.MaxNumber)
            try:
                if self.height == min(self.heights) and self.height!= self.MaxNumber:
                    self.height = self.height + 1
            except ValueError:
                pass
            self.total = self.total + self.height
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Swimming","Soccer","Cricket","Skating","Martial Arts"]
        random.shuffle(self.BarNames)

        self.answer = self.BarNames[self.BarHeights.index(min(self.BarHeights))]
                
        self.YAxisLabel = ["Number of children"]
        self.XAxisLabel = ["Types of sport"]

        self.wrongAnswers = []

        for i in range(len(self.BarNames)):
            if self.BarNames[i]!=self.answer:
                self.wrongAnswers.append(self.BarNames[i])
                                
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        
        self.FunctionCall = "P4DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+")"
        self.problem = str(self.total) + " children were asked to name their favourite sport. The following bar graph shows their choice."
        self.problem = self.problem + " Which is the least popular sport?"
        
        
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def GenerateProblemTypeMCQ2d(self):
        '''e.g.:
        '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"]
        self.problem_type = 'ProblemTypeMCQ2d'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = random.choice([10,15,20,25,30])
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        self.total = 0
        '''making sure that there is only 1 least popular sport'''
        for _i in range(self.Bars):
            self.height = randint(self.Interval,self.MaxNumber)
            try:
                if self.height == min(self.heights) and self.height!= self.MaxNumber:
                    self.height = self.height + 1
                elif self.height == max(self.heights):
                    self.height = self.height - 1
            except ValueError:
                pass
            self.total = self.total + self.height
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Swimming","Soccer","Cricket","Skating","Martial Arts"]
        random.shuffle(self.BarNames)

        self.answer = max(self.heights) - min(self.heights)
                
        self.YAxisLabel = ["Number of children"]
        self.XAxisLabel = ["Types of sport"]

        self.wrongAnswers = []

        self.wrongAnswers.append(self.answer + 1)
        self.wrongAnswers.append(self.answer - 1)
        self.wrongAnswers.append(self.answer - 2)
        self.wrongAnswers.append(self.answer + 2)
                                        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        
        self.FunctionCall = "P4DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+")"
        self.problem = str(self.total) + " children were asked to name their favourite sport. The following bar graph shows their choice."
        self.problem = self.problem + " How many more children chose most popular sport than least popular sport as their favourite sport?"
        
        
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType2(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation please refer to Problem 1 at <a href='/Learn/Primary-Grade-4/Data-Analysis/Tables-and-Bar-Graphs#WP1' target='_blank'><u>Tables and Bar Graphs</u></a>"
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
        
        self.names = random.sample(PersonName.PersonName,5)
        self.coupons = random.sample([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,26,28,29,30,
                                      31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],10)
        
        self.FiftyCentsCouponTotal = 0
        self.OneDollarCouponTotal = 0

        for i in range(5):
            self.FiftyCentsCouponTotal = self.FiftyCentsCouponTotal + self.coupons[i]
            self.OneDollarCouponTotal = self.OneDollarCouponTotal + self.coupons[i+5]
                                      
        self.problem = 'The table below shows the number of 50&cent; parking coupons and $1 parking coupons that 5 people used in a certain week.<br /><br />'
        self.problem = self.problem + '<table border=0>'
        self.problem = self.problem + '<tr><td rowspan=2 width=60px style="vertical-align:middle; background:#F4D162"><b>Person</b></td><td colspan=2 style="vertical-align:middle; background:#F4D162"><b>50-cent parking coupons</b></td><td colspan=2 style="vertical-align:middle; background:#F4D162"><b>$1 parking coupons</b></td><td rowspan=2 width=90px style="vertical-align:middle; background:#F4D162"><b>Total amount</b></td></tr>'
        self.problem = self.problem + '<tr><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Number of coupons used</b></td><td width=95px style="vertical-align:middle; background:#F4AECF"><b>Amount spent</b></td><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Number of coupons used</b></td><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Amount spent</b></td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[0]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[0])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[0]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[5])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[5])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[0]*float(0.5)+self.coupons[5])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[1]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[1])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[1]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[6])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[6])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[1]*float(0.5)+self.coupons[6])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[2]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[2])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[2]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[7])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[7])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[2]*float(0.5)+self.coupons[7])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[3]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[3])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[3]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[8])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[8])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[3]*float(0.5)+self.coupons[8])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[4]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[4])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[4]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[9])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[9])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[4]*float(0.5)+self.coupons[9])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4AECF"><b>Total</b></td><td style="vertical-align:middle; background:#F4AECF">'+str(self.FiftyCentsCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$'+str(self.FiftyCentsCouponTotal*float(0.5))+'</td><td style="vertical-align:middle; background:#F4AECF">'+str(self.OneDollarCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$'+str(self.OneDollarCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$?</td></tr>'
        self.problem = self.problem + '</table><br><br>' 
        
        self.problem = self.problem + "Who used the most number of parking coupons?"
        
        self.CouponsPerPerson = []
        
        for i in range(5):
            self.CouponsPerPerson.append(self.coupons[i]+self.coupons[i+5])
        
        self.answer = self.names[self.CouponsPerPerson.index(max(self.CouponsPerPerson))]
                

        self.wrongAnswers = []
        
        for i in range(len(self.names)):
            if self.names[i] != self.answer:
                self.wrongAnswers.append(self.names[i])        
        
        self.unit = ''
        '''dummy function call just to be consistent with other draw bar graph problems'''
        self.FunctionCall = ''
        self.template = "MCQTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
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
        
        self.names = random.sample(PersonName.PersonName,5)
        self.coupons = random.sample([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,26,28,29,30,
                                      31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],10)
        
        self.FiftyCentsCouponTotal = 0
        self.OneDollarCouponTotal = 0

        for i in range(5):
            self.FiftyCentsCouponTotal = self.FiftyCentsCouponTotal + self.coupons[i]
            self.OneDollarCouponTotal = self.OneDollarCouponTotal + self.coupons[i+5]
                                      
        self.problem = 'The table below shows the number of 50&cent; parking coupons and $1 parking coupons that 5 people used in a certain week.<br /><br />'
        self.problem = self.problem + '<table border=0>'
        self.problem = self.problem + '<tr><td rowspan=2 width=60px style="vertical-align:middle; background:#F4D162"><b>Person</b></td><td colspan=2 style="vertical-align:middle; background:#F4D162"><b>50-cent parking coupons</b></td><td colspan=2 style="vertical-align:middle; background:#F4D162"><b>$1 parking coupons</b></td><td rowspan=2 width=90px style="vertical-align:middle; background:#F4D162"><b>Total amount</b></td></tr>'
        self.problem = self.problem + '<tr><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Number of coupons used</b></td><td width=95px style="vertical-align:middle; background:#F4AECF"><b>Amount spent</b></td><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Number of coupons used</b></td><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Amount spent</b></td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[0]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[0])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[0]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[5])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[5])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[0]*float(0.5)+self.coupons[5])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[1]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[1])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[1]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[6])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[6])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[1]*float(0.5)+self.coupons[6])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[2]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[2])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[2]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[7])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[7])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[2]*float(0.5)+self.coupons[7])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[3]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[3])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[3]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[8])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[8])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[3]*float(0.5)+self.coupons[8])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[4]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[4])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[4]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[9])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[9])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[4]*float(0.5)+self.coupons[9])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4AECF"><b>Total</b></td><td style="vertical-align:middle; background:#F4AECF">'+str(self.FiftyCentsCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$'+str(self.FiftyCentsCouponTotal*float(0.5))+'</td><td style="vertical-align:middle; background:#F4AECF">'+str(self.OneDollarCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$'+str(self.OneDollarCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$?</td></tr>'
        self.problem = self.problem + '</table><br><br>' 
        
        self.problem = self.problem + "Who spent the most amount of money on parking?"
        
        self.AmountSpentPerPerson = []
        
        for i in range(5):
            self.AmountSpentPerPerson.append(self.coupons[i]*float(0.5)+self.coupons[i+5])
        
        self.answer = self.names[self.AmountSpentPerPerson.index(max(self.AmountSpentPerPerson))]
                

        self.wrongAnswers = []
        
        for i in range(len(self.names)):
            if self.names[i] != self.answer:
                self.wrongAnswers.append(self.names[i])        
        
        self.unit = ''
        '''dummy function call just to be consistent with other draw bar graph problems'''
        self.FunctionCall = ''
        self.template = "MCQTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
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
        
        self.names = random.sample(PersonName.PersonName,5)
        self.coupons = random.sample([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,26,28,29,30,
                                      31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],10)
        
        self.FiftyCentsCouponTotal = 0
        self.OneDollarCouponTotal = 0

        for i in range(5):
            self.FiftyCentsCouponTotal = self.FiftyCentsCouponTotal + self.coupons[i]
            self.OneDollarCouponTotal = self.OneDollarCouponTotal + self.coupons[i+5]
                                      
        self.problem = 'The table below shows the number of 50&cent; parking coupons and $1 parking coupons that 5 people used in a certain week.<br /><br />'
        self.problem = self.problem + '<table border=0>'
        self.problem = self.problem + '<tr><td rowspan=2 width=60px style="vertical-align:middle; background:#F4D162"><b>Person</b></td><td colspan=2 style="vertical-align:middle; background:#F4D162"><b>50-cent parking coupons</b></td><td colspan=2 style="vertical-align:middle; background:#F4D162"><b>$1 parking coupons</b></td><td rowspan=2 width=90px style="vertical-align:middle; background:#F4D162"><b>Total amount</b></td></tr>'
        self.problem = self.problem + '<tr><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Number of coupons used</b></td><td width=95px style="vertical-align:middle; background:#F4AECF"><b>Amount spent</b></td><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Number of coupons used</b></td><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Amount spent</b></td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[0]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[0])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[0]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[5])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[5])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[0]*float(0.5)+self.coupons[5])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[1]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[1])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[1]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[6])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[6])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[1]*float(0.5)+self.coupons[6])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[2]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[2])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[2]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[7])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[7])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[2]*float(0.5)+self.coupons[7])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[3]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[3])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[3]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[8])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[8])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[3]*float(0.5)+self.coupons[8])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[4]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[4])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[4]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[9])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[9])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[4]*float(0.5)+self.coupons[9])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4AECF"><b>Total</b></td><td style="vertical-align:middle; background:#F4AECF">'+str(self.FiftyCentsCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$'+str(self.FiftyCentsCouponTotal*float(0.5))+'</td><td style="vertical-align:middle; background:#F4AECF">'+str(self.OneDollarCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$'+str(self.OneDollarCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$?</td></tr>'
        self.problem = self.problem + '</table><br><br>' 
        
        self.problem = self.problem + "Who spent the least amount of money on parking?"
        
        self.AmountSpentPerPerson = []
        
        for i in range(5):
            self.AmountSpentPerPerson.append(self.coupons[i]*float(0.5)+self.coupons[i+5])
        
        self.answer = self.names[self.AmountSpentPerPerson.index(min(self.AmountSpentPerPerson))]
                

        self.wrongAnswers = []
        
        for i in range(len(self.names)):
            if self.names[i] != self.answer:
                self.wrongAnswers.append(self.names[i])        
        
        self.unit = ''
        '''dummy function call just to be consistent with other draw bar graph problems'''
        self.FunctionCall = ''
        self.template = "MCQTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
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
        
        self.names = random.sample(PersonName.PersonName,5)
        self.coupons = random.sample([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,26,28,29,30,
                                      31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],10)
        
        self.FiftyCentsCouponTotal = 0
        self.OneDollarCouponTotal = 0

        for i in range(5):
            self.FiftyCentsCouponTotal = self.FiftyCentsCouponTotal + self.coupons[i]
            self.OneDollarCouponTotal = self.OneDollarCouponTotal + self.coupons[i+5]
            
        self.TwoRandomPeopleIndices = random.sample([0,1,2,3,4],2)
        
        self.TotalParkingCoupons1 = self.coupons[self.TwoRandomPeopleIndices[0]] + self.coupons[self.TwoRandomPeopleIndices[0] + 5]
        self.TotalParkingCoupons2 = self.coupons[self.TwoRandomPeopleIndices[1]] + self.coupons[self.TwoRandomPeopleIndices[1] + 5]
                                      
        self.problem = 'The table below shows the number of 50&cent; parking coupons and $1 parking coupons that 5 people used in a certain week.<br /><br />'
        self.problem = self.problem + '<table border=0>'
        self.problem = self.problem + '<tr><td rowspan=2 width=60px style="vertical-align:middle; background:#F4D162"><b>Person</b></td><td colspan=2 style="vertical-align:middle; background:#F4D162"><b>50-cent parking coupons</b></td><td colspan=2 style="vertical-align:middle; background:#F4D162"><b>$1 parking coupons</b></td><td rowspan=2 width=90px style="vertical-align:middle; background:#F4D162"><b>Total amount</b></td></tr>'
        self.problem = self.problem + '<tr><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Number of coupons used</b></td><td width=95px style="vertical-align:middle; background:#F4AECF"><b>Amount spent</b></td><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Number of coupons used</b></td><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Amount spent</b></td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[0]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[0])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[0]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[5])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[5])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[0]*float(0.5)+self.coupons[5])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[1]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[1])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[1]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[6])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[6])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[1]*float(0.5)+self.coupons[6])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[2]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[2])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[2]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[7])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[7])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[2]*float(0.5)+self.coupons[7])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[3]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[3])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[3]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[8])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[8])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[3]*float(0.5)+self.coupons[8])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[4]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[4])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[4]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[9])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[9])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[4]*float(0.5)+self.coupons[9])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4AECF"><b>Total</b></td><td style="vertical-align:middle; background:#F4AECF">'+str(self.FiftyCentsCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$'+str(self.FiftyCentsCouponTotal*float(0.5))+'</td><td style="vertical-align:middle; background:#F4AECF">'+str(self.OneDollarCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$'+str(self.OneDollarCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$?</td></tr>'
        self.problem = self.problem + '</table><br><br>' 
        
        if self.TotalParkingCoupons1 > self.TotalParkingCoupons2:
            self.problem = self.problem + "How many more parking coupons did "+self.names[self.TwoRandomPeopleIndices[0]]+" use than "+self.names[self.TwoRandomPeopleIndices[1]]+"?"
        else:
            self.problem = self.problem + "How many more parking coupons did "+self.names[self.TwoRandomPeopleIndices[1]]+" use than "+self.names[self.TwoRandomPeopleIndices[0]]+"?"
        
        self.answer = abs(self.TotalParkingCoupons1-self.TotalParkingCoupons2)
                

        self.wrongAnswers = []
        
        i=0
        while i!=3:
            j = randint(-5,5)
            if j!=0 and (self.answer+j) not in self.wrongAnswers and (self.answer+j)>0:
                self.wrongAnswers.append(self.answer+j)
                i = i + 1
            
        self.unit = ''
        '''dummy function call just to be consistent with other draw bar graph problems'''
        self.FunctionCall = ''
        self.template = "MCQTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def GenerateProblemTypeMCQ3e(self):
        '''e.g.:
        '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemTypeMCQ3e'
        self.CheckAnswerType = 1
        
        self.names = random.sample(PersonName.PersonName,5)
        self.coupons = random.sample([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,26,28,29,30,
                                      31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],10)
        
        self.FiftyCentsCouponTotal = 0
        self.OneDollarCouponTotal = 0

        for i in range(5):
            self.FiftyCentsCouponTotal = self.FiftyCentsCouponTotal + self.coupons[i]
            self.OneDollarCouponTotal = self.OneDollarCouponTotal + self.coupons[i+5]
                                                 
        self.problem = 'The table below shows the number of 50&cent; parking coupons and $1 parking coupons that 5 people used in a certain week.<br /><br />'
        self.problem = self.problem + '<table border=0>'
        self.problem = self.problem + '<tr><td rowspan=2 width=60px style="vertical-align:middle; background:#F4D162"><b>Person</b></td><td colspan=2 style="vertical-align:middle; background:#F4D162"><b>50-cent parking coupons</b></td><td colspan=2 style="vertical-align:middle; background:#F4D162"><b>$1 parking coupons</b></td><td rowspan=2 width=90px style="vertical-align:middle; background:#F4D162"><b>Total amount</b></td></tr>'
        self.problem = self.problem + '<tr><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Number of coupons used</b></td><td width=95px style="vertical-align:middle; background:#F4AECF"><b>Amount spent</b></td><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Number of coupons used</b></td><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Amount spent</b></td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[0]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[0])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[0]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[5])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[5])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[0]*float(0.5)+self.coupons[5])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[1]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[1])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[1]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[6])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[6])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[1]*float(0.5)+self.coupons[6])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[2]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[2])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[2]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[7])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[7])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[2]*float(0.5)+self.coupons[7])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[3]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[3])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[3]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[8])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[8])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[3]*float(0.5)+self.coupons[8])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[4]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[4])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[4]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[9])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[9])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[4]*float(0.5)+self.coupons[9])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4AECF"><b>Total</b></td><td style="vertical-align:middle; background:#F4AECF">'+str(self.FiftyCentsCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$'+str(self.FiftyCentsCouponTotal*float(0.5))+'</td><td style="vertical-align:middle; background:#F4AECF">'+str(self.OneDollarCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$'+str(self.OneDollarCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$?</td></tr>'
        self.problem = self.problem + '</table><br><br>' 
 
        if self.OneDollarCouponTotal > self.FiftyCentsCouponTotal:
            self.problem = self.problem + "How many more $1 parking coupons than 50-cent parking coupons were used altogether?"
        else:
            self.problem = self.problem + "How many more 50-cent parking coupons than $1 parking coupons were used altogether?"
            
        self.answer = abs(self.OneDollarCouponTotal-self.FiftyCentsCouponTotal)
                

        self.wrongAnswers = []
        
        i=0
        while i!=3:
            j = randint(-5,5)
            if j!=0 and (self.answer+j) not in self.wrongAnswers and (self.answer+j)>0:
                self.wrongAnswers.append(self.answer+j)
                i = i + 1
            
        self.unit = ''
        '''dummy function call just to be consistent with other draw bar graph problems'''
        self.FunctionCall = ''
        self.template = "MCQTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def GenerateProblemTypeMCQ3f(self):
        '''e.g.:
        '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = 'ProblemTypeMCQ3f'
        self.CheckAnswerType = 1
        
        self.names = random.sample(PersonName.PersonName,5)
        self.coupons = random.sample([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,26,28,29,30,
                                      31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],10)
        
        self.FiftyCentsCouponTotal = 0
        self.OneDollarCouponTotal = 0

        for i in range(5):
            self.FiftyCentsCouponTotal = self.FiftyCentsCouponTotal + self.coupons[i]
            self.OneDollarCouponTotal = self.OneDollarCouponTotal + self.coupons[i+5]
                                                 
        self.problem = 'The table below shows the number of 50&cent; parking coupons and $1 parking coupons that 5 people used in a certain week.<br /><br />'
        self.problem = self.problem + '<table border=0>'
        self.problem = self.problem + '<tr><td rowspan=2 width=60px style="vertical-align:middle; background:#F4D162"><b>Person</b></td><td colspan=2 style="vertical-align:middle; background:#F4D162"><b>50-cent parking coupons</b></td><td colspan=2 style="vertical-align:middle; background:#F4D162"><b>$1 parking coupons</b></td><td rowspan=2 width=90px style="vertical-align:middle; background:#F4D162"><b>Total amount</b></td></tr>'
        self.problem = self.problem + '<tr><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Number of coupons used</b></td><td width=95px style="vertical-align:middle; background:#F4AECF"><b>Amount spent</b></td><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Number of coupons used</b></td><td width=90px style="vertical-align:middle; background:#F4AECF"><b>Amount spent</b></td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[0]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[0])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[0]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[5])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[5])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[0]*float(0.5)+self.coupons[5])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[1]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[1])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[1]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[6])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[6])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[1]*float(0.5)+self.coupons[6])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[2]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[2])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[2]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[7])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[7])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[2]*float(0.5)+self.coupons[7])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[3]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[3])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[3]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[8])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[8])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[3]*float(0.5)+self.coupons[8])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4D4D1">'+self.names[4]+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[4])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[4]*float(0.5))+'</td><td style="vertical-align:middle; background:#F4D4D1">'+str(self.coupons[9])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[9])+'</td><td style="vertical-align:middle; background:#F4D4D1">$'+str(self.coupons[4]*float(0.5)+self.coupons[9])+'</td></tr>'
        self.problem = self.problem + '<tr><td style="vertical-align:middle; background:#F4AECF"><b>Total</b></td><td style="vertical-align:middle; background:#F4AECF">'+str(self.FiftyCentsCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$'+str(self.FiftyCentsCouponTotal*float(0.5))+'</td><td style="vertical-align:middle; background:#F4AECF">'+str(self.OneDollarCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$'+str(self.OneDollarCouponTotal)+'</td><td style="vertical-align:middle; background:#F4AECF">$?</td></tr>'
        self.problem = self.problem + '</table><br><br>' 
 
        self.problem = self.problem + "How much money was spent altogether on parking in the week?"
            
        self.answer = (self.OneDollarCouponTotal+float(0.5)*self.FiftyCentsCouponTotal)
                

        self.wrongAnswers = []
        
        i=0
        while i!=3:
            j = randint(-5,5)
            if j!=0 and (self.answer+j) not in self.wrongAnswers and (self.answer+j)>0:
                self.wrongAnswers.append(self.answer+j)
                i = i + 1
            
        self.unit = ''
        '''dummy function call just to be consistent with other draw bar graph problems'''
        self.FunctionCall = ''
        self.template = "MCQTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType3(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation please refer to Problem 2 at <a href='/Learn/Primary-Grade-4/Data-Analysis/Tables-and-Bar-Graphs#WP2' target='_blank'><u>Tables and Bar Graphs</u></a>"
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