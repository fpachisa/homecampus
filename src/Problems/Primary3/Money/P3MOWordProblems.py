'''
Created on Apr 23, 2013
Module: P3MOWordProblems
Generates the Word problems on Money for Primary 3

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

class P3MOWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemType4",],5:["ProblemType5",],
                            6:["ProblemType6",],7:["ProblemType7",],8:["ProblemType8",],9:["ProblemType9",],10:["ProblemType10",],
                            11:["ProblemType11",],12:["ProblemType12",],13:["ProblemType13",],14:["ProblemType14",],15:["ProblemType15",],
                            16:["ProblemType16",],17:["ProblemType17",],18:["ProblemType18",],19:["ProblemType19",],20:["ProblemType20",],
                            21:["ProblemType21",],22:["ProblemType22",],23:["ProblemType23",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],9:[self.GenerateProblemType9(),],
                                    10:[self.GenerateProblemType10(),],
                                    11:[self.GenerateProblemType11(),],12:[self.GenerateProblemType12(),],13:[self.GenerateProblemType13(),],
                                    14:[self.GenerateProblemType14(),],15:[self.GenerateProblemType15(),],16:[self.GenerateProblemType16(),],
                                    17:[self.GenerateProblemType17(),],18:[self.GenerateProblemType18(),],19:[self.GenerateProblemType19(),],
                                    20:[self.GenerateProblemType20(),],
                                    21:[self.GenerateProblemType21(),],22:[self.GenerateProblemType22(),],23:[self.GenerateProblemType23(),],
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
        #return self.GenerateProblemType20()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),"ProblemType2":self.GenerateProblemType2(),"ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),"ProblemType5":self.GenerateProblemType5(),"ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),"ProblemType8":self.GenerateProblemType8(),"ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10":self.GenerateProblemType10(),
                            "ProblemType11":self.GenerateProblemType11(),"ProblemType12":self.GenerateProblemType12(),"ProblemType13":self.GenerateProblemType13(),
                            "ProblemType14":self.GenerateProblemType14(),"ProblemType15":self.GenerateProblemType15(),"ProblemType16":self.GenerateProblemType16(),
                            "ProblemType17":self.GenerateProblemType17(),"ProblemType18":self.GenerateProblemType18(),"ProblemType19":self.GenerateProblemType19(),
                            "ProblemType20":self.GenerateProblemType20(),
                            "ProblemType21":self.GenerateProblemType21(),"ProblemType22":self.GenerateProblemType22(),"ProblemType23":self.GenerateProblemType23(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        [Person.Girlname] <saved> $12< in her bank>.
        She bought <a glass of lemonade for> $2.50 and <a pastry for> $7.90.
        How much money had she left?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['saved',' in her bank','a glass of lemonade for','a pastry for',randint(16,20),randint(1,4),randint(4,9),'the lemonade and the pastry'],
                      ['had',' with her','a set of bangles for','a hairclip for',randint(20,30),randint(3,10),randint(2,5),'the bangles and the hairclip'],
                      ['had',' in her wallet','a toy for','a book for',randint(35,40),randint(5,15),randint(5,15),'the toy and the book'],
                      ['went to a fruit shop with','','a bag of apples for','a box of grapes for',randint(15,20),randint(2,6),randint(3,7),'the apples and the grapes'],
                      ['went to a movie theatre with','','a movie ticket for','a cup of soda for',randint(20,25),randint(7,12),randint(2,5),'the movie ticket and the soda'],
                      ['counted',' in her money bank','a cycle for','a helmet for',randint(93,100),randint(50,70),randint(10,20),'the cycle and the helmet'],
                      ['saved',' in her piggy bank','a cup of yogurt for','a sandwich for',randint(15,20),randint(1,4),randint(3,7),'the yogurt and the sandwich'],
                      ['had','','a storybook for','a bag of potato chips for',randint(20,25),randint(7,12),randint(1,4),'the storybook and the potato chips'],
                      ['received',' from her parents','a hairband for','a pair of flip-flops for',randint(30,40),randint(3,10),randint(10,15),'the hairband and the flip-flops'],
                      ['earned',' doing chores','a present for her friend for','a pencil case for',randint(20,25),randint(5,10),randint(3,7),'the present and the pencil case']]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(5,95,5)
        self.cents2 = random.randrange(5,95,5)
        
        self.amount1 = self.item[4]
        self.number1 = self.item[5]
        self.number2 = self.item[6]
        self.amount2 = Decimal(self.number1*100+self.cents1)/100
        self.amount3 = Decimal(self.number2*100+self.cents2)/100
                
        self.answer = self.amount1 - (self.amount2+self.amount3)
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.amount3 = Decimal(self.amount3).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s %s $%s%s.<br><br>"%(self.name,self.item[0],self.amount1,self.item[1])
        self.problem = self.problem + "She bought %s $%s and %s $%s.<br><br>"%(self.item[2],self.amount2,self.item[3],self.amount3)
        self.problem = self.problem + "How much money had she left?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.amount1,self.amount2,self.amount3,self.name,self.item[7],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,amount3,amount1,amount2,name,item7,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        # No direct 1-1 mapping between the variable names in GenerateProblem and Explain
        # Check the values of the 3 amounts
        if Decimal(amount1)==Decimal(amount2):
            firstCell = 'medium'
            secondCell = 'medium'
            if Decimal(amount1)==Decimal(answer):
                thirdCell = 'medium'
                upBrace = 'medium3'
            elif Decimal(amount1)>Decimal(answer):
                thirdCell = 'small'
                upBrace = 'medium2small1'
            else:
                thirdCell = 'large'
                upBrace = 'large1medium2'
        elif Decimal(amount1)>Decimal(amount2):
            if Decimal(answer)<Decimal(amount2):
                firstCell = 'large'
                secondCell = 'medium'
                thirdCell = 'small'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)<Decimal(amount1) and Decimal(answer)>Decimal(amount2):
                firstCell = 'large'
                secondCell = 'small'
                thirdCell = 'medium'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)>Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'small'
                thirdCell = 'large'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)==Decimal(amount2):
                firstCell = 'large'
                secondCell = 'medium'
                thirdCell = 'medium'
                upBrace = 'large1medium2'
            elif Decimal(answer)==Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'small'
                thirdCell = 'medium'
                upBrace = 'medium2small1'
        elif Decimal(amount1)<Decimal(amount2):
            if Decimal(answer)>Decimal(amount2):
                firstCell = 'small'
                secondCell = 'medium'
                thirdCell = 'large'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)<Decimal(amount2) and Decimal(answer)>Decimal(amount1):
                firstCell = 'small'
                secondCell = 'large'
                thirdCell = 'medium'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)<Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'large'
                thirdCell = 'small'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)==Decimal(amount2):
                firstCell = 'small'
                secondCell = 'medium'
                thirdCell = 'medium'
                upBrace = 'medium2small1'
            elif Decimal(answer)==Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'large'
                thirdCell = 'medium'
                upBrace = 'large1medium2'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        self.color3 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td colspan=3>$%s</td></tr>"%(amount3)
        self.solution_text = self.solution_text + "<tr><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(upBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(self.color1,self.color2,self.color3)
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstCell,secondCell,thirdCell)
        self.solution_text = self.solution_text + "<tr><td>$%s</td><td>$%s</td><td>?</td></tr>"%(amount1,amount2)
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)+Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s spent $%s on %s.</font>"%(name,str(Decimal(amount1)+Decimal(amount2)),item7)
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s.00 &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount3,str(Decimal(amount1)+Decimal(amount2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>She had $%s left.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        A <pair of soccer shoes> costs $64.85.
        A <soccer ball> costs $36.40 less than the <pair of soccer shoes>.
        [Person.Boyname] buys two such <soccer balls>.
        How much does he pay the cashier?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['pair of soccer shoes','soccer ball','soccer balls',randint(50,70),randint(30,40),'soccer shoes','soccer ball'],
                      ['water gun','dart board','dart boards',randint(15,30),randint(5,10),'water gun','dart board'],
                      ['can of paint','paintbrush','paintbrushes',randint(30,40),randint(15,20),'paint','paintbrush'],
                      ['toy phone','floor puzzle','floor puzzles',randint(20,30),randint(5,15),'toy phone','puzzle'],
                      ['bicycle','skateboard','skateboards',randint(70,90),randint(30,45),'bicycle','skateboard'],
                      ['box of chocolates','box of cookies','boxes of cookies',randint(15,25),randint(6,11),'chocolates','cookies'],
                      ['book of stickers','box of pencils','boxes of pencils',randint(5,7),randint(2,3),'stickers','pencils'],
                      ['box of pies','box of muffins','boxes of muffins',randint(5,10),randint(2,3),'pies','muffins'],
                      ['cup of ice cream','bottle of soda','bottles of soda',randint(3,5),randint(1,2),'ice cream','soda'],
                      ['pack of art paper','pack of popsicle sticks','packs of popsicle sticks',randint(4,6),randint(1,2),'art paper','popsicle sticks']]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(0,95,5)
        self.cents2 = random.randrange(5,95,5)
        
        self.number1 = self.item[3]
        self.number2 = self.item[4]
        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100
                
        self.answer = 2 * (self.amount1 - self.amount2)
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "A %s costs $%s.<br><br>"%(self.item[0],self.amount1)
        self.problem = self.problem + "A %s costs $%s less than the %s.<br><br>"%(self.item[1],self.amount2,self.item[0])
        self.problem = self.problem + "%s buys two such %s.<br><br>"%(self.name,self.item[2])
        self.problem = self.problem + "How much does he pay the cashier?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.amount1,self.amount2,self.item[1],self.item[2],self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,amount1,amount2,item1,item2,item5,item6,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if Decimal(amount2)<Decimal(answer)/2:
            secondCell = 'medium'
            thirdCell = 'small'
            upBrace = 'medium1small1'
        elif Decimal(amount2)>Decimal(answer)/2:
            secondCell = 'small'
            thirdCell = 'medium'
            upBrace = 'medium1small1'
        else:
            secondCell = 'medium'
            thirdCell = 'medium'
            upBrace = 'medium2'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%s</td></tr>"%(amount1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(upBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'></td></tr>"%(item5,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td>&nbsp;</td></tr>"%(item6,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(secondCell,thirdCell)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td><td>$%s</td></tr>"%(amount2)
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)-Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>The cost of 1 %s is $%s.</font>"%(item1,str(Decimal(amount1)-Decimal(amount2)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(str(Decimal(amount1)-Decimal(amount2)),str(Decimal(amount1)-Decimal(amount2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>The cost of 2 %s is $%s.</font>"%(item2,answer)
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>He pays $%s to the cashier.</font>"%(answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        [Person.Girlname1] and [Person.Girlname2] <have> $20 <altogether>.
        <They buy two bags of potato chips for> $2.80< each>.
        How much money do they have left?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.GirlName,2)
        
        self.items = [['have','altogether','They buy two bags of potato chips for',' each',randint(12,20),randint(2,4)],
                      ['save','altogether','They buy two pendants for',' each',randint(70,90),randint(10,30)],
                      ['earn','altogether','They spend',' each',randint(70,90),randint(5,30)],
                      ['save','altogether','They give away',' each',randint(70,90),randint(10,30)],
                      ['go to a stationery shop with','altogether','Each of them spends',' on some stationery',randint(25,40),randint(5,11)],
                      ['go to a store with','altogether','They buy two purses for',' each',randint(40,60),randint(12,18)],
                      ['have','altogether','They buy two loaves of bread for',' each',randint(15,20),randint(3,6)],
                      ['receive','from their parents altogether','Each of them buys a comic book for','',randint(20,30),randint(3,7)],
                      ['count','in their coin-bank altogether','They buy two keychains for',' each',randint(20,30),randint(3,7)],
                      ['save','altogether','They buy two hairbands for',' each',randint(30,40),randint(7,13)]]
        
        self.item = random.choice(self.items)
        
        self.cents2 = random.randrange(5,95,5)
        
        self.number1 = self.item[4]
        self.number2 = self.item[5]
        self.amount1 = self.number1
        self.amount2 = Decimal(self.number2*100+self.cents2)/100
                
        self.answer = self.amount1 - 2*self.amount2
        
        TWOPLACES = Decimal(10) ** -2

        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s and %s %s $%s %s.<br><br>"%(self.names[0],self.names[1],self.item[0],self.amount1,self.item[1])
        self.problem = self.problem + "%s $%s%s.<br><br>"%(self.item[2],self.amount2,self.item[3])
        self.problem = self.problem + "How much money do they have left?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.amount1,self.amount2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,amount1,amount2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if Decimal(answer) < Decimal(amount2):
            firstCell = 'medium'
            secondCell = 'medium'
            thirdCell = 'small'
            upBrace = 'medium2small1' 
        elif Decimal(answer) > Decimal(amount2):
            firstCell = 'small'
            secondCell = 'small'
            thirdCell = 'medium'
            upBrace = 'medium1small2'
        else:
            firstCell = 'medium'
            secondCell = 'medium'
            thirdCell = 'medium'
            upBrace = 'medium3'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td colspan=3>$%s</td></tr>"%(amount1)
        self.solution_text = self.solution_text + "<tr><td colspan =3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(upBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;height:25px;border:white solid 1px;'></td></tr>"%(self.color1,self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstCell,secondCell,thirdCell)
        self.solution_text = self.solution_text + "<tr><td>$%s</td><td>$%s</td><td>?</td></tr>"%(amount2,amount2)
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount2,amount2,str(Decimal(amount2)*2))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>They spend $%s altogether.</font>"%(str(Decimal(amount2)*2))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(str(Decimal(amount1)),str((Decimal(amount2)*2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>They have $%s left.</font>"%(answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        [Person.Boyname] had $21.60.
        He received another $30 from his father.
        He spent $12.40 on a <raincoat>.
        How much money had he left?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['raincoat',randint(10,30)],['pair of jeans',randint(25,45)],['can of coconut water',randint(1,3)],['bag of popcorn',randint(3,5)],['packet of sweets',randint(3,10)],['bag of marbles',randint(3,7)],['box of colour pens',randint(10,20)],['bag of seashells',randint(5,15)],['pizza',randint(10,20)],['toy',randint(10,30)]]
        
        self.item = random.choice(self.items)
        self.item1 = random.choice(['father','mother','grandfather','grandmother','uncle','brother','sister'])
        
        self.cents3 = random.randrange(5,95,5)
        self.cents2 = random.randrange(5,95,5)
        
        self.number3 = self.item[1]
        self.number1 = random.randrange(5,self.number3+5,5)
        self.number2 = randint(self.number3-3,self.number3+randint(3,20))
        
        self.amount1 = self.number1
        self.amount2 = Decimal(self.number2*100+self.cents2)/100
        self.amount3 = Decimal(self.number3*100+self.cents3)/100
                
        self.answer = self.amount1 + self.amount2 - self.amount3
        
        TWOPLACES = Decimal(10) ** -2

        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.amount3 = Decimal(self.amount3).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s had $%s.<br><br>"%(self.name,self.amount2)
        self.problem = self.problem + "He received another $%s from his %s.<br><br>"%(self.amount1,self.item1)
        self.problem = self.problem + "He spent $%s on a %s.<br><br>"%(self.amount3,self.item[0])
        self.problem = self.problem + "How much money had he left?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.amount2,self.amount1,self.amount3,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,amount1,amount2,amount3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if Decimal(answer) < Decimal(amount3):
            firstCell = 'large'
            secondCell = 'medium'
            upBrace = 'large1medium1'
        else:
            firstCell = 'medium'
            secondCell = 'large'
            upBrace = 'large1medium1'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td colspan=2>$%s + $%s</td></tr>"%(amount1,amount2)
        self.solution_text = self.solution_text + "<tr><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(upBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;height:25px;border:white solid 1px;'></td></tr>"%(self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstCell,secondCell)
        self.solution_text = self.solution_text + "<tr><td>$%s</td><td>?</td></tr>"%(amount3)
        self.solution_text = self.solution_text + "</table>"

        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)+Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>He had $%s altogether.</font>"%(str(Decimal(amount1)+Decimal(amount2)))

        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(str(Decimal(amount1)+Decimal(amount2)),str(Decimal(amount3)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>He had $%s left.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        [Person.Girlname] has $9.25 at first.
        Then she saves another $3.95.
        She wants to buy a <dollhouse> that costs $12.45.
        How much more must she save to buy the <dollhouse>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['dollhouse',randint(10,20)],['playgym',randint(30,50)],
                      ['teddy bear',randint(10,30)],['mug',randint(8,15)],
                      ['backpack',randint(8,15)],['hat',randint(12,20)],
                      ['novel',randint(5,15)],['tote bag',randint(10,25)],
                      ['shirt',randint(15,30)],['superhero costume',randint(50,90)]]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(5,95,5)
        self.cents2 = random.randrange(5,95,5)
        self.cents3 = random.randrange(5,95,5)
        
        self.number3 = self.item[1]
        self.number1 = int(float(randint(2,4))*self.number3/10)
        self.number2 = int(float(randint(2,4))*self.number3/10)
        
        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100
        self.amount3 = Decimal(self.number3*100+self.cents3)/100
                
        self.answer = self.amount3 - (self.amount1 + self.amount2)
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.amount3 = Decimal(self.amount3).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s has $%s at first.<br><br>"%(self.name,self.amount1)
        self.problem = self.problem + "Then she saves another $%s.<br><br>"%(self.amount2)
        self.problem = self.problem + "She wants to buy a %s that costs $%s.<br><br>"%(self.item[0],self.amount3)
        self.problem = self.problem + "How much more must she save to buy the %s?"%(self.item[0])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.amount1,self.amount2,self.amount3,self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,amount1,amount2,amount3,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        # Check the values of the 3 amounts
        if Decimal(amount1)==Decimal(amount2):
            firstCell = 'medium'
            secondCell = 'medium'
            if Decimal(amount1)==Decimal(answer):
                thirdCell = 'medium'
                upBrace = 'medium3'
            elif Decimal(amount1)>Decimal(answer):
                thirdCell = 'small'
                upBrace = 'medium2small1'
            else:
                thirdCell = 'large'
                upBrace = 'large1medium2'
        elif Decimal(amount1)>Decimal(amount2):
            if Decimal(answer)<Decimal(amount2):
                firstCell = 'large'
                secondCell = 'medium'
                thirdCell = 'small'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)<Decimal(amount1) and Decimal(answer)>Decimal(amount2):
                firstCell = 'large'
                secondCell = 'small'
                thirdCell = 'medium'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)>Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'small'
                thirdCell = 'large'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)==Decimal(amount2):
                firstCell = 'large'
                secondCell = 'medium'
                thirdCell = 'medium'
                upBrace = 'large1medium2'
            elif Decimal(answer)==Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'small'
                thirdCell = 'medium'
                upBrace = 'medium2small1'
        elif Decimal(amount1)<Decimal(amount2):
            if Decimal(answer)>Decimal(amount2): #done
                firstCell = 'small'
                secondCell = 'medium'
                thirdCell = 'large'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)<Decimal(amount2) and Decimal(answer)>Decimal(amount1): #done
                firstCell = 'small'
                secondCell = 'large'
                thirdCell = 'medium'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)<Decimal(amount1): #done
                firstCell = 'medium'
                secondCell = 'large'
                thirdCell = 'small'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)==Decimal(amount2):
                firstCell = 'small'
                secondCell = 'medium'
                thirdCell = 'medium'
                upBrace = 'medium2small1'
            elif Decimal(answer)==Decimal(amount1): #done
                firstCell = 'medium'
                secondCell = 'large'
                thirdCell = 'medium'
                upBrace = 'large1medium2'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        self.color3 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td colspan=3>$%s</td></tr>"%(amount3)
        self.solution_text = self.solution_text + "<tr><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(upBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(self.color1,self.color2,self.color3)
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstCell,secondCell,thirdCell)
        self.solution_text = self.solution_text + "<tr><td>$%s</td><td>$%s</td><td>?</td></tr>"%(amount1,amount2)
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)+Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>She has $%s altogether.</font>"%(str(Decimal(amount1)+Decimal(amount2)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount3,str(Decimal(amount1)+Decimal(amount2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>She must save $%s more to buy the %s.</font>"%(answer,item)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        [Person.Auntyname] bought <a tray of 30 eggs> for $6.35.
        She gave the cashier 4 <two-dollar> notes.
        How much change did she receive?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [['a tray of 30 eggs','two-dollar',randint(4,8),2],
                      ['a bottle of ketchup','two-dollar',randint(2,6),2],
                      ['a box of cherries','two-dollar',randint(6,10),2],
                      ['a movie DVD','five-dollar',randint(10,20),5],
                      ['a magazine','five-dollar',randint(10,20),5],
                      ['a cake','five-dollar',randint(10,20),5],
                      ['a tin of milk powder','ten-dollar',randint(20,40),10],
                      ['some groceries','ten-dollar',randint(40,60),10],
                      ['a set of coursebooks for her son','ten-dollar',randint(60,80),10],
                      ['a painting','ten-dollar',randint(70,90),10]
                      ]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(5,95,5)

        self.number1 = self.item[2]
        self.number2 = self.number1/self.item[3] + 1
        
        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = self.number2 * self.item[3]
                
        self.answer = self.amount2 - self.amount1
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s bought %s for $%s.<br><br>"%(self.name,self.item[0],self.amount1)
        self.problem = self.problem + "She gave the cashier %d %s notes.<br><br>"%(self.number2,self.item[1])
        self.problem = self.problem + "How much change did she receive?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.amount1,self.number2,self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,amount1,number2,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td colspan=2>%d &times; $%d</td></tr>"%(number2,item3)
        self.solution_text = self.solution_text + "<tr><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large1small1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;height:25px;border:white solid 1px;'></td></tr>"%(self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_large.png' /></td><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>$%s</td><td>?</td></tr>"%(amount1)
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>%d &nbsp;&times;&nbsp; $%d &nbsp;=&nbsp; $%s</font>"%(number2,item3,number2*item3)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>She gave $%d to the cashier.</font>"%(number2*item3)

        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%d.00 &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(number2*item3,amount1,answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>She received a change of $%s.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        [Person.Auntyname1] and [Person.Auntyname2] <went to a supermarket>.
        [Person.Auntyname1] <spent> $42.50< on groceries>.
        [Person.Auntyname2] <spent> $6.75 less than [Person.Auntyname1].
        How much did they <spend> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.AuntyName,2)
        
        self.items = [['went to a supermarket','spent',' on groceries','spent','spend',randint(30,50),randint(5,15)],
                      ['went shopping at a mall','spent',' on a dress','spent','spend',randint(30,50),randint(5,15)],
                      ['went to a restaurant','spent',' on meals for her family','spent','spend',randint(25,35),randint(5,15)],
                      ['bought books for their children','spent','','spent','spend',randint(45,60),randint(25,35)],
                      ['saved some money','saved','','saved','save',randint(20,50),randint(5,15)],
                      ['sold their wares at a park','earned','','earned','earn',randint(35,50),randint(5,15)],
                      ['each received a sum of money','received','','received','receive',randint(30,60),randint(5,20)],
                      ['paid their utility bills','paid','','paid','pay',randint(25,45),randint(5,15)],
                      ['bought toys at a toys shop','paid',' to the cashier','paid','pay',randint(30,60),randint(5,20)],
                      ['went to a bakery','spent',' on pastries and puffs','spent','spend',randint(20,30),randint(5,10)]]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(0,95,5)
        self.cents2 = random.randrange(5,95,5)

        self.number1 = self.item[5]
        self.number2 = self.item[6]
        
        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100
                
        self.answer = self.amount1 + self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s and %s %s.<br><br>"%(self.names[0],self.names[1],self.item[0])
        self.problem = self.problem + "%s %s $%s%s.<br><br>"%(self.names[0],self.item[1],self.amount1,self.item[2])
        self.problem = self.problem + "%s %s $%s less than %s.<br><br>"%(self.names[1],self.item[3],self.amount2,self.names[0])
        self.problem = self.problem + "How much did they %s altogether?"%(self.item[4])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.names,self.amount1,self.amount2,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,names,amount1,amount2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if Decimal(amount2)<Decimal(Decimal(amount1)-Decimal(amount2)):
            secondCell = 100
            thirdCell = 'small'
        else:
            secondCell = 50
            thirdCell = 'medium'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%s</td></tr>"%(amount1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium1small1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'></td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(names[0],self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'></td><td>&nbsp;</td></tr>"%(names[1],self.color2,secondCell)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(thirdCell)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>$%s</td></tr>"%(amount2)
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)-Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s %s $%s.</font>"%(names[1],item1,str(Decimal(amount1)-Decimal(amount2)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,str(Decimal(amount1)-Decimal(amount2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>They %s $%s altogether.</font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        [Person.Girlname] bought <a printer and a ream of paper>.
        The <ream of paper> cost $12.45.
        The <printer> cost $65.75 more.
        How much did she spend altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['a printer and a ream of paper','ream of paper','printer',randint(5,10),randint(60,78),'paper','printer'],
                      ['a toy computer and a hula hoop','hula hoop','toy computer',randint(5,15),randint(35,68),'hula hoop','toy computer'],
                      ['a pair of shoes and a pair of socks','socks','shoes',randint(3,10),randint(15,25),'socks','shoes'],
                      ['a skirt and a belt','belt','skirt',randint(10,15),randint(10,15),'belt','skirt'],
                      ['a jar of honey and a loaf of bread','loaf of bread','jar of honey',randint(1,4),randint(3,10),'bread','honey'],
                      ['a bottle of hair spray and a hairclip','hair clip','bottle of hair spray',randint(2,6),randint(3,6),'hair clip','hair spray'],
                      ['a burger and a packet of drink','packet of drink','burger',randint(1,2),randint(2,5),'drink','burger'],
                      ['a stapler and a roll of tape','roll of tape','stapler',randint(1,2),randint(2,4),'tape','stapler'],
                      ['a bar of chocolate and a packet of candies','packet of candies','bar of chocolate',randint(2,4),randint(1,3),'candies','chocolate'],
                      ['a sheet of stickers and a notebook','notebook','sheet of stickers',randint(1,3),randint(1,3),'notebook','stickers']]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(5,95,5)
        self.cents2 = random.randrange(0,95,5)

        self.number1 = self.item[3]
        self.number2 = self.item[4]
        
        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100
                
        self.answer = self.amount1 + self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s bought %s.<br><br>"%(self.name,self.item[0])
        self.problem = self.problem + "The %s cost $%s.<br><br>"%(self.item[1],self.amount1)
        self.problem = self.problem + "The %s cost $%s more.<br><br>"%(self.item[2],self.amount2)
        self.problem = self.problem + "How much did she spend altogether?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.amount1,self.amount2,self.item[2],self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,amount1,amount2,item2,item5,item6,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if Decimal(amount1)>Decimal(amount2):
            firstCell = 'medium'
            secondCell = 'small'
            bottomCellWidth = 150
        elif Decimal(amount1)<Decimal(amount2):
            firstCell = 'small'
            secondCell = 'medium'
            bottomCellWidth = 150
        else:
            firstCell = 'medium'
            secondCell = 'medium'
            bottomCellWidth = 200

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%s</td><td>$%s</td></tr>"%(amount1,amount2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstCell,secondCell)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px'></td><td>&nbsp;</td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(item5,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'></td><td>&nbsp;</td></tr>"%(item6,self.color2,bottomCellWidth)
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)+Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>The %s cost $%s.</font>"%(item2,str(Decimal(amount1)+Decimal(amount2)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,str(Decimal(amount1)+Decimal(amount2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>She spent $%s altogether.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        [Person.Boyname] bought <an icecream bar and a packet of lollipops>.
        He gave the cashier $10 and received $2.35 change.
        The <icecream bar> cost $3.45.
        How much did the <packet of lollipops> cost?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['an icecream bar and a packet of lollipops','icecream bar','packet of lollipops',randint(1,4),randint(2,5),'icecream','lollipops'],
                      ['a green pen and a clear file','green pen','clear file',randint(1,4),randint(1,3),'pen','file'],
                      ['a bunch of bananas and a watermelon','bunch of bananas','watermelon',randint(1,3),randint(3,5),'bananas','watermelon'],
                      ['a magazine and a comic book','magazine','comic book',randint(3,8),randint(2,6),'magazine','comic book'],
                      ['a toy truck and a puzzle game','toy truck','puzzle game',randint(15,25),randint(10,30),'toy truck','puzzle'],
                      ['a set of pegs and a set of hangers','set of pegs','set of hangers',randint(3,7),randint(6,12),'pegs','hangers'],
                      ['a water bottle and a lunch box','water bottle','lunch box',randint(5,12),randint(7,12),'water bottle','lunch box'],
                      ['a watch and a belt','watch','belt',randint(15,50),randint(10,25),'watch','belt'],
                      ['a shirt and a sweater','shirt','sweater',randint(15,25),randint(40,70),'shirt','sweater'],
                      ['a shower curtain and a floor mat','shower curtain','floor mat',randint(10,25),randint(15,30),'shower curtain','floor mat']]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(5,95,5)
        self.cents2 = random.randrange(5,95,5)

        self.number1 = self.item[3]
        self.number2 = self.item[4]
        
        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100
                
        self.total = self.amount1 + self.amount2
        
        self.gave = (int(self.total/10)+1)*10
        self.change = Decimal(self.gave) - (self.amount1+self.amount2)
        
        self.answer = self.amount2
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.change = Decimal(self.change).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s bought %s.<br><br>"%(self.name,self.item[0])
        self.problem = self.problem + "He gave the cashier $%d and received $%s change.<br><br>"%(self.gave,self.change)
        self.problem = self.problem + "The %s cost $%s.<br><br>"%(self.item[1],self.amount1)
        self.problem = self.problem + "How much did the %s cost?"%(self.item[2])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.gave,self.change,self.amount1,self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,gave,change,cost1,item5,item6,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        if Decimal(answer)<cost1:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%s</td></tr>"%(cost1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'></td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;text-align:left;vertical-align:middle;width:100px'>&nbsp;$%s &minus; $%s</td></tr>"%(item5,self.color1,gave,change)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:100px'></td><td>&nbsp;</td></tr>"%(item6,self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_medium.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
            self.solution_text = self.solution_text + "</table>"
        else:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%s</td></tr>"%(cost1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:100px'></td><td style='width:50px'>&nbsp;</td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;text-align:left;vertical-align:middle;width:100px'>&nbsp;$%s &minus; $%s</td></tr>"%(item5,self.color1,gave,change)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px'></td></tr>"%(item6,self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
            self.solution_text = self.solution_text + "</table>"
            

        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%d.00 &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(gave,change,str(Decimal(gave)-Decimal(change)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>The %s and the %s cost $%s altogether.</font>"%(item5,item6,str(Decimal(gave)-Decimal(change)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(str(Decimal(gave)-Decimal(change)),cost1,answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>The %s cost $%s.</font>"%(item6,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:
        <Every week >[Person.Girlname] <saves some of her pocket money>.
        She <saved> $14.25< last week>.
        She <saved> $15.80 more< this week>.
        How much did she <save in the two weeks>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['Every week ','saves some of her pocket money','saved',' last week','saved',' this week','save in the two weeks',randint(10,20),randint(10,20),'last week','this week','saved','weeks'],
                      ['','is collecting money for a charity','collected',' yesterday','collected',' today','collect in the two days',randint(20,30),randint(10,20),'yesterday','today','collected','days'],
                      ['','does household chores for which she gets money','got',' last week','got',' this week','get in the two weeks',randint(10,20),randint(10,20),'last week','this week','got','weeks'],
                      ['Every morning ','delivers newspaper for which she gets paid','got',' last week','got',' this week','get in the two weeks',randint(30,40),randint(10,20),'last week','this week','got','weeks'],
                      ['','sold her used books over the weekend','sold some of her books on Saturday and received','','sold the rest of her books on Sunday and received','','receive in the two days',randint(30,40),randint(10,15),'Saturday','Sunday','received','days'],
                      ['','bought lunch at the school canteen on Monday and Friday','spent',' at the canteen on Monday','spent',' at the canteen on Friday','spend at the canteen in the two days',randint(2,4),randint(1,2),'Monday','Friday','spent','days'],
                      ['Every month ','visits the bookshop to buy either stationery or books','bought a set of crayons for',' last month','bought a novel for',' this month','spend at the bookshop in the two months',randint(5,10),randint(3,7),'last month','this month','spent','months'],
                      ['Every day ','buys a drink from the vending machine','bought a drink for',' yesterday','bought a drink for',' today','spend at the vending machine in the two days',randint(1,2),randint(0,1),'yesterday','today','spent','days'],
                      ['','likes to collect stamps','spent',' on stamps in 2011','spent',' on stamps in 2012','spend on stamps in the two years',randint(30,40),randint(10,20),'in 2011','in 2012','spent','years'],
                      ['','went to her school carnival over the weekend','spent',' at the carnival on Saturday','spent',' at the carnival on Sunday','spend at the carnival in the two days',randint(5,10),randint(5,10),'Saturday','Sunday','spent','days']]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(5,95,5)
        self.cents2 = random.randrange(5,95,5)

        self.number1 = self.item[7]
        self.number2 = self.item[8]
        
        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100
        
        self.answer = self.amount1 + self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s%s %s.<br><br>"%(self.item[0],self.name,self.item[1])
        self.problem = self.problem + "She %s $%s%s.<br><br>"%(self.item[2],self.amount1,self.item[3])
        self.problem = self.problem + "She %s $%s more%s.<br><br>"%(self.item[4],self.amount2,self.item[5])
        self.problem = self.problem + "How much did she %s?"%(self.item[6])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.amount1,self.amount2,self.item[9],self.item[10],self.item[11],self.item[12],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,amount1,amount2,item9,item10,item11,item12,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if Decimal(amount1)>Decimal(amount2):
            firstCell = 'medium'
            secondCell = 'small'
            thirdCellWidth = 150
        elif Decimal(amount1)==Decimal(amount2):
            firstCell = 'medium'
            secondCell = 'medium'
            thirdCellWidth = 150
        else:
            firstCell = 'small'
            secondCell = 'medium'
            thirdCellWidth = 200

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%s</td><td>$%s</td></tr>"%(amount1,amount2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstCell,secondCell)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px'></td><td>&nbsp;</td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(item9,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;width:%s'></td></tr>"%(item10,self.color2,thirdCellWidth)
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)+Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>She %s $%s %s.</font>"%(item11,str(Decimal(amount1)+Decimal(amount2)),item10)
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,str(Decimal(amount1)+Decimal(amount2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>She %s $%s in the two %s.</font>"%(item11,answer,item12)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:
        [Person.Girlname1] <has> $52.45< in her bag>.
        She <has> $9.65 more than [Person.Name1].
        [Person.Name1] <has> $24.80 more /less than [Person.Name2].
        How much money does [Person.Name2] <have>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.GirlName,2)+[random.choice(PersonName.BoyName)]
        
        self.items = [['has',' in her bag','have'],['saves',' in her bank','save'],['earns',' for helping her neighbours','earn'],['spends',' on books','spend'],['collects',' during a charity drive','collect'],['shares',' with her brother','share'],['donates',' to a pet charity','donate'],['receives',' from her father','receive'],['gets',' for housework','get'],['counts',' in her coin-bank','count']]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(5,95,5)
        self.cents2 = random.randrange(5,95,5)
        self.cents3 = random.randrange(5,95,5)

        self.MoreLessFlag = randint(1,2)
        
        if self.MoreLessFlag == 1: # more and more
            self.number3 = randint(15,20) # is the answer 
            self.amount3 = Decimal(self.number3*100+self.cents3)/100
            self.number2 = randint(5,15)
            self.amount2 = self.amount3 + Decimal(self.number2*100+self.cents2)/100
            self.number1 = randint(5,10)
            self.amount1 = self.amount2 + Decimal(self.number1*100+self.cents1)/100
            self.DisplayAmount1 = Decimal(self.number1*100+self.cents1)/100
            self.DisplayAmount2 = Decimal(self.number2*100+self.cents2)/100
        else:
            self.number2 = randint(15,20) # is the answer 
            self.amount2 = Decimal(self.number2*100+self.cents2)/100
            self.number1 = randint(5,15)
            self.amount1 = self.amount2 + Decimal(self.number1*100+self.cents1)/100
            self.number3 = randint(5,10)
            self.amount3 = self.amount1 + Decimal(self.number3*100+self.cents3)/100
            self.DisplayAmount1 = self.amount1 - self.amount2
            self.DisplayAmount2 = self.amount3 - self.amount2
        
        self.answer = self.amount3
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.DisplayAmount1 = Decimal(self.DisplayAmount1).quantize(TWOPLACES)
        self.DisplayAmount2 = Decimal(self.DisplayAmount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s %s $%s%s.<br><br>"%(self.names[0],self.item[0],self.amount1,self.item[1])
        self.problem = self.problem + "She %s $%s more than %s.<br><br>"%(self.item[0],self.DisplayAmount1,self.names[1])
        if self.MoreLessFlag == 1:
            self.problem = self.problem + "%s %s $%s more than %s.<br><br>"%(self.names[1],self.item[0],self.DisplayAmount2,self.names[2])
        else:
            self.problem = self.problem + "%s %s $%s less than %s.<br><br>"%(self.names[1],self.item[0],self.DisplayAmount2,self.names[2])
        self.problem = self.problem + "How much money does %s %s?"%(self.names[2],self.item[2])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.MoreLessFlag,self.amount1,self.DisplayAmount1,self.DisplayAmount2,self.names,self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,flag,amount1,amount2,amount3,names,item0,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if Decimal(amount2) > Decimal(amount3):
            downBrace1 = 'medium'
            downBrace2 = 'small'
            upBrace = 'medium2small1'
        elif Decimal(amount2) == Decimal(amount3):
            downBrace1 ='medium'
            downBrace2 ='medium'
            upBrace = 'medium3'
        else:
            downBrace1 ='small'
            downBrace2 ='medium'
            upBrace = 'medium2small1'
        
        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        self.color3 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        if flag==1:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3>$%s</td></tr>"%(amount1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(upBrace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-left:white solid 1px;border-right:white dotted 2px;'></td><td style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-right:white solid 1px;'></td></tr>"%(names[0],self.color1,self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-left:white solid 1px;border-right:white dotted 2px;'></td><td style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-right:white solid 2px;'></td><td style='vertical-align:bottom'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(names[1],self.color3,self.color3,downBrace1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td style='padding-top:0px; padding-bottom:10px'>$%s</td></tr>"%(amount2)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td></tr>"%(names[2],self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_medium.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(downBrace2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td><td>$%s</td></tr>"%(amount3)
        else:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%s</td></tr>"%(amount1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium1small1.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-left:white solid 1px;border-right:white dotted 2px;width:100px'></td><td style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-right:white solid 1px;width:50px'></td></tr>"%(names[0],self.color1,self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='vertical-align:bottom'><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"%(names[1],self.color3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td style='padding-top:0px; padding-bottom:10px'>$%s</td></tr>"%(amount2)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-left:white solid 1px;border-right:white dotted 2px;'></td><td colspan=2 style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-right:white solid 1px;width:40px'></td></tr>"%(names[2],self.color2,self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td colspan=2>$%s</td></tr>"%(amount3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=4><img src='/images/explanation/P3_model_down_brace_large1medium1.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=4>?</td></tr>"
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)-Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s %s $%s.</font>"%(names[1],item0,str(Decimal(amount1)-Decimal(amount2)))
        
        if flag==1:
            self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(str(Decimal(amount1)-Decimal(amount2)),amount3,answer)
        else:
            self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(str(Decimal(amount1)-Decimal(amount2)),amount3,answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s %s $%s.</font>"%(names[2],item0,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType12(self):       
        '''e.g.:
        [Person.Name1] and [Person.Name2] each had the same amount of money at first.
        [Person.Name1] <bought a toy for> $34.80 <and had> $12.70 left.
        [Person.Name2] <bought a book for> $12.65<>.
        How much money did [Person.Name2] have left?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.PersonName,2)
        
        self.items = [['bought a toy for','and had','bought a book for','',randint(20,40),randint(5,20)],
                      ['bought a ride-on car for','and had','bought some stationery for','',randint(35,60),randint(15,35)],
                      ['bought a cake for','and had','bought a present for a friend for','',randint(15,40),randint(10,15)],
                      ['bought a booklet of stick-on tattoos for','and had','bought a sheet of stickers for','',randint(5,20),randint(2,5)],
                      ['bought a board game for','and had','bought a jigsaw puzzle for','',randint(20,50),randint(10,20)],
                      ['spent','on clothes and had','spent',' on some art supplies',randint(20,30),randint(10,20)],
                      ['spent','on groceries and had','spent',' on a tub of ice cream',randint(25,30),randint(5,15)],
                      ['spent','on a wall poster and had','spent',' on a photo frame',randint(15,25),randint(5,15)],
                      ['spent','on a kite and had','spent',' on a fridge magnet',randint(5,15),randint(2,5)],
                      ['spent','on bag of balls and had','spent',' on a roll of tape',randint(4,10),randint(1,4)]]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(5,95,5)
        self.cents2 = random.randrange(5,95,5)
        self.cents3 = random.randrange(5,95,5)

        self.number1 = self.item[4]
        self.number2 = int(float(randint(2,5))/10 * self.number1)
        self.number3 = self.item[5]

        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100        
        self.amount3 = Decimal(self.number3*100+self.cents3)/100
        
        self.answer = self.amount1 + self.amount2 - self.amount3
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.amount3 = Decimal(self.amount3).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s and %s each had the same amount of money at first.<br><br>"%(self.names[0],self.names[1])
        self.problem = self.problem + "%s %s $%s %s $%s left.<br><br>"%(self.names[0],self.item[0],self.amount1,self.item[1],self.amount2)
        self.problem = self.problem + "%s %s $%s%s.<br><br>"%(self.names[1],self.item[2],self.amount3,self.item[3])
        self.problem = self.problem + "How much money did %s have left?"%(self.names[1])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.amount1,self.amount2,self.amount3,self.names,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType12(self,problem,answer,amount1,amount2,amount3,names,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if Decimal(amount1)==Decimal(amount2):
            firstCell = 'medium'
            firstCellColspan = 2
            secondCell = 'medium'
            secondCellColspan = 2
            if Decimal(amount2)==Decimal(amount3):
                thirdCell = 'medium'
                thirdCellColspan = 2
                fourthCell = 'medium'
                fourthCellColspan = 2
            elif Decimal(amount2)>Decimal(amount3):
                thirdCell = 'small'
                thirdCellColspan = 1
                fourthCell = 'large'
                fourthCellColspan = 3
            else:
                thirdCell = 'large'
                thirdCellColspan = 3
                fourthCell = 'small'
                fourthCellColspan = 1
        elif Decimal(amount2)>Decimal(amount1):
            if Decimal(amount3)<Decimal(amount1):
                firstCell = 'medium'
                firstCellColspan = 2
                secondCell = 'large'
                secondCellColspan = 3
                thirdCell = 'small'
                thirdCellColspan = 1
                fourthCell = 'large1small1'
                fourthCellColspan = 4
            elif Decimal(amount3)<Decimal(amount2) and Decimal(amount3)>Decimal(amount1):
                firstCell = 'small'
                firstCellColspan = 1
                secondCell = 'large'
                secondCellColspan = 3
                thirdCell = 'medium'
                thirdCellColspan = 2
                fourthCell = 'medium'
                fourthCellColspan = 2
            elif Decimal(amount3)>Decimal(amount2):
                firstCell = 'medium'
                firstCellColspan = 2
                secondCell = 'large'
                secondCellColspan = 3
                thirdCell = 'large1small1'
                thirdCellColspan = 4
                fourthCell = 'small'
                fourthCellColspan = 1
            elif Decimal(amount3)==Decimal(amount1):
                firstCell = 'medium'
                firstCellColspan = 2
                secondCell = 'large'
                secondCellColspan = 3
                thirdCell = 'medium'
                thirdCellColspan = 2
                fourthCell = 'large'
                fourthCellColspan = 3
            elif Decimal(amount3)==Decimal(amount2):
                firstCell = 'small'
                firstCellColspan = 1
                secondCell = 'medium'
                secondCellColspan = 2
                thirdCell = 'medium'
                thirdCellColspan = 2
                fourthCell = 'small'
                fourthCellColspan = 1
        elif Decimal(amount2)<Decimal(amount1):
            if Decimal(amount3)>Decimal(amount1):
                firstCell = 'large'
                firstCellColspan = 3
                secondCell = 'medium'
                secondCellColspan = 2
                thirdCell = 'large1small1'
                thirdCellColspan = 4
                fourthCell = 'small'
                fourthCellColspan = 1
            elif Decimal(amount3)<Decimal(amount1) and Decimal(amount3)>Decimal(amount2):
                firstCell = 'large1small1'
                firstCellColspan = 4
                secondCell = 'small'
                secondCellColspan = 1
                thirdCell = 'medium'
                thirdCellColspan = 2
                fourthCell = 'large'
                fourthCellColspan = 3
            elif Decimal(amount3)<Decimal(amount2):
                firstCell = 'large'
                firstCellColspan = 3
                secondCell = 'medium'
                secondCellColspan = 2
                thirdCell = 'small'
                thirdCellColspan = 1
                fourthCell = 'large1small1'
                fourthCellColspan = 4
            elif Decimal(amount3)==Decimal(amount1):
                firstCell = 'medium'
                firstCellColspan = 2
                secondCell = 'small'
                secondCellColspan = 1
                thirdCell = 'medium'
                thirdCellColspan = 2
                fourthCell = 'small'
                fourthCellColspan = 1
            elif Decimal(amount3)==Decimal(amount2):
                firstCell = 'medium'
                firstCellColspan = 2
                secondCell = 'small'
                secondCellColspan = 1
                thirdCell = 'small'
                thirdCellColspan = 1
                fourthCell = 'medium'
                fourthCellColspan = 2

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        self.color3 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>$%s</td><td colspan=%d>$%s</td></tr>"%(firstCellColspan,amount1,secondCellColspan,amount2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstCellColspan,firstCell,secondCellColspan,secondCell)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;'></td><td colspan=%d style='background-color:mistyrose;height:25px;border:white solid 1px;'></td></tr>"%(names[0],firstCellColspan,self.color1,secondCellColspan)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='width:50px'>&nbsp;</td><td style='width:50px'>&nbsp;</td><td style='width:50px'>&nbsp;</td><td style='width:50px'>&nbsp;</td><td style='width:50px'>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;'></td><td colspan=%d style='background-color:lavenderblush;height:25px;border:white solid 1px;'></td></tr>"%(names[1],thirdCellColspan,self.color2,fourthCellColspan)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(thirdCellColspan,thirdCell,fourthCellColspan,fourthCell)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-top:0px; padding-bottom:10px'>$%s</td><td colspan=%d style='padding-top:0px; padding-bottom:10px'>?</td></tr>"%(thirdCellColspan,amount3,fourthCellColspan)
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)+Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s and %s each had $%s at first.</font>"%(names[0],names[1],str(Decimal(amount1)+Decimal(amount2)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(str(Decimal(amount1)+Decimal(amount2)),amount3,answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s had $%s left.</font>"%(names[1],answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType13(self):       
        '''e.g.:
        [Person.Boyname] had $8.30.
        [Person.Girlname] had $1.20 more than him.
        [Person.Girlname] spent $5.60 on a <crayon set>.
        How much money had she left?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = [random.choice(PersonName.BoyName)]+[random.choice(PersonName.GirlName)]
        
        self.items = [['crayon set',randint(4,10)],['headband',randint(4,7)],
                      ['set of bangles',randint(4,10)],['pencil case',randint(7,12)],
                      ['bag',randint(7,12)],['top',randint(10,12)],['bottle of juice',randint(2,5)],
                      ['can of soda',randint(1,4)],['bag of potato chips',randint(1,4)],['chicken pie',randint(2,5)]]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(5,95,5)
        self.cents2 = random.randrange(5,95,5)
        self.cents3 = random.randrange(5,95,5)

        self.number1 = randint(12,19)
        self.number2 = randint(1,8)
        self.number3 = self.item[1]
        
        if self.number2 == self.number3:
            self.number2 = self.number2 + 1

        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100        
        self.amount3 = Decimal(self.number3*100+self.cents3)/100
        
        self.answer = self.amount1 + self.amount2 - self.amount3
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.amount3 = Decimal(self.amount3).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s had $%s.<br><br>"%(self.names[0],self.amount1)
        self.problem = self.problem + "%s had $%s more than him.<br><br>"%(self.names[1],self.amount2)
        self.problem = self.problem + "%s spent $%s on a %s.<br><br>"%(self.names[1],self.amount3,self.item[0])
        self.problem = self.problem + "How much money had she left?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.amount1,self.amount2,self.amount3,self.names,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType13(self,problem,answer,amount1,amount2,amount3,names,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        amount2Brace = 'medium'
        amount2Colspan = 2
        amount1Brace = 'large'
        amount1Colspan = 3
        if Decimal(answer) > Decimal(amount1):
            answerBrace = 'large1small1'
            answerColspan1 = 3
            answerColspan2 = 1
            answerColspan3 = 1
            answerColspan = 4
            amount3Brace = 'small'
            amount3Colspan = 1
        elif Decimal(answer) < Decimal(amount1):
            answerBrace = 'medium'
            answerColspan1 = 2
            answerColspan2 = 1
            answerColspan3 = 2
            answerColspan = 2
            amount3Brace = 'large'
            amount3Colspan = 3

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        self.color3 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>$%s</td><td style='width:50px'>&nbsp;</td><td style='width:50px'>&nbsp;</td></tr>"%(amount1Colspan,amount1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td>&nbsp;</td><td>&nbsp;</td></tr>"%(amount1Colspan,amount1Brace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;'></td><td colspan=%d style='padding-bottom:0px;vertical-align:bottom'>$%s</td></tr>"%(names[0],amount1Colspan,self.color1,amount2Colspan,amount2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='width:50px'>&nbsp;</td><td style='width:50px'>&nbsp;</td><td style='width:50px'>&nbsp;</td><td colspan=%d style='width:100px;padding-bottom:3px'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(amount2Colspan,amount2Brace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border-left:white solid 1px;border-top:white solid 1px;border-bottom:white solid 1px;border-right:white dotted 1px;'></td><td colspan=%d style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-right:white dotted 1px;'></td><td colspan=%d style='background-color:palevioletred;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-right:white solid 1px'></td></tr>"%(names[1],answerColspan1,self.color2,answerColspan2,self.color3,answerColspan3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(answerColspan,answerBrace,amount3Colspan,amount3Brace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-top:0px; padding-bottom:10px'>?</td><td colspan=%d style='padding-top:0px; padding-bottom:10px'>$%s</td></tr>"%(answerColspan,amount3Colspan,amount3)
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)+Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s had $%s at first.</font>"%(names[1],str(Decimal(amount1)+Decimal(amount2)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(str(Decimal(amount1)+Decimal(amount2)),amount3,answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s had $%s left.</font>"%(names[1],answer)
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType14(self):       
        '''e.g.:
        [Person.Girlname] has some money.
        Her brother has $87.20.
        If she buys a <dollhouse> for $32.70, she will have $34.90 less than her brother.
        How much does she have?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['dollhouse',randint(20,40)],['carrot cake',randint(20,40)],
                      ['jar of honey',randint(10,20)],['box of cookies',randint(5,10)],
                      ['bag of candies',randint(3,7)],['roll of ribbon',randint(2,5)],
                      ['ring binder',randint(3,10)],['set of coasters',randint(5,15)],
                      ['scrapbook',randint(5,15)],['bag of beads',randint(2,5)]]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(5,95,5)
        self.cents2 = random.randrange(5,95,5)
        self.cents3 = random.randrange(5,95,5)

        self.number1 = randint(50,98)
        self.number2 = self.item[1]
        self.number3 = randint(25,40) + self.number2

        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100        
        self.amount3 = Decimal(self.number3*100+self.cents3)/100
        self.amount4 = self.amount1 - (self.amount3 - self.amount2)
        
        self.answer = self.amount3
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.amount4 = Decimal(self.amount4).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s has some money.<br><br>"%(self.name)
        self.problem = self.problem + "Her brother has $%s.<br><br>"%(self.amount1)
        self.problem = self.problem + "If she buys a %s for $%s, she will have $%s less than her brother.<br><br>"%(self.item[0],self.amount2,self.amount4)
        self.problem = self.problem + "How much does she have?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.amount1,self.amount2,self.amount4,self.name,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType14(self,problem,answer,amount1,amount2,amount4,name,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        leftAmount = Decimal(answer) - Decimal(amount2)
        middleAmount = Decimal(amount2)
        rightAmount = Decimal(amount4) - Decimal(amount2)
        if Decimal(leftAmount)==Decimal(middleAmount): # leftCell = 'medium'; middleCell = 'medium'
            leftCellWidth = 100
            middleCellWidth = 100
            firstBrace = 'medium2'
            secondBrace = 'medium'
            if Decimal(leftAmount)==Decimal(rightAmount): # rightCell = 'medium'
                rightCellWidth = 100
                upBrace = 'medium3'
                thirdBrace = 'medium2'
            elif Decimal(leftAmount)>Decimal(rightAmount): # rightCell = 'small'
                rightCellWidth = 50
                upBrace = 'medium2small1'
                thirdBrace = 'medium1small1'
            else: # rightCell = 'large'
                rightCellWidth = 150
                upBrace = 'large1medium2'
                thirdBrace = 'large1medium1'
        elif Decimal(leftAmount)>Decimal(middleAmount):
            if Decimal(rightAmount)<Decimal(middleAmount): # leftCell = 'large'; middleCell = 'medium'; rightCell = 'small' 
                leftCellWidth = 150
                middleCellWidth = 100
                rightCellWidth = 50
                upBrace = 'large2'
                firstBrace = 'large1medium1'
                secondBrace = 'medium'
                thirdBrace = 'medium1small1'
            elif Decimal(rightAmount)<Decimal(leftAmount) and Decimal(rightAmount)>Decimal(middleAmount): # leftCell = 'large'; middleCell = 'small'; rightCell = 'medium' 
                leftCellWidth = 150
                middleCellWidth = 50
                rightCellWidth = 100
                upBrace = 'large2'
                firstBrace = 'large1small1'
                secondBrace = 'small'
                thirdBrace = 'medium1small1'
            elif Decimal(rightAmount)>Decimal(leftAmount):# leftCell = 'medium'; middleCell = 'small'; rightCell = 'large'
                leftCellWidth = 100
                middleCellWidth = 50
                rightCellWidth = 150
                upBrace = 'large2'
                firstBrace = 'medium1small1'
                secondBrace = 'small'
                thirdBrace = 'large1small1'
            elif Decimal(rightAmount)==Decimal(middleAmount): # leftCell = 'large'; middleCell = 'medium'; rightCell = 'medium'  
                leftCellWidth = 150
                middleCellWidth = 100
                rightCellWidth = 150
                upBrace = 'large1medium2'
                firstBrace = 'large1medium1'
                secondBrace = 'medium'
                thirdBrace = 'medium2'
            elif Decimal(rightAmount)==Decimal(leftAmount): # leftCell = 'medium'; middleCell = 'small'; rightCell = 'medium'  
                leftCellWidth = 100
                middleCellWidth = 50
                rightCellWidth = 100
                upBrace = 'medium2small1'
                firstBrace = 'medium1small1'
                secondBrace = 'small'
                thirdBrace = 'medium1small1'
        elif Decimal(leftAmount)<Decimal(middleAmount):
            if Decimal(rightAmount)>Decimal(middleAmount): # leftCell = 'small'; middleCell = 'medium'; rightCell = 'large'  
                leftCellWidth = 50
                middleCellWidth = 100
                rightCellWidth = 150
                upBrace = 'large2'
                firstBrace = 'medium1small1'
                secondBrace = 'medium'
                thirdBrace = 'large1medium1'
            elif Decimal(rightAmount)<Decimal(middleAmount) and Decimal(rightAmount)>Decimal(leftAmount): # leftCell = 'small'; middleCell = 'large'; rightCell = 'medium' 
                leftCellWidth = 50
                middleCellWidth = 150
                rightCellWidth = 100
                upBrace = 'large2'
                firstBrace = 'large1small1'
                secondBrace = 'large'
                thirdBrace = 'large1medium1'
            elif Decimal(rightAmount)<Decimal(leftAmount): # leftCell = 'medium'; middleCell = 'large'; rightCell = 'small'  
                leftCellWidth = 100
                middleCellWidth = 150
                rightCellWidth = 50
                upBrace = 'large2'
                firstBrace = 'large1medium1'
                secondBrace = 'large'
                thirdBrace = 'large1small1'
            elif Decimal(rightAmount)==Decimal(middleAmount): # leftCell = 'small'; middleCell = 'medium'; rightCell = 'medium' 
                leftCellWidth = 50
                middleCellWidth = 100
                rightCellWidth = 100
                upBrace = 'medium2small1'
                firstBrace = 'medium1small1'
                secondBrace = 'medium'
                thirdBrace = 'medium2'
            elif Decimal(rightAmount)==Decimal(leftAmount): # leftCell = 'medium'; middleCell = 'large'; rightCell = 'medium' 
                leftCellWidth = 100
                middleCellWidth = 150
                rightCellWidth = 100
                upBrace = 'large1medium2'
                firstBrace = 'large1medium1'
                secondBrace = 'large'
                thirdBrace = 'large1medium1'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        self.color3 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3>$%s</td></tr>"%(amount1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(upBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>Brother</td><td colspan=3 style='background-color:%s;height:25px;border:white solid 1px;'></td></tr>"%(self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border-left:white solid 1px;border-top:white solid 1px;border-bottom:white solid 1px;width:%dpx'></td><td style='background-color:%s;height:25px;border-left:white dotted 1px;border-right:white solid 1px;border-top:white solid 1px;border-bottom:white solid 1px;width:%dpx'></td><td style='height:25px;border-top:white dotted 1px;border-bottom:white dotted 1px;border-right:white dotted 1px;width:%dpx'></td></tr>"%(name,self.color2,leftCellWidth,self.color2,middleCellWidth,rightCellWidth)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td>&nbsp;</td></tr>"%(secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td style='padding-top:0px;padding-bottom:0px'>$%s</td><td>&nbsp;</td></tr>"%(amount2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(thirdBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td colspan=2 style='padding-top:0px;padding-bottom:0px'>$%s</td></tr>"%(amount4)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td>&nbsp;</td></tr>"%(firstBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-top:0px;padding-bottom:0px'>?</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount4,amount2,str(Decimal(amount4)-Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s has $%s less than her brother.</font>"%(name,str(Decimal(amount4)-Decimal(amount2)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,str(Decimal(amount4)-Decimal(amount2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>She has $%s.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType15(self):       
        '''e.g.:
        A <water bottle> costs $12.45.
        A <lunch box> costs $4.55 less.
        [Person.Boyname] wants to buy both the items.
        How much money will he need?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['water bottle','lunch box',randint(8,15),randint(2,5),'water bottle','lunch box'],
                      ['box of cereal','bottle of milk',randint(4,6),randint(2,3),'cereal','milk'],
                      ['box of poster colours','set of brushes',randint(15,25),randint(5,10),'poster colours','brushes'],
                      ['lamp','candle holder',randint(15,25),randint(5,12),'lamp','candle holder'],
                      ['mat','towel',randint(10,20),randint(5,8),'mat','towel'],
                      ['book','pen',randint(20,30),randint(5,15),'book','pen'],
                      ['headset','computer mouse',randint(25,45),randint(5,10),'headset','computer mouse'],
                      ['pen holder','fridge magnet',randint(8,15),randint(3,6),'pen holder','fridge magnet'],
                      ['bathroom mirror','soap dispenser',randint(35,45),randint(30,33),'bathroom mirror','soap dispenser'],
                      ['cooking pan','serving dish',randint(15,25),randint(5,10),'cooking pan','serving dish'],
                      ['toy truck','bubble kit',randint(20,30),randint(10,15),'toy truck','bubble kit'],
                      ['kite','kite spool',randint(15,25),randint(10,12),'kite','kite spool'],
                      ['bag of balloons','balloon pump',randint(5,8),randint(1,3),'bag of balloons','balloon pump'],
                      ['kettle','mug',randint(15,25),randint(8,10),'kettle','mug'],
                      ['a pair of swimming goggles','swimming cap',randint(25,35),randint(10,15),'swimming goggles','swimming cap']]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(0,95,5)
        self.cents2 = random.randrange(5,95,5)

        self.number1 = self.item[2]
        self.number2 = self.item[3]

        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100        
        
        self.answer = self.amount1 + self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "A %s costs $%s.<br><br>"%(self.item[0],self.amount1)
        self.problem = self.problem + "A %s costs $%s less.<br><br>"%(self.item[1],self.amount2)
        self.problem = self.problem + "%s wants to buy both the items.<br><br>"%(self.name)
        self.problem = self.problem + "How much money will he need?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.amount1,self.amount2,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType15",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType15(self,problem,answer,amount1,amount2,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        amount3 = Decimal(amount1)-Decimal(amount2)
        if amount3>Decimal(amount2):
            firstCellWidth = 100
            secondCellBrace = 'small'
            amount1CellBrace = 'medium1small1'
        elif amount3<Decimal(amount2):
            firstCellWidth = 50
            secondCellBrace = 'medium'
            amount1CellBrace = 'medium1small1'
        else:
            firstCellWidth = 100
            secondCellBrace = 'medium'
            amount1CellBrace = 'medium2'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%s</td></tr>"%(amount1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(amount1CellBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px'></td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(item[4],self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td><td>&nbsp;</td></tr>"%(item[5],self.color2,firstCellWidth)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td style='vertical-align:top;'><img src='/images/explanation/P3_model_down_brace_%s.png' /><br>$%s</td></tr>"%(secondCellBrace,amount2)
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)-Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>The %s costs $%s.</font>"%(item[1],str(Decimal(amount1)-Decimal(amount2)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,str(Decimal(amount1)-Decimal(amount2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>He will need $%s to buy both the items.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType16(self):       
        '''e.g.:
        <A store has a promotion on toys.>
        A <spinning top> that has a usual price of $17.80 is selling at a discounted price of $12.40.
        [Person.Boyname] buys two such <spinning tops>.
        How much discount does he receive altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['A store has a promotion on toys.','spinning top','spinning tops',randint(10,20)],
                      ['Coffee beans are on sale at a supermarket.','bag of coffee beans','bags of coffee beans',randint(10,20)],
                      ['A toys store has water bottles on sale.','water bottle','water bottles',randint(10,20)],
                      ['Tea kettles are on promotion at a department store.','tea kettle','tea kettles',randint(15,30)],
                      ['Bean bags are on sale at a furniture fair.','bean bag','bean bags',randint(20,40)],
                      ['Shirts are on clearance at a store.','shirt','shirts',randint(20,40)],
                      ['An IT shop has a year-end promotion on several items.','flash drive','flash drives',randint(15,25)],
                      ['A furniture store is selling rugs on promotion.','rug','rugs',randint(35,50)],
                      ['A year-end sale has school bags on clearance.','school bag','school bags',randint(25,45)],
                      ['A bed and linen store has a clearance sale.','blanket','blankets',randint(20,40)]]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(0,95,5)
        self.cents2 = random.randrange(5,95,5)

        self.number1 = self.item[3]
        self.number2 = int(float(randint(5,7))/10*self.number1)

        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100        
        
        self.answer = 2 * (self.amount1 - self.amount2)
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s<br><br>"%(self.item[0])
        self.problem = self.problem + "A %s that has a usual price of $%s is selling at a discounted price of $%s.<br><br>"%(self.item[1],self.amount1,self.amount2)
        self.problem = self.problem + "%s buys two such %s.<br><br>"%(self.name,self.item[2])
        self.problem = self.problem + "How much discount does he receive altogether?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType16(self.problem,self.answer,self.amount1,self.amount2,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType16",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType16(self,problem,answer,amount1,amount2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        usualPrice = Decimal(amount1)
        sellingPrice = Decimal(amount2)
        discount = Decimal(usualPrice)-Decimal(sellingPrice)
        if sellingPrice>Decimal(discount):
            sellingPriceBrace = 'large'
            discountBrace = 'medium'
            usualPriceBrace = 'large1medium1'
        elif sellingPrice<Decimal(discount): # this shouldn't happen
            sellingPriceBrace = 'medium'
            discountBrace = 'large'
            usualPriceBrace = 'large1medium1'
        else: #sellingPrice = discount
            sellingPriceBrace = 'medium'
            discountBrace = 'medium'
            usualPriceBrace = 'medium2'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%s</td></tr>"%(usualPrice)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(usualPriceBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;height:25px;border:white solid 1px;'></td></tr>"%(item1,self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(sellingPriceBrace,discountBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%s</td><td>?</td></tr>"%(sellingPrice)
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(str(usualPrice),str(sellingPrice),str(discount))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>He receives a discount of $%s on one %s.</font>"%(str(discount),item1)
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(str(discount),str(discount),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>He receives a discount of $%s altogether.</font>"%(answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType17(self):       
        '''e.g.:
        <An adult ticket at a museum> costs $25.90.
        It costs $12.10 more than <a child ticket>.
        [Person.Auntyname] bought <an adult ticket and a child ticket>.
        How much did she pay for the two <tickets>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [['An adult ticket at a museum','a child ticket','an adult ticket and a child ticket','tickets','adult ticket','child ticket','A child ticket'],
                      ["A child ticket at a kid's indoor playground","an adult ticket","a child ticket and an adult ticket","tickets",'child ticket','adult ticket','An adult ticket'],
                      ["A child pass at a kid's water park","an adult pass","a child pass and an adult pass","passes",'child pass','adult pass',"An adult pass"],
                      ["A regular meal at a restaurant","a kid's meal","a regular meal and a kid's meal","meals",'regular meal',"kid's meal","A kid's meal"],
                      ['A regular train pass','a senior citizen train pass','a regular pass and a senior citizen pass','passes','regular pass','senior citizen pass','A senior citizen train pass'],
                      ['An adult ticket at a butterfly park','a child ticket','an adult ticket and a child ticket','tickets','adult ticket','child ticket','A child ticket'],
                      ['A regular entry pass at an amusement park','a child entry pass','a regular entry pass and a child entry pass','entry passes','regular pass','child pass','A child entry pass'],
                      ['A 3D movie ticket','a regular movie ticket','a 3D movie ticket and a regular movie ticket','movie tickets','3D movie ticket','regular movie ticket','A regular movie ticket'],
                      ['A dance show pass at an arts festival','a music show pass','a dance show pass and a music show pass','two passes','dance show pass','music show pass','A music show pass'],
                      ['A coupon booklet for games at a funfair','a coupon booklet for food','a coupon booklet for games and a coupon booklet for food','coupon booklets','games','food','A coupon booklet for food']]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(0,95,5)
        self.cents2 = random.randrange(5,95,5)

        self.number1 = randint(20,30)
        self.number2 = int(float(randint(5,7))/10*self.number1)

        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100        
        
        self.answer = self.amount1 + self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s costs $%s.<br><br>"%(self.item[0],self.amount1)
        self.problem = self.problem + "It costs $%s more than %s.<br><br>"%(self.amount2,self.item[1])
        self.problem = self.problem + "%s bought %s.<br><br>"%(self.name,self.item[2])
        self.problem = self.problem + "How much did she pay for the two %s?"%(self.item[3])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType17(self.problem,self.answer,self.amount1,self.amount2,self.item[3],self.item[4],self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType17",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType17(self,problem,answer,amount1,amount2,item3,item4,item5,item6,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        amount3 = Decimal(amount1)-Decimal(amount2)
        if amount3>Decimal(amount2):
            firstCellWidth = 100
            secondCellBrace = 'small'
            amount1CellBrace = 'medium1small1'
        elif amount3<Decimal(amount2):
            firstCellWidth = 50
            secondCellBrace = 'medium'
            amount1CellBrace = 'medium1small1'
        else:
            firstCellWidth = 100
            secondCellBrace = 'medium'
            amount1CellBrace = 'medium2'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%s</td></tr>"%(amount1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(amount1CellBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px'></td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(item4,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td><td>&nbsp;</td></tr>"%(item5,self.color2,firstCellWidth)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td style='vertical-align:top;'><img src='/images/explanation/P3_model_down_brace_%s.png' /><br>$%s</td></tr>"%(secondCellBrace,amount2)
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)-Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s costs $%s.</font>"%(item6,str(Decimal(amount1)-Decimal(amount2)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,str(Decimal(amount1)-Decimal(amount2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>She paid $%s for the two %s.</font>"%(answer,item3)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType18(self):       
        '''e.g.:
        [Person.Boyname1] and [Person.Boyname2] went to a <mall>.
        [Person.Boyname1] bought a <hat> for $43.10.
        [Person.Boyname2] bought a different <hat> that was $12.90 cheaper.
        How much did the two boys spend altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.BoyName,2)
        
        self.items = [['mall','hat',randint(30,50)],['mall','pair of sweatpants',randint(25,50)],['store','headset',randint(30,50)],['toys store','toy helicopter',randint(15,30)],['toys store','monopoly board game',randint(20,50)],['sports store','pair of shin guards',randint(20,35)],['sports store','pair of tennis shoes',randint(25,50)],['book fair','picture book',randint(20,40)],['furniture store','stool',randint(25,35)],['supermarket','box of cookies',randint(10,20)]]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(0,95,5)
        self.cents2 = random.randrange(5,95,5)

        self.number1 = self.item[2]
        self.number2 = int(float(randint(2,4))/10*self.number1)

        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100        
        
        self.answer = self.amount1 + self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s and %s went to a %s.<br><br>"%(self.names[0],self.names[1],self.item[0])
        self.problem = self.problem + "%s bought a %s for $%s.<br><br>"%(self.names[0],self.item[1],self.amount1)
        self.problem = self.problem + "%s bought a different %s that was $%s cheaper.<br><br>"%(self.names[1],self.item[1],self.amount2)
        self.problem = self.problem + "How much did the two boys spend altogether?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType18(self.problem,self.answer,self.names[0],self.names[1],self.amount1,self.amount2,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType18",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType18(self,problem,answer,name0,name1,amount1,amount2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        amount3 = Decimal(amount1)-Decimal(amount2)
        if amount3>Decimal(amount2):
            firstCellWidth = 100
            secondCellBrace = 'small'
            amount1CellBrace = 'medium1small1'
        elif amount3<Decimal(amount2):
            firstCellWidth = 50
            secondCellBrace = 'medium'
            amount1CellBrace = 'medium1small1'
        else:
            firstCellWidth = 100
            secondCellBrace = 'medium'
            amount1CellBrace = 'medium2'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%s</td></tr>"%(amount1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(amount1CellBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px'></td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(name0,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td><td>&nbsp;</td></tr>"%(name1,self.color2,firstCellWidth)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td style='vertical-align:top;'><img src='/images/explanation/P3_model_down_brace_%s.png' /><br>$%s</td></tr>"%(secondCellBrace,amount2)
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)-Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s bought his %s for $%s.</font>"%(name1,item1,str(Decimal(amount1)-Decimal(amount2)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,str(Decimal(amount1)-Decimal(amount2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>The two boys spent $%s altogether.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType19(self):       
        '''e.g.:
        [Person.Girlname] had $50.
        She bought <some groceries> for $35.25 and spent another $7.90 on <transportation>.
        How much money had she left?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['some groceries','transportation',randint(20,60),randint(5,10)],
                      ['a blouse','a scarf',randint(20,60),randint(10,20)],
                      ['some books','a purse',randint(20,50),randint(10,20)],
                      ['a bag','a belt',randint(30,40),randint(15,25)],
                      ['a skirt','a watch',randint(20,30),randint(35,45)],
                      ['a T-shirt','a jacket',randint(15,25),randint(35,55)],
                      ['a pair of jeans','food',randint(30,50),randint(5,20)],
                      ['a wallet','some toys',randint(15,25),randint(5,50)],
                      ['a present for her friend','a greeting card',randint(15,30),randint(2,5)],
                      ['a pair of sunglasses','a sunscreen lotion',randint(20,50),randint(7,15)]]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(0,95,5)
        self.cents2 = random.randrange(5,95,5)

        self.number1 = self.item[2]
        self.number2 = self.item[3]

        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100
        
        self.amount3 = int(self.amount1 + self.amount2) + randint(2,15)       
        
        self.answer = self.amount3 - self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s had $%d.<br><br>"%(self.name,self.amount3)
        self.problem = self.problem + "She bought %s for $%s and spent another $%s on %s.<br><br>"%(self.item[0],self.amount1,self.amount2,self.item[1])
        self.problem = self.problem + "How much money had she left?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType19(self.problem,self.answer,self.amount1,self.amount2,self.amount3,self.name,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType19",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType19(self,problem,answer,amount1,amount2,amount3,name,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        # Check the values of the 3 amounts
        if Decimal(amount1)==Decimal(amount2):
            firstCell = 'medium'
            secondCell = 'medium'
            if Decimal(amount1)==Decimal(answer):
                thirdCell = 'medium'
                upBrace = 'medium3'
            elif Decimal(amount1)>Decimal(answer):
                thirdCell = 'small'
                upBrace = 'medium2small1'
            else:
                thirdCell = 'large'
                upBrace = 'large1medium2'
        elif Decimal(amount1)>Decimal(amount2):
            if Decimal(answer)<Decimal(amount2):
                firstCell = 'large'
                secondCell = 'medium'
                thirdCell = 'small'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)<Decimal(amount1) and Decimal(answer)>Decimal(amount2):
                firstCell = 'large'
                secondCell = 'small'
                thirdCell = 'medium'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)>Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'small'
                thirdCell = 'large'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)==Decimal(amount2):
                firstCell = 'large'
                secondCell = 'medium'
                thirdCell = 'medium'
                upBrace = 'large1medium2'
            elif Decimal(answer)==Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'small'
                thirdCell = 'medium'
                upBrace = 'medium2small1'
        elif Decimal(amount1)<Decimal(amount2):
            if Decimal(answer)>Decimal(amount2):
                firstCell = 'small'
                secondCell = 'medium'
                thirdCell = 'large'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)<Decimal(amount2) and Decimal(answer)>Decimal(amount1):
                firstCell = 'small'
                secondCell = 'large'
                thirdCell = 'medium'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)<Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'large'
                thirdCell = 'small'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)==Decimal(amount2):
                firstCell = 'small'
                secondCell = 'medium'
                thirdCell = 'medium'
                upBrace = 'medium2small1'
            elif Decimal(answer)==Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'large'
                thirdCell = 'medium'
                upBrace = 'large1medium2'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        self.color3 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td colspan=3>$%s</td></tr>"%(amount3)
        self.solution_text = self.solution_text + "<tr><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(upBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(self.color1,self.color2,self.color3)
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstCell,secondCell,thirdCell)
        self.solution_text = self.solution_text + "<tr><td>$%s</td><td>$%s</td><td>?</td></tr>"%(amount1,amount2)
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)+Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s spent $%s altogether.</font>"%(name,str(Decimal(amount1)+Decimal(amount2)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s.00 &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount3,str(Decimal(amount1)+Decimal(amount2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>She had $%s left.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType20(self):       
        '''e.g.:
        [Person.Boyname] <has> $49.20.
        He wants to buy two <cricket bats> that cost $38.90 each.
        How much more money must he <have>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['saves','cricket bats','save',randint(25,45),'cricket bats'],
                      ['saves','soccer balls','save',randint(20,35),'soccer balls'],
                      ['saves','table tennis bats','save',randint(15,30),'table tennis bats'],
                      ['saves','tennis rackets','save',randint(35,45),'tennis rackets'],
                      ['saves','pairs of swimming goggles','save',randint(15,35),'pairs of goggles'],
                      ['saves','helmets','save',randint(10,30),'helmets'],
                      ['saves','golf clubs','save',randint(25,40),'golf clubs'],
                      ['has','watermelons','have',randint(3,6),'watermelons'],
                      ['has','pencil cases','have',randint(5,15),'pencil cases'],
                      ['has','boxes of chocolates','have',randint(5,25),'boxes of chocolates'],
                      ['has','cans of soup','have',randint(2,5),'cans of soup'],
                      ['has','cartons of juice','have',randint(3,7),'cartons of juice'],
                      ['has','bottles of soda','have',randint(2,5),'bottles of soda'],
                      ['has','sharpeners','have',randint(3,10),'sharpeners']]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(60,95,5)
        self.cents2 = random.randrange(5,35,5)

        self.number2 = self.item[3]
        self.number1 = randint(int(1.1*self.number2),int(1.8*self.number2))
        
        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100     
        
        self.answer = 2*self.amount2 - self.amount1
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s %s $%s.<br><br>"%(self.name,self.item[0],self.amount1)
        self.problem = self.problem + "He wants to buy two %s that cost $%s each.<br><br>"%(self.item[1],self.amount2)
        self.problem = self.problem + "How much more money must he %s?"%(self.item[2])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType20(self.problem,self.answer,self.amount1,self.amount2,self.item[1],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType20",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType20(self,problem,answer,amount1,amount2,item1,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        self.color3 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%s</td><td colspan=2>$%s</td></tr>"%(amount2,amount2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium.png' /></td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='padding-right:7px;'>2 %s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;width:50px;'></td><td style='border:white solid 1px;'></td></tr>"%(item4,self.color2,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_large.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'>$%s</td><td style='padding-bottom:3px;'>?</td></tr>"%(amount1)
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount2,amount2,str(Decimal(amount2)+Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>The cost of 2 %s is $%s.</font>"%(item1,str(Decimal(amount2)+Decimal(amount2)))
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(str(Decimal(amount2)+Decimal(amount2)),amount1,answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>He must save $%s more.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType21(self):       
        '''e.g.:
        [Person.Girlname] <earned> $50< in three days>.
        She <earned> $12.45 <on Day 1>, $23.90 <on Day 2> and the rest <on Day 3>.
        How much did she <earn on Day 3>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['earned',' in three days','earned','on Day 1','on Day 2','on Day 3','earn on Day 3',randint(50,100),'on Day 1 and Day 2','on Day 3'],
                      ['saved',' in three weeks','saved','in Week 1','in Week 2','in Week 3','save in Week 3',randint(30,50),'in Week 1 and Week 2','in Week 3'],
                      ['spent',' in three days','spent','on Day 1','on Day 2','on Day 3','spend on Day 3',randint(10,30),'on Day 1 and Day 2','on Day 3'],
                      ['spent',' on shopping','spent','on a T-shirt',' on a bracelet','on a necklace','spend on the necklace',randint(30,60),'on the T-shirt and the bracelet','on the necklace'],
                      ['received',' from her family members','received','from her mother','from her uncle','from her grandmother','receive from her grandmother',randint(50,100),'from her mother and her grandmother','from her grandmother'],
                      ['went to a school festival and spent','','spent','on games','on food','on rides','spend on rides',randint(30,50),'on games and food','on rides'],
                      ['paid',' in various bills','paid','for food','for taxi','for groceries','pay for groceries',randint(30,50),'for food and taxi','for groceries'],
                      ['earned',' for doing chores','earned','for babysitting','for mowing','for cleaning her house','earn for cleaning her house',randint(20,40),'for babysitting and mowing','for cleaning her house'],
                      ['spent',' at a bookshop','spent','on a book','on a puzzle','on a box of colours','spend on the box of colours',randint(30,60),'on the book and the puzzle','on the box of colours'],
                      ['saved',' in three days','saved','on Thursday','on Friday','on Saturday','save on Saturday',randint(20,40),'on Thursday and Friday','on Saturday']]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(5,95,5)
        self.cents2 = random.randrange(5,95,5)

        self.number = self.item[7]
        self.number1 = int(float(randint(25,40))/100*self.number)
        self.number2 = int(float(randint(25,40))/100*self.number)
        
        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.number2*100+self.cents2)/100     

        self.answer = self.number - (self.amount1+self.amount2)
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s %s $%d%s.<br><br>"%(self.name,self.item[0],self.number,self.item[1])
        self.problem = self.problem + "She %s $%s %s, $%s %s and the rest %s.<br><br>"%(self.item[2],self.amount1,self.item[3],self.amount2,self.item[4],self.item[5])
        self.problem = self.problem + "How much did she %s?"%(self.item[6])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType21(self.problem,self.answer,self.number,self.amount1,self.amount2,self.name,self.item[2],self.item[8],self.item[9],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType21",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType21(self,problem,answer,total,amount1,amount2,name,item2,item8,item9,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        # Check the values of the 3 amounts
        if Decimal(amount1)==Decimal(amount2):
            firstCell = 'medium'
            secondCell = 'medium'
            if Decimal(amount1)==Decimal(answer):
                thirdCell = 'medium'
                upBrace = 'medium3'
            elif Decimal(amount1)>Decimal(answer):
                thirdCell = 'small'
                upBrace = 'medium2small1'
            else:
                thirdCell = 'large'
                upBrace = 'large1medium2'
        elif Decimal(amount1)>Decimal(amount2):
            if Decimal(answer)<Decimal(amount2):
                firstCell = 'large'
                secondCell = 'medium'
                thirdCell = 'small'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)<Decimal(amount1) and Decimal(answer)>Decimal(amount2):
                firstCell = 'large'
                secondCell = 'small'
                thirdCell = 'medium'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)>Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'small'
                thirdCell = 'large'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)==Decimal(amount2):
                firstCell = 'large'
                secondCell = 'medium'
                thirdCell = 'medium'
                upBrace = 'large1medium2'
            elif Decimal(answer)==Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'small'
                thirdCell = 'medium'
                upBrace = 'medium2small1'
        elif Decimal(amount1)<Decimal(amount2):
            if Decimal(answer)>Decimal(amount2):
                firstCell = 'small'
                secondCell = 'medium'
                thirdCell = 'large'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)<Decimal(amount2) and Decimal(answer)>Decimal(amount1):
                firstCell = 'small'
                secondCell = 'large'
                thirdCell = 'medium'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)<Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'large'
                thirdCell = 'small'
                upBrace = 'large1medium1small1'
            elif Decimal(answer)==Decimal(amount2):
                firstCell = 'small'
                secondCell = 'medium'
                thirdCell = 'medium'
                upBrace = 'medium2small1'
            elif Decimal(answer)==Decimal(amount1):
                firstCell = 'medium'
                secondCell = 'large'
                thirdCell = 'medium'
                upBrace = 'large1medium2'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        self.color3 = random.choice(['yellow','gold','greenyellow','lemonchiffon','lightgoldenrodyellow','mediumspringgreen','navajowhite','peachpuff'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td colspan=3>$%s</td></tr>"%(total)
        self.solution_text = self.solution_text + "<tr><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(upBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(self.color1,self.color2,self.color3)
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstCell,secondCell,thirdCell)
        self.solution_text = self.solution_text + "<tr><td>$%s</td><td>$%s</td><td>?</td></tr>"%(amount1,amount2)
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,str(Decimal(amount1)+Decimal(amount2)))
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%s %s $%s %s.</font>"%(name,item2,str(Decimal(amount1)+Decimal(amount2)),item8)
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%d.00 &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(total,str(Decimal(amount1)+Decimal(amount2)),answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>She %s $%s %s.</font>"%(item2,answer,item9)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType22(self):       
        '''e.g.:
        [Person.Girlname1] <counts> 15 <twenty-cent coins in her coin-bank>.
        [Person.Girlname2] <counts> $2.50< in her wallet>.
        How much money do the two girls <have> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.GirlName,2)
        
        self.items = [['counts','twenty-cent coins in her coin-bank','counts',' in her wallet','have',randint(2,20),20,'twenty-cent coins'],
                      ['has','tewnty-cent coins with her','has',' with her','have',randint(2,20),20,'twenty-cent coins'],
                      ['earns','twenty-cent coins for helping her mother','earns',' for helping her neighbour','earn',randint(5,20),20,'twenty-cent coins'],
                      ['collects','five-cent coins','collects','','collect',randint(2,20),5,'five-cent coins'],
                      ['gets','five-cent coins from her teacher','gets',' from her brother','get',randint(2,20),5,'five-cent coins'],
                      ['saves','ten-cent coins in a week','saves',' in a week','save in a week',randint(2,20),10,'ten-cent coins'],
                      ['spends','ten-cent coins on a pencil','spends',' on a pen','spend',randint(2,20),10,'ten-cent coins'],
                      ['wins','ten-cent coins in a game at a funfair','wins','','win',randint(2,20),10,'ten-cent coins'],
                      ['receives','fifty-cent coins from her father','receives',' from her grandmother','receive',randint(5,10),50,'fifty-cent coins'],
                      ['spends','fifty-cent coins on a pancake at the bakery','spends',' on some cupcakes','spend',randint(4,10),50,'fifty-cent coins'],
                      ['earns','fifty-cent coins','earns','','earn',randint(2,20),50,'fifty-cent coins']]
        
        self.item = random.choice(self.items)
        
        self.cents1 = random.randrange(5,95,5)

        self.number1 = randint(2,10)
        self.number2 = self.item[5]
        self.number3 = self.item[6]
        self.cents2 = self.number2*self.number3
        
        self.amount1 = Decimal(self.number1*100+self.cents1)/100
        self.amount2 = Decimal(self.cents2)/100     

        self.answer = self.amount1 + self.amount2
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s %s %d %s.<br><br>"%(self.names[0],self.item[0],self.number2,self.item[1])
        self.problem = self.problem + "%s %s $%s%s.<br><br>"%(self.names[1],self.item[2],self.amount1,self.item[3])
        self.problem = self.problem + "How much money do the two girls %s altogether?"%(self.item[4])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType22(self.problem,self.answer,self.amount1,self.amount2,self.number2,self.number3,self.names,self.item[0],self.item[4],self.item[7],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType22",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType22(self,problem,answer,amount2,amount1,number2,number3,names,item0,item4,item7,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        # no direct mapping between the variable names in GenerateProblem and Explain
        # amount1: number2 x number3; girl1's money
        # amount2: girl 2's money
        if amount1 > amount2:
            if amount2 > (amount1-amount2):
                amount1Brace = 'large'
                amount2Brace = 'medium'
                diffCellWidth = 50
            elif amount2 < (amount1-amount2):
                amount1Brace = 'large'
                amount2Brace = 'small'
                diffCellWidth = 100
            else:
                amount1Brace = 'medium'
                amount2Brace = 'small'
                diffCellWidth = 50
        elif amount1 < amount2:
            if amount1 > (amount2-amount1):
                amount1Brace = 'medium'
                amount2Brace = 'large'
                diffCellWidth = 50
            elif amount1 < (amount2-amount1):
                amount1Brace = 'small'
                amount2Brace = 'large'
                diffCellWidth = 100
            else:
                amount1Brace = 'small'
                amount2Brace = 'medium'
                diffCellWidth = 50
        elif amount1 == amount2:
            amount1Brace = 'medium'
            amount2Brace = 'medium'
                
        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left;'>%d %s</td><td>&nbsp; = &nbsp;</td><td style='text-align:left'>%d &nbsp;&times;&nbsp; %d &cent;</td></tr>"%(number2,item7,number2,number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp; = &nbsp;</td><td style='text-align:left'>%d &cent;</td></tr>"%(number2*number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp; = &nbsp;</td><td style='text-align:left'>$%s</td></tr>"%(str(amount1))
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s %s $%s.</font>"%(names[0],item0,str(amount1))

        self.solution_text = self.solution_text + "<br><br><br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        if amount1 > amount2:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%s</td></tr>"%(amount1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(amount1Brace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'></td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(names[0],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='width:%dpx'></td></tr>"%(names[1],self.color2,diffCellWidth)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td>&nbsp;</td></tr>"%(amount2Brace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'>$%s</td><td>&nbsp;</td></tr>"%(amount2)
        elif amount1 < amount2:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%s</td></tr>"%(amount1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(amount1Brace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='width:%dpx'>&nbsp;</td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(names[0],self.color1,diffCellWidth)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'></td></tr>"%(names[1],self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"%(amount2Brace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'>$%s</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"%(amount2)
        elif amount1 == amount2:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%s</td></tr>"%(amount1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(amount1Brace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(names[0],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td></tr>"%(names[1],self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(amount2Brace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'>$%s</td></tr>"%(amount2)
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><br><font class='ExplanationFont'>$%s &nbsp;+&nbsp; $%s &nbsp;=&nbsp; $%s</font>"%(amount1,amount2,answer)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>The two girls %s $%s altogether.</font>"%(item4,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType23(self):       
        '''e.g.:
        [Person.Name1] and [Person.Name2] <shared> $1.20.
        [Person.Name1] <received> $0.40 more than [Person.Name2].
        How much did [Person.Name2] <receive>?
        Give your answer in cents.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.PersonName,2)
        
        self.items = [['shared','received','receive'],['had','had','have'],['saved','saved','save'],['collected','collected','collect'],['counted','counted','count'],['spent','spent','spend'],['shared','got','get'],['earned','earned','earn'],['won','won','win'],['donated','donated','donate']]
        
        self.item = random.choice(self.items)
        
        self.cents = random.randrange(10,90,5)

        self.cents1 = random.randrange(10,95,5)
        self.cents2 = self.cents*2+self.cents1
        
        self.amount1 = Decimal(self.cents1)/100
        self.amount2 = Decimal(self.cents2)/100

        self.answer = self.cents
        
        TWOPLACES = Decimal(10) ** -2

        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)

        self.problem = "%s and %s %s $%s.<br><br>"%(self.names[0],self.names[1],self.item[0],self.amount2)
        self.problem = self.problem + "%s %s $%s more than %s.<br><br>"%(self.names[0],self.item[1],self.amount1,self.names[1])
        self.problem = self.problem + "How much did %s %s?<br><br>Give your answer in cents."%(self.names[1],self.item[2])
                   
        self.unit = "&cent;"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType23(self.problem,self.answer,self.amount1,self.amount2,self.names,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType23",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType23(self,problem,answer,amount1,amount2,names,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        amount3 = Decimal(Decimal(answer)/100)
        amount1Cents = int(Decimal(amount1)*100)
        amount2Cents = int(Decimal(amount2)*100)
        if amount3 < amount1:
            answerBrace = 'small'
            diffBrace = 'medium'
        elif amount3 > amount1:
            answerBrace = 'medium'
            diffBrace = 'small'
        elif amount3 == amount1:
            answerBrace = 'medium'
            diffBrace = 'medium'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border-left:white solid 1px;border-top:white solid 1px;border-bottom:white solid 1px;border-right:white dotted 1px;'></td><td style='background-color:%s;height:25px;border-right:white solid 1px;border-top:white solid 1px;border-bottom:white solid 1px;'></td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;$%s</td></tr>"%(names[0],self.color2,self.color2,amount2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td>&nbsp;</td></tr>"%(names[1],self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-top:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td style='padding-top:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(answerBrace,diffBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'>?</td><td style='padding-bottom:3px;'>$%s</td></tr>"%(amount1)
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;'>$%s &nbsp;&minus;&nbsp; $%s</td><td>&nbsp; = &nbsp;</td><td style='text-align:left'>%d &cent; &nbsp;&minus;&nbsp; %d &cent;</td></tr>"%(amount2,amount1,amount2Cents,amount1Cents)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp; = &nbsp;</td><td style='text-align:left'>%d &cent;</td></tr>"%(amount2Cents-amount1Cents)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;'>%d &cent; &nbsp;&divide;&nbsp; 2</td><td>&nbsp; = &nbsp;</td><td style='text-align:left'>%d &cent;</td></tr>"%(amount2Cents-amount1Cents,answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>%s %s %d &cent;.</font>"%(names[1],item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False