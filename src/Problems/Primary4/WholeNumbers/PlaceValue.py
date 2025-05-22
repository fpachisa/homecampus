'''
Created on Jan 11, 2012
Module: PlaceValue
Generates the PlaceValue problems for Primary 5

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

class PlaceValue:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        random = randint(1,8)
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
            if randint(1,2)==1:
                return self.GenerateProblemType5()
            else:
                return self.GenerateProblemTypeMCQ5()
        elif random==6:
            if randint(1,2)==1:
                return self.GenerateProblemType6()
            else:
                return self.GenerateProblemTypeMCQ6()
        elif random==7:
            if randint(1,2)==1:
                return self.GenerateProblemType7()
            else:
                return self.GenerateProblemTypeMCQ7()
        elif random==8:
            if randint(1,2)==1:
                return self.GenerateProblemType8()
            else:
                return self.GenerateProblemTypeMCQ8()
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType5","ProblemTypeMCQ5",],
                            6:["ProblemType6","ProblemTypeMCQ6",],
                            7:["ProblemType7","ProblemTypeMCQ7",],
                            8:["ProblemType8","ProblemTypeMCQ8",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemType5(),self.GenerateProblemTypeMCQ5(),],
                                    6:[self.GenerateProblemType6(),self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemType7(),self.GenerateProblemTypeMCQ7(),],
                                    8:[self.GenerateProblemType8(),self.GenerateProblemTypeMCQ8(),],
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
        #return self.GenerateProblemTypeMCQ8()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),
                            "ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g.:
        What does the digit 7 stand for in 71453? '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 5)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.digitPlace = randint(0,len(self.digits)-1)      
        self.randomDigit = self.digits[self.digitPlace]
        
        self.problem1 = "What is the value of %s in %s?" %(self.randomDigit, self.number)
        self.problem2 = "What does the digit %s stand for in %s?" %(self.randomDigit, self.number)
        
        self.problem = random.choice([self.problem1,self.problem2])
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.randomDigit
        self.multiplier = str(1)
        for _i in range(5-self.digitPlace-1):
            self.multiplier = self.multiplier + '0'
        
        self.answer = str(self.answer*int(self.multiplier))

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number,self.randomDigit,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType1(self,problem,answer,number,RandomDigit,multiplier):
        self.PlaceValue = {1:"ten thousands",2:"thousands",3:"hundreds",4:"tens",5:"ones"}
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Create a place value table as shown below:<br>"
        self.solution_text = self.solution_text + "<table id=explanation border=1><tr>"
        for i in range(5):
            self.solution_text = self.solution_text + "<td>"+self.PlaceValue[i+1]+"</td>"
        self.solution_text = self.solution_text + "</tr><tr>"
        for i in range(5):
            self.solution_text = self.solution_text + "<td>"+str(number)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br><br>"
        self.solution_text = self.solution_text + "Since the "+str(RandomDigit)+" is in "+self.PlaceValue[5-len(str(multiplier))+1]+" place, the value of it is "+str(RandomDigit)+" x "+multiplier
        self.solution_text = self.solution_text + " = "+answer   
        self.solution_text = self.solution_text + "<br><br><i><b>The value of digit "+str(RandomDigit)+" in "+str(number)+" = "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
                
    def GenerateProblemType2(self):
        '''e.g.:
            Write the missing number:
            47815 = 40000+___+800+10+5'''
        
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''First digit cannot be zero'''
        self.firstDigit = random.sample([1,2,3,4,5,6,7,8,9], 1)
        self.digits = random.sample([0,1,2,3,4,5,6,7,8,9], 4)
        self.digits = self.firstDigit + self.digits
        
        self.number = ''
        self.breakDown = []
        for d in self.digits:
            self.number = self.number + str(d)
            
        i = len(self.digits)
        while i != 0:
            self.breakDownDigit = str(self.digits[len(self.digits)-i])          
            i =i-1
            
            '''If the digit is zero don't generate the breakdown
            e.g.: 350847 = ___+50000+800+40+7'''
            if(self.breakDownDigit!='0'):
                for _j in range(i):
                    self.breakDownDigit = self.breakDownDigit + '0'
                self.breakDown.append(self.breakDownDigit)
        
        self.missingDigit = randint(0,len(self.breakDown)-1)
        rand = randint(1,10)
        '''80% of the time pattern would be 123456 = 100000+____+3000+400+50+6        
        20% of the time pattern would be ______ = 100000+20000+3000+400+50+6'''
        self.flag = ''
        if (rand<=8):
            self.answer = self.breakDown[self.missingDigit]
            self.breakDown[self.missingDigit]="___"
            self.flag = '1'
        else:
            self.answer = self.number
            self.number = "___"
            self.flag = '2'
        '''80% of the time pattern would be 123456 = 100000+____+3000+400+50+6        
        20% of the time pattern would be 123456 = 6+3000+100000+400+_____'''        
        if(rand<=8):       
            self.problem = "Write the missing number:<br> %s = %s" %(self.number,"+".join(self.breakDown))
        else:
            self.flag = self.flag + '1'
            ''' copying to another list as don't want to shuffle the original list'''
            self.breakDown1 = list(self.breakDown)
            random.shuffle(self.breakDown1)
            self.problem = "Write the missing number:<br> %s = %s" %(self.number,"+".join(self.breakDown1))
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.breakDown,self.missingDigit,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType2(self,problem,answer,number,breakDown,missingDigit,flag):
        self.PlaceValue = {1:"ten thousands",2:"thousands",
                           3:"hundreds",4:"tens",5:"ones"}      
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        if flag == '1' or flag == '11':
            breakDown[missingDigit] = answer         
            self.solution_text = self.solution_text + "Create a place value table as shown below:<br>"
            self.solution_text = self.solution_text + "<table id=explanation border=1><tr>"
            for i in range(5):
                self.solution_text = self.solution_text + "<td>"+self.PlaceValue[i+1]+"</td>"
            self.solution_text = self.solution_text + "</tr><tr>"
            for i in range(5):
                self.solution_text = self.solution_text + "<td>"+str(number)[i]+"</td>"
            self.solution_text = self.solution_text + "</tr></table><br>"
            self.solution_text = self.solution_text + "Based on the above table the number "+str(number)+" can be represented as<br>"
            self.solution_text = self.solution_text +  "+".join(breakDown)
            self.solution_text = self.solution_text + "<br><br><i><b>Hence the missing number is "+str(answer)+"</b></i>"
        elif flag == '2':
            self.solution_text = self.solution_text + "The missing number can be constructed by joining the first digit of given numbers<br>"
            self.solution_text = self.solution_text + "Hence the missing number is "
            self.solution_text = self.solution_text + str(answer)
        elif flag == '21':
            self.solution_text = self.solution_text + "First re-arrange the numbers from largest to smallest like shown below:<br><br>"
            self.solution_text = self.solution_text +  "+".join(breakDown)
            self.solution_text = self.solution_text + "<br>Then the missing number can be constructed by joining the first digit of above re-arranged numbers<br>"
            self.solution_text = self.solution_text + "Hence the missing number is "
            self.solution_text = self.solution_text + str(answer)
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g.:
         What number is 100 less than 353400?
        '''
        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.value = [100,1000,10000,200,2000,20000,300,3000,30000,
                      400,4000,40000,500,5000,50000]
        self.number = randint(50001,99999)
        self.randomIndex = randint(0,len(self.value)-1)

        if(randint(1,2)==1):
            self.flag = 'add'
            if(randint(1,2)==1):
                self.problem = "What number is %d more than %d?" %(self.value[self.randomIndex],self.number)
            else:
                self.problem = "%d more than %d is:" %(self.value[self.randomIndex],self.number)
            self.answer = self.value[self.randomIndex] + self.number
        else:
            self.flag = 'sub'
            if(randint(1,2)==1):
                self.problem = "What number is %d less than %d?" %(self.value[self.randomIndex],self.number)
            else:
                self.problem = "%d less than %d is:" %(self.value[self.randomIndex],self.number)
            self.answer = self.number - self.value[self.randomIndex]
                        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.number,self.value[self.randomIndex],self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType3(self,problem,answer,number,value,flag):   
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        if flag == 'add':      
            self.solution_text = self.solution_text + "To get the correct answer add "+str(value)+" to "+str(number)+":<br>"
            self.solution_text = self.solution_text + str(number)+" + "+str(value)+" = "+str(answer)
            self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+str(answer)+"</b></i>"
        elif flag == 'sub':
            self.solution_text = self.solution_text + "To get the correct answer subtract "+str(value)+" from "+str(number)+":<br>"
            self.solution_text = self.solution_text + str(number)+" - "+str(value)+" = "+str(answer)
            self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+str(answer)+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType4(self):
        '''e.g.:
        9136485
        Which digit is in ten thousands place'''

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 5)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
            
        self.digitPlace = {"tens":3,"hundreds":2,"thousands":1,"ten thousands":0}
        
        self.place = self.digitPlace.keys()[randint(0,len(self.digitPlace)-1)]
        
        self.answer = self.digits[self.digitPlace[self.place]]
        self.problem = "%s<br>Which digit is in the %s place?" %(self.number,self.place)
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,str(self.answer),self.number,self.place)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType4(self,problem,answer,number,place):
        self.PlaceValue = {1:"ten thousands",2:"thousands",3:"hundreds",4:"tens",5:"ones"}
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Create a place value table as shown below:<br>"
        self.solution_text = self.solution_text + "<table id=explanation border=1><tr>"
        for i in range(5):
            self.solution_text = self.solution_text + "<td>"+self.PlaceValue[i+1]+"</td>"
        self.solution_text = self.solution_text + "</tr><tr>"
        for i in range(5):
            self.solution_text = self.solution_text + "<td>"+str(number)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br><br>"
        self.solution_text = self.solution_text + "Hence the number at the "+place+" place is:"
        self.solution_text = self.solution_text + "<br><br><i><b>"+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5(self):
        '''e.g.:
        How many tens are there in 16000?
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        
        '''Generating a 5 digit number with 3 zeroes at the end'''
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 2)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.zeroes = '000'
        self.number = self.number + self.zeroes
            
        self.digitPlace = {"tens":10,"hundreds":100,"thousands":1000}
        
        '''Randomly select tens, hundreds or thousands keyword in the problem'''
        self.randPlace = randint(0,2)        
        self.problem = "How many %s are there in %s?" %(self.digitPlace.keys()[self.randPlace],self.number)
        
        self.answer =int(self.number)/(self.digitPlace[self.digitPlace.keys()[self.randPlace]])
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,str(self.answer),self.number,self.digitPlace.keys()[self.randPlace])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType5(self,problem,answer,number,place):
        self.PlaceValue = {"tens":1,"hundreds":2,"thousands":3}
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        if (self.PlaceValue[place]==1):
            self.solution_text = self.solution_text + "To find out how many "+place+" is there in "+str(number)+" remove "+str(self.PlaceValue[place])+" zero from it"+":<br>"
            self.solution_text = self.solution_text + "Removing "+str(self.PlaceValue[place])+" zero give us the number:"
        else:
            self.solution_text = self.solution_text + "To find out how many "+place+" is there in "+str(number)+" remove "+str(self.PlaceValue[place])+" zeroes from it"+":<br>"
            self.solution_text = self.solution_text + "Removing "+str(self.PlaceValue[place])+" zeroes give us the number:"
        self.solution_text = self.solution_text + "<br><br><i><b>"+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6(self):
        '''e.g.:
        How many hundreds must be added to 26000 to make 50000?
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        '''Generating a 5 digit number with 3 zeroes at the end'''
        self.digits = random.sample([1,2,3,4,5,6,7,8], 2)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.zeroes = '000'
        self.number = self.number + self.zeroes
            
        self.digitPlace = {"tens":10,"hundreds":100}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.answer = randint(10,90)
        self.finalNumber = self.digitPlace[self.digitPlace.keys()[self.randPlace]]*self.answer + int(self.number)        
        self.problem = "How many %s must be added to %s to make %d?" %(self.digitPlace.keys()[self.randPlace],self.number,self.finalNumber)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,str(self.answer),int(self.number),self.finalNumber,self.digitPlace.keys()[self.randPlace])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType6(self,problem,answer,number,finalNumber,place):
        self.PlaceValue = {"tens":1,"hundreds":2,"thousands":3}
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "First, subtract "+str(number)+" from "+str(finalNumber)+"<br>"
        self.solution_text = self.solution_text + str(finalNumber)+" - "+str(number)+" = "+str(finalNumber-number)+"<br><br>"
        if (self.PlaceValue[place]==1):
            self.solution_text = self.solution_text + "To find out how many "+place+" is there in "+str(finalNumber-number)+" remove "+str(self.PlaceValue[place])+" zero from it"+":<br>"
            self.solution_text = self.solution_text + "Removing "+str(self.PlaceValue[place])+" zero give us the number:"
        else:
            self.solution_text = self.solution_text + "To find out how many "+place+" is there in "+str(finalNumber-number)+" remove "+str(self.PlaceValue[place])+" zeroes from it"+":<br>"
            self.solution_text = self.solution_text + "Removing "+str(self.PlaceValue[place])+" zeroes give us the number:"
        self.solution_text = self.solution_text + "<br><br><i><b>"+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7(self):
        '''e.g.:
        280 tens more than 46 020 is:
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        '''Generating a random number'''
        self.number = randint(10000,60000)
            
        self.digitPlace = {"tens":10,"hundreds":100,}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.multiplier = randint(100,250)
        
        self.problem = "%d %s more than %d is:" %(self.multiplier,self.digitPlace.keys()[self.randPlace],self.number)
        self.answer = (self.digitPlace[self.digitPlace.keys()[self.randPlace]])*self.multiplier + self.number
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,str(self.answer),self.number,self.multiplier,self.digitPlace.keys()[self.randPlace])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType7(self,problem,answer,number,multiplier,place):
        self.PlaceValue = {"tens":10,"hundreds":100,"thousands":1000}
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        if (self.PlaceValue[place]==10):
            self.solution_text = self.solution_text + "To find the value of "+str(multiplier)+" "+place+", add "+str(len(str(self.PlaceValue[place]))-1)+" zero to it"+"<br>"
            self.solution_text = self.solution_text + "adding "+str(len(str(self.PlaceValue[place]))-1)+" zero to "+str(multiplier)+" gives "+str(multiplier*self.PlaceValue[place])+"<br><br>"
        else:
            self.solution_text = self.solution_text + "To find the value of "+str(multiplier)+" "+place+", add "+str(len(str(self.PlaceValue[place]))-1)+" zeroes to it"+"<br>"
            self.solution_text = self.solution_text + "adding "+str(len(str(self.PlaceValue[place]))-1)+" zeroes to "+str(multiplier)+" gives "+str(multiplier*self.PlaceValue[place])+"<br><br>"
        self.solution_text = self.solution_text + "now add "+str(multiplier*self.PlaceValue[place])+" to "+str(number)+" to get the answer<br>"
        self.solution_text = self.solution_text + str(multiplier*self.PlaceValue[place])+" + "+str(number)+" = "
        self.solution_text = self.solution_text + "<br><br><i><b>"+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8(self):
        '''e.g.:
        2 ten thousand 1 hundred 24 ones=
        '''
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.TenThousandDigit = randint(2,9)
        self.hundredDigit = randint(10,99)
        self.onesDigit = randint(10,99)
        
        self.problem = "%d ten thousands %d hundreds %d ones=______(in figures)" % (self.TenThousandDigit,
                                                                                 self.hundredDigit,self.onesDigit)
        
        self.answer = self.TenThousandDigit*10000+self.hundredDigit*100+self.onesDigit
        self.number = str(self.TenThousandDigit)+str(self.hundredDigit)+str(self.onesDigit)
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.number,str(self.answer),self.TenThousandDigit,self.hundredDigit,self.onesDigit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}

    def ExplainType8(self,problem,number,answer,TD,HD,OD):
        self.PlaceValue = {1:"ten thousands",2:"thousands",3:"hundreds",4:"tens",5:"ones"}
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Create a place value table as shown below and insert the numbers given at appropriate places:<br>"
        self.solution_text = self.solution_text + "<table id=explanation border=1><tr>"
        for i in range(5):
            self.solution_text = self.solution_text + "<td>"+self.PlaceValue[i+1]+"</td>"
        self.solution_text = self.solution_text + "</tr><tr>"
        for i in range(5):
            self.solution_text = self.solution_text + "<td></td>"            
        self.solution_text = self.solution_text + "</tr></table><br><br>"
        self.solution_text = self.solution_text + "First insert "+str(TD)+" at ten thousands place, now since there is a 2 digit number for hundreds the first digit("+number[1]+ ") will go to thousands place and second one("+number[2]+") will go to hundreds place.<br>"
        self.solution_text = self.solution_text + "Fill in rest of the places in similar fashion. The place value table will look like this<br>"
        self.solution_text = self.solution_text + "<table id=explanation border=1><tr>"
        for i in range(5):
            self.solution_text = self.solution_text + "<td>"+self.PlaceValue[i+1]+"</td>"
        self.solution_text = self.solution_text + "</tr><tr>"
        for i in range(5):
            self.solution_text = self.solution_text + "<td>"+str(number)[i]+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        self.solution_text = self.solution_text + "write all these numbers together and you get your answer."
        self.solution_text = self.solution_text + "<br><br><i><b>"+answer+"</b></i>"
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
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type,
                'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}
        

    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        What does the digit 7 stand for in 71453? '''
        
        self.problem_type = "ProblemTypeMCQ1"
        self.complexity_level = "easy"
        self.HCScore = 3
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 5)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.digitPlace = randint(0,len(self.digits)-1)      
        self.randomDigit = self.digits[self.digitPlace]
        
        self.problem1 = "What is the value of %s in %s?" %(self.randomDigit, self.number)
        self.problem2 = "What does the digit %s stand for in %s?" %(self.randomDigit, self.number)
        
        self.problem = random.choice([self.problem1,self.problem2])
                
        self.template = "MCQTypeProblems.html"
        
        self.answer = self.randomDigit
        self.multiplier = str(1)
        for _i in range(5-self.digitPlace-1):
            self.multiplier = self.multiplier + '0'
        
        self.answer = str(self.answer*int(self.multiplier))
        
        self.wrongAnswers = []    
        ''' entering different number of zeroes behind the correct digit'''
        for i in range(5):
            self.wrongAnswer = str(self.randomDigit)
            for j in range(i):
                self.wrongAnswer = self.wrongAnswer + '0'
            self.wrongAnswers.append(self.wrongAnswer)
        
        '''Adding other digits other than zeroes behind the correct digit'''
        for i in range(self.digitPlace,len(self.digits)):
            self.wrongAnswer = str(self.randomDigit)
            for j in range(i-1,len(self.digits)):
                self.wrongAnswer = self.wrongAnswer + str(self.digits[j])
            self.wrongAnswers.append(self.wrongAnswer)
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number,self.randomDigit,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
            Write the missing number:
            47815 = 40000+___+800+10+5'''
        self.problem_type = "ProblemTypeMCQ2"
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''First digit cannot be zero'''
        self.firstDigit = random.sample([1,2,3,4,5,6,7,8,9], 1)
        self.digits = random.sample([0,1,2,3,4,5,6,7,8,9], 4)
        self.digits = self.firstDigit + self.digits
        
        self.number = ''
        self.breakDown = []
        for d in self.digits:
            self.number = self.number + str(d)
            
        i = len(self.digits)
        while i != 0:
            self.breakDownDigit = str(self.digits[len(self.digits)-i])          
            i =i-1
            
            '''If the digit is zero don't generate the breakdown
            e.g.: 350847 = ___+50000+800+40+7'''
            if(self.breakDownDigit!='0'):
                for _j in range(i):
                    self.breakDownDigit = self.breakDownDigit + '0'
                self.breakDown.append(self.breakDownDigit)
        
        self.wrongAnswers = []
        '''Generating wrong answers'''            
        for i in range(len(self.breakDown)):
            self.wrongAnswers.append(self.breakDown[i])        

        self.missingDigit = randint(0,len(self.breakDown)-1)
        rand = randint(1,10)
        '''80% of the time pattern would be 123456 = 100000+____+3000+400+50+6        
        20% of the time pattern would be ______ = 100000+20000+3000+400+50+6'''
        self.flag = ''
        if (rand<=8):
            self.answer = self.breakDown[self.missingDigit]
            self.breakDown[self.missingDigit]="___"
            self.flag = '1'
        else:
            self.answer = self.number
            self.number = "___"
            self.flag = '2'
        '''80% of the time pattern would be 123456 = 100000+____+3000+400+50+6        
        20% of the time pattern would be 123456 = 6+3000+100000+400+_____'''        
        if(rand<=8):       
            self.problem = "Write the missing number:<br> %s = %s" %(self.number,"+".join(self.breakDown))
        else:
            self.flag = self.flag + '1'
            ''' copying to another list as don't want to shuffle the original list'''
            self.breakDown1 = list(self.breakDown)
            random.shuffle(self.breakDown1)
            self.problem = "Write the missing number:<br> %s = %s" %(self.number,"+".join(self.breakDown1))

        self.template = "MCQTypeProblems.html"
        
        '''This problem type is not using generic method GenerateMCQ because only 2 wrong answers are 
        randomly selected in this problem unlike 3 in rest'''
        
        '''Removing correct answers from the wrongAnswers list'''
        self.wrongAnswers = filter(self.removeCorrectAnswer,self.wrongAnswers)
        
        '''Randomly selecting 2 wrong answer and 1 wrong answer and 1 correct answer is always included
        in this example the wrong answer which is always included is 7815'''                     
        self.wrongAnswers = random.sample(self.wrongAnswers,2)
        self.wrongAnswer =''
        for i in range(self.missingDigit,len(self.digits)):
            self.wrongAnswer = self.wrongAnswer + str(self.digits[i])
            
        '''If the correct answer is the last digit of the number then the wrong answer would be same as
        correct answer so checking for that. 
        for e.g.: 247815 = 200000+40000+7000+800+10+___. In this case wrong answer is changed to 55'''
        if (self.wrongAnswer==self.answer):
            self.wrongAnswer = self.wrongAnswer * 2
            
        self.wrongAnswers.append(self.wrongAnswer)
        self.wrongAnswers.append(self.answer)
        random.shuffle(self.wrongAnswers)
        self.answer1 = str(self.wrongAnswers[0])
        self.answer2 = str(self.wrongAnswers[1])
        self.answer3 = str(self.wrongAnswers[2])
        self.answer4 = str(self.wrongAnswers[3])        

        self.value1 = self.answer1
        self.value2 = self.answer2
        self.value3 = self.answer3
        self.value4 = self.answer4
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.breakDown,self.missingDigit,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
             
        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'answer4':self.answer4,'value1':self.value1,'value2':self.value2
                ,'value3':self.value3,'value4':self.value4,'explain':self.explain,'problem_type':self.problem_type,
                'grade':self.grade,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":self.CheckAnswerType}
        
    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
         What number is 100 less than 353400?
        '''
        self.problem_type = "ProblemTypeMCQ3"
        self.CheckAnswerType = 1
        self.grade = 4
        
        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.value = [100,1000,10000,200,2000,20000,300,3000,30000,
                      400,4000,40000,500,5000,50000]
        self.number = randint(50001,80000)
        self.randomIndex = randint(0,len(self.value)-1)

        if(randint(1,2)==1):
            self.flag = 'add'
            if(randint(1,2)==1):
                self.problem = "What number is %d more than %d?" %(self.value[self.randomIndex],self.number)
            else:
                self.problem = "%d more than %d is:" %(self.value[self.randomIndex],self.number)
            self.answer = self.value[self.randomIndex] + self.number
        else:
            self.flag = 'sub'
            if(randint(1,2)==1):
                self.problem = "What number is %d less than %d?" %(self.value[self.randomIndex],self.number)
            else:
                self.problem = "%d less than %d is:" %(self.value[self.randomIndex],self.number)
            self.answer = self.number - self.value[self.randomIndex]
        
        self.template = "MCQTypeProblems.html"           

        self.wrongAnswers = []
        self.wrongAnswers.append(self.answer+100)
        self.wrongAnswers.append(self.answer-100)
        self.wrongAnswers.append(self.answer+1000)
        self.wrongAnswers.append(self.answer-1000)

                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.number,self.value[self.randomIndex],self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ4(self):
        '''e.g.:
        9136485
        Which digit is in ten thousands place'''
        self.problem_type = "ProblemTypeMCQ4"
        self.CheckAnswerType = 1
        self.grade = 4
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 5)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
            
        self.digitPlace = {"tens":3,"hundreds":2,"thousands":1,"ten thousands":0}
        
        self.place = self.digitPlace.keys()[randint(0,len(self.digitPlace)-1)]
        
        self.answer = self.digits[self.digitPlace[self.place]]
        self.problem = "%s<br>Which digit is in the %s place?" %(self.number,self.place)
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers = self.digits
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,str(self.answer),self.number,self.place)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ5(self):
        '''e.g.:
        How many tens are there in 16000?
        '''
        self.problem_type = "ProblemTypeMCQ5"
        self.CheckAnswerType = 1
        self.grade = 4
        self.complexity_level = "medium"
        self.HCScore = 5
        
        '''Generating a 5 digit number with 3 zeroes at the end'''
        self.digits = random.sample([1,2,3,4,5,6,7,8,9], 2)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.zeroes = '000'
        self.number = self.number + self.zeroes
            
        self.digitPlace = {"tens":10,"hundreds":100,"thousands":1000}
        
        '''Randomly select tens, hundreds or thousands keyword in the problem'''
        self.randPlace = randint(0,2)        
        self.problem = "How many %s are there in %s?" %(self.digitPlace.keys()[self.randPlace],self.number)
        
        self.answer =int(self.number)/(self.digitPlace[self.digitPlace.keys()[self.randPlace]])
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers=[]
        self.wrongAnswers.append(divmod(int(self.number),10)[0])
        self.wrongAnswers.append(divmod(int(self.number),100)[0])
        self.wrongAnswers.append(divmod(int(self.number),1000)[0])
        self.wrongAnswers.append(divmod(int(self.number),10000)[0])
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,str(self.answer),self.number,self.digitPlace.keys()[self.randPlace])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ6(self):
        '''e.g.:
        How many hundreds must be added to 26000 to make 50000?
        '''
        self.problem_type = "ProblemTypeMCQ6"
        self.CheckAnswerType = 1
        self.grade = 4
        self.complexity_level = "medium"
        self.HCScore = 5
        '''Generating a 5 digit number with 3 zeroes at the end'''
        self.digits = random.sample([1,2,3,4,5,6,7,8], 2)
        self.number = ''
        for d in self.digits:
            self.number = self.number + str(d)
        self.zeroes = '000'
        self.number = self.number + self.zeroes
            
        self.digitPlace = {"tens":10,"hundreds":100}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.answer = randint(10,90)
        self.finalNumber = self.digitPlace[self.digitPlace.keys()[self.randPlace]]*self.answer + int(self.number)        
        self.problem = "How many %s must be added to %s to make %d?" %(self.digitPlace.keys()[self.randPlace],self.number,self.finalNumber)
        
        self.wrongAnswers = []
        self.wrongAnswers.append(int((self.finalNumber-int(self.number))/10))
        self.wrongAnswers.append(int((self.finalNumber-int(self.number))/100))
        self.wrongAnswers.append(int((self.finalNumber-int(self.number))/1000))
        self.wrongAnswers.append(int((self.finalNumber-int(self.number))))
        
        self.template = "MCQTypeProblems.html"
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,str(self.answer),int(self.number),self.finalNumber,self.digitPlace.keys()[self.randPlace])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ7(self):
        '''e.g.:
        280 tens more than 46 020 is:
        '''
        self.problem_type = "ProblemTypeMCQ7"
        self.CheckAnswerType = 1
        self.grade = 4
        self.complexity_level = "medium"
        self.HCScore = 5
        '''Generating a random number'''
        self.number = randint(10000,60000)
            
        self.digitPlace = {"tens":10,"hundreds":100,}
        
        '''Randomly select tens, hundreds keyword in the problem'''
        self.randPlace = randint(0,len(self.digitPlace)-1)
        self.multiplier = randint(100,250)
        
        self.problem = "%d %s more than %d is:" %(self.multiplier,self.digitPlace.keys()[self.randPlace],self.number)
        self.answer = (self.digitPlace[self.digitPlace.keys()[self.randPlace]])*self.multiplier + self.number
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.number + self.multiplier*10)
        self.wrongAnswers.append(self.number + self.multiplier*100)
        self.wrongAnswers.append(self.number - self.multiplier*10)
        self.wrongAnswers.append(self.number + self.multiplier)
        
        self.template = "MCQTypeProblems.html"
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,str(self.answer),self.number,self.multiplier,self.digitPlace.keys()[self.randPlace])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)

    def GenerateProblemTypeMCQ8(self):
        '''e.g.:
        2 ten thousand 1 hundred 24 ones=
        '''
        self.problem_type = "ProblemTypeMCQ8"
        self.CheckAnswerType = 1
        self.grade = 4
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.TenThousandDigit = randint(2,9)
        self.hundredDigit = randint(10,99)
        self.onesDigit = randint(10,99)
        
        self.problem = "%d ten thousands %d hundreds %d ones=______(in figures)" % (self.TenThousandDigit,
                                                                                 self.hundredDigit,self.onesDigit)
        
        self.answer = self.TenThousandDigit*10000+self.hundredDigit*100+self.onesDigit
        self.number = str(self.TenThousandDigit)+str(self.hundredDigit)+str(self.onesDigit)
        
        self.wrongAnswers = []
        self.wrongAnswers.append(self.TenThousandDigit*1000+self.hundredDigit*100+self.onesDigit)
        self.wrongAnswers.append(self.TenThousandDigit*10000+self.hundredDigit*1000+self.onesDigit)
        self.wrongAnswers.append(self.TenThousandDigit*10000+self.hundredDigit*100+self.onesDigit*10)
        self.wrongAnswers.append(self.TenThousandDigit*1000+self.hundredDigit*1000+self.onesDigit*10)
        
        self.template = "MCQTypeProblems.html"
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.number,str(self.answer),self.TenThousandDigit,self.hundredDigit,self.onesDigit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)   
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        try:
            return (int(answer)==int(InputAnswer))
        except ValueError:
            return False                           
    