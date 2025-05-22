'''
Created on Jan 08, 2012

Module: WriteInFigures
It generates WriteInFigures problems for Primary 4.

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
from Utils import Figures2Words
from Problems import PersonName

class WriteInFigures:
    
    def __init__(self):
        pass
        
    def GenerateProblem(self):
        random = randint(1,100)
        if random <= 50:
            if randint(1,2)==1:
                return self.GenerateProblemType1()
            else:
                return self.GenerateProblemTypeMCQ1()
        elif (random >50 and random<=85):
            if randint(1,2)==1:
                return self.GenerateProblemType2()
            else:
                return self.GenerateProblemTypeMCQ2()
        elif (random >85 and random<90):
            if randint(1,2)==1:
                return self.GenerateProblemType3()
            else:
                return self.GenerateProblemTypeMCQ3()
        elif (random >90 and random<95):
            if randint(1,2)==1:
                return self.GenerateProblemType4()
            else:
                return self.GenerateProblemTypeMCQ4()
        else:
            if randint(1,2)==1:
                return self.GenerateProblemType5()
            else:
                return self.GenerateProblemTypeMCQ5()
        #return self.GenerateProblemType5()                     
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType5","ProblemTypeMCQ5",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemType5(),self.GenerateProblemTypeMCQ5(),],
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
        #return self.GenerateProblemTypeMCQ5()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            }
        return self.ProblemType[problem_type]
                        
    def GenerateProblemType1(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.problem = "Write in figures:<br/>"
        self.number = randint(10000,99999)
        f = Figures2Words.Figures2Words()
        self.NumberInWords = f.toWords(self.number)
        self.problem = self.problem + self.NumberInWords
        self.answer = str(self.number)
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}
       
    def GenerateProblemType2(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.personName = random.choice(PersonName.PersonName)
        self.number = randint(10000,99000)
        f = Figures2Words.Figures2Words()
        self.words = f.toWords(self.number)
        
        self.ProblemPool = [self.personName+" "+random.choice(["sold","bought","purchased"])+" "+random.choice(["a car"])+" for "+self.words+".<br>Write the amount in figures.",
                            "Population of a town is "+self.words+".<br>Write the population in figures.",
                            "Total number of primary school students on the island are "+self.words+".<br>Write the total number of students in figures.",
                            ]
                            

        self.problem = random.choice(self.ProblemPool)
        self.answer = str(self.number)
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def GenerateProblemType3(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.personName = random.choice(PersonName.PersonName)
        self.number = randint(5000,30000)
        f = Figures2Words.Figures2Words()
        self.words = f.toWords(self.number)
        
        self.ProblemPool = ["Monthly salary of "+self.personName+" is "+self.words+".<br>Write the salary in figures.",
                            "Total number of spectators in the stadium are "+self.words+".<br>Write the number of spectators in figures.",
                            "Total number of people visited "+random.choice(["science museum","natural history museum","art museum","cultural fair"])+" last week were "+self.words+".<br>Write in figures."
                            ]
                            
        self.problem = random.choice(self.ProblemPool)
        self.answer = str(self.number)
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}
        
    def GenerateProblemType4(self):
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.personName = random.sample(PersonName.PersonName,2)
        self.museums = random.sample(["science museum","natural history museum","art museum","cartoon museum"],2)
        self.number1 = randint(5000,20000)
        self.number2 = randint(5000,20000)
        f = Figures2Words.Figures2Words()
        self.words1 = f.toWords(self.number1)
        self.words2 = f.toWords(self.number2)
        
        self.ProblemPool = ["Monthly salary of "+self.personName[0]+" and "+self.personName[1]+" is "+self.words1+" and "+self.words2+" respectively. Write in figures their combined monthly salary.",
                            "Last week "+self.words1+" people visited "+self.museums[0]+" and "+ self.words2+ " visited "+self.museums[1]+". Write in figures the total visitors for last week who visited the museum.",
                            "Total number of employees in company A is "+self.words1+" and company B is "+self.words2+". Express in figures the total number of employees in both companies."
                            ]
        
        self.problem = random.choice(self.ProblemPool)
        self.answer = str(self.number1+self.number2)
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}
        
    def GenerateProblemType5(self):
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.personName = random.sample(PersonName.PersonName,2)
        self.games = random.sample(["football","cricket","hockey","basket-ball"],2)
        self.number1 = randint(30000,50000)
        self.number2 = randint(30000,50000)
        f = Figures2Words.Figures2Words()
        self.words1 = f.toWords(self.number1)
        self.words2 = f.toWords(self.number2)
        
        self.ProblemPool = [self.words1+" people watched the "+self.games[0]+" and "+self.words2+" watched "+self.games[1]+". Write in figures the total viewership for both games.",
                            "Population of town A is "+self.words1+" and town B is "+self.words2+". Write in figures the total population of both towns.",
                            self.personName[0]+" bought a car for "+self.words1+" and "+self.personName[1]+" bought a different car for "+self.words2+". Write in figures the total amount they spent on cars."
                            ]
        
        self.problem = random.choice(self.ProblemPool)
        self.answer = str(self.number1+self.number2)
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}
                           
    def GenerateProblemTypeMCQ1(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.CheckAnswerType = 1
        
        self.problem_type = "ProblemTypeMCQ1"       
        self.problem = "Choose the correct answer in figures:<br/>"
        self.number = randint(10000,99999)
        f = Figures2Words.Figures2Words()
        self.NumberInWords = f.toWords(self.number)
        self.problem = self.problem + self.NumberInWords
        self.answer = str(self.number)
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''        
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain,
                                       self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ2(self):
        self.problem_type = "ProblemTypeMCQ2"
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.CheckAnswerType = 1
                
        self.personName = random.choice(PersonName.PersonName)
        self.number = randint(10000,99000)
        f = Figures2Words.Figures2Words()
        self.words = f.toWords(self.number)
        
        self.ProblemPool = [self.personName+" "+random.choice(["sold","bought","purchased"])+" "+random.choice(["a car"])+" for "+self.words+".<br>Choose the correct amount in figures.",
                            "Population of a town is "+self.words+".<br>Choose the correct population in figures.",
                            "Total number of primary school students on the island are "+self.words+".<br>Choose the total number of students in figures.",
                            ]
                            

        self.problem = random.choice(self.ProblemPool)
        self.answer = str(self.number)
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain,
                                       self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ3(self):
        self.problem_type = "ProblemTypeMCQ3"
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.CheckAnswerType = 1
                
        self.personName = random.choice(PersonName.PersonName)
        self.number = randint(5000,30000)
        f = Figures2Words.Figures2Words()
        self.words = f.toWords(self.number)
        
        self.ProblemPool = ["Monthly salary of "+self.personName+" is "+self.words+".<br>Choose the correct salary in figures.",
                            "Total number of spectators in the stadium are "+self.words+".<br>Choose the correct number of spectators in figures.",
                            "Total number of people visited "+random.choice(["science museum","natural history museum","art museum","cultural fair"])+" last week were "+self.words+".<br>Choose the correct number of visitors in figures."
                            ]
                            
        self.problem = random.choice(self.ProblemPool)
        self.answer = str(self.number)
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain,
                                       self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ4(self):
        self.problem_type = "ProblemTypeMCQ4"
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.grade = 4
        self.CheckAnswerType = 1
                
        self.personName = random.sample(PersonName.PersonName,2)
        self.museums = random.sample(["science museum","natural history museum","art museum","cartoon museum"],2)
        self.number1 = randint(5000,20000)
        self.number2 = randint(5000,20000)
        f = Figures2Words.Figures2Words()
        self.words1 = f.toWords(self.number1)
        self.words2 = f.toWords(self.number2)
        
        self.ProblemPool = ["Monthly salary of "+self.personName[0]+" and "+self.personName[1]+" is "+self.words1+" and "+self.words2+" respectively. Choose in figures their combined monthly salary.",
                            "Last week "+self.words1+" people visited "+self.museums[0]+" and "+ self.words2+ " visited "+self.museums[1]+". Choose in figures the total visitors for last week who visited museums.",
                            "Total number of employees in company A is "+self.words1+" and company B is "+self.words2+". Choose in figures the total number of employees in both companies."
                            ]
        
        self.problem = random.choice(self.ProblemPool)
        self.answer = str(self.number1+self.number2)
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain,
                                       self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ5(self):
        self.problem_type = "ProblemTypeMCQ5"
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.grade = 4
        self.CheckAnswerType = 1
                
        self.personName = random.sample(PersonName.PersonName,2)
        self.games = random.sample(["football","cricket","hockey","basket-ball"],2)
        self.number1 = randint(30000,50000)
        self.number2 = randint(30000,50000)
        f = Figures2Words.Figures2Words()
        self.words1 = f.toWords(self.number1)
        self.words2 = f.toWords(self.number2)
        
        self.ProblemPool = [self.words1+" people watched the "+self.games[0]+" and "+self.words2+" watched "+self.games[1]+". Choose in figures the total viewership for both games.",
                            "Population of town A is "+self.words1+" and town B is "+self.words2+". Choose in figures the total population of both towns.",
                            self.personName[0]+" bought a car for "+self.words1+" and "+self.personName[1]+" bought a different car for "+self.words2+". Choose in figures the total amount they spent on cars."
                            ]
        
        self.problem = random.choice(self.ProblemPool)
        self.answer = str(self.number1+self.number2)
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain,
                                       self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)
    
    def GenerateGenericMCQ(self,problem,answer,problem_type,explain,complexity_level,HCScore,grade,CheckAnswerType):
        self.template = "MCQTypeProblems.html"
        answer = int(answer)
        '''All the values of wrongAnswers must be a string'''
        self.wrongAnswers = [str(answer + random.randrange(10,100,10)),]
        self.wrongAnswers.append(str(answer - random.randrange(10,100,10)))
        self.wrongAnswers.append(str(answer + random.randrange(200,1000,100)))
        self.wrongAnswers.append(str(answer - random.randrange(200,1000,100)))
        self.wrongAnswers.append(str(answer)[1:])
        self.wrongAnswers.append(str(answer)[:-1])
        for answers in self.wrongAnswers[:]:
            if answers == answer:
                self.wrongAnswers.remove(answers)              
        self.wrongAnswers = random.sample(self.wrongAnswers,3)
        '''all answer must be string'''
        answer = str(answer)
        self.wrongAnswers.append(answer)
        random.shuffle(self.wrongAnswers)
        self.answer1 = self.wrongAnswers[0]
        self.answer2 = self.wrongAnswers[1]
        self.answer3 = self.wrongAnswers[2]
        self.answer4 = self.wrongAnswers[3]
        self.value1 = self.answer1
        self.value2 = self.answer2
        self.value3 = self.answer3
        self.value4 = self.answer4               
        return {'problem':problem,'answer':answer,'template':self.template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'answer4':self.answer4,'value1':self.value1,'value2':self.value2
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type,
                'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}
        
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
        if CheckAnswerType==1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False 

    def ExplainType1(self,problem,answer,number):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.PlaceValue = ["ones","tens","hundreds"]
        self.Value = {2:"million",1:"thousand"}
        self.ThreeDigitGroup,self.remainder = divmod(len(number),3)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/><br/>"
        self.solution_text = self.solution_text + "Fill the place value table as shown below:<br/>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1><tr>"
        if(self.remainder!=0):
            self.solution_text = self.solution_text + "<td colspan="+str(self.remainder)+">"+self.Value[self.ThreeDigitGroup]+"</td>"
            self.solution_text = self.solution_text + "<td>&nbsp;</td>"            
        for i in range(self.ThreeDigitGroup-1):
            self.solution_text = self.solution_text + "<td colspan=3>"+self.Value[self.ThreeDigitGroup-1]+"</td>"
            self.solution_text = self.solution_text + "<td>&nbsp;</td>"
        self.solution_text = self.solution_text + "<td colspan=3></td>"
        self.solution_text = self.solution_text + "</tr><tr>"        
        for i in range(self.remainder):
            if self.remainder==1:
                self.solution_text = self.solution_text + "<td>"+self.PlaceValue[i]+"</td>"
            else:
                self.solution_text = self.solution_text + "<td>"+self.PlaceValue[3-i-2]+"</td>"     
        for j in range(self.ThreeDigitGroup):
            if(self.remainder==0 and j==0):
                # if the number length is exactly divisible by 3 then avoiding one extra blank space at the beginning of the table
                self.solution_text = self.solution_text
            else:
                self.solution_text = self.solution_text + "<td>&nbsp;</td>"
            for i in range(3):               
                self.solution_text = self.solution_text + "<td>"+self.PlaceValue[3-i-1]+"</td>"
        self.solution_text = self.solution_text + "</tr><tr>"
        for i in range(self.remainder):
            self.solution_text = self.solution_text + "<td>"+number[i]+"</td>"     
        for j in range(self.ThreeDigitGroup):
            if(self.remainder==0 and j==0):
                # if the number length is exactly divisible by 3 then avoiding one extra blank space at the beginning of the table
                self.solution_text = self.solution_text
            else:
                self.solution_text = self.solution_text + "<td>&nbsp;</td>"
            for i in range(3):               
                self.solution_text = self.solution_text + "<td>"+number[i+self.remainder+j*3]+"</td>"        
        self.solution_text = self.solution_text + "</tr></table><br>"
        self.solution_text = self.solution_text + "based on above table you can write the number as:<br/>"
        self.solution_text = self.solution_text + "<i><b>"+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def ExplainType2(self,problem,answer,amount1,amount2):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.PlaceValue = ["ones","tens","hundreds"]
        self.Value = {2:"million",1:"thousand"}
        number = str(amount1)
        self.ThreeDigitGroup,self.remainder = divmod(len(number),3)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/><br/>"
        self.solution_text = self.solution_text + "Fill the place value table with first number as shown below:<br/>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1><tr>"
        if(self.remainder!=0):
            self.solution_text = self.solution_text + "<td colspan="+str(self.remainder)+">"+self.Value[self.ThreeDigitGroup]+"</td>"
            self.solution_text = self.solution_text + "<td>&nbsp;</td>"            
        for i in range(self.ThreeDigitGroup-1):
            self.solution_text = self.solution_text + "<td colspan=3>"+self.Value[self.ThreeDigitGroup-1]+"</td>"
            self.solution_text = self.solution_text + "<td>&nbsp;</td>"
        self.solution_text = self.solution_text + "<td colspan=3></td>"
        self.solution_text = self.solution_text + "</tr><tr>"        
        for i in range(self.remainder):
            if self.remainder==1:
                self.solution_text = self.solution_text + "<td>"+self.PlaceValue[i]+"</td>"
            else:
                self.solution_text = self.solution_text + "<td>"+self.PlaceValue[3-i-2]+"</td>"     
        for j in range(self.ThreeDigitGroup):
            if(self.remainder==0 and j==0):
                # if the number length is exactly divisible by 3 then avoiding one extra blank space at the beginning of the table
                self.solution_text = self.solution_text
            else:
                self.solution_text = self.solution_text + "<td>&nbsp;</td>"
            for i in range(3):               
                self.solution_text = self.solution_text + "<td>"+self.PlaceValue[3-i-1]+"</td>"
        self.solution_text = self.solution_text + "</tr><tr>"
        for i in range(self.remainder):
            self.solution_text = self.solution_text + "<td>"+number[i]+"</td>"     
        for j in range(self.ThreeDigitGroup):
            if(self.remainder==0 and j==0):
                # if the number length is exactly divisible by 3 then avoiding one extra blank space at the beginning of the table
                self.solution_text = self.solution_text
            else:
                self.solution_text = self.solution_text + "<td>&nbsp;</td>"
            for i in range(3):               
                self.solution_text = self.solution_text + "<td>"+number[i+self.remainder+j*3]+"</td>"        
        self.solution_text = self.solution_text + "</tr></table><br>"

        number = str(amount2)
        self.ThreeDigitGroup,self.remainder = divmod(len(number),3)
        self.solution_text = self.solution_text + "Now, fill the place value table with second number as shown below:<br/>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1><tr>"
        if(self.remainder!=0):
            self.solution_text = self.solution_text + "<td colspan="+str(self.remainder)+">"+self.Value[self.ThreeDigitGroup]+"</td>"
            self.solution_text = self.solution_text + "<td>&nbsp;</td>"            
        for i in range(self.ThreeDigitGroup-1):
            self.solution_text = self.solution_text + "<td colspan=3>"+self.Value[self.ThreeDigitGroup-1]+"</td>"
            self.solution_text = self.solution_text + "<td>&nbsp;</td>"
        self.solution_text = self.solution_text + "<td colspan=3></td>"
        self.solution_text = self.solution_text + "</tr><tr>"        
        for i in range(self.remainder):
            if self.remainder==1:
                self.solution_text = self.solution_text + "<td>"+self.PlaceValue[i]+"</td>"
            else:
                self.solution_text = self.solution_text + "<td>"+self.PlaceValue[3-i-2]+"</td>"     
        for j in range(self.ThreeDigitGroup):
            if(self.remainder==0 and j==0):
                # if the number length is exactly divisible by 3 then avoiding one extra blank space at the beginning of the table
                self.solution_text = self.solution_text
            else:
                self.solution_text = self.solution_text + "<td>&nbsp;</td>"
            for i in range(3):               
                self.solution_text = self.solution_text + "<td>"+self.PlaceValue[3-i-1]+"</td>"
        self.solution_text = self.solution_text + "</tr><tr>"
        for i in range(self.remainder):
            self.solution_text = self.solution_text + "<td>"+number[i]+"</td>"     
        for j in range(self.ThreeDigitGroup):
            if(self.remainder==0 and j==0):
                # if the number length is exactly divisible by 3 then avoiding one extra blank space at the beginning of the table
                self.solution_text = self.solution_text
            else:
                self.solution_text = self.solution_text + "<td>&nbsp;</td>"
            for i in range(3):               
                self.solution_text = self.solution_text + "<td>"+number[i+self.remainder+j*3]+"</td>"        
        self.solution_text = self.solution_text + "</tr></table><br>"

        self.solution_text = self.solution_text + "Add the two numbers = "+str(amount1)+" + "+str(amount2)+" = "+str(amount1+amount2)
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain            