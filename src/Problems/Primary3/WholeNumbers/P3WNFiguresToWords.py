'''
Created on Feb 22, 2013
Module: P3WNFiguresToWords
Generates the Figures to Words problems for Primary 3

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
  

History:
  
'''
import random
import string
from random import randint
from Utils import Figures2Words
from Problems import PersonName
import logging

class P3WNFiguresToWords:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2a","ProblemType2b","ProblemType2c",],
                            3:["ProblemType3a","ProblemType3b","ProblemType3c","ProblemType3d",],
                            4:["ProblemType4a","ProblemType4b","ProblemType4c","ProblemType4d",],
                            5:["ProblemType5a","ProblemType5b","ProblemType5c",],
                            6:["ProblemType6a","ProblemType6b","ProblemType6c",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2a(),self.GenerateProblemType2b(),self.GenerateProblemType2c(),],
                                    3:[self.GenerateProblemType3a(),self.GenerateProblemType3b(),self.GenerateProblemType3c(),self.GenerateProblemType3d(),],
                                    4:[self.GenerateProblemType4a(),self.GenerateProblemType4b(),self.GenerateProblemType4c(),self.GenerateProblemType4d(),],
                                    5:[self.GenerateProblemType5a(),self.GenerateProblemType5b(),self.GenerateProblemType5c(),],
                                    6:[self.GenerateProblemType6a(),self.GenerateProblemType6b(),self.GenerateProblemType6c(),],
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
        #return self.GenerateProblemType6c()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2a":self.GenerateProblemType2a(),"ProblemType2b":self.GenerateProblemType2b(),"ProblemType2c":self.GenerateProblemType2c(),
                            "ProblemType3a":self.GenerateProblemType3a(),"ProblemType3b":self.GenerateProblemType3b(),"ProblemType3c":self.GenerateProblemType3c(),
                            "ProblemType3d":self.GenerateProblemType3d(),
                            "ProblemType4a":self.GenerateProblemType4a(),"ProblemType4b":self.GenerateProblemType4b(),"ProblemType4c":self.GenerateProblemType4c(),
                            "ProblemType4d":self.GenerateProblemType4d(),
                            "ProblemType5a":self.GenerateProblemType5a(),"ProblemType5b":self.GenerateProblemType5b(),"ProblemType5c":self.GenerateProblemType5c(),
                            "ProblemType6a":self.GenerateProblemType6a(),"ProblemType6b":self.GenerateProblemType6b(),"ProblemType6c":self.GenerateProblemType6c(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        Write the following number in words.
        9824 '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number = randint(1000,9999)
        self.problem = "Write the following number in words.:<br>"
        self.problem = self.problem + str(self.number)

        self.answer = self.FiguresToWordsStatement(self.number)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType1(self,problem,answer,number):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        self.solution_text = self.FiguresToWordsTable(number)
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;=&nbsp; %s"%(number,answer)
        self.solution_text = self.solution_text + "</font>" 
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2a(self):       
        '''e.g.:
            <An amusement park> received 1489 visitors. Write the number of visitors in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number = randint(1000,9999)
        self.items = ['An amusement park','A science museum','A water park','A theme park','A zoo','A bird park',
                      'An animal safari park','A vegetable farm','A strawberry farm','An art museum']
        
        self.item = random.choice(self.items)
        
        self.problem = "%s received %d visitors. Write the number of visitors in words."%(self.item,self.number)

        self.answer = self.FiguresToWordsStatement(self.number)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def GenerateProblemType2b(self):       
        '''e.g.:
            <A primary school> has 2658 <pupils>. Write the number of <pupils> in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number = randint(1000,9999)
        self.items = [['A primary school','pupils'],['A town','people'],['A company','employees'],['An island','residents'],['A forest','trees'],
                      ['A wildlife sanctuary','animals'],['A university','students'],['A library','books'],['A computer warehouse','computers'],
                      ['A bookstore','pens'],['A toy store','toys']]
        
        self.item = random.choice(self.items)
        
        self.problem = "%s has %d %s. Write the number of %s in words."%(self.item[0],self.number,self.item[1],self.item[1])

        self.answer = self.FiguresToWordsStatement(self.number)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def GenerateProblemType2c(self):       
        '''e.g.:
            [Person.Unclename] <has> $1239 <in his bank account>. Express this amount in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number = randint(1000,9999)
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['has','in his bank account'],['earned','last year'],['spent','on himself'],['gave','to charity'],['had','in his savings account'],
                      ['paid','in travel expenses'],['won','in lotto'],['gave','to his wife'],['spent','on air tickets for a holiday'],['received','as a bonus']]
        
        self.item = random.choice(self.items)
        
        self.problem = "%s %s $%d %s. Express this amount in words."%(self.name,self.item[0],self.number,self.item[1])

        self.answer = self.FiguresToWordsStatement(self.number)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType2(self,problem,answer,number):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        self.solution_text = self.FiguresToWordsTable(number)
                
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s.<br><br>"%(number,answer)
        self.solution_text = self.solution_text + "</font>" 
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3a(self):       
        '''e.g.:
            What is the sum of 1239 and 4567? Express your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(1000,4999)
        self.number2 = randint(1000,4999)
        self.number = self.number1 + self.number2
        
        self.problem1 = "What is the sum of %d and %d? Express your answer in words."%(self.number1,self.number2)
        self.problem2 = "Find the sum of %d and %d. Write your answer in words."%(self.number1,self.number2)
        
        self.problem = random.choice([self.problem1,self.problem2])

        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3a(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType3a(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1 + number2
        
        self.solution_text = "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "The sum of %d and %d is %d."%(number1,number2,number)
        self.solution_text = self.solution_text + "</font><br>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s."%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3b(self):       
        '''e.g.:
            [Person.name] <had> 5224 <beads> and [Person.name] <had> 2025 <beads>. How many <beads> did they <have> altogether? Express your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(1000,4999)
        self.number2 = randint(1000,4999)
        self.number = self.number1 + self.number2
        
        self.names = random.sample(PersonName.PersonName,2)
        
        self.items = [['had','beads','have'],['collected','stamps','collect'],['had','rubberbands','have'],['bought','buttons','buy'],
                      ['won','points','win'],['had','safety pins','have'],['bought','stickers','buy'],['collected','flags','collect'],
                      ['got','pins','get'],['had','tacks','have']]

        self.item = random.choice(self.items)
               
        self.problem = "%s %s %d %s and %s %s %d %s. How many %s did they %s altogether? Express your answer in words."%(self.names[0],self.item[0],self.number1,self.item[1],
                                                                                                                         self.names[1],self.item[0],self.number2,self.item[1],
                                                                                                                         self.item[1],self.item[2])

        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3b(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType3b(self,problem,answer,number1,number2,item0,item1):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1 + number2
        
        self.solution_text = "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "They %s %d %s altogether."%(item0,number,item1)
        self.solution_text = self.solution_text + "</font><br>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s."%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3c(self):       
        '''e.g.:
            <Town A has> 3589 <residents> and <Town B has> 2904 <residents>. What is the total <number of residents in the two towns>? Give your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(1000,4999)
        self.number2 = randint(1000,4999)
        self.number = self.number1 + self.number2
        
        self.items = [['Town A has','residents','Town B has','residents','number of residents in the two towns'],
                      ['Company A has','workers','Company B has','workers','number of workers in the two companies'],
                      ['Museum A has','paintings','Museum B has','paintings','number of paintings in the two museums'],
                      ['Store A has','movie CDs','Store B has','movie CDs','number of movie CDs in the two stores'],
                      ['Library A has','books','Library B has','books','number of books in the two libraries'],
                      ['Bakery A sold','muffins','Bakery B sold','muffins','number of muffins sold by the two bakeries'],
                      ['School A has','pipuls','School B has','pupils','number of pupils in the two schools'],
                      ['Ship A has','passengers','Ship B has','passengers','number of passengers on the two ships'],
                      ['Grocery Store A sold','cans of milk','Grocery Store B sold','cans of milk','number of cans of milk sold by the two grocery stores'],
                      ['Farmer A sold','eggs','Farmer B sold','eggs','number of eggs sold by the two farmers']]
               
        self.item = random.choice(self.items)
        
        self.problem = "%s %d %s and %s %d %s. What is the total %s? Give your answer in words."%(self.item[0], self.number1, self.item[1],
                                                                                                  self.item[2], self.number2, self.item[3],self.item[4])
        
        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3c(self.problem,self.answer,self.number1,self.number2,self.item[4])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType3c(self,problem,answer,number1,number2,item4):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1 + number2
        
        self.solution_text = "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "The total %s is %d."%(item4,number)
        self.solution_text = self.solution_text + "</font><br>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s."%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3d(self):       
        '''e.g.:
            <A grocery store sold> 2904 <chicken eggs> and 1290 <duck eggs>. How many <eggs did the grocery store sell> altogether? Give your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(1000,4999)
        self.number2 = randint(1000,4999)
        self.number = self.number1 + self.number2
        
        self.items = [['A grocery store sold','chicken eggs','duck eggs','eggs did the grocery store sell','The grocery store sold','eggs'],
                      ['A fruiterer had','apples','oranges','fruits did the fruiterer have','The fruiterer had','fruits'],
                      ['A farmer had','hens','ducks','birds did the farmer have','The farmer had','birds'],
                      ['A phone shop sold','SIM cards','calling cards','cards did the phone shop sell','The phone shop sold','cards'],
                      ['A post office sold','envelopes','stamps','envelopes and stamps did the post office sell','The post office sold','envelopes and stamps'],
                      ['A supermarket had','bags of rice','bags of sugar','bags of rice and sugar did the supermarket have','The supermarket had','bags of rice and sugar'],
                      ['An amusement park received','adults','children','people did the amusement park receive','The amusement park received','people'],
                      ['A school had','boys','girls','children did the school have','The school had','children'],
                      ['A library had','books','DVDs','books and DVDs did the library have','The library had','books and DVDs'],
                      ['A bakery sold','cupcakes','muffins','cupcakes and muffins did the bakery sell','The bakery sold','cupcakes and muffins']]
        
        self.item = random.choice(self.items)
        
        self.problem = "%s %d %s and %d %s. How many %s altogether? Give your answer in words."%(self.item[0],self.number1,self.item[1],self.number2,
                                                                                                 self.item[2],self.item[3])

        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3d(self.problem,self.answer,self.number1,self.number2,self.item[4],self.item[5])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3d",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType3d(self,problem,answer,number1,number2,item4,item5):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1 + number2
        
        self.solution_text = "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "%s %d %s altogether."%(item4,number,item5)
        self.solution_text = self.solution_text + "</font><br>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s."%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4a(self):       
        '''e.g.:
            What is the difference between 4567 and 1234? Express your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(5999,9999)
        self.number2 = randint(1000,4499)
        
        self.number = self.number1 - self.number2
        
        self.problem = "What is the difference between %d and %d? Express your answer in words."%(self.number1,self.number2)
        
        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4a(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType4a(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1 - number2
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "The difference between %d and %d is %d.<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s."%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4b(self):       
        '''e.g.:
            [Person.Girlname] had 5224 <beads>. She gave away 2028 <beads> to her <sister/friend/cousin/buddy>. How many <beads> has she left now? Write your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(5999,9999)
        self.number2 = randint(1000,4499)
        
        self.number = self.number1 - self.number2
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = ['beads','stamps','rubberbands','buttons','pushpins','safety pins','stickers','flags','pins','tacks']
        
        self.item = random.choice(self.items)
        self.item1 = random.choice(['sister','friend','cousin','buddy'])
                      
        self.problem = "%s had %d %s. She gave away %d %s to her %s. How many %s had she left? Write your answer in words."%(self.name,self.number1,self.item,
                                                                                                                                 self.number2,self.item,self.item1,self.item)
        
        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4b(self.problem,self.answer,self.number1,self.number2,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType4b(self,problem,answer,number1,number2,item):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1 - number2
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "She had %d %s left.<br>"%(number,item)
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s."%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4c(self):       
        '''e.g.:
            There were 8467 <birds in a village>. 1239 <birds migrated out of the village>. How many <birds were left in the village>? Give your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(5999,9999)
        self.number2 = randint(1000,4499)
        
        self.number = self.number1 - self.number2
        
        self.items1 = [['birds in a village','birds migrated out of the village','birds were left in the village'],
                       ['children who took a maths test','children got 5 stars on the maths test','children did not get 5 stars on the maths test'],
                       ['workers in a factory','workers left the factory','workers were left in the factory'],
                       ['people on a beach','people left the beach','people were left on the beach'],
                       ['spectators in a stadium','spectators left the stadium','spectators were left in the stadium'],
                       ['passengers at a railway station','passengers boarded a train','passengers were left at the railway station'],
                       ['beads at first','beads were used to make a necklace','beads were left'],
                       ['plants at a nursery','plants were sold','plants were left'],
                       ['loaves of bread made by a bakery','loaves of bread were sold','loaves of bread were left unsold'],
                       ['oranges in a farm','oranges were picked','oranges were left in the farm']]
        
        self.items2 = [['birds living in a village migrated away from the village','birds were left in the village'],
                       ['children who took a test got 5 stars on the test','children did not get 5 stars on the test'],
                       ['workers who work in a factory left the factory','workers were left in the factory'],
                       ['people who were on a beach left the beach','people were left on the beach'],
                       ['spectators who were watching a soccer game in a stadium left the stadium','spectators were left in the stadium'],
                       ['passengers who were waiting at a railway station boarded a train','passengers were left at the railway station'],
                       ['beads were used to make a necklace','beads were left'],['plants at a nursery were sold','plants were left'],
                       ['loaves of bread made by a bakery were sold','loaves of bread were left unsold'],
                       ['oranges in a farm were picked','oranges were left in the farm']]
        
        
        self.item1 = random.choice(self.items1)
        self.item2 = random.choice(self.items2)
                      
        self.problem1 = "There were %d %s. %d %s. How many %s? Give your answer in words."%(self.number1,self.item1[0],self.number2,self.item1[1],self.item1[2])
        self.problem2 = "%d out of %d %s. How many %s? Give your answer in words."%(self.number2,self.number1,self.item2[0],self.item2[1])
        
        self.flag = randint(1,2)
        if self.flag==1: 
            self.problem = self.problem1
            self.left = self.item1[2]
        else:
            self.problem = self.problem2
            self.left = self.item2[1]
        
        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4c(self.problem,self.answer,self.number1,self.number2,self.left)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType4c(self,problem,answer,number1,number2,left):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1 - number2
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "%d %s.<br>"%(number,left)
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s."%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain


    def GenerateProblemType4d(self):       
        '''e.g.:
            <A grocery store sold> 2904 <chicken eggs> and 1290 <duck eggs>. How many more <chicken eggs than duck eggs did the grocery store sell>? Give your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(5999,9999)
        self.number2 = randint(1000,4499)
        
        self.number = self.number1 - self.number2
        
        self.items = [['A grocery store sold','chicken eggs','duck eggs','chicken eggs than duck eggs did the grocery store sell','The grocery store sold'],
                      ['A fruiterer had','mangoes','guavas','mangoes than guavas did the fruiterer have','The fruiterer had'],
                      ['A farmer had','carrots','radishes','carrots than radishes did the farmer have','The farmer had'],
                      ['A phone shop sold','calling cards','SIM cards','calling cards than SIM cards did the phone shop sell','The phone shop sold'],
                      ['A post office sold','stamps','envelopes','stamps than envelopes did the post office sell','The post office sold'],
                      ['A supermarket had','bags of rice','bags of sugar','bags of rice than sugar did the supermarket have','The supermarket had'],
                      ['An amusement park received','adults','children','adults than children did the amusement park receive','The amusement park received'],
                      ['A school had','boys','girls','boys than girls did the school have','The school had'],
                      ['A library had','books','DVDs','books than DVDs did the library have','The library had'],
                      ['A bakery sold','cupcakes','muffins','cupcakes than muffins did the bakery sell','The bakery sold']]        
        
        
        self.item = random.choice(self.items)
                      
        self.problem = "%s %d %s and %d %s. How many more %s? Give your answer in words."%(self.item[0],self.number1,self.item[1],self.number2,self.item[2],self.item[3])
        
        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4d(self.problem,self.answer,self.number1,self.number2,self.item[1],self.item[2],self.item[4])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4d",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType4d(self,problem,answer,number1,number2,item1,item2,item4):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1 - number2
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "%s %d more %s than %s.<br>"%(item4,number,item1,item2)
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s."%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain


    def GenerateProblemType5a(self):       
        '''e.g.:
            Find the product of 1234 and 4. Express your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(1001,1110)
        self.number2 = randint(4,7)
        
        self.number = self.number1 * self.number2
        
        self.problem1 = "Find the product of %d and %d. Express your answer in words."%(self.number1,self.number2)
        self.problem2 = "What is %d &times; %d? Write your answer in words."%(self.number1,self.number2)
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5a(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType5a(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1 * number2
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "The product of %d and %d is %d.<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s.<br><br>"%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5b(self):       
        '''e.g.:
            The cost of a <computer> is $750. What is the cost of 4 such <computers>? Write your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(750,1400)
        self.number2 = randint(4,7)
        
        self.number = self.number1 * self.number2
        
        self.items = [['computer','computers'],['sofa set','sofa sets'],['diamond ring','diamond rings'],['bed','beds'],['TV set','TV sets'],
                      ['dining table set','dining table sets'],['camera','cameras'],['book shelf','book shelves'],['home entertainment system','home entertainment systems']
                      ,['laptop','laptops']]
        
        self.item = random.choice(self.items)
        
        self.problem = "The cost of a %s is $%d. What is the cost of %d such %s? Write your answer in words."%(self.item[0],self.number1,self.number2,self.item[1])
        
        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5b(self.problem,self.answer,self.number1,self.number2,self.item[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType5b(self,problem,answer,number1,number2,item1):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1 * number2
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>$%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; $%d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "The cost of %d such %s is $%d.<br>"%(number2,item1,number)
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s.<br><br>"%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5c(self):       
        '''e.g.:
            <Person.Unclename> gives away 500 <marbles> to each of his 4 <pupils / sons / nephews / children>. How many <marbles> does he give away altogether? Give your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(750,1400)
        self.number2 = randint(4,7)
        
        self.number = self.number1 * self.number2
        
        self.name = random.choice(PersonName.UncleName)
                              
        self.items = ['marbles','stamps','stickers','flags','rubberbands','buttons','keyrings','darts','animal cards','cards']
              
        self.item = random.choice(self.items)
        
        self.item1 = random.choice(['pupils','nephews'])
        
        self.problem = "%s gives away %d %s to each of his %d %s. How many %s does he give away altogether? Give your answer in words."%(self.name,self.number1,self.item,
                                                                                                                                         self.number2,self.item1,self.item)
        
        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5c(self.problem,self.answer,self.number1,self.number2,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType5c(self,problem,answer,number1,number2,item):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1 * number2
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "He gives away %d %s altogether.<br>"%(number,item)
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s.<br><br>"%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6a(self):       
        '''e.g.:
            What is 5200 &divide; 4? Express your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number = randint(1011,1400)
        self.number2 = randint(4,7)
        
        self.number1 = self.number * self.number2
        
        self.problem1 = "What is %d &divide; %d? Express your answer in words."%(self.number1,self.number2)
        self.problem2 = "Write the quotient of %d &divide; %d in words."%(self.number1,self.number2)
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6a(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType6a(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1/number2
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "The quotient of %d &divide; %d is %d.<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s.<br><br>"%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
   
    def GenerateProblemType6b(self):       
        '''e.g.:
            4 <friends / brothers / cousins> <divided / shared> 4600 <marbles> equally among themselves. How many marbles did each <friend / brother / cousin> get? Express your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number = randint(1011,1400)
        self.number2 = randint(4,7)
        
        self.number1 = self.number * self.number2
        
        self.items = ['marbles','stamps','stickers','flags','rubberbands','buttons','keyrings','darts','animal cards','cards']
        
        self.item = random.choice(self.items)
        
        self.item1 = random.choice(['friend','brother','cousin'])
        
        self.item2 = random.choice(['divided','shared'])
        
        self.problem = "%d %ss %s %d %s equally among themselves. How many %s did each %s get? Express your answer in words."%(self.number2,self.item1,self.item2,self.number1,
                                                                                                                              self.item,self.item,self.item1)
        
        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6b(self.problem,self.answer,self.number1,self.number2,self.item1,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType6b(self,problem,answer,number1,number2,item1,item):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1/number2
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "Each %s got %d %s.<br>"%(item1,number,item)
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s.<br><br>"%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
   
    def GenerateProblemType6c(self):       
        '''e.g.:
            <Person.Unclename> paid $4000 for 4 identical <computers>. What was the cost of each <computer>? Give your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number = randint(1011,1400)
        self.number2 = randint(4,7)
        
        self.number1 = self.number * self.number2
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['computers','computer'],['sofa sets','sofa set'],['diamond rings','diamond ring'],['beds','bed'],['TV sets','TV set']
                      ,['dining table sets','dining table set'],['cameras','camera'],['book shelves','book shelf'],['home entertainment systems','home entertainment system'],
                      ['laptops','laptop']]
        
        self.item = random.choice(self.items)
        
        self.problem = "%s paid $%d for %d identical %s. What was the cost of each %s? Give your answer in words."%(self.name,self.number1,self.number2,self.item[0],
                                                                                                                    self.item[1])
                                                                                                                    
        self.answer = self.FiguresToWordsStatement(self.number)        
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6c(self.problem,self.answer,self.number1,self.number2,self.item[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType6c(self,problem,answer,number1,number2,item1):
        self.answer_text = "<br>The correct answer is:<br>"+answer

        number = number1/number2
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>$%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; $%d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "The cost of each %s was $%d.<br>"%(item1,number)
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + self.FiguresToWordsTable(number)        
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "In words, we write %d as %s.<br><br>"%(number,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
      
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        ''' Check the answers with the InputAnswer. It removes all white spaces, "and" and special characters like 
        ("-",",","." so that this method can return true as long as main keywords match)'''
        
        if (template=="MCQTypeProblems.html"):
            InputAnswer= string.join(InputAnswer.split(),"")
            answer = string.join(answer.split(),"")
        else:            
            ''' removing " and" with a space in front so that it doesn't remove and from "thousand" '''
            while  answer.partition(" and")[1]!="":
                answer = answer.partition(" and")[0]+answer.partition(" and")[2]
            while  answer.partition(",")[1]!="":
                answer = answer.partition(",")[0]+answer.partition(",")[2]
            while  answer.partition("-")[1]!="":
                answer = answer.partition("-")[0]+answer.partition("-")[2]
            while  answer.partition(".")[1]!="":
                answer = answer.partition(".")[0]+answer.partition(".")[2]

            answer = string.join(answer.split(),"")
            InputAnswer = str(InputAnswer)
            while  InputAnswer.partition(" and")[1]!="":
                InputAnswer = InputAnswer.partition(" and")[0]+InputAnswer.partition(" and")[2]
            while  InputAnswer.partition(",")[1]!="":
                InputAnswer = InputAnswer.partition(",")[0]+InputAnswer.partition(",")[2]
            while  InputAnswer.partition("-")[1]!="":
                InputAnswer = InputAnswer.partition("-")[0]+InputAnswer.partition("-")[2]
            while  InputAnswer.partition(".")[1]!="":
                InputAnswer = InputAnswer.partition(".")[0]+InputAnswer.partition(".")[2]

            InputAnswer = string.join(InputAnswer.split(),"")
            
        return (InputAnswer.lower()==answer.lower())                           
   
    def FiguresToWordsTable(self,number):
        colorOnes = 'purple'
        colorTens = 'dodgerblue'
        colorHundreds = 'hotpink'
        colorThousands = 'darkorange'
        
        thousands,remHundreds  = divmod(number,1000)
        hundreds,remTens = divmod(remHundreds,100)
        tens,ones = divmod(remTens,10)
        
        figureToWords = [[0,'-'],[1,'one'],[2,'two'],[3,'three'],[4,'four'],[5,'five'],[6,'six'],[7,'seven'],[8,'eight'],[9,'nine']]
        figureToWordsTens = [[0,'-'],[1,'one'],[2,'twenty'],[3,'thirty'],[4,'forty'],[5,'fifty'],[6,'sixty'],[7,'seventy'],[8,'eighty'],[9,'ninety']]
        figureToWords1Tens = [[0,'ten'],[1,'eleven'],[2,'twelve'],[3,'thirteen'],[4,'fourteen'],[5,'fifteen'],[6,'sixteen'],[7,'seventeen'],[8,'eighteen'],[9,'nineteen']]
        
        figuresToWordsTable = "<br><br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        figuresToWordsTable = figuresToWordsTable + "<tr><td style='background-color:%s;height:35px;width:150px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Thousands</font></td><td style='background-color:%s;height:35px;width:150px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Hundreds</font></td><td style='background-color:%s;height:35px;width:100px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Tens</font></td><td style='background-color:%s;height:35px;width:100px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Ones</font></td></tr>"%(colorThousands,colorHundreds,colorTens,colorOnes)
        figuresToWordsTable = figuresToWordsTable + "<tr><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td><td style='height:60px;border:white solid 1px;'>%d</td></tr>"%(thousands,hundreds,tens,ones)
        figuresToWordsTable = figuresToWordsTable + "<tr><td style='padding:0'><img src='/images/explanation/P3_model_arrow_thousands.png' /></td><td style='padding:0'><img src='/images/explanation/P3_model_arrow_hundreds.png' /></td>"
        if tens==1:
            figuresToWordsTable = figuresToWordsTable + "<td colspan=2 style='padding:0'><img src='/images/explanation/P3_model_arrow_1tens.png' /></td></tr>"
        else:
            figuresToWordsTable = figuresToWordsTable + "<td style='padding:0'><img src='/images/explanation/P3_model_arrow_tens.png' /></td><td style='padding:0'><img src='/images/explanation/P3_model_arrow_ones.png' /></td></tr>"
        
        figuresToWordsTable = figuresToWordsTable + "<tr>"
        if thousands>0:
            figuresToWordsTable = figuresToWordsTable + "<td style='height:35px;white-space:nowrap;'>%s thousand</td>"%(figureToWords[thousands][1])
        else:
            figuresToWordsTable = figuresToWordsTable + "<td style='height:35px;white-space:nowrap;'>%s</td>"%(figureToWords[thousands][1])
        if hundreds>0:
            figuresToWordsTable = figuresToWordsTable + "<td style='height:35px;white-space:nowrap;'>%s hundred</td>"%(figureToWords[hundreds][1])
        else:
            figuresToWordsTable = figuresToWordsTable + "<td style='height:35px;white-space:nowrap;'>%s</td>"%(figureToWords[hundreds][1])
        if tens==0:
            figuresToWordsTable = figuresToWordsTable + "<td style='height:35px;white-space:nowrap;'>%s</td>"%(figureToWords[0][1])
            figuresToWordsTable = figuresToWordsTable + "<td style='height:35px;white-space:nowrap;'>%s</td>"%(figureToWords[ones][1])
        elif tens==1:
            figuresToWordsTable = figuresToWordsTable + "<td colspan=2 style='height:35px;white-space:nowrap;'>%s</td>"%(figureToWords1Tens[ones][1])
        else:
            figuresToWordsTable = figuresToWordsTable + "<td style='height:35px;white-space:nowrap;'>%s</td>"%(figureToWordsTens[tens][1])
            figuresToWordsTable = figuresToWordsTable + "<td style='height:35px;white-space:nowrap;'>%s</td>"%(figureToWords[ones][1])
        figuresToWordsTable = figuresToWordsTable + "</tr>"
        figuresToWordsTable = figuresToWordsTable + "</table><br><br>"
        
        return figuresToWordsTable 
    
    def FiguresToWordsStatement(self,number):
        
        thousands,remHundreds  = divmod(number,1000)
        hundreds,remTens = divmod(remHundreds,100)
        tens,ones = divmod(remTens,10)
        
        figureToWords = [[0,'-'],[1,'one'],[2,'two'],[3,'three'],[4,'four'],[5,'five'],[6,'six'],[7,'seven'],[8,'eight'],[9,'nine']]
        figureToWordsTens = [[0,'-'],[1,'one'],[2,'twenty'],[3,'thirty'],[4,'forty'],[5,'fifty'],[6,'sixty'],[7,'seventy'],[8,'eighty'],[9,'ninety']]
        figureToWords1Tens = [[0,'ten'],[1,'eleven'],[2,'twelve'],[3,'thirteen'],[4,'fourteen'],[5,'fifteen'],[6,'sixteen'],[7,'seventeen'],[8,'eighteen'],[9,'nineteen']]
        
        figuresToWords = ""
        if thousands>0:
            figuresToWords = figuresToWords + "%s thousand"%(figureToWords[thousands][1])

        if hundreds>0:
            if tens>0 or ones>0:
                figuresToWords = figuresToWords + ", "
            else:
                figuresToWords = figuresToWords + " and "
            figuresToWords = figuresToWords + "%s hundred"%(figureToWords[hundreds][1])
        '''else:
            if tens>0 or ones>0:
                figuresToWords = figuresToWords + " and "'''

        if tens==0:
            if ones!=0:
                figuresToWords = figuresToWords + " and "
                figuresToWords = figuresToWords + "%s"%(figureToWords[ones][1])
        elif tens==1:
            figuresToWords = figuresToWords + " and "
            figuresToWords = figuresToWords + "%s"%(figureToWords1Tens[ones][1])
        else:
            figuresToWords = figuresToWords + " and "
            figuresToWords = figuresToWords + "%s"%(figureToWordsTens[tens][1])
            if ones>0:
                figuresToWords = figuresToWords + "-"
                figuresToWords = figuresToWords + "%s"%(figureToWords[ones][1])
        
        return figuresToWords 