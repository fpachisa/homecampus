'''
Created on Jan 18, 2011

Module: MultiplyDivide
Generates "Find the Pattern" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random
from random import randint

class MultiplyDivide:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        random = randint(1,2)
        if random==1:
            if randint(1,2)==1:
                return self.GenerateProblemType1()
            else:
                return self.GenerateProblemTypeMCQ1()
        elif random==2:
            if randint(1,2)==1:
                return self.GenerateProblemType2()
            else:
                return self.GenerateProblemTypeMCQ2()
        #return self.GenerateProblemTypeMCQ2()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:"ProblemType1",2:"ProblemTypeMCQ2",3:"ProblemTypeMCQ1",4:"ProblemType2",}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemTypeMCQ2(),3:self.GenerateProblemTypeMCQ1(),
                                    4:self.GenerateProblemType2()}
        
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(self.GenerateProblemType.values())
        else:
            if LastProblemID in self.ProblemType.values():
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if v == LastProblemID][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return self.GenerateProblemType[NextProblemKey]
            else:
                return random.choice(self.GenerateProblemType.values())
        #return self.GenerateProblemType1()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g.:
        What is 382 x 1000?'''
        
        '''Randomly selecting one type out of the below where last one getting max weightage'''
        randomSelect = randint(1,8)
        if randomSelect==1:
            '''randomly generating even numbers between 8 & 88'''
            self.number = random.choice(range(8,88,2))
            self.multiplier = random.choice([5,50])
            self.flag = 1
        elif randomSelect==2:
            '''randomly generating multiples of 4 between 8 & 88'''
            self.number = random.choice(range(8,88,4))
            self.multiplier = random.choice([25,50])
            self.flag = 2
        elif randomSelect==3:
            '''randomly generating multiples of 5 between 15 & 95'''
            self.number = random.choice(range(15,95,5))
            self.multiplier = random.choice([20,40])
            self.flag = 3
        elif randomSelect==4:
            self.tens =  int(round(randint(11,94),-1))
            self.hunderds = int(round(randint(111,949),-2))
            self.thousands = int(round(randint(1111,9499),-3))
            self.number = random.choice([self.tens,self.hunderds,self.thousands])
            self.multiplier = random.choice([self.tens,self.hunderds,self.thousands])
            self.flag = 4
        else:
            self.number = randint(11,888)
            self.multiplier = random.choice([10,100,1000])
            self.flag = 5
                                
        self.problem="What is %d &times; %d?"%(self.number,self.multiplier)
        self.answer = self.number*self.multiplier          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.number,self.multiplier,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1"}

    def ExplainType1(self,problem,answer,number,multiplier,flag):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        if flag==1:
            self.solution_text = self.solution_text + "Let's first break the number "+str(number)+" as : "+str(number/2)+" &times; 2<br><br>"
            self.solution_text = self.solution_text + "So, "+str(number)+" &times; "+str(multiplier)+" = "+str(number/2)+" &times; 2 &times; "+str(multiplier)+"<br><br>"
            self.solution_text = self.solution_text + " = "+str(number/2)+" &times; "+str(2*multiplier)+"<br><br>"
            if (multiplier==5):
                self.solution_text = self.solution_text + " Since multiplying by 10 means adding 1 zero to the number"
                self.solution_text = self.solution_text + "= "+str(number/2)+" <span style='color:red'>0"
            elif (multiplier==50):
                self.solution_text = self.solution_text + " Since multiplying by 100 means adding 2 zeroes to the number"
                self.solution_text = self.solution_text + " = "+str(number/2)+" <span style='color:red'>00"
        if flag==2:
            if (multiplier==50):
                self.solution_text = self.solution_text + "Let's first break the number "+str(number)+" as : "+str(number/2)+" &times; 2<br><br>"
                self.solution_text = self.solution_text + "So, "+str(number)+" &times; "+str(multiplier)+" = "+str(number/2)+" &times; 2 &times; "+str(multiplier)+"<br><br>"
                self.solution_text = self.solution_text + " = "+str(number/2)+" &times; "+str(2*multiplier)+"<br><br>"
                self.solution_text = self.solution_text + " Since multiplying by 100 means adding 2 zeroes to the number"
                self.solution_text = self.solution_text + "= "+str(number/2)+" <span style='color:red'>00"
            elif (multiplier==25):
                self.solution_text = self.solution_text + "Let's first break the number "+str(number)+" as : "+str(number/4)+" &times; 4<br><br>"
                self.solution_text = self.solution_text + "So, "+str(number)+" &times; "+str(multiplier)+" = "+str(number/4)+" &times; 4 &times; "+str(multiplier)+"<br><br>"
                self.solution_text = self.solution_text + " = "+str(number/4)+" &times; "+str(4*multiplier)+"<br><br>"
                self.solution_text = self.solution_text + " Since multiplying by 100 means adding 2 zeroes to the number"
                self.solution_text = self.solution_text + "= "+str(number/4)+" <span style='color:red'>00"                
        if flag==3:
            if (multiplier==20):
                self.solution_text = self.solution_text + "Let's first break the number "+str(number)+" as : "+str(number/5)+" &times; 5<br><br>"
                self.solution_text = self.solution_text + "So, "+str(number)+" &times; "+str(multiplier)+" = "+str(number/5)+" &times; 5 &times; "+str(multiplier)+"<br><br>"
                self.solution_text = self.solution_text + " = "+str(number/5)+" &times; "+str(5*multiplier)+"<br><br>"
                self.solution_text = self.solution_text + " Since multiplying by 100 means adding 2 zeroes to the number"
                self.solution_text = self.solution_text + "= "+str(number/5)+" <span style='color:red'>00"
            elif (multiplier==40):
                self.solution_text = self.solution_text + "Let's first break the number "+str(number)+" as : "+str(number/5)+" &times; 5<br><br>"
                self.solution_text = self.solution_text + "So, "+str(number)+" &times; "+str(multiplier)+" = "+str(number/5)+" &times; 5 &times; "+str(multiplier)+"<br><br>"
                self.solution_text = self.solution_text + " This can be further broken down to :"+str(number/5)+" &times; 5 &times; 2 &times; "+str(multiplier/2)+"<br><br>"
                self.solution_text = self.solution_text + " = "+str(number/5)+" &times; 2 &times; "+str(5*multiplier/2)+"<br><br>"
                self.solution_text = self.solution_text + " Since multiplying by 100 means adding 2 zeroes to the number"
                self.solution_text = self.solution_text + "= "+str(number*2/5)+" <span style='color:red'>00" 
        if flag==4:
            self.solution_text = self.solution_text + "Multiply the first digits and add remaining zeroes to the multiplied number"
        if flag==5:
            if (multiplier==10):
                self.solution_text = self.solution_text + "Multiplying a number by 10 means adding 1 zero to the number"
                self.solution_text = self.solution_text + "= "+str(number)+" <span style='color:red'>0"
            elif (multiplier==100):
                self.solution_text = self.solution_text + "Multiplying a number by 100 means adding 2 zeroes to the number"
                self.solution_text = self.solution_text + "= "+str(number)+" <span style='color:red'>00"
            elif (multiplier==1000):
                self.solution_text = self.solution_text + "Multiplying a number by 1000 means adding 3 zeroes to the number"
                self.solution_text = self.solution_text + "= "+str(number)+" <span style='color:red'>000"                
        self.solution_text = self.solution_text + "</span><br><br><i><b>Hence the correct answer is "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain   

    def GenerateProblemType2(self):
        '''e.g.:
        Divide 150 by 30'''

        self.tens =  int(round(randint(11,94),-1))
        self.hunderds = int(round(randint(111,949),-2))
        self.thousands = int(round(randint(1111,9499),-3))
        self.divisor = random.choice([self.tens,self.hunderds,self.thousands])
        self.answer = randint(3,20)
        self.number = self.divisor * self.answer
                                
        self.problem="Divide %d by %d"%(self.number,self.divisor)
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,str(self.answer),self.number,self.divisor)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2"}

    def ExplainType2(self,problem,answer,number,divisor):
        if len(str(divisor))==2:
            divisor1 = 10
        elif len(str(divisor))==3:
            divisor1 = 100
        else:
            divisor1 = 1000
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "The problem "+str(number)+" &divide; "+str(divisor)+" can be expressed as "+str(number)+" &divide; "+str(divisor1)+" &divide; "+str(divisor/divisor1)+"<br><br>"
        if divisor1 == 10:
            self.solution_text = self.solution_text + "First divide "+str(number)+" by "+str(divisor1)+" which means remove 1 zero from the number and divide by "+str(divisor/divisor1)+"<br><br>"
        if divisor1 == 100:
            self.solution_text = self.solution_text + "First divide "+str(number)+" by "+str(divisor1)+" which means remove 2 zeroes from the number and divide by "+str(divisor/divisor1)+"<br><br>"
        if divisor1 == 1000:
            self.solution_text = self.solution_text + "First divide "+str(number)+" by "+str(divisor1)+" which means remove 3 zeroes from the number and divide by "+str(divisor/divisor1)+"<br><br>"
        self.solution_text = self.solution_text +"= "+str(number/divisor1)+" &divide; "+str(divisor/divisor1)+"<br><br>"
        self.solution_text = self.solution_text +"= "+answer
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain   

    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type):
        
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
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type}
        

    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        What is 382 x 1000?'''
        
        '''Randomly selecting one type out of the below where last one getting max weightage'''
        self.problem_type = "ProblemTypeMCQ1"
        self.wrongAnswers = []
        randomSelect = randint(1,8)
        if randomSelect==1:
            '''randomly generating even numbers between 8 & 88'''
            self.number = random.choice(range(8,88,2))
            self.multiplier = random.choice([5,50])
            self.wrongAnswers.append(str(self.number*5))
            self.wrongAnswers.append(str(self.number*50))
            self.flag = 1
        elif randomSelect==2:
            '''randomly generating multiples of 4 between 8 & 88'''
            self.number = random.choice(range(8,88,4))
            self.multiplier = random.choice([25,50])
            self.wrongAnswers.append(str(self.number*25))
            self.wrongAnswers.append(str(self.number*50))
            self.flag = 2
        elif randomSelect==3:
            '''randomly generating multiples of 5 between 15 & 95'''
            self.number = random.choice(range(15,95,5))
            self.multiplier = random.choice([20,40])
            self.wrongAnswers.append(str(self.number*20))
            self.wrongAnswers.append(str(self.number*40))
            self.flag = 3
        elif randomSelect==4:
            self.tens =  int(round(randint(11,94),-1))
            self.hunderds = int(round(randint(111,949),-2))
            self.thousands = int(round(randint(1111,9499),-3))
            self.number = random.choice([self.tens,self.hunderds,self.thousands])
            self.multiplier = random.choice([self.tens,self.hunderds,self.thousands])
            self.flag = 4
        else:
            self.number = randint(11,888)
            self.multiplier = random.choice([10,100,1000])
            self.flag = 5
                                
        self.problem="What is %d x %d?"%(self.number,self.multiplier)
        self.answer = self.number*self.multiplier          
        
        self.template = "MCQTypeProblems.html"

        self.wrongAnswers.append(str(self.answer*10))
        self.wrongAnswers.append(str(self.answer/10))
        self.wrongAnswers.append(str(int(self.answer/100)))
        self.wrongAnswers.append(str(int(round(self.answer,-1))))
        self.wrongAnswers.append(str(int(round(self.answer,-2))))
        self.wrongAnswers.append(str(int(round(self.answer,-3))))

        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.number,self.multiplier,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)            

    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        Divide 150 by 30'''
        self.problem_type = "ProblemTypeMCQ2"
        '''Randomly selecting one type out of the below where last one getting max weightage'''
        self.tens =  int(round(randint(11,94),-1))
        self.hunderds = int(round(randint(111,949),-2))
        self.thousands = int(round(randint(1111,9499),-3))
        self.divisor = random.choice([self.tens,self.hunderds,self.thousands])
        self.answer = randint(3,20)
        self.number = self.divisor * self.answer
                                
        self.problem="Divide %d by %d"%(self.number,self.divisor)         
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers=[]        
        for _i in range(15):
            wrongAnswer = randint(3,20)
            if str(wrongAnswer) not in self.wrongAnswers:
                self.wrongAnswers.append(str(wrongAnswer))

        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,str(self.answer),self.number,self.divisor)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)

    def checkAnswer(self,template,answer,InputAnswer):
        try:
            return (int(answer)==int(InputAnswer))
        except ValueError:
            return False  