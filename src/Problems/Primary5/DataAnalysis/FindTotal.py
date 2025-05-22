'''
Created on Oct 06, 2011

Module: FindTotal
Generates "Finding the total" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random
from random import randint
from Problems import PersonName

class FindTotal:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"easy":[self.GenerateProblemType1(),
                                    self.GenerateProblemTypeMCQ1()],
                            "medium":[self.GenerateProblemType2(),
                                self.GenerateProblemTypeMCQ2()],
                            }
        try:
            return random.choice(self.ProblemType[level])
        except KeyError:
            return random.choice(random.choice(self.ProblemType.values()))
        #return self.GenerateProblemTypeMCQ2()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType5","ProblemTypeMCQ5",],
                            6:["ProblemType6","ProblemTypeMCQ6",],
                            7:["ProblemType7","ProblemTypeMCQ7",],
                            8:["ProblemType8","ProblemTypeMCQ8",],
                            9:["ProblemType9a","ProblemTypeMCQ9a","ProblemType9b","ProblemTypeMCQ9b",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemType5(),self.GenerateProblemTypeMCQ5(),],
                                    6:[self.GenerateProblemType6(),self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemType7(),self.GenerateProblemTypeMCQ7(),],
                                    8:[self.GenerateProblemType8(),self.GenerateProblemTypeMCQ8(),],
                                    9:[self.GenerateProblemType9a(),self.GenerateProblemTypeMCQ9a(),self.GenerateProblemType9b(),self.GenerateProblemTypeMCQ9b(),],
                                    }
        
        #Creating one more problem type so it creates a list and not a list of lists
        self.ProblemTypes = []
        
        for i in self.ProblemType.values():
            for k in i:
                self.ProblemTypes.append(k)
                
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(random.choice(self.GenerateProblemType.values()))
        else:
            if LastProblemID in self.ProblemTypes:
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if LastProblemID in v][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return random.choice(self.GenerateProblemType[NextProblemKey])
            else:
                return random.choice(random.choice(self.GenerateProblemType.values()))
        #return self.GenerateProblemTypeMCQ9b()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9a":self.GenerateProblemType9a(),
                            "ProblemType9b":self.GenerateProblemType9b(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),
                            "ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            "ProblemTypeMCQ9a":self.GenerateProblemTypeMCQ9a(),
                            "ProblemTypeMCQ9b":self.GenerateProblemTypeMCQ9b(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g.:
        Average of 3 numbers is 12. Find the sum of the 3 numbers'''
        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.number1 = randint(0,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.ProblemSelection = randint(1,3)
        if self.ProblemSelection == 1:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.average = (self.number1 + self.number2 + self.number3)/3
            self.answer = str(self.number1+self.number2+self.number3)
            self.flag = 1
        elif self.ProblemSelection == 2:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.average = (self.number1 + self.number2 + self.number3+self.number4)/4
            self.answer = str(self.number1+self.number2+self.number3+self.number4)            
            self.flag = 2
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.average = (self.number1 + self.number2 + self.number3+self.number4+self.number5)/5
            self.answer = str(self.number1+self.number2+self.number3+self.number4+self.number5)            
            self.flag = 3                    
        
        self.problem1 = "Find the total of "+str(self.ProblemSelection+2)+" numbers if their average is "+str(self.average)+"."
        self.problem2 = "The average of "+str(self.ProblemSelection+2)+" numbers is "+str(self.average)+". What is their sum?"
        self.problem3 = "The average of "+str(self.ProblemSelection+2)+" numbers is "+str(self.average)+". Find the sum of those numbers."
        self.problem4 = "What is the sum of "+str(self.ProblemSelection+2)+" numbers if their average is "+str(self.average)+"?"
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.average,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}    
    
    def ExplainType1(self,problem,answer,average,flag):
        self.answer_text = "The correct answer is:<br>"+str(answer)
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Average of the items</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Total of all items &divide; Number of items</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Or,</td><td style='padding-left:0px; padding-right:0px'>&nbsp;</td><td style='text-align:left'>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>Total of all items</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Average of the items &times; Number of items</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Average of the items</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(average)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of items</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(flag+2)+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total of all items</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(average)+" &times; "+str(flag+2)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Data-Analysis/Finding-Average" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.:
        Find the average of the given numbers. (Write your answer correct up to 1 decimal places)'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(0,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.ProblemSelection = randint(1,3)

        if self.ProblemSelection == 1:
            self.average = round(float(self.number1 + self.number2 + self.number3)/3,2)
            self.answer = str(self.number1+self.number2+self.number3)
            self.flag = 1
        elif self.ProblemSelection == 2:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4)/4,2)
            self.answer = str(self.number1+self.number2+self.number3+self.number4)            
            self.flag = 2
        else:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4+self.number5)/5,2)
            self.answer = str(self.number1+self.number2+self.number3+self.number4+self.number5)            
            self.flag = 3                    

        self.problem1 = "Find the total of "+str(self.ProblemSelection+2)+" numbers if their average is "+str(self.average)+"."
        self.problem2 = "The average of "+str(self.ProblemSelection+2)+" numbers is "+str(self.average)+". What is their sum?"
        self.problem3 = "The average of "+str(self.ProblemSelection+2)+" numbers is "+str(self.average)+". Find the sum of those numbers."
        self.problem4 = "What is the sum of "+str(self.ProblemSelection+2)+" numbers if their average is "+str(self.average)+"?"
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
        self.problem = self.problem + "<br>(Round off to the nearest whole number if required)"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.average,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def GenerateProblemType3(self):
        '''e.g.:
        [Person.name] had <number> bags of [marbles] containing an average of <average> [marbles] each. What was the total number of marbles in the bags?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice(['marbles','beads','shells','forks','spoons','plates','rubberbands','apples','oranges','pears',
                      'peaches','potatoes','guavas','kiwifruits','candies','bars of chocolate','coasters','straws'])
        
        if self.NumberOfItems == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.average = (self.number1 + self.number2 + self.number3)/3
            self.answer = str(self.number1+self.number2+self.number3)
        elif self.NumberOfItems == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.average = (self.number1 + self.number2 + self.number3+self.number4)/4
            self.answer = str(self.number1+self.number2+self.number3+self.number4)            
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.average = (self.number1 + self.number2 + self.number3+self.number4+self.number5)/5
            self.answer = str(self.number1+self.number2+self.number3+self.number4+self.number5)
                               
        self.problem = self.name+" had "+str(self.NumberOfItems)+" bags of "+self.items+" containing an average of "+str(self.average)
        self.problem = self.problem +" "+self.items+" each. What was the total number of "+self.items+" in the bags?"
        
        self.item1 = "bags"
        
        self.unit = self.items
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.average,self.item1,self.items,self.NumberOfItems,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def GenerateProblemType4(self):
        '''e.g.:
        <number> boxes contain an average of <average> [pencils] per box. How many [pencils] are there altogether?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice(['pencils','sharpeners','erasers','rulers','pens','crayons','highlighters','markers','cookies','bars of chocolate','cans of juice'])
        
        if self.NumberOfItems == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.average = (self.number1 + self.number2 + self.number3)/3
            self.answer = str(self.number1+self.number2+self.number3)
        elif self.NumberOfItems == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.average = (self.number1 + self.number2 + self.number3+self.number4)/4
            self.answer = str(self.number1+self.number2+self.number3+self.number4)            
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.average = (self.number1 + self.number2 + self.number3+self.number4+self.number5)/5
            self.answer = str(self.number1+self.number2+self.number3+self.number4+self.number5)
                               
        self.problem = str(self.NumberOfItems)+" boxes contain an average of "+str(self.average)+" "+self.items+" per box. "
        self.problem = self.problem + "How many "+self.items+" are there altogether?"
        
        self.item1 = "boxes"
        self.unit = self.items
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.average,self.item1,self.items,self.NumberOfItems,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def GenerateProblemType5(self):
        '''e.g.:
        The average score of <number> [pupils] in a [maths test] is <average> [marks]. Find the total number of [marks] scored.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice([['pupils','maths test','marks','marks'],['students','science exam','marks','marks'],
                                    ['players','basketball game','points','points'],['players','cricket game','runs','runs'],
                                    ['friends','video game','points','points'],
                                    ['players','volleyball video game','points','points'],['kids','computer game','points','points']])
        
        if self.NumberOfItems == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.average = (self.number1 + self.number2 + self.number3)/3
            self.answer = str(self.number1+self.number2+self.number3)
        elif self.NumberOfItems == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.average = (self.number1 + self.number2 + self.number3+self.number4)/4
            self.answer = str(self.number1+self.number2+self.number3+self.number4)            
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.average = (self.number1 + self.number2 + self.number3+self.number4+self.number5)/5
            self.answer = str(self.number1+self.number2+self.number3+self.number4+self.number5)
                               
        self.problem = "The average score of "+str(self.NumberOfItems)+" "+self.items[0]+" in a "+self.items[1]+" is "+str(self.average)+" "+self.items[2]+"."
        self.problem = self.problem+" Find the total number of "+self.items[3]+" scored."
        
        self.unit = self.items[2]
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.average,self.items[0],self.items[2],self.NumberOfItems,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}

    def GenerateProblemType6(self):
        '''e.g.:
        What is the total number of [shirts sewn] by [Person.Girlname] in <number> days if she [sewed] an average of <average> [shirts] per day?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.GirlName)
        self.items = random.choice([['shirts sewn','sewed','shirts'],['skirts sewn','sewed','skirts'],['cushion covers sewn','sewed','cushion covers'],
                                    ['curtains sewn','sewed','curtains'],['glasses of lemonade sold','sold','glasses of lemonade'],['toys sold','sold','toys'],
                                    ['pizza orders received','received','pizza orders'],['rolls of lace bought','bought','rolls of lace'],['mathematics problems solved','solved','problems'],
                                    ['number of pages of a novel read','read','pages']])
        
        if self.NumberOfItems == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.average = (self.number1 + self.number2 + self.number3)/3
            self.answer = str(self.number1+self.number2+self.number3)
        elif self.NumberOfItems == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.average = (self.number1 + self.number2 + self.number3+self.number4)/4
            self.answer = str(self.number1+self.number2+self.number3+self.number4)            
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.average = (self.number1 + self.number2 + self.number3+self.number4+self.number5)/5
            self.answer = str(self.number1+self.number2+self.number3+self.number4+self.number5)
                               
        self.problem = "What is the total number of "+self.items[0]+" by "+self.name+" in "+str(self.NumberOfItems)+" days "
        self.problem = self.problem + "if she "+self.items[1]+" an average of "+str(self.average)+" "+self.items[2]+" per day?"
        
        self.item1 = "days"
        self.unit = self.items[2]
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.average,self.item1,self.items[0],self.NumberOfItems,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}
    
    def ExplainType3(self,problem,answer,average,item1,items,numberOfItems,unit):
        self.answer_text = "The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Average of the items</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Total of all items &divide; Number of items</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Or,</td><td style='padding-left:0px; padding-right:0px'>&nbsp;</td><td style='text-align:left'>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>Total of all items</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Average of the items &times; Number of items</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Average "+items+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(average)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item1+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(numberOfItems)+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total "+items+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(average)+" &times; "+str(numberOfItems)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Data-Analysis/Finding-Average" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):
        '''e.g.:
        [Person.name] spent an average of $<amount> on <number> diferent [books]. Find the total cost of the [books].'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = float(randint(200,3000))/100
        self.number2 = float(randint(200,3000))/100
        self.number3 = float(randint(200,3000))/100
        self.number4 = float(randint(200,3000))/100
        self.number5 = float(randint(200,3000))/100
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice(['books','toys','pens','rolls of coloured strings','water bottles','soccer balls','keychains','bracelets','plants','lunchboxes'])
        
        if self.NumberOfItems == 3:
            self.average = round(float(self.number1 + self.number2 + self.number3)/3,2)            
        elif self.NumberOfItems == 4:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4)/4,2)
        else:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4+self.number5)/5,2)

        self.answer = str(round(self.average * self.NumberOfItems,2))

        if len(str(self.average).partition(".")[2])==1:
            self.average = str(self.average)+"0"                               
        if len(str(self.answer).partition(".")[2])==1:
            self.answer = str(self.answer)+"0"                               

        self.problem = self.name+" spent an average of $"+str(self.average)+" on "+str(self.NumberOfItems)+" different "+self.items+". Find the total cost of the "+self.items+"."
        
        self.item1 = self.items
        self.item2 = "spent"
        self.item3 = "cost"
        self.unit = ""
        self.dollar = "$"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.average,self.item1,self.item2,self.item3,self.NumberOfItems,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":self.dollar}

    def GenerateProblemType8(self):
        '''e.g.:
        What is the total mass of <number> [packages] if their average mass is <decimal> kg?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = float(randint(2000,4000))/100
        self.number2 = float(randint(2000,4000))/100
        self.number3 = float(randint(2000,4000))/100
        self.number4 = float(randint(2000,4000))/100
        self.number5 = float(randint(2000,4000))/100
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice(['boys', 'girls', 'children', 'people', 'cartons', 'boxes', 'suitcases', 'sacks of sugar', 'sacks of rice'])
        
        if self.NumberOfItems == 3:
            self.average = round(float(self.number1 + self.number2 + self.number3)/3,2)            
        elif self.NumberOfItems == 4:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4)/4,2)
        else:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4+self.number5)/5,2)

        self.answer = str(round(self.average * self.NumberOfItems,2))

        if len(str(self.average).partition(".")[2])==1:
            self.average = str(self.average)+"0"                               
        if len(str(self.answer).partition(".")[2])==1:
            self.answer = str(self.answer)+"0"                               

        self.problem = "What is the total mass of "+str(self.NumberOfItems)+" "+self.items+" if their average mass is "+str(self.average)+" kg?"
        
        self.item1 = self.items
        self.item2 = "mass"
        self.item3 = "mass"
        self.unit = "kg"
        self.dollar = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.average,self.item1,self.item2,self.item3,self.NumberOfItems,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":self.dollar}

    def GenerateProblemType9a(self):
        '''e.g.:
        Find the total length of <number> [strips of ribbon] if their average length is <decimal> cm.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = float(randint(200,4000))/100
        self.number2 = float(randint(200,4000))/100
        self.number3 = float(randint(200,4000))/100
        self.number4 = float(randint(200,4000))/100
        self.number5 = float(randint(200,4000))/100
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice(['strips of ribbon','pieces of lace','strips of tape','pieces of wire','pieces of string','sticks','straws','twigs','pencils'])
        
        if self.NumberOfItems == 3:
            self.average = round(float(self.number1 + self.number2 + self.number3)/3,2)            
        elif self.NumberOfItems == 4:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4)/4,2)
        else:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4+self.number5)/5,2)

        self.answer = str(round(self.average * self.NumberOfItems,2))

        if len(str(self.average).partition(".")[2])==1:
            self.average = str(self.average)+"0"                               
        if len(str(self.answer).partition(".")[2])==1:
            self.answer = str(self.answer)+"0"                               

        self.problem = "Find the total length of "+str(self.NumberOfItems)+" "+self.items+" if their average length is "+str(self.average)+" cm."
        
        self.item1 = self.items
        self.item2 = "length"
        self.item3 = "length"
        self.unit = "cm"
        self.dollar = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.average,self.item1,self.item2,self.item3,self.NumberOfItems,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType9a",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":self.dollar}

    def GenerateProblemType9b(self):
        '''e.g.:
        What is the total length of <number> [pieces of fabric] if their average length is <decimal> m.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = float(randint(200,4000))/100
        self.number2 = float(randint(200,4000))/100
        self.number3 = float(randint(200,4000))/100
        self.number4 = float(randint(200,4000))/100
        self.number5 = float(randint(200,4000))/100
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice(['strips of cloth','pieces of ribbon','sheets of foil','sheets of wrapper','pieces of rope','pieces of cable','pieces of thread','poles','pipes','logs of wood'])
        
        if self.NumberOfItems == 3:
            self.average = round(float(self.number1 + self.number2 + self.number3)/3,2)            
        elif self.NumberOfItems == 4:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4)/4,2)
        else:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4+self.number5)/5,2)

        self.answer = str(round(self.average * self.NumberOfItems,2))

        if len(str(self.average).partition(".")[2])==1:
            self.average = str(self.average)+"0"                               
        if len(str(self.answer).partition(".")[2])==1:
            self.answer = str(self.answer)+"0"                               

        self.problem = "What is the total length of "+str(self.NumberOfItems)+" "+self.items+" if their average length is "+str(self.average)+" m."
        
        self.item1 = self.items
        self.item2 = "length"
        self.item3 = "length"
        self.unit = "m"
        self.dollar = ""
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.average,self.item1,self.item2,self.item3,self.NumberOfItems,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType9b",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":self.dollar}
    
    def ExplainType7(self,problem,answer,average,item1,item2,item3,numberOfItems,unit,dollar):
        self.answer_text = "The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>We know,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Average of the items</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Total of all items &divide; Number of items</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Or,</td><td style='padding-left:0px; padding-right:0px'>&nbsp;</td><td style='text-align:left'>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right'>Total of all items</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>Average of the items &times; Number of items</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Average "+item2+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(average)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item1+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(numberOfItems)+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left' colspan='2'><br>Therefore,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total "+item3+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(average)+" &times; "+str(numberOfItems)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+dollar+str(answer)+" "+unit+"</td></tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Data-Analysis/Finding-Average" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,
                    CheckAnswerType,grade,complexity_level,HCScore):
        
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
                'CheckAnswerType':CheckAnswerType,'grade':5,"complexity_level":complexity_level,"HCScore":HCScore}      

    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        Average of 3 numbers is 12. Find the sum of the 3 numbers'''
        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.number1 = randint(0,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.ProblemSelection = randint(1,3)
        if self.ProblemSelection == 1:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.average = (self.number1 + self.number2 + self.number3)/3
            self.answer = self.number1+self.number2+self.number3
            self.flag = 1
        elif self.ProblemSelection == 2:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.average = (self.number1 + self.number2 + self.number3+self.number4)/4
            self.answer = self.number1+self.number2+self.number3+self.number4            
            self.flag = 2
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.average = (self.number1 + self.number2 + self.number3+self.number4+self.number5)/5
            self.answer = self.number1+self.number2+self.number3+self.number4+self.number5           
            self.flag = 3                    
        
        self.problem1 = "Find the total of "+str(self.ProblemSelection+2)+" numbers if their average is "+str(self.average)+"."
        self.problem2 = "The average of "+str(self.ProblemSelection+2)+" numbers is "+str(self.average)+". What is their sum?"
        self.problem3 = "The average of "+str(self.ProblemSelection+2)+" numbers is "+str(self.average)+". Find the sum of those numbers."
        self.problem4 = "What is the sum of "+str(self.ProblemSelection+2)+" numbers if their average is "+str(self.average)+"?"
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
        
        self.problem_type = "ProblemTypeMCQ1"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 5
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.average,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        Find the average of the given numbers. (Write your answer correct up to 1 decimal places)'''
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(0,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.ProblemSelection = randint(1,3)

        if self.ProblemSelection == 1:
            self.average = round(float(self.number1 + self.number2 + self.number3)/3,2)
            self.answer = self.number1+self.number2+self.number3
            self.flag = 1
        elif self.ProblemSelection == 2:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4)/4,2)
            self.answer = self.number1+self.number2+self.number3+self.number4           
            self.flag = 2
        else:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4+self.number5)/5,2)
            self.answer = self.number1+self.number2+self.number3+self.number4+self.number5            
            self.flag = 3                    

        self.problem1 = "Find the total of "+str(self.ProblemSelection+2)+" numbers if their average is "+str(self.average)+"."
        self.problem2 = "The average of "+str(self.ProblemSelection+2)+" numbers is "+str(self.average)+". What is their sum?"
        self.problem3 = "The average of "+str(self.ProblemSelection+2)+" numbers is "+str(self.average)+". Find the sum of those numbers."
        self.problem4 = "What is the sum of "+str(self.ProblemSelection+2)+" numbers if their average is "+str(self.average)+"?"
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
        
        self.problem_type = "ProblemTypeMCQ2"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 5
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.average,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)   

    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
        [Person.name] had <number> bags of [marbles] containing an average of <average> [marbles] each. What was the total number of marbles in the bags?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice(['marbles','beads','shells','forks','spoons','plates','rubberbands','apples','oranges','pears',
                      'peaches','potatoes','guavas','kiwifruits','candies','bars of chocolate','coasters','straws'])
        
        if self.NumberOfItems == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.average = (self.number1 + self.number2 + self.number3)/3
        elif self.NumberOfItems == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.average = (self.number1 + self.number2 + self.number3+self.number4)/4
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.average = (self.number1 + self.number2 + self.number3+self.number4+self.number5)/5
        
        self.answer = self.average * self.NumberOfItems
        
        self.problem = self.name+" had "+str(self.NumberOfItems)+" bags of "+self.items+" containing an average of "+str(self.average)
        self.problem = self.problem +" "+self.items+" each. What was the total number of "+self.items+" in the bags?"
        
        self.item1 = "bags"
        
        self.unit = self.items
        
        self.problem_type = "ProblemTypeMCQ3"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 5
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))
        self.wrongAnswers.append(str(self.average))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.average,self.item1,self.items,self.NumberOfItems,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)   

    def GenerateProblemTypeMCQ4(self):
        '''e.g.:
        <number> boxes contain an average of <average> [pencils] per box. How many [pencils] are there altogether?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice(['pencils','sharpeners','erasers','rulers','pens','crayons','highlighters','markers','cookies','bars of chocolate','cans of juice'])
        
        if self.NumberOfItems == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.average = (self.number1 + self.number2 + self.number3)/3
        elif self.NumberOfItems == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.average = (self.number1 + self.number2 + self.number3+self.number4)/4
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.average = (self.number1 + self.number2 + self.number3+self.number4+self.number5)/5
        
        self.answer = self.average * self.NumberOfItems
        self.problem = str(self.NumberOfItems)+" boxes contain an average of "+str(self.average)+" "+self.items+" per box. "
        self.problem = self.problem + "How many "+self.items+" are there altogether?"
        
        self.item1 = "boxes"
        self.unit = self.items
        
        self.problem_type = "ProblemTypeMCQ4"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 5
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))
        self.wrongAnswers.append(str(self.average))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.average,self.item1,self.items,self.NumberOfItems,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)   

    def GenerateProblemTypeMCQ5(self):
        '''e.g.:
        The average score of <number> [pupils] in a [maths test] is <average> [marks]. Find the total number of [marks] scored.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice([['pupils','maths test','marks','marks'],['students','science exam','marks','marks'],
                                    ['players','basketball game','points','points'],['players','cricket game','runs','runs'],
                                    ['friends','video game','points','points'],
                                    ['players','volleyball video game','points','points'],['kids','computer game','points','points']])
        
        if self.NumberOfItems == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.average = (self.number1 + self.number2 + self.number3)/3
        elif self.NumberOfItems == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.average = (self.number1 + self.number2 + self.number3+self.number4)/4
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.average = (self.number1 + self.number2 + self.number3+self.number4+self.number5)/5

        self.answer = self.average * self.NumberOfItems                               
        self.problem = "The average score of "+str(self.NumberOfItems)+" "+self.items[0]+" in a "+self.items[1]+" is "+str(self.average)+" "+self.items[2]+"."
        self.problem = self.problem+" Find the total number of "+self.items[3]+" scored."
        
        self.unit = self.items[2]
        
        self.problem_type = "ProblemTypeMCQ5"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 5
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))
        self.wrongAnswers.append(str(self.average))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.average,self.items[0],self.items[2],self.NumberOfItems,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)   

    def GenerateProblemTypeMCQ6(self):
        '''e.g.:
        What is the total number of [shirts sewn] by [Person.Girlname] in <number> days if she [sewed] an average of <average> [shirts] per day?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = randint(2,30)
        self.number2 = randint(2,30)
        self.number3 = randint(2,20)
        self.number4 = randint(2,20)
        self.number5 = randint(2,20)
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.GirlName)
        self.items = random.choice([['shirts sewn','sewed','shirts'],['skirts sewn','sewed','skirts'],['cushion covers sewn','sewed','cushion covers'],
                                    ['curtains sewn','sewed','curtains'],['glasses of lemonade sold','sold','glasses of lemonade'],['toys sold','sold','toys'],
                                    ['pizza orders received','received','pizza orders'],['rolls of lace bought','bought','rolls of lace'],['mathematics problems solved','solved','problems'],
                                    ['number of pages of a novel read','read','pages']])
        
        if self.NumberOfItems == 3:
            div, mod = divmod(self.number1+self.number2,3)
            self.number3 = random.randrange((div+2)*3,(div+8)*3,3) - self.number1 - self.number2
            self.average = (self.number1 + self.number2 + self.number3)/3
        elif self.NumberOfItems == 4:
            div, mod = divmod(self.number1+self.number2+self.number3,4)
            self.number4 = random.randrange((div+2)*4,(div+8)*4,4) - self.number1 - self.number2 - self.number3
            self.average = (self.number1 + self.number2 + self.number3+self.number4)/4
        else:
            div, mod = divmod(self.number1+self.number2+self.number3+self.number4,5)
            self.number5 = random.randrange((div+2)*5,(div+8)*5,5) - self.number1 - self.number2 - self.number3 - self.number4
            self.average = (self.number1 + self.number2 + self.number3+self.number4+self.number5)/5

        self.answer = self.average * self.NumberOfItems                               
        self.problem = "What is the total number of "+self.items[0]+" by "+self.name+" in "+str(self.NumberOfItems)+" days "
        self.problem = self.problem + "if she "+self.items[1]+" an average of "+str(self.average)+" "+self.items[2]+" per day?"
        
        self.item1 = "days"
        self.unit = self.items[2]
        
        self.problem_type = "ProblemTypeMCQ6"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 5
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+2))
        self.wrongAnswers.append(str(self.answer-2))
        self.wrongAnswers.append(str(self.average))

        self.answer = str(self.answer)           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.average,self.item1,self.items[0],self.NumberOfItems,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)   

    def GenerateProblemTypeMCQ7(self):
        '''e.g.:
        [Person.name] spent an average of $<amount> on <number> diferent [books]. Find the total cost of the [books].'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = float(randint(200,3000))/100
        self.number2 = float(randint(200,3000))/100
        self.number3 = float(randint(200,3000))/100
        self.number4 = float(randint(200,3000))/100
        self.number5 = float(randint(200,3000))/100
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice(['books','toys','pens','rolls of coloured strings','water bottles','soccer balls','keychains','bracelets','plants','lunchboxes'])
        
        if self.NumberOfItems == 3:
            self.average = round(float(self.number1 + self.number2 + self.number3)/3,2)            
        elif self.NumberOfItems == 4:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4)/4,2)
        else:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4+self.number5)/5,2)

        self.answer = round(self.average * self.NumberOfItems,2)

        if len(str(self.average).partition(".")[2])==1:
            self.average = str(self.average)+"0"                               
                             

        self.problem = self.name+" spent an average of $"+str(self.average)+" on "+str(self.NumberOfItems)+" different "+self.items+". Find the total cost of the "+self.items+"."
        
        self.item1 = self.items
        self.item2 = "spent"
        self.item3 = "cost"
        self.unit = ""
        self.dollar = "$"
        
        self.problem_type = "ProblemTypeMCQ7"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 5
        
        self.wrongAnswers = []
        for i in range(2):
            wrongAnswer = self.answer + (i+1)*0.05
            self.wrongAnswers.append(str(wrongAnswer))
        for i in range(2):
            wrongAnswer = self.answer - (i+1)*0.05
            self.wrongAnswers.append(str(wrongAnswer))

        self.wrongAnswers.append(self.average)

        if len(str(self.answer).partition(".")[2])==1:
            self.answer = str(self.answer)+"0"
        else:
            self.answer = str(self.answer)  
                                          
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.average,self.item1,self.item2,self.item3,self.NumberOfItems,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)   

    def GenerateProblemTypeMCQ8(self):
        '''e.g.:
        What is the total mass of <number> [packages] if their average mass is <decimal> kg?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = float(randint(2000,4000))/100
        self.number2 = float(randint(2000,4000))/100
        self.number3 = float(randint(2000,4000))/100
        self.number4 = float(randint(2000,4000))/100
        self.number5 = float(randint(2000,4000))/100
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice(['boys', 'girls', 'children', 'people', 'cartons', 'boxes', 'suitcases', 'sacks of sugar', 'sacks of rice'])
        
        if self.NumberOfItems == 3:
            self.average = round(float(self.number1 + self.number2 + self.number3)/3,2)            
        elif self.NumberOfItems == 4:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4)/4,2)
        else:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4+self.number5)/5,2)

        self.answer = round(self.average * self.NumberOfItems,2)

        if len(str(self.average).partition(".")[2])==1:
            self.average = str(self.average)+"0"                               

        self.problem = "What is the total mass of "+str(self.NumberOfItems)+" "+self.items+" if their average mass is "+str(self.average)+" kg?"
        
        self.item1 = self.items
        self.item2 = "mass"
        self.item3 = "mass"
        self.unit = "kg"
        self.dollar = ""
        
        self.problem_type = "ProblemTypeMCQ8"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 5
        
        self.wrongAnswers = []
        for i in range(2):
            wrongAnswer = self.answer + (i+1)*0.05
            self.wrongAnswers.append(str(wrongAnswer))
        for i in range(2):
            wrongAnswer = self.answer - (i+1)*0.05
            self.wrongAnswers.append(str(wrongAnswer))

        self.wrongAnswers.append(self.average)

        if len(str(self.answer).partition(".")[2])==1:
            self.answer = str(self.answer)+"0"
        else:
            self.answer = str(self.answer)  
                                          
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.average,self.item1,self.item2,self.item3,self.NumberOfItems,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)   

    def GenerateProblemTypeMCQ9a(self):
        '''e.g.:
        Find the total length of <number> [strips of ribbon] if their average length is <decimal> cm.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = float(randint(200,4000))/100
        self.number2 = float(randint(200,4000))/100
        self.number3 = float(randint(200,4000))/100
        self.number4 = float(randint(200,4000))/100
        self.number5 = float(randint(200,4000))/100
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice(['strips of ribbon','pieces of lace','strips of tape','pieces of wire','pieces of string','sticks','straws','twigs','pencils'])
        
        if self.NumberOfItems == 3:
            self.average = round(float(self.number1 + self.number2 + self.number3)/3,2)            
        elif self.NumberOfItems == 4:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4)/4,2)
        else:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4+self.number5)/5,2)

        self.answer = round(self.average * self.NumberOfItems,2)

        if len(str(self.average).partition(".")[2])==1:
            self.average = str(self.average)+"0"                               

        self.problem = "Find the total length of "+str(self.NumberOfItems)+" "+self.items+" if their average length is "+str(self.average)+" cm."
        
        self.item1 = self.items
        self.item2 = "length"
        self.item3 = "length"
        self.unit = "cm"
        self.dollar = ""
        
        self.problem_type = "ProblemTypeMCQ9a"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 5
        
        self.wrongAnswers = []
        for i in range(2):
            wrongAnswer = self.answer + (i+1)*0.05
            self.wrongAnswers.append(str(wrongAnswer))
        for i in range(2):
            wrongAnswer = self.answer - (i+1)*0.05
            self.wrongAnswers.append(str(wrongAnswer))

        self.wrongAnswers.append(self.average)

        if len(str(self.answer).partition(".")[2])==1:
            self.answer = str(self.answer)+"0"
        else:
            self.answer = str(self.answer)  
                                          
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.average,self.item1,self.item2,self.item3,self.NumberOfItems,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)   

    def GenerateProblemTypeMCQ9b(self):
        '''e.g.:
        What is the total length of <number> [pieces of fabric] if their average length is <decimal> m.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
                
        self.number1 = float(randint(200,4000))/100
        self.number2 = float(randint(200,4000))/100
        self.number3 = float(randint(200,4000))/100
        self.number4 = float(randint(200,4000))/100
        self.number5 = float(randint(200,4000))/100
        self.NumberOfItems = randint(3,5)
        self.name = random.choice(PersonName.PersonName)
        self.items = random.choice(['strips of cloth','pieces of ribbon','sheets of foil','sheets of wrapper','pieces of rope','pieces of cable','pieces of thread','poles','pipes','logs of wood'])
        
        if self.NumberOfItems == 3:
            self.average = round(float(self.number1 + self.number2 + self.number3)/3,2)            
        elif self.NumberOfItems == 4:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4)/4,2)
        else:
            self.average = round(float(self.number1 + self.number2 + self.number3+self.number4+self.number5)/5,2)

        self.answer = round(self.average * self.NumberOfItems,2)

        if len(str(self.average).partition(".")[2])==1:
            self.average = str(self.average)+"0"                               

        self.problem = "What is the total length of "+str(self.NumberOfItems)+" "+self.items+" if their average length is "+str(self.average)+" m."
        
        self.item1 = self.items
        self.item2 = "length"
        self.item3 = "length"
        self.unit = "m"
        self.dollar = ""
        
        self.problem_type = "ProblemTypeMCQ9b"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 1
        self.grade = 5
        
        self.wrongAnswers = []
        for i in range(2):
            wrongAnswer = self.answer + (i+1)*0.05
            self.wrongAnswers.append(str(wrongAnswer))
        for i in range(2):
            wrongAnswer = self.answer - (i+1)*0.05
            self.wrongAnswers.append(str(wrongAnswer))

        self.wrongAnswers.append(self.average)

        if len(str(self.answer).partition(".")[2])==1:
            self.answer = str(self.answer)+"0"
        else:
            self.answer = str(self.answer)  
                                          
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.average,self.item1,self.item2,self.item3,self.NumberOfItems,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)   

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
        if CheckAnswerType == 1:
            try:
                return (str(answer)==str(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswerType == 2:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False              