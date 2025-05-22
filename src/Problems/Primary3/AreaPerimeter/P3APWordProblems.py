'''
Created on Jan 27, 2014
Module: P3APWordProblems
Generates the Word Problems on Area and Perimeter for Primary 3

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
from Problems import PersonName

class P3APWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType9",],3:["ProblemType2",],4:["ProblemType10",],
                            5:["ProblemType3",],6:["ProblemType11",],7:["ProblemType4",],8:["ProblemType12",],
                            9:["ProblemType5",],10:["ProblemType13",],11:["ProblemType6",],12:["ProblemType14",],
                            13:["ProblemType7",],14:["ProblemType15",],15:["ProblemType8",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType9(),],3:[self.GenerateProblemType2(),],
                                    4:[self.GenerateProblemType10(),],5:[self.GenerateProblemType3(),],6:[self.GenerateProblemType11(),],
                                    7:[self.GenerateProblemType4(),],8:[self.GenerateProblemType12(),],9:[self.GenerateProblemType5(),],
                                    10:[self.GenerateProblemType13(),],11:[self.GenerateProblemType6(),],12:[self.GenerateProblemType14(),],
                                    13:[self.GenerateProblemType7(),],14:[self.GenerateProblemType15(),],15:[self.GenerateProblemType8(),],
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
        #return self.GenerateProblemType15()
        
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
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        self.side = random.randrange(30,100,10)
        self.rounds = randint(3,8)
        self.problem = "%s ran %d rounds of a square ground of side %d m. Find the total distance he ran."%(self.name,self.rounds,self.side)
        
        self.answer = self.rounds * self.side * 4

        self.unit = "m"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit,self.side,self.rounds)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,unit,dollar_unit,length,rounds):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Distance covered in 1 round of the square ground<br>"
        self.solution_text = self.solution_text + "=&nbsp; Perimeter of the square ground<br>"
        self.solution_text = self.solution_text + "=&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d<br>"%(length,length,length,length)
        self.solution_text = self.solution_text + "=&nbsp; %d %s<br><br>"%(length*4,unit)
        
        self.solution_text = self.solution_text + "Distance covered in %d rounds of the square ground<br>"%(rounds)
        self.solution_text = self.solution_text + "=&nbsp; %d &nbsp;&times;&nbsp; %d %s<br>"%(rounds,length*4,unit)
        self.solution_text = self.solution_text + "=&nbsp; %d %s<br><br>"%(answer,unit)
        
        self.solution_text = self.solution_text + "He ran a total distance of %d %s.<br>"%(answer,unit)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        self.length = randint(7,9)
        self.breadth = self.length - randint(1,self.length-5)
        self.perimeter = 2 * (self.length + self.breadth)
        self.InitialLength = (self.perimeter * randint(5,8))/10
        
        self.problem = "%s has %d m of net with him. He is using it to fence up a rectangular garden measuring %d m by %d m. "%(self.name,self.InitialLength,self.length,self.breadth)
        self.problem = self.problem + "How many more metres of net will he need to fence up the garden?"
        
        self.answer = self.perimeter - self.InitialLength

        self.unit = "m"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.dollar_unit,self.length,self.breadth,self.InitialLength)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,unit,dollar_unit,length,breadth,initial):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Total length of net needed to fence up the garden<br>"
        self.solution_text = self.solution_text + "=&nbsp; Perimeter of the rectangular garden<br>"
        self.solution_text = self.solution_text + "=&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d<br>"%(length,breadth,length,breadth)
        self.solution_text = self.solution_text + "=&nbsp; %d %s<br><br>"%(length*2+breadth*2,unit)
        
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d %s<br>"%(length*2+breadth*2,initial,answer,unit)
        
        self.solution_text = self.solution_text + "He will need another %d %s of net to fence up the garden.<br>"%(answer,unit)

        self.solution_text = self.solution_text + "</font>"
       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        self.length = random.randrange(100,200,10)
        self.breadth = self.length - random.randrange(30,60,10)
        self.perimeter = 2 * (self.length + self.breadth)
        self.gap = random.choice([2,5,10])
        
        self.problem = "Farmer %s has a rectangular farm measuring %d m by %d m. He is planting trees around the farm at every %d m. "%(self.name,self.length,self.breadth,self.gap)
        self.problem = self.problem + "How many trees will he need to plant?"
        
        self.answer = self.perimeter / self.gap

        self.unit = "trees"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit,self.dollar_unit,self.length,self.breadth,self.gap)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,unit,dollar_unit,length,breadth,gap):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Distance around the farm<br>"
        self.solution_text = self.solution_text + "=&nbsp; Perimeter of the farm<br>"
        self.solution_text = self.solution_text + "=&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d<br>"%(length,breadth,length,breadth)
        self.solution_text = self.solution_text + "=&nbsp; %d m<br><br>"%(length*2+breadth*2)

        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(length*2+breadth*2,gap,answer)
        
        self.solution_text = self.solution_text + "He will need to plant %d trees.<br>"%(answer)

        self.solution_text = self.solution_text + "</font>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.unit = random.choice(["cm","m"])
        self.breadth = random.randrange(10,40,5)
        self.times = random.choice([["twice",2],["thrice",3],["four times",4],["five times",5]])
        self.length = self.breadth * self.times[1]
        self.perimeter = 2 * (self.length + self.breadth)
        
        self.problem = "The length of a rectangle is %d %s. Its length is %s as long as its breadth. "%(self.length,self.unit,self.times[0])
        self.problem = self.problem + "What is the perimeter of the rectangle?"
        
        self.answer = self.perimeter

        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit,self.dollar_unit,self.length,self.times[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,unit,dollar_unit,length,times):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:54px;'>Breadth</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;Length &nbsp;&divide;&nbsp; %d</div><br>"%(times)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:54px;'></div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d &nbsp;&divide;&nbsp; %d</div><br>"%(length,times)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:54px;'></div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d %s</div><br><br>"%(length/times,unit)

        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:64px;'>Perimeter</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d</div><br>"%(length,length/times,length,length/times)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:64px;'></div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d %s</div><br><br>"%(answer,unit)
        
        self.solution_text = self.solution_text + "The perimeter of the rectangle is %d %s."%(answer,unit)
        self.solution_text = self.solution_text + "</font>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        self.MatchstickLength = randint(4,6)
        self.multiple = randint(3,4)
        self.breadth = self.MatchstickLength * self.multiple
        self.length = self.MatchstickLength * (self.multiple + 1)
        self.perimeter = 2 * (self.length + self.breadth)
        self.NumberofMatchstick = self.perimeter / self.MatchstickLength
        
        self.problem = "%s has %d matchsticks. Each matchstick is %d cm long. "%(self.name,self.NumberofMatchstick,self.MatchstickLength)
        self.problem = self.problem + "She uses the matchsticks to make a rectangle that is %d cm wide. What will be the length of the rectangle she makes?"%(self.breadth)
        
        self.answer = self.length

        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit,self.dollar_unit,self.breadth,self.MatchstickLength,self.NumberofMatchstick)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,unit,dollar_unit,breadth,matchLength,matchCount):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:64px;'>%d &nbsp;&times;&nbsp; %d</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d</div><br>"%(matchCount,matchLength,matchCount*matchLength)
        self.solution_text = self.solution_text + "The perimeter of the rectangle is %d %s.<br><br>"%(matchCount*matchLength,unit)
        
        self.solution_text = self.solution_text + "A rectangle has 2 sides that are called breadth.<br>"
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:64px;'>%d &nbsp;&times;&nbsp; 2</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d</div><br>"%(breadth,breadth*2)
        self.solution_text = self.solution_text + "The 2 breadths are %d %s long altogether.<br><br>"%(breadth*2,unit)
        
        self.solution_text = self.solution_text + "A rectangle has 2 sides that are called length.<br>"
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:64px;'>%d &nbsp;&minus;&nbsp; %d</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d</div><br>"%(matchCount*matchLength,breadth*2,matchCount*matchLength-breadth*2)
        self.solution_text = self.solution_text + "The 2 lengths are %d %s long altogether.<br><br>"%(matchCount*matchLength-breadth*2,unit)

        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:64px;'>%d &nbsp;&divide;&nbsp; 2</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d</div><br>"%(matchCount*matchLength-breadth*2,answer)
        self.solution_text = self.solution_text + "The length of the rectangle she makes is <b>%d %s</b>.<br><br>"%(answer,unit)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.side = randint(5,9)
        self.breadth = self.side
        self.length = 2 * self.side
        self.perimeter = 2 * (self.breadth + self.length)
        
        self.problem = "A carpenter has 2 square wooden tiles of side %d cm each. "%(self.side)
        self.problem = self.problem + "He joins them side by side to make a rectangular tile. Find the perimeter of the rectangular tile."
        
        self.answer = self.perimeter

        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit,self.side)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,unit,dollar_unit,side):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Breadth of the rectangular tile<br>"
        self.solution_text = self.solution_text + "= &nbsp;Length of the side of the square tile<br>"
        self.solution_text = self.solution_text + "= &nbsp;%d %s</div><br><br>"%(side,unit)

        self.solution_text = self.solution_text + "Length of the rectangular tile<br>"
        self.solution_text = self.solution_text + "= &nbsp;Length of the side of the square tile &nbsp;+&nbsp; Length of the side of the square tile<br>"
        self.solution_text = self.solution_text + "= &nbsp;%d &nbsp;+&nbsp; %d</div><br>"%(side,side)
        self.solution_text = self.solution_text + "= &nbsp;%d %s</div><br><br>"%(side*2,unit)

        self.solution_text = self.solution_text + "Perimeter of the rectangular tile<br>"
        self.solution_text = self.solution_text + "= &nbsp;%d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d<br>"%(side,side*2,side,side*2)
        self.solution_text = self.solution_text + "= &nbsp;%d %s</div><br><br>"%(answer,unit)

        self.solution_text = self.solution_text + "The perimeter of the rectangular tile is %d %s."%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.side = randint(5,9)
        self.breadth = self.side
        self.length = 4 * self.side
        self.perimeter = 2 * (self.breadth + self.length)
        
        self.problem = "You have 4 squares each of side %d cm. Join the squares to form a bigger four-sided figure. "%(self.side)
        self.problem = self.problem + "What is the longest possible perimeter that can be got?"
        
        self.answer = self.perimeter

        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.dollar_unit,self.side)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,unit,dollar_unit,side):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Using the 4 squares we can form either a bigger square or a rectangle.<br><br>"
        self.solution_text = self.solution_text + "<u>Figure A</u><br>"
        self.solution_text = self.solution_text + "Let's form a big square using the 4 small squares:<br>"
        self.solution_text = self.solution_text + "Side of the big square<br>"
        self.solution_text = self.solution_text + "= &nbsp;Side of the small square &nbsp;+&nbsp; Side of the small square<br>"
        self.solution_text = self.solution_text + "= &nbsp;%d &nbsp;+&nbsp; %d</div><br>"%(side,side)
        self.solution_text = self.solution_text + "= &nbsp;%d %s</div><br><br>"%(side*2,unit)
        
        self.solution_text = self.solution_text + "Perimeter of the big square<br>"
        self.solution_text = self.solution_text + "= &nbsp;%d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d</div><br>"%(side*2,side*2,side*2,side*2)
        self.solution_text = self.solution_text + "= &nbsp;%d %s</div><br><br><br>"%(side*8,unit)

        self.solution_text = self.solution_text + "<u>Figure B</u><br>"
        self.solution_text = self.solution_text + "Let's form a rectangle by putting the 4 small squares in a row:<br>"
        self.solution_text = self.solution_text + "Length of the rectangle<br>"
        self.solution_text = self.solution_text + "= &nbsp;Side of the small square &nbsp;+&nbsp; Side of the small square &nbsp;+&nbsp; Side of the small square &nbsp;+&nbsp; Side of the small square<br>"
        self.solution_text = self.solution_text + "= &nbsp;%d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d</div><br>"%(side,side,side,side)
        self.solution_text = self.solution_text + "= &nbsp;%d %s</div><br><br>"%(side*4,unit)
        
        self.solution_text = self.solution_text + "Breadth of the rectangle<br>"
        self.solution_text = self.solution_text + "= &nbsp;Side of the small square<br>"
        self.solution_text = self.solution_text + "= &nbsp;%d %s</div><br><br>"%(side,unit)

        self.solution_text = self.solution_text + "Perimeter of the rectangle<br>"
        self.solution_text = self.solution_text + "= &nbsp;%d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d</div><br>"%(side*4,side,side*4,side)
        self.solution_text = self.solution_text + "= &nbsp;%d %s</div><br><br>"%(side*10,unit)
        
        self.solution_text = self.solution_text + "The longest possible perimeter that can be got is <b>%d %s</b>."%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        self.pupils = randint(4,9)
        self.length = random.randrange(12,20,2)
        self.breadth = self.length - random.randrange(4,8,2)
        
        self.perimeter = 2 * (self.breadth + self.length)
        
        self.TotalLength = self.perimeter * self.pupils
        
        self.problem = "%s gives one rectangular card of sides %d cm by %d cm to each of her %d pupils. "%(self.name,self.length,self.breadth,self.pupils)
        self.problem = self.problem + "She wants her pupils to glue a ribbon around their own card. Find the length of the ribbon they will need altogether."
        
        self.answer = self.TotalLength

        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.unit,self.dollar_unit,self.length,self.breadth,self.pupils)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,unit,dollar_unit,length,breadth,pupils):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Perimeter of 1 card<br>"
        self.solution_text = self.solution_text + "=&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d<br>"%(length,breadth,length,breadth)
        self.solution_text = self.solution_text + "=&nbsp; %d %s<br>"%((length+breadth)*2,unit)
        self.solution_text = self.solution_text + "Each pupil needs %d %s of ribbon for their card.<br><br>"%((length+breadth)*2,unit)
        
        self.solution_text = self.solution_text + "%d pupils will need,<br>"%(pupils)
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d %s<br><br>"%(pupils,(length+breadth)*2,answer,unit)
        
        self.solution_text = self.solution_text + "They will need %d %s of ribbon altogether.<br>"%(answer,unit)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.side = randint(7,9)
        self.length = randint(3,5)
        self.breadth = self.length - randint(1,2)
        
        self.RectangleArea = self.length * self.breadth
        self.WallArea = self.side * self.side
        self.UnPaintedArea = self.WallArea - self.RectangleArea
        
        self.problem = "A boy paints a rectangle of %d m by %d m on a square wall of side %d m. "%(self.length,self.breadth,self.side)
        self.problem = self.problem + "What area of the wall is left unpainted?"
        
        self.answer = self.UnPaintedArea

        self.unit = "m<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.unit,self.dollar_unit,self.side,self.length,self.breadth)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,unit,dollar_unit,side,length,breadth):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:100px;'>Area of square</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d &nbsp;&times;&nbsp; %d</div><br>"%(side,side)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:100px;'></div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;'>&nbsp;%d %s</div><br>"%(side*side,unit)
        self.solution_text = self.solution_text + "Total area of the wall is %d %s.<br><br><br>"%(side*side,unit)
        
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:120px;'>Area of rectangle</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d &nbsp;&times;&nbsp; %d</div><br>"%(length,breadth)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:120px;'></div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;'>&nbsp;%d %s</div><br>"%(length*breadth,unit)
        self.solution_text = self.solution_text + "Total painted area on the wall is %d %s.<br><br><br>"%(length*breadth,unit)

        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d %s<br>"%(side*side,length*breadth,answer,unit)
        
        self.solution_text = self.solution_text + "The area of the wall that is left unpainted is %d %s.<br>"%(answer,unit)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        self.side = randint(2,4)
        self.stamps = random.choice([4,9])
        
        self.problem = "%s has %d square stamps of side %d cm each. She glues them onto an envelope to form a bigger square. "%(self.name,self.stamps,self.side)
        self.problem = self.problem + "What area of the envelope does the bigger square cover?"
        
        self.answer = self.side * self.side * self.stamps

        self.unit = "cm<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.unit,self.dollar_unit,self.side,self.stamps)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,unit,dollar_unit,side,stamps):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Side of the bigger square<br>"
        sideCount = 0
        if stamps==4:
            self.solution_text = self.solution_text + "= &nbsp;Side of the small square &nbsp;+&nbsp; Side of the small square<br>"
            self.solution_text = self.solution_text + "= &nbsp;%d &nbsp;+&nbsp; %d</div><br>"%(side,side)
            self.solution_text = self.solution_text + "= &nbsp;%d cm</div><br><br>"%(side*2)
            sideCount = 2
        else:
            self.solution_text = self.solution_text + "= &nbsp;Side of the small square &nbsp;+&nbsp; Side of the small square &nbsp;+&nbsp; Side of the small square<br>"
            self.solution_text = self.solution_text + "= &nbsp;%d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d</div><br>"%(side,side,side)
            self.solution_text = self.solution_text + "= &nbsp;%d cm</div><br><br>"%(side*3)
            sideCount = 3
            
        
        self.solution_text = self.solution_text + "Area of the bigger square<br>"
        self.solution_text = self.solution_text + "= &nbsp;%d &nbsp;&times;&nbsp; %d</div><br>"%(side*sideCount,side*sideCount)
        self.solution_text = self.solution_text + "= &nbsp;%d %s</div><br><br>"%(answer,unit)

        self.solution_text = self.solution_text + "The area of the envelope that the bigger square covers is %d %s.<br>"%(answer,unit)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        self.MatchstickLength = randint(2,3)
        self.NumberofMatchstick = random.choice([8,12])
        self.side = (self.NumberofMatchstick / 4) * self.MatchstickLength 
        
        self.problem = "%s forms a square using %d matchsticks each %d cm long. "%(self.name,self.NumberofMatchstick,self.MatchstickLength)
        self.problem = self.problem + "What is the area covered by the square?"
        
        self.answer = self.side * self.side

        self.unit = "cm<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.unit,self.dollar_unit,self.NumberofMatchstick,self.MatchstickLength)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,unit,dollar_unit,matchCount,matchLength):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Number of matchsticks on each side of the square<br>"
        self.solution_text = self.solution_text + "= &nbsp;%d &nbsp;&divide;&nbsp; 4<br>"%(matchCount)
        self.solution_text = self.solution_text + "= &nbsp;%d<br>"%(matchCount/4)
        self.solution_text = self.solution_text + "There are %d matchsticks on each side of the square.<br><br>"%(matchCount/4)
        
        self.solution_text = self.solution_text + "Length of a side of the square<br>"
        self.solution_text = self.solution_text + "= &nbsp;%d &nbsp;&times;&nbsp; %d cm<br>"%(matchCount/4,matchLength)
        self.solution_text = self.solution_text + "= &nbsp;%d cm<br>"%(matchCount/4*matchLength)
        self.solution_text = self.solution_text + "Each side of the square is %d cm long.<br><br>"%(matchCount/4*matchLength)

        self.solution_text = self.solution_text + "Area of the square<br>"
        self.solution_text = self.solution_text + "= &nbsp;%d &nbsp;&times;&nbsp; %d</div><br>"%(matchCount/4*matchLength,matchCount/4*matchLength)
        self.solution_text = self.solution_text + "= &nbsp;%d %s</div><br><br>"%(answer,unit)

        self.solution_text = self.solution_text + "The area covered by the square is %d %s.<br>"%(answer,unit)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType12(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.breadth = randint(5,9)
        self.times = random.choice([["twice",2],["thrice",3],["four times",4]])
        self.length = self.breadth * self.times[1]
        
        self.problem = "A rectangle is %s as long as it is wide. "%(self.times[0])
        self.problem = self.problem + "If its length is %d m, find its area."%(self.length)
        
        self.answer = self.length * self.breadth

        self.unit = "m<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.unit,self.dollar_unit,self.length,self.times[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType12(self,problem,answer,unit,dollar_unit,length,times):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:54px;'>Breadth</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;Length &nbsp;&divide;&nbsp; %d</div><br>"%(times)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:54px;'></div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d &nbsp;&divide;&nbsp; %d</div><br>"%(length,times)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:54px;'></div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d m</div><br><br>"%(length/times)

        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:40px;'>Area</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d &nbsp;&times;&nbsp; %d</div><br>"%(length,length/times)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:40px;'></div><div style='display:inline-block;width:25px;text-align:center;'>=</div><div style='display:inline-block;'>&nbsp;%d %s</div><br><br>"%(answer,unit)
        
        self.solution_text = self.solution_text + "The area of the rectangle is %d %s."%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType13(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        self.side = randint(4,9)
        self.perimeter = 4 * self.side
        
        self.problem = "%s uses %d m of fencing material to fence up a square garden. "%(self.name,self.perimeter)
        self.problem = self.problem + "What is the area of the garden?"
        
        self.answer = self.side * self.side

        self.unit = "m<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.unit,self.dollar_unit,self.perimeter)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType13(self,problem,answer,unit,dollar_unit,perimeter):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Perimeter of the square garden<br>"
        self.solution_text = self.solution_text + "=&nbsp; Length of fencing material used<br>"
        self.solution_text = self.solution_text + "=&nbsp; %d m<br><br>"%(perimeter)
        
        self.solution_text = self.solution_text + "Side of the square garden<br>"
        self.solution_text = self.solution_text + "=&nbsp; Perimeter &nbsp;&divide;&nbsp; 4<br>"
        self.solution_text = self.solution_text + "=&nbsp; %d &nbsp;&divide;&nbsp; 4<br>"%(perimeter)
        self.solution_text = self.solution_text + "=&nbsp; %d m<br><br>"%(perimeter/4)

        self.solution_text = self.solution_text + "Area of the square garden<br>"
        self.solution_text = self.solution_text + "=&nbsp; Side &nbsp;&times;&nbsp; Side<br>"
        self.solution_text = self.solution_text + "=&nbsp; %d &nbsp;&times;&nbsp; %d<br>"%(perimeter/4,perimeter/4)
        self.solution_text = self.solution_text + "=&nbsp; %d %s<br><br>"%(answer,unit)

        self.solution_text = self.solution_text + "The area of the square garden is %d %s.<br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"
       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text

        return self.explain

    def GenerateProblemType14(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        self.length = random.randrange(5,10,5)
        self.number = randint(3,5)
        self.breadth = randint(3,8) 
        self.length = self.length * self.number
        
        
        self.problem = "%s cut %d cm by %d cm of cloth into %d equal pieces. "%(self.name,self.length,self.breadth,self.number)
        self.problem = self.problem + "What is the area of each piece?"
        
        self.answer = (self.length * self.breadth) / self.number

        self.unit = "cm<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.unit,self.dollar_unit,self.length,self.breadth,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType14(self,problem,answer,unit,dollar_unit,length,breadth,number):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of the cloth<br>"
        self.solution_text = self.solution_text + "=&nbsp; %d &nbsp;&times;&nbsp; %d<br>"%(length,breadth)
        self.solution_text = self.solution_text + "=&nbsp; %d %s<br><br><br>"%(length*breadth,unit)
        
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d<br>"%(length*breadth,number)
        self.solution_text = self.solution_text + "=&nbsp; %d %s<br><br>"%(answer,unit)

        self.solution_text = self.solution_text + "The area of each piece is %d %s.<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType15(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        self.length = random.randrange(20,40,10)
        self.breadth = randint(4,9)
        
        self.problem = "%s used half of a %d cm by %d cm fabric to make a dress for her doll. "%(self.name,self.length,self.breadth)
        self.problem = self.problem + "What area of the fabric was left?"
        
        self.answer = (self.length * self.breadth) / 2

        self.unit = "cm<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.unit,self.dollar_unit,self.length,self.breadth)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType15",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType15(self,problem,answer,unit,dollar_unit,length,breadth):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:120px;'>Area of rectangle</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d &nbsp;&times;&nbsp; %d</div><br>"%(length,breadth)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:120px;'></div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;'>&nbsp;%d %s</div><br>"%(length*breadth,unit)
        self.solution_text = self.solution_text + "There was %d %s of fabric at first.<br><br><br>"%(length*breadth,unit)
        
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; 2 &nbsp;=&nbsp; %d<br>"%(length*breadth,answer)
        self.solution_text = self.solution_text + "%d %s of the fabric was used for making the doll.<br>"%(answer,unit)
        self.solution_text = self.solution_text + "%d %s of the fabric was left.<br><br>"%(answer,unit)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False          