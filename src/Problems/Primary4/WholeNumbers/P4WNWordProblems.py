'''
Created on Aug 13, 2012
Module: P4WNWordProblems
Generates the "Whole Number Word Problems" problems for Primary 6

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
  

History:
  
'''
import random
from random import randint
from Problems import PersonName
import logging

class P4WNWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2a","ProblemType2b",],3:["ProblemType3",],
                            4:["ProblemType4",],5:["ProblemType5",],6:["ProblemType6",],
                            7:["ProblemType7",],8:["ProblemType8",],
                            }
        
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2a(),self.GenerateProblemType2b(),],3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],
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
        #return self.GenerateProblemType8()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2a":self.GenerateProblemType2a(),
                            "ProblemType2b":self.GenerateProblemType2b(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.name = random.choice(PersonName.PersonName)
        
        self.multiplier = random.randrange(100,600,50) 
        self.TotalMass =  self.multiplier * 9
        self.Fruits = [["watermelon",6*self.multiplier],["papaya",2*self.multiplier],["mango",self.multiplier]]
        self.RandomFruit = random.choice(self.Fruits)
        
        self.problem = self.name + " has a watermelon, a papaya and a mango. The mass of the watermelon is three times the mass of the papaya."
        self.problem = self.problem + " The mass of the mango is half the mass of the papaya. If the three fruits have a mass of "+str(self.TotalMass)
        self.problem = self.problem + " grams, what is the mass of the "+self.RandomFruit[0]+"?"
        self.problem = self.problem + " Express your answer in grams."
        
        self.answer = self.RandomFruit[1]
        self.CheckAnswerType = 1

        self.unit = "grams"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary-Grade-4/Whole-Numbers/Word-Problems#WP1' target='_blank'><u>Whole Numbers: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2a(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.names = random.sample(PersonName.BoyName,2)
        
        self.multiplier = randint(2,5) 
        self.LessMarbles = randint(30,100)
        self.MoreMarbles = self.multiplier * self.LessMarbles
        self.diff = self.MoreMarbles - self.LessMarbles
        
        self.problem = self.names[0] + " had "+str(self.diff)+" more marbles than "+self.names[1]+". "+self.names[0]+" had "+str(self.multiplier)+" times as many marbles as "+self.names[1]+"."
        self.problem = self.problem + " How many marbles had the two boys altogether?"
        
        self.answer = self.LessMarbles + self.MoreMarbles
        self.CheckAnswerType = 1

        self.unit = "marbles"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2a",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            
        
    def GenerateProblemType2b(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.names = random.sample(PersonName.BoyName,2)
        
        self.multiplier = random.choice([3,5]) 
        self.LessMarbles = randint(30,100)
        self.MoreMarbles = self.multiplier * self.LessMarbles
        self.diff = self.MoreMarbles - self.LessMarbles
        
        self.problem = self.names[0] + " had "+str(self.diff)+" more marbles than "+self.names[1]+". "+self.names[0]+" had "+str(self.multiplier)+" times as many marbles as "+self.names[1]+". "
        self.problem = self.problem + self.names[0]+" gave some marbles to "+self.names[1]+". In the end, the two boys had an equal number of marbles."
        self.problem = self.problem + " How many marbles did "+self.names[0]+" give to "+self.names[1]+"?"
        
        self.answer = self.diff / 2
        self.CheckAnswerType = 1

        self.unit = "marbles"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2b",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType2(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary-Grade-4/Whole-Numbers/Word-Problems#WP2' target='_blank'><u>Whole Numbers: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.Group1 = ["adults", "children"]
        self.Group2 = ["girls", "boys"]

        '''trying to randomize among more adults than children and vice versa..similarly more girls than boys'''
        self.RandomIndexGroup1 = [0,1]
        self.RandomIndexGroup2 = [0,1]
        
        random.shuffle(self.RandomIndexGroup1)
        random.shuffle(self.RandomIndexGroup2)
                        
        self.more1 = randint(150,500)
        self.number1 = randint(600,1000)
        self.number2 = self.more1 + self.number1
        
        if self.RandomIndexGroup1[0] == 1:
            self.number3 = randint(2,4) * self.number2 / 10
            self.number4 = self.number2 - self.number3
        else:
            self.number3 = randint(2,4) * self.number1 / 10
            self.number4 = self.number1 - self.number3
        
        self.more2 = self.number4 - self.number3
        
        self.total = self.number1 + self.number2
            
        self.problem = str(self.total)+" people went to watch a 3D movie. There were "+str(self.more1)+" more "+self.Group1[self.RandomIndexGroup1[0]]
        self.problem = self.problem + " than "+self.Group1[self.RandomIndexGroup1[1]]+". If there were "+str(self.more2)+" more "+self.Group2[self.RandomIndexGroup2[0]]
        self.problem = self.problem + " than "+self.Group2[self.RandomIndexGroup2[1]]+", how many "
        
        if randint(1,2)==1:
            self.problem = self.problem + self.Group2[self.RandomIndexGroup2[1]] + " went to watch the movie?"
            self.answer = self.number3
            self.unit = self.Group2[self.RandomIndexGroup2[1]]
        else:
            self.problem = self.problem + self.Group2[self.RandomIndexGroup2[0]] + " went to watch the movie?"
            self.answer = self.number4
            self.unit = self.Group2[self.RandomIndexGroup2[0]]

        self.CheckAnswerType = 1

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType3(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary-Grade-4/Whole-Numbers/Word-Problems#WP3' target='_blank'><u>Whole Numbers: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.EachPacket = randint(5,10)
        self.EachCarton = randint(20,100)
        self.NumberOfCarton = randint(3,6)
        self.total = self.NumberOfCarton * self.EachCarton * self.EachPacket
        
        self.problem =  str(self.NumberOfCarton)+" cartons have "+str(self.total)+" crayons altogether. "
        self.problem = self.problem + "Each carton has an equal number of packets. "
        self.problem = self.problem + "Each packet contains "+str(self.EachPacket)+" crayons. "
        self.problem = self.problem + "Find the number of packets in each carton."
        
        self.answer = self.EachCarton
        self.unit = "packets"

        self.CheckAnswerType = 1

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType4(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 4 at <a href='/Learn/Primary-Grade-4/Whole-Numbers/Word-Problems#WP4' target='_blank'><u>Whole Numbers: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType5(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.EachDay = randint(30,100)
        self.himself = randint(3,10)
        self.fruit = random.choice(["apples","oranges","mangoes","papayas","watermelons"])
        
        self.Months = {"January":31,"March":31,"April":30,"May":31,"June":30,"July":31,
                  "August":31,"September":30,"October":31,"November":30,"December":31}
        
        self.month = random.choice(self.Months.keys())
        self.days = self.Months[self.month]
        
        self.problem =  "A farmer picks "+str(self.EachDay)+" kg of "+self.fruit+" a day. "
        self.problem = self.problem + "He keeps "+str(self.himself)+" kg of "+self.fruit+" for himself each day and sells the rest. "
        self.problem = self.problem + "Find the mass of "+self.fruit+" he will sell in "+self.month+"."
        
        self.answer = (self.EachDay-self.himself) * self.days
        self.unit = "kg"

        self.CheckAnswerType = 1

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType5(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 5 at <a href='/Learn/Primary-Grade-4/Whole-Numbers/Word-Problems#WP5' target='_blank'><u>Whole Numbers: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType6(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.GirlName,3) 
        
        self.tennis = randint(50,150)
        self.ball = randint(2,10)
        
        self.number1 = randint(2,3)
        
        self.BallNumbers = random.sample([4,5,6],2)
        self.BallNumber1 = self.BallNumbers[0]
        self.BallNumber2 = self.BallNumbers[1]
        
        self.BallNumber3 = randint(7,10)
                
        self.problem = self.names[0]+", "+self.names[1]+" and "+self.names[2]+" went to a sports shop and bought similar tennis paraphernalia. "
        self.problem = self.problem + self.names[0]+" paid $"+str(self.number1*self.tennis+self.BallNumber1*self.ball)+" for "+str(self.number1)+" tennis rackets and "+str(self.BallNumber1)+" tennis balls. "
        self.problem = self.problem + self.names[1]+" paid $"+str(self.number1*self.tennis+self.BallNumber2*self.ball)+" for "+str(self.number1)+" tennis rackets and "+str(self.BallNumber2)+" tennis balls. "
        self.problem = self.problem + "If "+self.names[2]+" bought "+str(self.BallNumber3)+" tennis balls, how much did she pay?"
        
        self.answer = self.BallNumber3 * self.ball
        
        self.unit = ""
        self.dollar = "$"

        self.CheckAnswerType = 1

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                "dollar_unit":self.dollar}            

    def ExplainType6(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 6 at <a href='/Learn/Primary-Grade-4/Whole-Numbers/Word-Problems#WP6' target='_blank'><u>Whole Numbers: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType7(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName) 
        
        self.CushionCloth = randint(1,3)
        self.CurtainCloth = randint(2,4) * self.CushionCloth
        
        self.Curtains = randint(2,4)
        self.Cushions = randint(4,8)

        self.total = self.CurtainCloth*self.Curtains + self.CushionCloth*self.Cushions
                                
        self.problem = self.name + " used "+str(self.total)+" m of cloth to make "+str(self.Curtains)+" similar curtains and "+str(self.Cushions)+" similar cushion covers. "
        if randint(1,2)==1:
            self.problem = self.problem + "She used "+str(self.CurtainCloth)+" m of cloth to make each curtain. "
            self.problem = self.problem + "How much cloth did she use to make each cushion cover?"
            self.answer = self.CushionCloth
        else:
            self.problem = self.problem + "She used "+str(self.CushionCloth)+" m of cloth to make each cushion cover. "
            self.problem = self.problem + "How much cloth did she use to make each curtain?"
            self.answer = self.CurtainCloth
        
        self.unit = "m"
        self.dollar = ""

        self.CheckAnswerType = 1

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                "dollar_unit":self.dollar}            

    def ExplainType7(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 7 at <a href='/Learn/Primary-Grade-4/Whole-Numbers/Word-Problems#WP7' target='_blank'><u>Whole Numbers: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType8(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.PersonName,2)
        
        self.times = randint(2,4)
        self.multiplier = randint (20,50)
        
        self.total = (self.times + 1) * self.multiplier
        self.given = randint(2,5) * self.multiplier / 10
                                
        self.problem = self.names[0]+" and "+self.names[1]+" had "+str(self.total)+" paper clips altogether. "
        self.problem = self.problem + self.names[0]+" gave away "+str(self.given)+" paper clips to "+self.names[1]+". "
        self.problem = self.problem + "In the end, "+self.names[0]+" had "+str(self.times)+" times as many paper clips as "+self.names[1]+". "
        
        self.flag = randint(1,4)
        if self.flag==1:
            self.problem = self.problem + "How many paper clips did "+self.names[0]+" have in the end?"
            self.answer = self.times * self.multiplier
        elif self.flag==2:
            self.problem = self.problem + "How many paper clips did "+self.names[1]+" have in the end?"
            self.answer = self.multiplier
        elif self.flag==3:
            self.problem = self.problem + "How many paper clips did "+self.names[0]+" have in the beginning?"
            self.answer = self.times * self.multiplier + self.given
        elif self.flag==4:
            self.problem = self.problem + "How many paper clips did "+self.names[1]+" have in the beginning?"
            self.answer = self.multiplier - self.given
        
        self.unit = "paper clips"
        self.dollar = ""

        self.CheckAnswerType = 1

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.unit,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                "dollar_unit":self.dollar}            

    def ExplainType8(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 8 at <a href='/Learn/Primary-Grade-4/Whole-Numbers/Word-Problems#WP8' target='_blank'><u>Whole Numbers: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False                                  