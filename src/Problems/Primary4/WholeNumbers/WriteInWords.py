'''
Created on Jan 10, 2012

Module: WriteInWords
Generates the WriteInWords problems for Primary 4

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
  

History:
  
'''
import random
import string
from random import randint
from Utils import Figures2Words
from Problems import PersonName

class WriteInWords:
    
    def __init__(self):
        pass
        
    def GenerateProblem(self):
        """ randomly decides which question to generate with given weightage
        Probtype1 with 50% and so on """
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
        
        self.problem = "Write in words:<br/>"
        self.number = randint(10000,99999)
        f = Figures2Words.Figures2Words()
        self.NumberInWords = f.toWords(self.number)
        self.problem = self.problem + str(self.number)
        self.answer = self.NumberInWords
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
        
        self.ProblemPool = [self.personName+" "+random.choice(["sold","bought","purchased"])+" "+random.choice(["a car"])+" for $"+str(self.number)+".<br>Write the amount in words.",
                            "Population of a town is "+str(self.number)+".<br>Write the population in words.",
                            "Total number of primary school students on the island are "+str(self.number)+".<br>Write the total number of students in words.",
                            ]
                            

        self.problem = random.choice(self.ProblemPool)
        self.answer = self.words
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
        
        self.ProblemPool = ["Monthly salary of "+self.personName+" is $"+str(self.number)+".<br>Write the salary in words.",
                            "Total number of spectators in the stadium are "+str(self.number)+".<br>Write the number of spectators in words.",
                            "Total number of people visited "+random.choice(["science museum","natural history museum","art museum","cultural fair"])+" last week were "+str(self.number)+".<br>Write in words."
                            ]
                            
        self.problem = random.choice(self.ProblemPool)
        self.answer = self.words
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
        
        self.ProblemPool = ["Monthly salary of "+self.personName[0]+" and "+self.personName[1]+" is $"+str(self.number1)+" and $"+str(self.number2)+" respectively. Write in words their combined monthly salary.",
                            "Last week "+str(self.number1)+" people visited "+self.museums[0]+" and "+ str(self.number2)+ " visited "+self.museums[1]+". Write in words the total visitors for last week who visited the museum.",
                            "Total number of employees in company A is "+str(self.number1)+" and company B is "+str(self.number2)+". Express in words the total number of employees in both companies."
                            ]
        
        self.problem = random.choice(self.ProblemPool)
        self.answer = f.toWords(self.number1+self.number2)
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
        
        self.ProblemPool = [str(self.number1)+" people watched the "+self.games[0]+" and "+str(self.number2)+" watched "+self.games[1]+". Write in words the total viewership for both games.",
                            "Population of town A is "+str(self.number1)+" and town B is "+str(self.number2)+". Write in words the total population of both towns.",
                            self.personName[0]+" bought a car for $"+str(self.number1)+" and "+self.personName[1]+" bought a different car for $"+str(self.number2)+". Write in words the total amount they spent on cars."
                            ]
        
        self.problem = random.choice(self.ProblemPool)
        self.answer = f.toWords(self.number1+self.number2)
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
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.problem_type = "ProblemTypeMCQ1"       
        self.problem = "Choose the correct answer in words:<br/>"
        self.number = randint(10000,99999)
        f = Figures2Words.Figures2Words()
        self.NumberInWords = f.toWords(self.number)
        self.problem = self.problem + str(self.number)
        self.answer = self.NumberInWords
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''        
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain,self.number,
                                       self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ2(self):
        self.problem_type = "ProblemTypeMCQ2"
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.personName = random.choice(PersonName.PersonName)
        self.number = randint(10000,99000)
        f = Figures2Words.Figures2Words()
        self.words = f.toWords(self.number)
        
        self.ProblemPool = [self.personName+" "+random.choice(["sold","bought","purchased"])+" "+random.choice(["a car"])+" for $"+str(self.number)+".<br>Write the amount in words.",
                            "Population of a town is "+str(self.number)+".<br>Write the population in words.",
                            "Total number of primary school students on the island are "+str(self.number)+".<br>Write the total number of students in words.",
                            ]
                            

        self.problem = random.choice(self.ProblemPool)
        self.answer = self.words
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain,self.number,
                                       self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ3(self):
        self.problem_type = "ProblemTypeMCQ3"
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.personName = random.choice(PersonName.PersonName)
        self.number = randint(10000,99000)
        f = Figures2Words.Figures2Words()
        self.words = f.toWords(self.number)
        
        self.ProblemPool = [self.personName+" "+random.choice(["sold","bought","purchased"])+" "+random.choice(["a car"])+" for $"+str(self.number)+".<br>Write the amount in words.",
                            "Population of a town is "+str(self.number)+".<br>Write the population in words.",
                            "Total number of primary school students on the island are "+str(self.number)+".<br>Write the total number of students in words.",
                            ]
                            

        self.problem = random.choice(self.ProblemPool)
        self.answer = self.words
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain,self.number,
                                       self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ4(self):
        self.problem_type = "ProblemTypeMCQ4"
        self.complexity_level = "medium"
        self.HCScore = 5
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.personName = random.sample(PersonName.PersonName,2)
        self.museums = random.sample(["science museum","natural history museum","art museum","cartoon museum"],2)
        self.number1 = randint(5000,20000)
        self.number2 = randint(5000,20000)
        f = Figures2Words.Figures2Words()
        
        self.ProblemPool = ["Monthly salary of "+self.personName[0]+" and "+self.personName[1]+" is $"+str(self.number1)+" and $"+str(self.number2)+" respectively. Write in words their combined monthly salary.",
                            "Last week "+str(self.number1)+" people visited "+self.museums[0]+" and "+ str(self.number2)+ " visited "+self.museums[1]+". Write in words the total visitors for last week who visited the museum.",
                            "Total number of employees in company A is "+str(self.number1)+" and company B is "+str(self.number2)+". Express in words the total number of employees in both companies."
                            ]
        
        self.problem = random.choice(self.ProblemPool)
        self.answer = f.toWords(self.number1+self.number2)
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain,self.number1+self.number2,
                                       self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ5(self):
        self.problem_type = "ProblemTypeMCQ5"
        
        self.complexity_level = "medium"
        self.HCScore = 5
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.personName = random.sample(PersonName.PersonName,2)
        self.games = random.sample(["football","cricket","hockey","basket-ball"],2)
        self.number1 = randint(30000,50000)
        self.number2 = randint(30000,50000)
        f = Figures2Words.Figures2Words()
        
        self.ProblemPool = [str(self.number1)+" people watched the "+self.games[0]+" and "+str(self.number2)+" watched "+self.games[1]+". Write in words the total viewership for both games.",
                            "Population of town A is "+str(self.number1)+" and town B is "+str(self.number2)+". Write in words the total population of both towns.",
                            self.personName[0]+" bought a car for $"+str(self.number1)+" and "+self.personName[1]+" bought a different car for $"+str(self.number2)+". Write in words the total amount they spent on cars."
                            ]
        
        self.problem = random.choice(self.ProblemPool)
        self.answer = f.toWords(self.number1+self.number2)
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain,self.number1+self.number2,
                                       self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)
    
    def GenerateGenericMCQ(self,problem,answer,problem_type,explain,number,complexity_level,HCScore,grade,CheckAnswerType):
        ''' Generates multiple wrong answers and then pick only 3 wrong and 1 correct and shuffles them.
            Also makes sure the wrong answer doesn't match with the correct answer
            it returns a dictionary with problem, answer (correct answer), template, 4 answers (3 wrong and 1 correct) &
            4 values (for radio buttons). A bug in radio button was taking only first word of the selected answer
            so sending answers in value by removing white spaces'''
        self.template = "MCQTypeProblems.html"
        f =  Figures2Words.Figures2Words()   
        self.wrongAnswers = [f.toWords(number + random.randrange(10,100,10))]
        self.wrongAnswers.append(f.toWords(number - random.randrange(10,100,10)))
        self.wrongAnswers.append(f.toWords(number + random.randrange(200,1000,100)))
        self.wrongAnswers.append(f.toWords(number - random.randrange(200,1000,100)))
        self.wrongAnswers.append(f.toWords(int(str(number)[1:])))
        self.wrongAnswers.append(f.toWords(int(str(number)[:-1])))
        for answers in self.wrongAnswers[:]:
            if answers == answer:
                self.wrongAnswers.remove(answers)              
        self.wrongAnswers = random.sample(self.wrongAnswers,3)
        self.wrongAnswers.append(answer)
        random.shuffle(self.wrongAnswers)
        self.answer1 = str(self.wrongAnswers[0])
        self.answer2 = str(self.wrongAnswers[1])
        self.answer3 = str(self.wrongAnswers[2])
        self.answer4 = str(self.wrongAnswers[3])
        self.value1 = string.join(self.answer1.split(),"")
        self.value2 = string.join(self.answer2.split(),"")
        self.value3 = string.join(self.answer3.split(),"")
        self.value4 = string.join(self.answer4.split(),"")              
        return {'problem':problem,'answer':answer,'template':self.template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'answer4':self.answer4,'value1':self.value1,'value2':self.value2
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type,
                'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}
        
    def checkAnswer(self,template, answer,input,CheckAnswerType):
        ''' Check the answers with the input. It removes all white spaces, "and" and special characters like 
        ("-",",","." so that this method can return true as long as main keywords match)'''
        
        if (template=="MCQTypeProblems.html"):
            input= string.join(input.split(),"")
            answer = string.join(answer.split(),"")
        else:            
            ''' removing " and" with a space in front so that it doesn't remove and from "thousand" '''
            while  answer.partition(" and")[1]!="":
                answer = answer.partition(" and")[0]+answer.partition(" and")[2]
            while  answer.partition(",")[1]!="":
                answer = answer.partition(",")[0]+answer.partition(",")[2]
            while  answer.partition("-")[1]!="":
                answer = answer.partition("-")[0]+answer.partition("-")[2]
            while  answer.partition(".")[1]!="":
                answer = answer.partition(".")[0]+answer.partition(".")[2]

            answer = string.join(answer.split(),"")
            input = str(input)
            while  input.partition(" and")[1]!="":
                input = input.partition(" and")[0]+input.partition(" and")[2]
            while  input.partition(",")[1]!="":
                input = input.partition(",")[0]+input.partition(",")[2]
            while  input.partition("-")[1]!="":
                input = input.partition("-")[0]+input.partition("-")[2]
            input = string.join(input.split(),"")
            
        return (input.lower()==answer.lower())      
        
    def ExplainType1(self,problem,answer,number):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.PlaceValue = ["ones","tens","hundreds"]
        self.Value = {2:"million",1:"thousand"}
        self.ThreeDigitGroup,self.remainder = divmod(len(number),3)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Create a place value table as shown below:<br/>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1><tr>"
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
        if(self.remainder!=0):
            self.solution_text = self.solution_text + "<td colspan="+str(self.remainder)+">"+self.Value[self.ThreeDigitGroup]+"</td>"
            self.solution_text = self.solution_text + "<td>&nbsp;</td>"            
        for i in range(self.ThreeDigitGroup-1):
            self.solution_text = self.solution_text + "<td colspan=3>"+self.Value[self.ThreeDigitGroup-1]+"</td>"
            self.solution_text = self.solution_text + "<td>&nbsp;</td>"
        self.solution_text = self.solution_text + "<td colspan=3></td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        self.solution_text = self.solution_text + "based on above table you can write the number as:<br/>"
        self.solution_text = self.solution_text + "<i><b>"+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain                      

    def ExplainType2(self,problem,answer,amount1,amount2):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.PlaceValue = ["ones","tens","hundreds"]
        self.Value = {2:"million",1:"thousand"}
        number = str(amount1+amount2)
        self.ThreeDigitGroup,self.remainder = divmod(len(number),3)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Total = "+str(amount1)+" + "+str(amount2)+" = "+number+"<br/><br/>"
        self.solution_text = self.solution_text + "Create a place value table as shown below:<br/>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1><tr>"
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
        if(self.remainder!=0):
            self.solution_text = self.solution_text + "<td colspan="+str(self.remainder)+">"+self.Value[self.ThreeDigitGroup]+"</td>"
            self.solution_text = self.solution_text + "<td>&nbsp;</td>"            
        for i in range(self.ThreeDigitGroup-1):
            self.solution_text = self.solution_text + "<td colspan=3>"+self.Value[self.ThreeDigitGroup-1]+"</td>"
            self.solution_text = self.solution_text + "<td>&nbsp;</td>"
        self.solution_text = self.solution_text + "<td colspan=3></td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        self.solution_text = self.solution_text + "based on above table you can write the number as:<br/>"
        self.solution_text = self.solution_text + "<i><b>"+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain         