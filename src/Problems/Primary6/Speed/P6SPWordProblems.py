'''
Created on May 02, 2012
Module: P6SPWordProblems
Generates the "Distance, Time and Speed Word Problems" problems for Primary 6

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
import string

class P6SPWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemTypeMCQ3",],
                            4:["ProblemType4",],5:["ProblemType5",],6:["ProblemType6",],
                            7:["ProblemType7",],8:["ProblemType8",],9:["ProblemType9",],
                            10:["ProblemTypeMCQ10",],11:["ProblemType11",],12:["ProblemTypeMCQ12","ProblemType12",],
                            }
        
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],3:[self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4(),],5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],9:[self.GenerateProblemType9(),],
                                    10:[self.GenerateProblemTypeMCQ10(),],11:[self.GenerateProblemType11(),],
                                    12:[self.GenerateProblemTypeMCQ12(),self.GenerateProblemType12(),]
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
        #return self.GenerateProblemType12()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemTypeMCQ10":self.GenerateProblemTypeMCQ10(),
                            "ProblemType11":self.GenerateProblemType11(),
                            "ProblemType12":self.GenerateProblemType12(),
                            "ProblemTypeMCQ12":self.GenerateProblemTypeMCQ12(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g: A bird flies in search of food from her nest in a tree to a stream 1800 metres away in 3 minutes. 
                What is the speed at which she flies?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.speed = random.randrange(200,600,10)
        self.time = randint(3,10)
        self.distance = self.speed * self.time

        self.problem = "A bird flies in search of food from her nest in a tree to a stream "+str(self.distance)+" metres away in "+str(self.time)+" minutes."
        self.problem = self.problem + " What is the speed at which she flies?"

        self.answer = self.speed
        self.CheckAnswerType = 1

        self.unit = "m/min"
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
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Speed/Distance-Time-Speed#WP1' target='_blank'><u>Distance, Time and Speed</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g: A lorry is going at a speed of 40 km/h. At this speed, how far can it go in 1/2 h?'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.numerator = 1
        self.denominator = randint(2,12)
        if self.denominator <= 4:
            self.speed = random.randrange(self.denominator*10,self.denominator*20,self.denominator)
        elif self.denominator > 4 and self.denominator <=7:
            self.speed = random.randrange(self.denominator*5,self.denominator*10,self.denominator)
        else:
            self.speed = random.randrange(self.denominator*3,self.denominator*6,self.denominator)
        
        self.distance = self.speed / self.denominator

        self.problem = "<table class='FractionsTable'><tr><td>A lorry is going at a speed of "+str(self.speed)+" km/h. At this speed, how far can it go in</td></tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'><tr><td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br />"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td><td>&nbsp;h?</td></tr></table>"

        self.answer = self.distance
        self.CheckAnswerType = 1

        self.unit = "km"
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
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Speed/Distance-Time-Speed#WP2' target='_blank'><u>Distance, Time and Speed</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,
                    CheckAnswerType,grade,complexity_level,HCScore):
        
        
        '''Removing correct answers from the wrongAnswers list'''
        wrongAnswers = filter(self.removeCorrectAnswer,wrongAnswers)
                             
        '''Randomly selecting 3 wrong answers and adding the correct answer as well'''
        try:
            wrongAnswers = random.sample(wrongAnswers,3)
        except ValueError:
            pass
            
        wrongAnswers.append(answer)
        random.shuffle(wrongAnswers)
        try:
            self.answer1 = wrongAnswers[0]
            self.answer2 = wrongAnswers[1]
            self.answer3 = wrongAnswers[2]
            self.answer4 = wrongAnswers[3]         
        except IndexError:
            pass
        try:
            self.value1 = str(self.answer1[0])+"/"+str(self.answer1[1])+"/"+str(self.answer1[2])
            self.value2 = str(self.answer2[0])+"/"+str(self.answer2[1])+"/"+str(self.answer2[2])
            self.value3 = str(self.answer3[0])+"/"+str(self.answer3[1])+"/"+str(self.answer3[2])
            self.value4 = str(self.answer4[0])+"/"+str(self.answer4[1])+"/"+str(self.answer4[2])
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answerM1':self.answer1[0],'answerN1':self.answer1[1],'answerD1':self.answer1[2],
                'answerM2':self.answer2[0],'answerN2':self.answer2[1],'answerD2':self.answer2[2],
                'answerM3':self.answer3[0],'answerN3':self.answer3[1],'answerD3':self.answer3[2],
                'answerM4':self.answer4[0],'answerN4':self.answer4[1],'answerD4':self.answer4[2],
                'value1':self.value1,'value2':self.value2,'value3':self.value3,'value4':self.value4,
                'explain':explain,'problem_type':problem_type,
                'CheckAnswerType':CheckAnswerType,'grade':6,"complexity_level":complexity_level,"HCScore":HCScore}      

    def GenerateProblemTypeMCQ3(self):
        '''e.g: A train is running at a speed of 180 km/h. At this speed, how long will the train take to travel the 270-km long distance between Station A and Station B?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.denominator = randint(2,7)
        self.numerator = randint(self.denominator+1,10)
        
        while self.numerator%self.denominator==0:
            self.denominator = randint(2,7)
            self.numerator = randint(self.denominator+1,10)            
        
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        self.numerator = self.numerator / self.gcf
        self.denominator = self.denominator / self.gcf
        
        self.multiplier = random.randrange(10,30,10)
        self.speed = self.denominator * self.multiplier
        self.distance = self.numerator * self.multiplier
            
        self.problem = "A train is running at a speed of "+str(self.speed)+" km/h. At this speed, how long will the train take to travel the "+str(self.distance)+"-km long distance between Station A and Station B?<br><br>"
                    
        self.mixed,self.numerator = divmod(self.numerator,self.denominator)
        self.answer1 = self.mixed
        self.answer2 = self.numerator
        self.answer3 = self.denominator
        self.answer = [self.answer1,self.answer2,self.answer3]
        
        self.problem_type = "ProblemTypeMCQ3"
        self.template = "FractionMCQTypeProblems.html"
        self.CheckAnswerType = 2
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append([self.answer1+1,self.answer2,self.answer3])
        self.wrongAnswers.append([self.answer1,self.answer2,self.answer3+1])
        self.wrongAnswers.append([self.answer1,self.answer2+1,self.answer3])         
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ3(self.problem,self.answer1,self.answer2,self.answer3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def ExplainTypeMCQ3(self,problem,answer1,answer2,answer3):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        self.answer_text = self.answer_text + "<td>"+str(answer1)+"&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*(len(str(answer3))/2)+str(answer2)+"&nbsp;"*(len(str(answer3))/2)+"</u><br>"+"&nbsp;"*(len(str(answer2))/2)+str(answer3)+"</td>"            
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Speed/Distance-Time-Speed#WP3' target='_blank'><u>Distance, Time and Speed</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g: An aeroplane from New Delhi to Singapore takes about 5 1/2 hours to cover 
                the distance of 4142 km. What is the average speed of the aeroplane?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.speed = randint(400,800)
        
        self.mixed = randint(1,7)
        self.numerator = randint(1,5)
        self.denominator = randint(self.numerator+1,9)
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        self.numerator = self.numerator / self.gcf
        self.denominator = self.denominator / self.gcf
        
        self.distance = self.speed * (self.denominator*self.mixed+self.numerator)/self.denominator

        self.problem = "<table class='FractionsTable'><tr><td>An aeroplane from City A to City B takes about "+str(self.mixed)+"&nbsp;</td><td><u>"+str(self.numerator)+"</u><br />"+str(self.denominator)+"</td><td>&nbsp;hours to cover</td></tr></table>"
        self.problem = self.problem + "the distance of "+str(self.distance)+" km. What is the average speed of the aeroplane?<br><br>"
        self.problem = self.problem + "(Write your answer correct to 1 decimal place)"

        self.answer = round(float(self.distance*self.denominator)/(self.denominator*self.mixed+self.numerator),1) 
        self.CheckAnswerType = 3

        self.unit = "km/hr"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType4(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Speed/Average-Speed#WP1' target='_blank'><u>Average Speed</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType5(self):
        '''e.g: Julie cycles at a speed of 215 m/min. 
            How long does it take her to cycle a distance of 1500 m? Round off your answer to the nearest minute.
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.gender = random.choice([[random.choice(PersonName.GirlName),"her"],[random.choice(PersonName.BoyName),"him"]])
        
        self.speed = randint(100,400)
        self.distance = random.randrange(1000,2000,10)
        
        self.time = int(round(float(self.distance)/self.speed,0))

        self.problem = self.gender[0]+" cycles at a speed of "+str(self.speed)+" m/min. How long does it take "+self.gender[1]+" to cycle a distance of "+str(self.distance)+" m? <br><br>Round off your answer to the nearest minute."

        self.answer = self.time 
        self.CheckAnswerType = 1

        self.unit = "minutes"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType5(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Speed/Average-Speed#WP2' target='_blank'><u>Average Speed</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6(self):
        '''e.g: A roller skater skates at an average speed of 35 km/h. Find the distance he covers in 15 minutes.
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.speed = randint(10,40)
        self.time = random.randrange(10,50,5)
        self.distance = round(float(self.speed*self.time)/60,2)

        self.problem = "A roller skater skates at an average speed of "+str(self.speed)+" km/h. Find the distance he covers in "+str(self.time)+" minutes.<br><br>"
        self.problem = self.problem + "(Express your answer to 2 decimal places)"

        self.answer = self.distance
        self.CheckAnswerType = 3

        self.unit = "km"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType6(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Speed/Average-Speed#WP3' target='_blank'><u>Average Speed</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7(self):
        '''e.g: In a 10-km race, Grace ran the first 2 km in 1/5  h, the next 6 km at a speed 
                of 9 km/h and the last stretch at 12 km/h. What was her average speed for the run? 
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.gender = random.choice([[random.choice(PersonName.GirlName),"her"],[random.choice(PersonName.BoyName),"his"]])
        
        self.leg1 = randint(2,3)
        self.leg2 = randint(4,6)
        self.leg3 = randint(2,3)
        self.total = self.leg1 + self.leg2 + self.leg3
        
        self.numerator =  self.leg1
        self.denominator = randint(6,12)
        self.speed2 = randint(6,10)
        self.speed3 = self.denominator
        
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.numerator, self.denominator)
        self.numerator = self.numerator / self.gcf
        self.denominator = self.denominator / self.gcf

        self.problem = "<table class='FractionsTable'><tr><td>In a "+str(self.total)+"-km race, "+self.gender[0]+" ran the first "+str(self.leg1)+" km in&nbsp;</td>"
        self.problem = self.problem + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br />"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td><td>&nbsp;h, the next "+str(self.leg2)+" km at a</td></tr></table>"
        self.problem = self.problem + "speed of "+str(self.speed2)+" km/h and the last stretch at "+str(self.speed3)+" km/h. What was "+self.gender[1]+" average speed for the run?<br><br>"
        self.problem = self.problem + "(Round off your answer to 2 decimal places)"

        self.answer = round(float(self.total)/((float(self.numerator)/self.denominator)+float(self.leg2)/self.speed2+float(self.leg3)/self.speed3),2)
        self.CheckAnswerType = 3

        self.unit = "km/hr"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType7(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Speed/Advanced-Word-Problems#WP1' target='_blank'><u>Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8(self):
        '''e.g: Bella is taking an adventurous trip through a jungle. 
                First, she trekked for 30 minutes into the thick jungle at an average speed of 6 km/h. 
                Next, she took a boat to cross a lake which rode her at an average speed of 20 km/h for 12 minutes. 
                For the last part of her trip, she hiked for 2 hours at an average speed of 4 km/h. 
                Find the total distance she covered on her trip. 
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.gender = random.choice([[random.choice(PersonName.GirlName),"her","she","her"],[random.choice(PersonName.BoyName),"his","he","him"]])

        self.minutes = [10,12,15,18,20,24,30,36,40,42,45,48,50,54]
        self.minutes1 = random.choice(self.minutes)
        self.minutes2 = random.choice(self.minutes)
        self.hour = randint(2,5)
        self.speed1 = randint(4,8)
        self.speed2 = random.randrange(10,40,10)
        self.speed3 = randint(2,5)
        
        self.problem = self.gender[0]+" is taking an adventurous trip through a jungle. First, "+self.gender[2]+" trekked for "+str(self.minutes1)+" minutes into the "
        self.problem = self.problem + "thick jungle at an average speed of "+str(self.speed1)+" km/h. Next, "+self.gender[2]+" took a boat to cross a lake which rode "
        self.problem = self.problem + self.gender[3]+" at an average speed of "+str(self.speed2)+" km/h for "+str(self.minutes2)+" minutes. For the last part of "
        self.problem = self.problem + self.gender[1]+" trip, "+self.gender[2]+" hiked for "+str(self.hour)+" hours at an average speed of "+str(self.speed3)+" km/h. "
        self.problem = self.problem + "Find the total distance "+self.gender[2]+" covered on "+self.gender[1]+" trip.<br><br>"
        self.problem = self.problem + "(Round off your answer to 2 decimal places)"

        self.answer = round(float(self.minutes1*self.speed1)/60 + float(self.minutes2*self.speed2)/60 + float(self.hour*self.speed3),2)
        
        self.CheckAnswerType = 3

        self.unit = "km"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType8(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Speed/Advanced-Word-Problems#WP2' target='_blank'><u>Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType9(self):
        '''e.g: Eric walked at an average pace of 65 m/min for the first half of the distance to his friend's house. 
                Calculate his average speed for the second half of the distance if he took a total of 18 minutes to reach his friend's house which was 1.3 km away. 
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.gender = random.choice([[random.choice(PersonName.GirlName),"her","she"],[random.choice(PersonName.BoyName),"his","he"]])

        self.speed1 = random.randrange(50,100,5)
        self.time1 = randint(5,15)
        self.TotalDistance = float(self.speed1 * self.time1 * 2) / 1000
        self.time2 = randint(5,15)
        self.TotalTime = self.time1 + self.time2
        self.speed2 = round(float(self.speed1*self.time1)/self.time2,0)
        
        
        self.problem = self.gender[0]+" walked at an average pace of "+str(self.speed1)+" m/min for the first half of the distance to "+self.gender[1]+" friend's house. "
        self.problem = self.problem + "Calculate "+self.gender[1]+" average speed for the second half of the distance if "+self.gender[2]+" took a total of "+str(self.TotalTime)+" minutes to reach "+self.gender[1]+" friend's house which was "+str(self.TotalDistance)+" km away."
        self.problem = self.problem + "<br><br>(Round off your answer to the nearest whole number)"

        self.answer = int(round(float(self.TotalDistance*1000/2)/(self.TotalTime-(float(self.TotalDistance*1000/2)/self.speed1)),0))
        
        self.CheckAnswerType = 1

        self.unit = "m/min"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType9",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType9(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Speed/Advanced-Word-Problems#WP3' target='_blank'><u>Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ10(self):
        '''e.g: Sally and Molly started from the same point at the same time in two different cars and drove on the same route to reach the same destination at average speeds of 40 km/h and 45 km/h respectively. 
                If the route was 270 kilometres long and if Molly arrived at the destination at 5:30 pm, when did Sally arrive there?  
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.names = random.sample(PersonName.GirlName,2)
        
        self.speed1 = random.randrange(30,60,5)
        self.speed2 = random.randrange(30,60,5)
        while self.speed1==self.speed2:
            self.speed2 = random.randrange(30,60,5)
            
        self.gcf = LcmGcf.LcmGcf().find_gcf(self.speed1, self.speed2)
        
        self.distance = self.speed1*self.speed2 / self.gcf
        
        self.hour = randint(1,5)
        self.minutes = randint(10,45)

        self.time1 = self.distance/self.speed1    
        self.time2 = self.distance/self.speed2
        
        if self.time2 < self.time1:
            self.speed = self.speed1
            self.speed1 = self.speed2
            self.speed2 = self.speed
            self.time = self.time1
            self.time1 = self.time2
            self.time2 = self.time
            
        self.diff = self.time2 - self.time1
        self.MinutesDiff = self.diff * 60
        h1,m1 = divmod(self.MinutesDiff,60)
        self.hour1 = self.hour + h1
        self.minutes1 = self.minutes + m1
        h1,m1 = divmod(self.minutes1,60)
        self.hour1 = self.hour1 + h1
        self.minutes1 = m1            

                    
        self.problem = self.names[0]+" and "+self.names[1]+" started from the same point at the same time in two different cars and drove on the same route to reach the same destination at average speeds of "+str(self.speed1)+" km/h and "+str(self.speed2)+" km/h respectively." 
        self.problem = self.problem + "<br><br>If the route was "+str(self.distance)+" kilometres long and if "+self.names[0]+" arrived at the destination at "+str(self.hour)+":"+str(self.minutes)+" pm, when did "+self.names[1]+" arrive there?"

        if len(str(self.minutes1))==1:
            self.minutes1 = "0"+str(self.minutes1)
        self.answer = str(self.hour1)+":"+str(self.minutes1)+" pm"
        
        self.problem_type = "ProblemTypeMCQ10"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 4
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.hour1-1)+":"+str(self.minutes1)+" pm")
        self.wrongAnswers.append(str(self.hour1+1)+":"+str(self.minutes1)+" pm")
        self.wrongAnswers.append(str(self.hour1)+":"+str(self.minutes1-5)+" pm")
        self.wrongAnswers.append(str(self.hour1)+":"+str(self.minutes1+5)+" pm")         
        self.wrongAnswers.append(str(self.hour1)+":"+str(self.minutes1+10)+" pm")
        self.wrongAnswers.append(str(self.hour1)+":"+str(self.minutes1)+" am")
        self.wrongAnswers.append(str(self.hour1+1)+":"+str(self.minutes1)+" am")
        self.wrongAnswers.append(str(self.hour1)+":"+str(self.minutes1-5)+" am")
        self.wrongAnswers.append(str(self.hour1)+":"+str(self.minutes1+5)+" am")         
        self.wrongAnswers.append(str(self.hour1)+":"+str(self.minutes1+10)+" am")
                                      
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ10(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ1(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def ExplainTypeMCQ10(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "For detailed explanation refer to Word Problem 4 at <a href='/Learn/Primary6/Speed/Advanced-Word-Problems#WP4' target='_blank'><u>Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateMCQ1(self,wrongAnswers,problem,answer,template,explain,problem_type,
                    CheckAnswerType,grade,complexity_level,HCScore):
        
        
        '''Removing correct answers from the wrongAnswers list'''
        wrongAnswers = filter(self.removeCorrectAnswer,wrongAnswers)
                             
        '''Randomly selecting 3 wrong answers and adding the correct answer as well'''
        try:
            wrongAnswers = random.sample(wrongAnswers,3)
        except ValueError:
            pass
            
        wrongAnswers.append(answer)
        random.shuffle(wrongAnswers)
        try:
            self.answer1 = wrongAnswers[0]
            self.answer2 = wrongAnswers[1]
            self.answer3 = wrongAnswers[2]
            self.answer4 = wrongAnswers[3]         
        except IndexError:
            pass
        try:
            self.value1 = string.join(self.answer1.split(),"")
            self.value2 = string.join(self.answer2.split(),"")
            self.value3 = string.join(self.answer3.split(),"")
            self.value4 = string.join(self.answer4.split(),"")
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,'answer4':self.answer4,
                'value1':self.value1,'value2':self.value2,'value3':self.value3,'value4':self.value4,
                'explain':explain,'problem_type':problem_type,
                'CheckAnswerType':CheckAnswerType,'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore}      

    def GenerateProblemType11(self):
        '''e.g: Carol and Maya took part in a 20-km cycle race. 
                Carol rode at an average speed of 22 km/h while Maya rode at an average speed of 25 km/h. 
                How far apart will the two girls be when Maya has covered half the distance? 
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.gender = random.choice([[random.sample(PersonName.GirlName,2),"girls"],[random.sample(PersonName.BoyName,2),"boys"]])

        self.numerator = randint(1,3)
        self.denominator = randint(self.numerator+1,5)
        self.speed1 = random.randrange(self.denominator*2,self.denominator*6,self.denominator)
       
        self.speed2 = random.randrange(self.denominator*2,self.denominator*6,self.denominator)
        
        while self.speed1<=self.speed2:
            self.speed1 = random.randrange(self.denominator*2,self.denominator*6,self.denominator)
            self.speed2 = random.randrange(self.denominator*2,self.denominator*6,self.denominator)
            
        self.distance = 2 * self.speed1*self.numerator/self.denominator
                
        self.problem = self.gender[0][0]+" and "+self.gender[0][1]+" took part in a "+str(self.distance)+"-km cycle race. "
        self.problem = self.problem + self.gender[0][0]+" rode at an average speed of "+str(self.speed1)+" km/h while "+self.gender[0][1]+" rode at an average speed of "+str(self.speed2)+" km/h."
        self.problem = self.problem + " How far apart will the two "+self.gender[1]+" be when "+self.gender[0][0]+" has covered half the distance?"

        self.answer = self.distance/2 - (self.numerator*self.speed2/self.denominator)
        
        self.CheckAnswerType = 1

        self.unit = "km"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType11",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType11(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 5 at <a href='/Learn/Primary6/Speed/Advanced-Word-Problems#WP5' target='_blank'><u>Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ12(self):
        '''e.g: James and Lily, who were standing 29.25 km apart, started running towards each other at 0915. 
        James ran at an average speed of 5.5 km/h while Lily ran at an average speed of 7.5 km/h.  
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.names = random.sample(PersonName.PersonName,2)         

        self.CombinedSpeed = randint(8,18)
        self.speed1 = float(randint(self.CombinedSpeed*10/4,self.CombinedSpeed*3*10/4))/10
        self.speed2 = self.CombinedSpeed - float(self.speed1)

        self.TotalTimeTaken = randint(1,4)+float(random.choice([6,12,15,18,24,30,36,42,45,48]))/60
        self.TotalDistance = float(self.CombinedSpeed * self.TotalTimeTaken)
        
        self.hour = randint(12,15)
        self.minutes = randint(10,45)
                             
        self.problem = self.names[0]+" and "+self.names[1]+", who were standing "+str(self.TotalDistance)+" km apart, started running towards each other at "+str(self.hour)+str(self.minutes)+". " 
        self.problem = self.problem + self.names[0]+" ran at an average speed of "+str(self.speed1)+" km/h while "+self.names[1]+" ran at an average speed of "+str(self.speed2)+" km/h. "
        self.problem = self.problem + "At what time did they meet?"

        self.MinutesAdd = int(self.TotalTimeTaken*60)
        h1,m1 = divmod(self.MinutesAdd,60)
        self.hour1 = int(self.hour) + h1
        self.minutes1 = int(self.minutes) + m1
        h1,m1 = divmod(self.minutes1,60)
        self.hour1 = self.hour1 + h1
        self.minutes1 = m1        

        if self.minutes1 < 10:
            self.minutes1 = '0'+str(self.minutes1) 
        
        self.answer = str(self.hour1)+str(self.minutes1)
        
        self.problem_type = "ProblemTypeMCQ12"
        self.template = "MCQTypeProblems.html"
        self.CheckAnswerType = 5
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.hour1+1)+str(self.minutes1))
        self.wrongAnswers.append(str(self.hour1-1)+str(self.minutes1))
        if int(self.minutes1)>=15 and int(self.minutes1)<20:
            self.wrongAnswers.append(str(self.hour1)+str(int(self.minutes1)-5))
        else:
            self.wrongAnswers.append(str(self.hour1+2)+str(self.minutes1))
        if int(self.minutes1)>=20:
            self.wrongAnswers.append(str(self.hour1)+str(int(self.minutes1)-10))
        else:
            self.wrongAnswers.append(str(self.hour1-2)+str(self.minutes1))
                                      
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ12(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ1(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def ExplainTypeMCQ12(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "For detailed explanation refer to Word Problem 6 at <a href='/Learn/Primary6/Speed/Advanced-Word-Problems#WP6' target='_blank'><u>Advanced Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType12(self):
        '''e.g: James and Lily, who were standing 29.25 km apart, started running towards each other at 0915. 
        James ran at an average speed of 5.5 km/h while Lily ran at an average speed of 7.5 km/h. 
        How much distance had Lily run when they both met?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.names = random.sample(PersonName.PersonName,2)         

        self.CombinedSpeed = randint(8,18)
        self.speed1 = float(randint(self.CombinedSpeed*10/4,self.CombinedSpeed*3*10/4))/10
        self.speed2 = self.CombinedSpeed - float(self.speed1)

        self.TotalTimeTaken = randint(1,4)+float(random.choice([6,12,15,18,24,30,36,42,45,48]))/60
        self.TotalDistance = float(self.CombinedSpeed * self.TotalTimeTaken)
        
        self.hour = randint(12,15)
        self.minutes = randint(10,45)
                             
        self.problem = self.names[0]+" and "+self.names[1]+", who were standing "+str(self.TotalDistance)+" km apart, started running towards each other at "+str(self.hour)+str(self.minutes)+". " 
        self.problem = self.problem + self.names[0]+" ran at an average speed of "+str(self.speed1)+" km/h while "+self.names[1]+" ran at an average speed of "+str(self.speed2)+" km/h. "
        self.problem = self.problem + "How much distance had Lily run when they both met?"
        
        self.answer = round(self.TotalTimeTaken * self.speed2,3)
        
        self.CheckAnswerType = 3

        self.unit = "km"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType12",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit}            

    def ExplainType12(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 6 at <a href='/Learn/Primary6/Speed/Advanced-Word-Problems#WP6' target='_blank'><u>Advanced Word Problems</u></a>"
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
                answer=str(answer[0])+"/"+str(answer[1])+"/"+str(answer[2])
                '''for some weird reason there is an extra / at end of input..so removing it'''
                return answer==str(InputAnswer[:-1])
            except ValueError:
                return False
        elif CheckAnswer==3:
            try:
                return float(answer)==float(InputAnswer)
            except ValueError:
                return False
        elif CheckAnswer==4:
            try:
                '''for some weird reason there is an extra / at end of input..so removing it'''
                return answer==str(InputAnswer[:-1])
            except ValueError:
                return False
        elif CheckAnswer==5:
            try:
                return answer==str(InputAnswer)
            except ValueError:
                return False                                   