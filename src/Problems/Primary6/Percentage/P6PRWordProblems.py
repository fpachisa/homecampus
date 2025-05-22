'''
Created on May 09, 2012
Module: P6PRWordProblems
Generates the "Percentage Word Problems" problems for Primary 6

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
from Utils import LcmGcf
from Problems import PersonName


class P6PRWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],
                            4:["ProblemType4",],5:["ProblemType5",],6:["ProblemType6",],
                            7:["ProblemType7",],8:["ProblemType8",],9:["ProblemType9",],
                            10:["ProblemType10",],11:["ProblemType11",],12:["ProblemType12",],
                            13:["ProblemType13",],14:["ProblemType14",],15:["ProblemType15",],
                            16:["ProblemType16",],17:["ProblemType17",],18:["ProblemType18",],
                            
                            }
        
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],9:[self.GenerateProblemType9(),],
                                    10:[self.GenerateProblemType10(),],11:[self.GenerateProblemType11(),],12:[self.GenerateProblemType12(),],
                                    13:[self.GenerateProblemType13(),],14:[self.GenerateProblemType14(),],15:[self.GenerateProblemType15(),],
                                    16:[self.GenerateProblemType16(),],17:[self.GenerateProblemType17(),],18:[self.GenerateProblemType18(),],
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
        #return self.GenerateProblemType15()
        
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
                            "ProblemType12":self.GenerateProblemType12(),
                            "ProblemType13":self.GenerateProblemType13(),
                            "ProblemType14":self.GenerateProblemType14(),
                            "ProblemType15":self.GenerateProblemType15(),
                            "ProblemType16":self.GenerateProblemType16(),
                            "ProblemType17":self.GenerateProblemType17(),
                            "ProblemType18":self.GenerateProblemType18(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g: In an auto show, 42.5% of the cars are used cars. 
        Given that 714 cars are used cars, what is the total number of cars in the show?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        ''' using pre-defined decimals so that the multiplication of these two gives 00 at the end'''
        self.decimals = random.choice([[20,5],[25,4],[25,8],[50,4],[60,5],[80,5]])
        
        self.percentage = str(randint(1,5))+str(self.decimals[0])[0]+"."+str(self.decimals[0])[1]
        if round(float(self.percentage),0)==float(self.percentage):
            self.percentage = int(float(self.percentage))
        self.multiplier = str(random.randrange(10,30,2))+"."+str(self.decimals[1])
        self.UsedCars = int(float(self.percentage)*float(self.multiplier))

        self.problem = "In an auto show, "+str(self.percentage)+"% of the cars are used cars."
        self.problem = self.problem + " Given that "+str(self.UsedCars)+" cars are used cars, what is the total number of cars in the show?"

        self.answer = int(self.UsedCars*100/float(self.percentage))
        self.CheckAnswerType = 1

        self.unit = "cars"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Percentage/Finding-Whole-Given-Part-and-Percentage#WP1' target='_blank'><u>Finding Whole Given Part and Percentage</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g: Emily was 32 cm taller than Chloe. If Emily stood at 125% of Chloe's height, how tall was Emily? '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.names = random.sample(PersonName.PersonName,2)
        self.decimals = random.choice([[20,5],[25,4],[25,8]])
        
        self.height = str(randint(11,13))+str(self.decimals[1])
        self.percentage = 100+self.decimals[0]
        self.diff = (int(self.percentage)-100)*int(self.height) / 100
        
        self.problem = self.names[0]+" was "+str(self.diff)+" cm taller than "+self.names[1]+". If "+self.names[0]+" stood at "+str(self.percentage)+"% of "+self.names[1]+"'s height, how tall was "+self.names[0]+"?"

        self.answer = int(self.height) + self.diff
        
        self.CheckAnswerType = 1

        self.unit = "cm"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType2(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Percentage/Finding-Whole-Given-Part-and-Percentage#WP2' target='_blank'><u>Finding Whole Given Part and Percentage</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g: After a 15% service tax, Lisa's restaurant bill was $41.40. Find the amount of service tax she paid.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.gender = random.choice([[random.choice(PersonName.GirlName),"she"],[random.choice(PersonName.BoyName),"he"]])
        
        self.percentage = randint(5,15)
        self.percentage1 = 100+self.percentage
        self.bill = float(random.randrange(self.percentage1*40,self.percentage1*100,self.percentage1))/100
        
        self.problem = "After a "+str(self.percentage)+"% service tax, "+self.gender[0]+"'s restaurant bill was $"+str(self.bill)+". Find the amount of service tax "+self.gender[1]+" paid."

        self.answer = self.bill * (self.percentage1 - 100) / self.percentage1
        
        self.CheckAnswerType = 2

        self.unit = ""
        self.dollar_unit = "$"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType3(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Percentage/Finding-Whole-Given-Part-and-Percentage#WP3' target='_blank'><u>Finding Whole Given Part and Percentage</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g: Emma painted 1/8 of her 40 keyrings red, 30% of them blue and the rest of them green. How many keyrings did she paint green?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.name = random.choice(PersonName.GirlName)
        
        self.numbers = random.choice([[2,[random.choice([20,30,40,50]),random.choice([10,20,30,40])]],
                                     [3,random.choice([[12,25],[15,40],[30,20]])],
                                     [4,random.choice([[20,random.choice([10,20,30,40,50])],[12,25]])],
                                     [5,random.choice([[20,random.choice([10,20,30,40,50])],[25,40],[30,random.choice([10,20,30,40,50])],[40,random.choice([10,20,30,40,50])]])],
                                     [6,random.choice([[30,random.choice([10,20,30,40,50])],[24,25]])],
                                     [8,random.choice([[40,30],[32,25]])]
                                    ])
        
        self.problem = self.name+" painted 1/"+str(self.numbers[0])+" of her "+str(self.numbers[1][0])+" keyrings red, "+str(self.numbers[1][1])+"% of them blue and the rest of them green. How many keyrings did she paint green?"

        self.answer = self.numbers[1][0] - (self.numbers[1][0]/self.numbers[0]) - (self.numbers[1][1]*self.numbers[1][0]/100)
        
        self.CheckAnswerType = 1

        self.unit = "green keyrings"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType4(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 4 at <a href='/Learn/Primary6/Percentage/Finding-Whole-Given-Part-and-Percentage#WP4' target='_blank'><u>Finding Whole Given Part and Percentage</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType5(self):
        '''e.g: Michael had a collection of hip-hop, rock and jazz music songs. He had 168 hip-hop songs. 
                Hip-hop and rock made 70% of his collection. For every 3 hip-hop songs in his collection he had 5 rock songs. 
                How many songs did he have in his collection?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.name = random.choice(PersonName.BoyName)
        
        self.number1 = randint(5,9)
        self.number2 = randint(4,8)
        self.multiplier = LcmGcf.LcmGcf().find_lcm(self.number1, self.number2)
        self.HipHopRock = random.randrange(self.multiplier*2,200,self.multiplier)
        
        self.ratio1 = randint(25*self.number1,75*self.number1)/100
        self.ratio2 = self.number1 - self.ratio1
        
        self.HipHop = self.ratio1*self.HipHopRock/self.number1
        
        self.problem = self.name+" had a collection of hip-hop, rock and jazz music songs. He had "+str(self.HipHop)+" hip-hop songs."
        self.problem = self.problem + " Hip-hop and rock made "+str(self.number2*10)+"% of his collection. For every "+str(self.ratio1)+" hip-hop songs in his collection he had "+str(self.ratio2)+" rock songs."
        self.problem = self.problem + " How many songs did he have in his collection?" 
        
        self.answer = self.HipHopRock*10/self.number2
        
        self.CheckAnswerType = 1

        self.unit = "songs"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType5(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 5 at <a href='/Learn/Primary6/Percentage/Finding-Whole-Given-Part-and-Percentage#WP5' target='_blank'><u>Finding Whole Given Part and Percentage</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType6(self):
        '''e.g: Lisa's salary was raised from $4000 to $4800 per month. What was the percentage increase in her monthly salary?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.gender = random.choice([[random.choice(PersonName.BoyName),"his"],[random.choice(PersonName.GirlName),"her"]])
        self.InitialSalary = random.randrange(4000,10000,100)
        self.PercentIncrease = randint(5,20)
        self.FinalSalary = (100+self.PercentIncrease) * self.InitialSalary / 100
        self.problem = self.gender[0]+"'s salary was raised from $"+str(self.InitialSalary)+" to $"+str(self.FinalSalary)+" per month. What was the percentage increase in "+self.gender[1]+" monthly salary?"
        
        self.answer = self.PercentIncrease
        
        self.CheckAnswerType = 1

        self.unit = "%"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType6(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Percentage/Finding-Percentage-Increase-Decrease#WP1' target='_blank'><u>Finding Percentage Increase Decrease</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType7(self):
        '''e.g: The price of a chair was reduced from $270 to $189 in a sale. Find the percentage discount on the chair.'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.InitialPrice = random.randrange(100,300,10)
        self.PercentDecrease = random.randrange(10,40,10)
        self.FinalPrice = self.InitialPrice - (self.InitialPrice*self.PercentDecrease/100)

        self.problem = "The price of a chair was reduced from $"+str(self.InitialPrice)+" to $"+str(self.FinalPrice)+" in a sale. Find the percentage discount on the chair."
        
        self.answer = self.PercentDecrease
        
        self.CheckAnswerType = 1

        self.unit = "%"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType7(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Percentage/Finding-Percentage-Increase-Decrease#WP2' target='_blank'><u>Finding Percentage Increase Decrease</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType8(self):
        '''e.g: Joey had a leaky water bottle that leaked 15 ml of water every 10 minutes. 
            What was the percentage decrease in the water in the bottle 1 hour after the bottle was filled up to 450 ml?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.name = random.choice(PersonName.PersonName)
        self.leak = random.randrange(5,30,5)
        self.leak1 = self.leak * 60 / 10
        self.percentage = random.choice([10,20,25,40,50])
        self.total = self.leak1 * 100 / self.percentage

        self.problem = self.name+" had a leaky water bottle that leaked "+str(self.leak)+" ml of water every 10 minutes. "
        self.problem = self.problem + "What was the percentage decrease in the water in the bottle 1 hour after the bottle was filled up to "+str(self.total)+" ml?"
        
        self.answer = self.percentage
        
        self.CheckAnswerType = 1

        self.unit = "%"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType8(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Percentage/Finding-Percentage-Increase-Decrease#WP3' target='_blank'><u>Finding Percentage Increase Decrease</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType9(self):
        '''e.g: Due to some roadworks on the usual route from home to school, Peggy has to take another route to school which is 7% longer. 
        This increase in distance is 126 m. What is the length of the new route?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.name = random.choice(PersonName.PersonName)

        self.PercentIncrease = randint(5,15)
        self.multiplier = randint(5,20)
        self.DistanceIncrease = self.multiplier * self.PercentIncrease
        self.NewDistance = self.multiplier * (100 + self.PercentIncrease)
        
        self.problem = "Due to some roadworks on the usual route from home to school, "+self.name+" has to take another route to school which is "+str(self.PercentIncrease)+"% longer."
        self.problem = self.problem + " This increase in distance is "+str(self.DistanceIncrease)+" m. What is the length of the new route?"
        
        self.answer = self.NewDistance
        
        self.CheckAnswerType = 1

        self.unit = "m"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType9",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType9(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 4 at <a href='/Learn/Primary6/Percentage/Finding-Percentage-Increase-Decrease#WP4' target='_blank'><u>Finding Percentage Increase Decrease</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType10(self):
        '''e.g: Sue bought a piece of cloth 140 cm long. After washing it, the cloth shrank by 4% along its length. 
        What is the length of the cloth now?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.name = random.choice(PersonName.GirlName)

        self.PercentDecrease = randint(3,20)
        self.OldLength = random.randrange(50,300,10)
        self.NewLength = float(100-self.PercentDecrease) * self.OldLength / 100 
        
        self.problem = self.name+" bought a piece of cloth "+str(self.OldLength)+" cm long. After washing it, the cloth shrank by "+str(self.PercentDecrease)+"% along its length."
        self.problem = self.problem + " What is the length of the cloth now?"
        
        self.answer = self.NewLength
        
        self.CheckAnswerType = 2

        self.unit = "cm"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType10",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType10(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 5 at <a href='/Learn/Primary6/Percentage/Finding-Percentage-Increase-Decrease#WP5' target='_blank'><u>Finding Percentage Increase Decrease</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType11(self):
        '''e.g: Justin bought a T-shirt at 12% off and received an additional membership discount of $7. 
                If the T-shirt cost him $15, what was the original price of the T-shirt?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.name = random.choice(PersonName.BoyName)

        self.cost = randint(5,15)
        self.discount = randint(20,50) * self.cost / 100
        self.percentage = 100 - (self.cost + self.discount)*random.choice([2,4])
        
        self.problem = self.name+" bought a T-shirt at "+str(self.percentage)+"% off and received an additional membership discount of $"+str(self.discount)+"."
        self.problem = self.problem + " If the T-shirt cost him $"+str(self.cost)+", what was the original price of the T-shirt?"
        
        self.answer = (self.cost+self.discount) * 100 / (100-self.percentage)
        
        self.CheckAnswerType = 1

        self.unit = ""
        self.dollar_unit = "$"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType11",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType11(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Percentage/Advanced-Word-Problems#WP1' target='_blank'><u>Percentage - Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType12(self):
        '''e.g: 40% of the 7920 visitors to an amusement park were children. 25% of the children and 1/3 of the adults were repeat visitors. How many percent of
                the visitors were visiting the amusement park for the first time?'''
        
        self.complexity_level = "difficult"
        self.HCScore = 7

        self.numbers = random.choice([[40,25,random.choice([3,5,6,12])],[50,20,random.choice([5,10])],
                                      [25,40,random.choice([3,5,6,12])],[20,50,random.choice([5,10])]
                                     ])
        
        self.total = random.randrange(3000,8000,10)
                
        self.problem = str(self.numbers[0])+"% of the "+str(self.total)+" visitors to an amusement park were children. "+str(self.numbers[1])+"% of the"
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>children and&nbsp;</td><td style='text-align:center'><u>"+"&nbsp;"*len(str(self.numbers[2]))+"1"+"&nbsp;"*len(str(self.numbers[2]))+"</u><br />"+str(self.numbers[2])+"</td><td>&nbsp;of the adults were repeat visitors. How many percent of</td></tr></table>"
        self.problem = self.problem + "the visitors were visiting the amusement park for the first time?"
        
        self.children1 = self.numbers[0]*self.total/100
        self.adult1 = self.total - self.children1
        self.children2 = self.numbers[1]*self.children1/100
        self.adult2 = self.adult1/self.numbers[2]
        self.repeat = self.children2+self.adult2
        self.FirstTime = self.total - self.repeat 
        
        self.answer = (self.FirstTime)*100/self.total
        
        self.CheckAnswerType = 1

        self.unit = "% first time visitors"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType12",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType12(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Percentage/Advanced-Word-Problems#WP2' target='_blank'><u>Percentage - Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType13(self):
        '''e.g: Sarah had 55 cards. She gave 20% of them to her sister, 25% of the remaining to her brother and the rest to her best friend. 
                How many percent of the cards did she give to her best friend?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.gender = random.choice([[random.choice(PersonName.GirlName),"She","her","she"],[random.choice(PersonName.BoyName),"He","his","he"]])
                
        self.numbers = random.choice([[20,25,random.randrange(15,60,5)],[50,20,random.randrange(20,60,10)],
                                      [75,40,random.randrange(20,80,20)],[25,random.choice([40,80]),random.randrange(20,80,20)]
                                     ])

        self.problem = self.gender[0]+" had "+str(self.numbers[2])+" cards. "+self.gender[1]+" gave "+str(self.numbers[0])+"% of them to "+self.gender[2]+" sister, "+str(self.numbers[1])+"% of the remaining to "+self.gender[2]+" brother and the rest to "+self.gender[2]+" best friend."
        self.problem = self.problem + " How many percent of the cards did "+self.gender[3]+" give to "+self.gender[2]+" best friend?"
        
        self.sister = self.numbers[0]*self.numbers[2]/100
        self.brother = self.numbers[1]*(self.numbers[2] - self.sister)/100
        
        self.answer = (self.numbers[2]-self.sister-self.brother)*100/self.numbers[2] 
        
        self.CheckAnswerType = 1

        self.unit = "%"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType13",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType13(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Percentage/Advanced-Word-Problems#WP3' target='_blank'><u>Percentage - Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType14(self):
        '''e.g: 80% of the children in a class have pets. 45% of them have dogs, 40% have cats and the rest have birds. 
                If 3 children in the class have birds, how many children are there in the class?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.children = random.choice([3,4,5])
        self.percentage1 = self.children * random.choice([2,4,5,10])
        self.diff = 100 - self.percentage1
        self.percentage2 = randint(25*self.diff,75*self.diff)/100
        self.percentage3 = self.diff - self.percentage2
        self.children2 = self.children*100/self.percentage1
        
        self.percentage = self.children2 * random.choice([1,2,4,5,10])
        
        while self.percentage < 20 or self.percentage > 80:
            self.children = random.choice([3,4,5])
            self.percentage1 = self.children * random.choice([2,4,5,10])
            self.diff = 100 - self.percentage1
            self.percentage2 = randint(25*self.diff,75*self.diff)/100
            self.percentage3 = self.diff - self.percentage2
            self.children2 = self.children*100/self.percentage1
            self.percentage = self.children2 *  random.choice([1,2,4,5,10])
        
        self.problem = str(self.percentage)+"% of the children in a class have pets. "
        self.problem = self.problem + str(self.percentage2)+"% of them have dogs, "+str(self.percentage3)+"% have cats and the rest have birds. "
        self.problem = self.problem + "If "+str(self.children)+" children in the class have birds, how many children are there in the class?"
        
        self.CheckAnswerType = 1

        self.answer = self.children*100*100/(self.percentage1*self.percentage)
        
        self.unit = "children"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType14",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType14(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 4 at <a href='/Learn/Primary6/Percentage/Advanced-Word-Problems#WP4' target='_blank'><u>Percentage - Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType15(self):
        '''e.g: A movie rental shop has 1375 movies for children. 40% of the movies are rated G while the rest are rated PG. 
                The shop adds a few more G-rated movies to its collection increasing the number of G-rated movies to 45%. 
                How many G-rated movies are added?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.numbers = random.choice([[25,40,randint(5,20)],[40,25,randint(3,15)],[50,20,randint(2,10)],[20,50,randint(5,20)]])
        
        self.InitialMovies = self.numbers[0] * self.numbers[2]
        self.percentage1 = self.numbers[1]
        self.InitialPGMovies = (100-self.percentage1)*self.InitialMovies / 100
        self.percentage2 = 100 - random.choice([20,25,40])
        self.FinalMovies = self.InitialPGMovies * 100 / (100-self.percentage2)
        
        self.problem = "A movie rental shop has "+str(self.InitialMovies)+" movies for children. "+str(self.percentage1)+"% of the movies are rated G while the rest are rated PG. "
        self.problem = self.problem + "The shop adds a few more G-rated movies to its collection increasing the number of G-rated movies to "+str(self.percentage2)+"%. "
        self.problem = self.problem + "How many G-rated movies are added?"
        
        self.CheckAnswerType = 1

        self.answer = self.FinalMovies - self.InitialMovies
        
        self.unit = "G-rated movies"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType15",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType15(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 5 at <a href='/Learn/Primary6/Percentage/Advanced-Word-Problems#WP5' target='_blank'><u>Percentage - Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType16(self):
        '''e.g: Alice organized a yard sale of her old books on Saturday and Sunday, and expected to sell an equal number of books on each day. 
                However, due to heavy rains on Saturday she could sell only 20% of her books that day. She managed to sell the rest of them on Sunday. 
                Had she sold 36 more books on Saturday, she would have met her expectation. Find the number of books she sold altogether.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.name = random.choice(PersonName.GirlName)
        
        self.numbers = random.choice([[15,3,randint(6,12)],[20,2,randint(8,20)],[25,5,randint(3,5)],[30,3,randint(6,12)],[40,2,randint(8,20)],])
        self.percentage = 50 - self.numbers[0]
        self.books = self.numbers[1] * self.numbers[2]

        self.problem = self.name+" organized a yard sale of her old books on Saturday and Sunday, and expected to sell an equal number of books on each day. "
        self.problem = self.problem + "However, due to heavy rains on Saturday she could sell only "+str(self.percentage)+"% of her books that day. She managed to sell the rest of them on Sunday. "
        self.problem = self.problem + "Had she sold "+str(self.books)+" more books on Saturday, she would have met her expectation. Find the number of books she sold altogether."
        
        self.CheckAnswerType = 1
        
        self.answer = self.books * 100 / self.numbers[0] 

        self.unit = "books"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType16(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType16",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType16(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 6 at <a href='/Learn/Primary6/Percentage/Advanced-Word-Problems#WP6' target='_blank'><u>Percentage - Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType17(self):
        '''e.g: Grandma let Jon and Ron share her collection of seashells between them. 
                Jon being the older of the two demanded a bigger share and took 160 seashells. 
                Soon he realized he was being unfair. 
                So, he gave 32 of his seashells to Ron which increased the number of seashells that Ron got by 25%. 
                How many seashells were there in grandma's collection?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.names = random.sample(PersonName.BoyName,2)
        
        self.numbers = random.choice([[15,3,randint(6,12)],[20,2,randint(8,20)],[25,5,randint(3,5)],[30,3,randint(6,12)],[40,2,randint(8,20)],])
        self.percentage = self.numbers[0]
        self.seashells1 = random.randrange(120,200,10)
        self.seashells2 = self.numbers[1] * self.numbers[2]

        self.problem = "Grandma let "+self.names[0]+" and "+self.names[1]+" share her collection of seashells between them. "
        self.problem = self.problem + self.names[0]+" being the older of the two demanded a bigger share and took "+str(self.seashells1)+" seashells. Soon he realized he was being unfair. "
        self.problem = self.problem + "So, he gave "+str(self.seashells2)+" of his seashells to "+self.names[1]+" which increased the number of seashells that "+self.names[1]+" got by "+str(self.percentage)+"%. "
        self.problem = self.problem + "How many seashells were there in grandma's collection?"
        
        self.CheckAnswerType = 1
        
        self.answer = self.seashells1 + self.seashells2 * 100 / self.numbers[0] 

        self.unit = "seashells"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType17(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType17",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType17(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 7 at <a href='/Learn/Primary6/Percentage/Advanced-Word-Problems#WP7' target='_blank'><u>Percentage - Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType18(self):
        '''e.g: Erica has a sum of money that she is using to buy blouses at a clothing store. 
                If she buys 2 similar blouses she will be short of 20% of the cost. 
                If she buys 1 blouse she will have $45 left. Find the cost of each blouse.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5

        self.name = random.choice(PersonName.GirlName)
        
        self.numbers = random.choice([[15,3,randint(6,12)],[20,2,randint(8,20)],[25,5,randint(3,5)],[30,3,randint(6,12)],[40,2,randint(8,20)],])
        self.percentage = 50 - self.numbers[0]
        self.price = self.numbers[1] * self.numbers[2]

        self.problem = self.name+" has a sum of money that she is using to buy blouses at a clothing store. "
        self.problem = self.problem + "If she buys 2 similar blouses she will be short of "+str(self.percentage)+"% of the cost. "
        self.problem = self.problem + "If she buys 1 blouse she will have $"+str(self.price)+" left. Find the cost of each blouse."
        
        self.CheckAnswerType = 2
        
        self.answer = float(self.price) * 100 / (2*self.numbers[0]) 

        self.unit = ""
        self.dollar_unit = "$"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType18(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType18",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':self.dollar_unit}            

    def ExplainType18(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 8 at <a href='/Learn/Primary6/Percentage/Advanced-Word-Problems#WP8' target='_blank'><u>Percentage - Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
                                                                              
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False
        elif CheckAnswer==2:
            try:
                return float(answer)==float(InputAnswer)
            except ValueError:
                return False                                            