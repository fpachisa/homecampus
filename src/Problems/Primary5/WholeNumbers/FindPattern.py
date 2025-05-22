'''
Created on Jan 18, 2011

Module: FindPattern
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

class FindPattern:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        if randint(1,2)==1:
            return self.GenerateProblemType1()
        else:
            return self.GenerateProblemTypeMCQ1()
        #return self.GenerateProblemType1()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:"ProblemType1",2:"ProblemTypeMCQ1"}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemTypeMCQ1()}
        
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
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g.:
        Complete the number pattern:
        641103,642103,______,644103,645103'''

        self.numbers=[]
        self.number = randint(100000,888888)
        '''Adding the first number to the numbers list'''       
        self.numbers.append(str(self.number))
        
        self.pattern = random.choice([100,500,1000,5000,10000])
        
        '''50% of the time the pattern will be added and 50% of the time it will be subtracted'''
        if(randint(1,2)==1):
            for _i in range(4):
                self.number = self.number + self.pattern
                self.numbers.append(str(self.number))
            self.flag = "add"
        else:
            for _i in range(4):
                self.number = self.number - self.pattern
                self.numbers.append(str(self.number))
            self.flag = "sub"
                 
        missingNumber = randint(0,len(self.numbers)-1)
       
        self.answer = self.numbers[missingNumber]
        self.numbers[missingNumber] = "______"
        
        self.problem = "Complete the number pattern:<br>%s,%s,%s,%s,%s"%(self.numbers[0],self.numbers[1],
                                                                    self.numbers[2],self.numbers[3],self.numbers[4])
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.numbers,missingNumber,self.flag,self.pattern)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1"}

    def ExplainType1(self,problem,answer,numbers,missingNumber,flag,pattern):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        if missingNumber == 0:
            self.solution_text = self.solution_text + "Since the first number is blank, lets compare numbers 2 and 3<br>"
            if flag == "add":
                self.solution_text = self.solution_text + "Number 3 is greater than number 2. The difference between the two numbers is ("+numbers[2]+" - "+numbers[1]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 3 by adding "+str(pattern)+" to "+numbers[1]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 3 and number 4. Difference between these two numbers is ("+numbers[3]+" - "+numbers[2]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by adding "+str(pattern)+" to the previous number."
                self.solution_text = self.solution_text + "So the pattern is to add "+str(pattern)+" to the previous number which means the number 2 ("+str(numbers[1])+ " ) in the series came by adding "+str(pattern)+" to the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to subtract "+str(pattern)+" from "+str(numbers[1])+"<br>"
                self.solution_text = self.solution_text + str(numbers[1])+" - "+str(pattern)+" = "+str(answer)
            elif flag == "sub":
                self.solution_text = self.solution_text + "Number 3 is less than number 2. The difference between the two numbers is ("+numbers[1]+" - "+numbers[2]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 3 by subtracting "+str(pattern)+" from "+numbers[1]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 3 and number 4. Difference between these two numbers is ("+numbers[2]+" - "+numbers[3]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by subtracting "+str(pattern)+" from the previous number."
                self.solution_text = self.solution_text + "So the pattern is to subtract "+str(pattern)+" from the previous number which means the number 2 ("+str(numbers[1])+ " ) in the series came by subtracting "+str(pattern)+" from the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to add "+str(pattern)+" to "+str(numbers[1])+"<br>"
                self.solution_text = self.solution_text + str(numbers[1])+" + "+str(pattern)+" = "+str(answer)
        elif missingNumber == 1:
            self.solution_text = self.solution_text + "Since the second number is blank, lets compare numbers 3 and 4<br>"
            if flag == "add":
                self.solution_text = self.solution_text + "Number 4 is greater than number 3. The difference between the two numbers is ("+numbers[3]+" - "+numbers[2]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 4 by adding "+str(pattern)+" to "+numbers[2]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 4 and number 5. Difference between these two numbers is ("+numbers[4]+" - "+numbers[3]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by adding "+str(pattern)+" to the previous number."
                self.solution_text = self.solution_text + "So the pattern is to add "+str(pattern)+" to the previous number which means the number 3 ("+str(numbers[2])+ " ) in the series came by adding "+str(pattern)+" to the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to add "+str(pattern)+" to "+str(numbers[0])+"<br>"
                self.solution_text = self.solution_text + str(numbers[0])+" + "+str(pattern)+" = "+str(answer)
            elif flag == "sub":
                self.solution_text = self.solution_text + "Number 4 is less than number 3. The difference between the two numbers is ("+numbers[2]+" - "+numbers[3]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 4 by subtracting "+str(pattern)+" from "+numbers[2]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 4 and number 5. Difference between these two numbers is ("+numbers[3]+" - "+numbers[4]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by subtracting "+str(pattern)+" from the previous number."
                self.solution_text = self.solution_text + "So the pattern is to subtract "+str(pattern)+ " from the previous number which means the number 3 ("+str(numbers[2])+ " ) in the series came by subtracting "+str(pattern)+" from the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to subtract "+str(pattern)+" from "+str(numbers[0])+"<br>"
                self.solution_text = self.solution_text + str(numbers[0])+" - "+str(pattern)+" = "+str(answer)
        elif missingNumber == 2:
            self.solution_text = self.solution_text + "First compare numbers 1 and 2<br>"
            if flag == "add":
                self.solution_text = self.solution_text + "Number 2 is greater than number 1. The difference between the two numbers is ("+numbers[1]+" - "+numbers[0]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 2 by adding "+str(pattern)+" to "+numbers[0]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 4 and number 5. Difference between these two numbers is ("+numbers[4]+" - "+numbers[3]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by adding "+str(pattern)+" to the previous number."
                self.solution_text = self.solution_text + "So the pattern is to add "+str(pattern)+" to the previous number which means the number 4 ("+str(numbers[3])+ " ) in the series came by adding "+str(pattern)+" to the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to add "+str(pattern)+" to "+str(numbers[1])+"<br>"
                self.solution_text = self.solution_text + str(numbers[1])+" + "+str(pattern)+" = "+str(answer)
            elif flag == "sub":
                self.solution_text = self.solution_text + "Number 1 is greater than number 2. The difference between the two numbers is ("+numbers[0]+" - "+numbers[1]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 2 by subtracting "+str(pattern)+" from "+numbers[0]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 4 and number 5. Difference between these two numbers is ("+numbers[3]+" - "+numbers[4]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by subtracting "+str(pattern)+" from the previous number."
                self.solution_text = self.solution_text + "So the pattern is to subtract "+str(pattern)+" from the previous number which means the number 4 ("+str(numbers[3])+ " ) in the series came by subtracting "+str(pattern)+" from the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to subtract "+str(pattern)+" from "+str(numbers[1])+"<br>"
                self.solution_text = self.solution_text + str(numbers[1])+" - "+str(pattern)+" = "+str(answer)
        elif missingNumber == 3:
            self.solution_text = self.solution_text + "First compare numbers 1 and 2<br>"
            if flag == "add":
                self.solution_text = self.solution_text + "Number 2 is greater than number 1. The difference between the two numbers is ("+numbers[1]+" - "+numbers[0]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 2 by adding "+str(pattern)+" to "+numbers[0]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 2 and number 3. Difference between these two numbers is ("+numbers[2]+" - "+numbers[1]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by adding "+str(pattern)+" to the previous number."
                self.solution_text = self.solution_text + "So the pattern is to add "+str(pattern)+" to the previous number which means the number 5 ("+str(numbers[4])+ " ) in the series came by adding "+str(pattern)+" to the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to add "+str(pattern)+" to "+str(numbers[2])+"<br>"
                self.solution_text = self.solution_text + str(numbers[2])+" + "+str(pattern)+" = "+str(answer)
            elif flag == "sub":
                self.solution_text = self.solution_text + "Number 1 is greater than number 2. The difference between the two numbers is ("+numbers[0]+" - "+numbers[1]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 2 by subtracting "+str(pattern)+" from "+numbers[0]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 2 and number 3. Difference between these two numbers is ("+numbers[1]+" - "+numbers[2]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by subtracting "+str(pattern)+" from the previous number."
                self.solution_text = self.solution_text + "So the pattern is to subtract "+str(pattern)+" from the previous number which means the number 5 ("+str(numbers[4])+ " ) in the series came by subtracting "+str(pattern)+" from the missing number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to subtract "+str(pattern)+" from "+str(numbers[2])+"<br>"
                self.solution_text = self.solution_text + str(numbers[2])+" - "+str(pattern)+" = "+str(answer)
        elif missingNumber == 4:
            self.solution_text = self.solution_text + "First compare numbers 1 and 2<br>"
            if flag == "add":
                self.solution_text = self.solution_text + "Number 2 is greater than number 1. The difference between the two numbers is ("+numbers[1]+" - "+numbers[0]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 2 by adding "+str(pattern)+" to "+numbers[0]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 2 and number 3. Difference between these two numbers is ("+numbers[2]+" - "+numbers[1]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by adding "+str(pattern)+" to the previous number.<br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to add "+str(pattern)+" to "+str(numbers[3])+"<br><br>"
                self.solution_text = self.solution_text + str(numbers[3])+" + "+str(pattern)+" = "+str(answer)
            elif flag == "sub":
                self.solution_text = self.solution_text + "Number 1 is greater than number 2. The difference between the two numbers is ("+numbers[0]+" - "+numbers[1]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This means you can get number 2 by subtracting "+str(pattern)+" from "+numbers[0]+"<br><br>"
                self.solution_text = self.solution_text + "Let's check the same with number 2 and number 3. Difference between these two numbers is ("+numbers[1]+" - "+numbers[2]+") "+str(pattern)+"<br><br>"
                self.solution_text = self.solution_text + "This confirms that we can get the next number in this series by subtracting "+str(pattern)+" from the previous number.<br><br>"
                self.solution_text = self.solution_text + "Hence to get the missing number we have to subtract "+str(pattern)+" from "+str(numbers[3])+"<br>"
                self.solution_text = self.solution_text + str(numbers[3])+" - "+str(pattern)+" = "+str(answer)       
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the missing number in the pattern is "+answer+"</b></i>"
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
        Complete the number pattern:
        641103,642103,______,644103,645103
        
        643103
        653103
        648103
        644103'''
        self.problem_type = "ProblemTypeMCQ1"
        self.numbers=[]
        self.number = randint(100000,888888)
        '''Adding the first number to the numbers list'''       
        self.numbers.append(str(self.number))
        
        self.pattern = random.choice([100,500,1000,5000,10000])
        
        '''50% of the time the pattern will be added and 50% of the time it will be subtracted'''      
        if(randint(1,2)==1):
            for _i in range(4):
                self.number = self.number + self.pattern
                self.numbers.append(str(self.number))
            self.flag = "add"
        else:
            for _i in range(4):
                self.number = self.number - self.pattern
                self.numbers.append(str(self.number))
            self.flag = "sub"        
            
        missingNumber = randint(0,len(self.numbers)-1)
        
        self.answer = self.numbers[missingNumber]
        self.numbers[missingNumber] = "______"
        
        self.problem = "Complete the number pattern:<br>%s,%s,%s,%s,%s"%(self.numbers[0],self.numbers[1],
                                                                    self.numbers[2],self.numbers[3],self.numbers[4])

        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = []    
        self.wrongAnswers.append(str(int(self.answer)+self.pattern))
        self.wrongAnswers.append(str(int(self.answer)-self.pattern))
        self.wrongAnswers.append(str(int(self.answer)+2*self.pattern))
        self.wrongAnswers.append(str(int(self.answer)-2*self.pattern))
        self.wrongAnswers.append(str(int(self.answer)+10*self.pattern))
        self.wrongAnswers.append(str(int(self.answer)-10*self.pattern))
        self.wrongAnswers.append(str(int(self.answer)+5*self.pattern))
        self.wrongAnswers.append(str(int(self.answer)-5*self.pattern))
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.numbers,missingNumber,self.flag,self.pattern)
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