'''
Created on May 14, 2013
Module: P3LMWordProblems
Generates the word problems on Length Mass Volume for Primary 3

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

class P3LMWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemType4",],5:["ProblemType5",],
                            6:["ProblemType6",],7:["ProblemType7",],8:["ProblemType8",],9:["ProblemType9",],10:["ProblemType10",],
                            11:["ProblemType11",],12:["ProblemType12",],13:["ProblemType13",],14:["ProblemType14",],15:["ProblemType15",],
                            16:["ProblemType16",],17:["ProblemType17",],18:["ProblemType18",],19:["ProblemType19",],20:["ProblemType20",],
                            21:["ProblemType21",],22:["ProblemType22",],23:["ProblemType23",],24:["ProblemType24",],25:["ProblemType25",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1()],2:[self.GenerateProblemType2()],3:[self.GenerateProblemType3()],
                                    4:[self.GenerateProblemType4()],5:[self.GenerateProblemType5()],6:[self.GenerateProblemType6()],
                                    7:[self.GenerateProblemType7()],8:[self.GenerateProblemType8()],
                                    9:[self.GenerateProblemType9()],10:[self.GenerateProblemType10()],
                                    11:[self.GenerateProblemType11()],12:[self.GenerateProblemType12()],13:[self.GenerateProblemType13()],
                                    14:[self.GenerateProblemType14()],15:[self.GenerateProblemType15()],16:[self.GenerateProblemType16()],
                                    17:[self.GenerateProblemType17()],18:[self.GenerateProblemType18()],
                                    19:[self.GenerateProblemType19()],20:[self.GenerateProblemType20()],
                                    21:[self.GenerateProblemType21()],22:[self.GenerateProblemType22()],23:[self.GenerateProblemType23()],
                                    24:[self.GenerateProblemType24()],25:[self.GenerateProblemType25()],
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
        #return self.GenerateProblemType4()
        
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
                            "ProblemType24":self.GenerateProblemType24(),"ProblemType25":self.GenerateProblemType25(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        [Person.Name] has 300 ml of <milk in a cup>.
        <He/She> also has 1300 ml of <milk in a bottle>.
        Find the total amount of <milk> <he/she> has.
        Give your answer in litres and milllilitres.
        (Write your answer as in the example below.
        Example: 5 l 67 ml)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice([[random.choice(PersonName.GirlName),"she","She"],[random.choice(PersonName.BoyName),"he","He"]])
        
        self.items = [['milk in a cup','milk in a bottle','milk',random.randrange(50,300,10),random.randrange(1000,3000,100)],
                      ['water in a glass','water in a jar','water',random.randrange(50,300,10),random.randrange(1000,5000,100)],
                      ['guava juice in a glass','guava juice in a jug','guava juice',random.randrange(50,300,10),random.randrange(1000,5000,100)],
                      ['soup in a bowl','soup in a pot','soup',random.randrange(100,300,10),random.randrange(500,2000,100)],
                      ['light soy sauce','dark soy sauce','soy sauce',random.randrange(500,1000,10),random.randrange(100,1000,100)],
                      ['lemonade in a bottle','lemonade in a dispenser','lemonade',random.randrange(1000,2000,100),random.randrange(5000,7000,100)],
                      ['apple cider in a bottle','apple cider in a can','apple cider',random.randrange(1000,2000,100),random.randrange(1000,2000,100)],
                      ['olive oil in a bottle','olive oil in a canister','olive oil',random.randrange(500,1000,100),random.randrange(1000,3000,100)],
                      ['purple paint','orange paint','paint',random.randrange(100,5000,100),random.randrange(500,4900,100)],
                      ['red ink','blue ink','ink',random.randrange(50,2000,10),random.randrange(500,2000,100)]]
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[3]
        self.number2 = self.item[4]
        
        self.problem = "%s has %d ml of %s.<br>"%(self.name[0],self.number1,self.item[0])
        self.problem = self.problem + "%s also has %d ml of %s.<br>"%(self.name[1].capitalize(),self.number2,self.item[1])
        self.problem = self.problem + "Find the total amount of %s %s has in litres and milllilitres.<br><br>"%(self.item[2],self.name[1])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 <font class='litreFont'>l</font>&nbsp; 293 <font class='litreFont'>ml</font>)"
        
        self.number = self.number1+self.number2
                   
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d l %d ml"%(div,mod)
        self.answer1 = "%d <font class='litreFont'>l</font> &nbsp;%d <font class='litreFont'>ml</font>"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.answer1,self.number1,self.number2,self.name[2],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,answer1,number1,number2,name2,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer1),unit)

        if number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        elif number1 > number2:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>%d <font class='litreFont'>ml</font></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table>"

        number = number1+number2
        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 <font class='litreFont'>ml</font> = 1 <font class='litreFont'>l</font><br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>ml</font> = %d <font class='litreFont'>l</font></font></div></td>"%(div*1000,div)
        else:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 <font class='litreFont'>ml</font> = 1 <font class='litreFont'>l</font></font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td><td>=</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(number1,number2,number)
        if mod>0:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(div*1000,mod)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>l</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer1)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>%s has &nbsp;%s &nbsp;of %s.</font>"%(name2,answer1,item2)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        [Person.Girlname] <has> a <rope> 75 cm long.
        She <has> another <rope> 255 cm long.
        What is the total length of the two <ropes>?
        Give your answer in metres and centimetres.
        (Write your answer as in the example below.
        Example: 5 m 67 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['has','rope','ropes'],['cuts','string','strings'],['has','kitestring','kitestrings'],['weaves','lace','laces'],['has','ribbon','ribbons'],['has','wire','wires'],['has','tape','tapes'],['cuts','piece of fabric','pieces of fabric'],['draws','line','lines'],['buys','beaded string','beaded strings']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(50,499)
        self.number2 = randint(51,500)
        
        self.problem = "%s %s a %s %d cm long.<br>"%(self.name,self.item[0],self.item[1],self.number1)
        self.problem = self.problem + "She %s another %s %d cm long.<br>"%(self.item[0],self.item[1],self.number2)
        self.problem = self.problem + "What is the total length of the two %s in metres and centimetres?<br><br>"%(self.item[2])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 23 cm)"
                
        self.number = self.number1+self.number2
                   
        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,number1,number2,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        elif number1 > number2:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>%d cm</td><td>%d cm</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table>"

        number = number1+number2
        div,mod = divmod(number,100)
        if div > 1:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d cm = %d m</font></div></td>"%(div*100,div)
        else:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d cm &nbsp;+&nbsp; %d cm</td><td>=</td><td>%d cm</td></tr>"%(number1,number2,number)
        if mod>0:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(div*100,mod)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The total length of the two %s is %s.</font>"%(item2,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        <A dictionary> has a mass of 1200 g.
        <A novel> has a mass of 500 g.
        What is their total mass?
        Give your answer in kilograms and grams.
        (Write your answer as in the example below.
        Example: 5 kg 678 g)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['A dictionary','A diary',randint(100,2000),randint(100,2000)],
                      ['A tub of icecream','A bag of nuts',randint(200,1000),randint(500,2000)],
                      ['A box','A carton',randint(500,5000),randint(500,4999)],['A brick','A cinder block',randint(200,1000),randint(2000,5000)],['A bunch of lettuce','A bag of potatoes',randint(200,500),randint(500,2000)],['A fish','A turkey',randint(200,3000),randint(3000,6000)],['A ride-on toy car','A wall clock',randint(1000,3000),randint(500,2000)],['A suitcase','A laptop',randint(1000,6500),randint(1000,3000)],['A baby','Another baby',randint(2500,5000),randint(3000,4999)],['A TV set','A printer',randint(2500,7000),randint(1000,2999)]]
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[2]
        self.number2 = self.item[3]
        
        self.problem = "%s has a mass of %d g.<br>"%(self.item[0],self.number1)
        self.problem = self.problem + "%s has a mass of %d g.<br>"%(self.item[1],self.number2)
        self.problem = self.problem + "What is their total mass in kilograms and grams?<br><br>"
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 kg 293 g)"
                
        self.number = self.number1+self.number2
                   
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d kg %d g"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        elif number1 > number2:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>%d g</td><td>%d g</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table>"

        number = number1+number2
        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d g = %d kg</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d g &nbsp;+&nbsp; %d g</td><td>=</td><td>%d g</td></tr>"%(number1,number2,number)
        if mod>0:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g &nbsp;+&nbsp; %d g</td></tr>"%(div*1000,mod)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d kg &nbsp;+&nbsp; %d g</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>Their total mass is %s.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        [Person.Boyname] <cycles> 1200 m< from his house to his friend's house>.
        Then he <cycles> 3250 m< to the library>.
        What is the total distance he <cycles> in kilometres and metres?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                      ['cycles'," from his house to his friend's house",'cycles',' to the library','cycles',random.randrange(1000,2000,100),random.randrange(1000,2000,100)],
                      ['walks',' to the bus stop','rides',' on the bus to his school','travels',random.randrange(200,500,50),random.randrange(2000,5000,100)],
                      ['jogs',' to the park','jogs',' in the park','jogs',random.randrange(500,1000,100),random.randrange(600,1200,100)],
                      ['bikes',' to the playground','bikes another',' to visit his grandmother','bikes',random.randrange(1000,2000,100),random.randrange(1000,2000,100)],
                      ['runs',' in the gym','swims',' in the swimming pool','covers',random.randrange(1000,3000,100),random.randrange(200,500,50)],
                      ['rides',' on a train','walks',' to a coffee shop','travels',random.randrange(5000,8000,100),random.randrange(200,500,50)],
                      ['travels',' to meet his uncle','travels',' to meet his teacher','travels',random.randrange(1000,3000,100),random.randrange(1000,3000,100)],
                      ['cycles',' to a sports complex','runs',' on a track','covers',random.randrange(2000,3000,100),random.randrange(300,900,50)],
                      ['walks',' to a cafe','walks',' to his home','walks',random.randrange(200,500,50),random.randrange(500,700,50)]
                      ]        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[5]
        self.number2 = self.item[6]
        
        self.problem = "%s %s %d m%s.<br>"%(self.name,self.item[0],self.number1,self.item[1])
        self.problem = self.problem + "Then he %s %d m%s.<br>"%(self.item[2],self.number2,self.item[3])
        self.problem = self.problem + "What is the total distance he %s in kilometres and metres?<br><br>"%(self.item[4])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 km 293 m)"
                
        self.number = self.number1+self.number2
                   
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d km %d m"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":5,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,number1,number2,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        elif number1 > number2:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>%d m</td><td>%d m</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;tezt-align:right;'><img src='/images/explanation/P3_model_distance_arrow_%s.png' /></td><td style='padding-bottom:3px;text-align:left;'><img src='/images/explanation/P3_model_distance_arrow_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right;'><img src='/images/explanation/P3_model_distance_%s.png' /></td><td style='text-align:left;white-space:nowrap'><img src='/images/explanation/P3_model_distance_%s.png' /><img src='/images/explanation/P3_model_distance_end.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3><img src='/images/explanation/P3_model_distance_arrow_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3>?</td></tr>"
        self.solution_text = self.solution_text + "</table>"

        number = number1+number2
        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = self.solution_text + "<br><br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d km</font></div>"%(div*1000,div)
        elif div==1:
            self.solution_text = self.solution_text + "<br><br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km</font></div>"
        else:   #div<1 i.e. 0 km
            self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m &nbsp;+&nbsp; %d m</td><td>=</td><td>%d m</td></tr>"%(number1,number2,number)
        if mod>0:
            if div>=1:
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(div*1000,mod)
                self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>He %s a total distance of %s.</font>"%(item4,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        [Person.Name]'s house is 36 km from <the beach>.
        It is 4 times as far from <the airport> as <the beach>.
        Find the distance between [Person.Name]'s house and <the airport>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.PersonName)
        
        self.items = [
                      ['the beach','the airport',randint(10,20),randint(3,6)],
                      ['City A','City B',randint(20,100),randint(3,9)],
                      ['the university','the zoo',randint(5,15),randint(3,6)],
                      ['the forest','the mountains',randint(15,30),randint(3,9)],
                      ['the river','the village',randint(15,30),randint(3,9)],
                      ['the wildlife sanctuary','the bird sanctuary',randint(10,20),randint(3,6)],
                      ['the theme park','the water park',randint(5,20),randint(3,6)],
                      ['the museum','the water park',randint(5,20),randint(3,6)],
                      ['the ski resort','the water park',randint(5,20),randint(3,6)],
                      ['the cricket stadium','the water park',randint(5,20),randint(3,6)]
                      ]
        self.item = random.choice(self.items)
        
        self.number1 = self.item[2]
        self.number2 = self.item[3]

        self.problem = "%s's house is %d km from %s.<br>"%(self.name,self.number1,self.item[0])
        self.problem = self.problem + "It is %d times as far from %s as %s.<br>"%(self.number2,self.item[1],self.item[0])
        self.problem = self.problem + "Find the distance between %s's house and %s."%(self.name,self.item[1])
                
        self.answer = self.number1*self.number2
                          
        self.unit = "km"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.name,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,number1,number2,name,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>%d km</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr>"
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:10px;border:white solid 1px;width:50px'></td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td colspan=%d>?</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br>"
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d km &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d km"%(number1,number2,answer)
        self.solution_text = self.solution_text + "<br><br>The distance between %s's house and %s is %d km.</font>"%(name,item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:The mass of a <sack of wheat> is 38 kg.
        The mass of a <sack of corn> is 24 kg.
        How much heavier is the <sack of wheat> than the <sack of corn>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.PersonName)
        
        self.items = [
                      ['sack of wheat','sack of corn',randint(10,30),randint(5,20),'wheat','corn'],
                      ['sack of sugar','sack of oats',randint(10,30),randint(5,20),'sugar','oats'],
                      ['box of notebooks','box of tiles',randint(10,30),randint(5,20),'notebooks','tiles'],
                      ['box of watermelons','box of mangoes',randint(10,30),randint(5,20),'watermelons','mangoes'],
                      ['carton of books','carton of photoframes',randint(20,40),randint(5,20),'books','photoframes'],
                      ['carton of oil paints','carton of acrylic colours',randint(10,30),randint(5,20),'oil','acrylic'],
                      ['crate of milk bottles','crate of soda cans',randint(10,30),randint(5,20),'milk','soda'],
                      ['crate of tomatoes','crate of bananas',randint(10,30),randint(5,20),'tomatoes','bananas'],
                      ['bag of pebbles','bag of marbles',randint(10,30),randint(5,20),'pebbles','marbles'],
                      ['boy','girl',randint(10,30),randint(5,20),'boy','girl']
                      ]
        self.item = random.choice(self.items)
        
        self.number1 = self.item[2]
        self.number2 = self.item[3]
        
        self.problem = "The mass of a %s is %d kg.<br>"%(self.item[0],self.number1+self.number2)
        self.problem = self.problem + "The mass of a %s is %d kg.<br>"%(self.item[1],self.number1)
        self.problem = self.problem + "How much heavier is the %s than the %s?"%(self.item[0],self.item[1])
                
        self.answer = self.number2
                          
        self.unit = "kg"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[1],self.item[4],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,number1,number2,item0,item1,item4,item5,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1==number2:
            firstBrace = 'medium2'
            secondBrace = 'medium'
            thirdBrace = 'medium'
        elif number1>number2:
            firstBrace = 'large'
            secondBrace = 'medium'
            thirdBrace = 'small'
        else:
            firstBrace = 'large'
            secondBrace = 'small'
            thirdBrace = 'medium'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d kg</td></tr>"%(number1+number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'></td></tr>"%(item4,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td>&nbsp;</td></tr>"%(item5,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(secondBrace,thirdBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d kg</td><td>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d kg &nbsp;&minus;&nbsp; %d kg &nbsp;=&nbsp; %d kg"%(number1+number2,number1,answer)
        self.solution_text = self.solution_text + "<br><br>The %s is %d kg heavier than the %s.</font>"%(item0,answer,item1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text

        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        [Person.Name] cut a <wire> into 4 equal pieces of 178 cm each.
        What was the length of the original <wire>?
        Give your answer in metres and centimetres.
        (Write your answer as in the example below.
        Example: 5 m 67 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.PersonName)
        
        self.items = [
                      ['wire',randint(101,198)],
                      ['ribbon',randint(101,198)],
                      ['pipe',randint(101,198)],
                      ['string',randint(101,198)],
                      ['pole',randint(101,198)],
                      ['cable',randint(101,198)],
                      ['wooden log',randint(101,198)],
                      ['rope',randint(101,198)],
                      ['fishing line',randint(101,198)],
                      ['sticky tape',randint(101,198)]
                      ]
                
        self.item = random.choice(self.items)
        
        self.number1 = self.item[1]
        self.number2 = randint(3,5)
        
        self.problem = "%s cut a %s into %d equal pieces of %d cm each.<br>"%(self.name,self.item[0],self.number2,self.number1)
        self.problem = self.problem + "What was the length of the original %s in metres and centimetres?<br><br>"%(self.item[0])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 23 cm)"
                
        self.number = self.number1*self.number2
                   
        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,number1,number2,item0,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;&nbsp;&nbsp;</td><td>%d cm</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td>"
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:20px;border:white solid 1px;width:50px'></td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table>"

        number = number1*number2
        div,mod = divmod(number,100)
        if div > 1:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d cm = %d m</font></div></td>"%(div*100,div)
        else:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d cm &nbsp;&times;&nbsp; %d</td><td>=</td><td>%d cm</td></tr>"%(number1,number2,number)
        if mod>0:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(div*100,mod)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The length of the original %s was %s.</font>"%(item0,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:[Person.Unclename] has 625 g of <seeds>.
            He <packs> the <seeds> equally into 5 <bags>.
            Find the mass of <seeds> in each <bag>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [
                      ['seeds','packs','bags','bag',random.randrange(50,200,5)],
                      ['corn chips','packs','bags','bag',random.randrange(100,400,5)],
                      ['corn kernels','packs','packets','packet',random.randrange(100,400,5)],
                      ['rice crackers','puts','packets','packet',random.randrange(50,200,5)],
                      ['beads','puts','packets','packet',random.randrange(50,200,5)],
                      ['buttons','packs','packets','packet',random.randrange(50,200,5)],
                      ['plant food','packs','packets','packet',random.randrange(50,200,5)],
                      ['soil','puts','bags','bag',random.randrange(50,200,5)],
                      ['fish food','puts','packets','packet',random.randrange(50,200,5)],
                      ['grains','puts','bags','bag',random.randrange(50,200,5)]
                      ]        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[4]
        self.number2 = randint(3,9)
        
        self.problem = "%s has %d g of %s.<br>"%(self.name,self.number1*self.number2,self.item[0])
        self.problem = self.problem + "He %s the %s equally into %d %s.<br>"%(self.item[1],self.item[0],self.number2,self.item[2])
        self.problem = self.problem + "Find the mass of %s in each %s."%(self.item[0],self.item[3])
                
        self.answer = self.number1
                          
        self.unit = "g"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,number1,number2,item0,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d>%d g</td></tr>"%(number2,number1*number2)
        self.solution_text = self.solution_text + "<tr><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr>"
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:20px;border:white solid 1px;width:50px'></td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d g &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d g"%(number1*number2,number2,answer)
        self.solution_text = self.solution_text + "<br><br>The mass of %s in each %s is %d g.</font>"%(item0,item3,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
       
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:[Person.Unclename] had 8 <pails> each containing 13 l of <water>.
        What is the total volume of <water> he had?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [
                      ['pails','water',randint(10,20)],
                      ['pails','paint',randint(10,20)],
                      ['fish tanks','water',randint(30,100)],
                      ['tanks','fruit juice',randint(20,100)],
                      ['containers','sunflower oil',randint(20,50)],
                      ['containers','milk',randint(20,50)],
                      ['barrels','diesel',randint(20,50)],
                      ['barrels','honey',randint(20,50)],
                      ['cans','gasoline',randint(20,50)],
                      ['cans','petrol',randint(20,50)]
                      ]
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[2]
        self.number2 = randint(3,9)

        self.problem = "%s had %d %s each containing %d <font class='litreFont'>l</font>&nbsp; of %s.<br>"%(self.name,self.number2,self.item[0],self.number1,self.item[1])
        self.problem = self.problem + "What is the total volume of %s he had?"%(self.item[1])
                
        self.answer = self.number1*self.number2
                          
        self.unit = "<font class='litreFont'>l</font>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,number1,number2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>l</font></td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr>"
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:20px;border:white solid 1px;width:50px'></td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td colspan=%d>?</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d <font class='litreFont'>l</font> &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d <font class='litreFont'>l</font>"%(number1,number2,answer)
        self.solution_text = self.solution_text + "<br><br>He had a total of %d <font class='litreFont'>l</font>&nbsp; of %s.</font>"%(answer,item1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:[Person.Girlname] has <a plastic wrap> of length 135 cm.
            She cuts it into 5 pieces.
            What is the length of each piece?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                      ['a plastic wrap',randint(30,100)],
                      ['an aluminium foil',randint(30,100)],
                      ['a butter paper',randint(30,100)],
                      ['a gift wrapper',randint(30,100)],
                      ['a printed cloth',randint(30,100)],
                      ['a yellow thread',randint(30,100)],
                      ['a thick string',randint(30,100)],
                      ['a beaded lace',randint(30,100)],
                      ['a jute rope',randint(30,100)],
                      ['a blue plastic rope',randint(30,100)]
                      ]
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[1]
        self.number2 = randint(4,9)

        self.problem = "%s has %s of length %d cm.<br>"%(self.name,self.item[0],self.number1*self.number2)
        self.problem = self.problem + "She cuts it into %d pieces.<br>"%(self.number2)
        self.problem = self.problem + "What is the length of each piece?"
                
        self.answer = self.number1
                          
        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d>%d cm</td></tr>"%(number2,number1*number2)
        self.solution_text = self.solution_text + "<tr><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr>"
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:20px;border:white solid 1px;width:50px'></td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d cm &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d cm"%(number1*number2,number2,answer)
        self.solution_text = self.solution_text + "<br><br>The length of each piece is %d cm.</font>"%(answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:The total mass of 3 identical <magazines> is 789 g.
            What is the mass of each <magazine>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                      ['magazines','magazine',randint(60,180)],
                      ['wooden blocks','wooden block',randint(60,180)],
                      ['logs of wood','log of wood',randint(60,180)],
                      ['paperweights','paperweight',randint(60,180)],
                      ['granite tiles','granite tile',randint(60,180)],
                      ['polished stones','polished stone',randint(60,180)],
                      ['blocks of butter','block of butter',randint(60,180)],
                      ['pen stands','pen stand',randint(60,180)],
                      ['bottles of glue','bottle of glue',randint(60,180)],
                      ['tape dispensers','tape dispenser',randint(60,180)]
                      ]
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[2]
        self.number2 = randint(3,5)

        self.problem = "The total mass of %d identical %s is %d g.<br>"%(self.number2,self.item[0],self.number1*self.number2)
        self.problem = self.problem + "What is the mass of each %s?"%(self.item[1])
                
        self.answer = self.number1
                          
        self.unit = "g"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.number1,self.number2,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,number1,number2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d>%d g</td></tr>"%(number2,number1*number2)
        self.solution_text = self.solution_text + "<tr><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr>"
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:20px;border:white solid 1px;width:50px'></td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d g &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d g"%(number1*number2,number2,answer)
        self.solution_text = self.solution_text + "<br><br>The mass of each %s is %d g.</font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType12(self):       
        '''e.g.:[Person.Boyname] had 728 ml of <orange juice>.
        He had 95 ml less <orange juice> than [Person.Girlname].
        How much <orange juice> had [Person.Girlname]?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = [random.choice(PersonName.BoyName),random.choice(PersonName.GirlName)]
        
        self.items = [
                      ['orange juice',randint(300,700),randint(100,250)],
                      ['watermelon juice',randint(200,500),randint(50,150)],
                      ['milkshake',randint(300,500),randint(50,200)],
                      ['chocolate shake',randint(300,500),randint(50,200)],
                      ['sparkling water',randint(300,700),randint(50,200)],
                      ['water',randint(300,700),randint(50,200)],
                      ['glycerine',randint(200,500),randint(50,100)],
                      ['paint',randint(400,800),randint(50,150)],
                      ['varnish',randint(200,600),randint(50,150)],
                      ['soda',randint(200,400),randint(50,100)]
                      ]
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[1]
        self.number2 = self.item[2]

        self.problem = "%s had %d <font class='litreFont'>ml</font>&nbsp; of %s.<br>"%(self.names[0],self.number1,self.item[0])
        self.problem = self.problem + "He had %d <font class='litreFont'>ml</font>&nbsp; less %s than %s.<br>"%(self.number2,self.item[0],self.names[1])
        self.problem = self.problem + "How much %s had %s?"%(self.item[0],self.names[1])
                
        self.answer = self.number1 + self.number2
                          
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.number1,self.number2,self.names[0],self.names[1],self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType12(self,problem,answer,number1,number2,name0,name1,item0,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d <font class='litreFont'>ml</font></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td>&nbsp;</td></tr>"%(name0,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'></td></tr>"%(name1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_large.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;=&nbsp; %d <font class='litreFont'>ml</font>"%(number1,number2,answer)
        self.solution_text = self.solution_text + "<br><br>&nbsp;&nbsp;&nbsp;%s had %d <font class='litreFont'>ml</font> of %s.</font>"%(name1,answer,item0)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType13(self):       
        '''e.g.:[Person.Boyname] had 1000 g of <nuts>.
        He packed the <nuts> into bags of 200 g each.
        How many bags did he make?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                      ['nuts',random.choice([50,100,200,250,300,400,500,600])],
                      ['brown rice',random.choice([50,100,200,250,300,400,500,600])],
                      ['fine sugar',random.choice([50,100,200,250,300,400,500,600])],
                      ['sweet potatoes',random.choice([50,100,200,250,300,400,500,600])],
                      ['shallots',random.choice([50,100,200,250,300,400,500,600])],
                      ['chickpeas',random.choice([50,100,200,250,300,400,500,600])],
                      ['pasta shells',random.choice([50,100,200,250,300,400,500,600])],
                      ['bread crumbs',random.choice([50,100,200,250,300,400,500,600])],
                      ['baby carrots',random.choice([50,100,200,250,300,400,500,600])],
                      ['cherry tomatoes',random.choice([50,100,200,250,300,400,500,600])]
                      ]

        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[1]
        self.number2 = randint(3,9)

        self.problem = "%s had %d g of %s.<br>"%(self.name,self.number1*self.number2,self.item[0])
        self.problem = self.problem + "He packed the %s into bags of %d g each.<br>"%(self.item[0],self.number1)
        self.problem = self.problem + "How many bags did he make?"
                
        self.answer = self.number2
                          
        self.unit = "bags"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType13(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=5>%d g</td></tr>"%(number1*number2)
        self.solution_text = self.solution_text + "<tr><td colspan=5 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small5.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d g</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d g</td><td colspan=2 style='height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>. . . . .</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px'>%d g</td></tr>"%(self.color1,number1,self.color1,number1,self.color1,number1)
        self.solution_text = self.solution_text + "<tr><td colspan=5><img src='/images/explanation/P3_model_down_brace_small5.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td colspan=5>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d"%(number1*number2,number1,answer)
        self.solution_text = self.solution_text + "<br><br>He made %d bags.</font>"%(answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType14(self):       
        '''e.g.:A <wooden block tower> is 146 cm <tall>.
    Another <wooden block tower> is 185 cm <tall>.
    What is the total <height> of the two <towers> in metres and centimetres?
    (Write your answer as in the example below.
    Example: 5 m 67 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                      ['wooden block tower','tall','height','towers',randint(110,300),randint(110,300)],
                      ['pillar','tall','height','pillars',randint(110,300),randint(110,300)],
                      ['cabinet','tall','height','cabinets',randint(110,300),randint(110,300)],
                      ['door','tall','height','doors',randint(110,300),randint(110,300)],
                      ['ceiling','high','height','ceilings',randint(200,400),randint(200,400)],
                      ['man','tall','height','men',randint(130,200),randint(130,200)],
                      ['hall','long','length','halls',randint(200,400),randint(200,400)],
                      ['mat','long','length','mats',randint(130,200),randint(130,200)],
                      ['tram','long','length','trams',randint(300,400),randint(300,400)],
                      ['curtain','wide','width','curtains',randint(110,300),randint(110,300)],
                      ['stream','wide','width','streams',randint(200,400),randint(200,400)]
                      ]
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[4]
        self.number2 = self.item[5]
        
        self.problem = "A %s is %d cm %s.<br>"%(self.item[0],self.number1,self.item[1])
        self.problem = self.problem + "Another %s is %d cm %s.<br>"%(self.item[0],self.number2,self.item[1])
        self.problem = self.problem + "What is the total %s of the two %s in metres and centimetres?<br><br>"%(self.item[2],self.item[3])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 23 cm)"
               
        self.number = self.number1+self.number2
                   
        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""               
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.number1,self.number2,self.item[2],self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType14(self,problem,answer,number1,number2,item2,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        elif number1 > number2:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>%d cm</td><td>%d cm</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table>"

        number = number1+number2
        div,mod = divmod(number,100)
        if div > 1:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d cm = %d m</font></div></td>"%(div*100,div)
        else:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d cm &nbsp;+&nbsp; %d cm</td><td>=</td><td>%d cm</td></tr>"%(number1,number2,number)
        if mod>0:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(div*100,mod)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The total %s of the two %s is %s.</font>"%(item2,item3,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType15(self):       
        '''e.g.:[Person.Girlname] <swims> 10 <laps of a pool>.
        If she <swims> a total distance of 500 m, what is the <length of each lap of the pool>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                      ['swims','laps of a pool','length of each lap of the pool',random.randrange(10,40,5),randint(5,10),'lap'],
                      ['runs','rounds of a track','length of one round of the track',random.randrange(25,100,5),randint(5,10),'round'],
                      ['runs','times around a stadium','length of each round of the stadium',random.randrange(25,100,5),randint(5,10),'round'],
                      ['cycles','rounds of a cycling track','length of one round of the track',random.randrange(25,100,5),randint(5,10),'round'],
                      ['cycles','rounds of a circuit','length of one round of the circuit',random.randrange(25,100,5),randint(5,10),'round'],
                      ['jogs',"rounds of a jogger's track",'length of one round of the track',random.randrange(25,100,5),randint(5,10),'round'],
                      ['jogs','rounds of a field','length of each round of the field',random.randrange(25,100,5),randint(5,10),'round'],
                      ['walks','rounds around a block','length of each round of the block',random.randrange(25,100,5),randint(5,10),'round'],
                      ['skates','rounds of a skating track','length of one round of the skating track',random.randrange(25,100,5),randint(5,10),'round'],
                      ['walks','rounds of a trail','length of one round of the trail',random.randrange(25,100,5),randint(5,10),'round']
                      ]
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[3]
        self.number2 = self.item[4]

        self.problem = "%s %s %d %s.<br>"%(self.name,self.item[0],self.number2,self.item[1])
        self.problem = self.problem + "If she %s a total distance of %d m, what is the %s?"%(self.item[0],self.number1*self.number2,self.item[2])
       
        self.answer = self.number1
        
        self.unit = "m"
        self.dollar_unit = ""               
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.number1,self.number2,self.item[2],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType15",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType15(self,problem,answer,number1,number2,item2,item5,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d>%d m</td></tr>"%(number2,number1*number2)
        self.solution_text = self.solution_text + "<tr><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr>"
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:20px;border:white solid 1px;width:50px'></td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d m &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d m"%(number1*number2,number2,answer)
        self.solution_text = self.solution_text + "<br><br>The %s is %d m.</font>"%(item2,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType16(self):       
        '''e.g.:<Container A> has a mass of 725 kg.
        <Container A> is 5 times as heavy as <Container B>.
        What is the mass of <Container B>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                      ['Container A','Container A','Container B','Container B',randint(50,100),randint(2,9),'Container A','Container B'],
                      ['Box A','Box A','Box B','Box B',randint(50,100),randint(2,9),'Box A','Box B'],
                      ['A zebra','The zebra','a mountain goat','the mountain goat',randint(30,100),randint(3,7),'zebra','goat'],
                      ['A baby elephant','The baby elephant','a lion','the lion',randint(70,120),randint(2,6),'elephant','lion'],
                      ['Log A','Log A','Log B','Log B',randint(30,100),randint(2,9),'Log A','Log B'],
                      ['A container','The container','a suitcase','the suitcase',randint(10,30),randint(2,9),'container','suitcase'],
                      ['Trunk A','Trunk A','Trunk B','Trunk B',randint(30,100),randint(2,9),'Trunk A','Trunk B'],
                      ['A trunk','The trunk','a suitcase','the suitcase',randint(10,30),randint(4,9),'trunk','suitcase'],
                      ['A sofa set','The sofa set','a mattress','the mattress',randint(20,80),randint(3,5),'sofa set','mattress'],
                      ['A fish','The fish','a turtle','the turtle',randint(5,30),randint(2,4),'fish','turtle']
                      ]

        self.item = random.choice(self.items)
        
        self.number1 = self.item[4]
        self.number2 = self.item[5]

        self.problem = "%s has a mass of %d kg.<br>"%(self.item[0],self.number1*self.number2)
        self.problem = self.problem + "%s is %d times as heavy as %s.<br>"%(self.item[1],self.number2,self.item[2])
        self.problem = self.problem + "What is the mass of %s?"%(self.item[3])
       
        self.answer = self.number1
        
        self.unit = "kg"
        self.dollar_unit = ""               
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType16(self.problem,self.answer,self.number1,self.number2,self.item[3],self.item[6],self.item[7],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType16",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType16(self,problem,answer,number1,number2,item3,item6,item7,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.colors = random.choice([['aqua','cornflowerblue'],['blueviolet','violet'],['cyan','royalblue'],['darkmagenta','darkorchid'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['turquoise','royalblue']])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d kg</td></tr>"%(number2,number1*number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td>"%(item6)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:20px;border:white solid 1px;width:50px'></td>"%(self.colors[0])
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px'></td></tr>"%(item7,self.colors[1])
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td ><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d kg &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d kg"%(number1*number2,number2,answer)
        self.solution_text = self.solution_text + "<br><br>The mass of %s is %d kg.</font>"%(item3,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType17(self):       
        '''e.g.:There <was> 980 g of <flour in a bag>.
        After [Person.Name] used some of the <flour to make a dessert, there was> 350 g of <flour left in the bag>.
        What was the mass of <flour used to make the dessert>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.PersonName)
        
        self.items = [
                      ['was','flour in a bag','flour to make a dessert, there was','flour left in the bag','flour used to make the dessert',random.randrange(400,980,10),'of flour was used to make the dessert','goldenrod','gold'],
                      ['was','sugar in a jar','sugar to make a jelly, there was','sugar left in the jar','sugar used to make the jelly',random.randrange(400,980,10),'of sugar was used to make the jelly','goldenrod','gold'],
                      ['was','sand in a container','sand for an artwork, there was','sand left in the container','sand used for the artwork',random.randrange(400,980,10),'of sand was used for the artwork','chocolate','burlywood'],
                      ['were','buttons in a container','buttons for a craft project, there were','buttons left in the container','buttons used for the craft project',random.randrange(400,980,10),'of buttons were used for the craft project','purple','plum'],
                      ['were','grains in a packet','grains to feed her pet birds, there were','grains left in the packet','grains used to feed the birds',random.randrange(400,980,10),'of grains were used to feed the birds','darksalmon','bisque'],
                      ['was','fish food in a packet','fish food to feed her pet fishes, there was','fish food left in the packet','fish food used to feed the fishes',random.randrange(400,980,10),'of fish food was used to feed the fishes','deeppink','lightpink'],
                      ['were','chocolate chips in a bag','chocolate chips to make cookies, there were','chocolate chips left in the bag','chocolate chips used to make the cookies',random.randrange(400,980,10),'of chocolate chips were used to make the cookies','chocolate','burlywood'],
                      ['were','apples in a basket','apples to make a pie, there were','apples left in the basket','apples used to make the pie',random.randrange(400,980,10),'of apples were used to make the pie','firebrick','lightcoral'],
                      ['was','chicken meat in a tray','chicken meat to make a dish, there was','chicken meat left in the tray','chicken meat used to make the dish',random.randrange(400,980,10),'of chicken meat was used to make the dish','tomato','orange'],
                      ['were','fruits in a basket','fruits to make a fruit custard, there were','fruits left in the basket','fruits used to make the custard',random.randrange(400,980,10),'of fruits were used to make the custard','orange','yellow']
                      ]

        self.item = random.choice(self.items)
        
        self.number1 = self.item[5]
        self.number2 = (self.item[5] * randint(30,70))/100

        self.problem = "There %s %d g of %s.<br>"%(self.item[0],self.number1,self.item[1])
        self.problem = self.problem + "After %s used some of the %s %d g of %s.<br>"%(self.name,self.item[2],self.number2,self.item[3])
        self.problem = self.problem + "What was the mass of %s?"%(self.item[4])
       
        self.answer = self.number1 - self.number2
        
        self.unit = "g"
        self.dollar_unit = ""               
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType17(self.problem,self.answer,self.number1,self.number2,self.item[6],self.item[7],self.item[8],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType17",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType17(self,problem,answer,number1,number2,item6,color1,color2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if answer==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        elif answer > number2:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'

        #self.colors = random.choice([['goldenrod','gold'],['orange','yellow'],['chocolate','burlywood'],['tomato','orange'],['darksalmon','bisque'],['deeppink','lightpink'],['purple','plum'],['firebrick','lightcoral']])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d g</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(color1,color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>?</td><td>%d g</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d g &nbsp;&minus;&nbsp; %d g &nbsp;=&nbsp; %d g"%(number1,number2,answer)
        self.solution_text = self.solution_text + "<br><br>%d g %s.</font>"%(answer,item6)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType18(self):       
        '''e.g.:[Person.Boyname] had 2 l of <rose syrup>.
            He used 420 ml of it.
            What was the volume of the <rose syrup> left in litres and millilitres?
            (Write your answer as in the example below.
            Example: 5 l 678 ml)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                      ['rose syrup',random.randrange(200,800,10),'deeppink','lightpink'],
                      ['honey',random.randrange(200,800,10),'goldenrod','gold'],
                      ['canola oil',random.randrange(200,800,10),'goldenrod','gold'],
                      ['wall paint',random.randrange(200,800,10),'purple','plum'],
                      ['mango yogurt',random.randrange(200,800,10),'orange','yellow'],
                      ['chicken stock',random.randrange(200,800,10),'darksalmon','bisque'],
                      ['vegetable stock',random.randrange(200,800,10),'orange','yellow'],
                      ['ketchup',random.randrange(200,800,10),'firebrick','lightcoral'],
                      ['chilli sauce',random.randrange(200,800,10),'chocolate','burlywood'],
                      ['tomato soup',random.randrange(200,800,10),'tomato','orange']
                      ]

        self.item = random.choice(self.items)
        self.item = self.items[9]
        
        self.number1 = self.item[1]
        self.number2 = randint(2,9)
        
        self.problem = "%s had %d <font class='litreFont'>l</font>&nbsp; of %s.<br>"%(self.name,self.number2,self.item[0])
        self.problem = self.problem + "He used %d <font class='litreFont'>ml</font>&nbsp; of it.<br>"%(self.number1)
        self.problem = self.problem + "What was the volume of %s left in litres and millilitres?<br><br>"%(self.item[0])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 <font class='litreFont'>l</font>&nbsp; 293 <font class='litreFont'>ml</font>)"
       
        self.number = self.number2*1000-self.number1
                   
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d l %d ml"%(div,mod)
        self.answer1 = "%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""
                
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType18(self.problem,self.answer,self.answer1,self.number1,self.number2,self.item[0],self.item[2],self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType18",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType18(self,problem,answer,answer1,number1,number2,item0,item2,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer1),unit)
        
        tempNumber = number2*1000-number1
        if number1==tempNumber:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        elif number1 < tempNumber:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'
        else:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'

        color1 = item2
        color2 = item3
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d <font class='litreFont'>l</font></td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(color1,color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>%d <font class='litreFont'>ml</font></td><td>?</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br>"

        number = number2*1000-number1
        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <font class='litreFont'>l</font> = 1000 <font class='litreFont'>ml</font><br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>l</font> = %d <font class='litreFont'>ml</font></font></div></td>"%(number2,number2*1000)
        else:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <font class='litreFont'>l</font> = 1000 <font class='litreFont'>ml</font></font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>l</font> &nbsp;&minus;&nbsp; %d <font class='litreFont'>ml</font></td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;&minus;&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number2,number1,number2*1000,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(number)
        if mod>0:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(div*1000,mod)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>l</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer1)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>%s &nbsp;of %s was left.</font>"%(answer1,item0)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType19(self):       
        '''e.g.:[Person.Auntyname] <cooked> 875 g of <rice> on <Monday>.
    She <cooked> 955 g of <rice> on <Tuesday>.
    What was the total mass of <rice> she <cooked> in the two days?
    Write your answer in kilograms and grams.
    (Write your answer as in the example below.
    Example: 5 kg 678 g)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [
                      ['cooked','rice',random.randrange(505,800,5),random.randrange(505,800,5)],
                      ['cooked','vegetables',random.randrange(505,800,5),random.randrange(505,800,5)],
                      ['sold','flour',random.randrange(505,800,5),random.randrange(505,800,5)],
                      ['sold','salt',random.randrange(505,800,5),random.randrange(505,800,5)],
                      ['ate','chicken meat',random.randrange(505,600,5),random.randrange(505,600,5)],
                      ['ate','apples',random.randrange(505,600,5),random.randrange(505,600,5)],
                      ['bought','red beans',random.randrange(505,800,5),random.randrange(505,800,5)],
                      ['bought','blueberries',random.randrange(505,800,5),random.randrange(505,800,5)],
                      ['used','cake mix',random.randrange(505,800,5),random.randrange(505,800,5)],
                      ['used','grapes',random.randrange(505,800,5),random.randrange(505,800,5)]
                      ]

        self.item = random.choice(self.items)
        
        self.number1 = self.item[2]
        self.number2 = self.item[3]
        
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        
        self.day0 = randint(0,6)
        if self.day0 != 6:
            self.day1 = self.day0 + 1
        else:
            self.day1 = 0 
        
        firstDay = self.days[self.day0]
        secondDay = self.days[self.day1]
        
        self.problem = "%s %s %d g of %s on %s.<br>"%(self.name,self.item[0],self.number1,self.item[1],self.days[self.day0])
        self.problem = self.problem + "She %s %d g of %s on %s.<br>"%(self.item[0],self.number2,self.item[1],self.days[self.day1])
        self.problem = self.problem + "What was the total mass of %s she %s in the two days?<br><br>"%(self.item[1],self.item[0])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 kg 293 g)"
       
        self.number = self.number1 + self.number2
                   
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d kg %d g"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""
                
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType19(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[1],firstDay,secondDay,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType19",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType19(self,problem,answer,number1,number2,item0,item1,firstDay,secondDay,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            topCellWidth = 100
            topColspan = 1
            bottomCellWidth = 100
            bottomColspan = 1
        elif number1>number2:
            firstBrace = 'large'
            secondBrace = 'medium'
            topCellWidth = 150
            topColspan = 2
            bottomCellWidth = 100
            bottomColspan = 1
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            topCellWidth = 100
            topColspan = 1
            bottomCellWidth = 150
            bottomColspan = 2

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='width:%dpx'>%d g</td></tr>"%(topColspan,topCellWidth,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;width:%dpx'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(topColspan,topCellWidth,firstBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'></td><td>&nbsp;</td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(firstDay,topColspan,self.color1,topCellWidth)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'></td></tr>"%(secondDay,bottomColspan,self.color2,bottomCellWidth)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='width:%dpx'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(bottomColspan,bottomCellWidth,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='width:%dpx'>%d g</td></tr>"%(bottomColspan,bottomCellWidth,number2)
        self.solution_text = self.solution_text + "</table><br>"

        number = number1+number2
        div,mod = divmod(number,1000)
        
        self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d g &nbsp;+&nbsp; %d g</td><td>=</td><td>%d g</td></tr>"%(number1,number2,number)
        if mod>0:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g &nbsp;+&nbsp; %d g</td></tr>"%(div*1000,mod)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d kg &nbsp;+&nbsp; %d g</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>She %s %s of %s in the two days.</font>"%(item0,answer,item1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType20(self):       
        '''e.g.:[Person.Boyname] has 8 <bottles> of <water>.
            Each <bottle> contains 125 ml of <water>.
            He pours all the <water> into an empty <cooler>.
            How much <water> will be there in the <cooler> in the end?
            (Write your answer as in the example below.
            Example: 5 l 678 ml)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                      ['bottles','water','bottle','cooler',random.randrange(200,300,25)],
                      ['cans','juice','can','jar',random.randrange(200,300,25)],
                      ['cups','milk','cup','container',random.randrange(200,300,25)],
                      ['bowls','soup','bowl','saucepan',random.randrange(200,300,25)],
                      ['mugs','coffee','mug','pot',random.randrange(200,300,25)],
                      ['cups','tea','cup','kettle',random.randrange(200,300,25)],
                      ['vials','oil','vial','can',random.randrange(200,300,25)],
                      ['bottles','shampoo','bottle','dispenser',random.randrange(200,300,25)],
                      ['containers','body lotion','container','dispenser',random.randrange(200,300,25)],
                      ['bottles','ketchup','bottle','pot',random.randrange(200,300,25)]
                      ]

        self.item = random.choice(self.items)
        
        self.number1 = self.item[4]
        self.number2 = randint(6,9)

        self.problem = "%s has %d %s of %s.<br>"%(self.name,self.number2,self.item[0],self.item[1])
        self.problem = self.problem + "Each %s contains %d <font class='litreFont'>ml</font>&nbsp; of %s.<br>"%(self.item[2],self.number1,self.item[1])
        self.problem = self.problem + "He pours all the %s into an empty %s.<br>"%(self.item[1],self.item[3])
        self.problem = self.problem + "How much %s will be there in the %s in the end? Write in litres and millilitres.<br><br>"%(self.item[1],self.item[3])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 1 <font class='litreFont'>l</font>&nbsp; 293 <font class='litreFont'>ml</font>)"
       
        self.number = self.number2*self.number1
                   
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d l %d ml"%(div,mod)
        self.answer1 = "%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""
                
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType20(self.problem,self.answer,self.answer1,self.number1,self.number2,self.item[1],self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType20",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType20(self,problem,answer,answer1,number1,number2,item1,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer1),unit)

        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>ml</font></td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr>"
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:20px;border:white solid 1px;width:50px'></td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td colspan=%d>?</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table>"

        number = number1*number2
        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 <font class='litreFont'>ml</font> = 1 <font class='litreFont'>l</font><br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>ml</font> = %d <font class='litreFont'>l</font></font></div></td>"%(div*1000,div)
        else:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 <font class='litreFont'>ml</font> = 1 <font class='litreFont'>l</font></font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>ml</font> &nbsp;&times;&nbsp; %d</td><td>=</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(number1,number2,number)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>l</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer1)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>There will be &nbsp;%s&nbsp; of %s in the %s in the end.</font>"%(answer1,item1,item3)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType21(self):       
        '''e.g.:[Person.Auntyname] buys a <basket> of <oranges.>
        The mass of the <basket> of <oranges> is 2256 g.
        The mass of the <basket> when empty is 289 g.
        Find the mass of the <oranges> in kilograms and grams.
        (Write your answer as in the example below.
        Example: 5 kg 678 g)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [
                      ['basket','oranges',randint(2000,3000),randint(200,700)],
                      ['basket','flowers',randint(2000,3000),randint(200,700)],
                      ['box','eggplants',randint(2000,3000),randint(200,700)],
                      ['box','chocolates',randint(2000,3000),randint(200,700)],
                      ['tin','biscuits',randint(2000,3000),randint(200,700)],
                      ['tin','almonds',randint(2000,3000),randint(200,700)],
                      ['crate','mangoes',randint(2000,3000),randint(200,700)],
                      ['crate','pineapples',randint(2000,3000),randint(200,700)],
                      ['carton','books',randint(2000,3000),randint(200,700)],
                      ['carton','tiles',randint(2000,3000),randint(200,700)]
                      ]

        self.item = random.choice(self.items)
        
        self.number1 = self.item[2]
        self.number2 = self.item[3]

        self.problem = "%s buys a %s of %s.<br>"%(self.name,self.item[0],self.item[1])
        self.problem = self.problem + "The mass of the %s of %s is %d g.<br>"%(self.item[0],self.item[1],self.number1)
        self.problem = self.problem + "The mass of the %s when empty is %d g.<br>"%(self.item[0],self.number2)
        self.problem = self.problem + "Find the mass of the %s in kilograms and grams.<br><br>"%(self.item[1])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 kg 678 g)"
       
        self.number = self.number1 - self.number2
                   
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d kg %d g"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""
                
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType21(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType21",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType21(self,problem,answer,number1,number2,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td colspan=2>%d g</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large1small1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'>%s</td><td style='background-color:%s;border:white solid 1px;'>%s</td></tr>"%(self.color1,item0,self.color2,item1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td><td><img src='/images/explanation/P3_model_down_brace_large.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d g</td><td>?</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table>"

        number = number1-number2
        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d g = %d kg</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d g &nbsp;&minus;&nbsp; %d g</td><td>=</td><td>%d g</td></tr>"%(number1,number2,number)
        if mod>0:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g &nbsp;+&nbsp; %d g</td></tr>"%(div*1000,mod)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d kg &nbsp;+&nbsp; %d g</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The mass of the %s is %s.</font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType22(self):       
        '''e.g.:[Person.Auntyname] has 2300 g of <brown rice>.
    She buys another 3 kg 850 g of <brown rice>.
    How much <brown rice> does she have altogether in kilograms and grams?
    (Write your answer as in the example below.
    Example: 5 kg 678 g)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = ['brown rice','flour','cheese','butter','meat','tomatoes','red onions','white potatoes','fertilizer','sand']

        self.item = random.choice(self.items)
        
        self.number1 = random.randrange(1025,4025,50)
        self.number2 = random.randrange(1020,4020,50)
        
        div2,mod2 = divmod(self.number2,1000)

        self.problem = "%s has %d g of %s.<br>"%(self.name,self.number1,self.item)
        self.problem = self.problem + "She buys another %d kg %d g of %s.<br>"%(div2,mod2,self.item)
        self.problem = self.problem + "How much %s does she have altogether in kilograms and grams?<br><br>"%(self.item)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 kg 678 g)"
       
        self.number = self.number1 + self.number2
                   
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d kg %d g"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""
                
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType22(self.problem,self.answer,self.number1,self.number2,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType22",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType22(self,problem,answer,number1,number2,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div2,mod2 = divmod(number2,1000)
        number = number1+number2
        div,mod = divmod(number,1000)

        if number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        elif number1 > number2:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'

        self.colors = random.choice([['aqua','cornflowerblue'],['cyan','royalblue'],['darkmagenta','darkorchid'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['turquoise','royalblue'],['tomato','orange'],['purple','plum'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>%d g</td><td>%d kg %d g</td></tr>"%(number1,div2,mod2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>&nbsp;&nbsp;&nbsp;&nbsp;%d kg %d g &nbsp;<br>=&nbsp; %d kg &nbsp;+&nbsp; %d g<br>=&nbsp; %d g + %d g<br>=&nbsp; %d g</font></div></td>"%(div2,mod2,div2,mod2,div2*1000,mod2,number2)
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d g &nbsp;+&nbsp; %d kg %d g</td><td>=</td><td>%d g &nbsp; + %d g</td></tr>"%(number1,div2,mod2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g</td></tr>"%(number)
        if mod>0:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g &nbsp;+&nbsp; %d g</td></tr>"%(div*1000,mod)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d kg &nbsp;+&nbsp; %d g</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>She has %s of %s altogether.</font>"%(answer,item)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType23(self):       
        '''e.g.:[Person.Girlname] bought 6 m of <cloth>.
        She <used> 275 cm of it to <make a shirt>.
        How much <cloth> did she have left?
        Give your answer in metres and centimetres.
        (Write your answer as in the example below.
        Example: 5 m 67 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                      ['cloth','used','make a shirt',random.randrange(150,300,5),randint(5,9)],
                      ['fabric','used','make clothes for her doll',random.randrange(100,200,5),randint(4,9)],
                      ['aluminium foil','used','make a tray',random.randrange(150,300,5),randint(5,9)],
                      ['ribbon','used','make bows',random.randrange(150,300,5),randint(5,9)],
                      ['beaded string','used','make a necklace',random.randrange(150,300,5),randint(5,9)],
                      ['lace','gave','her friend',random.randrange(150,300,5),randint(5,9)],
                      ['rope','gave','her brother',random.randrange(300,500,5),randint(5,9)],
                      ['butter paper','used','make a photo scrapbook',random.randrange(300,500,5),randint(7,9)],
                      ['wallpaper','used','cover a wall',random.randrange(300,700,5),randint(8,9)],
                      ['gift wrapper','used','wrap a gift',random.randrange(100,200,5),randint(4,9)]
                      ]

        self.item = random.choice(self.items)
        
        self.number1 = self.item[4]
        self.number2 = self.item[3]
        
        self.problem = "%s bought %d m of %s.<br>"%(self.name,self.number1,self.item[0])
        self.problem = self.problem + "She %s %d cm of it to %s.<br>"%(self.item[1],self.number2,self.item[2])
        self.problem = self.problem + "How much %s did she have left?<br>"%(self.item[0])
        self.problem = self.problem + "Give your answer in metres and centimetres.<br><br>"
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 68 cm)"
       
        self.number = self.number1*100 - self.number2
                   
        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""
                
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType23(self.problem,self.answer,self.number1,self.number2,self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType23",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType23(self,problem,answer,number1,number2,item0,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        number = number1*100-number2
        if number2==number:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        elif number2 < number:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'
        else:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'

        self.colors = random.choice([['aqua','cornflowerblue'],['cyan','royalblue'],['darkmagenta','darkorchid'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['turquoise','royalblue'],['tomato','orange'],['purple','plum'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d m</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>%d cm</td><td>?</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br>"

        number = number1*100-number2
        div,mod = divmod(number,100)

        self.solution_text = self.solution_text + "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d cm</font></div></td>"%(number1,number1*100)
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m &nbsp;&minus;&nbsp; %d cm</td><td>=</td><td>%d cm &nbsp;&minus;&nbsp; %d cm</td></tr>"%(number1,number2,number1*100,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm</td></tr>"%(number)
        if mod>0:
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(div*100,mod)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>She had %s of %s left.</font>"%(answer,item0)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType24(self):       
        '''e.g.:A bottle has a capacity of 1 l. 
            How many more millilitres of iced tea are needed to fill the bottle to the brim if the bottle contains 250 ml of iced tea?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                      ['bottle','iced tea'],
                      ['container','shampoo'],
                      ['cooler','water'],
                      ['jar','honey'],
                      ['can','liquid detergent'],
                      ['jug','grape juice'],
                      ['bottle','glue'],
                      ['dispenser','fruit punch'],
                      ['pail','paint'],
                      ['pot','soup']
                      ]

        self.item = random.choice(self.items)
        
        self.number1 = randint(1,5)
        self.number2 = random.randrange(200,900,10)
        
        self.problem = "A %s has a capacity of %d <font class='litreFont'>l</font> .<br>"%(self.item[0],self.number1)
        self.problem = self.problem + "How many more millilitres of %s are needed to fill the %s to the brim if the %s contains %d <font class='litreFont'>ml</font>&nbsp; of %s?"%(self.item[1],self.item[0],self.item[0],self.number2,self.item[1])
       
        self.answer = self.number1*1000-self.number2
        
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""
                
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType24(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType24",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType24(self,problem,answer,number1,number2,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        number = number1*1000-number2
        if number2==number:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        elif number2 < number:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'
        else:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'

        self.colors = random.choice([['aqua','cornflowerblue'],['cyan','royalblue'],['darkmagenta','darkorchid'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['turquoise','royalblue'],['tomato','orange'],['purple','plum'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d <font class='litreFont'>l</font></td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td></tr>"%(self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>%d <font class='litreFont'>ml</font></td><td>?</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table>"

        if number1>1:
            self.solution_text = self.solution_text + "<div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <font class='litreFont'>l</font> = 1000 <font class='litreFont'>ml</font><br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d <font class='litreFont'>l</font> = %d <font class='litreFont'>ml</font></font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = self.solution_text + "<div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <font class='litreFont'>l</font> = 1000 <font class='litreFont'>ml</font></font></div></td>"
        self.solution_text = self.solution_text + "<br><br><table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>l</font> &nbsp;&minus;&nbsp; %d <font class='litreFont'>ml</font></td><td>=</td><td>%d <font class='litreFont'>ml</font> &nbsp;&minus;&nbsp; %d <font class='litreFont'>ml</font></td></tr>"%(number1,number2,number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>%d <font class='litreFont'>ml</font>&nbsp; more %s is needed to fill the %s to the brim.</font>"%(answer,item1,item0)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType25(self):       
        '''e.g.:[Person.Girlname] had 220 ml of <green tea>.
        She completely filled 5 <teacups> with all the <green tea>.
        What was the capacity of each <teacup>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                      ['green tea','teacups','teacup',random.randrange(40,150,10)],
                      ['tea tree oil','vials','vial',random.randrange(100,150,10)],
                      ['watermelon juice','glasses','glass',random.randrange(40,150,10)],
                      ['body wash','bottles','bottle',random.randrange(100,250,10)],
                      ['perfume','vials','vial',random.randrange(40,100,10)],
                      ['lotion','containers','container',random.randrange(100,200,10)],
                      ['rose drink','cups','cup',random.randrange(150,250,10)],
                      ['chocolate shake','tumblers','tumbler',random.randrange(150,250,10)],
                      ['banana shake','tumblers','tumbler',random.randrange(150,250,10)],
                      ['glycerine','containers','container',random.randrange(100,150,10)]
                      ]

        self.item = random.choice(self.items)
        
        self.number1 = self.item[3]
        self.number2 = randint(3,9)

        self.problem = "%s had %d <font class='litreFont'>ml</font>&nbsp; of %s.<br>"%(self.name,self.number1*self.number2,self.item[0])
        self.problem = self.problem + "She completely filled %d %s with all the %s.<br>"%(self.number2,self.item[1],self.item[0])
        self.problem = self.problem + "What was the capacity of each %s?"%(self.item[2])
       
        self.answer = self.number1
        
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""
                
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType25(self.problem,self.answer,self.number1,self.number2,self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType25",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType25(self,problem,answer,number1,number2,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise','pink'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d>%d <font class='litreFont'>ml</font></td></tr>"%(number2,number1*number2)
        self.solution_text = self.solution_text + "<tr><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr>"
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:20px;border:white solid 1px;width:50px'></td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d <font class='litreFont'>ml</font> &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d <font class='litreFont'>ml</font>"%(number1*number2,number2,answer)
        self.solution_text = self.solution_text + "<br><br>The capacity of each %s was %d <font class='litreFont'>ml</font> .</font>"%(item2,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswer == 2:
            try:
                answer1 = string.join(str(answer).split(),"")
                '''If user enter answer as 1l 007 ml that should also be correct'''
                if len(answer1.partition("l")[2])==4:
                    answer2 = answer1.partition("l")[0]+"l0"+answer1.partition("l")[2]
                elif len(answer1.partition("l")[2])==3:
                    answer2 = answer1.partition("l")[0]+"l00"+answer1.partition("l")[2]
                else:
                    answer2 = answer1
                InputAnswer = string.join(str(InputAnswer).split(),"")
                return answer1.capitalize() == InputAnswer.capitalize() or answer2.capitalize() == InputAnswer.capitalize()
            except ValueError:
                return False
        elif CheckAnswer == 3:
            try:
                answer1 = string.join(str(answer).split(),"")
                '''If user enter answer as 1m 04 cm that should also be correct'''
                if len(answer1.partition("m")[2])==3:
                    answer2 = answer1.partition("m")[0]+"m0"+answer1.partition("m")[2]
                else:
                    answer2 = answer1
                InputAnswer = string.join(str(InputAnswer).split(),"")
                return answer1.capitalize() == InputAnswer.capitalize() or answer2.capitalize() == InputAnswer.capitalize()
            except ValueError:
                return False
        elif CheckAnswer == 4:
            try:
                answer1 = string.join(str(answer).split(),"")
                '''If user enter answer as 1kg 007 g that should also be correct'''
                if len(answer1.partition("kg")[2])==3:
                    answer2 = answer1.partition("kg")[0]+"kg0"+answer1.partition("kg")[2]
                elif len(answer1.partition("kg")[2])==2:
                    answer2 = answer1.partition("kg")[0]+"kg00"+answer1.partition("kg")[2]
                else:
                    answer2 = answer1
                InputAnswer = string.join(str(InputAnswer).split(),"")
                return answer1.capitalize() == InputAnswer.capitalize() or answer2.capitalize() == InputAnswer.capitalize()
            except ValueError:
                return False
        elif CheckAnswer == 5:
            try:
                answer1 = string.join(str(answer).split(),"")
                '''If user enter answer as 1km 007 m that should also be correct'''
                if len(answer1.partition("km")[2])==3:
                    answer2 = answer1.partition("km")[0]+"km0"+answer1.partition("km")[2]
                elif len(answer1.partition("km")[2])==2:
                    answer2 = answer1.partition("km")[0]+"km00"+answer1.partition("km")[2]
                else:
                    answer2 = answer1
                InputAnswer = string.join(str(InputAnswer).split(),"")
                return answer1.capitalize() == InputAnswer.capitalize() or answer2.capitalize() == InputAnswer.capitalize()
            except ValueError:
                return False
          
