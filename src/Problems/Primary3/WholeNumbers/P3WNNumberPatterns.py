'''
Created on Feb 26, 2013
Module: P3WNNumberPatterns
Generates the Number Patterns problems for Primary 3

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

class P3WNNumberPatterns:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
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
        #return self.GenerateProblemType1()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        Complete the number pattern.
        1234, 1244, 1254, ________, 1274'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.numbers=[]

        self.pattern = random.choice([5,10,20,50,100,200,300,400,500,600,700,800,900,1000])
        
        self.number = randint(1000,9999-4*self.pattern)
        
        '''Adding the first number to the numbers list'''       
        self.numbers.append(str(self.number))
        
        for _i in range(4):
            self.number = self.number + self.pattern
            self.numbers.append(str(self.number))
        
        self.OriginalNumbers = list(self.numbers)
        
        missingNumber = randint(0,len(self.numbers)-1)
       
        self.answer = self.numbers[missingNumber]
        self.numbers[missingNumber] = "____"
        
        self.name = random.choice(PersonName.GirlName)
        self.items = ['stones','tiles','ribbons','eggs','paper bags','dry leaves','paper boats','shells','magnetic frames','paper balls']
        
        self.item = random.choice(self.items)
        
        self.problem1 = "Complete the number pattern.<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem2 = "Fill in the missing number in the number pattern below.<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem3 = "What is the missing number in the number pattern below?<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem4 = "A counting tape has numbers arranged in a pattern. Find the missing number in the counting tape below.<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem5 = "%s has some %s with numbers on them that she is arranging in a pattern. What is the missing number in %s's pattern?<br><br>%s, %s, %s, %s, %s"%(self.name,self.item,self.name,self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.OriginalNumbers,self.pattern)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def GenerateProblemType2(self):       
        '''e.g.:
        Complete the number pattern.
        1234, 1244, 1254, ________, 1274'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.numbers=[]

        self.pattern = random.choice([5,10,20,50,100,200,300,400,500,600,700,800,900,1000])
        
        self.number = randint(1000+4*self.pattern,9999)
        
        '''Adding the first number to the numbers list'''       
        self.numbers.append(str(self.number))
        
        for _i in range(4):
            self.number = self.number - self.pattern
            self.numbers.append(str(self.number))
                 
        self.OriginalNumbers = list(self.numbers)
        
        missingNumber = randint(0,len(self.numbers)-1)
       
        self.answer = self.numbers[missingNumber]
        self.numbers[missingNumber] = "____"
        
        self.name = random.choice(PersonName.GirlName)
        self.items = ['stones','tiles','ribbons','eggs','paper bags','dry leaves','paper boats','shells','magnetic frames','paper balls']
        
        self.item = random.choice(self.items)
        
        self.problem1 = "Complete the number pattern.<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem2 = "Fill in the missing number in the number pattern below.<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem3 = "What is the missing number in the number pattern below?<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem4 = "A counting tape has numbers arranged in a pattern. Find the missing number in the counting tape below.<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem5 = "%s has some %s with numbers on them that she is arranging in a pattern. What is the missing number in %s's pattern?<br><br>%s, %s, %s, %s, %s"%(self.name,self.item,self.name,self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.OriginalNumbers,self.pattern)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}
      
    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        Complete the number pattern.
        1234, 1244, 1254, ________, 1274'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.numbers=[]

        self.pattern = random.choice([5,10,20,50,100,200,300,400,500,600,700,800,900,1000])
        
        self.number = randint(1000,9999-4*self.pattern)
        
        '''Adding the first number to the numbers list'''       
        self.numbers.append(str(self.number))
        
        for _i in range(4):
            self.number = self.number + self.pattern
            self.numbers.append(str(self.number))

        self.OriginalNumbers = list(self.numbers)
                 
        missingNumber = randint(0,len(self.numbers)-1)
       
        self.answer = self.numbers[missingNumber]
        self.numbers[missingNumber] = "____"
        
        self.name = random.choice(PersonName.GirlName)
        self.items = ['stones','tiles','ribbons','eggs','paper bags','dry leaves','paper boats','shells','magnetic frames','paper balls']
        
        self.item = random.choice(self.items)
        
        self.problem1 = "Complete the number pattern.<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem2 = "Fill in the missing number in the number pattern below.<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem3 = "What is the missing number in the number pattern below?<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem4 = "A counting tape has numbers arranged in a pattern. Find the missing number in the counting tape below.<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem5 = "%s has some %s with numbers on them that she is arranging in a pattern. What is the missing number in %s's pattern?<br><br>%s, %s, %s, %s, %s"%(self.name,self.item,self.name,self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])
        
        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = [str(int(self.answer)+100),str(int(self.answer)-100),str(int(self.answer)+200),str(int(self.answer)-200),str(int(self.answer)+10),str(int(self.answer)-10)]
        
        self.wrongAnswers = random.sample(self.wrongAnswers,3)
        self.wrongAnswers.append(self.answer)
        
        random.shuffle(self.wrongAnswers)

                                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.OriginalNumbers,self.pattern)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'answer1':self.wrongAnswers[0],'answer2':self.wrongAnswers[1],'answer3':self.wrongAnswers[2],'answer4':self.wrongAnswers[3],
                'value1':self.wrongAnswers[0],'value2':self.wrongAnswers[1],'value3':self.wrongAnswers[2],'value4':self.wrongAnswers[3],}
      
    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        Complete the number pattern.
        1234, 1244, 1254, ________, 1274'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.numbers=[]

        self.pattern = random.choice([5,10,20,50,100,200,300,400,500,600,700,800,900,1000])
        
        self.number = randint(1000+4*self.pattern,9999)
        
        '''Adding the first number to the numbers list'''       
        self.numbers.append(str(self.number))
        
        for _i in range(4):
            self.number = self.number - self.pattern
            self.numbers.append(str(self.number))

        self.OriginalNumbers = list(self.numbers)
                         
        missingNumber = randint(0,len(self.numbers)-1)
       
        self.answer = self.numbers[missingNumber]
        self.numbers[missingNumber] = "____"
        
        self.name = random.choice(PersonName.GirlName)
        self.items = ['stones','tiles','ribbons','eggs','paper bags','dry leaves','paper boats','shells','magnetic frames','paper balls']
        
        self.item = random.choice(self.items)
        
        self.problem1 = "Complete the number pattern.<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem2 = "Fill in the missing number in the number pattern below.<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem3 = "What is the missing number in the number pattern below?<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem4 = "A counting tape has numbers arranged in a pattern. Find the missing number in the counting tape below.<br><br>%s, %s, %s, %s, %s"%(self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        self.problem5 = "%s has some %s with numbers on them that she is arranging in a pattern. What is the missing number in %s's pattern?<br><br>%s, %s, %s, %s, %s"%(self.name,self.item,self.name,self.numbers[0],self.numbers[1],self.numbers[2],self.numbers[3],self.numbers[4])
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])
        
        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = [str(int(self.answer)+100),str(int(self.answer)-100),str(int(self.answer)+200),str(int(self.answer)-200),str(int(self.answer)+10),str(int(self.answer)-10)]
        
        self.wrongAnswers = random.sample(self.wrongAnswers,3)
        self.wrongAnswers.append(self.answer)
        
        random.shuffle(self.wrongAnswers)

                                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.OriginalNumbers,self.pattern)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'answer1':self.wrongAnswers[0],'answer2':self.wrongAnswers[1],'answer3':self.wrongAnswers[2],'answer4':self.wrongAnswers[3],
                'value1':self.wrongAnswers[0],'value2':self.wrongAnswers[1],'value3':self.wrongAnswers[2],'value4':self.wrongAnswers[3],}

    def ExplainType1(self,problem,answer,originalNumbers,pattern):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Rule: Add %d to get the next number.<br><br>"%(pattern)
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + "<blockquote><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><font style='font-size:0.9em;'>+ %d</font></td><td>&nbsp;</td><td><font style='font-size:0.9em;'>+ %d</font></td><td>&nbsp;</td><td><font style='font-size:0.9em;'>+ %d</font></td><td>&nbsp;</td><td><font style='font-size:0.9em;'>+ %d</font></td></tr>"%(pattern,pattern,pattern,pattern)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/number_pattern_arrow.png' /></td><td>&nbsp;</td><td><img src='/images/explanation/number_pattern_arrow.png' /></td><td>&nbsp;</td><td><img src='/images/explanation/number_pattern_arrow.png' /></td><td>&nbsp;</td><td><img src='/images/explanation/number_pattern_arrow.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%s</td><td>&nbsp;</td><td style='text-align:left'>%s</td><td>&nbsp;</td><td style='text-align:left'>%s</td><td>&nbsp;</td><td style='text-align:left'>%s</td><td>&nbsp;</td><td style='text-align:left'>%s</td></tr>"%(originalNumbers[0],originalNumbers[1],originalNumbers[2],originalNumbers[3],originalNumbers[4])
        self.solution_text = self.solution_text + "</table></blockquote><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The missing number is %s.<br><br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def ExplainType2(self,problem,answer,originalNumbers,pattern):
        self.answer_text = "<br>The correct answer is:<br>%s"%(str(answer))

        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Rule: Subtract %d to get the next number.<br><br>"%(pattern)
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + "<blockquote><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><font style='font-size:0.9em;'>&minus; %d</font></td><td>&nbsp;</td><td><font style='font-size:0.9em;'>&minus; %d</font></td><td>&nbsp;</td><td><font style='font-size:0.9em;'>&minus; %d</font></td><td>&nbsp;</td><td><font style='font-size:0.9em;'>&minus; %d</font></td></tr>"%(pattern,pattern,pattern,pattern)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/number_pattern_arrow.png' /></td><td>&nbsp;</td><td><img src='/images/explanation/number_pattern_arrow.png' /></td><td>&nbsp;</td><td><img src='/images/explanation/number_pattern_arrow.png' /></td><td>&nbsp;</td><td><img src='/images/explanation/number_pattern_arrow.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%s</td><td>&nbsp;</td><td style='text-align:left'>%s</td><td>&nbsp;</td><td style='text-align:left'>%s</td><td>&nbsp;</td><td style='text-align:left'>%s</td><td>&nbsp;</td><td style='text-align:left'>%s</td></tr>"%(originalNumbers[0],originalNumbers[1],originalNumbers[2],originalNumbers[3],originalNumbers[4])
        self.solution_text = self.solution_text + "</table></blockquote><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The missing number is %s.<br><br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False