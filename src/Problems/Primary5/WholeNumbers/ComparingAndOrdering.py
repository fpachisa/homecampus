'''
Created on Jan 17, 2011

Module: ComparingAndOrdering
Generates the Comparing and Ordering problems for Primary 5

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

class ComparingAndOrdering:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        random = randint(1,6)
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
        elif random==3:
            if randint(1,2)==1:
                return self.GenerateProblemType3()
            else:
                return self.GenerateProblemTypeMCQ3()
        elif random==4:
            if randint(1,2)==1:
                return self.GenerateProblemType4()
            else:
                return self.GenerateProblemTypeMCQ4()
        elif random==5:
            return self.GenerateProblemTypeMCQ5()
        elif random==6:
            return self.GenerateProblemTypeMCQ6()
        #return self.GenerateProblemTypeMCQ5()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:"ProblemType1",2:"ProblemTypeMCQ2",3:"ProblemType3",4:"ProblemTypeMCQ4",5:"ProblemTypeMCQ5",
                            6:"ProblemTypeMCQ6",7:"ProblemTypeMCQ1",8:"ProblemType2",9:"ProblemTypeMCQ3",10:"ProblemType4"}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemTypeMCQ2(),3:self.GenerateProblemType3(),
                                    4:self.GenerateProblemTypeMCQ4(),5:self.GenerateProblemTypeMCQ5(),6:self.GenerateProblemTypeMCQ6(),
                                    7:self.GenerateProblemTypeMCQ1(),8:self.GenerateProblemType2(),9:self.GenerateProblemTypeMCQ3(),
                                    10:self.GenerateProblemType4()}
        
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
        #return self.GenerateProblemTypeMCQ5()                       
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            }
        return self.ProblemType[problem_type]
    
    def GenerateProblemType1(self):
        '''e.g.
        Which number is the greatest:
        708560
        693129
        663470
        711572
        '''
        i=0
        self.numbers=[]
        while i!=4:
            number = randint(100000,999999)           
            if(number not in self.numbers):
                self.numbers.append(number)
                i=i+1
        self.problem = "Which number is the greatest:<br>%d<br>%d<br>%d<br>%d"%(self.numbers[0],self.numbers[1],
                                                                    self.numbers[2],self.numbers[3])
        
        self.answer = max(self.numbers)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1"}

    def ExplainType1(self,problem,answer,numbers):
        k = 0
        self.place = {1:"first",2:"second",3:"third",4:"fourth",5:"fifth",6:"sixth"}
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "In order to find out the greatest number, lets compare each digit of the given numbers.<br>"
        while len(numbers)!=1:
            numbersDigit=[]
            j=0
            for i in range(len(numbers)):
                numbersDigit.append(int(str(numbers[i])[k]))
            self.solution_text = self.solution_text + "Lets compare the "+self.place[k+1]+" digit of each number<br>"
            self.solution_text = self.solution_text + "i.e. compare the digits "+str(numbersDigit)+"<br>"
            for i in range(len(numbersDigit)):
                if numbersDigit[i]!=max(numbersDigit):
                    del numbers[i-j]
                    j=j+1
            if len(numbers)>1:
                self.solution_text = self.solution_text + "Smallest out of these digits is "+str(min(numbersDigit))+" which belongs to numbers "+str(numbers)+". So we cannot determine the greatest number by this digit <br>"
            k=k+1
        self.solution_text = self.solution_text + "Greatest out of these digits is "+str(max(numbersDigit))+" which belongs to number "+answer
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the greatest number is "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.
        Which number is the smallest:
        708560
        693129
        663470
        711572
        '''
        i=0
        self.numbers=[]
        while i!=4:
            number = randint(100000,999999)           
            if(number not in self.numbers):
                self.numbers.append(number)
                i=i+1
        self.problem = "Which number is the smallest:<br>%d<br>%d<br>%d<br>%d"%(self.numbers[0],self.numbers[1],
                                                                    self.numbers[2],self.numbers[3])
        
        self.answer = min(self.numbers)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2"}

    def ExplainType2(self,problem,answer,numbers):
        k = 0
        self.place = {1:"first",2:"second",3:"third",4:"fourth",5:"fifth",6:"sixth"}
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "In order to find out the smallest number, lets compare each digit of the given numbers.<br>"
        while len(numbers)!=1:
            numbersDigit=[]
            j=0
            for i in range(len(numbers)):
                numbersDigit.append(int(str(numbers[i])[k]))
            self.solution_text = self.solution_text + "Lets compare the "+self.place[k+1]+" digit of each number<br>"
            self.solution_text = self.solution_text + "i.e. compare the digits "+str(numbersDigit)+"<br>"
            for i in range(len(numbersDigit)):
                if numbersDigit[i]!=min(numbersDigit):
                    del numbers[i-j]
                    j=j+1
            if len(numbers)>1:
                self.solution_text = self.solution_text + "Smallest out of these digits is "+str(min(numbersDigit))+" which belongs to numbers "+str(numbers)+". So we cannot determine the smallest number by this digit <br>"
            k=k+1
        self.solution_text = self.solution_text + "Smallest out of these digits is "+str(min(numbersDigit))+" which belongs to number "+answer
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the smallest number is "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):
        '''e.g.
        Rearrange the following digit to form the greatest possible 6 digit number:
        7 8 3 1 5 9'''        
        self.digits = random.sample([0,1,2,3,4,5,6,7,8,9], 6)
        
        self.problem = "Rearrange the following digit to form the greatest possible 6 digit number:<br>%d %d %d %d %d %d"%(self.digits[0],self.digits[1],
                                                                                                                       self.digits[2],self.digits[3],
                                                                                                                       self.digits[4],self.digits[5])
        
        self.greatest = ""
        """Sorting the digits in descending order"""
        self.digits.sort(reverse=True)
        for i in range(len(self.digits)):
            self.greatest=self.greatest+str(self.digits[i])
                
        self.answer = int(self.greatest)
        
        self.template = "EnterTypeProblems.html"                           

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.digits)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3"}

    def ExplainType3(self,problem,answer,digits):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "First arrange the given digits from greatest to smallest as shown:"
        self.solution_text = self.solution_text + str(digits)
        self.solution_text = self.solution_text + "<br>Writing down this digits together give us the number:"+answer+"<br>"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the greatest possible six digit number is "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4(self):
        self.digits = random.sample([0,1,2,3,4,5,6,7,8,9], 6)
        
        self.problem = "Rearrange the following digit to form the smallest possible 6 digit number:<br>%d %d %d %d %d %d"%(self.digits[0],self.digits[1],
                                                                                                                       self.digits[2],self.digits[3],
                                                                                                                       self.digits[4],self.digits[5])
        
        self.greatest = ""
        
        self.digits.sort()
        for i in range(len(self.digits)):
            self.greatest=self.greatest+str(self.digits[i])
                
        self.answer = int(self.greatest)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,str(self.answer),self.digits)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4"}

    def ExplainType4(self,problem,answer,digits):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "First arrange the given digits from smallest to greatest as shown:"
        self.solution_text = self.solution_text + str(digits)
        if digits[0] == 0:
            self.solution_text = self.solution_text + "<br>Since 0 is the first digit, ignore 0"
            self.solution_text = self.solution_text + "<br>Writing down the remaining digits together give us the number:"+answer+"<br>"
        else:
            self.solution_text = self.solution_text + "<br>Writing down this digits together give us the number: "+answer+"<br>"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the smallest possible six digit number is "+answer+"</b></i>"
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
        '''e.g.
        Which number is the greatest:
        708560
        693129
        663470
        711572
        '''
        self.problem_type = "ProblemTypeMCQ1"
        i=0
        self.numbers=[]
        while i!=4:
            number = randint(100000,999999)           
            if(number not in self.numbers):
                self.numbers.append(number)
                i=i+1
        
        self.problem = "Which number is the greatest:<br>%d<br>%d<br>%d<br>%d"%(self.numbers[0],self.numbers[1],
                                                                    self.numbers[2],self.numbers[3])
        
        self.answer = max(self.numbers)
        
        self.template = "MCQTypeProblems.html"
        
        '''List of wrong answers is same as the list of numbers displayed'''
        self.wrongAnswers = list(self.numbers)    
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)

    def GenerateProblemTypeMCQ2(self):
        '''e.g.
        Which number is the smallest:
        708560
        693129
        663470
        711572
        '''
        self.problem_type = "ProblemTypeMCQ2"
        i=0
        self.numbers=[]
        while i!=4:
            number = randint(100000,999999)           
            if(number not in self.numbers):
                self.numbers.append(number)
                i=i+1
        
        self.problem = "Which number is the smallest:<br>%d<br>%d<br>%d<br>%d"%(self.numbers[0],self.numbers[1],
                                                                    self.numbers[2],self.numbers[3])
        
        self.answer = min(self.numbers)
        
        self.template = "MCQTypeProblems.html"
        
        '''List of wrong answers is same as the list of numbers displayed'''
        self.wrongAnswers = list(self.numbers)    
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,str(self.answer),self.numbers)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)

    def GenerateProblemTypeMCQ3(self):
        '''e.g.
        Rearrange the following digit to form the greatest possible 6 digit number:
        7 8 3 1 5 9
        
        853179
        513978
        987531
        918357'''
        self.problem_type = "ProblemTypeMCQ3"
        self.digits = random.sample([0,1,2,3,4,5,6,7,8,9], 6)
        
        self.problem = "Rearrange the following digit to form the greatest possible 6 digit number:<br>%d %d %d %d %d %d"%(self.digits[0],self.digits[1],
                                                                                                                       self.digits[2],self.digits[3],
                                                                                                                       self.digits[4],self.digits[5])
        
        self.greatest = ""
        """Sorting the digits in descending order"""
        self.digits.sort(reverse=True)
        for i in range(len(self.digits)):
            self.greatest=self.greatest+str(self.digits[i])
                
        self.answer = int(self.greatest)
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers =[]      
        '''Generate as many wrong answers as possible..here generating 6 wrong answers'''
        self.digits1 = list(self.digits)
        for _j in range(6):
            random.shuffle(self.digits1)
            self.wrongAnswer=""
            for i in range(len(self.digits1)):
                self.wrongAnswer=self.wrongAnswer+str(self.digits1[i])
            self.wrongAnswers.append(self.wrongAnswer)   
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.digits)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)

    def GenerateProblemTypeMCQ4(self):
        '''e.g.
        Rearrange the following digit to form the smallest possible 6 digit number:
        7 8 3 1 5 9
        
        853179
        513978
        987531
        918357'''
        self.problem_type = "ProblemTypeMCQ4"
        self.digits = random.sample([0,1,2,3,4,5,6,7,8,9], 6)
        
        self.problem = "Rearrange the following digit to form the smallest possible 6 digit number:<br>%d %d %d %d %d %d"%(self.digits[0],self.digits[1],
                                                                                                                       self.digits[2],self.digits[3],
                                                                                                                       self.digits[4],self.digits[5])
        
        self.greatest = ""
        """Sorting the digits in ascending order"""
        self.digits.sort()
        for i in range(len(self.digits)):
            self.greatest=self.greatest+str(self.digits[i])
                
        self.answer = int(self.greatest)
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers =[]      
        '''Generate as many wrong answers as possible..here generating 6 wrong answers'''
        self.digits1 = list(self.digits)
        for _j in range(6):
            random.shuffle(self.digits1)
            self.wrongAnswer=""
            for i in range(len(self.digits1)):
                self.wrongAnswer=self.wrongAnswer+str(self.digits1[i])
            self.wrongAnswers.append(self.wrongAnswer)   
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,str(self.answer),self.digits)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)

    def GenerateProblemTypeMCQ5(self):
        '''e.g.
        Arrange these numbers in increasing order:
        855945 301168 752315 419153
        
        301168,752315,419153,855945
        752315,301168,855945,419153
        301168,419153,752315,855945
        855945,419153,752315,301168'''
        self.problem_type = "ProblemTypeMCQ5"
        self.numbers=[]
        i=0
        while i!=4:
            number = randint(100000,999999)
            if (number not in self.numbers):
                self.numbers.append(number)
                i=i+1
        
        self.problem = "Arrange these numbers in increasing order:<br>%d %d %d %d"%(self.numbers[0],self.numbers[1],
                                                                                    self.numbers[2],self.numbers[3])

        """Sorting the numbers in ascending order"""
        self.numbers.sort()
                       
        self.answer = str(self.numbers[0])+","+str(self.numbers[1])+","+str(self.numbers[2])+","+str(self.numbers[3])
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers =[]      
        '''Generate as many wrong answers as possible..here generating 6 wrong answers'''
        for _j in range(6):
            random.shuffle(self.numbers)
            wrongAnswer=str(self.numbers[0])+","+str(self.numbers[1])+","+str(self.numbers[2])+","+str(self.numbers[3])
            self.wrongAnswers.append(wrongAnswer)   
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = "The correct answer is:<br>"+str(self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)

    def GenerateProblemTypeMCQ6(self):
        '''e.g.
        Arrange these numbers in decreasing order:
        855945 301168 752315 419153
        
        301168,752315,419153,855945
        752315,301168,855945,419153
        301168,419153,752315,855945
        855945,419153,752315,301168'''
        self.problem_type = "ProblemTypeMCQ6"
        self.numbers=[]
        i=0
        while i!=4:
            number = randint(100000,999999)
            if (number not in self.numbers):
                self.numbers.append(number)
                i=i+1
        
        self.problem = "Arrange these numbers in decreasing order:<br>%d %d %d %d"%(self.numbers[0],self.numbers[1],
                                                                                    self.numbers[2],self.numbers[3])

        """Sorting the numbers in descending order"""
        self.numbers.sort(reverse=True)
                       
        self.answer = str(self.numbers[0])+","+str(self.numbers[1])+","+str(self.numbers[2])+","+str(self.numbers[3])
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers =[]      
        '''Generate as many wrong answers as possible..here generating 6 wrong answers'''
        for _j in range(6):
            random.shuffle(self.numbers)
            wrongAnswer=str(self.numbers[0])+","+str(self.numbers[1])+","+str(self.numbers[2])+","+str(self.numbers[3])
            self.wrongAnswers.append(wrongAnswer)   
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = "The correct answer is:<br>"+str(self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)
       
    def checkAnswer(self,template,answer,InputAnswer):
        '''removing the "," from answer'''
        answer = str(answer)
        while  answer.partition(",")[1]!="":
            answer = answer.partition(",")[0]+answer.partition(",")[2]
        '''remove the "," from InputAnswer only if its a string'''
        InputAnswer = str(InputAnswer)
        while  InputAnswer.partition(",")[1]!="":
            InputAnswer = InputAnswer.partition(",")[0]+InputAnswer.partition(",")[2]      
        try:
            return int(answer)==int(InputAnswer)
        except ValueError:
            return False        