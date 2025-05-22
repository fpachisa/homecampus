'''
Created on Feb 04, 2014
Module: P3FRComparingOrdering
Generates the Comparing and Ordering Fractions questions for Primary 3

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
from decimal import Decimal
from Utils import LcmGcf

class P3FRComparingOrdering:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemTypeMCQ2",],3:["ProblemTypeMCQ3",],4:["ProblemTypeMCQ4",],
                            5:["ProblemType5",],6:["ProblemTypeMCQ6",],7:["ProblemTypeMCQ7",],8:["ProblemTypeMCQ8",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemTypeMCQ2(),],3:[self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemTypeMCQ4(),],5:[self.GenerateProblemType5(),],6:[self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemTypeMCQ7(),],8:[self.GenerateProblemTypeMCQ8(),],
                                    }
        
        #Creating one more problem type so it creates a list and not a list of lists
        self.ProblemTypes = []
        
        for i in self.ProblemType.values():
            for k in i:
                self.ProblemTypes.append(k)
                
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(self.GenerateProblemType[1])
        else:
            if LastProblemID in self.ProblemTypes:
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if LastProblemID in v][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return random.choice(self.GenerateProblemType[NextProblemKey])
            else:
                return random.choice(self.GenerateProblemType[1])
        #return self.GenerateProblemTypeMCQ2()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),
                            "ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominator = randint(3,6)
        self.numerator1 = randint(1,self.denominator-1)
        self.numerator2 = randint(1,self.denominator-1)
        while self.numerator1 == self.numerator2:
            self.numerator2 = randint(1,self.denominator-1)

        self.problem = self.CreateFractionStatement("Which is smaller:&nbsp;", self.numerator1, self.denominator, "or")
        self.problem = self.problem + self.CreateFractionStatement("&nbsp;", self.numerator2, self.denominator, "?")
        
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'

        self.AnswerDenominator = self.denominator
        if self.numerator1 < self.numerator2:
            self.AnswerNumerator = self.numerator1
        else:
            self.AnswerNumerator = self.numerator2
            
        self.answer = str(self.AnswerNumerator)+"/"+str(self.AnswerDenominator)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.unit,self.dollar_unit,self.numerator1,self.numerator2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,numerator,denominator,unit,dollar_unit,numerator1,numerator2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(numerator, denominator))
       
        self.solution_text = "<font class='ExplanationFont'>"
        
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">The fractions&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;and&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;have a common denominator.</div><br><br>'
        
        self.solution_text = self.solution_text + "The smaller fraction is the one with the smaller numerator.<br><br>"

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So,&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is the smaller fraction.</div>'
        
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ2(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.numerator1 = randint(1,6)
        self.numerator2 = self.numerator1
        self.denominator1 = randint(self.numerator1+1,10)
        self.denominator2 = randint(self.numerator1+1,10)
        if self.denominator1 == self.denominator2:
            self.denominator2 = self.denominator1 + 1
            
        self.flag = randint(1,3)
        self.multiplier = 0
        self.multiplier1 = (LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2))/self.denominator1
        self.multiplier2 = (LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2))/self.denominator2
        '''for 1 in 3 times, the fractions will be same'''
        if self.flag == 1:
            self.denominator1 = randint(3,6)
            self.numerator1 = randint(1,self.denominator1-1)
            self.multiplier = randint(3,6)
            self.numerator2 = self.numerator1 * self.multiplier
            self.denominator2 = self.denominator1 * self.multiplier

        self.problem = self.CreateFractionStatement("Choose the correct option to fill in the blank -- ", self.numerator1, self.denominator1, "&nbsp;is _________&nbsp;")
        self.problem = self.problem + self.CreateFractionStatement("", self.numerator2, self.denominator2, ": ") 
        
        if self.flag == 1:
            self.answer = "equal to"
        else:
            if self.denominator1 > self.denominator2:
                self.answer = "less than"
                self.flag = 2
            else:
                self.answer = "greater than"
                self.flag = 3
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.flag,self.multiplier,self.multiplier1,self.multiplier2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':"equal to",'value1':"equal to",'answer2':"less than",'value2':"less than",
                'answer3':"greater than",'value3':"greater than",}

    def ExplainType2(self,problem,answer,numerator1,denominator1,numerator2,denominator2,flag,multiplier,multiplier1,multiplier2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + 'To compare the two fractions, we must first express both the fractions with the same denominator by making a list of equivalent fractions.<br><br>'
        if flag==1:
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 1:&nbsp;</div>'
            for i in range (multiplier-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier)+'</p></div><br><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 2:&nbsp;</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div><br><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">From the above we see that&nbsp;</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is equal to&nbsp;</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div>'
        else:
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 1:&nbsp;</div>'
            for i in range (multiplier1-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div><br><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 2:&nbsp;</div>'
            for i in range (multiplier2-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div><br><br>'
                
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is %s&nbsp;</div>'%(answer)
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So,&nbsp;</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is %s&nbsp;</div>'%(answer)
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div>'
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ3(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.BoyName,1)+random.sample(PersonName.GirlName,2)
        self.item = random.choice(['pizza','cake','bar of chocolate'])
        self.denominators = random.sample([3,4,6,8],3)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.denominator3 = self.denominators[2]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        self.numerator3 = randint(1,self.denominator3-1)
        
        
        self.problem = "%s, %s and %s each had a similar %s.<br />" % (self.names[0],self.names[1],self.names[2],self.item)
        #Part-1
        stmt1 = self.names[0] + " ate"
        stmt2 = "of his " + self.item + ".<br />"
        self.problem = self.problem + self.CreateFractionStatement(stmt1, self.numerator1, self.denominator1, stmt2, enclose=True)
        
        #Part-2
        stmt1 = stmt2 = ""
        stmt1 = self.names[1] + " ate"
        stmt2 = "&nbsp;of her " + self.item + "."
        self.problem = self.problem + self.CreateFractionStatement(stmt1, self.numerator2, self.denominator2, stmt2, enclose=True)
        
        #Part-3
        stmt1 = stmt2 = ""
        stmt1 = self.names[2] + " ate"
        stmt2 = "&nbsp;of her " + self.item + "."
        self.problem = self.problem + self.CreateFractionStatement(stmt1, self.numerator3, self.denominator3, stmt2, enclose=True)
        
        self.multiplier1 = 1
        self.multiplier2 = 1
        self.multiplier3 = 1
        self.flag = randint(1,3)
        
        condition = ""
        
        if self.flag == 1:
            self.LCM = (LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator3))
            self.multiplier1 = self.LCM/self.denominator1
            self.multiplier3 = self.LCM/self.denominator3
            condition = "%s ate a bigger portion than %s."%(self.names[0],self.names[2])
            if Decimal(self.numerator1)/Decimal(self.denominator1) > Decimal(self.numerator3)/Decimal(self.denominator3):
                self.answer = "True"
            else:
                self.answer = "False"
        elif self.flag == 2:
            self.LCM = (LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2))
            self.multiplier1 = self.LCM/self.denominator1
            self.multiplier2 = self.LCM/self.denominator2
            condition = "%s ate a smaller portion than %s."%(self.names[0],self.names[1])
            if Decimal(self.numerator1)/Decimal(self.denominator1) < Decimal(self.numerator2)/Decimal(self.denominator2):
                self.answer = "True"
            else:
                self.answer = "False"            
        else:
            self.LCM = (LcmGcf.LcmGcf().find_lcm(self.denominator2, self.denominator3))
            self.multiplier2 = self.LCM/self.denominator2
            self.multiplier3 = self.LCM/self.denominator3
            condition = "%s ate a smaller portion than %s."%(self.names[1],self.names[2])
            if Decimal(self.numerator2)/Decimal(self.denominator2) < Decimal(self.numerator3)/Decimal(self.denominator3):
                self.answer = "True"
            else:
                self.answer = "False"
        
        #Add condition to the problem statement               
        self.problem = self.problem + "<br /><br />Is the following statement true or false?<br />"
        self.problem = self.problem + condition
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.names,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.numerator3,self.denominator3,self.multiplier1,self.multiplier2,self.multiplier3,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':"True",'value1':"True",'answer2':"False",'value2':"False",
                }

    def ExplainType3(self,problem,answer,names,numerator1,denominator1,numerator2,denominator2,numerator3,denominator3,multiplier1,multiplier2,multiplier3,flag):
        self.answer_text = "<br>The correct answer is:<br>%s"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + 'To compare the fractions, we must first express the fractions with the same denominator by making a list of equivalent fractions.<br><br>'
            
        if flag == 1:
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;&nbsp;&nbsp;</div>'%(names[0])
            for i in range (multiplier1-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div><br><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;&nbsp;&nbsp;</div>'%(names[2])
            for i in range (multiplier3-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3*multiplier3)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3*multiplier3)+'</p></div><br><br>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
            if numerator1*multiplier1>numerator3*multiplier3:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is greater than&nbsp;</div>'
            elif numerator1*multiplier1<numerator3*multiplier3:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is less than&nbsp;</div>'
            else:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;(%s) is equal to&nbsp;</div>'%(names[0])
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3*multiplier3)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3*multiplier3)+'</p></div>'
            if numerator1*multiplier1==numerator3*multiplier3:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">(%s).</div><br>'%(names[2])
            else:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'
            self.solution_text = self.solution_text + "<br>So, the statement, %s ate a bigger portion than %s, is %s."%(names[0],names[2],answer)
        elif flag == 2:
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;&nbsp;&nbsp;</div>'%(names[0])
            for i in range (multiplier1-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div><br><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;&nbsp;&nbsp;</div>'%(names[1])
            for i in range (multiplier2-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div><br><br>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
            if numerator1*multiplier1>numerator2*multiplier2:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is less than&nbsp;</div>'
            elif numerator1*multiplier1<numerator2*multiplier2:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is greater than&nbsp;</div>'
            else:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;(%s) is equal to&nbsp;</div>'%(names[0])
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
            if numerator1*multiplier1==numerator2*multiplier2:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">(%s).</div><br>'%(names[1])
            else:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'
            self.solution_text = self.solution_text + "<br>So, the statement, %s ate a smaller portion than %s, is %s."%(names[0],names[1],answer)
        else:
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;&nbsp;&nbsp;</div>'%(names[1])
            for i in range (multiplier2-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div><br><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;&nbsp;&nbsp;</div>'%(names[2])
            for i in range (multiplier3-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3*multiplier3)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3*multiplier3)+'</p></div><br><br>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
            if numerator2*multiplier2>numerator3*multiplier3:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is less than&nbsp;</div>'
            elif numerator2*multiplier2<numerator3*multiplier3:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is greater than&nbsp;</div>'
            else:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;(%s) is equal to&nbsp;</div>'%(names[1])
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3*multiplier3)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3*multiplier3)+'</p></div>'
            if numerator2*multiplier2==numerator3*multiplier3:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">(%s).</div><br>'%(names[2])
            else:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'
            
            self.solution_text = self.solution_text + "<br>So, the statement, %s ate a smaller portion than %s, is %s."%(names[1],names[2],answer)
        
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ4(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
       
        self.images = [['P3FR_ComparingOrdering_PT4a',"True",5,'greater'],['P3FR_ComparingOrdering_PT4b',"False",3,'less'],
                       ['P3FR_ComparingOrdering_PT4c',"True",5,'greater'],
                       ]
        self.ProblemImage = random.choice(self.images)
        
        self.problem = self.CreateFractionStatement("Study the following figure. Is the shaded fraction greater than", 1, 2, "?")
        self.problem = self.problem + "<br><br><img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.ProblemImage)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':"True",'value1':"True",'answer2':"False",'value2':"False",
                }

    def ExplainType4(self,problem,answer,images):
        self.answer_text = "<br>The correct answer is:<br>%s"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">The shaded portion of the figure represents the fraction&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(images[2])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>8</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">To compare the fractions, we must first list the equivalent fractions of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">1<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>2</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'

        for i in range (2):
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(1*(i+1))+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(2*(i+1))+'</p></div>'
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">4<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>8</p></div><br><br>'

        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(images[2])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>8</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is %s than&nbsp;</div>'%(images[3])
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">4<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>8</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">.</div><br>'
        
        self.solution_text = self.solution_text + "<br>So, the statement is %s."%(answer)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominators = random.choice([[3,random.choice([4,5,6,7,8,9,12])],[4,random.choice([5,6,7,8,10,12])],
                                           [5,random.choice([6,7,8,10])],[6,random.choice([8,9,10,12])]
                                           ])
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-2)
        self.numerator2 = randint(1,self.denominator2-2)
        if Decimal(self.numerator1)/Decimal(self.denominator1) == Decimal(self.numerator2)/Decimal(self.denominator2):
            self.numerator1 = self.numerator1 + 1

        self.multiplier1 = (LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2))/self.denominator1
        self.multiplier2 = (LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2))/self.denominator2

        self.problem = self.CreateFractionStatement("Which is greater:&nbsp;", self.numerator1, self.denominator1, "&nbsp;")
        self.problem = self.problem + self.CreateFractionStatement("or&nbsp;", self.numerator2, self.denominator2, "?") 
        
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'

        if Decimal(self.numerator1)/Decimal(self.denominator1) > Decimal(self.numerator2)/Decimal(self.denominator2):
            self.AnswerDenominator = self.denominator1
            self.AnswerNumerator = self.numerator1
        else:
            self.AnswerDenominator = self.denominator2
            self.AnswerNumerator = self.numerator2            
            
        self.answer = str(self.AnswerNumerator)+"/"+str(self.AnswerDenominator)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.unit,self.dollar_unit,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.multiplier1,self.multiplier2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,numerator,denominator,unit,dollar_unit,numerator1,denominator1,numerator2,denominator2,multiplier1,multiplier2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(numerator, denominator))
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + 'To compare the two fractions, we must first express the fractions using a common denominator.<br><br>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 1:&nbsp;&nbsp;&nbsp;</div>'
        for i in range (multiplier1-1):
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*(i+1))+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*(i+1))+'</p></div>'
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div><br><br>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 2:&nbsp;&nbsp;&nbsp;</div>'
        for i in range (multiplier2-1):
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*(i+1))+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*(i+1))+'</p></div>'
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div><br><br>'

        if numerator1*multiplier1>numerator2*multiplier2:
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is greater than&nbsp;</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So,&nbsp;</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is greater than&nbsp;</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        else:
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is greater than&nbsp;</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So,&nbsp;</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is greater than&nbsp;</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div>'
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ6(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
       
        self.name = random.choice(PersonName.PersonName)
        self.fractions = random.choice([[1,4,1,3,1,2,'P3FR_ComparingOrdering_PT6a','P3FR_ComparingOrdering_PT6b'],
                                        [1,4,1,2,3,4,'P3FR_ComparingOrdering_PT6c','P3FR_ComparingOrdering_PT6d'],
                                        [2,3,3,4,5,6,'P3FR_ComparingOrdering_PT6e','P3FR_ComparingOrdering_PT6f'],
                                        [1,10,2,5,5,10,'P3FR_ComparingOrdering_PT6g','P3FR_ComparingOrdering_PT6h'],
                                        [1,8,1,4,2,6,'P3FR_ComparingOrdering_PT6i','P3FR_ComparingOrdering_PT6j']
                                        ])

        self.denominator1 = self.fractions[1]
        self.denominator2 = self.fractions[3]
        self.denominator3 = self.fractions[5]
        self.numerator1 = self.fractions[0]
        self.numerator2 = self.fractions[2]
        self.numerator3 = self.fractions[4]
        
        self.JumbledFractions = [[self.numerator1,self.denominator1],[self.numerator2,self.denominator2],[self.numerator3,self.denominator3]]
        random.shuffle(self.JumbledFractions)
        
        self.denominator1 = self.JumbledFractions[0][1]
        self.numerator1 = self.JumbledFractions[0][0]
        self.denominator2 = self.JumbledFractions[1][1]
        self.numerator2 = self.JumbledFractions[1][0]
        self.denominator3 = self.JumbledFractions[2][1]
        self.numerator3 = self.JumbledFractions[2][0]
        
        self.LCM = (LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2))
        self.LCM = (LcmGcf.LcmGcf().find_lcm(self.LCM, self.denominator3))
        self.multiplier1 = self.LCM/self.denominator1
        self.multiplier2 = self.LCM/self.denominator2
        self.multiplier3 = self.LCM/self.denominator3
                
        self.problem = '%s arranges the following fractions in order, beginning with the smallest.<br><br>'%(self.name)
        
        self.problem = self.problem + "<div>"
        
        self.problem = self.problem + self.CreateFraction(self.numerator1, self.denominator1) + ", "
        self.problem = self.problem + self.CreateFraction(self.numerator2, self.denominator2) + ", "
        self.problem = self.problem + self.CreateFraction(self.numerator3, self.denominator3)
        
        self.problem = self.problem + "<br><br>Which of the following orders is correct?"
        self.problem = self.problem + "</div>"
        
        self.answer = "<img src='/images/P3ProblemImages/"+self.fractions[6]+".png'>"
        
        self.DisplayAnswer = '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(self.fractions[0])+'<br>__<br></p>'
        self.DisplayAnswer = self.DisplayAnswer + '<p style="line-height:20%;text-align:center;"><br>'+str(self.fractions[1])+'</p></div>'
        self.DisplayAnswer = self.DisplayAnswer + '<div style="width:10px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:2px;">,</div>'
        self.DisplayAnswer = self.DisplayAnswer + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(self.fractions[2])+'<br>__<br></p>'
        self.DisplayAnswer = self.DisplayAnswer + '<p style="line-height:20%;text-align:center;"><br>'+str(self.fractions[3])+'</p></div>'
        self.DisplayAnswer = self.DisplayAnswer + '<div style="width:10px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:2px;">,</div>'
        self.DisplayAnswer = self.DisplayAnswer + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(self.fractions[4])+'<br>__<br></p>'
        self.DisplayAnswer = self.DisplayAnswer + '<p style="line-height:20%;text-align:center;"><br>'+str(self.fractions[5])+'</p></div>'
        
        self.answers = ["<img src='/images/P3ProblemImages/"+self.fractions[6]+".png'>","<img src='/images/P3ProblemImages/"+self.fractions[7]+".png'>"]
        random.shuffle(self.answers)
        
        self.answer1 = self.answers[0]
        self.answer2 = self.answers[1]
        self.value1 = self.answers[0]
        self.value2 = self.answers[1]
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.DisplayAnswer,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.numerator3,self.denominator3,self.multiplier1,self.multiplier2,self.multiplier3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2,
                }

    def ExplainType6(self,problem,answer,numerator1,denominator1,numerator2,denominator2,numerator3,denominator3,multiplier1,multiplier2,multiplier3):
        self.answer_text = "<br>The correct answer is:<br>%s"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + 'To compare the fractions, we must first express them using a common denominator.<br><br>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 1:&nbsp;&nbsp;&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
        if multiplier1>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
        self.solution_text = self.solution_text + "<br><br>"

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 2:&nbsp;&nbsp;&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        if multiplier2>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
        self.solution_text = self.solution_text + "<br><br>"

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 3:&nbsp;&nbsp;&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3)+'</p></div>'
        if multiplier3>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3*multiplier3)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3*multiplier3)+'</p></div>'
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + "The fraction with the smallest numerator is the smallest fraction while the fraction with the biggest numerator is the biggest fraction.<br><br>So, beginning with the smallest, the fractions should be arranged in the following order:<blockquote>%s</blockquote>"%(answer)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ7(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominator1 = randint(5,10)
        self.denominator2 = randint(5,10)
        self.numerator1 = randint(1,self.denominator1-2)
        self.numerator2 = randint(1,self.denominator2-2)
        
        if self.numerator1 == self.numerator2 and self.denominator1 == self.denominator2:
            self.numerator1 = self.numerator1 + 1

        self.multiplier = 1
        self.multiplier1 = (LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2))/self.denominator1
        self.multiplier2 = (LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2))/self.denominator2

        self.problem = "Choose the correct option to fill in the blank.<br><br>"
        self.problem = self.problem + self.CreateFractionStatement("", self.numerator1, self.denominator1, "&nbsp;is &nbsp;_________&nbsp;")
        self.problem = self.problem + self.CreateFraction(self.numerator1, self.denominator2)
        self.flag = 1
        if Decimal(self.numerator1)/Decimal(self.denominator1)==Decimal(self.numerator2)/Decimal(self.denominator2):
            self.answer = "equal to"
            self.flag = 1
            self.multiplier = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        elif Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2):
            self.answer = "greater than"
            self.flag = 2
        else:
            self.answer = "less than"
            self.flag = 3
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.flag,self.multiplier,self.multiplier1,self.multiplier2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':"equal to",'value1':"equal to",'answer2':"less than",'value2':"less than",
                'answer3':"greater than",'value3':"greater than",}

    def ExplainType7(self,problem,answer,numerator1,denominator1,numerator2,denominator2,flag,multiplier,multiplier1,multiplier2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"
        if denominator1!=denominator2:
            self.solution_text = self.solution_text + 'To compare the fractions, we must first express them using a common denominator.<br><br>'
        if flag==1:
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 1:&nbsp;&nbsp;&nbsp;</div>'
            multi = multiplier/denominator1
            for i in range (multi-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            if multi==0:
                multi=1
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multi)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multi)+'</p></div><br><br>'
                
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 2:&nbsp;&nbsp;&nbsp;</div>'
            multi = multiplier/denominator2
            for i in range (multi-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            if multi==0:
                multi=1
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multi)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multi)+'</p></div><br><br>'

            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">From the above we see that&nbsp;</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is equal to&nbsp;</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div>'
        else:
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 1:&nbsp;&nbsp;&nbsp;</div>'
            for i in range (multiplier1-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div><br><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 2:&nbsp;&nbsp;&nbsp;</div>'
            for i in range (multiplier2-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div><br><br>'
                
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is %s&nbsp;</div>'%(answer)
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'
            if denominator1!=denominator2:
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So,&nbsp;</div>'
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is %s&nbsp;</div>'%(answer)
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div>'
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ8(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
       
        self.names = random.sample(PersonName.AuntyName,1)+random.sample(PersonName.PersonName,2)
        self.denominator1 = randint(3,6)
        self.numerator1 = randint(1,self.denominator1-1)
        self.denominator2 = randint(3,6)
        self.numerator2 = randint(1,self.denominator2-1)
        
        if Decimal(self.numerator1)/Decimal(self.denominator1)==Decimal(self.numerator2)/Decimal(self.denominator2):
            self.denominator2 = self.denominator1 + 1
        
        self.multiplier1 = (LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2))/self.denominator1
        self.multiplier2 = (LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2))/self.denominator2
        
        self.problem = '%s had 2 ribbons of the same length.<br><br>'%(self.names[0])
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">She cut</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:bottom;margin-left:-5px;"><p style="line-height:20%;text-align:center;color:#2B7657;">'+str(self.numerator1)+'<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:#2B7657;">'+str(self.denominator1)+'<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">of one of the ribbons for %s and</div>'%(self.names[1])
        self.problem = self.problem + '<div style="display:inline-block;"><div style="width:40px;display:inline-block;vertical-align:bottom;margin-left:-5px;"><p style="line-height:20%;text-align:center;color:#2B7657;">'+str(self.numerator2)+'<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:#2B7657;">'+str(self.denominator2)+'<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">of the other ribbon for %s.</div></div>'%(self.names[2])      
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = self.problem + "<br><br>Who got the bigger piece?"
            if Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2):
                self.answer = self.names[1]
            else:
                self.answer = self.names[2]
        else:
            self.problem = self.problem + "<br><br>Who got the smaller piece?"
            if Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2):
                self.answer = self.names[2]
            else:
                self.answer = self.names[1]            
       
        
        self.answer1 = self.names[1]
        self.answer2 = self.names[2]
        self.value1 = self.answer1
        self.value2 = self.answer2
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.multiplier1,self.multiplier2,self.names,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2,
                }

    def ExplainType8(self,problem,answer,numerator1,denominator1,numerator2,denominator2,multiplier1,multiplier2,names,flag):
        self.answer_text = "<br>The correct answer is:<br>%s"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"
        if denominator1!=denominator2:
            self.solution_text = self.solution_text + 'To compare the two fractions, we must first express the fractions using a common denominator.<br><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;&nbsp;&nbsp;</div>'%(names[1])
            for i in range (multiplier1-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div><br><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;&nbsp;&nbsp;</div>'%(names[2])
            for i in range (multiplier2-1):
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*(i+1))+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*(i+1))+'</p></div>'
                self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div><br><br>'

        if flag==1:
            if numerator1*multiplier1>numerator2*multiplier2:
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is greater than&nbsp;</div>'
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'
            else:
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is greater than&nbsp;</div>'
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So, %s got the bigger piece.</div>'%(answer)
        else:
            if numerator1*multiplier1>numerator2*multiplier2:
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is less than&nbsp;</div>'
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'
            else:
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is less than&nbsp;</div>'
                self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
                self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
                self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So, %s got the smaller piece.</div>'%(answer)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def CreateFraction(self,numerator,denominator,colorCode=""):
        #fraction = ""
        #fraction = fraction + '<div style="width:40px;display:inline-block;"><p style="line-height:20%;text-align:center;color:#'+colorCode+';">'+str(numerator)+'<br>__<br></p>'
        #fraction = fraction + '<p style="line-height:20%;text-align:center;color:#'+colorCode+';">'+str(denominator)+'</p></div>'
        
        fraction = ""
        fraction = fraction + "<table style='vertical-align: bottom;display:inline-block;padding:0 6px;line-height: 15px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>" + str(numerator) + "</td></tr> <tr><td>" + str(denominator) + "</td></tr></table>"
        
        return fraction
    
    def CreateFractionStatement(self,statement1,numerator,denominator,statement2, enclose=False, colorCode=""):
        #fraction = '<div style="display:inline-block;vertical-align:top;margin-top:10px;">'+statement1+' </div>'
        #fraction = fraction + '<div style="width:40px;display:inline-block;vertical-align:bottom;margin-left:-5px;"><p style="line-height:20%;text-align:center;color:#'+colorCode+';">'+str(numerator)+'<br>__<br></p>'
        #fraction = fraction + '<p style="line-height:20%;text-align:center;color:#'+colorCode+';">'+str(denominator)+'<br></p></div>'
        #fraction = fraction + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">'+statement2+'</div>'
        fraction = ""
        if enclose:
            fraction = fraction + "<div>"
        
        fraction = fraction + "<p style='margin: 0;display:inline-block;line-height: 2;'>" + statement1 + "</p>" + self.CreateFraction(numerator, denominator, colorCode)+ "<p style='margin:0;display:inline-block;line-height: 2;'>" + statement2 + "</p>"
        
        if enclose:
            fraction = fraction + "</div>"
            
        return fraction

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore,grade,CheckAnswerType):
                                    
        '''Randomly selecting 3 wrong answers and adding the correct answer as well'''
        try:
            wrongAnswers = random.sample(wrongAnswers,3)
        except ValueError:
            pass
            
        wrongAnswers.append(answer)
        random.shuffle(wrongAnswers)
        try:
            self.answer1 = wrongAnswers[0]
            self.answer2 = wrongAnswers[1]
            self.answer3 = wrongAnswers[2]
            self.answer4 = wrongAnswers[3]        
        except IndexError:
            pass
        try:
            self.value1 = str(self.answer1[0])+"/"+str(self.answer1[1])+"/"+str(self.answer1[2])
            self.value2 = str(self.answer2[0])+"/"+str(self.answer2[1])+"/"+str(self.answer2[2])
            self.value3 = str(self.answer3[0])+"/"+str(self.answer3[1])+"/"+str(self.answer3[2])
            self.value4 = str(self.answer4[0])+"/"+str(self.answer4[1])+"/"+str(self.answer4[2])
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answerM1':self.answer1[0],'answerN1':self.answer1[1],'answerD1':self.answer1[2],
                'answerM2':self.answer2[0],'answerN2':self.answer2[1],'answerD2':self.answer2[2],
                'answerM3':self.answer3[0],'answerN3':self.answer3[1],'answerD3':self.answer3[2],
                'answerM4':self.answer4[0],'answerN4':self.answer4[1],'answerD4':self.answer4[2],
                'value1':self.value1,'value2':self.value2,'value3':self.value3,'value4':self.value4,
                'explain':explain,'problem_type':problem_type,
                'grade':grade,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}       
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            AnswerNumerator = int(str(answer).partition("/")[0])
            AnswerDenominator = int(str(answer).partition("/")[2])
            if "/" in str(InputAnswer)    :
                try:
                    InputNumerator = int(str(InputAnswer).partition("/")[0])
                    InputDenominator = int(str(InputAnswer).partition("/")[2])
                    return (AnswerNumerator==InputNumerator and AnswerDenominator==InputDenominator)
                except ValueError:
                    return False
            else:
                return False
        elif CheckAnswer == 2:
            try:
                return str(answer) == str(InputAnswer)
            except ValueError:
                return False 
        elif CheckAnswer == 3:
            answer = str(answer)
            InputAnswer = "["+str(InputAnswer).partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[2]+"]"
            if(answer==InputAnswer):
                return True
            else:
                return False