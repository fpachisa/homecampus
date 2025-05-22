'''
Created on Sep 11, 2012
Module: P4DCWordProblems
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

class P4DCWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1a","ProblemType1b",],2:["ProblemType2",],3:["ProblemType3",],
                            4:["ProblemType4a","ProblemType4b",],5:["ProblemType5",],6:["ProblemType6",],
                            7:["ProblemType7",],8:["ProblemType8",],9:["ProblemType9",],
                            }
        
        self.GenerateProblemType = {1:[self.GenerateProblemType1a(),self.GenerateProblemType1b(),],2:[self.GenerateProblemType2(),],3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4a(),self.GenerateProblemType4b(),],5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],9:[self.GenerateProblemType9(),],
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
        #return self.GenerateProblemType6()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1a":self.GenerateProblemType1a(),
                            "ProblemType1b":self.GenerateProblemType1b(),
                            "ProblemType2":self.GenerateProblemType2(),                           
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4a":self.GenerateProblemType4a(),
                            "ProblemType4b":self.GenerateProblemType4b(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1a(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.names = random.sample(PersonName.GirlName,2)
        
        self.milk1 = float(random.randrange(10,95,5))/100
        self.milk2 = float(random.randrange(10,95,5))/100
        self.juice1 = float(random.randrange(10,95,5))/100
        self.juice2 = float(random.randrange(10,95,5))/100
        
        self.problem = self.names[0]+" bought "+str(self.milk1)+" litre of milk and "+str(self.juice1)+" litre of juice. "
        self.problem = self.problem + self.names[1]+" bought "+str(self.milk2)+" litre of milk and "+str(self.juice2)+" litre of juice. "
        self.problem = self.problem + " How many litres of beverages did the two girls buy altogether?"
        
        self.answer = self.milk1 + self.milk2 + self.juice1 + self.juice2
        self.CheckAnswerType = 1

        self.unit = "litres"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1a",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            
        
    def GenerateProblemType1b(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.names = random.sample(PersonName.GirlName,2)
        
        self.milk1 = float(random.randrange(10,95,5))/100
        self.milk2 = float(random.randrange(10,95,5))/100
        self.juice1 = float(random.randrange(10,95,5))/100
        self.juice2 = float(random.randrange(10,95,5))/100
        
        if (self.milk1 + self.juice1) == (self.milk2 + self.juice2):
            self.milk1 = self.milk1 + 0.5
        
        self.problem = self.names[0]+" bought "+str(self.milk1)+" litre of milk and "+str(self.juice1)+" litre of juice. "
        self.problem = self.problem + self.names[1]+" bought "+str(self.milk2)+" litre of milk and "+str(self.juice2)+" litre of juice. "
        if (self.milk1 + self.juice1) > (self.milk2 + self.juice2):
            self.problem = self.problem + " How many more litres of beverages did "+self.names[0]+" buy than "+self.names[1]+"?"
            self.answer = (self.milk1 + self.juice1) - (self.milk2 + self.juice2)
        else:
            self.problem = self.problem + " How many more litres of beverages did "+self.names[1]+" buy than "+self.names[0]+"?"
            self.answer = (self.milk2 + self.juice2) - (self.milk1 + self.juice1)

        self.CheckAnswerType = 1

        self.unit = "litres"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1b",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary-Grade-4/Decimal/Word-Problems#WP1' target='_blank'><u>Decimals: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.swim = random.randrange(500,900,50)
        self.run = round(float(randint(30,60))/10,1)
        self.cycle = round(float(randint(70,130))/10,1)
                
        self.problem = "In a certain competition, the participants had to swim a distance of "+str(self.swim)+" m, "
        self.problem = self.problem + "run a distance of "+str(self.run)+" km and cycle a distance of "+str(self.cycle)+" km. "
        self.problem = self.problem + "What was the total distance a participant had to cover? Give your answer in km."
                    
        self.answer = round(float(self.swim)/1000 + self.run + self.cycle,2) 

        self.CheckAnswerType = 1

        self.unit = "km"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType2(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary-Grade-4/Decimal/Word-Problems#WP2' target='_blank'><u>Decimals: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.names = random.sample(PersonName.BoyName,2)
        
        self.height1 = randint(140,200)
        self.height2 = randint(140,200)
        if self.height1 == self.height2:
            self.height1 = self.height2 + 10
        
        self.diff = abs(self.height1-self.height2)
        self.height1 = round(float(self.height1)/100,2)
        self.height2 = round(float(self.height2)/100,2)
                
        self.problem = self.names[0]+" is "+str(self.height1)+" m tall. "
        if self.height1 > self.height2:
            self.problem = self.problem + self.names[1]+" is "+str(self.diff)+" cm shorter than "+self.names[0]+"."
        else:
            self.problem = self.problem + self.names[1]+" is "+str(self.diff)+" cm taller than "+self.names[0]+"."
        
        self.problem = self.problem + " How tall is "+self.names[1]+"?"
        
        self.answer = self.height2 

        self.CheckAnswerType = 1

        self.unit = "m"
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
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary-Grade-4/Decimal/Word-Problems#WP3' target='_blank'><u>Decimals: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType4a(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.names = random.sample(PersonName.BoyName,2)
        
        self.weight = round(float(randint(110,300))/100,2)
        self.multiplier = {2:"twice",3:"thrice"}
        self.key = random.choice(self.multiplier.keys())
        self.value = self.multiplier[self.key]
                
        self.problem = self.names[0]+" and "+self.names[1]+" went to a strawberry farm. "
        self.problem = self.problem + self.names[0]+" picked "+str(self.weight)+" kg of strawberries. "
        self.problem = self.problem + self.names[1]+" picked "+self.value+" as much strawberries as "+self.names[0]+". "
        self.problem = self.problem + "Find the mass of the strawberries that "+self.names[1]+" picked."
        
        self.answer = self.weight * self.key

        self.CheckAnswerType = 1

        self.unit = "kg"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4a",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            
        
    def GenerateProblemType4b(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.names = random.sample(PersonName.BoyName,2)
        
        self.weight = round(float(randint(110,300))/100,2)
        self.multiplier = {2:"twice",3:"thrice"}
        self.key = random.choice(self.multiplier.keys())
        self.value = self.multiplier[self.key]
                
        self.problem = self.names[0]+" and "+self.names[1]+" went to a strawberry farm. "
        self.problem = self.problem + self.names[0]+" picked "+str(self.weight)+" kg of strawberries. "
        self.problem = self.problem + self.names[1]+" picked "+self.value+" as much strawberries as "+self.names[0]+". "
        self.problem = self.problem + "Find the mass of the strawberries that the two boys picked altogether."
        
        self.answer = self.weight * (1+self.key)

        self.CheckAnswerType = 1

        self.unit = "kg"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4b",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType4(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 4 at <a href='/Learn/Primary-Grade-4/Decimal/Word-Problems#WP4' target='_blank'><u>Decimals: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType5(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.length = random.randrange(2,10,2)
        self.breadth = round(float(random.randrange(15,75,10))/10,1)
        self.area = int(self.length * self.breadth)
                
        self.problem = "The area of a rectangle is "+str(self.area)+" cm<sup>2</sup>. If the length of the rectangle is "+str(self.length)+" cm, "
        self.problem = self.problem + "what is its breadth?"
        
        self.answer = self.breadth

        self.CheckAnswerType = 2

        self.unit = "cm"
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
        self.solution_text = "For detailed explanation refer to Word Problem 5 at <a href='/Learn/Primary-Grade-4/Decimal/Word-Problems#WP5' target='_blank'><u>Decimals: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType6(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3

        self.weight = round(float(randint(30,70))/100,2)
        self.number1 = randint(4,7)
        self.number2 = randint(5,9)
        
        if self.number1 == self.number2:
            self.number2 = self.number1 + 1
        
        self.total = self.weight * self.number1
        
        self.problem = "The mass of "+str(self.number1)+" identical paper weights is "+str(self.total)+" kg. "
        self.problem = self.problem + "Find the mass of "+str(self.number2)+" such paper weights. Round off your answer to the nearest kilogram."
        
        self.answer = int(round(self.weight*self.number2,0))

        self.CheckAnswerType = 3

        self.unit = "kg"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType6(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 6 at <a href='/Learn/Primary-Grade-4/Decimal/Word-Problems#WP6' target='_blank'><u>Decimals: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType7(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.PersonName)

        self.cost1 = round(float(random.randrange(110,290,5))/100,2)
        self.cost2 = round(float(random.randrange(310,590,5))/100,2)
        
        self.number1 = randint(3,6)
        
        self.total = self.cost1 + self.cost2*self.number1
        
        self.problem = self.name+" paid $"+str(self.total)+" for a bottle of orange juice and "+str(self.number1)+" packets of cake mix. "
        self.problem = self.problem + "The bottle of orange juice cost $"+str(self.cost1)+". How much did each packet of cake mix cost?"
        
        self.answer = self.cost2

        self.CheckAnswerType = 1

        self.unit = ""
        self.dollar_unit = "$"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'dollar_unit':self.dollar_unit}            

    def ExplainType7(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 7 at <a href='/Learn/Primary-Grade-4/Decimal/Word-Problems#WP7' target='_blank'><u>Decimals: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType8(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)

        self.cost1 = round(float(random.randrange(115,295,10))/100,2)
        
        self.more = random.randrange(15,45,5)
        self.less = random.randrange(15,45,5)
        
        self.number1 = randint(3,15)
        
        self.problem = "Shop A, Shop B and Shop C sell roses. Shop A sells one rose for $"+str(self.cost1)+". "
        self.problem = self.problem + "Shop B sells it for "+str(self.more)+" &cent; more than Shop A and "+str(self.less)+" &cent; less than Shop C. "
        self.problem = self.problem + "If "+self.name+" bought "+str(self.number1)+" roses from Shop C, how much did she spend?"
        
        self.answer = self.number1 * (self.cost1+round(float(self.more)/100,2)+round(float(self.less)/100,2))
        
        '''adding extra 0 to make it 2 decimals'''
        if len(str(self.answer).partition(".")[2])==1:
            self.answer = str(self.answer)+"0"

        self.CheckAnswerType = 1

        self.unit = ""
        self.dollar_unit = "$"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'dollar_unit':self.dollar_unit}            

    def ExplainType8(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 8 at <a href='/Learn/Primary-Grade-4/Decimal/Word-Problems#WP8' target='_blank'><u>Decimals: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType9(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.cost1 = round(float(random.randrange(115,395,10))/100,2)
        
        self.number1 = randint(4,8)
        self.number2 = randint(10,50)
        self.number3 = randint(10,30)
        
        self.total = self.number1*self.number2 + self.number3 
        
        self.fruit = random.choice(["apples","oranges","mangoes","peaches"])
        
        self.problem = "A fruiterer had "+str(self.total)+" "+self.fruit+". After keeping "+str(self.number3)+" "+self.fruit+" for himself, "
        self.problem = self.problem + " he packed the remaining "+self.fruit+" in bags of "+str(self.number1)+". If he sold each bag at $"
        self.problem = self.problem + str(self.cost1)+", how much money did he collect?"
        
        self.answer = self.number2 * self.cost1
        
        '''adding extra 0 to make it 2 decimals'''
        if len(str(self.answer).partition(".")[2])==1:
            self.answer = str(self.answer)+"0"

        self.CheckAnswerType = 1

        self.unit = ""
        self.dollar_unit = "$"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType9",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'dollar_unit':self.dollar_unit}            

    def ExplainType9(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 9 at <a href='/Learn/Primary-Grade-4/Decimal/Word-Problems#WP9' target='_blank'><u>Decimals: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return round(float(answer),2)==float(InputAnswer)
            except ValueError:
                return False
        elif CheckAnswer==2:
            try:
                return round(float(answer),1)==float(InputAnswer)
            except ValueError:
                return False
        elif CheckAnswer==3:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False                                                           