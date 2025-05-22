'''
Created on Apr 22, 2013
Module: P3MOSubtraction
Generates the Subtraction problems on Money for Primary 3

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

class P3MOSubtraction:
    
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
                            10:["ProblemType10",],
                            11:["ProblemType11",],
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
                                    10:[self.GenerateProblemType10(),],
                                    11:[self.GenerateProblemType11(),],
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
        return self.GenerateProblemTypeMCQ2()
        
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
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        Find the difference $%s and $%s.'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.decimal1digit1 = randint(5,9)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(0,self.decimal1digit1)
        self.decimal2digit2 = 0
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1digit1 = randint(5,9)
        self.number1digit2 = randint(5,9)
        self.number2digit1 = randint(0,self.number1digit1-1)
        self.number2digit2 = randint(0,self.number1digit2)
        
        self.number1 = str(self.number1digit1)+str(self.number1digit2)
        self.number2 = str(self.number2digit1)+str(self.number2digit2)
        
        self.amount1 = Decimal(int(self.number1)*100+int(self.decimal1))/100
        self.amount2 = Decimal(int(self.number2)*100+int(self.decimal2))/100
                
        self.answer = self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "Find the difference of $%s and $%s."%(self.amount1,self.amount2)
                   
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
        
        self.solution_text = self.GenerateSolution(answer,decimal1,decimal2,number1,number2,amount1,amount2)
        self.solution_text = self.solution_text +"</font>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        Subtract.
        $25.20 - $18.65 = ________'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.decimal1digit1 = randint(0,9)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(0,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(40,90)
        self.number2 = randint(20,self.number1-5)
        
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "Subtract.<br><br>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; _____."%(self.amount1,self.amount2)
                   
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

        self.solution_text = self.GenerateSolution(answer,decimal1,decimal2,number1,number2,amount1,amount2)
        self.solution_text = self.solution_text +"</font>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        [Person.Girlname] had $4.90 at first.
        She bought a <packet of gummies> for $2.55.
        How much money had she left?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = ['packet of gummies','carton of milk','box of chocolates','packet of juice','box of cereals','jar of mixed fruit jam','bag of nuts','jar of peanut butter','block of cheese','tube of toothpaste','bottle of shampoo','bag of potatoes','bag of frozen food','tray of eggs','block of butter','cup of yogurt','bottle of hand wash','can of mixed fruit','watermelon','cantaloupe','bag of sweets','bar of chocolate','box of muffins']
        self.item = random.choice(self.items)
        
        self.decimal1digit1 = randint(0,9)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(0,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(6,20)
        self.number2 = randint(2,4)
        
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s had $%s at first.<br><br>"%(self.name,self.amount1)
        self.problem = self.problem + "She bought a %s for $%s.<br><br>How much money had she left?"%(self.item,self.amount2)
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.amount1,self.amount2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,decimal1,decimal2,number1,number2,amount1,amount2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = self.GenerateSolution(answer,decimal1,decimal2,number1,number2,amount1,amount2)
        self.solution_text = self.solution_text + "<br><br>She had $%s left.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        [Person.Boyname] <had> $44.90< in his wallet>.
        <After buying a pair of soccer shoes, he had> $12.35 <left in his wallet>.
        <What was the cost of the soccer shoes?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['had',' in his wallet','After buying a pair of soccer shoes, he had','left in his wallet','What was the cost of the soccer shoes?','The cost soccer shoes was','.'],
                      ['had',' in his wallet','He bought a toy gun for','and saved the rest','Find the sum of money he saved.','He saved','.'],
                      ['had',' with him','After buying a pair of tickets to a concert, he had','left','How much did he pay for the concert tickets?','He paid',' for the concert tickets.'],
                      ['had',' in his saving bank','He used some of his money to buy a waveboard and had','left in his saving bank','Find the cost of the waveboard.','The cost of the waveboard was','.'],
                      ['counted',' in his piggy bank','He put','back in the bank and used the rest to buy a helmet','How much money did he put back in his bank?','He put',' in his bank.'],
                      ['went to a toys shop with','','He bought a scooter for himself and had','left','How much did he spend on the scooter?','He spent',' on the scooter.'],
                      ['saved','','After buying a doll for his little sister he had','of his savings left','What was the cost of the doll?','The cost of the doll','.'],
                      ['went to a sports shop with','','He bought a pair of boxing gloves and had','left','How much did he spend on the boxing gloves?','He spent',' on the boxing gloves.'],
                      ['did chores for his neighbours and received','','He used some of that money to buy a bottle of perfume for his father and had','left','How much did he spend on the perfume?','He spent',' on the perfume.'],
                      ['received',' from his grandfather','He bought a surfboard with it and had','left','How much did he pay for the surfboard?','He paid',' for the surfboard.']]
        self.item = random.choice(self.items)
        
        self.decimal1digit1 = randint(0,9)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(0,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(60,88)
        self.number2 = self.number1 - randint(30,50)
        
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s %s $%s%s.<br><br>"%(self.name,self.item[0],self.amount1,self.item[1])
        self.problem = self.problem + "%s $%s %s.<br><br>"%(self.item[2],self.amount2,self.item[3])
        self.problem = self.problem + "%s"%(self.item[4])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.amount1,self.amount2,self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,decimal1,decimal2,number1,number2,amount1,amount2,item5,item6,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = self.GenerateSolution(answer,decimal1,decimal2,number1,number2,amount1,amount2)
        self.solution_text = self.solution_text + "<br><br>%s $%s%s</font>"%(item5,answer,item6)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        [Person.Auntyname] went to a <used items sale> and paid $98.75 for a <table> and a <microwave oven>.
        The <table> cost $25.45.
        Find the cost of the <microwave oven>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [['used items sale','table','microwave oven'],['yard sale','chair','chest of drawers'],['garage sale','carpet','fridge'],['second hand goods sale','lamp','fan'],['clearance sale','bag','dress'],['factory outlet','skirt','watch'],['garment factory outlet','sweater','coat'],['kitchen appliances sale','blender','food processor'],['department store sale','frying pan','wall clock'],['warehouse furniture sale','side table','TV table']]
        self.item = random.choice(self.items)
        
        self.decimal1digit1 = randint(0,9)
        self.decimal1digit2 = 0
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(50,88)
        self.number2 = randint(10,98-self.number1)
        
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.total = self.amount1 + self.amount2
        
        self.answer = self.amount1
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.total = Decimal(self.total).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)
        
        # Extracting the whole number and decimal parts out of 'total' to pass to the explanation 
        self.totalNumber1,self.totalDecimal1 = divmod(Decimal(self.total),1)
        self.totalDecimal1 = self.totalDecimal1 * 100
        
        self.problem = "%s went to a %s and paid $%s for a %s and a %s.<br><br>"%(self.name,self.item[0],self.total,self.item[1],self.item[2])
        self.problem = self.problem + "The %s cost $%s.<br><br>"%(self.item[1],self.amount2)
        self.problem = self.problem + "Find the cost of the %s."%(self.item[2])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,str(int(self.totalDecimal1)),self.decimal2,str(self.totalNumber1),self.number2,self.total,self.amount2,self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,decimal1,decimal2,number1,number2,amount1,amount2,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        self.solution_text = self.GenerateSolution(answer,decimal1,decimal2,number1,number2,amount1,amount2)
        self.solution_text = self.solution_text + "<br><br>The cost of the %s was $%s.</font>"%(item2,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        A <T-shirt> costs $12.45.
        A <bandana> costs $5.55 less.
        How much does the <bandana> cost?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.items = [['T-shirt','bandana'],['bouquet','vase'],['wooden easel','set of brushes'],['lamp','candle holder'],['mat','towel'],['book','pen'],['headset','pack of batteries'],['picture frame','paperweight'],['mirror','soap dish'],['pan','bowl'],['toy truck','bubble kit'],['soccer ball','cap'],['teddy bear','pen holder'],['kettle','mug'],['swimsuit','pair of armbands']]
        self.item = random.choice(self.items)
        
        self.decimal1digit1 = randint(0,9)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(11,20)
        self.number2 = randint(3,7)
        
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "A %s costs $%s.<br><br>"%(self.item[0],self.amount1)
        self.problem = self.problem + "A %s costs $%s less.<br><br>"%(self.item[1],self.amount2)
        self.problem = self.problem + "How much does the %s cost?"%(self.item[1])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.amount1,self.amount2,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,decimal1,decimal2,number1,number2,amount1,amount2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = self.GenerateSolution(answer,decimal1,decimal2,number1,number2,amount1,amount2)
        self.solution_text = self.solution_text + "<br><br>The %s costs $%s.</font>"%(item1,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        <A store had a promotion on toys.>
        [Person.Boyname] bought a <toy> for $9.90.
        The original price of the <toy> was $12.80.
        How much discount did he receive on the <toy>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['A store had a promotion on toys.','toy',randint(10,20)],['Coffee beans were on discount at a supermarket.','bag of coffee beans',randint(5,20)],['A toys store had water bottles on sale.','water bottle',randint(10,20)],['Tea kettles were on promotion at a department store.','tea kettle',randint(15,30)],['Bean bags were on sale at a furniture fair.','bean bag',randint(20,40)],['Shirts were on clearance at a store.','shirt',randint(20,40)],['An IT shop had a year-end promotion on several items.','computer mouse',randint(20,40)],['A furniture store was selling wall carpets on promotion.','wall carpet',randint(25,45)],['A year-end sale had school bags on clearance.','school bag',randint(30,50)],['A bed and linen store had a clearance sale.','bedsheet set',randint(40,60)]]
        self.item = random.choice(self.items)
        
        self.decimal1digit1 = randint(0,9)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = self.item[2]
        self.number2 = int(float(randint(6,8))*self.number1/10)
        
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s.<br><br>%s bought a %s for $%s.<br><br>"%(self.item[0],self.name,self.item[1],self.amount2)
        self.problem = self.problem + "The original price of the %s was $%s.<br><br>"%(self.item[1],self.amount1)
        self.problem = self.problem + "How much discount did he receive on the %s?"%(self.item[1])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.amount1,self.amount2,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,decimal1,decimal2,number1,number2,amount1,amount2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = self.GenerateSolution(answer,decimal1,decimal2,number1,number2,amount1,amount2)
        self.solution_text = self.solution_text + "<br><br>He received a discount of $%s on the %s.</font>"%(answer,item1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        <An adult ticket at a museum> costs $25.90.
        It costs $12.10 more than <a child ticket>.
        What is the cost of <a child ticket at the museum>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['An adult ticket at a museum','a child ticket','a child ticket at the museum'],["A child ticket at a kid's indoor playground","an adult ticket","an adult ticket at the indoor playground"],["A child entry ticket at a kid's water park","an adult entry ticket","an adult entry ticket at the water park"],["A regular meal at a restaurant","a kid's meal","a kid's meal at the restaurant"],['A regular train pass','a senior citizen train pass','a senior citizen train pass'],['A tram ticket for an adult at the zoo','a tram ticket for a child','a tram ticket for a child at the zoo'],['A regular entry pass at an amusement park','a child entry pass','a child entry pass at the amusement park'],['A 3D movie ticket','a regular movie ticket','a regular movie ticket'],['A dance show pass at an arts festival','a music show pass','a music show pass at the arts festival'],['A coupon booklet for rides at a carnival','a coupon booklet for food','a coupon booklet for food at the carnival']]
        self.item = random.choice(self.items)
        
        self.decimal1digit1 = randint(0,9)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(20,30)
        self.number2 = int(float(randint(5,7))*self.number1/10)
        
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s costs $%s.<br><br>"%(self.item[0],self.amount1)
        self.problem = self.problem + "It costs $%s more than %s.<br><br>"%(self.amount2,self.item[1])
        self.problem = self.problem + "What is the cost of %s?"%(self.item[2])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.amount1,self.amount2,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,decimal1,decimal2,number1,number2,amount1,amount2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = self.GenerateSolution(answer,decimal1,decimal2,number1,number2,amount1,amount2)
        self.solution_text = self.solution_text + "<br><br>The cost of %s is $%s.</font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        [Person.Boyname1] and [Person.Boyname2] <went shopping at a mall>.
        [Person.Boyname1] bought a <hat> for $43.10.
        [Person.Boyname2] bought a different <hat> that was $12.90 cheaper.
        How much did [Person.Boyname2] pay for his <hat>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.BoyName,2)
        
        self.items = [['went shopping at a mall','hat',randint(30,50)],['went to a store','music player',randint(70,90)],['went to a toys store','pack of play-dough',randint(15,25)],['went to a sports store','foosball table',randint(80,99)],['went to a sports store','carrom board',randint(70,90)],['went to a shoes store','pair of boots',randint(60,80)],['went to a mall','sweatshirt',randint(50,70)],['went to a book fest','book',randint(20,40)],['went to a furniture store','book shelf',randint(80,99)],['went to a painting exhibition','painting',randint(80,99)]]
        self.item = random.choice(self.items)
        
        self.decimal1digit1 = randint(0,9)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = self.item[2]
        self.number2 = int(float(randint(2,4))*self.number1/10)
        
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s and %s %s.<br><br>"%(self.names[0],self.names[1],self.item[0])
        self.problem = self.problem + "%s bought a %s for $%s.<br><br>"%(self.names[0],self.item[1],self.amount1)
        self.problem = self.problem + "%s bought a different %s that was $%s cheaper.<br><br>"%(self.names[1],self.item[1],self.amount2)
        self.problem = self.problem + "How much did %s pay for his %s?"%(self.names[1],self.item[1])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.decimal1,self.decimal2,self.number1,self.number2,self.amount1,self.amount2,self.item[1],self.names[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,decimal1,decimal2,number1,number2,amount1,amount2,item1,name,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = self.GenerateSolution(answer,decimal1,decimal2,number1,number2,amount1,amount2)        
        self.solution_text = self.solution_text + "<br><br>%s paid $%s for his %s.</font>"%(name,answer,item1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:
        [Person.Unclename] bought <some groceries> for $35.25.
        He gave the cashier $50.
        How much change did he receive?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = ['some groceries','a shirt','some kites','a wallet','a pair of pants','a belt','a watch','some toys','some petrol','a pair of shorts','a tie','a pair of sunglasses']
        self.item = random.choice(self.items)
        
        self.decimal1digit1 = randint(0,9)
        self.decimal1digit2 = 0
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        
        self.number1 = randint(20,50)
        
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = (self.number1/10+1)*10
                
        self.answer = self.amount2 - self.amount1
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s bought %s for $%s.<br><br>"%(self.name,self.item,self.amount1)
        self.problem = self.problem + "He gave the cashier $%d.<br><br>"%(self.amount2)
        self.problem = self.problem + "How much change did he receive?"
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,'00',self.decimal1,self.amount2,self.number1,self.amount2,self.amount1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,decimal1,decimal2,number1,number2,amount1,amount2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = self.GenerateSolution(answer,decimal1,decimal2,number1,number2,amount1,amount2)
        self.solution_text = self.solution_text + "<br><br>He received $%s in change.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:
        [Person.Boyname] has $49.20.
        He wants to buy a <cricket set> that costs $98.90.
        How much more money does he need to buy the <cricket set>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['cricket set','cricket set'],['pair of roller blades','roller blades'],['tennis set','tennis set'],['bicycle','bicycle'],['pair of running shoes','shoes'],['baseball glove','baseball glove'],['chess set','chess set'],['badminton set','badminton set'],['basketball set','basketball set'],['bowling set','bowling set']]
        self.item = random.choice(self.items)
        
        self.decimal1digit1 = randint(0,9)
        self.decimal1digit2 = 0
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(1,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(10,50)
        self.number2 = randint(70,98)
        
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount2 - self.amount1
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "%s has $%s.<br><br>"%(self.name,self.amount1)
        self.problem = self.problem + "He wants to buy a %s that costs $%s.<br><br>"%(self.item[0],self.amount2)
        self.problem = self.problem + "How much more money does he need to buy the %s?"%(self.item[1])
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.decimal2,self.decimal1,self.number2,self.number1,self.amount2,self.amount1,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,decimal1,decimal2,number1,number2,amount1,amount2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = self.GenerateSolution(answer,decimal1,decimal2,number1,number2,amount1,amount2)
        self.solution_text = self.solution_text + "<br><br>He needs $%s more to buy the %s.</font>"%(answer,item1)

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
        Find the difference $%s and $%s.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1"
        self.CheckAnswerType = 1

        self.decimal1digit1 = randint(5,9)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(0,self.decimal1digit1)
        self.decimal2digit2 = 0
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1digit1 = randint(5,9)
        self.number1digit2 = randint(5,9)
        self.number2digit1 = randint(0,self.number1digit1-1)
        self.number2digit2 = randint(0,self.number1digit2)
        
        self.number1 = str(self.number1digit1)+str(self.number1digit2)
        self.number2 = str(self.number2digit1)+str(self.number2digit2)
        
        self.amount1 = Decimal(int(self.number1)*100+int(self.decimal1))/100
        self.amount2 = Decimal(int(self.number2)*100+int(self.decimal2))/100
                
        self.answer = self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "Find the difference of $%s and $%s."%(self.amount1,self.amount2)
                   
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
        Subtract.
        $25.20 - $18.65 = ________'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ2"
        self.CheckAnswerType = 1

        self.decimal1digit1 = randint(0,9)
        self.decimal1digit2 = 5
        self.decimal1 = str(self.decimal1digit1)+str(self.decimal1digit2)
        self.decimal2digit1 = randint(0,9)
        self.decimal2digit2 = random.choice([0,5])
        self.decimal2 = str(self.decimal2digit1)+str(self.decimal2digit2)
        
        self.number1 = randint(40,90)
        self.number2 = randint(20,self.number1-5)
        
        self.amount1 = Decimal(self.number1*100+int(self.decimal1))/100
        self.amount2 = Decimal(self.number2*100+int(self.decimal2))/100
                
        self.answer = self.amount1 - self.amount2
        
        TWOPLACES = Decimal(10) ** -2
        
        self.amount1 = Decimal(self.amount1).quantize(TWOPLACES)
        self.amount2 = Decimal(self.amount2).quantize(TWOPLACES)
        self.answer = Decimal(self.answer).quantize(TWOPLACES)

        self.problem = "Subtract.<br><br>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; _____."%(self.amount1,self.amount2)
                   
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
            
    def GenerateSolution(self,answer,decimal1,decimal2,number1,number2,amount1,amount2):
        tenths1,hundredths1 = divmod(int(decimal1),10)
        tenths2,hundredths2 = divmod(int(decimal2),10)
        tens1,ones1 = divmod(int(number1),10)
        tens2,ones2 = divmod(int(number2),10)

        borrowFromOnes = 0
        borrowFromTens = 0
        
        diffHundredths = hundredths1-hundredths2

        if tenths1 >= tenths2:
            diffTenths = tenths1-tenths2
        else:
            diffTenths = 10+tenths1-tenths2
            borrowFromOnes = 1
        
        if borrowFromOnes == 0:
            if ones1 >= ones2:
                diffOnes = ones1-ones2
            else:
                diffOnes = 10+ones1-ones2
                borrowFromTens = 1
        else:
            if (ones1-1) >= ones2:
                diffOnes = ones1-1-ones2
            else:
                diffOnes = 10+ones1-1-ones2
                borrowFromTens = 1
        
        if borrowFromTens == 0:
            diffTens = tens1-tens2
        else:
            diffTens = tens1-1-tens2
        
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<br>$%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; ?<br><br>"%(amount1,amount2)
        
        self.solution_text = self.solution_text + "First, we subtract the cents.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable' border=0>"

        if tens1 == 0: # 3-digit numbers
            if borrowFromOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup><font style='font-size:11px'>%d</font></sup><del>%d</del></td><td>.</td><td><sup><font style='font-size:11px'>1</font></sup>%d</td><td>%d</td></tr>"%(ones1-1,ones1,tenths1,hundredths1)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%d</td><td>.</td><td>%d</td><td>%d</td></tr>"%(ones1,tenths1,hundredths1)
            self.solution_text = self.solution_text + "<tr><td>&minus;</td><td>$</td><td>%d</td><td>.</td><td>%d</td><td>%d </td></tr>"%(ones2,tenths2,hundredths2)
            self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:center;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(diffTenths,diffHundredths)
            self.solution_text = self.solution_text + "</table><br><br>"
        else:# 4-digit numbers
            if borrowFromTens == 1:
                if borrowFromOnes==1:
                    if ones1==0:
                        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup><font style='font-size:11px'>%d</font></sup><del>%d</del></td><td><sup><font style='font-size:11px'><sup><font style='font-size:11px'>9</font></sup><del>1</del></font></sup><del>%d</del></td><td>.</td><td><sup><font style='font-size:11px'>1</font></sup>%d</td><td>%d</td></tr>"%(tens1-1,tens1,ones1,tenths1,hundredths1)
                    else:
                        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%d</td><td><sup><font style='font-size:11px'>%d</font></sup><del>%d</del></td><td>.</td><td><sup><font style='font-size:11px'>1</font></sup>%d</td><td>%d</td></tr>"%(tens1,ones1-1,ones1,tenths1,hundredths1)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%d</td><td>%d</td><td>.</td><td>%d</td><td>%d</td></tr>"%(tens1,ones1,tenths1,hundredths1)
            else:
                if borrowFromOnes==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%d</td><td><sup><font style='font-size:11px'>%d</font></sup><del>%d</del></td><td>.</td><td><sup><font style='font-size:11px'>1</font></sup>%d</td><td>%d</td></tr>"%(tens1,ones1-1,ones1,tenths1,hundredths1)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%d</td><td>%d</td><td>.</td><td>%d</td><td>%d</td></tr>"%(tens1,ones1,tenths1,hundredths1)                
            if tens2 == 0:
                self.solution_text = self.solution_text + "<tr><td>&minus;</td><td>$</td><td>&nbsp;</td><td>%d</td><td>.</td><td>%d</td><td>%d </td></tr>"%(ones2,tenths2,hundredths2)
            else:
                self.solution_text = self.solution_text + "<tr><td>&minus;</td><td>$</td><td>%d</td><td>%d</td><td>.</td><td>%d</td><td>%d </td></tr>"%(tens2,ones2,tenths2,hundredths2)
            self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:center;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d </td></tr>"%(diffTenths,diffHundredths)
            self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "Next, we subtract the dollars.<br>"
        self.solution_text = self.solution_text + "<table class='ExplanationMoneyTable' border=0>"
        if tens1 == 0: # 3-digit numbers
            if borrowFromOnes==1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup><font style='font-size:11px'>%d</font></sup><del>%d</del></td><td>.</td><td><sup><font style='font-size:11px'>1</font></sup>%d</td><td>%d</td></tr>"%(ones1-1,ones1,tenths1,hundredths1)
            else:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%d</td><td>.</td><td>%d</td><td>%d</td></tr>"%(ones1,tenths1,hundredths1)
            self.solution_text = self.solution_text + "<tr><td>&minus;</td><td>$</td><td>%d</td><td>.</td><td>%d</td><td>%d </td></tr>"%(ones2,tenths2,hundredths2)
            self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:center;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%d</td><td>.</td><td>%d</td><td>%d </td></tr>"%(diffOnes,diffTenths,diffHundredths)
            self.solution_text = self.solution_text + "</table><br><br>"
        else: # 4-digit numbers
            if borrowFromTens == 1:
                if borrowFromOnes==1:
                    if ones1==0:
                        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup><font style='font-size:11px'>%d</font></sup><del>%d</del></td><td><sup><font style='font-size:11px'><sup><font style='font-size:11px'>9</font></sup><del>1</del></font></sup><del>%d</del></td><td>.</td><td><sup><font style='font-size:11px'>1</font></sup>%d</td><td>%d</td></tr>"%(tens1-1,tens1,ones1,tenths1,hundredths1)
                    else:
                        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup><font style='font-size:11px'>%d</font></sup><del>%d</del></td><td><sup><font style='font-size:11px'><sup><font style='font-size:11px'>1</font></sup>%d</font></sup><del>%d</del></td><td>.</td><td><sup><font style='font-size:11px'>1</font></sup>%d</td><td>%d</td></tr>"%(tens1-1,tens1,ones1-1,ones1,tenths1,hundredths1)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td><sup><font style='font-size:11px'>%d</font></sup><del>%d</del></td><td><sup><font style='font-size:11px'>1</font></sup>%d</td><td>.</td><td>%d</td><td>%d</td></tr>"%(tens1-1,tens1,ones1,tenths1,hundredths1)                
            else:
                if borrowFromOnes==1:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%d</td><td><sup><font style='font-size:11px'>%d</font></sup><del>%d</del></td><td>.</td><td><sup><font style='font-size:11px'>1</font></sup>%d</td><td>%d</td></tr>"%(tens1,ones1-1,ones1,tenths1,hundredths1)
                else:
                    self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%d</td><td>%d</td><td>.</td><td>%d</td><td>%d</td></tr>"%(tens1,ones1,tenths1,hundredths1)                
            if tens2 == 0:
                self.solution_text = self.solution_text + "<tr><td>&minus;</td><td>$</td><td>&nbsp;</td><td>%d</td><td>.</td><td>%d</td><td>%d </td></tr>"%(ones2,tenths2,hundredths2)
            else:
                self.solution_text = self.solution_text + "<tr><td>&minus;</td><td>$</td><td>%d</td><td>%d</td><td>.</td><td>%d</td><td>%d </td></tr>"%(tens2,ones2,tenths2,hundredths2)
            self.solution_text = self.solution_text + "<tr><td colspan=7 style='text-align:center;padding:0px 0px 0px 10px'><img src='/images/explanation/line.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$</td><td>%d</td><td>%d</td><td>.</td><td>%d</td><td>%d </td></tr>"%(diffTens,diffOnes,diffTenths,diffHundredths)
            self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "So, &nbsp; $%s &nbsp;&minus;&nbsp; $%s &nbsp;=&nbsp; $%s"%(amount1,amount2,answer)
        
        return self.solution_text