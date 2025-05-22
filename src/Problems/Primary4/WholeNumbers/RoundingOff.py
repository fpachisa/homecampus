'''
Created on Jan 15, 2012

Module: RoundingOff
Generates "Rounding off the numbers" problems for Primary 4

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

class RoundingOff:
    
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
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
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
        #return self.GenerateProblemTypeMCQ3()
        
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
        
        '''randomly generate 5 digit number which doesn't contain zeroes so that we can round it off'''
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 5)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        
        '''creating a dictionary so that use key to ask to round off any place and use the value to 
        round it off
        For e.g.: round off to hundreds place and then use formula round(number,-2)'''   
        self.placeDict = {"ten":-1,"hundred":-2,}
        self.placeDict1 = {"ten":"ones","hundred":"tens",}
        self.placeDict2 = {"ten":4,"hundred":3,}
        
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
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType1(self,problem,answer,number,roundOff,roundOff1,roundOff2):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Since we are rounding off to nearest "+roundOff+", lets check the number at "+roundOff1+" place.<br><br>"
        self.solution_text = self.solution_text + "If the number at "+roundOff1+" place is less than 5 then we put zeroes for all the digit after "+roundOff+" place.<br><br>"
        self.solution_text = self.solution_text + "And if the number at "+roundOff1+" place is equal to or greater than 5 then we put zeroes for all the digit after "+roundOff+" place and add one to the digit at "+roundOff+" place.<br><br>"
        if(int(number[roundOff2])<5):
            self.solution_text = self.solution_text + "Since the number at "+roundOff1+" place is "+number[roundOff2]+" which is less than 5"
        else:
            self.solution_text = self.solution_text + "Since the number at "+roundOff1+" place is "+number[roundOff2]+" which is equal to or greater than 5"
        self.solution_text = self.solution_text + "<br><br><i><b>The rounded off number would be "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain 

    def GenerateProblemType2(self):
        
        '''randomly generate 5 digit number which doesn't contain zeroes so that we can round it off'''
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = ''
        self.number2 = ''
        
        for d in random.sample([1,2,3,4,5,6,7,8,9], 3):
            self.number1 = self.number1 + str(d)

        for d in random.sample([1,2,3,4,5,6,7,8,9], 3):
            self.number2 = self.number2 + str(d)

        self.number1 = int(self.number1)
        self.number2 = int(self.number2)
                
        if self.number1 < self.number2:
            self.number3 = self.number1
            self.number1 = self.number2
            self.number2 = self.number3
                            
        if randint(1,2) == 1:
            self.roundOff = "ten"
            self.roundOff1 = "ones"
            self.roundOff2 = 2
            self.RoundOffNumber1 = int(round(self.number1,-1))
            self.RoundOffNumber2 = int(round(self.number2,-1))
            if randint(1,2) == 1:
                self.problem = "Round off each number to the nearest ten then estimate the value of:<br>"
                self.problem = self.problem + str(self.number1)+" + "+str(self.number2)+" &asymp; "       
                self.answer = self.RoundOffNumber1 + self.RoundOffNumber2 
                self.flag = 1
            else:
                self.problem = "Round off each number to the nearest ten then estimate the value of:<br>"
                self.problem = self.problem + str(self.number1)+" - "+str(self.number2)+" &asymp; "
                self.answer = self.RoundOffNumber1 - self.RoundOffNumber2
                self.flag = 2                 
        else:
            self.roundOff = "hundred"
            self.roundOff1 = "tens"
            self.roundOff2 = 1
            self.RoundOffNumber1 = int(round(self.number1,-2))
            self.RoundOffNumber2 = int(round(self.number2,-2))
            if randint(1,2) == 1:
                self.problem = "Round off each number to the nearest hundred then estimate the value of:<br>"
                self.problem = self.problem + str(self.number1)+" + "+str(self.number2)+" &asymp; "      
                self.answer = self.RoundOffNumber1 + self.RoundOffNumber2
                self.flag = 1 
            else:
                self.problem = "Round off each number to the nearest hundred then estimate the value of:<br>"
                self.problem = self.problem + str(self.number1)+" - "+str(self.number2)+" &asymp; "
                self.answer = self.RoundOffNumber1 - self.RoundOffNumber2
                self.flag = 2
                            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,str(self.answer),str(self.number1),str(self.number2),str(self.RoundOffNumber1),str(self.RoundOffNumber2),self.roundOff,self.roundOff1,self.roundOff2,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType2(self,problem,answer,number1,number2,RoundOffNumber1,RoundOffNumber2,roundOff,roundOff1,roundOff2,flag):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Since we are rounding off to nearest "+roundOff+", lets check the number at "+roundOff1+" place.<br><br>"
        self.solution_text = self.solution_text + "If the number at "+roundOff1+" place is less than 5 then we put zeroes for all the digit after "+roundOff+" place.<br><br>"
        self.solution_text = self.solution_text + "And if the number at "+roundOff1+" place is equal to or greater than 5 then we put zeroes for all the digit after "+roundOff+" place and add one to the digit at "+roundOff+" place.<br><br>"
        if(int(number1[roundOff2])<5):
            self.solution_text = self.solution_text + "Since the number at "+roundOff1+" place is "+number1[roundOff2]+" which is less than 5<br>"
            self.solution_text = self.solution_text + "The first number rounded off is "+RoundOffNumber1+"<br><br>"
        else:
            self.solution_text = self.solution_text + "Since the number at "+roundOff1+" place is "+number1[roundOff2]+" which is equal to or greater than 5<br>"
            self.solution_text = self.solution_text + "The first number rounded off is "+RoundOffNumber1+"<br><br>"
        if(int(number2[roundOff2])<5):
            self.solution_text = self.solution_text + "Since the number at "+roundOff1+" place is "+number2[roundOff2]+" which is less than 5<br>"
            self.solution_text = self.solution_text + "The second number rounded off is "+RoundOffNumber2+"<br><br>"
        else:
            self.solution_text = self.solution_text + "Since the number at "+roundOff1+" place is "+number2[roundOff2]+" which is equal to or greater than 5<br>"
            self.solution_text = self.solution_text + "The second number rounded off is "+RoundOffNumber2+"<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "Therefore, "+RoundOffNumber1+" + "+RoundOffNumber2+" = "+answer+"<br><br>"
            self.solution_text = self.solution_text + "<br><br><i><b>"+number1+" + "+number2+" &asymp; "+answer+"</b></i>"
        else:
            self.solution_text = self.solution_text + "Therefore, "+RoundOffNumber1+" - "+RoundOffNumber2+" = "+answer
            self.solution_text = self.solution_text + "<br><br><i><b>"+number1+" - "+number2+" &asymp; "+answer+"</b></i>"            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain 

    def GenerateProblemType3(self):
        
        '''randomly generate 5 digit number which doesn't contain zeroes so that we can round it off'''
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = ''
        self.number2 = ''
        self.number3 = ''
        
        for d in random.sample([4,5,6,7,8,9], 4):
            self.number1 = self.number1 + str(d)

        for d in random.sample([1,2,3,4,5,6], 3):
            self.number2 = self.number2 + str(d)

        for d in random.sample([1,2,3,4,5,6], 3):
            self.number3 = self.number3 + str(d)
            
        self.number1 = int(self.number1)
        self.number2 = int(self.number2)
        self.number3 = int(self.number3)
        self.numbers = [self.number1,self.number2,self.number3]
        self.roundOff = "hundred"
        self.roundOff1 = "tens"
        self.roundOff2 = 1
        self.RoundOffNumber1 = int(round(self.number1,-2))
        self.RoundOffNumber2 = int(round(self.number2,-2))
        self.RoundOffNumber3 = int(round(self.number3,-2))
        self.ProblemSelector = randint(1,4)
        
        self.problem = "Round off each number to the nearest hundred then estimate the value of:<br>"
        if self.ProblemSelector == 1:
            self.problem = self.problem + str(self.numbers[0])+" + "+str(self.numbers[1])+" + "+str(self.numbers[2])+" &asymp; "      
            self.answer = self.RoundOffNumber1 + self.RoundOffNumber2 + self.RoundOffNumber3
            self.flag = 1 
        elif self.ProblemSelector == 2:
            self.problem = self.problem + str(self.number1)+" - "+str(self.number2)+" - "+str(self.number3)+" &asymp; "
            self.answer = self.RoundOffNumber1 - self.RoundOffNumber2 - self.RoundOffNumber3
            self.flag = 2
        elif self.ProblemSelector == 3:
            self.problem = self.problem + str(self.number1)+" + "+str(self.number2)+" - "+str(self.number3)+" &asymp; "
            self.answer = self.RoundOffNumber1 + self.RoundOffNumber2 - self.RoundOffNumber3
            self.flag = 3
        elif self.ProblemSelector == 4:
            self.problem = self.problem + str(self.number1)+" - "+str(self.number2)+" + "+str(self.number3)+" &asymp; "
            self.answer = self.RoundOffNumber1 - self.RoundOffNumber2 + self.RoundOffNumber3
            self.flag = 4            
                                        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.numbers,self.roundOff,self.roundOff1,self.roundOff2,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType3(self,problem,answer,numbers,roundOff,roundOff1,roundOff2,flag):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Since we are rounding off to nearest "+roundOff+", lets check the number at "+roundOff1+" place.<br><br>"
        self.solution_text = self.solution_text + "If the number at "+roundOff1+" place is less than 5 then we put zeroes for all the digit after "+roundOff+" place.<br><br>"
        self.solution_text = self.solution_text + "And if the number at "+roundOff1+" place is equal to or greater than 5 then we put zeroes for all the digit after "+roundOff+" place and add one to the digit at "+roundOff+" place.<br><br>"
        if(int(str(numbers[0])[roundOff2+1])<5):
            self.solution_text = self.solution_text + "Since the number at "+roundOff1+" place is "+str(numbers[0])[roundOff2+1]+" which is less than 5<br>"
            self.solution_text = self.solution_text + "The first number rounded off is "+str(int(round(numbers[0],-2)))+"<br><br>"
        else:
            self.solution_text = self.solution_text + "Since the number at "+roundOff1+" place is "+str(numbers[0])[roundOff2+1]+" which is equal to or greater than 5<br>"
            self.solution_text = self.solution_text + "The first number rounded off is "+str(int(round(numbers[0],-2)))+"<br><br>"
        if(int(str(numbers[1])[roundOff2])<5):
            self.solution_text = self.solution_text + "Since the number at "+roundOff1+" place is "+str(numbers[1])[roundOff2]+" which is less than 5<br>"
            self.solution_text = self.solution_text + "The second number rounded off is "+str(int(round(numbers[1],-2)))+"<br><br>"
        else:
            self.solution_text = self.solution_text + "Since the number at "+roundOff1+" place is "+str(numbers[1])[roundOff2]+" which is equal to or greater than 5<br>"
            self.solution_text = self.solution_text + "The second number rounded off is "+str(int(round(numbers[1],-2)))+"<br><br>"
        if(int(str(numbers[2])[roundOff2])<5):
            self.solution_text = self.solution_text + "Since the number at "+roundOff1+" place is "+str(numbers[2])[roundOff2]+" which is less than 5<br>"
            self.solution_text = self.solution_text + "The third number rounded off is "+str(int(round(numbers[2],-2)))+"<br><br>"
        else:
            self.solution_text = self.solution_text + "Since the number at "+roundOff1+" place is "+str(numbers[2])[roundOff2]+" which is equal to or greater than 5<br>"
            self.solution_text = self.solution_text + "The third number rounded off is "+str(int(round(numbers[2],-2)))+"<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "Therefore, "+str(int(round(numbers[0],-2)))+" + "+str(int(round(numbers[1],-2)))+" + "+str(int(round(numbers[2],-2)))+" = "+answer+"<br><br>"
            self.solution_text = self.solution_text + "<br><br><i><b>"+str(numbers[0])+" + "+str(numbers[1])+" + "+str(numbers[2])+" &asymp; "+answer+"</b></i>"
        elif flag == 2:
            self.solution_text = self.solution_text + "Therefore, "+str(int(round(numbers[0],-2)))+" - "+str(int(round(numbers[1],-2)))+" - "+str(int(round(numbers[2],-2)))+" = "+answer+"<br><br>"
            self.solution_text = self.solution_text + "<br><br><i><b>"+str(numbers[0])+" - "+str(numbers[1])+" - "+str(numbers[2])+" &asymp; "+answer+"</b></i>"            
        elif flag == 3:
            self.solution_text = self.solution_text + "Therefore, "+str(int(round(numbers[0],-2)))+" + "+str(int(round(numbers[1],-2)))+" - "+str(int(round(numbers[2],-2)))+" = "+answer+"<br><br>"
            self.solution_text = self.solution_text + "<br><br><i><b>"+str(numbers[0])+" + "+str(numbers[1])+" - "+str(numbers[2])+" &asymp; "+answer+"</b></i>"
        elif flag == 4:
            self.solution_text = self.solution_text + "Therefore, "+str(int(round(numbers[0],-2)))+" - "+str(int(round(numbers[1],-2)))+" + "+str(int(round(numbers[2],-2)))+" = "+answer+"<br><br>"
            self.solution_text = self.solution_text + "<br><br><i><b>"+str(numbers[0])+" - "+str(numbers[1])+" + "+str(numbers[2])+" &asymp; "+answer+"</b></i>"            
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
                ,'problem_type':problem_type,'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}       

    def GenerateProblemTypeMCQ1(self):
        
        '''randomly generate 5 digit number which doesn't contain zeroes so that we can round it off'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 4
        self.problem_type = "ProblemTypeMCQ1"
        self.CheckAnswerType = 1
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 5)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        
        '''creating a dictionary so that use key to ask to round off any place and use the value to 
        round it off
        For e.g.: round off to hundreds place and then use formula round(number,-2)'''   
        self.placeDict = {"ten":-1,"hundred":-2,}
        self.placeDict1 = {"ten":"ones","hundred":"tens",}
        self.placeDict2 = {"ten":4,"hundred":3,}
        
        self.roundOff = self.placeDict.keys()[randint(0,len(self.placeDict)-1)]
        self.roundOff1 = self.placeDict1[self.roundOff]
        self.roundOff2 = self.placeDict2[self.roundOff]
        self.problem = "Round off %s to the nearest %s:"%(self.number,self.roundOff)
        
        '''using int here to remove the .0 from the end of the number'''
        self.answer = int(round(int(self.number),self.placeDict[self.roundOff]))
        
        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = []    
        self.wrongAnswers.append(str(self.answer+100))
        self.wrongAnswers.append(str(self.answer-100))
        self.wrongAnswers.append(str(self.answer+1000))
        self.wrongAnswers.append(str(self.answer-1000))
        self.wrongAnswers.append(str(self.answer+10))
        self.wrongAnswers.append(str(self.answer-10))
        self.wrongAnswers.append(str(int(round(int(self.number),-1))))
        self.wrongAnswers.append(str(int(round(int(self.number),-2))))
        self.wrongAnswers.append(str(int(round(int(self.number),-3))))
        
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.number,self.roundOff,self.roundOff1,self.roundOff2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ2(self):
        
        '''randomly generate 5 digit number which doesn't contain zeroes so that we can round it off'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.grade = 4
        self.problem_type = "ProblemTypeMCQ2"
        self.CheckAnswerType = 1
        
        self.number1 = ''
        self.number2 = ''
        
        for d in random.sample([1,2,3,4,5,6,7,8,9], 3):
            self.number1 = self.number1 + str(d)

        for d in random.sample([1,2,3,4,5,6,7,8,9], 3):
            self.number2 = self.number2 + str(d)

        self.number1 = int(self.number1)
        self.number2 = int(self.number2)
                
        if self.number1 < self.number2:
            self.number3 = self.number1
            self.number1 = self.number2
            self.number2 = self.number3
                            
        if randint(1,2) == 1:
            self.roundOff = "ten"
            self.roundOff1 = "ones"
            self.roundOff2 = 2
            self.RoundOffNumber1 = int(round(self.number1,-1))
            self.RoundOffNumber2 = int(round(self.number2,-1))
            if randint(1,2) == 1:
                self.problem = "Round off each number to the nearest ten then estimate the value of:<br>"
                self.problem = self.problem + str(self.number1)+" + "+str(self.number2)+" &asymp; "       
                self.answer = self.RoundOffNumber1 + self.RoundOffNumber2 
                self.flag = 1
            else:
                self.problem = "Round off each number to the nearest ten then estimate the value of:<br>"
                self.problem = self.problem + str(self.number1)+" - "+str(self.number2)+" &asymp; "
                self.answer = self.RoundOffNumber1 - self.RoundOffNumber2
                self.flag = 2                 
        else:
            self.roundOff = "hundred"
            self.roundOff1 = "tens"
            self.roundOff2 = 1
            self.RoundOffNumber1 = int(round(self.number1,-2))
            self.RoundOffNumber2 = int(round(self.number2,-2))
            if randint(1,2) == 1:
                self.problem = "Round off each number to the nearest hundred then estimate the value of:<br>"
                self.problem = self.problem + str(self.number1)+" + "+str(self.number2)+" &asymp; "      
                self.answer = self.RoundOffNumber1 + self.RoundOffNumber2
                self.flag = 1 
            else:
                self.problem = "Round off each number to the nearest hundred then estimate the value of:<br>"
                self.problem = self.problem + str(self.number1)+" - "+str(self.number2)+" &asymp; "
                self.answer = self.RoundOffNumber1 - self.RoundOffNumber2
                self.flag = 2
        
        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = []    
        self.wrongAnswers.append(str(self.answer+100))
        if self.answer > 100:
            self.wrongAnswers.append(str(self.answer-100))
        self.wrongAnswers.append(str(self.answer+1000))
        self.wrongAnswers.append(str(self.answer+10))
        if self.answer > 10:
            self.wrongAnswers.append(str(self.answer-10))
        
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,str(self.answer),str(self.number1),str(self.number2),str(self.RoundOffNumber1),str(self.RoundOffNumber2),self.roundOff,self.roundOff1,self.roundOff2,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ3(self):
        
        '''randomly generate 5 digit number which doesn't contain zeroes so that we can round it off'''
        self.complexity_level = "medium"
        self.HCScore = 5
        self.grade = 4
        self.problem_type = "ProblemTypeMCQ3"
        self.CheckAnswerType = 1
        
        self.number1 = ''
        self.number2 = ''
        self.number3 = ''
        
        for d in random.sample([4,5,6,7,8,9], 4):
            self.number1 = self.number1 + str(d)

        for d in random.sample([1,2,3,4,5,6], 3):
            self.number2 = self.number2 + str(d)

        for d in random.sample([1,2,3,4,5,6], 3):
            self.number3 = self.number3 + str(d)
            
        self.number1 = int(self.number1)
        self.number2 = int(self.number2)
        self.number3 = int(self.number3)
        self.numbers = [self.number1,self.number2,self.number3]
        self.roundOff = "hundred"
        self.roundOff1 = "tens"
        self.roundOff2 = 1
        self.RoundOffNumber1 = int(round(self.number1,-2))
        self.RoundOffNumber2 = int(round(self.number2,-2))
        self.RoundOffNumber3 = int(round(self.number3,-2))
        self.ProblemSelector = randint(1,4)
        
        self.problem = "Round off each number to the nearest hundred then estimate the value of:<br>"
        if self.ProblemSelector == 1:
            self.problem = self.problem + str(self.numbers[0])+" + "+str(self.numbers[1])+" + "+str(self.numbers[2])+" &asymp; "      
            self.answer = self.RoundOffNumber1 + self.RoundOffNumber2 + self.RoundOffNumber3
            self.flag = 1 
        elif self.ProblemSelector == 2:
            self.problem = self.problem + str(self.number1)+" - "+str(self.number2)+" - "+str(self.number3)+" &asymp; "
            self.answer = self.RoundOffNumber1 - self.RoundOffNumber2 - self.RoundOffNumber3
            self.flag = 2
        elif self.ProblemSelector == 3:
            self.problem = self.problem + str(self.number1)+" + "+str(self.number2)+" - "+str(self.number3)+" &asymp; "
            self.answer = self.RoundOffNumber1 + self.RoundOffNumber2 - self.RoundOffNumber3
            self.flag = 3
        elif self.ProblemSelector == 4:
            self.problem = self.problem + str(self.number1)+" - "+str(self.number2)+" + "+str(self.number3)+" &asymp; "
            self.answer = self.RoundOffNumber1 - self.RoundOffNumber2 + self.RoundOffNumber3
            self.flag = 4            
        
        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = []    
        self.wrongAnswers.append(str(self.answer+100))
        if self.answer > 100:
            self.wrongAnswers.append(str(self.answer-100))
        self.wrongAnswers.append(str(self.answer+1000))
        self.wrongAnswers.append(str(self.answer+10))
        if self.answer > 10:
            self.wrongAnswers.append(str(self.answer-10))
        
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.numbers,self.roundOff,self.roundOff1,self.roundOff2,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
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