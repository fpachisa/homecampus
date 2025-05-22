'''
Module: WriteInFigures
It generates WriteInFigures problems for Primary 5.

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2010, Home Campus.  All Rights Reserved.

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
                      
        self.ProblemType = {1:"ProblemType1",2:"ProblemTypeMCQ2",3:"ProblemType3",4:"ProblemTypeMCQ4",5:"ProblemType5",
                            6:"ProblemTypeMCQ1",7:"ProblemType2",8:"ProblemTypeMCQ3",9:"ProblemType4",10:"ProblemTypeMCQ5",}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemTypeMCQ2(),3:self.GenerateProblemType3(),
                                    4:self.GenerateProblemTypeMCQ4(),5:self.GenerateProblemType5(),6:self.GenerateProblemTypeMCQ1(),
                                    7:self.GenerateProblemType2(),8:self.GenerateProblemTypeMCQ3(),9:self.GenerateProblemType4(),
                                    10:self.GenerateProblemTypeMCQ5()}
        
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
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            }
        return self.ProblemType[problem_type]
                        
    def GenerateProblemType1(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.problem = "Write in figures:<br/>"
        self.number = randint(1000000,99999999)
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
                'grade':5,"complexity_level":self.complexity_level,"HCScore":self.HCScore,}
       
    def GenerateProblemType2(self):
        self.personName = random.choice(PersonName.PersonName)
        self.action = random.choice(["sold","bought","purchased"])
        self.itemPool = {"a car":randint(50000,150000),"a luxury car":randint(250000,700000),
                "an apartment":randint(200000,500000),"a condominium":randint(800000,2000000)}
        self.item = self.itemPool.keys()[randint(0,len(self.itemPool)-1)]
        self.amount = self.itemPool[self.item]
        f = Figures2Words.Figures2Words()
        self.NumberInWords = f.toWords(self.amount)
        self.problem = "%s %s %s for %s.<br> Write the amount in figures" %(self.personName,self.action,self.item,self.NumberInWords)
        self.answer = str(self.amount)
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.amount))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2"}

    def GenerateProblemType3(self):
        self.number = randint(50000,500000)
        f = Figures2Words.Figures2Words()
        self.NumberInWords = f.toWords(self.number)
        self.personName = random.choice(PersonName.PersonName)
        self.problem = "Annual salary of %s is %s.<br>Write the amount in figures" %(self.personName,self.NumberInWords)
        self.answer = str(self.number)
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3"}
    
    def GenerateProblemType4(self):
        self.number = randint(100000,2500000)
        self.lottery = random.choice(["Hot Lotto","TOTO","4D","World Lottery"])
        f = Figures2Words.Figures2Words()
        self.NumberInWords = f.toWords(self.number)
        self.problem = "The next %s jackpot prize money is %s.<br>Write the amount in figures." %(self.lottery,self.NumberInWords)
        self.answer = str(self.number)
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4"}
        
    def GenerateProblemType5(self):
        if (randint(1,2)==1):
            self.personName = random.choice(PersonName.BoyName)
            self.gender = "him"
        else:
            self.personName = random.choice(PersonName.GirlName)
            self.gender = "her"

        self.action = random.choice(["bought","purchased"])
        self.itemPool = {"a luxury car":randint(250000,700000),
                "an apartment":randint(200000,500000),"a condominium":randint(800000,2000000)}
        self.items = random.sample(self.itemPool.keys(),2)
        self.amount1 = self.itemPool[self.items[0]]
        self.amount2 = self.itemPool[self.items[1]]
        f = Figures2Words.Figures2Words()
        self.NumberInWords1 = f.toWords(self.amount1)
        self.NumberInWords2 = f.toWords(self.amount2)
        self.problem = "%s %s %s for %s and %s for %s.<br> Write the total amount spent by %s in figures:" %(self.personName,self.action,self.items[0],self.NumberInWords1,self.items[1],self.NumberInWords2,self.gender)
        self.answer = str(self.amount1+self.amount2)
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.amount1,self.amount2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5"}
                   
    def GenerateProblemTypeMCQ1(self):
        self.problem_type = "ProblemTypeMCQ1"
        self.problem = "Choose the correct answer:</br>"
        self.number = randint(1000000,99999999)
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
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain)

    def GenerateProblemTypeMCQ2(self):
        self.problem_type = "ProblemTypeMCQ2"
        self.personName = random.choice(PersonName.PersonName)
        self.action = random.choice(["sold","bought","purchased"])
        self.itemPool = {"a car":randint(50000,150000),"a luxury car":randint(250000,700000),
                "an apartment":randint(200000,500000),"a condominium":randint(800000,2000000)}
        self.item = self.itemPool.keys()[randint(0,len(self.itemPool)-1)]
        self.amount = self.itemPool[self.item]
        f = Figures2Words.Figures2Words()
        self.NumberInWords = f.toWords(self.amount)
        self.problem = "%s %s %s for %s.<br>Choose the correct amount in figures" %(self.personName,self.action,self.item,self.NumberInWords)
        self.answer = str(self.amount)
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.amount))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain)

    def GenerateProblemTypeMCQ3(self):
        self.problem_type = "ProblemTypeMCQ3"
        self.number = randint(50000,500000)
        f = Figures2Words.Figures2Words()
        self.NumberInWords = f.toWords(self.number)
        self.personName = random.choice(PersonName.PersonName)
        self.problem = "Annual salary of %s is %s.<br>Choose the correct amount in figures" %(self.personName,self.NumberInWords)
        self.answer = str(self.number)
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain)

    def GenerateProblemTypeMCQ4(self):
        self.problem_type = "ProblemTypeMCQ4"
        self.number = randint(100000,2500000)
        self.lottery = random.choice(["Hot Lotto","TOTO","4D","World Lottery"])
        f = Figures2Words.Figures2Words()
        self.NumberInWords = f.toWords(self.number)
        self.problem = "The next %s jackpot prize money is %s.<br>Choose the correct amount in figures." %(self.lottery,self.NumberInWords)
        self.answer = str(self.number)
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,str(self.number))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain)

    def GenerateProblemTypeMCQ5(self):
        if (randint(1,2)==1):
            self.personName = random.choice(PersonName.BoyName)
            self.gender = "him"
        else:
            self.personName = random.choice(PersonName.GirlName)
            self.gender = "her"
        self.problem_type = "ProblemTypeMCQ5"
        self.action = random.choice(["bought","purchased"])
        self.itemPool = {"a car":randint(50000,150000),"a luxury car":randint(250000,700000),
                "an apartment":randint(200000,500000),"a condominium":randint(800000,2000000)}
        self.items = random.sample(self.itemPool.keys(),2)
        self.amount1 = self.itemPool[self.items[0]]
        self.amount2 = self.itemPool[self.items[1]]
        f = Figures2Words.Figures2Words()
        self.NumberInWords1 = f.toWords(self.amount1)
        self.NumberInWords2 = f.toWords(self.amount2)
        self.problem = "%s %s %s for %s and <br>%s for %s.<br> Choose the correct amount spent by %s in figures:" %(self.personName,self.action,self.items[0],self.NumberInWords1,self.items[1],self.NumberInWords2,self.gender)
        self.answer = str(self.amount1+self.amount2)
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.amount1,self.amount2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return self.GenerateGenericMCQ(self.problem,self.answer,self.problem_type,self.explain)
    
    def GenerateGenericMCQ(self,problem,answer,problem_type,explain=''):
        self.template = "MCQTypeProblems.html"
        answer = int(answer)
        '''All the values of wrongAnswers must be a string'''
        self.wrongAnswers = [str(answer + randint(1,25)),]
        self.wrongAnswers.append(str(answer - randint(1,25)))
        self.wrongAnswers.append(str(answer + randint(50,100)))
        self.wrongAnswers.append(str(answer - randint(50,100)))
        self.wrongAnswers.append(str(answer + randint(100,10000)))
        self.wrongAnswers.append(str(answer - randint(100,10000)))
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
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type}
        
    def checkAnswer(self,template,answer,InputAnswer):
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
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
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
        number = str(amount1+amount2)
        self.ThreeDigitGroup,self.remainder = divmod(len(number),3)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/><br/>"
        self.solution_text = self.solution_text + "Total amount spent = "+str(amount1)+" + "+str(amount2)+" = "+number+"<br/><br/>"
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