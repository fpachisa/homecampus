'''
Created on Feb 23, 2013
Module: P3WNWordsToFigures
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

class P3WNWordsToFigures:
    
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
                            "ProblemType3a":self.GenerateProblemType3a(),"ProblemType3b":self.GenerateProblemType3b(),
                            "ProblemType3c":self.GenerateProblemType3c(),"ProblemType3d":self.GenerateProblemType3d(),
                            "ProblemType4a":self.GenerateProblemType4a(),"ProblemType4b":self.GenerateProblemType4b(),
                            "ProblemType4c":self.GenerateProblemType4c(),"ProblemType4d":self.GenerateProblemType4d(),
                            "ProblemType5a":self.GenerateProblemType5a(),"ProblemType5b":self.GenerateProblemType5b(),"ProblemType5c":self.GenerateProblemType5c(),
                            "ProblemType6a":self.GenerateProblemType6a(),"ProblemType6b":self.GenerateProblemType6b(),"ProblemType6c":self.GenerateProblemType6c(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        Write the following number in <numerals / figures>.
        9824 '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number = randint(1000,9999)
        self.NumberInWords = self.FiguresToWordsStatement(self.number)
        
        self.item = random.choice(['numerals','figures'])
        
        self.problem = "Write the following number in %s:<br><br>%s"%(self.item,self.NumberInWords)

        self.answer = self.number
        
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
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number)
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>So,<br>&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%s &nbsp;=&nbsp; %d"%(self.FiguresToWordsStatement(number),number)
        self.solution_text = self.solution_text + "</font>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2a(self):       
        '''e.g.:
            <An amusement park> received 1489 visitors. Write the number of visitors in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number = randint(1000,9999)
        self.NumberInWords = self.FiguresToWordsStatement(self.number)
        self.items = ['An amusement park','A science museum','A water park','A theme park','A zoo','A bird park',
                      'An animal safari park','A vegetable farm','A strawberry farm','An art museum']
        
        self.item = random.choice(self.items)
        
        self.item1 = random.choice(['figures','numerals'])
        
        self.problem = "%s received %s visitors. Write the number of visitors in %s."%(self.item,self.NumberInWords,self.item1)

        self.answer = self.number
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'dollar_unit':self.dollar_unit}

    def GenerateProblemType2b(self):       
        '''e.g.:
            <A primary school> has 2658 <pupils>. Write the number of <pupils> in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number = randint(1000,9999)
        self.NumberInWords = self.FiguresToWordsStatement(self.number)
        self.items = [['A primary school','pupils'],['A town','people'],['A company','employees'],['An island','residents'],['A forest','trees'],
                      ['A wildlife sanctuary','animals'],['A university','students'],['A library','books'],['A computer warehouse','computers'],
                      ['A bookstore','pens'],['A toy store','toys']]
        
        self.item = random.choice(self.items)
        
        self.item1 = random.choice(['figures','numerals'])
        
        self.problem = "%s has %s %s. Write the number of %s in %s."%(self.item[0],self.NumberInWords,self.item[1],self.item[1],self.item1)

        self.answer = self.number
        self.dollar_unit = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'dollar_unit':self.dollar_unit}

    def GenerateProblemType2c(self):       
        '''e.g.:
            [Person.Unclename] <has> $1239 <in his bank account>. Express this amount in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number = randint(1000,9999)
        self.NumberInWords = self.FiguresToWordsStatement(self.number)
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['has','in his bank account'],['earned','last year'],['spent','on himself'],['gave','to charity'],['had','in his savings account'],
                      ['paid','in travel expenses'],['won','in lotto'],['gave','to his wife'],['spent','on air tickets for a holiday'],['received','as a bonus']]
        
        self.item = random.choice(self.items)
        
        self.item1 = random.choice(['figures','numerals'])
        
        self.problem = "%s %s %s dollars %s. Express this amount in %s."%(self.name,self.item[0],self.NumberInWords,self.item[1],self.item1)

        self.answer = self.number
        self.dollar_unit = "$"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,number,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%d"%(dollar_unit,answer)

        self.solution_text = self.WordsToFiguresTable(number)
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>So,<br>&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%s &nbsp;=&nbsp; %d"%(self.FiguresToWordsStatement(number),number)
        self.solution_text = self.solution_text + "</font>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3a(self):       
        '''e.g.:
            What do you get when you add one hundred and thirty to four thousand and seven? Express your answer in <numerals / figures>.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(1000,4999)
        self.number2 = randint(1000,4999)
        self.number = self.number1 + self.number2
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
        self.NumberInWords2 = self.FiguresToWordsStatement(self.number2)
               
        self.item1 = random.choice(['figures','numerals'])
        
        self.problem = "What do you get when you add %s and %s? Express your answer in %s."%(self.NumberInWords1,self.NumberInWords2,self.item1)

        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3a(self.problem,self.answer,self.number,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType3a(self,problem,answer,number,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + self.WordsToFiguresTable(number2)
        self.solution_text = self.solution_text + "<br><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "Now, add.<br>%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
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
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
        self.NumberInWords2 = self.FiguresToWordsStatement(self.number2)
        
        self.names = random.sample(PersonName.PersonName,2)
        
        self.items = [['had','beads','have'],['collected','stamps','collect'],['had','rubberbands','have'],['bought','buttons','buy'],
                      ['won','points','win'],['had','safety pins','have'],['bought','stickers','buy'],['collected','flags','collect'],
                      ['got','pins','get'],['had','tacks','have']]

        self.item = random.choice(self.items)
        
        self.item1 = random.choice(['figures','numerals'])
               
        self.problem = "%s %s %s %s and %s %s %s %s. How many %s did they %s altogether? Express your answer in %s."%(self.names[0],self.item[0],self.NumberInWords1,
                                                                                                                      self.item[1],self.names[1],self.item[0],
                                                                                                                      self.NumberInWords2,self.item[1],
                                                                                                                      self.item[1],self.item[2],self.item1)

        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3b(self.problem,self.answer,self.number,self.number1,self.number2,self.names,self.item[0],self.item[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType3b(self,problem,answer,number,number1,number2,names,item0,item1):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s %s %d %s."%(names[0],item0,number1,item1)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + self.WordsToFiguresTable(number2)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s %s %d %s."%(names[1],item0,number2,item1)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "They %s %d %s altogether."%(item0,number,item1)
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
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
        self.NumberInWords2 = self.FiguresToWordsStatement(self.number2)
        
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
        
        self.item1 = random.choice(['figures','numerals'])
        
        self.problem = "%s %s %s and %s %s %s. What is the total %s? Give your answer in %s."%(self.item[0], self.NumberInWords1, self.item[1],
                                                                                                  self.item[2], self.NumberInWords2, self.item[3],self.item[4],self.item1)
        
        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3c(self.problem,self.answer,self.number,self.number1,self.number2,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType3c(self,problem,answer,number,number1,number2,item):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s %d %s."%(item[0],number1,item[1])
        self.solution_text = self.solution_text + "</font><br><br>" 
        
        self.solution_text = self.solution_text + self.WordsToFiguresTable(number2)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s %d %s."%(item[2],number2,item[3])
        self.solution_text = self.solution_text + "</font><br><br>" 

        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "The total %s is %d."%(item[4],number)
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
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
        self.NumberInWords2 = self.FiguresToWordsStatement(self.number2)
               
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
        
        self.item1 = random.choice(['figures','numerals'])
        
        self.problem = "%s %s %s and %s %s. How many %s altogether? Give your answer in %s."%(self.item[0],self.NumberInWords1,self.item[1],self.NumberInWords2,
                                                                                                 self.item[2],self.item[3],self.item1)

        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3d(self.problem,self.answer,self.number,self.number1,self.number2,self.item[1],self.item[2],self.item[4],self.item[5])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3d",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType3d(self,problem,answer,number,number1,number2,item1,item2,item4,item5):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s %d %s."%(item4,number1,item1)
        self.solution_text = self.solution_text + "</font><br><br>" 
        
        self.solution_text = self.solution_text + self.WordsToFiguresTable(number2)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s %d %s."%(item4,number2,item2)
        self.solution_text = self.solution_text + "</font><br><br>" 

        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "%s %d %s altogether."%(item4,number,item5)
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
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
        self.NumberInWords2 = self.FiguresToWordsStatement(self.number2)
                      
        self.item1 = random.choice(['figures','numerals'])
                              
        self.problem1 = "What is the difference between %s and %s? Express your answer in %s."%(self.NumberInWords1,self.NumberInWords2,self.item1)
        self.problem2 = "What do you get when you subtract %s from %s? Express your answer in %s."%(self.NumberInWords2,self.NumberInWords1,self.item1)
        self.problem3 = "Find the difference between %s and %s. Give your answer in %s."%(self.NumberInWords1,self.NumberInWords2,self.item1)
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4a(self.problem,self.answer,self.number,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType4a(self,problem,answer,number,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + self.WordsToFiguresTable(number2)
        self.solution_text = self.solution_text + "<br><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "Now, subtract.<br>%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
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
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
        self.NumberInWords2 = self.FiguresToWordsStatement(self.number2)
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = ['beads','stamps','rubberbands','buttons','pushpins','safety pins','stickers','flags','pins','tacks']
        
        self.item = random.choice(self.items)
        self.item1 = random.choice(['sister','friend','cousin','buddy'])
        self.item2 = random.choice(['figures','numerals'])
                      
        self.problem = "%s had %s %s. She gave away %s %s to her %s. How many %s had she left? Write your answer in %s."%(self.name,self.NumberInWords1,self.item,
                                                                                                                                 self.NumberInWords2,self.item,self.item1,self.item,
                                                                                                                                 self.item2)
        
        self.unit = self.item
        
        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4b(self.problem,self.answer,self.number,self.number1,self.number2,self.name,self.item,self.item1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":self.unit}

    def ExplainType4b(self,problem,answer,number,number1,number2,name,item,item1):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s had %d %s."%(name,number1,item)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + self.WordsToFiguresTable(number2)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "She gave away %d %s to her %s."%(number2,item,item1)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "She had %d %s left."%(number,item)
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
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
        self.NumberInWords2 = self.FiguresToWordsStatement(self.number2)

        self.items = [['birds in a village','birds migrated out of the village','birds were left in the village','There were','birds in the village at first','birds migrated out of the village'],
                       ['children who took a maths test','children got 5 stars on the maths test','children did not get 5 stars on the maths test','','children took the maths test','children got 5 stars on the maths test'],
                       ['workers in a factory','workers left the factory','workers were left in the factory','There were','workers in the factory at first','workers left the factory'],
                       ['people on a beach','people left the beach','people were left on the beach','There were','people on the beach at first','people left the beach'],
                       ['spectators in a stadium','spectators left the stadium','spectators were left in the stadium','There were','spectators in the stadium at first','spectators left the stadium'],
                       ['passengers at a railway station','passengers boarded a train','passengers were left at the railway station','There were','passengers at the railway station at first','passengers boarded the train'],
                       ['beads at first','beads were used to make a necklace','beads were left','There were','beads at first','beads were used to make the necklace'],
                       ['plants at a nursery','plants were sold','plants were left at the nursery','There were','plants at the nursery at first','plants were sold'],
                       ['loaves of bread made by a bakery','loaves of bread were sold','loaves of bread were left unsold','The bakery made','loaves of bread','loaves of bread were sold'],
                       ['oranges in a farm','oranges were picked','oranges were left in the farm','There were','oranges in the farm at first','oranges were picked']]
        
        self.item = random.choice(self.items)
        
        self.item3 = random.choice(['figures','numerals'])
                      
        self.problem = "There were %s %s. Then, %s %s. How many %s? Give your answer in %s."%(self.NumberInWords1,self.item[0],self.NumberInWords2,self.item[1],self.item[2],self.item3)
        
        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4c(self.problem,self.answer,self.number,self.number1,self.number2,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType4c(self,problem,answer,number,number1,number2,item):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s %d %s."%(item[3],number1,item[4])
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + self.WordsToFiguresTable(number2)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d %s."%(number2,item[5])
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "%d %s."%(number,item[2])
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
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
        self.NumberInWords2 = self.FiguresToWordsStatement(self.number2)

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
        
        self.item1 = random.choice(['figures','numerals'])
                      
        self.problem = "%s %s %s and %s %s. How many more %s? Give your answer in %s."%(self.item[0],self.NumberInWords1,self.item[1],
                                                                                        self.NumberInWords2,self.item[2],self.item[3],self.item1)
        
        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4d(self.problem,self.answer,self.number,self.number1,self.number2,self.item[1],self.item[2],self.item[4])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4d",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType4d(self,problem,answer,number,number1,number2,item1,item2,item4):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s %d %s."%(item4,number1,item1)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + self.WordsToFiguresTable(number2)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s %d %s."%(item4,number2,item2)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "%s %d more %s than %s."%(item4,number,item1,item2)
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
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
        
        self.item1 = random.choice(['figures','numerals'])
                      
        self.problem = "Multiply %s by %d. Express your answer in %s."%(self.NumberInWords1,self.number2,self.item1)
        
        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5a(self.problem,self.answer,self.number,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType5a(self,problem,answer,number,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5b(self):       
        '''e.g.:
            The cost of a <computer> is $750. What is the cost of 4 such <computers>? Write your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(1011,1400)
        self.number2 = randint(4,7)
        
        self.number = self.number1 * self.number2
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
                      
        self.items = [['computer','computers'],['sofa set','sofa sets'],['diamond ring','diamond rings'],['bed','beds'],['TV set','TV sets'],
                      ['dining table set','dining table sets'],['camera','cameras'],['book shelf','book shelves'],['home entertainment system','home entertainment systems']
                      ,['laptop','laptops']]
        
        self.item = random.choice(self.items)
        
        self.item1 = random.choice(['figures','numerals'])
        
        self.problem = "The cost of a %s is %s dollars. What is the cost of %d such %s? Write your answer in %s."%(self.item[0],self.NumberInWords1,
                                                                                                                   self.number2,self.item[1],self.item1)
        
        self.answer = self.number
        self.dollar_unit = "$"

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5b(self.problem,self.answer,self.number,self.number1,self.number2,self.item,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'dollar_unit':self.dollar_unit}

    def ExplainType5b(self,problem,answer,number,number1,number2,item,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%d"%(dollar_unit,answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The cost of a %s is $%d."%(item[0],number1)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "$%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; $%d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "The cost of %d %s is $%d."%(number2,item[1],number)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5c(self):       
        '''e.g.:
            <Person.Unclename> gives away 500 <marbles> to each of his 4 <pupils / sons / nephews / children>. How many <marbles> does he give away altogether? Give your answer in words.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(1000,1400)
        self.number2 = randint(4,7)
        
        self.number = self.number1 * self.number2
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)

        self.name = random.choice(PersonName.UncleName)
                              
        self.items = ['marbles','stamps','stickers','flags','rubberbands','buttons','keyrings','darts','animal cards','cards']
              
        self.item = random.choice(self.items)
        
        self.item1 = random.choice(['pupil','nephew'])
        
        self.item2 = random.choice(['figures','numerals'])
        
        self.unit = self.item
        
        self.problem = "%s gives away %s %s to each of his %d %ss. How many %s does he give away altogether? Give your answer in %s."%(self.name,self.NumberInWords1,self.item,
                                                                                                                                         self.number2,self.item1,self.item,self.item2)
        
        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5c(self.problem,self.answer,self.number,self.number1,self.number2,self.item,self.item1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":self.unit}

    def ExplainType5c(self,problem,answer,number,number1,number2,item,item1):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "He gives away %d %s to each %s."%(number1,item,item1)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "He gives away %d %s altogether."%(number,item)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6a(self):       
        '''e.g.:
            What do you get when you divide five thousand by 4? Express your answer in <numerals / figures>.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number = randint(1011,1400)
        self.number2 = randint(4,7)
        
        self.number1 = self.number * self.number2
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
        
        self.item1 = random.choice(['figures','numerals'])
        
        self.problem = "What do you get when you divide %s by %d? Express your answer in %s."%(self.NumberInWords1,self.number2,self.item1)
        
        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6a(self.problem,self.answer,self.number,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType6a(self,problem,answer,number,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
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
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
        
        self.items = ['marbles','stamps','stickers','flags','rubberbands','buttons','keyrings','darts','animal cards','cards']
        
        self.item = random.choice(self.items)
        
        self.item1 = random.choice(['friend','brother','cousin'])
        
        self.item2 = random.choice(['divided','shared'])
        
        self.item3 = random.choice(['figures','numerals'])
        
        self.problem = "%d %ss %s %s %s equally among themselves. How many %s did each %s get? Express your answer in %s."%(self.number2,self.item1,self.item2,self.NumberInWords1,
                                                                                                                              self.item,self.item,self.item1,self.item3)
        self.unit = self.item
        
        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6b(self.problem,self.answer,self.number,self.number1,self.number2,self.item1,self.item2,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":self.unit}

    def ExplainType6b(self,problem,answer,number,number1,number2,item1,item2,item):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The %ss %s %d %s equally among themselves."%(item1,item2,number1,item)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "Each %s got %d %s."%(item1,number,item)
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
        
        self.NumberInWords1 = self.FiguresToWordsStatement(self.number1)
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['computers','computer'],['sofa sets','sofa set'],['diamond rings','diamond ring'],['beds','bed'],['TV sets','TV set']
                      ,['dining table sets','dining table set'],['cameras','camera'],['book shelves','book shelf'],['home entertainment systems','home entertainment system'],
                      ['laptops','laptop']]
        
        self.item = random.choice(self.items)
        
        self.item1 = random.choice(['figures','numerals'])
        
        self.problem = "%s paid %s dollars for %d identical %s. What was the cost of each %s? Give your answer in %s."%(self.name,self.NumberInWords1,self.number2,self.item[0],
                                                                                                                    self.item[1],self.item1)
                                                                                                                    
        self.dollar_unit = "$"                                                                                                                    
        self.answer = self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6c(self.problem,self.answer,self.number,self.number1,self.number2,self.item,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"dollar_unit":"$"}

    def ExplainType6c(self,problem,answer,number,number1,number2,item,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%d"%(dollar_unit,answer)

        self.solution_text = self.WordsToFiguresTable(number1)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The %d %s cost $%d altogether."%(number2,item[0],number1)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>"
        self.solution_text = self.solution_text + "$%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; $%d<br>"%(number1,number2,number)
        self.solution_text = self.solution_text + "Each %s cost $%d."%(item[1],number)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        try:
            return int(answer)==int(InputAnswer)
        except ValueError:
            return False                          

    def WordsToFiguresTable(self,number):
        colorOnes = 'purple'
        colorTens = 'dodgerblue'
        colorHundreds = 'hotpink'
        colorThousands = 'darkorange'
        
        thousands,remHundreds  = divmod(number,1000)
        hundreds,remTens = divmod(remHundreds,100)
        tens,ones = divmod(remTens,10)
        
        figureToWordsThousands = ['-','one thousand','two thousand','three thousand','four thousand','five thousand','six thousand','seven thousand','eight thousand','nine thousand']
        figureToWordsHundreds = ['-','one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
        figureToWordsOnes = ['-','one','two','three','four','five','six','seven','eight','nine']
        figureToWordsTens = ['-','one','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
        figureToWords1Tens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
        
        figuresToWordsTable = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        figuresToWordsTable = figuresToWordsTable + "<tr><td style='background-color:%s;height:35px;width:150px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Thousands</font></td><td style='background-color:%s;height:35px;width:150px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Hundreds</font></td><td style='background-color:%s;height:35px;width:100px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Tens</font></td><td style='background-color:%s;height:35px;width:100px;white-space:nowrap;border:white solid 1px;'><font style='font-size:1.1em;'>Ones</font></td></tr>"%(colorThousands,colorHundreds,colorTens,colorOnes)
        figuresToWordsTable = figuresToWordsTable + "<tr><td style='height:60px;border:white solid 1px;white-space:nowrap;'>%s</td><td style='height:60px;border:white solid 1px;white-space:nowrap;'>%s</td>"%(figureToWordsThousands[thousands],figureToWordsHundreds[hundreds])
        if tens==1:
            figuresToWordsTable = figuresToWordsTable + "<td colspan=2 style='height:60px;border:white solid 1px;'>%s</td></tr>"%(figureToWords1Tens[ones])
        else:
            figuresToWordsTable = figuresToWordsTable + "<td style='height:60px;border:white solid 1px;'>%s</td><td style='height:60px;border:white solid 1px;'>%s</td></tr>"%(figureToWordsTens[tens],figureToWordsOnes[ones])

        figuresToWordsTable = figuresToWordsTable + "<tr><td style='padding:0'><img src='/images/explanation/P3_model_arrow_thousands.png' /></td><td style='padding:0'><img src='/images/explanation/P3_model_arrow_hundreds.png' /></td>"
        if tens==1:
            figuresToWordsTable = figuresToWordsTable + "<td colspan=2 style='padding:0'><img src='/images/explanation/P3_model_arrow_1tens.png' /></td></tr>"
        else:
            figuresToWordsTable = figuresToWordsTable + "<td style='padding:0'><img src='/images/explanation/P3_model_arrow_tens.png' /></td><td style='padding:0'><img src='/images/explanation/P3_model_arrow_ones.png' /></td></tr>"
        
        figuresToWordsTable = figuresToWordsTable + "<tr>"
        figuresToWordsTable = figuresToWordsTable + "<td style='height:35px;white-space:nowrap;'>%d</td>"%(thousands*1000)
        figuresToWordsTable = figuresToWordsTable + "<td style='height:35px;white-space:nowrap;'>%d</td>"%(hundreds*100)
        if tens==1:
            figuresToWordsTable = figuresToWordsTable + "<td colspan=2 style='height:35px;white-space:nowrap;'>%d</td>"%(tens*10+ones)
        else:
            figuresToWordsTable = figuresToWordsTable + "<td style='height:35px;white-space:nowrap;'>%d</td>"%(tens*10)
            figuresToWordsTable = figuresToWordsTable + "<td style='height:35px;white-space:nowrap;'>%d</td>"%(ones)
        figuresToWordsTable = figuresToWordsTable + "</tr>"
        figuresToWordsTable = figuresToWordsTable + "</table><br>"
        
        figuresToWordsTable = figuresToWordsTable + "<font class='ExplanationFont'>"
        if tens==1:
            figuresToWordsTable = figuresToWordsTable + "=&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d<br>=&nbsp; %d"%(thousands*1000,hundreds*100,tens*10+ones,number)
        else:
            figuresToWordsTable = figuresToWordsTable + "=&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d<br>=&nbsp; %d"%(thousands*1000,hundreds*100,tens*10,ones,number)
        figuresToWordsTable = figuresToWordsTable + "</font>"
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