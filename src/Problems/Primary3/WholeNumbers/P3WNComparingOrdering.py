'''
Created on Feb 24, 2013
Module: P3WNComparingOrdering
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
from Problems import PersonName
from random import randint
import string

class P3WNComparingOrdering:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1a","ProblemTypeMCQ1a","ProblemTypeMCQ1b","ProblemTypeMCQ1c",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3a","ProblemType3b","ProblemTypeMCQ3a","ProblemTypeMCQ3b","ProblemTypeMCQ3c",],
                            4:["ProblemType4a","ProblemType4b","ProblemTypeMCQ4a","ProblemTypeMCQ4b",],
                            5:["ProblemType5a","ProblemType5b","ProblemType5c","ProblemTypeMCQ5a","ProblemTypeMCQ5b","ProblemTypeMCQ5c",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1a(),self.GenerateProblemTypeMCQ1a(),self.GenerateProblemTypeMCQ1b(),self.GenerateProblemTypeMCQ1c(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3a(),self.GenerateProblemType3b(),self.GenerateProblemTypeMCQ3a(),self.GenerateProblemTypeMCQ3b(),self.GenerateProblemTypeMCQ3c(),],
                                    4:[self.GenerateProblemType4a(),self.GenerateProblemType4b(),self.GenerateProblemTypeMCQ4a(),self.GenerateProblemTypeMCQ4b(),],
                                    5:[self.GenerateProblemType5a(),self.GenerateProblemType5b(),self.GenerateProblemType5c(),self.GenerateProblemTypeMCQ5a(),self.GenerateProblemTypeMCQ5b(),self.GenerateProblemTypeMCQ5c(),],
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
        self.ProblemType = {"ProblemType1a":self.GenerateProblemType1a(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3a":self.GenerateProblemType3a(),
                            "ProblemType3b":self.GenerateProblemType3b(),
                            "ProblemType4a":self.GenerateProblemType4a(),
                            "ProblemType4b":self.GenerateProblemType4b(),
                            "ProblemType5a":self.GenerateProblemType5a(),
                            "ProblemType5b":self.GenerateProblemType5b(),
                            "ProblemType5c":self.GenerateProblemType5c(),
                            "ProblemTypeMCQ1a":self.GenerateProblemTypeMCQ1a(),
                            "ProblemTypeMCQ1b":self.GenerateProblemTypeMCQ1b(),
                            "ProblemTypeMCQ1c":self.GenerateProblemTypeMCQ1c(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3a":self.GenerateProblemTypeMCQ3a(),
                            "ProblemTypeMCQ3b":self.GenerateProblemTypeMCQ3b(),
                            "ProblemTypeMCQ3c":self.GenerateProblemTypeMCQ3c(),
                            "ProblemTypeMCQ4a":self.GenerateProblemTypeMCQ4a(),
                            "ProblemTypeMCQ4b":self.GenerateProblemTypeMCQ4b(),
                            "ProblemTypeMCQ5a":self.GenerateProblemTypeMCQ5a(),
                            "ProblemTypeMCQ5b":self.GenerateProblemTypeMCQ5b(),
                            "ProblemTypeMCQ5c":self.GenerateProblemTypeMCQ5c(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1a(self):       
        '''e.g.:
        You have 1234 and 1254. Which is greater / smaller?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1000,9999)
        self.number2 = randint(1000,9999)
        
        self.name = random.choice(PersonName.PersonName)
        while self.number1 == self.number2:
            self.number2 = randint(1000,9999)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem1 = "You have %d and %d. Which is greater?" %(self.number1,self.number2)
            self.problem2 = "Choose the greater of %d and %d." %(self.number1,self.number2)
            self.problem3 = "%s has two numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp; and &nbsp;&nbsp; %d<br><br>Find the greater of the two numbers." %(self.name,self.number1,self.number2)
            self.answer = max(self.number1,self.number2)
            self.smallerGreater = "greater"
        else:
            self.problem1 = "You have %d and %d. Which is smaller?" %(self.number1,self.number2)
            self.problem2 = "Choose the smaller of %d and %d." %(self.number1,self.number2)
            self.problem3 = "%s has two numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp; and &nbsp;&nbsp; %d<br><br>Find the smaller of the two numbers." %(self.name,self.number1,self.number2)
            self.answer = min(self.number1,self.number2)
            self.smallerGreater = "smaller"

        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1a(self.problem,self.answer,self.number1,self.number2,self.smallerGreater)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}


    def ExplainType1a(self,problem,answer,number1,number2,smallerGreater):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))
        
        self.solution_text = self.PlaceValueTable(number1,number2,0,0)
        self.solution_text = self.solution_text + "<blockquote>"
        self.solution_text = self.solution_text + self.ComparisonStatement(number1,number2,smallerGreater)
        self.solution_text = self.solution_text + "</blockquote>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain


    def GenerateProblemType2(self):       
        '''e.g.:
        Fill in the blank with <b>greater than</b>, <b>less than</b> or <b>equal to</b>.'''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1000,9999)
        self.number2 = randint(1000,9999)
        
        self.name = random.choice(PersonName.PersonName)

        self.flag = randint(1,3)
        '''one in 3 times numbers will be equal'''
        if self.flag == 3:
            self.number2 = self.number1

        self.problem = "Fill in the blank with <i>greater than</i>, <i>smaller than</i> or <i>equal to</i>.<br><br>"
        self.problem = self.problem + "%d is ______ %d"%(self.number1,self.number2)

        if self.number1 > self.number2:
            self.answer = "greater than"
            self.smallerGreater = "greater"
        elif self.number1 < self.number2:
            self.answer = "smaller than"
            self.smallerGreater = "smaller"
        else:
            self.answer = "equal to"
            self.smallerGreater = "equal"
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.smallerGreater)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}


    def ExplainType2(self,problem,answer,number1,number2,smallerGreater):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))
        
        self.solution_text = self.PlaceValueTable(number1,number2,0,0)
        self.solution_text = self.solution_text + "<blockquote>"
        self.solution_text = self.solution_text + self.ComparisonStatement(number1,number2,smallerGreater)
        if answer=="equal to":
            self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>Hence, %d is %s %d.</font></blockquote>"%(number1,answer,number2)
        else:
            self.solution_text = self.solution_text + "</blockquote>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3a(self):       
        '''e.g.:
        Compare 1234, 1254 and 5421. Which is greatest / smallest?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.numbers = []

        while len(self.numbers) < 3:
            self.number = randint(1000,9999)
            if self.number not in self.numbers:
                self.numbers.append(self.number)
        
        self.name = random.choice(PersonName.PersonName)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem1 = "Compare %d, %d and %d. Which is the greatest?" %(self.numbers[0],self.numbers[1],self.numbers[2])
            self.problem2 = "Which is the greatest of the following 3 numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d" %(self.numbers[0],self.numbers[1],self.numbers[2])
            self.problem3 = "You have %d, %d and %d. Which is the greatest of the three numbers?" %(self.numbers[0],self.numbers[1],self.numbers[2])
            self.problem4 = "%s has three numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d<br><br>Find the greatest of the 3 numbers." %(self.name,self.numbers[0],self.numbers[1],self.numbers[2])
            self.actualNumbers = list(self.numbers)
            self.numbers.sort(reverse=True)
            self.smallestGreatest = "greatest"
        else:
            self.problem1 = "Compare %d, %d and %d. Which is the smallest?" %(self.numbers[0],self.numbers[1],self.numbers[2])
            self.problem2 = "Which is the smallest of the following 3 numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d" %(self.numbers[0],self.numbers[1],self.numbers[2])
            self.problem3 = "You have %d, %d and %d. Which is the smallest of the three numbers?" %(self.numbers[0],self.numbers[1],self.numbers[2])
            self.problem4 = "%s has three numbers.<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d<br><br>Find the smallest of the 3 numbers." %(self.name,self.numbers[0],self.numbers[1],self.numbers[2])
            self.actualNumbers = list(self.numbers)
            self.numbers.sort()
            self.smallestGreatest = "smallest"

        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
        self.answer = self.numbers[0]
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3a(self.problem,self.answer,self.actualNumbers,self.smallestGreatest)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}


    def ExplainType3a(self,problem,answer,numbers,smallestGreatest):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))
        
        self.solution_text = self.PlaceValueTable(numbers[0],numbers[1],numbers[2],0)
        self.solution_text = self.solution_text + "<blockquote>"
        self.solution_text = self.solution_text + "<div class='side'><font class='ExplanationFont'>Compare the thousands, hundreds, tens and ones.</font></div>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        if smallestGreatest=="smallest":
            self.solution_text = self.solution_text + "%d is the smallest of the three numbers."%(answer)
        else:
            self.solution_text = self.solution_text + "%d is the greatest of the three numbers."%(answer)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "</blockquote>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3b(self):       
        '''e.g.:
        <Person.Name> has two numbers.
        1234   5421
        Which of these numbers is smaller / less /greater than 1254?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.numbers = []

        while len(self.numbers) < 3:
            self.number = randint(1000,9999)
            if self.number not in self.numbers:
                self.numbers.append(self.number)
        
        self.name = random.choice(PersonName.PersonName)
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.numbers.sort()
        else:
            self.numbers.sort(reverse=True)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem1 = "%s has two numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp %d &nbsp;&nbsp; and &nbsp;&nbsp; %d<br><br>Which of these is greater than %d?"%(self.name,self.numbers[0],self.numbers[2],self.numbers[1])
            self.problem2 = "Which of the following two numbers is greater than %d?<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp; or &nbsp;&nbsp; %d" %(self.numbers[1],self.numbers[0],self.numbers[2])
            self.problem3 = "You have %d and %d. Which of these numbers is greater than %d?" %(self.numbers[0],self.numbers[2],self.numbers[1])
            self.actualNumbers = list(self.numbers)
            self.numbers.sort(reverse=True)
            self.smallestGreatest = "greatest"
            self.item = "greater"
        else:
            self.item = random.choice(['smaller','less'])
            self.problem1 = "%s has two numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp %d &nbsp;&nbsp; and &nbsp;&nbsp; %d<br><br>Which of these is %s than %d?"%(self.name,self.numbers[0],self.numbers[2],self.item,self.numbers[1])
            self.problem2 = "Which of the following two numbers is %s than %d?<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp; or &nbsp;&nbsp; %d" %(self.item,self.numbers[1],self.numbers[0],self.numbers[2])
            self.problem3 = "You have %d and %d. Which of these numbers is %s than %d?" %(self.numbers[0],self.numbers[2],self.item,self.numbers[1])
            self.actualNumbers = list(self.numbers)
            self.numbers.sort()
            self.smallestGreatest = "smallest"

        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        self.answer = self.numbers[0]
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3b(self.problem,self.answer,self.actualNumbers,self.smallestGreatest,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}


    def ExplainType3b(self,problem,answer,numbers,smallestGreatest,smallerGreater):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))
        
        self.solution_text = self.PlaceValueTable(numbers[0],numbers[1],numbers[2],0)
        numbers.sort()
        self.solution_text = self.solution_text + "<div class='side' style='width:170px;'><font class='ExplanationFont'>Compare the thousands, hundreds, tens and ones.</font></div>"
        self.solution_text = self.solution_text + "<blockquote>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Arrange the numbers from the smallest to the greatest: <br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d<br><br>"%(numbers[0],numbers[1],numbers[2])
        if smallestGreatest=="smallest":
            self.solution_text = self.solution_text + "%d is %s than %d."%(answer,smallerGreater,numbers[1])
        else:
            self.solution_text = self.solution_text + "%d is %s than %d."%(answer,smallerGreater,numbers[1])
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "</blockquote>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4a(self):       
        '''e.g.:
        Arrange the numbers in order, beginning with the smallest / greatest. (Separate the numbers by either commas or spaces.)
        1234, 1254, 2541, 2451'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.numbers = []

        while len(self.numbers) < 4:
            self.number = randint(1000,9999)
            if self.number not in self.numbers:
                self.numbers.append(self.number)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "Arrange the numbers in order, beginning with the greatest.<br><br>"
            self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d, &nbsp;&nbsp; %d, &nbsp;&nbsp; %d, &nbsp;&nbsp; %d"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3])
            self.problem = self.problem + "<br><br>[ Separate the numbers by either <i>commas</i> or <i>spaces</i>. ]"
            self.numbers.sort(reverse=True)
            self.smallestGreatest = "greatest"
            self.otherSmallestGreatest = "smallest"
        else:
            self.problem = "Arrange the numbers in order, beginning with the smallest.<br><br>"
            self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d, &nbsp;&nbsp; %d, &nbsp;&nbsp; %d, &nbsp;&nbsp; %d"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3])
            self.problem = self.problem + "<br><br>[ Separate the numbers by either <i>commas</i> or <i>spaces</i>. ]"
            self.numbers.sort()
            self.smallestGreatest = "smallest"
            self.otherSmallestGreatest = "greatest"
        
        self.answer = '' 
        for i in range(len(self.numbers)):
            self.answer = self.answer + str(self.numbers[i])+" "
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4a(self.problem,self.answer,self.numbers,self.smallestGreatest,self.otherSmallestGreatest)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3}

    def ExplainType4a(self,problem,answer,numbers,smallestGreatest,otherSmallestGreatest):
        self.answer_text = "<br>The correct answer is:<br><br>%d &nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp; %d"%(numbers[0],numbers[1],numbers[2],numbers[3])
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>First, compare the thousands and arrange the numbers from the %s thousands to the %s thousands.<br><br>"%(smallestGreatest,otherSmallestGreatest)
        self.solution_text = self.solution_text + "Next, if needed, compare the hundreds, tens and ones to re-arrange the numbers.<br>"
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + self.PlaceValueTable(numbers[0],numbers[1],numbers[2],numbers[3])
        self.solution_text = self.solution_text + "<blockquote>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "From the %s to the %s, the numbers are:<br><br>"%(smallestGreatest,otherSmallestGreatest)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d"%(numbers[0],numbers[1],numbers[2],numbers[3])
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "</blockquote>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4b(self):       
        '''e.g.:
        <Person.Unclename 1> <earns> $1234. <Person.Unclename 2> <earns> $1254. <Person.Unclename 3> <earns> $5421. Arrange these amounts in order, beginning with the smallest / greatest. (Separate the amounts by either commas or spaces.)
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.names = random.sample(PersonName.UncleName,3)
        self.numbers = []

        while len(self.numbers) < 3:
            self.number = randint(1000,9999)
            if self.number not in self.numbers:
                self.numbers.append(self.number)
                
        self.items = ['earns','saves','spends','donates','gives away','wins','pays','has']
        
        self.item = random.choice(self.items)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "%s %s $%d. %s %s $%d. %s %s $%d."%(self.names[0],self.item,self.numbers[0],self.names[1],self.item,self.numbers[1],self.names[2],self.item,self.numbers[2])
            self.problem = self.problem + "<br><br>Arrange these amounts in order, beginning with the greatest.<br><br>[ Separate the amounts by <i>commas</i> or <i>spaces</i> and do NOT put the $ sign. ]"
            self.numbers.sort(reverse=True)
            self.smallestGreatest = "greatest"
            self.otherSmallestGreatest = "smallest"
        else:
            self.problem = "%s %s $%d. %s %s $%d. %s %s $%d."%(self.names[0],self.item,self.numbers[0],self.names[1],self.item,self.numbers[1],self.names[2],self.item,self.numbers[2])
            self.problem = self.problem + "<br><br>Arrange these amounts in order, beginning with the smallest.<br><br>[ Separate the amounts by <i>commas</i> or <i>spaces</i> and do NOT put the $ sign. ]"
            self.numbers.sort()
            self.smallestGreatest = "smallest"
            self.otherSmallestGreatest = "greatest"
        
        self.answer = '' 
            
        for i in range(len(self.numbers)):
            self.answer = self.answer + str(self.numbers[i])+" "
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4b(self.problem,self.answer,self.numbers,self.smallestGreatest,self.otherSmallestGreatest)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3}

    def ExplainType4b(self,problem,answer,numbers,smallestGreatest,otherSmallestGreatest):
        self.answer_text = "<br>The correct answer is:<br><br>%d &nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp; %d"%(numbers[0],numbers[1],numbers[2])
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>First, compare the thousands and arrange the numbers from the %s thousands to the %s thousands.<br><br>"%(smallestGreatest,otherSmallestGreatest)
        self.solution_text = self.solution_text + "Next, if needed, compare the hundreds, tens and ones to re-arrange the numbers.<br>"
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + self.PlaceValueTable(numbers[0],numbers[1],numbers[2],0)
        self.solution_text = self.solution_text + "<blockquote>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "From the %s to the %s, the amounts are:<br><br>"%(smallestGreatest,otherSmallestGreatest)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d"%(numbers[0],numbers[1],numbers[2])
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "</blockquote>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5a(self):       
        '''e.g.:
        Which is the smallest / greatest 4-digit number you can make using all these digits: 1, 2, 3 and 4?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.digits = random.sample([1,2,3,4,5,6,7,8,9],4)
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "What is the greatest 4-digit number you can make using all these digits: %d, %d, %d and %d?"%(self.digits[0],self.digits[1],self.digits[2],self.digits[3])
            self.digits.sort(reverse=True)
        else:
            self.problem = "What is the smallest 4-digit number you can make using all these digits: %d, %d, %d and %d?"%(self.digits[0],self.digits[1],self.digits[2],self.digits[3])
            self.digits.sort()           
        
        self.answer = '' 
            
        for i in range(len(self.digits)):
            self.answer = self.answer + str(self.digits[i])
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5a(self.problem,self.answer,self.digits,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType5a(self,problem,answer,digits,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        if flag==1:
            digits.sort(reverse=True)
            self.solution_text = "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "<br>Arrange the given digits from greatest to smallest to make the greatest 4-digit number.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d<br><br>"%(digits[0],digits[1],digits[2],digits[3])
            self.solution_text = self.solution_text + "The greatest 4-digit number is %s.<br>"%(answer)
            self.solution_text = self.solution_text + "</font>"
        else:
            digits.sort()
            self.solution_text = "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "<br>Arrange the given digits from smallest to greatest to make the smallest 4-digit number.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d<br><br>"%(digits[0],digits[1],digits[2],digits[3])
            self.solution_text = self.solution_text + "The smallest 4-digit number is %s.<br>"%(answer)
            self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5b(self):       
        '''e.g.:
        Which is the smallest / greatest 4-digit even number you can make using all these digits: 1, 2, 3 and 4?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.EvenDigits = random.sample([2,4,6,8],2)
        self.OddDigits = random.sample([1,3,5,7,9],2)
        
        self.digits = self.EvenDigits + self.OddDigits
        
        random.shuffle(self.digits)
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "What is the greatest 4-digit even number you can make using all these digits: %d, %d, %d and %d?"%(self.digits[0],self.digits[1],self.digits[2],self.digits[3])
            self.EvenDigits.sort()
            self.LastDigit = self.EvenDigits[0]
            self.RemainingDigits = self.OddDigits + [self.EvenDigits[1]]
            self.RemainingDigits.sort(reverse=True)
        else:
            self.problem = "What is the smallest 4-digit even number you can make using all these digits: %d, %d, %d and %d?"%(self.digits[0],self.digits[1],self.digits[2],self.digits[3])
            self.EvenDigits.sort(reverse=True)
            self.LastDigit = self.EvenDigits[0]
            self.RemainingDigits = self.OddDigits + [self.EvenDigits[1]]
            self.RemainingDigits.sort()
        
        self.answer = '' 
            
        for i in range(len(self.RemainingDigits)):
            self.answer = self.answer + str(self.RemainingDigits[i])
            
        self.answer = self.answer + str(self.LastDigit)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5b(self.problem,self.answer,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType5b(self,problem,answer,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        if flag==1:
            self.solution_text = "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "<br>First, pick out the smallest even digit from the given digits.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[3])
            self.solution_text = self.solution_text + "Next, arrange the remaining digits from greatest to smallest.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1],answer[2])
            self.solution_text = self.solution_text + "Finally, attach the smallest even digit that we picked out to the end of this list.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1],answer[2],answer[3])
            self.solution_text = self.solution_text + "The greatest 4-digit even number is %s.<br>"%(answer)
            self.solution_text = self.solution_text + "</font>"
        else:
            self.solution_text = "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "<br>First, pick out the greatest even digit from the given digits.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[3])
            self.solution_text = self.solution_text + "Next, arrange the remaining digits from smallest to greatest.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1],answer[2])
            self.solution_text = self.solution_text + "Finally, attach the greatest even digit that we picked out to the end of this list.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1],answer[2],answer[3])
            self.solution_text = self.solution_text + "The smallest 4-digit even number is %s.<br>"%(answer)
            self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5c(self):       
        '''e.g.:
        Which is the smallest / greatest 4-digit odd number you can make using all these digits: 1, 2, 3 and 4?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.EvenDigits = random.sample([2,4,6,8],2)
        self.OddDigits = random.sample([1,3,5,7,9],2)
        
        self.digits = self.EvenDigits + self.OddDigits
        
        random.shuffle(self.digits)
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "What is the greatest 4-digit odd number you can make using all these digits: %d, %d, %d and %d?"%(self.digits[0],self.digits[1],self.digits[2],self.digits[3])
            self.OddDigits.sort()
            self.LastDigit = self.OddDigits[0]
            self.RemainingDigits = self.EvenDigits + [self.OddDigits[1]]
            self.RemainingDigits.sort(reverse=True)
        else:
            self.problem = "What is the smallest 4-digit odd number you can make using all these digits: %d, %d, %d and %d?"%(self.digits[0],self.digits[1],self.digits[2],self.digits[3])
            self.OddDigits.sort(reverse=True)
            self.LastDigit = self.OddDigits[0]
            self.RemainingDigits = self.EvenDigits + [self.OddDigits[1]]
            self.RemainingDigits.sort()
        
        self.answer = '' 
            
        for i in range(len(self.RemainingDigits)):
            self.answer = self.answer + str(self.RemainingDigits[i])
            
        self.answer = self.answer + str(self.LastDigit)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5c(self.problem,self.answer,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType5c(self,problem,answer,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        
        if flag==1:
            self.solution_text = "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "<br>First, pick out the smallest odd digit from the given digits.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[3])
            self.solution_text = self.solution_text + "Next, arrange the remaining digits from greatest to smallest.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1],answer[2])
            self.solution_text = self.solution_text + "Finally, attach the smallest odd digit that we picked out to the end of this list.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1],answer[2],answer[3])
            self.solution_text = self.solution_text + "The greatest 4-digit odd number is %s.<br>"%(answer)
            self.solution_text = self.solution_text + "</font>"
        else:
            self.solution_text = "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "<br>First, pick out the greatest odd digit from the given digits.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[3])
            self.solution_text = self.solution_text + "Next, arrange the remaining digits from smallest to greatest.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1],answer[2])
            self.solution_text = self.solution_text + "Finally, attach the greatest odd digit that we picked out to the end of this list.<br><br>"
            self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>"%(answer[0],answer[1],answer[2],answer[3])
            self.solution_text = self.solution_text + "The smallest 4-digit odd number is %s.<br>"%(answer)
            self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemTypeMCQ1a(self):
        '''e.g.:
        You have 1234 and 1254. Which is greater / smaller?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1000,9999)
        self.number2 = randint(1000,9999)
        
        self.name = random.choice(PersonName.PersonName)
        while self.number1 == self.number2:
            self.number2 = randint(1000,9999)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem1 = "You have %d and %d. Which is greater?" %(self.number1,self.number2)
            self.problem2 = "Choose the greater of %d and %d." %(self.number1,self.number2)
            self.problem3 = "%s has two numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp; and &nbsp;&nbsp; %d<br><br>Find the greater of the two numbers." %(self.name,self.number1,self.number2)
            self.answer = max(self.number1,self.number2)
            self.smallerGreater = "greater"
        else:
            self.problem1 = "You have %d and %d. Which is smaller?" %(self.number1,self.number2)
            self.problem2 = "Choose the smaller of %d and %d." %(self.number1,self.number2)
            self.problem3 = "%s has two numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp; and &nbsp;&nbsp; %d<br><br>Find the smaller of the two numbers." %(self.name,self.number1,self.number2)
            self.answer = min(self.number1,self.number2)
            self.smallerGreater = "smaller"

        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
                
        self.template = "MCQType2Choices.html"
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1a(self.problem,self.answer,self.number1,self.number2,self.smallerGreater)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ1a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'answer1':self.number1,'answer2':self.number2,'value1':self.number1,'value2':self.number2}
        
    def GenerateProblemTypeMCQ1b(self):
        '''e.g.:
        <Person.Boyname 1> has a collection of 1234 <stamps>. <Person.Boyname 2> has a collection of 1254 <stamps>. Who has a bigger / smaller collection of <stamps>?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1000,9999)
        self.number2 = randint(1000,9999)
        
        self.names = random.sample(PersonName.BoyName,2)
        
        self.items = ['stamps','clay shells','marbles','paper clips','paper flags','crayons','stickers','toy cars','dry leaves','photos']
        
        self.item = random.choice(self.items)
        
        while self.number1 == self.number2:
            self.number2 = randint(1000,9999)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "%s has a collection of %d %s. %s has a collection of %d %s. Who has a bigger collection of %s?"%(self.names[0],self.number1,self.item,
                                                                                                                             self.names[1],self.number2,self.item,
                                                                                                                             self.item)
            self.AnswerNumber = max(self.number1,self.number2)
            self.smallerGreater = "bigger"
        else:
            self.problem = "%s has a collection of %d %s. %s has a collection of %d %s. Who has a smaller collection of %s?"%(self.names[0],self.number1,self.item,
                                                                                                                             self.names[1],self.number2,self.item,
                                                                                                                             self.item)
            self.AnswerNumber = min(self.number1,self.number2)
            self.smallerGreater = "smaller"

        if self.AnswerNumber == self.number1:
            self.answer = self.names[0]
        else:
            self.answer = self.names[1]

                
        self.template = "MCQType2Choices.html"
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1b(self.problem,self.answer,self.number1,self.number2,self.smallerGreater,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ1b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,
                'answer1':self.names[0],'answer2':self.names[1],'value1':self.names[0],'value2':self.names[1]}
        
    def ExplainType1b(self,problem,answer,number1,number2,smallerGreater,item):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))
        
        self.solution_text = self.PlaceValueTable(number1,number2,0,0)
        self.solution_text = self.solution_text + "<blockquote>"
        self.solution_text = self.solution_text + self.ComparisonStatement(number1,number2,smallerGreater)
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>Hence, %s has a %s collection of %s.</font></blockquote>"%(answer,smallerGreater,item)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ1c(self):
        '''e.g.:
        <Person.Unclename> <earns> $1234. <Person.Auntyname> <earns> $1254. Who <earns> more /less?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1000,9999)
        self.number2 = randint(1000,9999)
        
        self.names = random.sample(PersonName.AuntyName+PersonName.UncleName,2)
        
        self.items = ['earns','saves','spends','donates','gives away','wins','pays','has']
        
        self.item = random.choice(self.items)
        
        while self.number1 == self.number2:
            self.number2 = randint(1000,9999)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "%s %s $%d. %s %s $%d. Who %s more?"%(self.names[0],self.item,self.number1,self.names[1],self.item,self.number2,self.item)
            self.AnswerNumber = max(self.number1,self.number2)
            self.smallerGreater = "greater"
            self.moreLess = "more"
        else:
            self.problem = "%s %s $%d. %s %s $%d. Who %s less?"%(self.names[0],self.item,self.number1,self.names[1],self.item,self.number2,self.item)
            self.AnswerNumber = min(self.number1,self.number2)
            self.smallerGreater = "smaller"
            self.moreLess = "less"

        if self.AnswerNumber == self.number1:
            self.answer = self.names[0]
        else:
            self.answer = self.names[1]

                
        self.template = "MCQType2Choices.html"
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1c(self.problem,self.answer,self.number1,self.number2,self.smallerGreater,self.moreLess,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ1c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,
                'answer1':self.names[0],'answer2':self.names[1],'value1':self.names[0],'value2':self.names[1]}
        
    def ExplainType1c(self,problem,answer,number1,number2,smallerGreater,moreLess,item):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))
        
        self.solution_text = self.PlaceValueTable(number1,number2,0,0)
        self.solution_text = self.solution_text + "<blockquote>"
        self.solution_text = self.solution_text + self.ComparisonStatement(number1,number2,smallerGreater)
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>Hence, %s %s %s.</font></blockquote>"%(answer,item,moreLess)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        Fill in the blank with <b>greater than</b>, <b>less than</b> or <b>equal to</b>.'''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1000,9999)
        self.number2 = randint(1000,9999)
        
        self.name = random.choice(PersonName.PersonName)

        self.flag = randint(1,3)
        '''one in 3 times numbers will be equal'''
        if self.flag == 3:
            self.number2 = self.number1

        self.problem = "Choose the correct answer to fill the blank.<br><br>"
        self.problem = self.problem + "%d is ______ %d"%(self.number1,self.number2)

        if self.number1 > self.number2:
            self.answer = "greater than"
            self.smallerGreater = "greater"
        elif self.number1 < self.number2:
            self.answer = "smaller than"
            self.smallerGreater = "smaller"
        else:
            self.answer = "equal to"
            self.smallerGreater = "equal"
                
        self.template = "MCQType3Choices.html"
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.smallerGreater)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,
                'answer1':"greater than",'answer2':"smaller than",'answer3':"equal to",
                'value1':"greater than",'value2':"smaller than",'value3':"equal to",}
        
    def GenerateProblemTypeMCQ3a(self):
        '''e.g.:
        Compare 1234, 1254 and 5421. Which is greatest / smallest?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.numbers = []

        while len(self.numbers) < 3:
            self.number = randint(1000,9999)
            if self.number not in self.numbers:
                self.numbers.append(self.number)
        
        self.name = random.choice(PersonName.PersonName)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem1 = "Compare %d, %d and %d. Which is the greatest?" %(self.numbers[0],self.numbers[1],self.numbers[2])
            self.problem2 = "Which is the greatest of the following 3 numbers:<br><br>%d&nbsp;&nbsp;%d&nbsp;&nbsp;%d" %(self.numbers[0],self.numbers[1],self.numbers[2])
            self.problem3 = "You have %d, %d and %d. Which is the greatest of the three numbers?" %(self.numbers[0],self.numbers[1],self.numbers[2])
            self.problem4 = "%s has three numbers.<br><br>%d&nbsp;&nbsp;%d&nbsp;&nbsp;%d<br><br>Find the greatest of the 3 numbers." %(self.name,self.numbers[0],self.numbers[1],self.numbers[2])
            self.actualNumbers = list(self.numbers)
            self.numbers.sort(reverse=True)
            self.smallestGreatest = "greatest"
        else:
            self.problem1 = "Compare %d, %d and %d. Which is the smallest?" %(self.numbers[0],self.numbers[1],self.numbers[2])
            self.problem2 = "Which is the smallest of the following 3 numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d" %(self.numbers[0],self.numbers[1],self.numbers[2])
            self.problem3 = "You have %d, %d and %d. Which is the smallest of the three numbers?" %(self.numbers[0],self.numbers[1],self.numbers[2])
            self.problem4 = "%s has three numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp;&nbsp; %d<br><br>Find the smallest of the 3 numbers." %(self.name,self.numbers[0],self.numbers[1],self.numbers[2])
            self.actualNumbers = list(self.numbers)
            self.numbers.sort()
            self.smallestGreatest = "smallest"

        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
        self.answer = self.numbers[0]
        
        random.shuffle(self.numbers)
                
        self.template = "MCQType3Choices.html"
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3a(self.problem,self.answer,self.actualNumbers,self.smallestGreatest)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ3a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,
                'answer1':self.numbers[0],'answer2':self.numbers[1],'answer3':self.numbers[2],
                'value1':self.numbers[0],'value2':self.numbers[1],'value3':self.numbers[2],}
        
    def GenerateProblemTypeMCQ3b(self):
        '''e.g.:
        <Person.Name> has two numbers.
        1234   5421
        Which of these numbers is smaller / less /greater than 1254?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.numbers = []

        while len(self.numbers) < 3:
            self.number = randint(1000,9999)
            if self.number not in self.numbers:
                self.numbers.append(self.number)
        
        self.name = random.choice(PersonName.PersonName)
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.numbers.sort()
        else:
            self.numbers.sort(reverse=True)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem1 = "%s has two numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp; and &nbsp;&nbsp; %d<br><br>Which of these is greater than %d?"%(self.name,self.numbers[0],self.numbers[2],self.numbers[1])
            self.problem2 = "Which of the following two numbers is greater than %d?<br><br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp; or &nbsp;&nbsp; %d" %(self.numbers[1],self.numbers[0],self.numbers[2])
            self.problem3 = "You have %d and %d. Which of these numbers is greater than %d?" %(self.numbers[0],self.numbers[2],self.numbers[1])
            self.actualNumbers = list(self.numbers)
            self.numbers.sort(reverse=True)
            self.smallestGreatest = "greatest"
            self.item = "greater"
        else:
            self.item = random.choice(['smaller','less'])
            self.problem1 = "%s has two numbers:<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp; and &nbsp;&nbsp; %d<br><br>Which of these is %s than %d?"%(self.name,self.numbers[0],self.numbers[2],self.item,self.numbers[1])
            self.problem2 = "Which of the following two numbers is %s than %d?<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp; or &nbsp;&nbsp; %d" %(self.item,self.numbers[1],self.numbers[0],self.numbers[2])
            self.problem3 = "You have %d and %d. Which of these numbers is %s than %d?" %(self.numbers[0],self.numbers[2],self.item,self.numbers[1])
            self.actualNumbers = list(self.numbers)
            self.numbers.sort()
            self.smallestGreatest = "smallest"

        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        self.answer = self.numbers[0]
                
        self.AnswerNumber = [self.numbers[0],self.numbers[2]] 
        
        random.shuffle(self.AnswerNumber)
        
        self.template = "MCQType2Choices.html"
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3b(self.problem,self.answer,self.actualNumbers,self.smallestGreatest,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ3b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,
                'answer1':self.AnswerNumber[0],'answer2':self.AnswerNumber[1],
                'value1':self.AnswerNumber[0],'value2':self.AnswerNumber[1],}
        
    def GenerateProblemTypeMCQ3c(self):
        '''e.g.:
        <Last month, a fruiterer sold> 120 <mangoes>, 1324 <oranges> and 2451 <apples>.
        Complete the following sentence.
        <He sold> more / fewer _________ than <oranges>.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.numbers = []

        while len(self.numbers) < 3:
            self.number = randint(1000,9999)
            if self.number not in self.numbers:
                self.numbers.append(self.number)
        
        self.items = [['Last month, a fruiterer sold','mangoes','oranges','apples','','He sold','oranges','mangoes','oranges','apples'],
                        ['During a long weekend, an amusement park received','girls','boys','adults','','The amusement park received','boys','girls','boys','adults'],
                        ['A megamart had','cans of soup','cans of soda','cans of milk','','The megamart had','cans of soda','soup','soda','milk'],
                        ['At an IT sale, a dealer sold','printers','desktops','laptops','','The dealer sold','desktops','printers','desktops','laptops'],
                        ['At a book fair, a book dealer sold','coursebooks','comics','art books','','The book dealer sold','comics','coursebooks','comics','art books'],
                        ['On a sunny day, there were','girls','boys','adults', 'on a beach','There were','boys on the beach','girls','boys','adults'],
                        ['A movie rental shop had a collection of','cartoon movies','action movies','comedy movies','','There were','action movies','cartoon','action','comedy'],
                        ['On a certain day, there were','seniors','children','adults', 'who traveled by the train','There were','children who traveled by the train','seniors','children','adults'],
                        ['Last week, a baker baked','pies','cakes','loaves of bread','','The baker baked','cakes','pies','cakes','loaves of bread'],
                        ['A plant nursery had','ceramic pots','plastic pots','clay pots','','There were','plastic pots','ceramic','plastic','clay']]
        
        self.item = random.choice(self.items)

        self.sortFlag = randint(1,2)
        if self.sortFlag == 1:
            self.numbers.sort()
        else:
            self.numbers.sort(reverse=True)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "%s %d %s, %d %s and %d %s %s. Complete the following sentence.<br><br>%s more _______ than %s." %(self.item[0],self.numbers[0],self.item[1],
                                                                                                                          self.numbers[1],self.item[2],self.numbers[2],self.item[3],
                                                                                                                          self.item[4],self.item[5],self.item[6]
                                                                                                                          )
            if self.numbers[0]>self.numbers[1]:
                self.answer = self.item[1]
            else:
                self.answer = self.item[3]
            self.smallestGreatest = "greatest"
        else:
            self.problem = "%s %d %s, %d %s and %d %s %s. Complete the following sentence.<br><br>%s fewer _______ than %s." %(self.item[0],self.numbers[0],self.item[1],
                                                                                                                          self.numbers[1],self.item[2],self.numbers[2],self.item[3],
                                                                                                                          self.item[4],self.item[5],self.item[6]
                                                                                                                          )
            if self.numbers[0]<self.numbers[1]:
                self.answer = self.item[1]
            else:
                self.answer = self.item[3]
            self.smallestGreatest = "smallest"

                
        self.template = "MCQType2Choices.html"
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3c(self.problem,self.answer,self.numbers,self.item,self.smallestGreatest,self.sortFlag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ3c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,
                'answer1':self.item[1],'answer2':self.item[3],
                'value1':self.item[1],'value2':self.item[3],}
        
    def ExplainType3c(self,problem,answer,numbers,item,smallestGreatest,flag):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))
        
        self.solution_text = self.PlaceValueTable(numbers[0],numbers[1],numbers[2],0)
        numbers.sort()
        self.solution_text = self.solution_text + "<div class='side' style='width:170px;'><font class='ExplanationFont'>Compare the thousands, hundreds, tens and ones.</font></div>"
        self.solution_text = self.solution_text + "<blockquote>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Arrange the numbers from the smallest to the greatest: <br><br>"
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<table border=0>"
        self.solution_text = self.solution_text + "<tr><td style='width:75px;'>%d</td><td style='width:75px;'>%d</td><td style='width:75px;'>%d</td></tr>"%(numbers[0],numbers[1],numbers[2])
        if flag==1:
            self.solution_text = self.solution_text + "<tr><td style='white-space:nowrap;'>%s</td><td style='white-space:nowrap;'>%s</td><td style='white-space:nowrap;'>%s</td></tr>"%(item[7],item[8],item[9])
        else:
            self.solution_text = self.solution_text + "<tr><td style='white-space:nowrap;'>%s</td><td style='white-space:nowrap;'>%s</td><td style='white-space:nowrap;'>%s</td></tr>"%(item[9],item[8],item[7])
        self.solution_text = self.solution_text + "</table><br>"
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        if smallestGreatest=="smallest":
            self.solution_text = self.solution_text + "%s fewer <u>%s</u> than %s."%(item[5],answer,item[6])
        else:
            self.solution_text = self.solution_text + "%s more <u>%s</u> than %s."%(item[5],answer,item[6])
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "</blockquote>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain


    def ExplainType3(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))
        self.solution_text =  "Coming Soon!!"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ4a(self):
        '''e.g.:
        Arrange the numbers in order, beginning with the smallest / greatest. (Separate the numbers by either commas or spaces.)
        1234, 1254, 2541, 2451'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.numbers = []

        while len(self.numbers) < 4:
            self.number = randint(1000,9999)
            if self.number not in self.numbers:
                self.numbers.append(self.number)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "Arrange the numbers in order, beginning with the greatest.<br><br>"
            self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp; %d"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3])
            self.numbers.sort(reverse=True)
            self.actualNumbers = list(self.numbers)
            self.smallestGreatest = "greatest"
            self.otherSmallestGreatest = "smallest"
        else:
            self.problem = "Arrange the numbers in order, beginning with the smallest.<br><br>"
            self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp; %d &nbsp;&nbsp;&nbsp; %d"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3])
            self.numbers.sort()
            self.actualNumbers = list(self.numbers)
            self.smallestGreatest = "smallest"
            self.otherSmallestGreatest = "greatest"
        
        self.answer = '' 
        for i in range(len(self.numbers)):
            self.answer = self.answer + str(self.numbers[i])+"&nbsp;&nbsp;&nbsp;"
                
        self.wrongAnswers = []
        
        while len(self.wrongAnswers) < 3:
            random.shuffle(self.numbers)
            self.wrongAnswer = ''
            for i in range(len(self.numbers)):
                self.wrongAnswer = self.wrongAnswer + str(self.numbers[i])+"&nbsp;&nbsp;&nbsp;"
            
            if self.wrongAnswer!=self.answer and self.wrongAnswer not in self.wrongAnswers:
                self.wrongAnswers.append(self.wrongAnswer)
        
        
        self.wrongAnswers.append(self.answer)
        
        random.shuffle(self.wrongAnswers)
        
        self.template = "MCQTypeProblems.html"
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4a(self.problem,self.answer,self.actualNumbers,self.smallestGreatest,self.otherSmallestGreatest)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ4a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,
                'answer1':self.wrongAnswers[0],'answer2':self.wrongAnswers[1],'answer3':self.wrongAnswers[2],'answer4':self.wrongAnswers[3],
                'value1':self.wrongAnswers[0],'value2':self.wrongAnswers[1],'value3':self.wrongAnswers[2],'value4':self.wrongAnswers[3],}
        
    def GenerateProblemTypeMCQ4b(self):
        '''e.g.:
        <Person.Unclename 1> <earns> $1234. <Person.Unclename 2> <earns> $1254. <Person.Unclename 3> <earns> $5421. Arrange these amounts in order, beginning with the smallest / greatest. (Separate the amounts by either commas or spaces.)
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.names = random.sample(PersonName.UncleName,3)
        self.numbers = []

        while len(self.numbers) < 3:
            self.number = randint(1000,9999)
            if self.number not in self.numbers:
                self.numbers.append(self.number)
                
        self.items = ['earns','saves','spends','donates','gives away','wins','pays','has']
        
        self.item = random.choice(self.items)
                    
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "%s %s $%d. %s %s $%d. %s %s $%d."%(self.names[0],self.item,self.numbers[0],self.names[1],self.item,self.numbers[1],self.names[2],self.item,self.numbers[2])
            self.problem = self.problem + "<br><br>Arrange these amounts in order, beginning with the greatest."
            self.numbers.sort(reverse=True)
            self.actualNumbers = list(self.numbers)
            self.smallestGreatest = "greatest"
            self.otherSmallestGreatest = "smallest"
        else:
            self.problem = "%s %s $%d. %s %s $%d. %s %s $%d."%(self.names[0],self.item,self.numbers[0],self.names[1],self.item,self.numbers[1],self.names[2],self.item,self.numbers[2])
            self.problem = self.problem + "<br><br>Arrange these amounts in order, beginning with the smallest."
            self.numbers.sort()
            self.actualNumbers = list(self.numbers)
            self.smallestGreatest = "smallest"
            self.otherSmallestGreatest = "greatest"
            
        
        self.answer = '' 
        for i in range(len(self.numbers)):
            self.answer = self.answer + str(self.numbers[i])+"&nbsp;&nbsp;&nbsp;"
                       
        self.template = "MCQType3Choices.html"

        self.wrongAnswers = []
        
        while len(self.wrongAnswers) < 2:
            random.shuffle(self.numbers)
            self.wrongAnswer = ''
            for i in range(len(self.numbers)):
                self.wrongAnswer = self.wrongAnswer + str(self.numbers[i])+"&nbsp;&nbsp;&nbsp;"
            
            if self.wrongAnswer!=self.answer and self.wrongAnswer not in self.wrongAnswers:
                self.wrongAnswers.append(self.wrongAnswer)
        
        
        self.wrongAnswers.append(self.answer)
        
        random.shuffle(self.wrongAnswers)
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4b(self.problem,self.answer,self.actualNumbers,self.smallestGreatest,self.otherSmallestGreatest)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ4b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,
                'answer1':self.wrongAnswers[0],'answer2':self.wrongAnswers[1],'answer3':self.wrongAnswers[2],
                'value1':self.wrongAnswers[0],'value2':self.wrongAnswers[1],'value3':self.wrongAnswers[2],}
        
    def GenerateProblemTypeMCQ5a(self):
        '''e.g.:
        Which is the smallest / greatest 4-digit number you can make using all these digits: 1, 2, 3 and 4?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.digits = random.sample([1,2,3,4,5,6,7,8,9],4)
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "What is the greatest 4-digit number you can make using all these digits: %d, %d, %d and %d?"%(self.digits[0],self.digits[1],self.digits[2],self.digits[3])
            self.digits.sort(reverse=True)
        else:
            self.problem = "What is the smallest 4-digit number you can make using all these digits: %d, %d, %d and %d?"%(self.digits[0],self.digits[1],self.digits[2],self.digits[3])
            self.digits.sort()           
        
        self.answer = '' 
            
        for i in range(len(self.digits)):
            self.answer = self.answer + str(self.digits[i])
        
        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = []
        
        while len(self.wrongAnswers) < 3:
            random.shuffle(self.digits)
            self.wrongAnswer = ''
            for i in range(len(self.digits)):
                self.wrongAnswer = self.wrongAnswer + str(self.digits[i])
            
            if self.wrongAnswer!=self.answer and self.wrongAnswer not in self.wrongAnswers:
                self.wrongAnswers.append(self.wrongAnswer)
        
        
        self.wrongAnswers.append(self.answer)
        
        random.shuffle(self.wrongAnswers)
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5a(self.problem,self.answer,self.digits,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ5a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,
                'answer1':self.wrongAnswers[0],'answer2':self.wrongAnswers[1],'answer3':self.wrongAnswers[2],'answer4':self.wrongAnswers[3],
                'value1':self.wrongAnswers[0],'value2':self.wrongAnswers[1],'value3':self.wrongAnswers[2],'value4':self.wrongAnswers[3],}
        
    def GenerateProblemTypeMCQ5b(self):
        '''e.g.:
        Which is the smallest / greatest 4-digit even number you can make using all these digits: 1, 2, 3 and 4?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.EvenDigits = random.sample([2,4,6,8],2)
        self.OddDigits = random.sample([1,3,5,7,9],2)
        
        self.digits = self.EvenDigits + self.OddDigits
        
        random.shuffle(self.digits)
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "What is the greatest 4-digit even number you can make using all these digits: %d, %d, %d and %d?"%(self.digits[0],self.digits[1],self.digits[2],self.digits[3])
            self.EvenDigits.sort()
            self.LastDigit = self.EvenDigits[0]
            self.RemainingDigits = self.OddDigits + [self.EvenDigits[1]]
            self.RemainingDigits.sort(reverse=True)
        else:
            self.problem = "What is the smallest 4-digit even number you can make using all these digits: %d, %d, %d and %d?"%(self.digits[0],self.digits[1],self.digits[2],self.digits[3])
            self.EvenDigits.sort(reverse=True)
            self.LastDigit = self.EvenDigits[0]
            self.RemainingDigits = self.OddDigits + [self.EvenDigits[1]]
            self.RemainingDigits.sort()
        
        self.answer = '' 
            
        for i in range(len(self.RemainingDigits)):
            self.answer = self.answer + str(self.RemainingDigits[i])
            
        self.answer = self.answer + str(self.LastDigit)
        
        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = []
        
        while len(self.wrongAnswers) < 3:
            random.shuffle(self.digits)
            self.wrongAnswer = ''
            for i in range(len(self.digits)):
                self.wrongAnswer = self.wrongAnswer + str(self.digits[i])
            
            if self.wrongAnswer!=self.answer and self.wrongAnswer not in self.wrongAnswers:
                self.wrongAnswers.append(self.wrongAnswer)
        
        
        self.wrongAnswers.append(self.answer)
        
        random.shuffle(self.wrongAnswers)
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5b(self.problem,self.answer,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ5b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,
                'answer1':self.wrongAnswers[0],'answer2':self.wrongAnswers[1],'answer3':self.wrongAnswers[2],'answer4':self.wrongAnswers[3],
                'value1':self.wrongAnswers[0],'value2':self.wrongAnswers[1],'value3':self.wrongAnswers[2],'value4':self.wrongAnswers[3],}
        
    def GenerateProblemTypeMCQ5c(self):
        '''e.g.:
        Which is the smallest / greatest 4-digit odd number you can make using all these digits: 1, 2, 3 and 4?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.EvenDigits = random.sample([2,4,6,8],2)
        self.OddDigits = random.sample([1,3,5,7,9],2)
        
        self.digits = self.EvenDigits + self.OddDigits
        
        random.shuffle(self.digits)
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "What is the greatest 4-digit odd number you can make using all these digits: %d, %d, %d and %d?"%(self.digits[0],self.digits[1],self.digits[2],self.digits[3])
            self.OddDigits.sort()
            self.LastDigit = self.OddDigits[0]
            self.RemainingDigits = self.EvenDigits + [self.OddDigits[1]]
            self.RemainingDigits.sort(reverse=True)
        else:
            self.problem = "What is the smallest 4-digit odd number you can make using all these digits: %d, %d, %d and %d?"%(self.digits[0],self.digits[1],self.digits[2],self.digits[3])
            self.OddDigits.sort(reverse=True)
            self.LastDigit = self.OddDigits[0]
            self.RemainingDigits = self.EvenDigits + [self.OddDigits[1]]
            self.RemainingDigits.sort()
        
        self.answer = '' 
            
        for i in range(len(self.RemainingDigits)):
            self.answer = self.answer + str(self.RemainingDigits[i])
            
        self.answer = self.answer + str(self.LastDigit)
        
        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = []
        
        while len(self.wrongAnswers) < 3:
            random.shuffle(self.digits)
            self.wrongAnswer = ''
            for i in range(len(self.digits)):
                self.wrongAnswer = self.wrongAnswer + str(self.digits[i])
            
            if self.wrongAnswer!=self.answer and self.wrongAnswer not in self.wrongAnswers:
                self.wrongAnswers.append(self.wrongAnswer)
        
        
        self.wrongAnswers.append(self.answer)
        
        random.shuffle(self.wrongAnswers)
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5c(self.problem,self.answer,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ5c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,
                'answer1':self.wrongAnswers[0],'answer2':self.wrongAnswers[1],'answer3':self.wrongAnswers[2],'answer4':self.wrongAnswers[3],
                'value1':self.wrongAnswers[0],'value2':self.wrongAnswers[1],'value3':self.wrongAnswers[2],'value4':self.wrongAnswers[3],}
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswer == 2:
            try:
                return (str(answer)==str(InputAnswer).lower())
            except ValueError:
                return False  
        elif CheckAnswer == 3:
            try:
                InputAnswer = str(InputAnswer)
                while  InputAnswer.partition(",")[1]!="":
                    InputAnswer = InputAnswer.partition(",")[0]+InputAnswer.partition(",")[2]
                    
                InputAnswer = string.join(InputAnswer.split(),"")
                answer = string.join(answer.split(),"")
                return InputAnswer == answer
            except ValueError:
                return False
        if CheckAnswer == 4:
            try:
                return (str(answer)==str(InputAnswer))
            except ValueError:
                return False

    def PlaceValueTable(self,number1,number2,number3,number4):
        colorOnes = 'purple'
        colorTens = 'dodgerblue'
        colorHundreds = 'hotpink'
        colorThousands = 'darkorange'
        
        thousands1,remHundreds1 = divmod(number1,1000)
        hundreds1,remTens1 = divmod(remHundreds1,100)
        tens1,ones1 = divmod(remTens1,10)
        
        thousands2,remHundreds2 = divmod(number2,1000)
        hundreds2,remTens2 = divmod(remHundreds2,100)
        tens2,ones2 = divmod(remTens2,10)
        
        thousands3,remHundreds3 = divmod(number3,1000)
        hundreds3,remTens3 = divmod(remHundreds3,100)
        tens3,ones3 = divmod(remTens3,10)
        
        thousands4,remHundreds4 = divmod(number4,1000)
        hundreds4,remTens4 = divmod(remHundreds4,100)
        tens4,ones4 = divmod(remTens4,10)

        figuresToWordsTable = "<br><br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        figuresToWordsTable = figuresToWordsTable + "<tr><td>&nbsp;</td><td style='background-color:%s;height:35px;width:150px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Thousands</font></td><td style='background-color:%s;height:35px;width:150px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Hundreds</font></td><td style='background-color:%s;height:35px;width:100px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Tens</font></td><td style='background-color:%s;height:35px;width:100px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Ones</font></td></tr>"%(colorThousands,colorHundreds,colorTens,colorOnes)
        figuresToWordsTable = figuresToWordsTable + "<tr><td style='width:80px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td></tr>"%(number1,thousands1,hundreds1,tens1,ones1)
        figuresToWordsTable = figuresToWordsTable + "<tr><td>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td></tr>"%(number2,thousands2,hundreds2,tens2,ones2)
        if number3>0:
            figuresToWordsTable = figuresToWordsTable + "<tr><td>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td></tr>"%(number3,thousands3,hundreds3,tens3,ones3)
            if number4>0:
                figuresToWordsTable = figuresToWordsTable + "<tr><td>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td></tr>"%(number4,thousands4,hundreds4,tens4,ones4)
        figuresToWordsTable = figuresToWordsTable + "</table><br><br>"
        
        return figuresToWordsTable 
    
    def ComparisonStatement(self,number1,number2,smallerGreater):
        thousands1,remHundreds1  = divmod(number1,1000)
        hundreds1,remTens1 = divmod(remHundreds1,100)
        tens1,ones1 = divmod(remTens1,10)
        
        thousands2,remHundreds2  = divmod(number2,1000)
        hundreds2,remTens2 = divmod(remHundreds2,100)
        tens2,ones2 = divmod(remTens2,10)
        
        comparisonStatement = "<font class='ExplanationFont'>"
        if thousands1>thousands2:
            comparisonStatement = comparisonStatement + "Compare the thousands. %d thousands is greater than %d thousands.<br><br>"%(thousands1,thousands2)
            if smallerGreater=="smaller":
                comparisonStatement = comparisonStatement + "So, %d is smaller than %d."%(number2,number1)
            else:
                comparisonStatement = comparisonStatement + "So, %d is greater than %d."%(number1,number2)
        elif thousands1<thousands2:
            comparisonStatement = comparisonStatement + "Compare the thousands. %d thousands is smaller than %d thousands.<br><br>"%(thousands1,thousands2)
            if smallerGreater=="smaller":
                comparisonStatement = comparisonStatement + "So, %d is smaller than %d."%(number1,number2)
            else:
                comparisonStatement = comparisonStatement + "So, %d is greater than %d."%(number2,number1)
        elif thousands1==thousands2:
            comparisonStatement = comparisonStatement + "First, compare the thousands. They are the same.<br><br>"
            if hundreds1>hundreds2:
                comparisonStatement = comparisonStatement + "Then, compare the hundreds. %d hundreds is greater than %d hundreds.<br><br>"%(hundreds1,hundreds2)
                if smallerGreater=="smaller":
                    comparisonStatement = comparisonStatement + "So, %d is smaller than %d."%(number2,number1)
                else:
                    comparisonStatement = comparisonStatement + "So, %d is greater than %d."%(number1,number2)
            elif hundreds1<hundreds2:
                comparisonStatement = comparisonStatement + "Then, compare the hundreds. %d hundreds is smaller than %d hundreds.<br><br>"%(hundreds1,hundreds2)
                if smallerGreater=="smaller":
                    comparisonStatement = comparisonStatement + "So, %d is smaller than %d."%(number1,number2)
                else:
                    comparisonStatement = comparisonStatement + "So, %d is greater than %d."%(number2,number1)
            elif hundreds1==hundreds2:
                comparisonStatement = comparisonStatement + "Next, compare the hundreds. They are the same.<br><br>"
                if tens1>tens2:
                    comparisonStatement = comparisonStatement + "Then, compare the tens. %d tens is greater than %d tens.<br><br>"%(tens1,tens2)
                    if smallerGreater=="smaller":
                        comparisonStatement = comparisonStatement + "So, %d is smaller than %d."%(number2,number1)
                    else:
                        comparisonStatement = comparisonStatement + "So, %d is greater than %d."%(number1,number2)
                elif tens1<tens2:
                    comparisonStatement = comparisonStatement + "Then, compare the tens. %d tens is smaller than %d tens.<br><br>"%(tens1,tens2)
                    if smallerGreater=="smaller":
                        comparisonStatement = comparisonStatement + "So, %d is smaller than %d."%(number1,number2)
                    else:
                        comparisonStatement = comparisonStatement + "So, %d is greater than %d."%(number2,number1)
                elif tens1==tens2:
                    comparisonStatement = comparisonStatement + "Then, compare the tens. They are the same.<br><br>"
                    if ones1>ones2:
                        comparisonStatement = comparisonStatement + "Finally, compare the ones. %d ones is greater than %d ones.<br><br>"%(ones1,ones2)
                        if smallerGreater=="smaller":
                            comparisonStatement = comparisonStatement + "So, %d is smaller than %d."%(number2,number1)
                        else:
                            comparisonStatement = comparisonStatement + "So, %d is greater than %d."%(number1,number2)
                    elif ones1<ones2:
                        comparisonStatement = comparisonStatement + "Finally, compare the ones. %d ones is smaller than %d ones.<br><br>"%(ones1,ones2)
                        if smallerGreater=="smaller":
                            comparisonStatement = comparisonStatement + "So, %d is smaller than %d."%(number1,number2)
                        else:
                            comparisonStatement = comparisonStatement + "So, %d is greater than %d."%(number2,number1)
                    elif ones1==ones2:
                        comparisonStatement = comparisonStatement + "Finally, compare the ones. They are the same.<br><br>"
                        comparisonStatement = comparisonStatement + "The two numbers are equal."
        
        comparisonStatement = comparisonStatement + "</font>"
        
        return comparisonStatement
