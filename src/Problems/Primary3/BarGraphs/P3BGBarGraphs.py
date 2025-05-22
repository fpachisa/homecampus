'''
Created on Jan 01, 2014
Module: P3BGBarGraphs
Generates the "Interpreting data in bar graphs" problems for Primary 3

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

class P3BGBarGraphs:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:['ProblemTypeMCQ1a',],2:['ProblemTypeMCQ1d',],3:['ProblemTypeMCQ2c',],4:['ProblemTypeMCQ2e',],5:['ProblemTypeMCQ3a',],
                            6:['ProblemTypeMCQ3e',],7:['ProblemTypeMCQ4a',],8:['ProblemTypeMCQ5a',],9:['ProblemTypeMCQ5b',],10:['ProblemTypeMCQ6a',],
                            11:['ProblemTypeMCQ6d',],12:['ProblemTypeMCQ7a',],13:['ProblemTypeMCQ7c',],14:['ProblemTypeMCQ8a',],15:['ProblemTypeMCQ8d',],
                            16:['ProblemTypeMCQ9b',],17:['ProblemTypeMCQ9d',],18:['ProblemTypeMCQ10a',],19:['ProblemTypeMCQ10d',],20:['ProblemTypeMCQ11a',],
                            21:['ProblemTypeMCQ11d',],22:['ProblemTypeMCQ12a',],23:['ProblemTypeMCQ13c',],24:['ProblemTypeMCQ13d',],25:['ProblemTypeMCQ14a',],
                            26:['ProblemTypeMCQ14c',],27:['ProblemTypeMCQ1b',],28:['ProblemTypeMCQ1e',],29:['ProblemTypeMCQ2a',],30:['ProblemTypeMCQ2b',],
                            31:['ProblemTypeMCQ3c',],32:['ProblemTypeMCQ4b',],33:['ProblemTypeMCQ5d',],34:['ProblemTypeMCQ6b',],35:['ProblemTypeMCQ7d',],
                            36:['ProblemTypeMCQ8b',],37:['ProblemTypeMCQ8e',],38:['ProblemTypeMCQ9a',],39:['ProblemTypeMCQ9c',],40:['ProblemTypeMCQ10c',],
                            41:['ProblemTypeMCQ10e',],42:['ProblemTypeMCQ1c',],43:['ProblemTypeMCQ11c',],44:['ProblemTypeMCQ11e',],45:['ProblemTypeMCQ12c',],
                            46:['ProblemTypeMCQ13a',],47:['ProblemTypeMCQ14b',],48:['ProblemTypeMCQ14d',],49:['ProblemTypeMCQ1f',],50:['ProblemTypeMCQ1g',],
                            51:['ProblemTypeMCQ2d',],52:['ProblemTypeMCQ3b',],53:['ProblemTypeMCQ3d',],54:['ProblemTypeMCQ5c',],55:['ProblemTypeMCQ6c',],
                            56:['ProblemTypeMCQ7b',],57:['ProblemTypeMCQ8c',],58:['ProblemTypeMCQ9e',],59:['ProblemTypeMCQ10b',],60:['ProblemTypeMCQ11b',],
                            61:['ProblemTypeMCQ12b',],62:['ProblemTypeMCQ13b',],63:['ProblemTypeMCQ13e',],64:['ProblemTypeMCQ14e',],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemTypeMCQ1a(),],2:[self.GenerateProblemTypeMCQ1d(),],3:[self.GenerateProblemTypeMCQ2c(),],
                                   4:[self.GenerateProblemTypeMCQ2e(),],5:[self.GenerateProblemTypeMCQ3a(),],6:[self.GenerateProblemTypeMCQ3e(),],
                                   7:[self.GenerateProblemTypeMCQ4a(),],8:[self.GenerateProblemTypeMCQ5a(),],9:[self.GenerateProblemTypeMCQ5b(),],
                                   10:[self.GenerateProblemTypeMCQ6a(),],11:[self.GenerateProblemTypeMCQ6d(),],12:[self.GenerateProblemTypeMCQ7a(),],
                                   13:[self.GenerateProblemTypeMCQ7c(),],14:[self.GenerateProblemTypeMCQ8a(),],15:[self.GenerateProblemTypeMCQ8d(),],
                                   16:[self.GenerateProblemTypeMCQ9b(),],17:[self.GenerateProblemTypeMCQ9d(),],18:[self.GenerateProblemTypeMCQ10a(),],
                                   19:[self.GenerateProblemTypeMCQ10d(),],20:[self.GenerateProblemTypeMCQ11a(),],21:[self.GenerateProblemTypeMCQ11d(),],
                                   22:[self.GenerateProblemTypeMCQ12a(),],23:[self.GenerateProblemTypeMCQ13c(),],24:[self.GenerateProblemTypeMCQ13d(),],
                                   25:[self.GenerateProblemTypeMCQ14a(),],26:[self.GenerateProblemTypeMCQ14c(),],27:[self.GenerateProblemTypeMCQ1b(),],
                                   28:[self.GenerateProblemTypeMCQ1e(),],29:[self.GenerateProblemTypeMCQ2a(),],30:[self.GenerateProblemTypeMCQ2b(),],
                                   31:[self.GenerateProblemTypeMCQ3c(),],32:[self.GenerateProblemTypeMCQ4b(),],33:[self.GenerateProblemTypeMCQ5d(),],
                                   34:[self.GenerateProblemTypeMCQ6b(),],35:[self.GenerateProblemTypeMCQ7d(),],36:[self.GenerateProblemTypeMCQ8b(),],
                                   37:[self.GenerateProblemTypeMCQ8e(),],38:[self.GenerateProblemTypeMCQ9a(),],39:[self.GenerateProblemTypeMCQ9c(),],
                                   40:[self.GenerateProblemTypeMCQ10c(),],41:[self.GenerateProblemTypeMCQ10e(),],42:[self.GenerateProblemTypeMCQ1c(),],
                                   43:[self.GenerateProblemTypeMCQ11c(),],44:[self.GenerateProblemTypeMCQ11e(),],45:[self.GenerateProblemTypeMCQ12c(),],
                                   46:[self.GenerateProblemTypeMCQ13a(),],47:[self.GenerateProblemTypeMCQ14b(),],48:[self.GenerateProblemTypeMCQ14d(),],
                                   49:[self.GenerateProblemTypeMCQ1f(),],50:[self.GenerateProblemTypeMCQ1g(),],51:[self.GenerateProblemTypeMCQ2d(),],
                                   52:[self.GenerateProblemTypeMCQ3b(),],53:[self.GenerateProblemTypeMCQ3d(),],54:[self.GenerateProblemTypeMCQ5c(),],
                                   55:[self.GenerateProblemTypeMCQ6c(),],56:[self.GenerateProblemTypeMCQ7b(),],57:[self.GenerateProblemTypeMCQ8c(),],
                                   58:[self.GenerateProblemTypeMCQ9e(),],59:[self.GenerateProblemTypeMCQ10b(),],60:[self.GenerateProblemTypeMCQ11b(),],
                                   61:[self.GenerateProblemTypeMCQ12b(),],62:[self.GenerateProblemTypeMCQ13b(),],63:[self.GenerateProblemTypeMCQ13e(),],
                                   64:[self.GenerateProblemTypeMCQ14e(),],
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
        return self.GenerateProblemTypeMCQ3a()

    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {'ProblemTypeMCQ1a':self.GenerateProblemTypeMCQ1a(),'ProblemTypeMCQ1d':self.GenerateProblemTypeMCQ1d(),'ProblemTypeMCQ2c':self.GenerateProblemTypeMCQ2c(),
                            'ProblemTypeMCQ2e':self.GenerateProblemTypeMCQ2e(),'ProblemTypeMCQ3a':self.GenerateProblemTypeMCQ3a(),'ProblemTypeMCQ3e':self.GenerateProblemTypeMCQ3e(),
                            'ProblemTypeMCQ4a':self.GenerateProblemTypeMCQ4a(),'ProblemTypeMCQ5a':self.GenerateProblemTypeMCQ5a(),'ProblemTypeMCQ5b':self.GenerateProblemTypeMCQ5b(),
                            'ProblemTypeMCQ6a':self.GenerateProblemTypeMCQ6a(),'ProblemTypeMCQ6d':self.GenerateProblemTypeMCQ6d(),'ProblemTypeMCQ7a':self.GenerateProblemTypeMCQ7a(),
                            'ProblemTypeMCQ7c':self.GenerateProblemTypeMCQ7c(),'ProblemTypeMCQ8a':self.GenerateProblemTypeMCQ8a(),'ProblemTypeMCQ8d':self.GenerateProblemTypeMCQ8d(),
                            'ProblemTypeMCQ9b':self.GenerateProblemTypeMCQ9b(),'ProblemTypeMCQ9d':self.GenerateProblemTypeMCQ9d(),'ProblemTypeMCQ10a':self.GenerateProblemTypeMCQ10a(),
                            'ProblemTypeMCQ10d':self.GenerateProblemTypeMCQ10d(),'ProblemTypeMCQ11a':self.GenerateProblemTypeMCQ11a(),'ProblemTypeMCQ11d':self.GenerateProblemTypeMCQ11d(),
                            'ProblemTypeMCQ12a':self.GenerateProblemTypeMCQ12a(),'ProblemTypeMCQ13c':self.GenerateProblemTypeMCQ13c(),'ProblemTypeMCQ13d':self.GenerateProblemTypeMCQ13d(),
                            'ProblemTypeMCQ14a':self.GenerateProblemTypeMCQ14a(),'ProblemTypeMCQ14c':self.GenerateProblemTypeMCQ14c(),'ProblemTypeMCQ1b':self.GenerateProblemTypeMCQ1b(),
                            'ProblemTypeMCQ1e':self.GenerateProblemTypeMCQ1e(),'ProblemTypeMCQ2a':self.GenerateProblemTypeMCQ2a(),'ProblemTypeMCQ2b':self.GenerateProblemTypeMCQ2b(),
                            'ProblemTypeMCQ3c':self.GenerateProblemTypeMCQ3c(),'ProblemTypeMCQ4b':self.GenerateProblemTypeMCQ4b(),'ProblemTypeMCQ5d':self.GenerateProblemTypeMCQ5d(),
                            'ProblemTypeMCQ6b':self.GenerateProblemTypeMCQ6b(),'ProblemTypeMCQ7d':self.GenerateProblemTypeMCQ7d(),'ProblemTypeMCQ8b':self.GenerateProblemTypeMCQ8b(),
                            'ProblemTypeMCQ8e':self.GenerateProblemTypeMCQ8e(),'ProblemTypeMCQ9a':self.GenerateProblemTypeMCQ9a(),'ProblemTypeMCQ9c':self.GenerateProblemTypeMCQ9c(),
                            'ProblemTypeMCQ10c':self.GenerateProblemTypeMCQ10c(),'ProblemTypeMCQ10e':self.GenerateProblemTypeMCQ10e(),'ProblemTypeMCQ1c':self.GenerateProblemTypeMCQ1c(),
                            'ProblemTypeMCQ11c':self.GenerateProblemTypeMCQ11c(),'ProblemTypeMCQ11e':self.GenerateProblemTypeMCQ11e(),'ProblemTypeMCQ12c':self.GenerateProblemTypeMCQ12c(),
                            'ProblemTypeMCQ13a':self.GenerateProblemTypeMCQ13a(),'ProblemTypeMCQ14b':self.GenerateProblemTypeMCQ14b(),'ProblemTypeMCQ14d':self.GenerateProblemTypeMCQ14d(),
                            'ProblemTypeMCQ1f':self.GenerateProblemTypeMCQ1f(),'ProblemTypeMCQ1g':self.GenerateProblemTypeMCQ1g(),'ProblemTypeMCQ2d':self.GenerateProblemTypeMCQ2d(),
                            'ProblemTypeMCQ3b':self.GenerateProblemTypeMCQ3b(),'ProblemTypeMCQ3d':self.GenerateProblemTypeMCQ3d(),'ProblemTypeMCQ5c':self.GenerateProblemTypeMCQ5c(),
                            'ProblemTypeMCQ6c':self.GenerateProblemTypeMCQ6c(),'ProblemTypeMCQ7b':self.GenerateProblemTypeMCQ7b(),'ProblemTypeMCQ8c':self.GenerateProblemTypeMCQ8c(),
                            'ProblemTypeMCQ9e':self.GenerateProblemTypeMCQ9e(),'ProblemTypeMCQ10b':self.GenerateProblemTypeMCQ10b(),'ProblemTypeMCQ11b':self.GenerateProblemTypeMCQ11b(),
                            'ProblemTypeMCQ12b':self.GenerateProblemTypeMCQ12b(),'ProblemTypeMCQ13b':self.GenerateProblemTypeMCQ13b(),'ProblemTypeMCQ13e':self.GenerateProblemTypeMCQ13e(),
                            'ProblemTypeMCQ14e':self.GenerateProblemTypeMCQ14e(),
                            }
        return self.ProblemType[problem_type]
            
    def GenerateProblemTypeMCQ1a(self):
        '''e.g.:
        '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ1a'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = 100
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []

        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,10)
            self.heights.append(self.height)
            
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri"]
        self.YAxisLabel = ["Number of maths questions solved"]
        self.XAxisLabel = [""]
        
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.DayIndex = randint(0,4)
        self.answer = self.heights[self.DayIndex]
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+5)
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer-5)
        self.wrongAnswers.append(self.answer-10)
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Maths questions solved over 5 days")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
        self.problem = self.name + " drew a bar graph to show the number of maths questions she solved from Monday to Friday last week. "
        self.problem = self.problem + "How many questions did she solve on %s?<br>"%(self.days[self.DayIndex])
        
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1a(self.problem,self.answer,self.unit,self.name,self.days[self.DayIndex])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType1a(self,problem,answer,unit,name,day):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The height of the bar for %s is %d.<br><br>So, %s solved <b>%d</b> questions on %s."%(day,answer,name,answer,day)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemTypeMCQ1b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ1b'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = 100
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,10)
            try:
                if self.height == max(self.heights):
                    self.height = self.height - 10
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri"]
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        #random.shuffle(self.BarNames)
        self.YAxisLabel = ["Number of maths questions solved"]
        self.XAxisLabel = [""]

        
        self.answer = self.days[self.BarHeights.index(max(self.BarHeights))]
        self.wrongAnswers = []
        for i in range(len(self.days)):
            if self.days[i]!=self.answer:
                self.wrongAnswers.append(self.days[i])
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Maths questions solved over 5 days")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
        self.problem = self.name + " drew a bar graph to show the number of maths questions she solved from Monday to Friday last week. "
        self.problem = self.problem + "On which day did she solve the most number of questions?<br>"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1b(self.problem,self.answer,self.unit,self.name,max(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType1b(self,problem,answer,unit,name,maxQuestions):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The tallest bar in the graph is for %s (%d questions).<br><br>So, %s solved the most number of questions on <b>%s</b>."%(str(answer),maxQuestions,name,str(answer))
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemTypeMCQ1c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ1c'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = 100
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,10)
            try:
                if self.height == min(self.heights):
                    self.height = self.height + 10
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri"]
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        #random.shuffle(self.BarNames)
        self.YAxisLabel = ["Number of math questions solved"]
        self.XAxisLabel = [""]
        
        self.answer = self.days[self.BarHeights.index(min(self.BarHeights))]
        self.wrongAnswers = []
        for i in range(len(self.days)):
            if self.days[i]!=self.answer:
                self.wrongAnswers.append(self.days[i])
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Maths questions solved over 5 days")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
        self.problem = self.name + " drew a bar graph to show the number of maths questions she solved from Monday to Friday last week. "
        self.problem = self.problem + "On which day did she solve the fewest number of questions?<br>"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1c(self.problem,self.answer,self.unit,self.name,min(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType1c(self,problem,answer,unit,name,minQuestions):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The shortest bar in the graph is for %s (%d questions).<br><br>So, %s solved the fewest number of questions on <b>%s</b>."%(str(answer),minQuestions,name,str(answer))
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ1d(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ1d'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = 100
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri"]
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.YAxisLabel = ["Number of maths questions solved"]
        self.XAxisLabel = [""]
        self.DayIndex = randint(0,4)
        self.problem = self.name + " drew a bar graph to show the number of maths questions she solved from Monday to Friday last week. "
        self.problem = self.problem + "On which day did she solve %d questions?<br>"%(self.heights[self.DayIndex])
        self.answer = self.days[self.DayIndex]
        self.wrongAnswers = []
        for i in range(len(self.days)):
            if self.days[i]!=self.answer:
                self.wrongAnswers.append(self.days[i])
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Maths questions solved over 5 days")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1d(self.problem,self.answer,self.unit,self.name,self.heights[self.DayIndex])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType1d(self,problem,answer,unit,name,questions):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d is the height of the bar for %s.<br><br>So, %s solved %d questions on <b>%s</b>."%(questions,str(answer),name,questions,str(answer))
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ1e(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ1e'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = 100
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri"]
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.YAxisLabel = ["Number of maths questions solved"]
        self.XAxisLabel = [""]
        self.DayIndices = random.sample([0,1,2,3,4],2)
        self.diff = self.heights[self.DayIndices[0]] - self.heights[self.DayIndices[1]]
        self.problem = self.name + " drew a bar graph to show the number of maths questions she solved from Monday to Friday last week. "
        if self.diff > 0:
            self.problem = self.problem + "On which day did she solve %d fewer questions than on %s?<br>"%(self.diff,self.days[self.DayIndices[0]])
        else:
            self.problem = self.problem + "On which day did she solve %d more questions than on %s?<br>"%(abs(self.diff),self.days[self.DayIndices[0]])
        self.answer = self.days[self.DayIndices[1]]
        self.wrongAnswers = []
        for i in range(len(self.days)):
            if self.days[i]!=self.answer:
                self.wrongAnswers.append(self.days[i])
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Maths questions solved over 5 days")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1e(self.problem,self.answer,self.unit,self.heights[self.DayIndices[0]],self.days[self.DayIndices[0]],self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType1e(self,problem,answer,unit,question1,day1,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Number of questions solved on %s &nbsp;=&nbsp; %d<br><br>"%(day1,question1)
        if diff > 0:
            self.solution_text = self.solution_text + "%d fewer questions than %d &nbsp;=&nbsp; "%(abs(diff),question1)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(question1,abs(diff),question1-abs(diff))
            self.solution_text = self.solution_text + "%d is the height of the bar for %s.<br><br>"%(question1-abs(diff),str(answer))
            self.solution_text = self.solution_text + "She solved %d fewer questions on <b>%s</b> than on %s."%(abs(diff),str(answer),day1)
        else:
            self.solution_text = self.solution_text + "%d more questions than %d &nbsp;=&nbsp; "%(abs(diff),question1)
            self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(abs(diff),question1,question1+abs(diff))
            self.solution_text = self.solution_text + "%d is the height of the bar for %s.<br><br>"%(question1+abs(diff),str(answer))
            self.solution_text = self.solution_text + "She solved %d more questions on <b>%s</b> than on %s."%(abs(diff),str(answer),day1)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ1f(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ1f'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = 100
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri"]
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.YAxisLabel = ["Number of maths questions solved"]
        self.XAxisLabel = [""]
        self.DayIndices = random.sample([0,1,2,3,4],2)
        self.diff = self.heights[self.DayIndices[0]] - self.heights[self.DayIndices[1]]
        self.problem = self.name + " drew a bar graph to show the number of maths questions she solved from Monday to Friday last week. "
        if self.diff > 0:
            self.problem = self.problem + "How many more questions did she solve on %s than on %s?"%(self.days[self.DayIndices[0]],self.days[self.DayIndices[1]])
        else:
            self.problem = self.problem + "How many fewer questions did she solve on %s than on %s?"%(self.days[self.DayIndices[0]],self.days[self.DayIndices[1]])
        self.answer = abs(self.diff)
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer-10)
        self.wrongAnswers.append(self.answer+20)
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Maths questions solved over 5 days")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1f(self.problem,self.answer,self.unit,self.heights[self.DayIndices[0]],self.heights[self.DayIndices[1]],self.days[self.DayIndices[0]],self.days[self.DayIndices[1]],self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType1f(self,problem,answer,unit,question1,question2,day1,day2,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        if diff > 0:
            self.solution_text = self.solution_text + "Number of questions solved on %s &nbsp;=&nbsp; %d<br><br>"%(day1,question1)
            self.solution_text = self.solution_text + "Number of questions solved on %s &nbsp;=&nbsp; %d<br><br>"%(day2,question2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(question1,question2,answer)
            self.solution_text = self.solution_text + "She solved <b>%d</b> more questions on %s than on %s."%(answer,day1,day2)
        else:
            self.solution_text = self.solution_text + "Number of questions solved on %s &nbsp;=&nbsp; %d<br><br>"%(day2,question2)
            self.solution_text = self.solution_text + "Number of questions solved on %s &nbsp;=&nbsp; %d<br><br>"%(day1,question1)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(question2,question1,answer)
            self.solution_text = self.solution_text + "She solved <b>%d</b> fewer questions on %s than on %s."%(answer,day1,day2)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ1g(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ1g'
        self.CheckAnswerType = 1
        
        self.name = random.choice(PersonName.GirlName)
        
        self.MaxNumber = 100
        self.Interval = self.MaxNumber / 5
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri"]
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.YAxisLabel = ["Number of maths questions solved"]
        self.XAxisLabel = [""]
        self.DayIndex = randint(0,4)
        self.CorrectQuestions = randint(self.heights[self.DayIndex]*0.5,self.heights[self.DayIndex]*0.9)
        self.problem = self.name + " drew a bar graph to show the number of maths questions she solved from Monday to Friday last week. "
        self.problem = self.problem + "On %s she solved %d questions correctly. How many questions did she get wrong on %s?"%(self.days[self.DayIndex],
                                                                                                                              self.CorrectQuestions,self.days[self.DayIndex])
        self.answer = self.heights[self.DayIndex] - self.CorrectQuestions
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+1)
        self.wrongAnswers.append(self.answer+5)
        self.wrongAnswers.append(self.answer+3)
        self.wrongAnswers.append(self.answer-1)
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Maths questions solved over 5 days")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1g(self.problem,self.answer,self.unit,self.heights[self.DayIndex],self.CorrectQuestions,self.days[self.DayIndex])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType1g(self,problem,answer,unit,question1,question2,day):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Total number of questions solved on %s &nbsp;=&nbsp; %d<br><br>"%(day,question1)
        self.solution_text = self.solution_text + "Number of questions solved correctly on %s &nbsp;=&nbsp; %d<br><br>"%(day,question2)
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(question1,question2,answer)
        self.solution_text = self.solution_text + "She got <b>%d</b> questions wrong on %s.<br>"%(answer,day)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ2a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ2a'
        self.CheckAnswerType = 1
        self.MaxNumber = 600
        self.Interval = self.MaxNumber / 12
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,50)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,50)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["2008","2009","2010","2011","2012"]
        self.YAxisLabel = ["Annual rainfall in cm"]
        self.XAxisLabel = [""]
        self.YearIndex = randint(0,4)
        self.problem = "The annual rainfall in a city  for a 5-year period is recorded in the bar graph below. "
        self.problem = self.problem + "How much rainfall did the city receive in the year %s?<br>"%(self.BarNames[self.YearIndex])
        year = self.BarNames[self.YearIndex]
        self.answer = str(self.heights[self.YearIndex])+" cm"
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.heights[self.YearIndex]+50)+" cm")
        self.wrongAnswers.append(str(self.heights[self.YearIndex]+100)+" cm")
        self.wrongAnswers.append(str(self.heights[self.YearIndex]-50)+" cm")
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Annual rainfall for a 5-year period")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2a(self.problem,self.answer,self.unit,year)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType2a(self,problem,answer,unit,year):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The height of the bar for the year %s is %s.<br><br>So, the city received <b>%s</b> of rainfall in the year %s."%(year,answer,answer,year)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
                        
    def GenerateProblemTypeMCQ2b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ2b'
        self.CheckAnswerType = 1
        self.MaxNumber = 600
        self.Interval = self.MaxNumber / 12
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,25)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,25)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["2008","2009","2010","2011","2012"]
        self.YAxisLabel = ["Annual rainfall in cm"]
        self.XAxisLabel = [""]
        self.YearIndex = randint(0,4)
        self.problem = "The annual rainfall in a city  for a 5-year period is recorded in the bar graph below. "
        self.problem = self.problem + "In which year did the city receive %d cm of rainfall?<br>"%(self.heights[self.YearIndex])
        height = self.heights[self.YearIndex]
        self.answer = self.BarNames[self.YearIndex]
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
        self.BarTitle = json.dumps("Annual rainfall for a 5-year period")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2b(self.problem,self.answer,self.unit,height)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType2b(self,problem,answer,unit,height):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d cm is the height of the bar for the year %s.<br><br>So, the city received %d cm of rainfall in the year <b>%s</b>."%(height,answer,height,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
                        
    def GenerateProblemTypeMCQ2c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ2c'
        self.CheckAnswerType = 1
        self.MaxNumber = 600
        self.Interval = self.MaxNumber / 12
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,25)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,25)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["2008","2009","2010","2011","2012"]
        self.YAxisLabel = ["Annual rainfall in cm"]
        self.XAxisLabel = [""]
        self.YearIndices = random.sample([0,1,2,3,4],2)
        self.diff = self.heights[self.YearIndices[0]] - self.heights[self.YearIndices[1]] 
        self.problem = "The annual rainfall in a city for a 5-year period is recorded in the bar graph below. "
        if self.diff > 0:
            self.problem = self.problem + "In which year did the city receive %d cm less rainfall than in %s?<br>"%(self.diff,self.BarNames[self.YearIndices[0]])
        else:
            self.problem = self.problem + "In which year did the city receive %d cm more rainfall than in %s?<br>"%(abs(self.diff),self.BarNames[self.YearIndices[0]])
        year1 = self.BarNames[self.YearIndices[0]]
        self.answer = self.BarNames[self.YearIndices[1]]
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
        self.BarTitle = json.dumps("Annual rainfall for a 5-year period")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2c(self.problem,self.answer,self.unit,self.heights[self.YearIndices[0]],year1,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType2c(self,problem,answer,unit,amount1,year1,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Amount of rainfall received in %s &nbsp;=&nbsp; %d cm<br><br>"%(year1,amount1)
        if diff > 0:
            self.solution_text = self.solution_text + "%d cm less than %d cm &nbsp;=&nbsp; "%(abs(diff),amount1)
            self.solution_text = self.solution_text + "%d cm &nbsp;&minus;&nbsp; %d cm &nbsp;=&nbsp; %d cm<br><br>"%(amount1,abs(diff),amount1-abs(diff))
            self.solution_text = self.solution_text + "%d cm is the height of the bar for the year %s.<br><br>"%(amount1-abs(diff),str(answer))
            self.solution_text = self.solution_text + "In <b>%s</b> the city received %d cm less rainfall than in %s."%(str(answer),abs(diff),year1)
        else:
            self.solution_text = self.solution_text + "%d cm more than %d cm &nbsp;=&nbsp; "%(abs(diff),amount1)
            self.solution_text = self.solution_text + "%d cm &nbsp;+&nbsp; %d cm &nbsp;=&nbsp; %d cm<br><br>"%(abs(diff),amount1,amount1+abs(diff))
            self.solution_text = self.solution_text + "%d cm is the height of the bar for the year %s.<br><br>"%(amount1+abs(diff),str(answer))
            self.solution_text = self.solution_text + "In <b>%s</b> the city received %d cm more rainfall than in %s."%(str(answer),abs(diff),year1)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ2d(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ2d'
        self.CheckAnswerType = 1
        self.MaxNumber = 600
        self.Interval = self.MaxNumber / 12
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,25)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,25)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["2008","2009","2010","2011","2012"]
        self.YAxisLabel = ["Annual rainfall in cm"]
        self.XAxisLabel = [""]
        self.YearIndices = random.sample([0,1,2,3,4],2)
        self.diff = self.heights[self.YearIndices[0]] - self.heights[self.YearIndices[1]] 
        self.problem = "The annual rainfall in a city  for a 5-year period is recorded in the bar graph below. "
        if self.diff > 0:
            self.problem = self.problem + "How much more rainfall was recorded for %s than for %s?<br>"%(self.BarNames[self.YearIndices[0]],self.BarNames[self.YearIndices[1]])
        else:
            self.problem = self.problem + "How much less rainfall was recorded for %s than for %s?<br>"%(self.BarNames[self.YearIndices[0]],self.BarNames[self.YearIndices[1]])
        year1 = self.BarNames[self.YearIndices[0]]
        year2 = self.BarNames[self.YearIndices[1]]
        self.answer = str(abs(self.diff))+ " cm"
        self.wrongAnswers = []
        self.wrongAnswers.append(str(abs(self.diff)+50)+ " cm")
        self.wrongAnswers.append(str(abs(self.diff)+100)+ " cm")
        self.wrongAnswers.append(str(abs(self.diff)-50)+ " cm")
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Annual rainfall for a 5-year period")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2d(self.problem,self.answer,self.unit,self.heights[self.YearIndices[0]],self.heights[self.YearIndices[1]],year1,year2,self.diff)        
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType2d(self,problem,answer,unit,amount1,amount2,year1,year2,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        if diff > 0:
            self.solution_text = self.solution_text + "Amount of rainfall recorded for %s &nbsp;=&nbsp; %d cm<br><br>"%(year1,amount1)
            self.solution_text = self.solution_text + "Amount of rainfall recorded for %s &nbsp;=&nbsp; %d cm<br><br>"%(year2,amount2)
            self.solution_text = self.solution_text + "%d cm &nbsp;&minus;&nbsp; %d cm &nbsp;=&nbsp; %s<br><br>"%(amount1,amount2,answer)
            self.solution_text = self.solution_text + "There was <b>%s</b> more rainfall recorded for %s than for %s."%(answer,year1,year2)
        else:
            self.solution_text = self.solution_text + "Amount of rainfall recorded for %s &nbsp;=&nbsp; %d cm<br><br>"%(year1,amount1)
            self.solution_text = self.solution_text + "Amount of rainfall recorded for %s &nbsp;=&nbsp; %d cm<br><br>"%(year2,amount2)
            self.solution_text = self.solution_text + "%d cm &nbsp;&minus;&nbsp; %d cm &nbsp;=&nbsp; %s<br><br>"%(amount2,amount1,answer)
            self.solution_text = self.solution_text + "There was <b>%s</b> less rainfall recorded for %s than for %s."%(answer,year1,year2)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ2e(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ2e'
        self.CheckAnswerType = 1
        self.MaxNumber = 600
        self.Interval = self.MaxNumber / 12
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,50)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,50)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["2008","2009","2010","2011","2012"]
        self.YAxisLabel = ["Annual rainfall in cm"]
        self.XAxisLabel = [""]
        self.problem = "The annual rainfall in a city  for a 5-year period is recorded in the bar graph below. "
        self.problem = self.problem + "What is the total rainfall recorded for the given 5-year period?<br>"
        year1 = self.BarNames[0]
        year2 = self.BarNames[1]
        year3 = self.BarNames[2]
        year4 = self.BarNames[3]
        year5 = self.BarNames[4]
        self.answer = str(self.heights[0]+self.heights[1]+self.heights[2]+self.heights[3]+self.heights[4])+" cm"
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.heights[0]+self.heights[1]+self.heights[2]+self.heights[3]+self.heights[4]+50)+ " cm")
        self.wrongAnswers.append(str(self.heights[0]+self.heights[1]+self.heights[2]+self.heights[3]+self.heights[4]+100)+ " cm")
        self.wrongAnswers.append(str(self.heights[0]+self.heights[1]+self.heights[2]+self.heights[3]+self.heights[4]-50)+ " cm")
        self.wrongAnswers.append(str(self.heights[0]+self.heights[1]+self.heights[2]+self.heights[3]+self.heights[4]-100)+ " cm")
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Annual rainfall for a 5-year period")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2e(self.problem,self.answer,self.unit,self.heights[0],self.heights[1],self.heights[2],self.heights[3],self.heights[4],year1,year2,year3,year4,year5)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType2e(self,problem,answer,unit,amount1,amount2,amount3,amount4,amount5,year1,year2,year3,year4,year5):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Amount of rainfall recorded for %s &nbsp;=&nbsp; %d cm<br>"%(year1,amount1)
        self.solution_text = self.solution_text + "Amount of rainfall recorded for %s &nbsp;=&nbsp; %d cm<br>"%(year2,amount2)
        self.solution_text = self.solution_text + "Amount of rainfall recorded for %s &nbsp;=&nbsp; %d cm<br>"%(year3,amount3)
        self.solution_text = self.solution_text + "Amount of rainfall recorded for %s &nbsp;=&nbsp; %d cm<br>"%(year4,amount4)
        self.solution_text = self.solution_text + "Amount of rainfall recorded for %s &nbsp;=&nbsp; %d cm<br><br>"%(year5,amount5)
        self.solution_text = self.solution_text + "%d cm &nbsp;+&nbsp; %d cm &nbsp;+&nbsp; %d cm &nbsp;+&nbsp; %d cm &nbsp;+&nbsp; %d cm &nbsp;=&nbsp; %s<br><br>"%(amount1,amount2,amount3,amount4,amount5,answer)
        self.solution_text = self.solution_text + "Total rainfall recorded for the 5-year period is %s."%(answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemTypeMCQ3a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ3a'
        self.CheckAnswerType = 1
        self.MaxNumber = 400
        self.Interval = self.MaxNumber / 8
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        self.friends = random.sample(PersonName.PersonName,5)
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,25)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,25)
            except ValueError:
                pass
            self.heights.append(self.height)

        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = self.friends
        self.YAxisLabel = ["Points   scored"]
        self.XAxisLabel = [""]
        self.problem = "Five friends played a video game and scored some points. Their scores are shown in the bar graph below. "
        self.problem = self.problem + "Who scored the fewest points in the video game?<br>"
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
        self.BarTitle = json.dumps("Points scored in a video game")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3a(self.problem,self.answer,self.unit,min(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType3a(self,problem,answer,unit,minPoints):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The shortest bar in the graph is for %s (%d points).<br><br>So, <b>%s</b> scored the fewest points in the video game."%(str(answer),minPoints,str(answer))
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemTypeMCQ3b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ3b'
        self.CheckAnswerType = 1
        self.MaxNumber = 400
        self.Interval = self.MaxNumber / 8
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        self.friends = random.sample(PersonName.PersonName,5)
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,25)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,25)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = self.friends
        self.YAxisLabel = ["Points   scored"]
        self.XAxisLabel = [""]
        self.problem = "Five friends played a video game and scored some points. Their scores are shown in the bar graph below. "
        self.problem = self.problem + "Who scored the most points in the video game?<br>"
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
        self.BarTitle = json.dumps("Points scored in a video game")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3b(self.problem,self.answer,self.unit,max(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType3b(self,problem,answer,unit,maxPoints):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The tallest bar in the graph is for %s (%d points).<br><br>So, <b>%s</b> scored the most points in the video game."%(str(answer),maxPoints,str(answer))
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemTypeMCQ3c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ3c'
        self.CheckAnswerType = 1
        self.MaxNumber = 400
        self.Interval = self.MaxNumber / 8
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        self.friends = random.sample(PersonName.PersonName,5)
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,25)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,25)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = self.friends
        self.YAxisLabel = ["Points   scored"]
        self.XAxisLabel = [""]
        self.PersonIndex = randint(0,4)
        self.problem = "Five friends played a video game and scored some points. Their scores are shown in the bar graph below. "
        self.problem = self.problem + "How many points did %s score?"%(self.friends[self.PersonIndex])
        self.answer = self.heights[self.PersonIndex]
        self.wrongAnswers = []
        for i in range(len(self.BarNames)):
            if self.heights[i]!=self.answer:
                self.wrongAnswers.append(self.heights[i])
        self.wrongAnswers.append(self.answer+25)
        self.wrongAnswers.append(self.answer-25)
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Points scored in a video game")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3c(self.problem,self.answer,self.unit,self.friends[self.PersonIndex])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType3c(self,problem,answer,unit,name):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The height of the bar for %s is %d.<br><br>So, %s scored <b>%d</b> points."%(name,answer,name,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ3d(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ3d'
        self.CheckAnswerType = 1
        self.MaxNumber = 400
        self.Interval = self.MaxNumber / 8
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        self.friends = random.sample(PersonName.PersonName,5)
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,25)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,25)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = self.friends
        self.YAxisLabel = ["Points   scored"]
        self.XAxisLabel = [""]
        self.PersonIndex = randint(0,4)
        self.problem = "Five friends played a video game and scored some points. Their scores are shown in the bar graph below. "
        self.problem = self.problem + "Who scored %d points in the video game?<br>"%(self.heights[self.PersonIndex])
        self.answer = self.friends[self.PersonIndex]
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
        self.BarTitle = json.dumps("Points scored in a video game")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3d(self.problem,self.answer,self.unit,self.heights[self.PersonIndex])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType3d(self,problem,answer,unit,score):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d is the height of the bar for %s.<br><br>So, <b>%s</b> scored %d points in the video game."%(score,answer,answer,score)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
                        
    def GenerateProblemTypeMCQ3e(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ3e'
        self.CheckAnswerType = 1
        self.MaxNumber = 400
        self.Interval = self.MaxNumber / 8
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        self.friends = random.sample(PersonName.PersonName,5)
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,25)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,25)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = self.friends
        self.YAxisLabel = ["Points   scored"]
        self.XAxisLabel = [""]
        self.PersonIndices = random.sample([0,1,2,3,4],2)
        self.diff = self.heights[self.PersonIndices[0]] - self.heights[self.PersonIndices[1]]
        self.problem = "Five friends played a video game and scored some points. Their scores are shown in the bar graph below. "
        if self.diff > 0:
            self.problem = self.problem + "How many more points should %s score to equal %s's score?<br>"%(self.friends[self.PersonIndices[1]],self.friends[self.PersonIndices[0]])
        else:
            self.problem = self.problem + "How many more points should %s score to equal %s's score?<br>"%(self.friends[self.PersonIndices[0]],self.friends[self.PersonIndices[1]])
        self.answer = abs(self.diff)
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+25)
        self.wrongAnswers.append(self.answer-25)
        self.wrongAnswers.append(self.answer+50)
        
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Points scored in a video game")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3e(self.problem,self.answer,self.unit,self.heights[self.PersonIndices[0]],self.heights[self.PersonIndices[1]],self.friends[self.PersonIndices[1]],self.friends[self.PersonIndices[0]],self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType3e(self,problem,answer,unit,score1,score2,name1,name2,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        if diff > 0:
            self.solution_text = self.solution_text + "%s's score &nbsp;=&nbsp; %d<br><br>"%(name2,score1)
            self.solution_text = self.solution_text + "%s's score &nbsp;=&nbsp; %d<br><br>"%(name1,score2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(score1,score2,answer)
            self.solution_text = self.solution_text + "%s should score %d more points to equal %s's score."%(name1,answer,name2)
        else:
            self.solution_text = self.solution_text + "%s's score &nbsp;=&nbsp; %d<br><br>"%(name1,score2)
            self.solution_text = self.solution_text + "%s's score &nbsp;=&nbsp; %d<br><br>"%(name2,score1)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(score2,score1,answer)
            self.solution_text = self.solution_text + "%s should score %d more points to equal %s's score."%(name2,answer,name1)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
 
    def GenerateProblemTypeMCQ4a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ4a'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["T-shirts","shirts","tops","blouses","coats"]
        self.YAxisLabel = ["Number  of  pieces"]
        self.XAxisLabel = [""]
        self.ClothIndex = randint(0,4)
        self.problem = random.choice(PersonName.AuntyName)+" has a fashion store. The number of each type of clothing in her store is shown in the graph below. "
        self.problem = self.problem + "How many %s does she have in her store?<br>"%(self.BarNames[self.ClothIndex])
        article = self.BarNames[self.ClothIndex]
        self.answer = self.heights[self.ClothIndex]
        self.wrongAnswers = []
        for i in range(len(self.BarNames)):
            if self.heights[i]!=self.answer:
                self.wrongAnswers.append(self.heights[i])
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer-10)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Clothing in the fashion store")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4a(self.problem,self.answer,self.unit,article)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType4a(self,problem,answer,unit,article):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The height of the bar for %s is %d.<br><br>She has <b>%d</b> %s in her store."%(article,answer,answer,article)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            

    def GenerateProblemTypeMCQ4b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ4b'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["T-shirts","shirts","tops","blouses","coats"]
        self.YAxisLabel = ["Number  of  pieces"]
        self.XAxisLabel = [""]
        self.ClothIndices = random.sample([0,1,2,3,4],2)
        self.diff = self.heights[self.ClothIndices[0]] - self.heights[self.ClothIndices[1]]
        self.problem = random.choice(PersonName.AuntyName)+" has a fashion store. The number of each type of clothing in her store is shown in the graph below. "
        if self.diff > 0:
            self.problem = self.problem + "How many more %s than %s are there in her store?<br>"%(self.BarNames[self.ClothIndices[0]],self.BarNames[self.ClothIndices[1]])
        else:
            self.problem = self.problem + "How many fewer %s than %s are there in her store?<br>"%(self.BarNames[self.ClothIndices[0]],self.BarNames[self.ClothIndices[1]])
        article1 = self.BarNames[self.ClothIndices[0]]
        article2 = self.BarNames[self.ClothIndices[1]]
        count1 = self.heights[self.ClothIndices[0]]
        count2 = self.heights[self.ClothIndices[1]]
        self.answer = abs(self.diff)
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer-10)
        self.wrongAnswers.append(self.answer+20)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Clothing in the fashion store")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4b(self.problem,self.answer,self.unit,article1,article2,count1,count2,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType4b(self,problem,answer,unit,article1,article2,count1,count2,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        if diff > 0:
            self.solution_text = self.solution_text + "Number of %s &nbsp;=&nbsp; %d<br><br>"%(article1,count1)
            self.solution_text = self.solution_text + "Number of %s &nbsp;=&nbsp; %d<br><br>"%(article2,count2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count1,count2,answer)
            self.solution_text = self.solution_text + "She has <b>%d</b> more %s than %s in her store."%(answer,article1,article2)
        else:
            self.solution_text = self.solution_text + "Number of %s &nbsp;=&nbsp; %d<br><br>"%(article2,count2)
            self.solution_text = self.solution_text + "Number of %s &nbsp;=&nbsp; %d<br><br>"%(article1,count1)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count2,count1,answer)
            self.solution_text = self.solution_text + "She has <b>%d</b> fewer %s than %s in her store."%(answer,article1,article2)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemTypeMCQ5a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ5a'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*5,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*5,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri"]
        self.Days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.YAxisLabel = [""]
        self.XAxisLabel = ["Number  of  workers"]
        self.DayIndex = randint(0,4)
        self.problem = "The bar graph shows the number of workers who came to the factory from Monday to Friday. "
        self.problem = self.problem + "How many workers came to the factory on %s?<br>"%(self.Days[self.DayIndex])
        self.answer = self.heights[self.DayIndex]
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer-10)
        self.wrongAnswers.append(self.answer+20)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Workers who came to the factory over 5 days")
        
        self.FunctionCall = "P3DrawBarGraph2("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"

        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5a(self.problem,self.answer,self.unit,self.Days[self.DayIndex])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType5a(self,problem,answer,unit,day):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The length of the bar for %s is %d.<br><br>So, <b>%d</b> workers came to the factory on %s."%(day,answer,answer,day)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ5b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ5b'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*5,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*5,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri"]
        self.Days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.YAxisLabel = [""]
        self.XAxisLabel = ["Number  of  workers"]
        self.DayIndex = randint(0,4)
        self.problem = "The bar graph shows the number of workers who came to the factory from Monday to Friday. "
        self.problem = self.problem + "On which day did the factory have the fewest workers?<br>"
        
        self.answer = self.Days[self.BarHeights.index(min(self.BarHeights))]
        self.wrongAnswers = []
        for i in range(len(self.Days)):
            if self.Days[i]!=self.answer:
                self.wrongAnswers.append(self.Days[i])
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Workers who came to the factory over 5 days")
        
        self.FunctionCall = "P3DrawBarGraph2("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5b(self.problem,self.answer,self.unit,min(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType5b(self,problem,answer,unit,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The shortest bar in the graph is for %s (%d workers).<br><br>So, the factory had the fewest workers on <b>%s</b>."%(answer,count,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ5c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ5c'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*5,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*5,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri"]
        self.Days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.YAxisLabel = [""]
        self.XAxisLabel = ["Number  of  workers"]
        self.DayIndex = randint(0,4)
        self.problem = "The bar graph shows the number of workers who came to the factory from Monday to Friday. "
        self.problem = self.problem + "On which day did the factory have the most workers?<br>"
        
        self.answer = self.Days[self.BarHeights.index(max(self.BarHeights))]
        self.wrongAnswers = []
        for i in range(len(self.Days)):
            if self.Days[i]!=self.answer:
                self.wrongAnswers.append(self.Days[i])
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Workers who came to the factory over 5 days")
        
        self.FunctionCall = "P3DrawBarGraph2("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"

        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5c(self.problem,self.answer,self.unit,max(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType5c(self,problem,answer,unit,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The longest bar in the graph is for %s (%d workers).<br><br>So, the factory had the most workers on <b>%s</b>."%(answer,count,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ5d(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ5d'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*5,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*5,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri"]
        self.Days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.YAxisLabel = [""]
        self.XAxisLabel = ["Number  of  workers"]
        self.DayIndices = random.sample([0,1,2,3,4],2)
        self.diff = self.heights[self.DayIndices[0]] - self.heights[self.DayIndices[1]]
        self.problem = "The bar graph shows the number of workers who came to the factory from Monday to Friday. Study the graph and then fill in the blank below. <br><br>"
        if self.diff > 0:
            self.problem = self.problem + "There were %d more workers at the factory on  ____________  than on %s."%(abs(self.diff),self.Days[self.DayIndices[1]])
        else:
            self.problem = self.problem + "There were %d fewer workers at the factory on  ____________  than on %s."%(abs(self.diff),self.Days[self.DayIndices[1]])
        self.answer = self.Days[self.DayIndices[0]]
        self.wrongAnswers = []
        for i in range(len(self.Days)):
            if self.Days[i]!=self.answer:
                self.wrongAnswers.append(self.Days[i])
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Workers who came to the factory over 5 days")
        
        self.FunctionCall = "P3DrawBarGraph2("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5d(self.problem,self.answer,self.unit,self.Days[self.DayIndices[1]],self.heights[self.DayIndices[1]],self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType5d(self,problem,answer,unit,day,count,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        if diff > 0:
            self.solution_text = self.solution_text + "Number of workers on %s &nbsp;=&nbsp; %d<br><br>"%(day,count)
            self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count,abs(diff),count+abs(diff))
            self.solution_text = self.solution_text + "%d is the length of the bar for %s.<br><br>"%(count+abs(diff),answer)
            self.solution_text = self.solution_text + "There were %d more workers at the factory on <b><u>%s</u></b> than on %s.<br><br>"%(abs(diff),answer,day)
        else:
            self.solution_text = self.solution_text + "Number of workers on %s &nbsp;=&nbsp; %d<br><br>"%(day,count)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count,abs(diff),count-abs(diff))
            self.solution_text = self.solution_text + "%d is the length of the bar for %s.<br><br>"%(count-abs(diff),answer)
            self.solution_text = self.solution_text + "There were %d fewer workers at the factory on <b><u>%s</u></b> than on %s.<br><br>"%(abs(diff),answer,day)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ6a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ6a'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Fiction","Comic","Educational","Science","Language"]
        self.YAxisLabel = ["Number  of  books"]
        self.XAxisLabel = [""]
        self.BookIndex = randint(0,4)
        self.problem = "The following bar graph shows the number of books in various categories in a kids' library. "
        self.problem = self.problem + "How many books are there in the %s category?<br>"%(self.BarNames[self.BookIndex])
        BookCategory = self.BarNames[self.BookIndex]
        self.answer = self.heights[self.BookIndex]
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer-10)
        self.wrongAnswers.append(self.answer+20)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Books in a kids' library")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6a(self.problem,self.answer,self.unit,BookCategory)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType6a(self,problem,answer,unit,category):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The height of the bar for %s is %d.<br><br>So, there are <b>%d</b> books in the %s category."%(category,answer,answer,category)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ6b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ6b'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Fiction","Comic","Educational","Science","Language"]
        self.YAxisLabel = ["Number  of  books"]
        self.XAxisLabel = [""]
        self.BookIndex = randint(0,4)
        self.problem = "The following bar graph shows the number of books in various categories in a kids' library. "
        self.problem = self.problem + "Which category of books are the most common books in the library?<br>"
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
        self.BarTitle = json.dumps("Books in a kids' library")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6b(self.problem,self.answer,self.unit,min(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType6b(self,problem,answer,unit,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The tallest bar in the graph is for %s (%s books).<br><br>So, <b>%s</b> books are the most common books in the library."%(answer,count,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ6c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ6c'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Fiction","Comic","Educational","Science","Language"]
        self.YAxisLabel = ["Number  of  books"]
        self.XAxisLabel = [""]
        self.BookIndex = randint(0,4)
        self.problem = "The following bar graph shows the number of books in various categories in a kids' library. "
        self.problem = self.problem + "Which category of books are the least common books in the library?<br>"
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
        self.BarTitle = json.dumps("Books in a kids' library")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6c(self.problem,self.answer,self.unit,min(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType6c(self,problem,answer,unit,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The shortest bar in the graph is for %s (%s books).<br><br>So, <b>%s</b> books are the least common books in the library."%(answer,count,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ6d(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ6d'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Fiction","Comic","Educational","Science","Language"]
        self.YAxisLabel = ["Number  of  books"]
        self.XAxisLabel = [""]
        self.BookIndices = random.sample([0,1,2,3,4],2)
        self.diff = self.heights[self.BookIndices[0]] - self.heights[self.BookIndices[1]]
        self.problem = "Study the bar graph below and fill in the blank.<br><br>"
        if self.diff > 0:
            self.problem = self.problem + "There are _____ more books under the %s category than under the %s category.<br>"%(self.BarNames[self.BookIndices[0]],self.BarNames[self.BookIndices[1]])
        else:
            self.problem = self.problem + "There are _____ fewer books under the %s category than under the %s category.<br>"%(self.BarNames[self.BookIndices[0]],self.BarNames[self.BookIndices[1]])
            
        category1 = self.BarNames[self.BookIndices[0]]
        category2 = self.BarNames[self.BookIndices[1]]
        self.answer = abs(self.diff)
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer-10)
        self.wrongAnswers.append(self.answer+20)
        self.wrongAnswers.append(self.answer+30)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Categories of books in a kids' library")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6d(self.problem,self.answer,self.unit,category1,category2,self.heights[self.BookIndices[0]],self.heights[self.BookIndices[1]],self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType6d(self,problem,answer,unit,category1,category2,count1,count2,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        if diff > 0:
            self.solution_text = self.solution_text + "Number of books in the %s category &nbsp;=&nbsp; %d<br>"%(category1,count1)
            self.solution_text = self.solution_text + "Number of books in the %s category &nbsp;=&nbsp; %d<br><br>"%(category2,count2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count1,count2,answer)
            self.solution_text = self.solution_text + "There are <b>%d</b> more books in the %s category than in the %s category.<br><br>"%(answer,category1,category2)
        else:
            self.solution_text = self.solution_text + "Number of books in the %s category &nbsp;=&nbsp; %d<br>"%(category1,count1)
            self.solution_text = self.solution_text + "Number of books in the %s category &nbsp;=&nbsp; %d<br><br>"%(category2,count2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count2,count1,answer)
            self.solution_text = self.solution_text + "There are <b>%d</b> fewer books in the %s category than in the %s category.<br><br>"%(answer,category1,category2)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemTypeMCQ7a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["red","blue","orange","pink","purple"]
        self.problem_type = 'ProblemTypeMCQ7a'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["red","blue","orange","pink","purple"]
        self.YAxisLabel = [""]
        self.XAxisLabel = ["Number  of  pupils"]
        self.ColourIndex = randint(0,4)
        self.problem = "A survey conducted by a school shows the favourite colours of its pupils in the graph below. "
        self.problem = self.problem + "Which is the least popular colour among the pupils?<br>"
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
        self.colours = json.dumps(self.colours)
        self.BarTitle = json.dumps("Survey results showing the favourite colours of pupils")
        
        self.FunctionCall = "P3DrawBarGraph2("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"

        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7a(self.problem,self.answer,self.unit,min(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType7a(self,problem,answer,unit,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The shortest bar in the graph is for %s (%d pupils).<br><br>So, <b>%s</b> is the least popular colour among the pupils."%(answer,count,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ7b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["red","blue","orange","pink","purple"]
        self.problem_type = 'ProblemTypeMCQ7b'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["red","blue","orange","pink","purple"]
        self.YAxisLabel = [""]
        self.XAxisLabel = ["Number  of  pupils"]
        self.ColourIndex = randint(0,4)
        self.problem = "A survey conducted by a school shows the favourite colours of its pupils in the graph below. "
        self.problem = self.problem + "Which is the most popular colour among the pupils?<br>"
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
        self.colours = json.dumps(self.colours)
        self.BarTitle = json.dumps("Survey results showing the favourite colours of pupils")
        
        self.FunctionCall = "P3DrawBarGraph2("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7b(self.problem,self.answer,self.unit,max(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType7b(self,problem,answer,unit,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The longest bar in the graph is for %s (%d pupils).<br><br>So, <b>%s</b> is the most popular colour among the pupils."%(answer,count,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ7c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["red","blue","orange","pink","purple"]
        self.problem_type = 'ProblemTypeMCQ7c'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["red","blue","orange","pink","purple"]
        self.ColourNames = ["red","blue","orange","pink","purple"]
        self.YAxisLabel = [""]
        self.XAxisLabel = ["Number  of  pupils"]
        self.ColourIndex = randint(0,4)
        self.GirlsLike = (self.heights[self.ColourIndex] * 6)/10
        self.BoysLike = self.heights[self.ColourIndex] - self.GirlsLike
        self.problem = "A survey conducted by a school shows the favourite colours of its pupils in the graph below. "
        self.problem = self.problem + "If %d girls chose %s as their favourite colour, how many boys chose %s as their favourite colour?<br>"%(self.GirlsLike,self.BarNames[self.ColourIndex],
                                                                                                                                               self.BarNames[self.ColourIndex])
        self.answer = self.BoysLike
        self.wrongAnswers = []
        self.wrongAnswers.append(self.BoysLike+5)
        self.wrongAnswers.append(self.BoysLike-5)
        self.wrongAnswers.append(self.BoysLike+10)
        self.wrongAnswers.append(self.BoysLike-10)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(self.colours)
        self.BarTitle = json.dumps("Survey results showing the favourite colours of pupils")
        
        self.FunctionCall = "P3DrawBarGraph2("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7c(self.problem,self.answer,self.unit,self.ColourNames[self.ColourIndex],self.heights[self.ColourIndex],self.GirlsLike)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType7c(self,problem,answer,unit,colourName,totalLike,girlLike):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Total number of pupils who chose %s as their favourite colour &nbsp;=&nbsp; %d<br><br>"%(colourName,totalLike)
        self.solution_text = self.solution_text + "Number of girls who chose %s as their favourite colour &nbsp;=&nbsp; %d<br><br>"%(colourName,girlLike)
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(totalLike,girlLike,answer)
        self.solution_text = self.solution_text + "<b>%d</b> boys chose %s as their favourite colour.<br><br>"%(answer,colourName)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ7d(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["red","blue","orange","pink","purple"]
        self.problem_type = 'ProblemTypeMCQ7d'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["red","blue","orange","pink","purple"]
        self.YAxisLabel = [""]
        self.XAxisLabel = ["Number  of  pupils"]
        self.problem = "A survey conducted by a school shows the favourite colours of its pupils in the graph below. "
        self.problem = self.problem + "How many pupils are there in the school altogether?<br>"
        self.answer = self.heights[0]+self.heights[1]+self.heights[2]+self.heights[3]+self.heights[4]
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+15)
        self.wrongAnswers.append(self.answer-15)
        self.wrongAnswers.append(self.answer+20)
        self.wrongAnswers.append(self.answer-20)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(self.colours)
        self.BarTitle = json.dumps("Survey results showing the favourite colours of pupils")
        
        self.FunctionCall = "P3DrawBarGraph2("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7d(self.problem,self.answer,self.unit,self.heights[0],self.heights[1],self.heights[2],self.heights[3],self.heights[4])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType7d(self,problem,answer,unit,amount1,amount2,amount3,amount4,amount5):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Total number of pupils in the school<br>=&nbsp; Total number of pupils who took the survey<br>"
        self.solution_text = self.solution_text + "=&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;<br>=&nbsp; %d<br><br>"%(amount1,amount2,amount3,amount4,amount5,answer)
        self.solution_text = self.solution_text + "There are <b>%d</b> pupils in the school altogether."%(answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ8a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ8a'
        self.CheckAnswerType = 1
        self.MaxNumber = 150
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*6,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = random.sample(PersonName.PersonName,5)
        self.YAxisLabel = ["Amount  of  money  in  $"]
        self.XAxisLabel = [""]
        self.NameIndex = randint(0,4)
        self.problem = "The following bar graph shows the amount of money saved by %s, %s, %s, %s and %s in their piggy banks. "%(self.BarNames[0],self.BarNames[1],self.BarNames[2],
                                                                                                                        self.BarNames[3],self.BarNames[4])
        self.problem = self.problem + "Who saved $%d?<br>"%(self.heights[self.NameIndex])
        self.answer = self.BarNames[self.NameIndex]
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
        self.BarTitle = json.dumps("Amount of money saved by 5 people")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8a(self.problem,self.answer,self.unit,self.heights[self.NameIndex])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType8a(self,problem,answer,unit,amount):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d is the height of the bar for %s.<br><br>So, <b>%s</b> saved $%d."%(amount,answer,answer,amount)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ8b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ8b'
        self.CheckAnswerType = 1
        self.MaxNumber = 150
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*6,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = random.sample(PersonName.PersonName,5)
        self.YAxisLabel = ["Amount  of  money  in  $"]
        self.XAxisLabel = [""]
        self.NameIndex = randint(0,4)
        self.problem = "The following bar graph shows the amount of money saved by %s, %s, %s, %s and %s in their piggy banks. "%(self.BarNames[0],self.BarNames[1],self.BarNames[2],
                                                                                                                        self.BarNames[3],self.BarNames[4])
        self.problem = self.problem + "Who saved the most amount of money?<br>"
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
        self.BarTitle = json.dumps("Amount of money saved by 5 people")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8b(self.problem,self.answer,self.unit,max(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType8b(self,problem,answer,unit,amount):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The tallest bar in the graph is for %s ($%d).<br><br>So, <b>%s</b> saved the most amount of money."%(answer,amount,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ8c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ8c'
        self.CheckAnswerType = 1
        self.MaxNumber = 150
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*6,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = random.sample(PersonName.PersonName,5)
        self.YAxisLabel = ["Amount  of  money  in  $"]
        self.XAxisLabel = [""]
        self.NameIndex = randint(0,4)
        self.problem = "The following bar graph shows the amount of money saved by %s, %s, %s, %s and %s in their piggy banks. "%(self.BarNames[0],self.BarNames[1],self.BarNames[2],
                                                                                                                        self.BarNames[3],self.BarNames[4])
        self.problem = self.problem + "Who saved the least amount of money?"
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
        self.BarTitle = json.dumps("Amount of money saved by 5 people")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8c(self.problem,self.answer,self.unit,min(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType8c(self,problem,answer,unit,amount):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The shortest bar in the graph is for %s ($%d).<br><br>So, <b>%s</b> saved the least amount of money."%(answer,amount,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ8d(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ8d'
        self.CheckAnswerType = 1
        self.MaxNumber = 150
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*6,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = random.sample(PersonName.PersonName,5)
        self.YAxisLabel = ["Amount  of  money  in  $"]
        self.XAxisLabel = [""]
        self.NameIndices = random.sample([0,1,2,3,4],2)
        self.diff = self.heights[self.NameIndices[0]] - self.heights[self.NameIndices[1]]
        self.problem = "The following bar graph shows the amount of money saved by %s, %s, %s, %s and %s in their piggy banks. "%(self.BarNames[0],self.BarNames[1],self.BarNames[2],
                                                                                                                        self.BarNames[3],self.BarNames[4])
        if self.diff > 0:
            self.problem = self.problem + "How much more money should %s save to equal %s's savings?<br>"%(self.BarNames[self.NameIndices[1]],self.BarNames[self.NameIndices[0]])
        else:
            self.problem = self.problem + "How much more money should %s save to equal %s's savings?<br>"%(self.BarNames[self.NameIndices[0]],self.BarNames[self.NameIndices[1]])
        
        name1 = self.BarNames[self.NameIndices[0]]
        name2 = self.BarNames[self.NameIndices[1]]
        amount1 = self.heights[self.NameIndices[0]]
        amount2 = self.heights[self.NameIndices[1]]
        
        self.answer = abs(self.diff)
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+5)
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer+15)
        self.wrongAnswers.append(self.answer-5)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Amount of money saved by 5 people")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8d(self.problem,self.answer,self.unit,name1,name2,amount1,amount2,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType8d(self,problem,answer,unit,name1,name2,amount1,amount2,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        if diff > 0:
            self.solution_text = self.solution_text + "%s's savings &nbsp;=&nbsp; $%d<br><br>"%(name1,amount1)
            self.solution_text = self.solution_text + "%s's savings &nbsp;=&nbsp; $%d<br><br>"%(name2,amount2)
            self.solution_text = self.solution_text + "$%d &nbsp;&minus;&nbsp; $%d &nbsp;=&nbsp; $%d<br><br>"%(amount1,amount2,answer)
            self.solution_text = self.solution_text + "%s should save another $%d to equal %s's savings."%(name2,answer,name1)
        else:
            self.solution_text = self.solution_text + "%s's savings &nbsp;=&nbsp; $%d<br><br>"%(name2,amount2)
            self.solution_text = self.solution_text + "%s's savings &nbsp;=&nbsp; $%d<br><br>"%(name1,amount1)
            self.solution_text = self.solution_text + "$%d &nbsp;&minus;&nbsp; $%d &nbsp;=&nbsp; $%d<br><br>"%(amount2,amount1,answer)
            self.solution_text = self.solution_text + "%s should save another $%d to equal %s's savings."%(name1,answer,name2)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ8e(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ8e'
        self.CheckAnswerType = 1
        self.MaxNumber = 150
        self.Interval = self.MaxNumber / 15
        self.Bars = 5
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*6,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = random.sample(PersonName.PersonName,5)
        self.YAxisLabel = ["Amount  of  money  in  $"]
        self.XAxisLabel = [""]
        self.NameIndices = random.sample([0,1,2,3,4],2)
        self.problem = "The following bar graph shows the amount of money saved by %s, %s, %s, %s and %s in their piggy banks. "%(self.BarNames[0],self.BarNames[1],self.BarNames[2],self.BarNames[3],self.BarNames[4])
        self.problem = self.problem + "What is the total amount of money saved by %s and %s?<br>"%(self.BarNames[self.NameIndices[0]],self.BarNames[self.NameIndices[1]])
        
        name1 = self.BarNames[self.NameIndices[0]]
        name2 = self.BarNames[self.NameIndices[1]]
        amount1 = self.heights[self.NameIndices[0]]
        amount2 = self.heights[self.NameIndices[1]]

        self.answer = self.heights[self.NameIndices[0]] + self.heights[self.NameIndices[1]]
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+5)
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer+15)
        self.wrongAnswers.append(self.answer-5)
        self.wrongAnswers.append(self.answer-10)
        self.wrongAnswers.append(self.answer-15)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Amount of money saved by 5 people")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8e(self.problem,self.answer,self.unit,name1,name2,amount1,amount2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType8e(self,problem,answer,unit,name1,name2,amount1,amount2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Amount of money saved by %s &nbsp;=&nbsp; $%d<br>"%(name1,amount1)
        self.solution_text = self.solution_text + "Amount of money saved by %s &nbsp;=&nbsp; $%d<br><br>"%(name2,amount2)
        self.solution_text = self.solution_text + "$%d &nbsp;+&nbsp; $%d &nbsp;=&nbsp; $%d<br><br>"%(amount1,amount2,answer)
        self.solution_text = self.solution_text + "Total money saved by %s and %s is $%d."%(name1,name2,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemTypeMCQ9a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ9a'
        self.CheckAnswerType = 1
        self.MaxNumber = 600
        self.Interval = self.MaxNumber / 15
        self.Bars = 7
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*6,self.MaxNumber,20)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,20)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        self.Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.YAxisLabel = ["Number   of   visitors"]
        self.XAxisLabel = [""]
        self.DayIndex = randint(0,6)
        self.problem = "The bar graph below represents the number of visitors to the Natural History Museum last week. "
        self.problem = self.problem + "How many people visited the museum on %s?<br>"%(self.Days[self.DayIndex])
        
        self.answer = self.heights[self.DayIndex]
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+20)
        self.wrongAnswers.append(self.answer+30)
        self.wrongAnswers.append(self.answer+40)
        self.wrongAnswers.append(self.answer-20)
        self.wrongAnswers.append(self.answer-40)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Visitors to the Natural History Museum last week")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9a(self.problem,self.answer,self.unit,self.Days[self.DayIndex])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType9a(self,problem,answer,unit,day):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The height of the bar for %s is %d.<br><br>So, <b>%d</b> people visited the museum on %s."%(day,answer,answer,day)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ9b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ9b'
        self.CheckAnswerType = 1
        self.MaxNumber = 600
        self.Interval = self.MaxNumber / 15
        self.Bars = 7
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars-1):
            self.height = random.randrange(self.Interval*6,self.MaxNumber,20)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,20)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars-1):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        '''Adding one day with 0 visitors'''
        self.BarHeights.append([0,0])
        random.shuffle(self.BarHeights)
        
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        self.Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.YAxisLabel = ["Number   of   visitors"]
        self.XAxisLabel = [""]
        self.DayIndex = randint(0,6)
        self.problem = "The bar graph below represents the number of visitors to the Natural History Museum last week. "
        self.problem = self.problem + "On which day was the museum closed?<br>"
        
        self.answer = self.Days[self.BarHeights.index(min(self.BarHeights))]
        self.wrongAnswers = []
        for i in range(len(self.Days)):
            if self.Days[i]!=self.answer:
                self.wrongAnswers.append(self.Days[i])
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Visitors to the Natural History Museum last week")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9b(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType9b(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The height of the bar for %s is 0.<br><br>So, the museum was closed on <b>%s</b>."%(answer,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ9c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ9c'
        self.CheckAnswerType = 1
        self.MaxNumber = 600
        self.Interval = self.MaxNumber / 15
        self.Bars = 7
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*6,self.MaxNumber,20)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,20)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        self.Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.YAxisLabel = ["Number   of   visitors"]
        self.XAxisLabel = [""]
        self.DayIndices = random.sample([0,1,2,3,4,5,6],2)
        self.problem = "The bar graph below represents the number of visitors to the Natural History Museum last week. "
        self.diff = self.heights[self.DayIndices[0]] - self.heights[self.DayIndices[1]]
        if self.diff > 0:
            self.problem = self.problem + "How many more people visited the museum on %s than on %s?<br>"%(self.Days[self.DayIndices[0]],self.Days[self.DayIndices[1]])
        else:
            self.problem = self.problem + "How many fewer people visited the museum on %s than on %s?<br>"%(self.Days[self.DayIndices[0]],self.Days[self.DayIndices[1]])
        
        self.answer = abs(self.diff)
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+20)
        self.wrongAnswers.append(self.answer+30)
        self.wrongAnswers.append(self.answer+40)
        self.wrongAnswers.append(self.answer-20)
        self.wrongAnswers.append(self.answer-40)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Visitors to the Natural History Museum last week")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9c(self.problem,self.answer,self.unit,self.heights[self.DayIndices[0]],self.heights[self.DayIndices[1]],self.Days[self.DayIndices[0]],self.Days[self.DayIndices[1]],self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType9c(self,problem,answer,unit,count1,count2,day1,day2,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        if diff > 0:
            self.solution_text = self.solution_text + "Number of visitors on %s &nbsp;=&nbsp; %d<br><br>"%(day1,count1)
            self.solution_text = self.solution_text + "Number of visitors on %s &nbsp;=&nbsp; %d<br><br>"%(day2,count2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count1,count2,answer)
            self.solution_text = self.solution_text + "<b>%d</b> more people visited the museum on %s than on %s."%(answer,day1,day2)
        else:
            self.solution_text = self.solution_text + "Number of visitors on %s &nbsp;=&nbsp; %d<br><br>"%(day1,count1)
            self.solution_text = self.solution_text + "Number of visitors on %s &nbsp;=&nbsp; %d<br><br>"%(day2,count2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count2,count1,answer)
            self.solution_text = self.solution_text + "<b>%d</b> fewer people visited the museum on %s than on %s."%(answer,day1,day2)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ9d(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ9d'
        self.CheckAnswerType = 1
        self.MaxNumber = 600
        self.Interval = self.MaxNumber / 15
        self.Bars = 7
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*6,self.MaxNumber,20)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,20)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        self.Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.YAxisLabel = ["Number   of   visitors"]
        self.XAxisLabel = [""]
        self.problem = "The bar graph below represents the number of visitors to the Natural History Museum last week. "
        self.problem = self.problem + "Which was the busiest day at the museum in terms of number of visitors?<br>"
        
        self.answer = self.Days[self.BarHeights.index(max(self.BarHeights))]
        self.wrongAnswers = []
        for i in range(len(self.Days)):
            if self.Days[i]!=self.answer:
                self.wrongAnswers.append(self.Days[i])
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Visitors to the Natural History Museum last week")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9d(self.problem,self.answer,self.unit,max(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType9d(self,problem,answer,unit,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The tallest bar in the graph is for %s (%d visitors).<br><br>So, <b>%s</b> was the busiest day at the museum."%(answer,count,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ9e(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ9e'
        self.CheckAnswerType = 1
        self.MaxNumber = 600
        self.Interval = self.MaxNumber / 15
        self.Bars = 7
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*6,self.MaxNumber,20)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*3,self.MaxNumber,20)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        self.Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.YAxisLabel = ["Number   of   visitors"]
        self.XAxisLabel = [""]
        self.DayIndex = randint(0,6)
        self.adults = (self.heights[self.DayIndex]*6)/10
        self.children = self.heights[self.DayIndex] - self.adults
        self.problem = "The bar graph below represents the number of visitors to the Natural History Museum last week. "
        self.problem = self.problem + "If %d adults visited the museum on %s, how many children visited the museum that day?<br>"%(self.adults,self.Days[self.DayIndex])
        
        self.answer = self.children
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+5)
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer-15)
        self.wrongAnswers.append(self.answer-10)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Visitors to the Natural History Museum last week")
        
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9e(self.problem,self.answer,self.unit,self.Days[self.DayIndex],self.heights[self.DayIndex],self.adults)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType9e(self,problem,answer,unit,day,totalCount,adultCount):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Total number of visitors on %s &nbsp;=&nbsp; %d<br><br>"%(day,totalCount)
        self.solution_text = self.solution_text + "Number of adults visiting on %s &nbsp;=&nbsp; %d<br><br>"%(day,adultCount)
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(totalCount,adultCount,answer)
        self.solution_text = self.solution_text + "<b>%d</b> children visited the museum on %s.<br><br>"%(answer,day)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemTypeMCQ10a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ10a'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 20
        self.Bars = 6
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*8,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*8,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = []
        for _i in range(self.Bars):
            self.UncleName = random.choice(PersonName.ShortUncleName)
            while self.UncleName in self.BarNames or len(self.UncleName)>7:
                self.UncleName = random.choice(PersonName.ShortUncleName)
            self.BarNames.append(self.UncleName)
        
        self.YAxisLabel = ["Number   of   hours"]
        self.XAxisLabel = [""]
        self.problem = "%s, %s, %s, %s, %s and %s work in an office. The following bar graph shows the number of hours each of them worked last month. "%(self.BarNames[0],self.BarNames[1],self.BarNames[2],self.BarNames[3],self.BarNames[4],self.BarNames[5])
        self.problem = self.problem + "Who worked the most number of hours last month?<br>"
        
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
        self.BarTitle = json.dumps("Number of hours that 6 employees worked last month")
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10a(self.problem,self.answer,self.unit,max(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType10a(self,problem,answer,unit,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The tallest bar in the graph is for %s (%d hours).<br><br>So, <b>%s</b> worked the most number of hours last month."%(answer,count,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ10b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ10b'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 20
        self.Bars = 6
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*8,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*8,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = []
        for _i in range(self.Bars):
            self.UncleName = random.choice(PersonName.ShortUncleName)
            while self.UncleName in self.BarNames or len(self.UncleName)>7:
                self.UncleName = random.choice(PersonName.ShortUncleName)
            self.BarNames.append(self.UncleName)
        
        self.YAxisLabel = ["Number   of   hours"]
        self.XAxisLabel = [""]
        self.UncleIndices = random.sample([0,1,2,3,4,5],2)
        self.diff = self.heights[self.UncleIndices[0]] - self.heights[self.UncleIndices[1]]
        self.problem = "%s, %s, %s, %s, %s and %s work in an office. The following bar graph shows the number of hours each of them worked last month. "%(self.BarNames[0],self.BarNames[1],self.BarNames[2],self.BarNames[3],self.BarNames[4],self.BarNames[5])
        if self.diff > 0:
            self.problem = self.problem + "How many more hours did %s work than %s last month?"%(self.BarNames[self.UncleIndices[0]],self.BarNames[self.UncleIndices[1]])
        else:
            self.problem = self.problem + "How many fewer hours did %s work than %s last month?"%(self.BarNames[self.UncleIndices[0]],self.BarNames[self.UncleIndices[1]])
        
        uncle1 = self.BarNames[self.UncleIndices[0]]
        uncle2 = self.BarNames[self.UncleIndices[1]]
        hours1 = self.heights[self.UncleIndices[0]]
        hours2 = self.heights[self.UncleIndices[1]]
        self.answer = abs(self.diff)
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer-10)
        self.wrongAnswers.append(self.answer+20)
        self.wrongAnswers.append(self.answer+15)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Number of hours that 6 employees worked last month")
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10b(self.problem,self.answer,self.unit,uncle1,uncle2,hours1,hours2,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType10b(self,problem,answer,unit,uncle1,uncle2,hours1,hours2,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        if diff > 0:
            self.solution_text = self.solution_text + "Number of hours that %s worked &nbsp;=&nbsp; %d<br><br>"%(uncle1,hours1)
            self.solution_text = self.solution_text + "Number of hours that %s worked &nbsp;=&nbsp; %d<br><br>"%(uncle2,hours2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(hours1,hours2,answer)
            self.solution_text = self.solution_text + "%s worked <b>%d</b> more hours than %s last month."%(uncle1,answer,uncle2)
        else:
            self.solution_text = self.solution_text + "Number of hours that %s worked &nbsp;=&nbsp; %d<br><br>"%(uncle1,hours1)
            self.solution_text = self.solution_text + "Number of hours that %s worked &nbsp;=&nbsp; %d<br><br>"%(uncle2,hours2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(hours2,hours1,answer)
            self.solution_text = self.solution_text + "%s worked <b>%d</b> fewer hours than %s last month."%(uncle1,answer,uncle2)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ10c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ10c'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 20
        self.Bars = 6
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*8,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*8,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = []
        for _i in range(self.Bars):
            self.UncleName = random.choice(PersonName.ShortUncleName)
            while self.UncleName in self.BarNames or len(self.UncleName)>7:
                self.UncleName = random.choice(PersonName.ShortUncleName)
            self.BarNames.append(self.UncleName)
        
        self.YAxisLabel = ["Number   of   hours"]
        self.XAxisLabel = [""]
        self.problem = "%s, %s, %s, %s, %s and %s work in an office. The following bar graph shows the number of hours each of them worked last month. "%(self.BarNames[0],self.BarNames[1],self.BarNames[2],self.BarNames[3],self.BarNames[4],self.BarNames[5])
        self.problem = self.problem + "Who worked the fewest number of hours last month?<br>"
        
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
        self.BarTitle = json.dumps("Number of hours that 6 employees worked last month")
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10c(self.problem,self.answer,self.unit,min(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType10c(self,problem,answer,unit,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The shortest bar in the graph is for %s (%d hours).<br><br>So, <b>%s</b> worked the fewest number of hours last month."%(answer,count,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ10d(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ10d'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 20
        self.Bars = 6
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*8,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*8,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = []
        for _i in range(self.Bars):
            self.UncleName = random.choice(PersonName.ShortUncleName)
            while self.UncleName in self.BarNames or len(self.UncleName)>7:
                self.UncleName = random.choice(PersonName.ShortUncleName)
            self.BarNames.append(self.UncleName)
        
        self.YAxisLabel = ["Number   of   hours"]
        self.XAxisLabel = [""]
        self.UncleIndex = randint(0,5)
        self.problem = "%s, %s, %s, %s, %s and %s work in an office. The following bar graph shows the number of hours each of them worked last month. "%(self.BarNames[0],self.BarNames[1],self.BarNames[2],self.BarNames[3],self.BarNames[4],self.BarNames[5])
        self.problem = self.problem + "Who worked for %d hours last month?<br>"%(self.heights[self.UncleIndex])
        
        self.answer = self.BarNames[self.UncleIndex]
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
        self.BarTitle = json.dumps("Number of hours that 6 employees worked last month")
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10d(self.problem,self.answer,self.unit,self.heights[self.UncleIndex])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType10d(self,problem,answer,unit,amount):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d is the height of the bar for %s.<br><br>So, <b>%s</b> worked for %d hours last month."%(amount,answer,answer,amount)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ10e(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ10e'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 20
        self.Bars = 6
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars-1):
            self.height = random.randrange(self.Interval*8,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*8,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars-1):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.SameIndex = randint(0,4)
        self.BarHeights.append(self.BarHeights[self.SameIndex])
        self.BarNames = []
        for _i in range(self.Bars):
            self.UncleName = random.choice(PersonName.ShortUncleName)
            while self.UncleName in self.BarNames or len(self.UncleName)>7:
                self.UncleName = random.choice(PersonName.ShortUncleName)
            self.BarNames.append(self.UncleName)
        
        self.YAxisLabel = ["Number   of   hours"]
        self.XAxisLabel = [""]
        
        self.problem = "%s, %s, %s, %s, %s and %s work in an office. The following bar graph shows the number of hours each of them worked last month. "%(self.BarNames[0],self.BarNames[1],self.BarNames[2],self.BarNames[3],self.BarNames[4],self.BarNames[5])
        self.problem = self.problem + "Which two employees worked for the same number of hours last month?<br>"
        
        sameHourCount = self.heights[self.SameIndex]
        self.answer = self.BarNames[self.SameIndex] +" and "+self.BarNames[5]
        self.wrongAnswers = []
        if self.SameIndex != 4:
            self.wrongAnswers.append(self.BarNames[0] +" and "+self.BarNames[1])
            self.wrongAnswers.append(self.BarNames[2] +" and "+self.BarNames[3])
            self.wrongAnswers.append(self.BarNames[4] +" and "+self.BarNames[5])
        else:
            self.wrongAnswers.append(self.BarNames[0] +" and "+self.BarNames[1])
            self.wrongAnswers.append(self.BarNames[2] +" and "+self.BarNames[3])
            self.wrongAnswers.append(self.BarNames[4] +" and "+self.BarNames[2])           
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Number of hours that 6 employees worked last month")
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10e(self.problem,self.answer,self.unit,sameHourCount)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType10e(self,problem,answer,unit,sameHourCount):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The bars for %s are of the same height (%d hours).<br><br>So, <b>%s</b> worked for the same number of hours last month."%(answer,sameHourCount,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemTypeMCQ11a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ11a'
        self.CheckAnswerType = 1
        self.MaxNumber = 100
        self.Interval = self.MaxNumber / 10
        self.Bars = 6
        self.name = random.choice(PersonName.BoyName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*2,self.MaxNumber,5)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*2,self.MaxNumber,5)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Jan","Feb","Mar","Apr","May","Jun"]
        self.Months = ["January","February","March","April","May","June"]
        
        self.YAxisLabel = ["Number  of  kilometers"]
        self.XAxisLabel = [""]
        self.MonthIndex = randint(0,5)
        self.activity = random.choice([["cycling","cycled","cycle","cycled"],["jogging","jogged","jog","jogged"],["running","ran","run","run"]])
        
        self.problem = "%s loves %s. The following bar graph shows the number of kilometres he %s over a 6-month period. "%(self.name,self.activity[0],self.activity[1])
        self.problem = self.problem + "How far did he %s in the month of %s?<br>"%(self.activity[2],self.Months[self.MonthIndex])
        
        barTitle = "Distance %s by %s over a 6-month period"%(self.activity[3],self.name)
        self.answer = str(self.heights[self.MonthIndex]) + " km"
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.heights[self.MonthIndex]+5)+" km")
        self.wrongAnswers.append(str(self.heights[self.MonthIndex]+10)+" km")
        self.wrongAnswers.append(str(self.heights[self.MonthIndex]-5)+" km")
        self.wrongAnswers.append(str(self.heights[self.MonthIndex]-10)+" km")
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps(barTitle)
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11a(self.problem,self.answer,self.unit,self.Months[self.MonthIndex],self.heights[self.MonthIndex],self.activity[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType11a(self,problem,answer,unit,month,distance,activity):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The height of the bar for %s is %d.<br><br>So, he %s <b>%s</b> in the month of %s."%(month,distance,activity,answer,month)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ11b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ11b'
        self.CheckAnswerType = 1
        self.MaxNumber = 100
        self.Interval = self.MaxNumber / 10
        self.Bars = 6
        self.name = random.choice(PersonName.BoyName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*2,self.MaxNumber,5)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*2,self.MaxNumber,5)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Jan","Feb","Mar","Apr","May","Jun"]
        self.Months = ["January","February","March","April","May","June"]
        
        self.YAxisLabel = ["Number  of  kilometers"]
        self.XAxisLabel = [""]
        self.MonthIndex = randint(0,5)
        self.activity = random.choice([["cycling","cycled","cycle","cycled"],["jogging","jogged","jog","jogged"],["running","ran","run","run"]])
        
        self.problem = "%s loves %s. The following bar graph shows the number of kilometres he %s over a 6-month period. "%(self.name,self.activity[0],self.activity[1])
        self.problem = self.problem + "In which month did he %s %d km?<br>"%(self.activity[2],self.heights[self.MonthIndex])
        
        barTitle = "Distance %s by %s over a 6-month period"%(self.activity[3],self.name)
        self.answer = self.BarNames[self.MonthIndex]
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
        self.BarTitle = json.dumps(barTitle)
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11b(self.problem,self.answer,self.unit,self.heights[self.MonthIndex],self.activity[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType11b(self,problem,answer,unit,distance,activity):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d is the height of the bar for %s.<br><br>So, he %s %d km in <b>%s</b>."%(distance,answer,activity,distance,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ11c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ11c'
        self.CheckAnswerType = 1
        self.MaxNumber = 100
        self.Interval = self.MaxNumber / 10
        self.Bars = 6
        self.name = random.choice(PersonName.BoyName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*2,self.MaxNumber,5)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*2,self.MaxNumber,5)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Jan","Feb","Mar","Apr","May","Jun"]
        self.Months = ["January","February","March","April","May","June"]
        
        self.YAxisLabel = ["Number  of  kilometers"]
        self.XAxisLabel = [""]
        self.MonthIndex = randint(0,5)
        self.activity = random.choice([["cycling","cycled","cycle","cycled"],["jogging","jogged","jog","jogged"],["running","ran","run","run"]])
        
        self.problem = "%s loves %s. The following bar graph shows the number of kilometres he %s over a 6-month period. "%(self.name,self.activity[0],self.activity[1])
        self.problem = self.problem + "In which month did he %s the furthest?<br>"%(self.activity[2])
        
        barTitle = "Distance %s by %s over a 6-month period"%(self.activity[3],self.name)
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
        self.BarTitle = json.dumps(barTitle)
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11c(self.problem,self.answer,self.unit,max(self.heights),self.activity[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType11c(self,problem,answer,unit,distance,activity):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The tallest bar in the graph is for %s (%d km).<br><br>So, he %s the furthest in <b>%s</b>."%(answer,distance,activity,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ11d(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ11d'
        self.CheckAnswerType = 1
        self.MaxNumber = 100
        self.Interval = self.MaxNumber / 10
        self.Bars = 6
        self.name = random.choice(PersonName.BoyName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*2,self.MaxNumber,5)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*2,self.MaxNumber,5)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Jan","Feb","Mar","Apr","May","Jun"]
        self.Months = ["January","February","March","April","May","June"]
        
        self.YAxisLabel = ["Number  of  kilometers"]
        self.XAxisLabel = [""]
        self.MonthIndex = randint(0,5)
        self.activity = random.choice([["cycling","cycled","cycle","cycled"],["jogging","jogged","jog","jogged"],["running","ran","run","run"]])
        
        self.problem = "%s loves %s. The following bar graph shows the number of kilometres he %s over a 6-month period. "%(self.name,self.activity[0],self.activity[1])
        self.problem = self.problem + "In which month did he %s the shortest distance?<br>"%(self.activity[2])
        
        barTitle = "Distance %s by %s over a 6-month period"%(self.activity[3],self.name)
        self.answer = self.Months[self.BarHeights.index(min(self.BarHeights))]
        self.wrongAnswers = []
        for i in range(len(self.Months)):
            if self.Months[i]!=self.answer:
                self.wrongAnswers.append(self.Months[i])           
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps(barTitle)
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11d(self.problem,self.answer,self.unit,min(self.heights),self.activity[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType11d(self,problem,answer,unit,distance,activity):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The shortest bar in the graph is for %s (%d km).<br><br>So, he %s the shortest distance in <b>%s</b>."%(answer,distance,activity,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ11e(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ11e'
        self.CheckAnswerType = 1
        self.MaxNumber = 100
        self.Interval = self.MaxNumber / 10
        self.Bars = 6
        self.name = random.choice(PersonName.BoyName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for _i in range(self.Bars):
            self.height = random.randrange(self.Interval*2,self.MaxNumber,5)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*2,self.MaxNumber,5)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Jan","Feb","Mar","Apr","May","Jun"]
        self.Months = ["January","February","March","April","May","June"]
        
        self.YAxisLabel = ["Number  of  kilometers"]
        self.XAxisLabel = [""]
        self.MonthIndex = randint(0,5)
        self.activity = random.choice([["cycling","cycled","cycle","cycled"],["jogging","jogged","jog","jogged"],["running","ran","run","run"]])
        
        self.problem = "%s loves %s. The following bar graph shows the number of kilometres he %s over a 6-month period. "%(self.name,self.activity[0],self.activity[1])
        self.problem = self.problem + "How much distance did he %s altogether in the 6-month period?<br>"%(self.activity[2])
        
        barTitle = "Distance %s by %s over a 6-month period"%(self.activity[3],self.name)
        self.answer = str(self.heights[0]+self.heights[1]+self.heights[2]+self.heights[3]+self.heights[4]+self.heights[5]) + " km"
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.heights[0]+self.heights[1]+self.heights[2]+self.heights[3]+self.heights[4]+self.heights[5]+10) + " km")           
        self.wrongAnswers.append(str(self.heights[0]+self.heights[1]+self.heights[2]+self.heights[3]+self.heights[4]+self.heights[5]-10) + " km")
        self.wrongAnswers.append(str(self.heights[0]+self.heights[1]+self.heights[2]+self.heights[3]+self.heights[4]+self.heights[5]+15) + " km")
        self.wrongAnswers.append(str(self.heights[0]+self.heights[1]+self.heights[2]+self.heights[3]+self.heights[4]+self.heights[5]-15) + " km")
        self.wrongAnswers.append(str(self.heights[0]+self.heights[1]+self.heights[2]+self.heights[3]+self.heights[4]+self.heights[5]+20) + " km")
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps(barTitle)
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11e(self.problem,self.answer,self.unit,self.heights[0],self.heights[1],self.heights[2],self.heights[3],self.heights[4],self.heights[5],self.activity[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType11e(self,problem,answer,unit,amount1,amount2,amount3,amount4,amount5,amount6,activity):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Distance %s in January &nbsp;=&nbsp; %d km<br>"%(activity,amount1)
        self.solution_text = self.solution_text + "Distance %s in February &nbsp;=&nbsp; %d km<br>"%(activity,amount2)
        self.solution_text = self.solution_text + "Distance %s in March &nbsp;=&nbsp; %d km<br>"%(activity,amount3)
        self.solution_text = self.solution_text + "Distance %s in April &nbsp;=&nbsp; %d km<br>"%(activity,amount4)
        self.solution_text = self.solution_text + "Distance %s in May &nbsp;=&nbsp; %d km<br>"%(activity,amount5)
        self.solution_text = self.solution_text + "Distance %s in June &nbsp;=&nbsp; %d km<br><br>"%(activity,amount6)
        
        self.solution_text = self.solution_text + "%d km &nbsp;+&nbsp; %d km &nbsp;+&nbsp; %d km &nbsp;+&nbsp; %d km &nbsp;+&nbsp; %d km &nbsp;+&nbsp; %d km &nbsp;=&nbsp; %s<br><br>"%(amount1,amount2,amount3,amount4,amount5,amount6,str(answer))
        self.solution_text = self.solution_text + "He %s %s in the 6-month period."%(activity,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ12a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ12a'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.BoyName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars):
            '''making sure that sports car are not too many'''
            if i == 4:
                self.height = random.randrange(self.Interval*2,self.Interval*3,10)
            else:
                self.height = random.randrange(self.Interval*4,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Sedan","SUV","Pickup","Van","Sports"]
        
        self.YAxisLabel = [""]
        self.XAxisLabel = ["Number  of  cars"]
        self.CarIndex = randint(0,4)
        self.cars = ["sedans","SUVs","pickups","vans","sports cars"]
        self.problem = "There are various types of cars parked in a car park. The following bar graph shows the number of cars of each type. "
        self.problem = self.problem + "How many %s are there?"%(self.cars[self.CarIndex])
        
        self.answer = self.heights[self.CarIndex]
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer + 10)           
        self.wrongAnswers.append(self.answer - 10)
        self.wrongAnswers.append(self.answer + 20)
        self.wrongAnswers.append(self.answer - 20)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Types of cars parked in a carpark")
        self.FunctionCall = "P3DrawBarGraph2("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12a(self.problem,self.answer,self.unit,self.cars[self.CarIndex])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType12a(self,problem,answer,unit,carType):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The length of the bar for %s is %d.<br><br>So, there are <b>%d</b> %s."%(carType,answer,answer,carType)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ12b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ12b'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.BoyName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars):
            '''making sure that sports car are not too many'''
            if i == 4:
                self.height = random.randrange(self.Interval*2,self.Interval*3,10)
            else:
                self.height = random.randrange(self.Interval*4,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Sedan","SUV","Pickup","Van","Sports"]
        
        self.YAxisLabel = [""]
        self.XAxisLabel = ["Number  of  cars"]
        self.CarIndices = random.sample([0,1,2,3,4],2)
        self.diff = self.heights[self.CarIndices[0]] - self.heights[self.CarIndices[1]]
        self.cars = ["sedans","SUVs","pickups","vans","sports cars"]
        self.problem = "There are various types of cars parked in a car park. The following bar graph shows the number of cars of each type. "
        if self.diff > 0:
            self.problem = self.problem + "How many more %s than %s are there?"%(self.cars[self.CarIndices[0]],self.cars[self.CarIndices[1]])
        else:
            self.problem = self.problem + "How many fewer %s than %s are there?"%(self.cars[self.CarIndices[0]],self.cars[self.CarIndices[1]])
        
        self.answer = abs(self.diff)
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer + 10)           
        self.wrongAnswers.append(self.answer - 10)
        self.wrongAnswers.append(self.answer + 20)
        self.wrongAnswers.append(self.answer + 15)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Types of cars parked in a carpark")
        self.FunctionCall = "P3DrawBarGraph2("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12b(self.problem,self.answer,self.unit,self.cars[self.CarIndices[0]],self.cars[self.CarIndices[1]],self.heights[self.CarIndices[0]],self.heights[self.CarIndices[1]],self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType12b(self,problem,answer,unit,car1,car2,count1,count2,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        if diff > 0:
            self.solution_text = self.solution_text + "Number of %s &nbsp;=&nbsp; %d<br><br>"%(car1,count1)
            self.solution_text = self.solution_text + "Number of %s &nbsp;=&nbsp; %d<br><br>"%(car2,count2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count1,count2,answer)
            self.solution_text = self.solution_text + "There are <b>%d</b> more %s than %s."%(answer,car1,car2)
        else:
            self.solution_text = self.solution_text + "Number of %s &nbsp;=&nbsp; %d<br><br>"%(car1,count1)
            self.solution_text = self.solution_text + "Number of %s &nbsp;=&nbsp; %d<br><br>"%(car2,count2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count2,count1,answer)
            self.solution_text = self.solution_text + "There are <b>%d</b> fewer %s than %s."%(answer,car1,car2)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ12c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ12c'
        self.CheckAnswerType = 1
        self.MaxNumber = 200
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.BoyName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars):
            '''making sure that sports car are not too many'''
            if i == 4:
                self.height = random.randrange(self.Interval*2,self.Interval*3,10)
            else:
                self.height = random.randrange(self.Interval*4,self.MaxNumber,10)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,10)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Sedan","SUV","Pickup","Van","Sports"]
        
        self.YAxisLabel = [""]
        self.XAxisLabel = ["Number  of  cars"]
        self.cars = ["sedans","SUVs","pickups","vans","sports cars"]
        self.black = (self.heights[4] * randint(3,7))/10
        self.red = self.heights[4] - self.black
        self.problem = "There are various types of cars parked in a car park. The following bar graph shows the number of cars of each type. "
        self.problem = self.problem + "There are only two colours of sports cars in the car park: Black and Red. If there are %d black sports cars, how many sports cars are red in colour?"%(self.black)
        
        self.answer = self.red
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer + 10)           
        self.wrongAnswers.append(self.answer - 5)
        self.wrongAnswers.append(self.answer + 5)
        self.wrongAnswers.append(self.heights[4])
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Types of cars parked in a carpark")
        self.FunctionCall = "P3DrawBarGraph2("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12c(self.problem,self.answer,self.unit,self.heights[4],self.black)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType12c(self,problem,answer,unit,totalSports,black):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The length of the bar for sports cars is %d.<br><br>"%(totalSports)
        self.solution_text = self.solution_text + "So, total number of sports cars &nbsp;=&nbsp; %d<br><br>"%(totalSports)
        self.solution_text = self.solution_text + "Number of black sports cars &nbsp;=&nbsp; %d<br><br>"%(black)
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(totalSports,black,answer)
        self.solution_text = self.solution_text + "There are <b>%d</b> sports cars that are red in colour.<br><br>"%(answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ13a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ13a'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.UncleName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars):
            self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Games","Cars","Puzzles","Baby","Dolls"]
        bartitle = "Toys in %s's toys shop"%(self.name)
        
        self.YAxisLabel = ["Number   of   toys"]
        self.XAxisLabel = [""]
        
        self.ToyIndex = randint(0,4)
        self.problem = "%s counted the number of toys in each category in his toys shop. The result is shown in the following bar graph. "%(self.name)
        self.problem = self.problem + "How many toys are there in the %s category?"%(self.BarNames[self.ToyIndex])
        
        category = self.BarNames[self.ToyIndex]
        self.answer = self.heights[self.ToyIndex]
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer + 15)           
        self.wrongAnswers.append(self.answer - 15)
        self.wrongAnswers.append(self.answer + 5)
        self.wrongAnswers.append(self.answer - 5)
       
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps(bartitle)
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13a(self.problem,self.answer,self.unit,category)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType13a(self,problem,answer,unit,category):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The height of the bar for %s is %d.<br><br>So, there are <b>%d</b> toys in the %s category."%(category,answer,answer,category)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ13b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ13b'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.UncleName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars):
            self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Games","Cars","Puzzles","Baby","Dolls"]
        self.ToyNames = ["Games","Cars","Puzzles","Baby Toys","Dolls"]
        bartitle = "Toys in %s's toys shop"%(self.name)
        
        self.YAxisLabel = ["Number   of   toys"]
        self.XAxisLabel = [""]
        
        self.ToyIndex = randint(0,4)
        self.problem = "%s counted the number of toys in each category in his toys shop. The result is shown in the following bar graph. "%(self.name)
        self.problem = self.problem + "Which are the most common toys in the shop?"
        
        self.answer = self.ToyNames[self.BarHeights.index(max(self.BarHeights))]
        self.wrongAnswers = []
        for i in range(len(self.ToyNames)):
            if self.ToyNames[i]!=self.answer:
                self.wrongAnswers.append(self.ToyNames[i])
               
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps(bartitle)
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13b(self.problem,self.answer,self.unit,max(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType13b(self,problem,answer,unit,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The tallest bar in the graph is for %s (%d toys).<br><br>So, <b>%s</b> are the most common toys in the shop."%(answer,count,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ13c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ13c'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.UncleName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars):
            self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Games","Cars","Puzzles","Baby","Dolls"]
        self.ToyNames = ["Games","Cars","Puzzles","Baby Toys","Dolls"]
        bartitle = "Toys in %s's toys shop"%(self.name)
        
        self.YAxisLabel = ["Number   of   toys"]
        self.XAxisLabel = [""]
        
        self.ToyIndex = randint(0,4)
        self.problem = "%s counted the number of toys in each category in his toys shop. The result is shown in the following bar graph. "%(self.name)
        self.problem = self.problem + "Which are the least common toys in the shop?"
        
        self.answer = self.ToyNames[self.BarHeights.index(min(self.BarHeights))]
        self.wrongAnswers = []
        for i in range(len(self.ToyNames)):
            if self.ToyNames[i]!=self.answer:
                self.wrongAnswers.append(self.ToyNames[i])
               
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps(bartitle)
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13c(self.problem,self.answer,self.unit,min(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType13c(self,problem,answer,unit,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The shortest bar in the graph is for %s (%d toys).<br><br>So, <b>%s</b> are the least common toys in the shop."%(answer,count,answer)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ13d(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ13d'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.UncleName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars):
            self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Games","Cars","Puzzles","Baby","Dolls"]
        self.ToyCategory = ["Games","Cars","Puzzles","Baby Toys","Dolls"]
        self.ToyNames = ["games","cars","puzzles","baby toys","dolls"]
        bartitle = "Toys in %s's toys shop"%(self.name)
        
        self.YAxisLabel = ["Number   of   toys"]
        self.XAxisLabel = [""]
        
        self.ToyIndex = randint(0,4)
        self.ToySold = (self.heights[self.ToyIndex] * 6) / 10
        self.problem = "%s counted the number of toys in each category in his toys shop. The result is shown in the following bar graph. "%(self.name)
        self.problem = self.problem + "How many %s will he have left after selling %d of them?<br>"%(self.ToyNames[self.ToyIndex],self.ToySold)
        
        self.answer = self.heights[self.ToyIndex] - self.ToySold
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer + 10)
        self.wrongAnswers.append(self.answer + 20)
        self.wrongAnswers.append(self.answer - 5)
        self.wrongAnswers.append(self.answer - 10)
               
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps(bartitle)
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13d(self.problem,self.answer,self.unit,self.ToyCategory[self.ToyIndex],self.ToyNames[self.ToyIndex],self.heights[self.ToyIndex],self.ToySold)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType13d(self,problem,answer,unit,category,toys,total,sold):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The height of the bar for %s is %d.<br><br>"%(category,total)
        self.solution_text = self.solution_text + "So, total number of %s &nbsp;=&nbsp; %d<br><br>"%(toys,total)
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(total,sold,answer)
        self.solution_text = self.solution_text + "He will have <b>%d</b> %s left.<br><br>"%(answer,toys)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ13e(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ13e'
        self.CheckAnswerType = 1
        self.MaxNumber = 300
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.UncleName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars):
            self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Games","Cars","Puzzles","Baby","Dolls"]
        self.ToyNames = ["games","cars","puzzles","baby toys","dolls"]
        bartitle = "Toys in %s's toys shop"%(self.name)
        
        self.YAxisLabel = ["Number   of   toys"]
        self.XAxisLabel = [""]
        
        self.ToyIndices = random.sample([0,1,2,3,4],2)
        self.diff = self.heights[self.ToyIndices[0]] - self.heights[self.ToyIndices[1]]
        self.problem = "The bar graph below shows the number of different types of toys that %s had in his toys shop. "%(self.name)
        if self.diff > 0:
            self.problem = self.problem + "Then, a customer came to his shop and bought a few %s. In the end, %s had the same number of %s as %s left in his shop. How many %s did the customer buy?<br>"%(self.ToyNames[self.ToyIndices[0]],self.name,self.ToyNames[self.ToyIndices[0]],self.ToyNames[self.ToyIndices[1]],self.ToyNames[self.ToyIndices[0]])
        else:
            self.problem = self.problem + "Then, a customer came to his shop and bought a few %s. In the end, %s had the same number of %s as %s left in his shop. How many %s did the customer buy?<br>"%(self.ToyNames[self.ToyIndices[1]],self.name,self.ToyNames[self.ToyIndices[1]],self.ToyNames[self.ToyIndices[0]],self.ToyNames[self.ToyIndices[1]])
        
        self.answer = abs(self.diff)
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer + 10)
        self.wrongAnswers.append(self.answer + 20)
        self.wrongAnswers.append(self.answer - 5)
        self.wrongAnswers.append(self.answer + 5)
               
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps(bartitle)
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13e(self.problem,self.answer,self.unit,self.ToyNames[self.ToyIndices[0]],self.ToyNames[self.ToyIndices[1]],self.heights[self.ToyIndices[0]],self.heights[self.ToyIndices[1]],self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType13e(self,problem,answer,unit,toy1,toy2,count1,count2,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        if diff > 0:
            self.solution_text = self.solution_text + "Number of %s at first &nbsp;=&nbsp; %d<br><br>"%(toy1,count1)
            self.solution_text = self.solution_text + "Number of %s in the end &nbsp;=&nbsp; Number of %s in the shop &nbsp;=&nbsp; %d<br><br>"%(toy1,toy2,count2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count1,count2,answer)
            self.solution_text = self.solution_text + "The customer bought <b>%d</b> %s."%(answer,toy1)
        else:
            self.solution_text = self.solution_text + "Number of %s at first &nbsp;=&nbsp; %d<br><br>"%(toy2,count2)
            self.solution_text = self.solution_text + "Number of %s in the end &nbsp;=&nbsp; Number of %s in the shop &nbsp;=&nbsp; %d<br><br>"%(toy2,toy1,count1)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count2,count1,answer)
            self.solution_text = self.solution_text + "The customer bought <b>%d</b> %s."%(answer,toy2)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ14a(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ14a'
        self.CheckAnswerType = 1
        self.MaxNumber = 150
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.UncleName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars):
            self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Cherry","Almond","Banana","Mango","Lemon"]
        self.CakeTypes = ["cherry","almond","banana","mango","lemon"]
        
        self.YAxisLabel = ["Number   of   cakes"]
        self.XAxisLabel = [""]

        self.problem = "The following bar graph shows the number of different flavours of cakes that a bakery sold in a certain month. "
        self.problem = self.problem + "Which was the most popular flavour of cake among the bakery's customers?<br>"
        
        maxCake = self.CakeTypes[self.BarHeights.index(max(self.BarHeights))]
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
        self.BarTitle = json.dumps("Cakes sold by a bakery")
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14a(self.problem,self.answer,self.unit,maxCake,max(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType14a(self,problem,answer,unit,cake,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The tallest bar in the graph is for %s (%d cakes).<br><br>So, <b>%s</b>-flavoured cakes were the most popular among the bakery's customers."%(answer,count,cake)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ14b(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ14b'
        self.CheckAnswerType = 1
        self.MaxNumber = 150
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.UncleName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars):
            self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Cherry","Almond","Banana","Mango","Lemon"]
        self.CakeTypes = ["cherry","almond","banana","mango","lemon"]
        
        self.YAxisLabel = ["Number   of   cakes"]
        self.XAxisLabel = [""]

        self.problem = "The following bar graph shows the number of different flavours of cakes that a bakery sold in a certain month. "
        self.problem = self.problem + "Which was the least popular flavour of cake among the bakery's customers?"
        
        minCake = self.CakeTypes[self.BarHeights.index(min(self.BarHeights))]
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
        self.BarTitle = json.dumps("Cakes sold by a bakery")
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14b(self.problem,self.answer,self.unit,minCake,min(self.heights))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType14b(self,problem,answer,unit,cake,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The shortest bar in the graph is for %s (%d cakes).<br><br>So, <b>%s</b>-flavoured cakes were the least popular among the bakery's customers."%(answer,count,cake)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ14c(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ14c'
        self.CheckAnswerType = 1
        self.MaxNumber = 150
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.UncleName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars):
            self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        self.BarNames = ["Cherry","Almond","Banana","Mango","Lemon"]
        self.CakeNames = ["cherry","almond","banana","mango","lemon"]
        
        self.YAxisLabel = ["Number   of   cakes"]
        self.XAxisLabel = [""]
        self.CakeIndices = random.sample([0,1,2,3,4],2)
        self.diff = self.heights[self.CakeIndices[0]] - self.heights[self.CakeIndices[1]]
        self.problem = "The following bar graph shows the number of different flavours of cakes that a bakery sold in a certain month. "
        if self.diff > 0:
            self.problem = self.problem + "How many more %s cakes than %s cakes did the bakery sell?<br>"%(self.CakeNames[self.CakeIndices[0]],self.CakeNames[self.CakeIndices[1]])
        else:
            self.problem = self.problem + "How many fewer %s cakes than %s cakes did the bakery sell?<br>"%(self.CakeNames[self.CakeIndices[0]],self.CakeNames[self.CakeIndices[1]])
        
        self.answer = abs(self.diff)
        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+5)
        self.wrongAnswers.append(self.answer+15)
        self.wrongAnswers.append(self.answer+10)
        self.wrongAnswers.append(self.answer-5)
               
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Cakes sold by a bakery")
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14c(self.problem,self.answer,self.unit,self.CakeNames[self.CakeIndices[0]],self.CakeNames[self.CakeIndices[1]],self.heights[self.CakeIndices[0]],self.heights[self.CakeIndices[1]],self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType14c(self,problem,answer,unit,cake1,cake2,count1,count2,diff):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        if diff > 0:
            self.solution_text = self.solution_text + "Number of %s cakes sold &nbsp;=&nbsp; %d<br><br>"%(cake1,count1)
            self.solution_text = self.solution_text + "Number of %s cakes sold &nbsp;=&nbsp; %d<br><br>"%(cake2,count2)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count1,count2,answer)
            self.solution_text = self.solution_text + "The bakery sold <b>%d</b> more %s cakes than %s cakes."%(answer,cake1,cake2)
        else:
            self.solution_text = self.solution_text + "Number of %s cakes sold &nbsp;=&nbsp; %d<br><br>"%(cake2,count2)
            self.solution_text = self.solution_text + "Number of %s cakes sold &nbsp;=&nbsp; %d<br><br>"%(cake1,count1)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(count2,count1,answer)
            self.solution_text = self.solution_text + "The bakery sold <b>%d</b> fewer %s cakes than %s cakes."%(answer,cake1,cake2)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ14d(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ14d'
        self.CheckAnswerType = 1
        self.MaxNumber = 150
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.UncleName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars-1):
            self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            except ValueError:
                pass
            self.heights.append(self.height)
        self.SameIndex = randint(0,2)
        self.heights.append(self.heights[self.SameIndex])
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        
        self.BarNames = ["Cherry","Almond","Banana","Mango","Lemon"]
        self.CakeNames = ["cherry","almond","banana","mango","lemon"]
        
        self.YAxisLabel = ["Number   of   cakes"]
        self.XAxisLabel = [""]
        self.problem = "The following bar graph shows the number of different flavours of cakes that a bakery sold in a certain month. "
        self.problem = self.problem + "Which two flavours of cakes did the bakery sell in equal numbers?"
        
        equalCakesNames = "%s cakes and %s cakes"%(self.CakeNames[self.SameIndex],self.CakeNames[4])
        self.answer = "%s and %s"%(self.BarNames[self.SameIndex],self.BarNames[4])
        self.wrongAnswers = []
        self.wrongAnswers.append(self.BarNames[0]+" and "+self.BarNames[1])
        self.wrongAnswers.append(self.BarNames[2]+" and "+self.BarNames[3])
        self.wrongAnswers.append(self.BarNames[2]+" and "+self.BarNames[0])
        self.wrongAnswers.append(self.BarNames[3]+" and "+self.BarNames[1])
               
        '''json used to pass the list to javascript function'''
        self.BarHeights = json.dumps(self.BarHeights)
        self.BarNames = json.dumps(self.BarNames)
        self.YAxisLabel = json.dumps(self.YAxisLabel)
        self.XAxisLabel = json.dumps(self.XAxisLabel)
        self.colours = json.dumps(random.sample(self.colours,self.Bars))
        self.BarTitle = json.dumps("Cakes sold by a bakery")
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14d(self.problem,self.answer,self.unit,equalCakesNames,self.heights[self.SameIndex])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            
            
    def ExplainType14d(self,problem,answer,unit,equalCakesNames,sameHourCount):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The bars for %s are of the same height (%d cakes).<br><br>So, the bakery sold an equal number of <b>%s</b>."%(answer,sameHourCount,equalCakesNames)
        self.solution_text = self.solution_text + "</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text

        return self.explain
            
    def GenerateProblemTypeMCQ14e(self):
        '''e.g.:
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.colours = ["coral", "cyan", "magenta","mediumvioletred","royalblue","orange", "deepskyblue", "greenyellow"]
        self.problem_type = 'ProblemTypeMCQ14e'
        self.CheckAnswerType = 1
        self.MaxNumber = 150
        self.Interval = self.MaxNumber / 10
        self.Bars = 5
        self.name = random.choice(PersonName.UncleName)
        '''First number represents the height of the bar, second if 1=draw dotted line, 0=no dotted line'''
        self.BarHeights = []
        self.heights = []
        '''making sure that there is only 1 bar with max value'''
        for i in range(self.Bars):
            self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            try:
                while self.height in self.heights:
                    self.height = random.randrange(self.Interval*4,self.MaxNumber,15)
            except ValueError:
                pass
            self.heights.append(self.height)
        for i in range(self.Bars):
            if (self.heights[i]%self.Interval==0):
                self.dotted = 0
            else:
                self.dotted = 1
            self.BarHeights.append([self.heights[i],self.dotted])
        
        self.BarNames = ["Cherry","Almond","Banana","Mango","Lemon"]
        
        self.YAxisLabel = ["Number   of   cakes"]
        self.XAxisLabel = [""]
        self.CakeIndex = randint(0,4)
        self.problem = "The following bar graph shows the number of different flavours of cakes that a bakery sold in a certain month. Study the graph and fill in the blank below.<br><br>"
        self.problem = self.problem + "The bakery sold %d _______ cakes.<br>"%(self.heights[self.CakeIndex])
        
        self.answer = self.BarNames[self.CakeIndex]
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
        self.BarTitle = json.dumps("Cakes sold by a bakery")
        self.FunctionCall = "P3DrawBarGraph1("+str(self.MaxNumber)+","+str(self.Interval)+","+str(self.Bars)+","+self.BarHeights+","+self.BarNames+","+self.YAxisLabel+","+self.XAxisLabel+","+self.colours+","+self.BarTitle+")"
         
        self.unit = ''
        
        self.template = "DrawBarCharts.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14e(self.problem,self.answer,self.unit,self.heights[self.CakeIndex])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType,self.FunctionCall)            

    def ExplainType14e(self,problem,answer,unit,count):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d is the height of the bar for %s.<br><br>So, the bakery sold %d <b><u>%s</u></b> cakes."%(count,answer,count,answer)
        self.solution_text = self.solution_text + "</font>"
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