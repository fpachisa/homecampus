'''
Created on Mar 19, 2012
Module: MTTimeDuration
Generates the "Calculating Time Duration" problems for Primary 4

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
import string

class MTTimeDuration:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType3",],
                            3:["ProblemTypeMCQ1",],
                            4:["ProblemType2",],
                            5:["ProblemType4",],
                            6:["ProblemTypeMCQ2",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType3(),],
                                    3:[self.GenerateProblemTypeMCQ1(),],
                                    4:[self.GenerateProblemType2(),],
                                    5:[self.GenerateProblemType4(),],
                                    6:[self.GenerateProblemTypeMCQ2(),],
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
        #return self.GenerateProblemTypeMCQ2()

    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g.:
        Find the time elapsed in minutes between 11.30 am and 12.40 pm:'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        # Total number of minutes in a day is 1440
        self.number1 = randint(0,1239)
        self.number2 = self.number1 + randint(10,200)

        self.hour1,self.minute1 = divmod(self.number1,60)
        self.hour2,self.minute2 = divmod(self.number2,60)

        if self.hour1 < 12:
            self.time1 = "a.m."
        else:
            self.time1 = "p.m."
        if self.hour2 < 12:
            self.time2 = "a.m."
        else:
            self.time2 = "p.m."
            
        if self.hour1 == 0:
            self.hour1 = 12
        elif self.hour1 > 12:
            self.hour1 = self.hour1 - 12
        if self.hour2 == 0:
            self.hour2 = 12
        elif self.hour2 > 12:
            self.hour2 = self.hour2 - 12          
        
        if self.minute1 < 10:
            self.minute1 = '0'+str(self.minute1)
        if self.minute2 < 10:
            self.minute2 = '0'+str(self.minute2)

        self.problem = "Find the time elapsed in minutes between:<br><br>"
        self.problem = self.problem + str(self.hour1)+"."+str(self.minute1)+" "+self.time1+" and "
        self.problem = self.problem + str(self.hour2)+"."+str(self.minute2)+" "+self.time2
        
        self.answer = self.number2 - self.number1
        
        self.template = "EnterTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.time1,self.time2,self.hour1,self.hour2,self.minute1,self.minute2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":"minutes"}            

    def ExplainType1(self,problem,answer,number1,number2,time1,time2,hour1,hour2,minute1,minute2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" minutes"
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g.:
        Find the time elapsed in minutes between 11.30 am and 12.40 pm:'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        # Total number of minutes in a day is 1440
        self.number1 = randint(0,1409)
        self.number2 = self.number1 + randint(5,30)

        self.hour1,self.minute1 = divmod(self.number1,60)
        self.hour2,self.minute2 = divmod(self.number2,60)

        if self.hour1 < 12:
            self.time1 = "a.m."
        else:
            self.time1 = "p.m."
        if self.hour2 < 12:
            self.time2 = "a.m."
        else:
            self.time2 = "p.m."
            
        if self.hour1 == 0:
            self.hour1 = 12
        elif self.hour1 > 12:
            self.hour1 = self.hour1 - 12
        if self.hour2 == 0:
            self.hour2 = 12
        elif self.hour2 > 12:
            self.hour2 = self.hour2 - 12          
        
        if self.minute1 < 10:
            self.minute1 = '0'+str(self.minute1)
        if self.minute2 < 10:
            self.minute2 = '0'+str(self.minute2)

        self.problem = "Find the time elapsed in seconds between:<br><br>"
        self.problem = self.problem + str(self.hour1)+"."+str(self.minute1)+" "+self.time1+" and "
        self.problem = self.problem + str(self.hour2)+"."+str(self.minute2)+" "+self.time2
        
        self.answer = (self.number2 - self.number1)*60
        
        self.template = "EnterTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.time1,self.time2,self.hour1,self.hour2,self.minute1,self.minute2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":"seconds"}            

    def ExplainType2(self,problem,answer,number1,number2,time1,time2,hour1,hour2,minute1,minute2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" seconds"
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g.:
        Find the time elapsed in minutes between 11.30 am and 12.40 pm:'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        # Total number of minutes in a day is 1440
        self.number1 = randint(0,1409)
        self.number2 = self.number1 + randint(5,30)

        self.hour1,self.minute1 = divmod(self.number1,60)
        self.hour2,self.minute2 = divmod(self.number2,60)
           
        if self.hour1 < 10:
            self.hour1 = '0'+str(self.hour1)
        if self.hour2 < 10:
            self.hour2 = '0'+str(self.hour2)
        
        if self.minute1 < 10:
            self.minute1 = '0'+str(self.minute1)
        if self.minute2 < 10:
            self.minute2 = '0'+str(self.minute2)

        self.problem = "Find the time elapsed in seconds between:<br><br>"
        self.problem = self.problem + str(self.hour1)+" "+str(self.minute1)+" and "
        self.problem = self.problem + str(self.hour2)+" "+str(self.minute2)
        
        self.answer = (self.number2 - self.number1)*60
        
        self.template = "EnterTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.hour1,self.hour2,self.minute1,self.minute2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":"seconds"}            

    def ExplainType3(self,problem,answer,number1,number2,hour1,hour2,minute1,minute2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" seconds"
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g.:
        Find the time elapsed in minutes between 11.30 am and 12.40 pm:'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        # Total number of minutes in a day is 1440
        self.number1 = randint(0,1239)
        self.number2 = self.number1 + randint(10,200)

        self.hour1,self.minute1 = divmod(self.number1,60)
        self.hour2,self.minute2 = divmod(self.number2,60)

        if self.hour1 < 10:
            self.hour1 = '0'+str(self.hour1)
        if self.hour2 < 10:
            self.hour2 = '0'+str(self.hour2)
        
        if self.minute1 < 10:
            self.minute1 = '0'+str(self.minute1)
        if self.minute2 < 10:
            self.minute2 = '0'+str(self.minute2)

        self.problem = "Find the time elapsed in minutes between:<br><br>"
        self.problem = self.problem + str(self.hour1)+" "+str(self.minute1)+" and "
        self.problem = self.problem + str(self.hour2)+" "+str(self.minute2)
        
        self.answer = self.number2 - self.number1
        
        self.template = "EnterTypeProblems.html"        

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.hour1,self.hour2,self.minute1,self.minute2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,"unit":"minutes"}            

    def ExplainType4(self,problem,answer,number1,number2,hour1,hour2,minute1,minute2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" minutes"
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore,grade,CheckAnswerType):
        
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
            self.value1 = string.join(self.answer1.split(),"")
            self.value2 = string.join(self.answer2.split(),"")
            self.value3 = string.join(self.answer3.split(),"")
            self.value4 = string.join(self.answer4.split(),"")
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'answer4':self.answer4,'value1':self.value1,'value2':self.value2
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type,
                'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}      

    def GenerateProblemTypeMCQ1(self):        
        '''e.g.:
        Find the time elapsed in minutes between 11.30 am and 12.40 pm:'''
                
        self.problem_type = "ProblemTypeMCQ1"
        self.complexity_level = "medium"
        self.HCScore = 5
        self.CheckAnswerType = 2
        self.grade = 4
       
        # Total number of minutes in a day is 1440
        self.number1 = randint(0,1300)
        self.number2 = randint(0,1439)
        
        if self.number1 == self.number2:
            self.number2 = self.number1 + 75
            
        if self.number1 > self.number2:
            self.TempNumber = self.number1
            self.number1 = self.number2
            self.number2 = self.TempNumber

        self.hour1,self.minute1 = divmod(self.number1,60)
        self.hour2,self.minute2 = divmod(self.number2,60)

        if self.hour1 < 12:
            self.time1 = "a.m."
        else:
            self.time1 = "p.m."
        if self.hour2 < 12:
            self.time2 = "a.m."
        else:
            self.time2 = "p.m."
            
        if self.hour1 == 0:
            self.hour1 = 12
        elif self.hour1 > 12:
            self.hour1 = self.hour1 - 12
        if self.hour2 == 0:
            self.hour2 = 12
        elif self.hour2 > 12:
            self.hour2 = self.hour2 - 12          
        
        if self.minute1 < 10:
            self.minute1 = '0'+str(self.minute1)
        if self.minute2 < 10:
            self.minute2 = '0'+str(self.minute2)

        self.problem = "Find the time elapsed between:<br><br>"
        self.problem = self.problem + str(self.hour1)+"."+str(self.minute1)+" "+self.time1+" and "
        self.problem = self.problem + str(self.hour2)+"."+str(self.minute2)+" "+self.time2
        
        self.answer1,self.answer2 = divmod((self.number2 - self.number1),60)
        self.answer = str(self.answer1)+" hr "+str(self.answer2)+" min"
        
        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        for i in range(3):
            self.WrongAnswer1,self.WrongAnswer2 = divmod((self.number2 - self.number1 + 5*i),60)
            self.wrongAnswers.append(str(self.WrongAnswer1)+" hr "+str(self.WrongAnswer2)+" min")
        
        if self.number2 - self.number1 > 10:
            self.WrongAnswer1,self.WrongAnswer2 = divmod((self.number2 - self.number1 - 5),60)
            self.wrongAnswers.append(str(self.WrongAnswer1)+" hr "+str(self.WrongAnswer2)+" min")
            self.WrongAnswer1,self.WrongAnswer2 = divmod((self.number2 - self.number1 - 10),60)
            self.wrongAnswers.append(str(self.WrongAnswer1)+" hr "+str(self.WrongAnswer2)+" min")
        elif self.number2 - self.number1 > 5:
            self.WrongAnswer1,self.WrongAnswer2 = divmod((self.number2 - self.number1 - 5),60)
            self.wrongAnswers.append(str(self.WrongAnswer1)+" hr "+str(self.WrongAnswer2)+" min")           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ1(self.problem,self.answer,self.number1,self.number2,self.time1,self.time2,self.hour1,self.hour2,self.minute1,self.minute2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def ExplainTypeMCQ1(self,problem,answer,number1,number2,time1,time2,hour1,hour2,minute1,minute2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ2(self):        
        '''e.g.:
        Find the time elapsed in minutes between 11.30 am and 12.40 pm:'''
                
        self.problem_type = "ProblemTypeMCQ2"
        self.complexity_level = "medium"
        self.HCScore = 5
        self.CheckAnswerType = 2
        self.grade = 4
       
        # Total number of minutes in a day is 1440
        self.number1 = randint(0,1300)
        self.number2 = randint(0,1439)
        
        if self.number1 == self.number2:
            self.number2 = self.number1 + 75
            
        if self.number1 > self.number2:
            self.TempNumber = self.number1
            self.number1 = self.number2
            self.number2 = self.TempNumber

        self.hour1,self.minute1 = divmod(self.number1,60)
        self.hour2,self.minute2 = divmod(self.number2,60)

        if self.hour1 < 10:
            self.hour1 = '0'+str(self.hour1)
        if self.hour2 < 10:
            self.hour2 = '0'+str(self.hour2)          
        
        if self.minute1 < 10:
            self.minute1 = '0'+str(self.minute1)
        if self.minute2 < 10:
            self.minute2 = '0'+str(self.minute2)

        self.problem = "Find the time elapsed between:<br><br>"
        self.problem = self.problem + str(self.hour1)+" "+str(self.minute1)+" and "
        self.problem = self.problem + str(self.hour2)+" "+str(self.minute2)
        
        self.answer1,self.answer2 = divmod((self.number2 - self.number1),60)
        self.answer = str(self.answer1)+" hr "+str(self.answer2)+" min"
        
        self.template = "MCQTypeProblems.html"
               
        self.wrongAnswers = []    
        for i in range(3):
            self.WrongAnswer1,self.WrongAnswer2 = divmod((self.number2 - self.number1 + 5*i),60)
            self.wrongAnswers.append(str(self.WrongAnswer1)+" hr "+str(self.WrongAnswer2)+" min")
        
        if self.number2 - self.number1 > 10:
            self.WrongAnswer1,self.WrongAnswer2 = divmod((self.number2 - self.number1 - 5),60)
            self.wrongAnswers.append(str(self.WrongAnswer1)+" hr "+str(self.WrongAnswer2)+" min")
            self.WrongAnswer1,self.WrongAnswer2 = divmod((self.number2 - self.number1 - 10),60)
            self.wrongAnswers.append(str(self.WrongAnswer1)+" hr "+str(self.WrongAnswer2)+" min")
        elif self.number2 - self.number1 > 5:
            self.WrongAnswer1,self.WrongAnswer2 = divmod((self.number2 - self.number1 - 5),60)
            self.wrongAnswers.append(str(self.WrongAnswer1)+" hr "+str(self.WrongAnswer2)+" min")           
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ2(self.problem,self.answer,self.number1,self.number2,self.hour1,self.hour2,self.minute1,self.minute2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def ExplainTypeMCQ2(self,problem,answer,number1,number2,hour1,hour2,minute1,minute2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
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
                return string.join(answer.split(),"")==str(InputAnswer)
            except ValueError:
                return False                       