'''
Created on Apr 21, 2013
Module: P3MOAddition
Generates the Addition problems on Money for Primary 3

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
from decimal import Decimal

class P3MOAddition:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3",],
                            4:["ProblemType4",],
                            5:["ProblemType5",],
                            6:["ProblemType6",],
                            7:["ProblemType7",],
                            8:["ProblemType8",],
                            9:["ProblemType9",],
                            10:["ProblemType10a","ProblemType10b",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],
                                    5:[self.GenerateProblemType5(),],
                                    6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],
                                    8:[self.GenerateProblemType8(),],
                                    9:[self.GenerateProblemType9(),],
                                    10:[self.GenerateProblemType10a(),self.GenerateProblemType10b(),],
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
        #return self.GenerateProblemTypeMCQ2()
        
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
                            "ProblemType10a":self.GenerateProblemType10a(),
                            "ProblemType10b":self.GenerateProblemType10b(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        Add the following amounts.
        $5.25 + $18.60 = ________'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.decimal1digit1 = randint(0,8)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(0,9-self.decimal1digit1)
        self.decimal2digit2 = 0
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(10,80)
        self.number2 = randint(10,97-self.number1)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "Add the following amounts.<br><br>$%s + $%s = _____"%(self.amount1,self.amount2)
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.amount1,self.amount2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,decimal1,decimal2,number1,number2,amount1,amount2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        decimal1Q,decimal1R = divmod(int(decimal1),10)
        decimal2Q,decimal2R = divmod(int(decimal2),10)
        number1Q,number1R = divmod(number1,10)
        number2Q,number2R = divmod(number2,10)

        carryOverToTenths,sumHundredths = divmod(decimal1R+decimal2R,10)
        carryOverToOnes,sumTenths = divmod(decimal1Q+decimal2Q+carryOverToTenths,10)
        carryOverToTens,sumOnes = divmod(number1R+number2R+carryOverToOnes,10)
        sumTens = number1Q+number2Q+carryOverToTens
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; ?<br><br>"%(amount1,amount2)
        
        self.solution_text = self.solution_text + "First, we add the cents.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)                
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + "Next, we add the dollars.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        else:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(sumTens,sumOnes,sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + "So, $%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        Add the following amounts.
        $5.25 + $18.60 = ________'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.decimal1digit1 = randint(3,8)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(10-self.decimal1digit1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(10,80)
        self.number2 = randint(10,97-self.number1)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)
        
        self.problem = "Add the following amounts.<br><br>$%s + $%s = _____"%(self.amount1,self.amount2)
            
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.amount1,self.amount2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,decimal1,decimal2,number1,number2,amount1,amount2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        decimal1Q,decimal1R = divmod(int(decimal1),10)
        decimal2Q,decimal2R = divmod(int(decimal2),10)
        number1Q,number1R = divmod(number1,10)
        number2Q,number2R = divmod(number2,10)

        carryOverToTenths,sumHundredths = divmod(decimal1R+decimal2R,10)
        carryOverToOnes,sumTenths = divmod(decimal1Q+decimal2Q+carryOverToTenths,10)
        carryOverToTens,sumOnes = divmod(number1R+number2R+carryOverToOnes,10)
        sumTens = number1Q+number2Q+carryOverToTens
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; ?<br><br>"%(amount1,amount2)
        
        self.solution_text = self.solution_text + "First, we add the cents.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)                
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + "Next, we add the dollars.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        else:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(sumTens,sumOnes,sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "So, $%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        [Person.Girlname] <has> $8.30< in her savings at first>.
        <Then she saves another> $5.60<>.
        <How much money does she have>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['has',' in her savings at first','Then she saves another','','How much money does she have','She has',''],
                      ['received',' for doing chores around the house','She received another',' from grandma','How much money did she receive altogether','She received',' altogether'],
                      ['spent',' on food','She spent',' on transport','How much money did she spend altogether','She spent',' altogether'],
                      ['has','','Her sister has','','How much money do they have altogether','They have',' altogether'],
                      ['had',' at first','Then she received',' as pocket money','How much money does she have','She has',''],
                      ['saved',' last week','She saved',' this week','How much money did she save in the two weeks','She saved',' in the two weeks'],
                      ['earned','','Her brother earned','','How much money did they earn altogether','They earned',' altogether'],
                      ['saved','','Her cousin saved','','How much money did the two children save altogether','They saved',' altogether'],
                      ['bought a toy for','','She bought another toy for','','How much money did she spend on the two toys','She spent',' on the two toys'],
                      ['sold some buns and received','','She also sold some ice tea and received','','How much money did she receive altogether','She received',' altogether']]
        
        self.item = random.choice(self.items)

        self.decimal1digit1 = randint(3,8)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(10-self.decimal1digit1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(10,80)
        self.number2 = randint(10,97-self.number1)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)
        
        self.problem = "%s %s $%s%s.<br><br>"%(self.name,self.item[0],self.amount1,self.item[1])
        self.problem = self.problem + "%s $%s%s.<br><br>"%(self.item[2],self.amount2,self.item[3])
        self.problem = self.problem + "%s?"%(self.item[4])
            
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.item[5],self.item[6],self.amount1,self.amount2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,decimal1,decimal2,number1,number2,item5,item6,amount1,amount2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        decimal1Q,decimal1R = divmod(int(decimal1),10)
        decimal2Q,decimal2R = divmod(int(decimal2),10)
        number1Q,number1R = divmod(number1,10)
        number2Q,number2R = divmod(number2,10)

        carryOverToTenths,sumHundredths = divmod(decimal1R+decimal2R,10)
        carryOverToOnes,sumTenths = divmod(decimal1Q+decimal2Q+carryOverToTenths,10)
        carryOverToTens,sumOnes = divmod(number1R+number2R+carryOverToOnes,10)
        sumTens = number1Q+number2Q+carryOverToTens
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; ?<br><br>"%(amount1,amount2)

        self.solution_text = self.solution_text + "First, we add the cents.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)                
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + "Next, we add the dollars.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        else:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(sumTens,sumOnes,sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "So, $%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s"%(amount1,amount2,answer)
        
        self.solution_text = self.solution_text + "<br><br>%s $%s%s.</font>"%(item5,answer,item6)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        A <carton of milk> costs $3.15.
        A <box of chocolates> costs $5.85.
        What is the total cost of the <carton of milk> and the <box of chocolates>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['carton of milk','box of chocolates'],['packet of juice','box of cereals'],['jar of mixed fruit jam','bag of nuts'],['jar of peanut butter','block of cheese'],['tube of toothpaste','bottle of shampoo'],['bag of potatoes','bag of frozen food'],['tray of eggs','tub of ice cream'],['block of butter','container of yogurt'],['bottle of hand wash','packet of detergent'],['can of mixed fruit','tin of milk powder'],['rockmelon','punnet of strawberries'],['papaya','punnet of cherries'],['bag of mushrooms','box of grapes'],['bar of chocolate','can of cooking oil'],['loaf of fruitcake','bag of basmati rice']]
        
        self.item = random.choice(self.items)

        self.decimal1digit1 = randint(3,8)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(10-self.decimal1digit1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(3,5)
        self.number2 = randint(5,8)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)
        
        self.flag = randint(1,2)
        
        if self.flag == 1:
            self.problem = "A %s costs $%s.<br><br>"%(self.item[0],self.amount1)
            self.problem = self.problem + "A %s costs $%s.<br><br>"%(self.item[1],self.amount2)
            self.problem = self.problem + "What is the total cost of the %s and the %s?"%(self.item[0],self.item[1])
        else:
            self.problem = "%s bought a %s for $%s.<br><br>"%(self.name,self.item[0],self.amount1)
            self.problem = self.problem + "He also bought a %s for $%s.<br><br>"%(self.item[1],self.amount2)
            self.problem = self.problem + "How much did %s spend altogether?"%(self.name)
            
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.flag,self.amount1,self.amount2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,decimal1,decimal2,number1,number2,flag,amount1,amount2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        decimal1Q,decimal1R = divmod(int(decimal1),10)
        decimal2Q,decimal2R = divmod(int(decimal2),10)

        carryOverToTenths,sumHundredths = divmod(decimal1R+decimal2R,10)
        carryOverToOnes,sumTenths = divmod(decimal1Q+decimal2Q+carryOverToTenths,10)
        carryOverToTens,sumOnes = divmod(number1+number2+carryOverToOnes,10)
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; ?<br><br>"%(amount1,amount2)

        self.solution_text = self.solution_text + "First, we add the cents.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)                
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + "Next, we add the dollars.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        if carryOverToTens==1:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s &nbsp;&nbsp;&nbsp; %s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(carryOverToTens,sumOnes,sumTenths,sumHundredths)
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(sumOnes,sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "So, $%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s"%(amount1,amount2,answer)
        
        if flag == 1:
            self.solution_text = self.solution_text + "<br><br>The total cost of the two items is $%s."%(answer)
        else:
            self.solution_text = self.solution_text + "<br><br>He spent $%s altogether.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        [Person.Name] bought a <T-shirt> and a <bandana>.
        The <T-shirt> cost $25.40 and the <bandana> cost $6.75.
        How much did the two items cost altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.PersonName)
        
        self.items = [['T-shirt','bandana'],['bouquet','vase'],['wooden easel','set of oil paints'],['lamp','candle holder'],['bedsheet set','towel'],['book','pen'],['headset','pack of batteries'],['picture frame','paperweight'],['mirror','soap dish'],['sandwich maker','bowl'],['toy truck','bubble kit'],['soccer ball','cap'],['teddy bear','pen holder'],['kettle','serving tray'],['swimsuit','pair of armbands']]
        
        self.item = random.choice(self.items)

        self.decimal1digit1 = randint(3,8)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(10-self.decimal1digit1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(20,40)
        self.number2 = randint(5,15)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s bought a %s and a %s.<br><br>"%(self.name,self.item[0],self.item[1])
        self.problem = self.problem + "The %s cost $%s and the %s cost $%s.<br><br>"%(self.item[0],self.amount1,self.item[1],self.amount2)
        self.problem = self.problem + "How much did the two items cost altogether?"
            
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.amount1,self.amount2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,decimal1,decimal2,number1,number2,amount1,amount2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        decimal1Q,decimal1R = divmod(int(decimal1),10)
        decimal2Q,decimal2R = divmod(int(decimal2),10)
        number1Q,number1R = divmod(number1,10)
        number2Q,number2R = divmod(number2,10)

        carryOverToTenths,sumHundredths = divmod(decimal1R+decimal2R,10)
        carryOverToOnes,sumTenths = divmod(decimal1Q+decimal2Q+carryOverToTenths,10)
        carryOverToTens,sumOnes = divmod(number1R+number2R+carryOverToOnes,10)
        sumTens = number1Q+number2Q+carryOverToTens
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; ?<br><br>"%(amount1,amount2)

        self.solution_text = self.solution_text + "First, we add the cents.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)                
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        if number2>=10:
            self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        else:
            self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>&nbsp;</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + "Next, we add the dollars.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        else:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        if number2>=10:
            self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        else:
            self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>&nbsp;</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(sumTens,sumOnes,sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "So, $%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s"%(amount1,amount2,answer)
        
        self.solution_text = self.solution_text + "<br><br>The two items cost $%s altogether.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        [Person.Unclename1] and [Person.Unclename2] <went to the market to sell their wares>.
        [Person.Unclename1] <sold his pies for> $48.90.
        [Person.Unclename2] <sold his puffs for> $36.90.
        Find the total amount of money they <received>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.UncleName,2)
        
        self.items = [['went to the market to sell their wares','sold his pies for','sold his spring rolls for','received','received'],
                      ['own kite shops','sold some kites and received','sold some spools and received','received','received'],
                      ['went to a sale','bought a microphone for','bought a speaker for','spent on the two items','spent'],
                      ['went shopping','bought a wallet for','bought a bag for','spent on the two items','spent'],
                      ['went to a restaurant for dinner','paid a bill of','paid a bill of','paid at the restaurant','paid'],
                      ['each donated a sum of money to Angels Charity','donated','donated','donated','donated'],
                      ['drove to a petrol station','purchased petrol for','purchased petrol for','paid the cashier for petrol','paid'],
                      ['went to a yard sale','bought a chair for','bought a table for','spent at the yard sale','spent'],
                      ['went to buy toys for their children','bought a board game for','bought a remote car for','spent on the two items','spent'],
                      ['went to a supermarket','purchased his groceries for','purchased his groceries for','spent on groceries','spent']
                      ]        
        self.item = random.choice(self.items)

        self.decimal1digit1 = randint(3,8)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(10-self.decimal1digit1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(20,60)
        self.number2 = randint(20,97-self.number1)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s and %s %s.<br><br>"%(self.names[0],self.names[1],self.item[0])
        self.problem = self.problem + "%s %s $%s.<br><br>"%(self.names[0],self.item[1],self.amount1)
        self.problem = self.problem + "%s %s $%s.<br><br>"%(self.names[1],self.item[2],self.amount2)
        self.problem = self.problem + "Find the total amount of money they %s."%(self.item[3])
            
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.item[4],self.amount1,self.amount2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,decimal1,decimal2,number1,number2,item4,amount1,amount2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        decimal1Q,decimal1R = divmod(int(decimal1),10)
        decimal2Q,decimal2R = divmod(int(decimal2),10)
        number1Q,number1R = divmod(number1,10)
        number2Q,number2R = divmod(number2,10)

        carryOverToTenths,sumHundredths = divmod(decimal1R+decimal2R,10)
        carryOverToOnes,sumTenths = divmod(decimal1Q+decimal2Q+carryOverToTenths,10)
        carryOverToTens,sumOnes = divmod(number1R+number2R+carryOverToOnes,10)
        sumTens = number1Q+number2Q+carryOverToTens
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; ?<br><br>"%(amount1,amount2)

        self.solution_text = self.solution_text + "First, we add the cents.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)                
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + "Next, we add the dollars.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        else:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(sumTens,sumOnes,sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "So, $%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s"%(amount1,amount2,answer)
        
        self.solution_text = self.solution_text + "<br><br>They %s $%s altogether.</font>"%(item4,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        [Person.Unclename] <went to a museum>.
        He <bought a child ticket> for $8.45 and <an adult ticket> for $16.90.
        How much did he pay <the cashier>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['went to a museum','bought a child ticket','an adult ticket','the cashier','to the cashier'],
                      ['took his daughter to an indoor playground','purchased an adult ticket','a child ticket','the cashier','to the cashier'],
                      ["went to a kid's water park with his son","bought an entry ticket for himself","an entry ticket for his son","for the entry tickets","for the entry tickets"],
                      ["went to a restaurant","ordered a kid's meal for his daughter","a regular meal for himself","for the meals",'for the meals'],
                      ['took a train to the city with his father','bought a senior citizen ticket for his father','a regular ticket for himself','for the two tickets','for the two tickets'],
                      ['bought two tickets for a tram ride at the zoo','bought a child ticket for his nephew','a regular ticket for himself','for the two tickets','for the two tickets'],
                      ['went to an amusement park with his niece','purchased an entry pass for his niece','a regular pass for himself','for the two passes','for the two passes'],
                      ['went to the cinema','purchased a ticket for a regular show','a ticket for a 3D show','altogether','altogether'],
                      ['went to an arts festival','purchased a ticket for a music show','a ticket for a dance show','altogether','altogether'],
                      ['took his son to a carnival','bought a coupon booklet for food','a coupon booklet for rides','the cashier','to the cashier']]
        self.item = random.choice(self.items)

        self.decimal1digit1 = randint(3,8)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(10-self.decimal1digit1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(5,10)
        self.number2 = randint(15,25)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s %s.<br><br>"%(self.name,self.item[0])
        self.problem = self.problem + "He %s for $%s and %s for $%s.<br><br>"%(self.item[1],self.amount1,self.item[2],self.amount2)
        self.problem = self.problem + "How much did he pay %s?"%(self.item[3])
            
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.item[4],self.amount1,self.amount2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,decimal1,decimal2,number1,number2,item4,amount1,amount2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        tempDecimal = decimal1
        decimal1 = decimal2
        decimal2 = tempDecimal
        
        tempNumber = number1
        number1 = number2
        number2 = tempNumber
        
        decimal1Q,decimal1R = divmod(int(decimal1),10)
        decimal2Q,decimal2R = divmod(int(decimal2),10)
        number1Q,number1R = divmod(number1,10)
        number2Q,number2R = divmod(number2,10)

        carryOverToTenths,sumHundredths = divmod(decimal1R+decimal2R,10)
        carryOverToOnes,sumTenths = divmod(decimal1Q+decimal2Q+carryOverToTenths,10)
        carryOverToTens,sumOnes = divmod(number1R+number2R+carryOverToOnes,10)
        sumTens = number1Q+number2Q+carryOverToTens
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; ?<br><br>"%(amount2,amount1)

        self.solution_text = self.solution_text + "First, we add the cents.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)                
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        if number2>=10:
            self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        else:
            self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>&nbsp;</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + "Next, we add the dollars.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        else:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        if number2>=10:
            self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        else:
            self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>&nbsp;</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(sumTens,sumOnes,sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "So, $%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s"%(amount2,amount1,answer)
        
        self.solution_text = self.solution_text + "<br><br>He paid $%s %s.</font>"%(answer,item4)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        [Person.Girlname] bought <an eraser and a correction tape>.
        The <eraser> cost $0.55.
        The <correction tape> cost $1.20 more than the <eraser>.
        Find the cost of the <correction tape>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['an eraser and a correction tape','eraser','correction tape'],
                      ['a packet of salt and a bag of sugar','packet of salt','bag of sugar'],
                      ['an apple and an ice cream bar','apple','ice cream bar'],
                      ['a glue stick and a sharpener','glue stick','sharpener'],
                      ['a ribbon bow and a greeting card','ribbon bow','greeting card'],
                      ['a hair clip and a wristband','hair clip','wristband'],
                      ['a ruler and a sticker sheet','ruler','sticker sheet'],
                      ['a roll of tape and a stapler','roll of tape','stapler'],
                      ['a sticky notepad and a notebook','sticky notepad','notebook'],
                      ['a highlighter and a pen holder','highlighter','pen holder']]
        self.item = random.choice(self.items)

        self.decimal1digit1 = randint(3,8)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(10-self.decimal1digit1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(0,1)
        self.number2 = randint(0,2)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s bought %s.<br><br>"%(self.name,self.item[0])
        self.problem = self.problem + "The %s cost $%s.<br><br>"%(self.item[1],self.amount1)
        self.problem = self.problem + "The %s cost $%s more than the %s.<br><br>"%(self.item[2],self.amount2,self.item[1])
        self.problem = self.problem +"Find the cost of the %s."%(self.item[2])
            
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.item[2],self.amount1,self.amount2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,decimal1,decimal2,number1,number2,item2,amount1,amount2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)        
        
        decimal1Q,decimal1R = divmod(int(decimal1),10)
        decimal2Q,decimal2R = divmod(int(decimal2),10)

        carryOverToTenths,sumHundredths = divmod(decimal1R+decimal2R,10)
        carryOverToOnes,sumTenths = divmod(decimal1Q+decimal2Q+carryOverToTenths,10)
        sumOnes = number1+number2+carryOverToOnes
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; ?<br><br>"%(amount1,amount2)

        self.solution_text = self.solution_text + "First, we add the cents.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)                
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + "Next, we add the dollars.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(sumOnes,sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "So, $%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s"%(amount1,amount2,answer)
        
        self.solution_text = self.solution_text + "<br><br>The cost of the %s was $%s.</font>"%(item2,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        [Person.Boyname1] and [Person.Boyname2] went to a <mall>.
        [Person.Boyname1] bought a <shirt> for $15.90.
        [Person.Boyname2] bought a different <shirt> and paid $10.40 more than [Person.Boyname1].
        What was the cost of the <shirt> that [Person.Boyname2] bought?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.BoyName,2)
        
        self.items = [['mall','shirt'],['toys shop','chess board set'],['shoes store','pair of shoes'],['sports shop','badminton racket'],['bookstore','book'],['department store','vase'],['shop','picture frame'],['mega mart','water cooler'],['furniture shop','wall clock'],['store','night light']]
        self.item = random.choice(self.items)

        self.decimal1digit1 = randint(3,8)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(10-self.decimal1digit1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(10,20)
        self.number2 = randint(5,20)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s and %s went to a %s.<br><br>"%(self.names[0],self.names[1],self.item[0])
        self.problem = self.problem + "%s bought a %s for $%s.<br><br>"%(self.names[0],self.item[1],self.amount1)
        self.problem = self.problem + "%s bought a different %s and paid $%s more than %s.<br><br>"%(self.names[1],self.item[1],self.amount2,self.names[0])
        self.problem = self.problem +"What was the cost of the %s that %s bought?"%(self.item[1],self.names[1])
            
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.item[1],self.amount1,self.amount2,self.names[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,decimal1,decimal2,number1,number2,item1,amount1,amount2,name,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        decimal1Q,decimal1R = divmod(int(decimal1),10)
        decimal2Q,decimal2R = divmod(int(decimal2),10)
        number1Q,number1R = divmod(number1,10)
        number2Q,number2R = divmod(number2,10)

        carryOverToTenths,sumHundredths = divmod(decimal1R+decimal2R,10)
        carryOverToOnes,sumTenths = divmod(decimal1Q+decimal2Q+carryOverToTenths,10)
        carryOverToTens,sumOnes = divmod(number1R+number2R+carryOverToOnes,10)
        sumTens = number1Q+number2Q+carryOverToTens
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; ?<br><br>"%(amount1,amount2)

        self.solution_text = self.solution_text + "First, we add the cents.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)                
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        if number2>=10:
            self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        else:
            self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>&nbsp;</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + "Next, we add the dollars.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        else:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        if number2>=10:
            self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2Q,number2R,decimal2Q,decimal2R)
        else:
            self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>&nbsp;</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number2R,decimal2Q,decimal2R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(sumTens,sumOnes,sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "So, $%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s"%(amount1,amount2,answer)
        
        self.solution_text = self.solution_text + "<br><br>The cost of %s's %s was $%s.</font>"%(name,item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10a(self):       
        '''e.g.:
        <Chairs are on sale at a furniture fair.>
        [Person.Auntyname] wants to buy two <identical / similar> <chairs> selling at $35.40 each.
        How much money will she need?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [['Chairs are on sale at a furniture fair.','chairs','chair'],
                      ['Carpets are on sale at a night market.','carpets','carpet'],
                      ['Bags are on promotion at a year-end sale.','bags','bag'],
                      ['Cooking pots are on promotion at a megamart.','cooking pots','cooking pot'],
                      ['Dresses are on clearance at a fashion store.','dresses','dress'],
                      ['Blankets are on clearance at a department store.','blankets','blanket'],
                      ['Toasters are on discount at a kitchen store.','toasters','toaster'],
                      ['Cardigans are on discount at a clothing store.','cardigans','cardigan'],
                      ['Laundry baskets are on promotion at a furniture store.','laundry baskets','laundry basket'],
                      ['Coffee machines are on clearance at a megastore.','coffee machines','coffee machine']]
        self.item = random.choice(self.items)

        self.decimal1digit1 = randint(0,4)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        
        self.number1 = randint(20,45)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
                
        self.answer = self.amount1 * 2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s<br><br>"%(self.item[0])
        self.problem = self.problem + "%s wants to buy two similar %s selling at $%s each.<br><br>"%(self.name,self.item[1],self.amount1)
        self.problem = self.problem + "How much money will she need?"
            
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10a(self.problem,self.answer,self.decimal1,self.number1,self.amount1,self.item[1],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10a(self,problem,answer,decimal1,number1,amount1,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        decimal1Q,decimal1R = divmod(int(decimal1),10)
        number1Q,number1R = divmod(number1,10)

        carryOverToTenths,sumHundredths = divmod(decimal1R+decimal1R,10)
        carryOverToOnes,sumTenths = divmod(decimal1Q+decimal1Q+carryOverToTenths,10)
        carryOverToTens,sumOnes = divmod(number1R+number1R+carryOverToOnes,10)
        sumTens = number1Q+number1Q+carryOverToTens
        
        self.solution_text = "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>1 %s</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>$%s</td></tr>"%(item2,amount1)
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>2 %s</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>$%s &nbsp;+&nbsp; $%s</td></tr>"%(item1,amount1,amount1)
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td>?</td></tr></table>"
        self.solution_text = self.solution_text + "<br>"

        self.solution_text = self.solution_text +"<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "First, we add the cents.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)                
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + "Next, we add the dollars.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        else:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(sumTens,sumOnes,sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "So, $%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s"%(amount1,amount1,answer)
        
        self.solution_text = self.solution_text + "<br><br>She will need $%s.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10b(self):       
        '''e.g.:
        [Person.Auntyname] goes to a <furniture fair>.
        She buys two <identical / similar> <chairs> at $35.40 each.
        How much money does she pay?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [['furniture fair','chairs','chair'],
                      ['night market','carpets','carpet'],
                      ['year-end sale','bags','bag'],
                      ['megamart','cooking pots','cooking pot'],
                      ['clearance sale at a fashion store','dresses','dress'],
                      ['clearance sale at a department store','blankets','blanket'],
                      ['kitchen store selling items on discount','toasters','toaster'],
                      ['clothing store selling items on discount','cardigans','cardigan'],
                      ['furniture store having a promotion','laundry baskets','laundry basket'],
                      ['clearance sale at a megastore','coffee machines','coffee machine']]
        self.item = random.choice(self.items)

        self.decimal1digit1 = randint(0,4)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        
        self.number1 = randint(20,45)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
                
        self.answer = self.amount1 * 2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s goes to a %s.<br><br>"%(self.name,self.item[0])
        self.problem = self.problem + "She buys two identical %s at $%s each.<br><br>"%(self.item[1],self.amount1)
        self.problem = self.problem + "How much money does she pay?"
            
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10b(self.problem,self.answer,self.decimal1,self.number1,self.amount1,self.item[1],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10b(self,problem,answer,decimal1,number1,amount1,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        decimal1Q,decimal1R = divmod(int(decimal1),10)
        number1Q,number1R = divmod(number1,10)

        carryOverToTenths,sumHundredths = divmod(decimal1R+decimal1R,10)
        carryOverToOnes,sumTenths = divmod(decimal1Q+decimal1Q+carryOverToTenths,10)
        carryOverToTens,sumOnes = divmod(number1R+number1R+carryOverToOnes,10)
        sumTens = number1Q+number1Q+carryOverToTens
        
        self.solution_text = "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>1 %s</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>$%s</td></tr>"%(item2,amount1)
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>2 %s</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>$%s &nbsp;+&nbsp; $%s</td></tr>"%(item1,amount1,amount1)
        self.solution_text = self.solution_text + "<tr><td style='padding:0px'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td>?</td></tr></table>"
        self.solution_text = self.solution_text + "<br>"

        self.solution_text = self.solution_text +"<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "First, we add the cents.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)                
        else:
            if carryOverToOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"
        
        self.solution_text = self.solution_text + "Next, we add the dollars.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable'>"
        if carryOverToTenths==1:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td><sup>1</sup>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        else:
            if carryOverToOnes==1:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td><sup>1</sup>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
            else:
                if carryOverToTens==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup>1</sup>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)

        self.solution_text = self.solution_text + "<tr><td>+</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(number1Q,number1R,decimal1Q,decimal1R)
        self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:left;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%s</td><td>%s</td><td>.</td><td>%d</td><td>%d </td></tr>"%(sumTens,sumOnes,sumTenths,sumHundredths)
        self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "So, $%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s"%(amount1,amount1,answer)
        
        self.solution_text = self.solution_text + "<br><br>She pays $%s.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore,CheckAnswerType):
        
        '''Removing correct answers from the wrongAnswers list'''
        wrongAnswers = filter(self.removeCorrectAnswer,wrongAnswers)
        
        self.answer1=''
        self.answer2=''
        self.answer3=''
        self.answer4=''
                             
        '''Randomly selecting 3 wrong answers and adding the correct answer as well'''
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
                'grade':3,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}
        
    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        Add the following amounts.
        $5.25 + $18.60 = ________'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1"
        self.CheckAnswerType = 1

        self.decimal1digit1 = randint(0,8)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(0,9-self.decimal1digit1)
        self.decimal2digit2 = 0
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(10,80)
        self.number2 = randint(10,97-self.number1)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "Add the following amounts.<br><br>$%s + $%s = _____"%(self.amount1,self.amount2)
                   
        self.unit = ""
        self.dollar_unit = "$"      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [Decimal(self.answer+Decimal(.05)).quantize(TWOPLACES),
                             Decimal(self.answer-Decimal(.05)).quantize(TWOPLACES),
                             Decimal(self.answer+Decimal(1.05)).quantize(TWOPLACES),
                             Decimal(self.answer+Decimal(.50)).quantize(TWOPLACES),]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.amount1,self.amount2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        Add the following amounts.
        $5.25 + $18.60 = ________'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ2"
        self.CheckAnswerType = 1

        self.decimal1digit1 = randint(3,8)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(10-self.decimal1digit1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(10,80)
        self.number2 = randint(10,97-self.number1)
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)
        
        self.problem = "Add the following amounts.<br><br>$%s + $%s = _____"%(self.amount1,self.amount2)
            
        self.unit = ""
        self.dollar_unit = "$"      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [Decimal(self.answer+Decimal(.05)).quantize(TWOPLACES),
                             Decimal(self.answer-Decimal(.05)).quantize(TWOPLACES),
                             Decimal(self.answer+Decimal(1.05)).quantize(TWOPLACES),
                             Decimal(self.answer+Decimal(.50)).quantize(TWOPLACES),]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.amount1,self.amount2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False