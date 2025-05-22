'''
Created on Jan 18, 2011

Module: ApproximationEstimation
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

class ApproximationEstimation:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        random = randint(1,3)
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
        else:
            if randint(1,2)==1:
                return self.GenerateProblemType3()
            else:
                return self.GenerateProblemTypeMCQ3()
        #return self.GenerateProblemTypeMCQ3()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:"ProblemType1",2:"ProblemTypeMCQ2",3:"ProblemType3",4:"ProblemTypeMCQ1",5:"ProblemType2",
                            6:"ProblemTypeMCQ3"}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemTypeMCQ2(),3:self.GenerateProblemType3(),
                                    4:self.GenerateProblemTypeMCQ1(),5:self.GenerateProblemType2(),6:self.GenerateProblemTypeMCQ3(),
                                    }
        
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
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        
        '''randomly generate 6 digit number which doesn't contain zeroes so that we can round it off'''
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 6)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        
        '''creating a dictionary so that use key to ask to round off any place and use the value to 
        round it off
        For e.g.: round off to hundreds place and then use formula round(number,-2)'''   
        self.placeDict = {"tens":-1,"hundreds":-2,"thousands":-3,"ten thousands":-4}
        self.placeDict1 = {"tens":"ones","hundreds":"tens","thousands":"hundreds","ten thousands":"thousands"}
        self.placeDict2 = {"tens":5,"hundreds":4,"thousands":3,"ten thousands":2}
        
        self.roundOff = self.placeDict.keys()[randint(0,len(self.placeDict)-1)]
        self.roundOff1 = self.placeDict1[self.roundOff]
        self.roundOff2 = self.placeDict2[self.roundOff]
        self.problem = "Round off %s to the nearest %s:"%(self.number,self.roundOff)
        
        '''using int here to remove the .0 from the end of the number'''
        self.answer = int(round(int(self.number),self.placeDict[self.roundOff]))
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.number,self.roundOff,self.roundOff1,self.roundOff2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1"}

    def ExplainType1(self,problem,answer,number,roundOff,roundOff1,roundOff2):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Since we are rounding off to nearest "+roundOff+", lets check the number at "+roundOff1+" place.<br><br>"
        self.solution_text = self.solution_text + "If the number at "+roundOff1+" place is less than 5 then we put zeroes for all the digit after "+roundOff+" place.<br><br>"
        self.solution_text = self.solution_text + "And if the number at "+roundOff1+" place is equal to or greater than 5 then we put zeroes for all the digit after "+roundOff+" place and add one to the digit at "+roundOff+" place.<br><br>"
        if(int(number[roundOff2])<5):
            self.solution_text = self.solution_text + "Since the number at "+roundOff+" place is "+number[roundOff2]+" which is less than 5"
        else:
            self.solution_text = self.solution_text + "Since the number at "+roundOff+" place is "+number[roundOff2]+" which is equal to or greater than 5"
        self.solution_text = self.solution_text + "<br><br><i><b>The rounded off number would be "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain 
    
    def GenerateProblemType2(self):
        '''e.g.:
            A number rounded off to nearest thousand is 492000. What could be the greatest possible original number?'''
        
        '''randomly generate any 6 digits number'''
        self.number = randint(100000,999999)
        
        random = randint(1,4)
        if (random==1):
            self.number = int(round(self.number,-3))
            self.problem = "A number rounded off to nearest thousand is %d. What could be the greatest possible original number?"%(self.number)   
            self.answer = self.number + 499
            self.flag = 1
        elif (random==2):
            self.number = int(round(self.number,-3))
            self.problem = "A number rounded off to nearest thousand is %d. What could be the smallest possible original number?"%(self.number)   
            self.answer = self.number - 500
            self.flag = 2            
        elif (random==3):
            self.number = int(round(self.number,-2))
            self.problem = "A number rounded off to nearest hundred is %d. What could be the greatest possible original number?"%(self.number)   
            self.answer = self.number + 49
            self.flag = 3
        elif (random==4):
            self.number = int(round(self.number,-2))
            self.problem = "A number rounded off to nearest hundred is %d. What could be the smallest possible original number?"%(self.number)   
            self.answer = self.number - 50
            self.flag = 4
                    
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,str(self.answer),self.number,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2"}

    def ExplainType2(self,problem,answer,number,flag):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        if flag == 1:
            self.solution_text = self.solution_text + "Since we need to find the greatest possible original number that means the original number has been rounded down. In other words original number should be greater than the rounded off number.<br><br>"
            self.solution_text = self.solution_text + "To round down a number to nearest thousand digit, the digit at hundreds place should be less than 5.<br><br>"
            self.solution_text = self.solution_text + "So the maximum digit which is less than 5 is 4. Hence the digit at hundreds place should be 4.<br><br>"
            self.solution_text = self.solution_text + "Now digits at tens and ones place could be greatest possible single digit number which is 9.<br><br>"
            self.solution_text = self.solution_text + "Hence to get the greatest possible original number which was rounded off to "+str(number)+" ,we add 499 to it.<br><br>"
            self.solution_text = self.solution_text + str(number)+" + 499 = "+answer
        if flag == 2:
            self.solution_text = self.solution_text + "Since we need to find the smallest possible original number that means the original number has been rounded up. In other words original number should be less than the rounded off number.<br><br>"
            self.solution_text = self.solution_text + "To round up a number to nearest thousand digit, the digit at hundreds place should be greater than or equal to 5.<br><br>"
            self.solution_text = self.solution_text + "So the minimum digit at hundreds place will be 5.<br><br>"
            self.solution_text = self.solution_text + "Now digits at tens and ones place could be smallest possible single digit number which is 0.<br><br>"
            self.solution_text = self.solution_text + "Hence to get the smallest possible original number which was rounded off to "+str(number)+" ,we subtract 500 from it.<br><br>"
            self.solution_text = self.solution_text + str(number)+" - 500 = "+answer
        if flag == 3:
            self.solution_text = self.solution_text + "Since we need to find the greatest possible original number that means the original number has been rounded down. In other words original number should be greater than the rounded off number.<br><br>"
            self.solution_text = self.solution_text + "To round down a number to nearest hundred digit, the digit at tens place should be less than 5.<br><br>"
            self.solution_text = self.solution_text + "So the maximum digit which is less than 5 is 4. Hence the digit at tens place should be 4.<br><br>"
            self.solution_text = self.solution_text + "Now digit at ones place could be greatest possible single digit number which is 9.<br><br>"
            self.solution_text = self.solution_text + "Hence to get the greatest possible original number which was rounded off to "+str(number)+" ,we add 49 to it.<br><br>"
            self.solution_text = self.solution_text + str(number)+" + 49 = "+answer
        if flag == 4:
            self.solution_text = self.solution_text + "Since we need to find the smallest possible original number that means the original number has been rounded up. In other words original number should be less than the rounded off number.<br><br>"
            self.solution_text = self.solution_text + "To round up a number to nearest hundred digit, the digit at tens place should be greater than or equal to 5.<br><br>"
            self.solution_text = self.solution_text + "So the minimum digit at tens place will be 5.<br><br>"
            self.solution_text = self.solution_text + "Now digits at ones place could be smallest possible single digit number which is 0.<br><br>"
            self.solution_text = self.solution_text + "Hence to get the smallest possible original number which was rounded off to "+str(number)+" ,we subtract 50 from it.<br><br>"
            self.solution_text = self.solution_text + str(number)+" - 50 = "+answer
        self.solution_text = self.solution_text + "<br><br><i><b>The rounded off number would be "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain 
    
    def GenerateProblemType3(self):
        '''e.g.:
        Estimate the value of 1956 x 8
        (round off to the nearest thousand and then multiply)'''
                   
        '''Generating the numbers so that when rounding off to nearest thousand the number will
        be between 2000 and 9000'''
        self.number = randint(1501,9499)
        self.multiplier = randint(3,9)
        self.problem="Estimate the value of %d x %d <br>(round off to the nearest thousand and then multiply)"%(self.number,self.multiplier)
        self.answer=int(round(self.number,-3))*self.multiplier
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.number,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3"}

    def ExplainType3(self,problem,answer,number,multiplier):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "First round off the given number to the nearest thousand. In order to do that lets check the number at hundreds place.<br><br>"
        self.solution_text = self.solution_text + "If the number at hundreds place is less than 5 then we put zeroes for all the digit after thousands place.<br><br>"
        self.solution_text = self.solution_text + "And if the number at hundreds place is equal to or greater than 5 then we put zeroes for all the digit after thousands place and add one to the digit at thousands place.<br><br>"
        if(int(str(number)[3])<5):
            self.solution_text = self.solution_text + "Since the number at hundreds place is "+str(number)[3]+" which is less than 5"
        else:
            self.solution_text = self.solution_text + "Since the number at hundreds place is "+str(number)[3]+" which is equal to or greater than 5"
        self.solution_text = self.solution_text + "<br><br>The rounded off number would be "+str(int(round(self.number,-3)))
        self.solution_text = self.solution_text + "<br><br>Hence to get the estimated value of "+str(number)+" x "+str(multiplier)+" multiply "+str(int(round(self.number,-3)))+" by "+str(multiplier)
        self.solution_text = self.solution_text + "<br><br><i><b>The estimated value is "+answer+"</b></i>"
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
                ,'value3':self.value3,'value4':self.value4,'explain':explain
                ,'problem_type':problem_type}       

    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        Round off 824956 to the nearest tens:
        824960
        823960
        825000
        824950'''
       
        '''randomly generate 6 digit number which doesn't contain zeroes so that we can round it off'''
        self.problem_type = "ProblemTypeMCQ1"
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 6)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.number = int(self.number)
        
        '''creating a dictionay so that use key to ask to round off any place and use the value to 
        round it off
        For e.g.: round off to hundreds place and then use formula round(number,-2)'''   

        self.placeDict = {"tens":-1,"hundreds":-2,"thousands":-3,"ten thousands":-4}
        self.placeDict1 = {"tens":"ones","hundreds":"tens","thousands":"hundreds","ten thousands":"thousands"}
        self.placeDict2 = {"tens":5,"hundreds":4,"thousands":3,"ten thousands":2}
        
        self.roundOff = self.placeDict.keys()[randint(0,len(self.placeDict)-1)]
        self.roundOff1 = self.placeDict1[self.roundOff]
        self.roundOff2 = self.placeDict2[self.roundOff]
        
        self.problem = "Round off %d to the nearest %s:"%(self.number,self.roundOff)
        
        self.answer = int(round(self.number,self.placeDict[self.roundOff]))

        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = []    
        self.wrongAnswers.append(str(self.answer+100))
        self.wrongAnswers.append(str(self.answer-100))
        self.wrongAnswers.append(str(self.answer+1000))
        self.wrongAnswers.append(str(self.answer-1000))
        self.wrongAnswers.append(str(self.answer+10))
        self.wrongAnswers.append(str(self.answer-10))
        self.wrongAnswers.append(str(self.answer+1000))
        self.wrongAnswers.append(str(self.answer-1000))
        self.wrongAnswers.append(str(self.answer+10))
        self.wrongAnswers.append(str(self.answer-10))
        self.wrongAnswers.append(str(int(round(self.number,-1))))
        self.wrongAnswers.append(str(int(round(self.number,-2))))
        self.wrongAnswers.append(str(int(round(self.number,-3))))
        self.wrongAnswers.append(str(int(round(self.number,-4))))
        
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),str(self.number),self.roundOff,self.roundOff1,self.roundOff2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)

    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
            A number rounded off to nearest thousand is 492000. What could be the greatest possible original number?'''
        
        self.problem_type = "ProblemTypeMCQ2"
        '''randomly generate any 6 digits number'''
        self.number = randint(100000,999999)
        
        random = randint(1,4)
        if (random==1):
            self.flag = 1
            self.number = int(round(self.number,-3))
            self.problem = "A number rounded off to nearest thousand is %d. What could be the greatest possible original number?"%(self.number)   
            self.answer = self.number + 499
        elif (random==2):
            self.flag = 2
            self.number = int(round(self.number,-3))
            self.problem = "A number rounded off to nearest thousand is %d. What could be the smallest possible original number?"%(self.number)   
            self.answer = self.number - 500            
        elif (random==3):
            self.flag = 3
            self.number = int(round(self.number,-2))
            self.problem = "A number rounded off to nearest hundred is %d. What could be the greatest possible original number?"%(self.number)   
            self.answer = self.number + 49
        elif (random==4):
            self.flag = 4
            self.number = int(round(self.number,-2))
            self.problem = "A number rounded off to nearest hundred is %d. What could be the smallest possible original number?"%(self.number)   
            self.answer = self.number - 50

        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = []    
        self.wrongAnswers.append(str(self.number+100))
        self.wrongAnswers.append(str(self.number-100))
        self.wrongAnswers.append(str(self.number+500))
        self.wrongAnswers.append(str(self.number-500))
        self.wrongAnswers.append(str(self.number+499))
        self.wrongAnswers.append(str(self.number-499))
        self.wrongAnswers.append(str(self.number+49))
        self.wrongAnswers.append(str(self.answer-49))
        
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,str(self.answer),self.number,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)
    
    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
        Estimate the value of 1956 x 8
        (round off to the nearest thousand and then multiply)'''
        self.problem_type = "ProblemTypeMCQ3"          
        '''Generating the numbers so that when rounding off to nearest thousand the number will
        be between 2000 and 9000'''
        self.number = randint(1501,9499)
        self.multiplier = randint(3,9)
        self.problem="Estimate the value of %d x %d <br>(round off to the nearest thousand and then multiply)"%(self.number,self.multiplier)
        self.answer=int(round(self.number,-3))*self.multiplier

        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = []    
        self.wrongAnswers.append(str(int(round(self.number,-3)+1000)*self.multiplier))
        self.wrongAnswers.append(str(int(round(self.number,-3)-1000)*self.multiplier))
        self.wrongAnswers.append(str(int(round(self.number,-3)+2000)*self.multiplier))
        self.wrongAnswers.append(str(int(round(self.number,-3))*6))
        self.wrongAnswers.append(str(int(round(self.number,-3))*7))
        self.wrongAnswers.append(str(int(round(self.number,-3))*8))
        self.wrongAnswers.append(str(int(round(self.number,-3))*9))
                
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.number,self.multiplier)
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