'''
Created on Apr 26, 2013
Module: P3LMKiloGram
Generates the gram and Kilogram problems on Length Mass Volume for Primary 3

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

class P3LMKiloGram:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType7",],
                            6:["ProblemType8",],7:["ProblemType9",],8:["ProblemType10",],
                            9:["ProblemType11",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemType7(),],6:[self.GenerateProblemType8(),],
                                    7:[self.GenerateProblemType9(),],8:[self.GenerateProblemType10(),],
                                    9:[self.GenerateProblemType11(),],
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
        #return self.GenerateProblemType11()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10":self.GenerateProblemType10(),
                            "ProblemType11":self.GenerateProblemType11(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        Write in grams.
         5 kg 243 g = _________ g'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(100,999)

        self.problem = "Write in grams.<br><br>%d kg %d g = _____ g"%(self.number1,self.number2)
        
        self.answer = self.number1*1000+self.number2
                   
        self.unit = "g"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 kg = 1000 g<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d kg = %d g</font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 kg = 1000 g</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d kg %d g</td><td>=</td><td>%d kg &nbsp;+&nbsp; %d g</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g &nbsp;+&nbsp; %d g</td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        Write in grams.
         5 kg 24 g = _________ g'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(1,99)

        self.problem = "Write in grams.<br><br>%d kg %d g = _____ g"%(self.number1,self.number2)
        
        self.answer = self.number1*1000+self.number2
                   
        self.unit = "g"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 kg = 1000 g<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d kg = %d g</font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 kg = 1000 g</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d kg %d g</td><td>=</td><td>%d kg &nbsp;+&nbsp; %d g</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g &nbsp;+&nbsp; %d g</td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        Write in kilograms and grams.
         3456 g = _____ kg _____ g
        (Write your answer as in the example below.
        Example: 5 kg 238 g)'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.number3 = randint(1,9)
        self.number4 = randint(1,9)

        self.number = int(str(self.number1)+str(self.number2)+str(self.number3)+str(self.number4))
        self.problem = "Write in kilograms and grams.<br><br>"
        self.problem = self.problem + "%d g = ___ kg  ___ g<br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 kg 293 g)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d kg %d g"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,number,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d g = %d kg</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d g</td><td>=</td><td>%d g &nbsp;+&nbsp; %d g</td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d kg &nbsp;+&nbsp; %d g</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        Write in kilograms and grams.
         3456 g = _____ kg _____ g
        (Write your answer as in the example below.
        Example: 5 kg 238 g)'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(0,9)
        self.number3 = randint(1,9)
        self.number = int(str(self.number1)+'0'+str(self.number2)+str(self.number3))

        self.problem = "Write in kilograms and grams.<br><br>"
        self.problem = self.problem + "%d g = ___ kg  ___ g<br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 kg 293 g)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d kg %d g"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,number,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d g = %d kg</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d g</td><td>=</td><td>%d g &nbsp;+&nbsp; %d g</td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d kg &nbsp;+&nbsp; %d g</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        The mass of a <bag of sweets> is 1 kg 230 g.
        What is the mass of the <bag of sweets> in grams?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['bag of sweets',randint(1000,2000)],['packed school bag',randint(2000,5000)],['cake',randint(1000,5000)],['fish',randint(1000,9999)],['parcel',randint(1000,9999)],['piece of luggage',randint(1000,9999)],['pair of inline skates',randint(2000,4000)],['pack of beans',randint(1000,2000)],['tub of icecream',randint(1000,2000)],['bouquet of flowers',randint(1000,5000)]]
        
        self.item = random.choice(self.items)
        
        self.number = self.item[1]
        
        self.number1,self.number2 = divmod(self.number,1000)

        self.problem = "The mass of a %s is %d kg %d g.<br><br>"%(self.item[0],self.number1,self.number2)
        self.problem = self.problem + "What is the mass of the %s in grams?"%(self.item[0])
        
        self.answer = self.number
                   
        self.unit = "g"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,number1,number2,item0,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 kg = 1000 g<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d kg = %d g</font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 kg = 1000 g</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d kg %d g</td><td>=</td><td>%d kg &nbsp;+&nbsp; %d g</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g &nbsp;+&nbsp; %d g</td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The mass of the %s is %d g.</font>"%(item0,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        <A bag of fruits> has a mass of 1230 g.
        What is its mass in kilograms and grams?
        (Write your answer as in the example below.
        Example: 5 kg 678 g)'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.items = [['A bag of fruits',randint(1000,3000),'the bag of fruits'],
                      ['A bag of nuts',randint(1000,5000),'the bag of nuts'],
                      ['A bag of vegetables',randint(1000,3000),'the bag of vegetables'],
                      ['A bag of sand',randint(1000,9999),'the bag of sand'],
                      ['A bag of coloured pebbles',randint(1000,3000),'the bag of coloured pebbles'],
                      ['A dictionary',randint(1000,3000),'the dictionary'],
                      ['A printer',randint(1000,9999),'the printer'],
                      ['A cooking pot',randint(1000,3000),'the cooking pot'],
                      ['A flower pot',randint(1000,9999),'the flower pot'],
                      ['A chair',randint(1000,2000),'the chair']]
        
        self.item = random.choice(self.items)
        
        self.number = self.item[1]
        
        self.problem = "%s has a mass of %d g.<br><br>"%(self.item[0],self.number)
        self.problem = self.problem + "What is its mass in kilograms and grams?<br><br>"
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 kg 293 g)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d kg %d g"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number,self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,number,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d g = %d kg</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d g</td><td>=</td><td>%d g &nbsp;+&nbsp; %d g</td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d kg &nbsp;+&nbsp; %d g</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The mass of %s is %s.</font>"%(item2,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        [Person.Auntyname] <bought> 2 kg 300 g <of rice>.
        How much <rice did he buy> in grams?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [['bought','of rice','rice did she buy',random.randrange(5000,9900,100)],
                      ['bought','of meat','meat did she buy',random.randrange(5000,9900)],
                      ['sold','of flour','flour did she sell',random.randrange(5000,9000)],
                      ['sold','of cheese','cheese did she sell',random.randrange(1000,3000)],
                      ['cooked','of grains','grains did she cook',random.randrange(1000,2000)],
                      ['cooked','of pumpkin','pumpkin did she cook',random.randrange(1000,2000)],
                      ['had','of plant food','plant food did she have',random.randrange(1000,5000)],
                      ['had','of cookies','cookies did she have',random.randrange(1000,5000)],
                      ['used','of soil','soil did she use',random.randrange(1000,9900)],
                      ['used','of dough','dough did she use',random.randrange(1000,5000)]]
        
        self.item = random.choice(self.items)
        
        self.number = self.item[3]
        
        self.number1,self.number2 = divmod(self.number,1000)

        self.problem = "%s %s %d kg %d g %s.<br><br>"%(self.name,self.item[0],self.number1,self.number2,self.item[1])
        self.problem = self.problem + "How much %s in grams?"%(self.item[2])
        
        self.answer = self.number
                   
        self.unit = "g"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,number1,number2,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 kg = 1000 g<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d kg = %d g</font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 kg = 1000 g</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d kg %d g</td><td>=</td><td>%d kg &nbsp;+&nbsp; %d g</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g &nbsp;+&nbsp; %d g</td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d g</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>She %s %d g %s.</font>"%(item0,answer,item1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:
        [Person.Unclename] <bought> 2300 g <of rice>.
        How much <rice did she buy> in kilograms and grams?
        (Write your answer as in the example below.
        Example: 5 kg 678 g)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['bought','of rice','rice did he buy',random.randrange(5000,9900,100)],
                      ['bought','of meat','meat did he buy',random.randrange(5000,9900,100)],
                      ['sold','of flour','flour did he sell',random.randrange(5000,9000,100)],
                      ['sold','of cheese','cheese did he sell',random.randrange(1000,3000,100)],
                      ['cooked','of grains','grains did he cook',random.randrange(1000,2000,100)],
                      ['cooked','of pumpkin','pumpkin did he cook',random.randrange(1000,2000,100)],
                      ['had','of plant food','plant food did he have',random.randrange(1000,5000,100)],
                      ['had','of cookies','cookies did he have',random.randrange(1000,5000,100)],
                      ['used','of soil','soil did he use',random.randrange(1000,9900,100)],
                      ['used','of dough','dough did he use',random.randrange(1000,5000,100)]]
        
        self.item = random.choice(self.items)
        
        self.number = self.item[3]
        
        self.problem = "%s %s %d g %s.<br><br>"%(self.name,self.item[0],self.number,self.item[1])
        self.problem = self.problem + "How much %s in kilograms and grams?<br><br>"%(self.item[2])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 kg 293 g)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d kg %d g"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.number,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,number,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d g = %d kg</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 g = 1 kg</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d g</td><td>=</td><td>%d g &nbsp;+&nbsp; %d g</td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d kg &nbsp;+&nbsp; %d g</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>He %s %s %s.</font>"%(item0,answer,item1)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:
        Fill in the blank with 'kg' or 'g'.
         <The mass of a woman is about> 60 ____.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['The mass of a woman is about','kg',randint(40,70),'The mass of a person is usually measured in kilograms.<br>It is normal for a woman to have a mass of about','kg.<br>Only a toy woman would be as light as','g!'],
                      ['A sofa set has a mass of about','kg',random.choice([20,25,30,35,40,45,50]),'Furniture is meant to be strong and sturdy.<br>It is normal for a sofa set to have a mass of about','kg.<br>Only a toy sofa set would be as light as','g!'],
                      ['The mass of a television set is about','kg',random.choice([5,6,7,8,9,10,12,14,16,18,20]),'Televition sets are big.<br>It is normal for a TV set to have a mass of about','kg.<br>Only a toy TV set would be as light as','g!'],
                      ['A sack of rice has a mass of about','kg',random.choice([1,2,5,10,15,20,30,40,50]),'A sack is a big bag.<br>It is normal for a sack of rice to have a mass of about','kg.<br>Only a toy sack of rice would be as light as','g!'],
                      ['The mass of a box filled with books has a mass of about','kg',random.choice([1,2,5,10,15,20,30,40,50]),'Books can be either light or heavy and their masses can be measured in grams or kilograms.<br>However, it would be too light for a box filled with books to be only','g!<br>It would be normal for a box of books to have a mass of','kg.'],
                      ['The mass of a stuffed toy is about','g',random.choice([100,120,150,170,200,230,250,280,300,320,350,370,400,420,450,480,500]),'Stuffed toys may be big or small in size but they are light in mass.<br>It is normal for them to have a mass of','g.<br>A stuffed toy that has a mass of','kg would be too heavy to be called a toy!'],
                      ['A bunch of bananas has a mass of about','g',random.choice([300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]),'The mass of a bunch of bananas can be measured in either grams or kilograms.<br>However,','kg would be the mass of a whole truckful of bananas!<br>A bunch of bananas commonly has a mass of about','g.'],
                      ['The mass of a softball is about','g',random.choice([170,180,190,200,210,220,230,240,250,260,270,280]),'A softball is soft and light.<br>It is normal for it to have a mass of','g.<br>A softball that has a mass of','kg would be too heavy to be played with!'],
                      ['A baseball bat has a mass of about','g',random.choice([450,480,510,540,570,600,620,650,680,710,740,770,800,820,850,880]),'You hold a baseball bat in your hands to play baseball.<br>If it is as heavy as','kg, you would need a crane to lift it!<br>Normally, a baseball bat has a mass of','g.'],
                      ['A magazine has a mass of about','g',random.choice([100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400]),'Magazines come in different sizes and masses.<br>However, a magazine with a mass of','kg would belong in a museum!<br>It is common for a magazine to have a mass of','g.']]
        
        self.item = random.choice(self.items)
        self.number = self.item[2]
        
        self.problem = "Fill in the blank with 'kg' or 'g'.<br><br>"
        self.problem = self.problem + "%s %d ___."%(self.item[0],self.number)
        
        self.answer = self.item[1]
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.number,self.item[3],self.item[4],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,number,item3,item4,item5,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        self.solution_text =  "<font class='ExplanationFont'>%s %d %s %d %s</font>"%(item3,number,item4,number,item5)
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
        Write in grams.
         5 kg 243 g = _________ g'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1"
        self.CheckAnswerType = 1

        self.number1 = randint(1,9)
        self.number2 = randint(100,999)

        self.problem = "Write in grams.<br><br>%d kg %d g = _____ g"%(self.number1,self.number2)
        
        self.answer = self.number1*1000+self.number2
                   
        self.unit = "g"
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [float(self.answer)/100,
                             str(self.number1)+"."+str(self.number2),float(self.answer)/10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        Write in grams.
         5 kg 24 g = _________ g'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ2"
        self.CheckAnswerType = 1

        self.number1 = randint(1,9)
        self.number2 = randint(1,99)

        self.problem = "Write in grams.<br><br>%d kg %d g = _____ g"%(self.number1,self.number2)
        
        self.answer = self.number1*1000+self.number2
                   
        self.unit = "g"
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [float(self.answer)/100,
                             str(self.number1)+"."+str(self.number2),float(self.answer)/10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
        Write in kilograms and grams.
         3456 g = _____ kg _____ g
        (Write your answer as in the example below.
        Example: 5 kg 238 g)'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ3"
        self.CheckAnswerType = 2

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.number3 = randint(1,9)
        self.number4 = randint(1,9)

        self.number = int(str(self.number1)+str(self.number2)+str(self.number3)+str(self.number4))
        self.problem = "Write in kilograms and grams.<br><br>"
        self.problem = self.problem + "%d g = ___ kg  ___ g<br><br>"%(self.number)
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d kg %d g"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = ["%d kg %d g"%(divmod(self.number,10)),
                             "%d kg %d g"%(divmod(self.number,100)),
                             "%d kg %d g"%(divmod(self.number,1)),
                             str(self.number1)+str(self.number2)+" kg "+str(self.number3)+" g"]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ4(self):
        '''e.g.:
        Write in kilograms and grams.
         3456 g = _____ kg _____ g
        (Write your answer as in the example below.
        Example: 5 kg 238 g)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ4"
        self.CheckAnswerType = 2

        self.number1 = randint(1,9)
        self.number2 = randint(0,9)
        self.number3 = randint(1,9)
        self.number = int(str(self.number1)+'0'+str(self.number2)+str(self.number3))

        self.problem = "Write in kilograms and grams.<br><br>"
        self.problem = self.problem + "%d g = ___ kg  ___ g<br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 kg 293 g)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d kg %d g"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = ["%d kg %d g"%(divmod(self.number,10)),
                             "%d kg %d g"%(divmod(self.number,100)),
                             "%d kg %d g"%(divmod(self.number,1)),
                             str(self.number1)+str(self.number2)+" kg "+str(self.number3)+" g"]
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswer == 2:
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
        elif CheckAnswer == 3:
            try:
                return str(answer).capitalize() == str(InputAnswer).capitalize()
            except ValueError:
                return False