'''
Created on Sep 12, 2012
Module: P4FRWordProblems
Generates the "Fractions Word Problems" problems for Primary 4

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
from Problems import PersonName
from Utils import LcmGcf
import logging

class P4FRWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],
                            4:["ProblemType4",],5:["ProblemType5",],6:["ProblemType6",],
                            7:["ProblemType7a","ProblemType7b","ProblemType7c",],
                            }
        
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7a(),self.GenerateProblemType7b(),self.GenerateProblemType7c(),],
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
        #return self.GenerateProblemType2()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),                           
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7a":self.GenerateProblemType7a(),
                            "ProblemType7b":self.GenerateProblemType7b(),
                            "ProblemType7c":self.GenerateProblemType7c(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominator1 = randint(2,12)
        self.numerator1 = randint(1,self.denominator1-1)
        self.gcf1 = LcmGcf.LcmGcf().find_gcf(self.denominator1, self.numerator1)
        self.denominator1 = self.denominator1 / self.gcf1
        self.numerator1 = self.numerator1 / self.gcf1
        self.whole1 = randint(2,9)

        self.denominator2 = randint(2,12)
        self.numerator2 = randint(1,self.denominator2-1)
        self.gcf2 = LcmGcf.LcmGcf().find_gcf(self.denominator2, self.numerator2)
        self.denominator2 = self.denominator2 / self.gcf2
        self.numerator2 = self.numerator2 / self.gcf2
        self.whole2 = randint(2,9)

        self.denominator3 = random.choice([self.denominator1,self.denominator2])
        self.numerator3 = randint(1,self.denominator3-1)
        self.gcf3 = LcmGcf.LcmGcf().find_gcf(self.denominator3, self.numerator3)
        self.denominator3 = self.denominator3 / self.gcf3
        self.numerator3 = self.numerator3 / self.gcf3
        self.whole3 = randint(2,9)

        self.problem = "A farmer picked apples, bananas and oranges. He picked "+str(self.whole1)+" "+str(self.numerator1)+"&frasl;"+str(self.denominator1)+" kg of apples, "
        self.problem = self.problem + str(self.whole2)+" "+str(self.numerator2)+"&frasl;"+str(self.denominator2)+" kg of bananas and "
        self.problem = self.problem + str(self.whole3)+" "+str(self.numerator3)+"&frasl;"+str(self.denominator3)+" kg of oranges. Find the mass of fruits he picked altogether.<br><br>"
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
                
        if self.denominator1 == self.denominator3:
            self.AnswerNumerator = ((self.whole1*self.denominator1+self.numerator1)+(self.whole3*self.denominator3+self.numerator3))*self.denominator2+(self.whole2*self.denominator2+self.numerator2)*self.denominator1
        else:
            self.AnswerNumerator = ((self.whole2*self.denominator2+self.numerator2)+(self.whole3*self.denominator3+self.numerator3))*self.denominator1+(self.whole1*self.denominator1+self.numerator1)*self.denominator2
        
        self.AnswerDenominator = self.denominator1*self.denominator2
        
        self.AnswerGcf = LcmGcf.LcmGcf().find_gcf(self.AnswerDenominator,self.AnswerNumerator)
        self.AnswerDenominator = self.AnswerDenominator / self.AnswerGcf
        self.AnswerNumerator = self.AnswerNumerator / self.AnswerGcf
        
        div,mod = divmod(self.AnswerNumerator,self.AnswerDenominator)
        
        '''can't have answer as list (can't store list in datastore for tests module) so creating a string'''
        self.answer = str(div)+","+str(mod)+","+str(self.AnswerDenominator)
        
        self.CheckAnswerType = 1

        self.unit = "kg"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FractionAnswer':"Y"}            

    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<table id='fractionTable' class='FractionsTable'>" 
        self.answer_text = self.answer_text + "<tr><td>The correct answer is:&nbsp;</td>"
        answer = answer.split(",")
        self.answer0 = answer[0]
        self.answer1 = answer[1]
        self.answer2 = answer[2]
        if self.answer0!='0':
            self.answer_text = self.answer_text + "<td>"+self.answer0+"</td>"
        if self.answer1!='0':
            self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*(len(self.answer2)/2)+self.answer1+"&nbsp;"*(len(self.answer2)/2)+"</u><br>"+"&nbsp;"*(len(self.answer1)/2)+self.answer2+"</td>"
        self.answer_text = self.answer_text + "<td>&nbsp;"+unit+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary-Grade-4/Fractions/Fractions-Word-Problems-Grade-4#WP1' target='_blank'><u>Fractions: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name =  random.choice(PersonName.BoyName)
        
        self.denominator1 = random.choice([2,3,4,6,12])
        self.numerator1 = randint(1,self.denominator1-1)
        self.gcf1 = LcmGcf.LcmGcf().find_gcf(self.denominator1, self.numerator1)
        self.denominator1 = self.denominator1 / self.gcf1
        self.numerator1 = self.numerator1 / self.gcf1
        self.whole1 = randint(2,4)

        self.denominator2 = random.choice([2,3,4,6,12])
        self.numerator2 = randint(1,self.denominator2-1)
        self.gcf2 = LcmGcf.LcmGcf().find_gcf(self.denominator2, self.numerator2)
        self.denominator2 = self.denominator2 / self.gcf2
        self.numerator2 = self.numerator2 / self.gcf2
        self.whole2 = 0

        self.denominator3 = random.choice([self.denominator1,self.denominator2])
        self.numerator3 = randint(1,self.denominator3-1)
        self.gcf3 = LcmGcf.LcmGcf().find_gcf(self.denominator3, self.numerator3)
        self.denominator3 = self.denominator3 / self.gcf3
        self.numerator3 = self.numerator3 / self.gcf3
        self.whole3 = randint(2,4)
        
        if self.denominator1 == self.denominator3:
            self.TotalNumerator = ((self.whole1*self.denominator1+self.numerator1)+(self.whole3*self.denominator3+self.numerator3))*self.denominator2+(self.whole2*self.denominator2+self.numerator2)*self.denominator1
            self.TotalDenominator = self.denominator1*self.denominator2
        elif self.denominator2 == self.denominator3:
            self.TotalNumerator = ((self.whole2*self.denominator2+self.numerator2)+(self.whole3*self.denominator3+self.numerator3))*self.denominator1+(self.whole1*self.denominator1+self.numerator1)*self.denominator2
            self.TotalDenominator = self.denominator1*self.denominator2
        else:
            self.TotalNumerator = (self.whole1*self.denominator1+self.numerator1)*(self.denominator2*self.denominator3) + (self.whole2*self.denominator2+self.numerator2)*(self.denominator1*self.denominator3) + (self.whole3*self.denominator3+self.numerator3)*(self.denominator1*self.denominator2)
            self.TotalDenominator = self.denominator1*self.denominator2*self.denominator3
        
        
        self.TotalGcf = LcmGcf.LcmGcf().find_gcf(self.TotalDenominator,self.TotalNumerator)
        self.TotalDenominator = self.TotalDenominator / self.TotalGcf
        self.TotalNumerator = self.TotalNumerator / self.TotalGcf
        
        self.TotalWhole,self.TotalNumerator = divmod(self.TotalNumerator,self.TotalDenominator)        
       
        self.problem = self.name+" jogged "+str(self.TotalWhole)+" "
        if self.TotalNumerator!=0:
            self.problem = self.problem + str(self.TotalNumerator)+"&frasl;"+str(self.TotalDenominator)+" km altogether."
        self.problem = self.problem + " He jogged "+str(self.whole1)+" "+str(self.numerator1)+"&frasl;"+str(self.denominator1)+" km in the morning, "
        self.problem = self.problem + str(self.numerator2)+"&frasl;"+str(self.denominator2)+" km in the afternoon and the rest of the distance in the evening. How far did he jog in the evening?"
             
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        
        '''can't have answer as list (can't store list in datastore for tests module) so creating a string'''
        self.answer = str(self.whole3)+","+str(self.numerator3)+","+str(self.denominator3)
        
        self.CheckAnswerType = 1

        self.unit = "km"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FractionAnswer':"Y"}            

    def ExplainType2(self,problem,answer,unit):
        self.answer_text = "<table id='fractionTable' class='FractionsTable'>" 
        self.answer_text = self.answer_text + "<tr><td>The correct answer is:&nbsp;</td>"
        answer = answer.split(",")
        self.answer0 = answer[0]
        self.answer1 = answer[1]
        self.answer2 = answer[2]
        if self.answer0!='0':
            self.answer_text = self.answer_text + "<td>"+self.answer0+"</td>"
        if self.answer1!='0':
            self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*(len(self.answer2)/2)+self.answer1+"&nbsp;"*(len(self.answer2)/2)+"</u><br>"+"&nbsp;"*(len(self.answer1)/2)+self.answer2+"</td>"
        self.answer_text = self.answer_text + "<td>&nbsp;"+unit+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary-Grade-4/Fractions/Fractions-Word-Problems-Grade-4#WP2' target='_blank'><u>Fractions: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name =  random.choice(PersonName.BoyName)
        
        self.denominator1 = random.choice([2,3,4,5,6,7])
        self.numerator1 = randint(1,self.denominator1-1)
        self.gcf1 = LcmGcf.LcmGcf().find_gcf(self.denominator1, self.numerator1)
        self.denominator1 = self.denominator1 / self.gcf1
        self.numerator1 = self.numerator1 / self.gcf1

        self.number = randint(2,6)
      

        
        self.problem = self.name+" made some lemonade. He gave "+str(self.number)+" litres to his sister and "       
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>kept the rest for himself. If he kept&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*(len(str(self.denominator1))/2)+str(self.numerator1)+"&nbsp;"*(len(str(self.denominator1))/2)+"</u><br>"+"&nbsp;"*(len(str(self.numerator1))/2)+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of the lemonade for himself,</td></tr>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "how many litres of lemonade did he make?"
                       
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        
        self.AnswerDenominator = self.denominator1 - self.numerator1
        self.AnswerNumerator = self.denominator1 * self.number
        self.AnswerGcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)
        
        self.AnswerDenominator = self.AnswerDenominator / self.AnswerGcf
        self.AnswerNumerator = self.AnswerNumerator / self.AnswerGcf
        
        div,mod = divmod(self.AnswerNumerator,self.AnswerDenominator)
        '''can't have answer as list (can't store list in datastore for tests module) so creating a string'''
        self.answer = str(div)+","+str(mod)+","+str(self.AnswerDenominator)
        
        self.CheckAnswerType = 1

        self.unit = "litres"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FractionAnswer':"Y"}            

    def ExplainType3(self,problem,answer,unit):
        self.answer_text = "<table id='fractionTable' class='FractionsTable'>" 
        self.answer_text = self.answer_text + "<tr><td>The correct answer is:&nbsp;</td>"
        answer = answer.split(",")
        self.answer0 = answer[0]
        self.answer1 = answer[1]
        self.answer2 = answer[2]
        if self.answer0!='0':
            self.answer_text = self.answer_text + "<td>"+self.answer0+"</td>"
        if self.answer1!='0':
            self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*(len(self.answer2)/2)+self.answer1+"&nbsp;"*(len(self.answer2)/2)+"</u><br>"+"&nbsp;"*(len(self.answer1)/2)+self.answer2+"</td>"
        self.answer_text = self.answer_text + "<td>&nbsp;"+unit+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary-Grade-4/Fractions/Fractions-Word-Problems-Grade-4#WP3' target='_blank'><u>Fractions: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name =  random.choice(PersonName.GirlName)
        
        self.DenominatorLeft = randint(3,7)
        self.NumeratorLeft = randint(1,self.DenominatorLeft-1)
        
        self.GcfLeft = LcmGcf.LcmGcf().find_gcf(self.DenominatorLeft, self.NumeratorLeft)
        self.DenominatorLeft = self.DenominatorLeft / self.GcfLeft
        self.NumeratorLeft = self.NumeratorLeft / self.GcfLeft
        
        self.TotalNumerator = self.DenominatorLeft
        self.TotalDenominator = self.NumeratorLeft
        
        self.number = randint(1,5)
        
        self.TotalNumerator = self.TotalNumerator * self.number
        
        self.mixed,self.TotalNumerator = divmod(self.TotalNumerator,self.TotalDenominator)
        
        self.NumeratorSold = self.DenominatorLeft - self.NumeratorLeft
        self.DenominatorSold = self.DenominatorLeft
 
        self.GcfSold = LcmGcf.LcmGcf().find_gcf(self.DenominatorSold, self.NumeratorSold)
        self.DenominatorSold = self.DenominatorSold / self.GcfSold
        self.NumeratorSold = self.NumeratorSold / self.GcfSold       
        
                
        self.problem = "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<td>"+self.name+" had&nbsp;</td>"
        self.problem = self.problem + "<td>"+str(self.mixed)+"</td>"
        if self.TotalNumerator!=0:            
            self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*(len(str(self.TotalDenominator))/2)+str(self.TotalNumerator)+"&nbsp;"*(len(str(self.TotalDenominator))/2)+"</u><br>"+"&nbsp;"*(len(str(self.TotalNumerator))/2)+str(self.TotalDenominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp;kg of peanuts. She sold&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*(len(str(self.DenominatorSold))/2)+str(self.NumeratorSold)+"&nbsp;"*(len(str(self.DenominatorSold))/2)+"</u><br>"+"&nbsp;"*(len(str(self.NumeratorSold))/2)+str(self.DenominatorSold)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of them.</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "Find the mass of peanuts she had left."       
        
        self.answer = self.number
        
        self.CheckAnswerType = 2

        self.unit = "kg"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                }            

    def ExplainType4(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        
        self.solution_text = "For detailed explanation refer to Word Problem 4 at <a href='/Learn/Primary-Grade-4/Fractions/Fractions-Word-Problems-Grade-4#WP4' target='_blank'><u>Fractions: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType5(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name =  random.choice(PersonName.BoyName)
        
        self.numbers = [[2,3,6],[2,5,10],[3,4,12]]
        
        self.numbers = random.choice(self.numbers)
        self.denominator1 = self.numbers[0]
        self.denominator2 = self.numbers[1]        
        self.number = randint(5,10) * self.numbers[2]
        
        self.problem = "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<td>"+self.name+" has "+str(self.number)+" coins.&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*(len(str(self.denominator1))/2)+str(1)+"&nbsp;"*(len(str(self.denominator1))/2)+"</u><br>"+"&nbsp;"*(len(str(1))/2)+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of them are Singapore coins,&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*(len(str(self.denominator2))/2)+str(1)+"&nbsp;"*(len(str(self.denominator2))/2)+"</u><br>"+"&nbsp;"*(len(str(1))/2)+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of them are US</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "coins and the rest are Indian coins. How many Indian coins does he have?"       
        
        self.answer = self.number - self.number/self.denominator1 - self.number/self.denominator2
        
        self.CheckAnswerType = 2

        self.unit = "coins"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                }            

    def ExplainType5(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        
        self.solution_text = "For detailed explanation refer to Word Problem 5 at <a href='/Learn/Primary-Grade-4/Fractions/Fractions-Word-Problems-Grade-4#WP5' target='_blank'><u>Fractions: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType6(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name =  random.choice(PersonName.GirlName)
        
        self.denominator1 = random.choice([2,3,4,5,6,7,8])
        self.numerator1 = randint(1,self.denominator1-1)
        self.gcf1 = LcmGcf.LcmGcf().find_gcf(self.denominator1, self.numerator1)
        
        self.denominator1 = self.denominator1 / self.gcf1
        self.numerator1 = self.numerator1 / self.gcf1
        
        self.number = randint(10,20)
        
        self.LengthUsed = self.numerator1 * self.number
        
        self.problem = "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<td>"+self.name+" had a piece of ribbon. She used&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*(len(str(self.denominator1))/2)+str(self.numerator1)+"&nbsp;"*(len(str(self.denominator1))/2)+"</u><br>"+"&nbsp;"*(len(str(self.numerator1))/2)+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of it to make bows.</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "She used "+str(self.LengthUsed)+" cm of the ribbon to make bows. Find the length of the ribbon she had at first."       
        
        self.answer = self.LengthUsed * self.denominator1 / self.numerator1
        
        self.CheckAnswerType = 2

        self.unit = "cm"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                }            

    def ExplainType6(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        
        self.solution_text = "For detailed explanation refer to Word Problem 6 at <a href='/Learn/Primary-Grade-4/Fractions/Fractions-Word-Problems-Grade-4#WP6' target='_blank'><u>Fractions: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType7a(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name =  random.choice(PersonName.BoyName)
        
        self.numbers = [[2,3,6*randint(10,20)],
                        [2,4,8*randint(10,16)],
                        [2,5,10*randint(8,14)],
                        [2,6,12*randint(7,10)],
                        [3,4,12*randint(7,12)],
                        [3,5,15*randint(6,10)],
                        [3,6,18*randint(5,7)],
                        [4,5,20*randint(4,8)],
                        [4,6,24*randint(4,8)],
                        [4,7,28*randint(4,6)],
                        [5,6,30*randint(3,5)],
                        [5,7,35*randint(2,4)]
                        ]
        
        self.numbers = random.choice(self.numbers)
        
        self.SpentDenominator = self.numbers[0]
        self.SpentNumerator = randint(1,self.SpentDenominator-1)
        self.SpentGcf = LcmGcf.LcmGcf().find_gcf(self.SpentDenominator,self.SpentNumerator)
        
        self.SpentDenominator = self.SpentDenominator / self.SpentGcf
        self.SpentNumerator = self.SpentNumerator / self.SpentGcf

        self.LeftDenominator = self.numbers[1]
        self.LeftNumerator = randint(1,self.LeftDenominator-1)
        self.LeftGcf = LcmGcf.LcmGcf().find_gcf(self.LeftDenominator,self.LeftNumerator)
        
        self.LeftDenominator = self.LeftDenominator / self.LeftGcf
        self.LeftNumerator = self.LeftNumerator / self.LeftGcf
        
        self.Total = self.numbers[2]
        
        self.problem = self.name + " received $"+str(self.Total)+" of pocket money."
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<td>He spent&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*(len(str(self.SpentDenominator))/2)+str(self.SpentNumerator)+"&nbsp;"*(len(str(self.SpentDenominator))/2)+"</u><br>"+"&nbsp;"*(len(str(self.SpentNumerator))/2)+str(self.SpentDenominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of it on a pair of shoes and&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*(len(str(self.LeftDenominator))/2)+str(self.LeftNumerator)+"&nbsp;"*(len(str(self.LeftDenominator))/2)+"</u><br>"+"&nbsp;"*(len(str(self.LeftNumerator))/2)+str(self.LeftDenominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of the remaining on a watch.</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "How much did the shoes cost?"       
        
        self.answer = self.Total * self.SpentNumerator / self.SpentDenominator
        
        self.CheckAnswerType = 2

        self.unit = ""
        self.template = "EnterTypeProblems.html"
        self.dollar_unit = "$"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7a",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'dollar_unit':self.dollar_unit
                }            
        
    def GenerateProblemType7b(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name =  random.choice(PersonName.BoyName)
        
        self.numbers = [[2,3,6*randint(10,20)],
                        [2,4,8*randint(10,16)],
                        [2,5,10*randint(8,14)],
                        [2,6,12*randint(7,10)],
                        [3,4,12*randint(7,12)],
                        [3,5,15*randint(6,10)],
                        [3,6,18*randint(5,7)],
                        [4,5,20*randint(4,8)],
                        [4,6,24*randint(4,8)],
                        [4,7,28*randint(4,6)],
                        [5,6,30*randint(3,5)],
                        [5,7,35*randint(2,4)]
                        ]
        
        self.numbers = random.choice(self.numbers)
        
        self.SpentDenominator = self.numbers[0]
        self.SpentNumerator = randint(1,self.SpentDenominator-1)
        self.SpentGcf = LcmGcf.LcmGcf().find_gcf(self.SpentDenominator,self.SpentNumerator)
        
        self.SpentDenominator = self.SpentDenominator / self.SpentGcf
        self.SpentNumerator = self.SpentNumerator / self.SpentGcf

        self.LeftDenominator = self.numbers[1]
        self.LeftNumerator = randint(1,self.LeftDenominator-1)
        self.LeftGcf = LcmGcf.LcmGcf().find_gcf(self.LeftDenominator,self.LeftNumerator)
        
        self.LeftDenominator = self.LeftDenominator / self.LeftGcf
        self.LeftNumerator = self.LeftNumerator / self.LeftGcf
        
        self.Total = self.numbers[2]
        
        self.problem = self.name + " received $"+str(self.Total)+" of pocket money."
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<td>He spent&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*(len(str(self.SpentDenominator))/2)+str(self.SpentNumerator)+"&nbsp;"*(len(str(self.SpentDenominator))/2)+"</u><br>"+"&nbsp;"*(len(str(self.SpentNumerator))/2)+str(self.SpentDenominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of it on a pair of shoes and&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*(len(str(self.LeftDenominator))/2)+str(self.LeftNumerator)+"&nbsp;"*(len(str(self.LeftDenominator))/2)+"</u><br>"+"&nbsp;"*(len(str(self.LeftNumerator))/2)+str(self.LeftDenominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of the remaining on a watch.</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "Find the sum of money he had left in the end."       
        
        self.answer = ((self.Total - self.Total * self.SpentNumerator / self.SpentDenominator) * (self.LeftDenominator - self.LeftNumerator)) / self.LeftDenominator
        
        self.CheckAnswerType = 2

        self.unit = ""
        self.template = "EnterTypeProblems.html"
        self.dollar_unit = "$"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7b",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'dollar_unit':self.dollar_unit
                }            
        
    def GenerateProblemType7c(self):
        '''e.g: '''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name =  random.choice(PersonName.BoyName)
        
        self.numbers = [[2,3,6*randint(10,20)],
                        [2,4,8*randint(10,16)],
                        [2,5,10*randint(8,14)],
                        [2,6,12*randint(7,10)],
                        [3,4,12*randint(7,12)],
                        [3,5,15*randint(6,10)],
                        [3,6,18*randint(5,7)],
                        [4,5,20*randint(4,8)],
                        [4,6,24*randint(4,8)],
                        [4,7,28*randint(4,6)],
                        [5,6,30*randint(3,5)],
                        [5,7,35*randint(2,4)]
                        ]
        
        self.numbers = random.choice(self.numbers)
        
        self.SpentDenominator = self.numbers[0]
        self.SpentNumerator = randint(1,self.SpentDenominator-1)
        self.SpentGcf = LcmGcf.LcmGcf().find_gcf(self.SpentDenominator,self.SpentNumerator)
        
        self.SpentDenominator = self.SpentDenominator / self.SpentGcf
        self.SpentNumerator = self.SpentNumerator / self.SpentGcf

        self.LeftDenominator = self.numbers[1]
        self.LeftNumerator = randint(1,self.LeftDenominator-1)
        self.LeftGcf = LcmGcf.LcmGcf().find_gcf(self.LeftDenominator,self.LeftNumerator)
        
        self.LeftDenominator = self.LeftDenominator / self.LeftGcf
        self.LeftNumerator = self.LeftNumerator / self.LeftGcf
        
        self.Total = self.numbers[2]
        
        self.problem = self.name + " received $"+str(self.Total)+" of pocket money."
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<td>He spent&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*(len(str(self.SpentDenominator))/2)+str(self.SpentNumerator)+"&nbsp;"*(len(str(self.SpentDenominator))/2)+"</u><br>"+"&nbsp;"*(len(str(self.SpentNumerator))/2)+str(self.SpentDenominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of it on a pair of shoes and&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>"+"&nbsp;"*(len(str(self.LeftDenominator))/2)+str(self.LeftNumerator)+"&nbsp;"*(len(str(self.LeftDenominator))/2)+"</u><br>"+"&nbsp;"*(len(str(self.LeftNumerator))/2)+str(self.LeftDenominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of the remaining on a watch.</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "Find the sum of money he had left in the end."       

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
                
        self.AnswerNumerator = ((self.Total - self.Total * self.SpentNumerator / self.SpentDenominator) * (self.LeftDenominator - self.LeftNumerator)) / self.LeftDenominator
        self.AnswerDenominator = self.Total
        
        self.AnswerGcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator,self.AnswerDenominator)
        self.AnswerNumerator = self.AnswerNumerator / self.AnswerGcf
        self.AnswerDenominator = self.AnswerDenominator / self.AnswerGcf
        
        self.mixed, self.AnswerNumerator = divmod(self.AnswerNumerator,self.AnswerDenominator)
        
        self.answer = str(self.mixed)+","+str(self.AnswerNumerator)+","+str(self.AnswerDenominator)
        
        self.CheckAnswerType = 1

        self.unit = ""
        self.template = "EnterTypeProblems.html"
        self.dollar_unit = ""

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7c(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7c",'CheckAnswerType':self.CheckAnswerType,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'FractionAnswer':"Y"
                }            

    def ExplainType7(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar_unit+str(answer)+" "+unit
        
        self.solution_text = "For detailed explanation refer to Word Problem 7 at <a href='/Learn/Primary-Grade-4/Fractions/Fractions-Word-Problems-Grade-4#WP7' target='_blank'><u>Fractions: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def ExplainType7c(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<table id='fractionTable' class='FractionsTable'>" 
        self.answer_text = self.answer_text + "<tr><td>The correct answer is:&nbsp;</td>"
        answer = answer.split(",")
        self.answer0 = answer[0]
        self.answer1 = answer[1]
        self.answer2 = answer[2]
        if self.answer0!='0':
            self.answer_text = self.answer_text + "<td>"+self.answer0+"</td>"
        if self.answer1!='0':
            self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*(len(self.answer2)/2)+self.answer1+"&nbsp;"*(len(self.answer2)/2)+"</u><br>"+"&nbsp;"*(len(self.answer1)/2)+self.answer2+"</td>"
        self.answer_text = self.answer_text + "<td>&nbsp;"+unit+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
                
        self.solution_text = "For detailed explanation refer to Word Problem 7 at <a href='/Learn/Primary-Grade-4/Fractions/Fractions-Word-Problems-Grade-4#WP7' target='_blank'><u>Fractions: Word Problems (Grade 4)</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
                if " " in str(InputAnswer):             
                    try:
                        InputMixed = int(str(InputAnswer).partition(" ")[0])
                        RemainingInput = str(InputAnswer).partition(" ")[2]
                        InputDenominator = int(str(RemainingInput).partition("/")[2])
                        InputNumerator = int(str(RemainingInput).partition("/")[0])
                        InputGCF = LcmGcf.LcmGcf().find_gcf(InputNumerator,InputDenominator)
                        InputAnswer = str(InputMixed)+","+str(InputNumerator/InputGCF)+","+str(InputDenominator/InputGCF)
                        logging.info(answer)
                        logging.info(InputAnswer)
                    except ValueError:
                        return False 
                elif "/" in str(InputAnswer):
                    try:            
                        InputNumerator = int(str(InputAnswer).partition("/")[0])
                        InputDenominator = int(str(InputAnswer).partition("/")[2])
                        InputGCF = LcmGcf.LcmGcf().find_gcf(InputNumerator,InputDenominator)
                        div,mod = divmod(InputNumerator/InputGCF,InputDenominator/InputGCF)
                        InputAnswer = str(div)+","+str(mod)+","+str(InputDenominator/InputGCF)
                        logging.info(answer)
                        logging.info(InputAnswer)                        
                    except ValueError:
                        return False                
                else:
                    try:
                        InputAnswer = str(InputAnswer)+",0,1"
                    except ValueError:
                        return False
                return InputAnswer == answer
        elif CheckAnswer==2:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False