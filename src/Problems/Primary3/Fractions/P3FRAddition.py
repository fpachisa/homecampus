'''
Created on Feb 07, 2014
Module: P3FRAddition
Generates the Adding Fractions questions for Primary 3

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
  

History:
  
'''
import random
from Problems import PersonName
from Utils import LcmGcf

class P3FRAddition:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemTypeMCQ2",],3:["ProblemType3",],4:["ProblemTypeMCQ4",],
                            5:["ProblemType5",],6:["ProblemTypeMCQ6",],7:["ProblemType7",],8:["ProblemType8",],
                            9:["ProblemType9",],10:["ProblemType10",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemTypeMCQ2(),],3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemTypeMCQ4(),],5:[self.GenerateProblemType5(),],6:[self.GenerateProblemTypeMCQ6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],9:[self.GenerateProblemType9(),],
                                    10:[self.GenerateProblemType10(),],
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
        #return self.GenerateProblemType10()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10":self.GenerateProblemType10(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.fractions = random.choice([[1,2,1,10],
                                        [1,2,1,6],
                                        [1,2,1,4],
                                        [1,2,1,3],
                                        [1,2,1,5],
                                        [1,2,1,12],
                                        [1,3,1,6],
                                        [1,3,1,4],
                                        [1,3,1,9],
                                        [1,3,1,12],
                                        ])

        self.numerator1 = self.fractions[0]
        self.denominator1 = self.fractions[1]
        self.numerator2 = self.fractions[2]
        self.denominator2 = self.fractions[3]
        
        self.problem = self.CreateFractionStatement("Add&nbsp;", self.numerator1, self.denominator1, "&nbsp;") 
        self.problem = self.problem + self.CreateFractionStatement("and&nbsp;", self.numerator2, self.denominator2, ".")
        
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'

        self.LCM = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.multiplier1 = self.LCM/self.denominator1
        self.multiplier2 = self.LCM/self.denominator2
        
        self.denominator3 = self.LCM
        self.numerator3 = self.numerator1*self.LCM/self.denominator1 + self.numerator2*self.LCM/self.denominator2
        
        self.GCF = LcmGcf.LcmGcf().find_gcf(self.numerator3,self.denominator3)
        self.AnswerNumerator = self.numerator3 / self.GCF
        self.AnswerDenominator = self.denominator3 / self.GCF
        
        self.answer = str(self.AnswerNumerator)+"/"+str(self.AnswerDenominator)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.multiplier1,self.multiplier2,self.GCF)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,answerNumerator,answerDenominator,numerator1,denominator1,numerator2,denominator2,multiplier1,multiplier2,GCF):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(answerNumerator, answerDenominator,"white"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;=&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">&nbsp;?</div><br><br>'

        self.solution_text = self.solution_text + 'To add fractions, we must first express the fractions with the same denominator.<br><br>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 1:&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
        if multiplier1>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 2:&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        if multiplier2>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
        self.solution_text = self.solution_text + "<br><br>"
            
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Next, do the addition:</div><br>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;=&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1+numerator2*multiplier2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div><br><br>'
        
        if GCF>1:
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Finally, we simplify the fraction:</div><br>'
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1+numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(GCF)+'<br><br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(GCF)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(answerNumerator)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answerDenominator)+'</p></div><br><br>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So,&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;=&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(answerNumerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answerDenominator)+'</p></div><br><br>'
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ2(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.fractions = random.choice([[1,4,1,6],
                                        [1,4,1,8],
                                        [1,4,1,12],
                                        [1,5,1,10],
                                        [1,6,1,12]
                                        ])

        self.numerator1 = self.fractions[0]
        self.denominator1 = self.fractions[1]
        self.numerator2 = self.fractions[2]
        self.denominator2 = self.fractions[3]
        
        self.problem = "Choose the correct answer from below in the simplest form.<br><br>"
        self.problem = self.problem + self.CreateFraction(self.numerator1, self.denominator1) + " + "
        self.problem = self.problem + self.CreateFraction(self.numerator2, self.denominator2) + " = "
        
        self.LCM = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.multiplier1 = self.LCM/self.denominator1
        self.multiplier2 = self.LCM/self.denominator2
        
        self.denominator3 = self.LCM
        self.numerator3 = self.numerator1*self.LCM/self.denominator1 + self.numerator2*self.LCM/self.denominator2
        
        self.GCF = LcmGcf.LcmGcf().find_gcf(self.numerator3,self.denominator3)
        self.AnswerNumerator = self.numerator3 / self.GCF
        self.AnswerDenominator = self.denominator3 / self.GCF
        
        self.answer = self.CreateFractionShowMCQ(self.AnswerNumerator,self.AnswerDenominator,"#2B7657")
        
        self.answers = [[self.CreateFractionShowMCQ((self.numerator1+self.numerator2),self.AnswerDenominator,"#2B7657"),"WRONG"],
                        [self.CreateFractionShowMCQ((self.numerator1+self.numerator2),(self.denominator1+self.denominator2),"#2B7657"),"WRONG"],
                        [self.CreateFractionShowMCQ(self.AnswerNumerator,(self.denominator1+self.denominator2),"#2B7657"),"WRONG"],
                        ]
        
        self.answers = random.sample(self.answers,2)
        self.answers.append([self.CreateFractionShowMCQ(self.AnswerNumerator,self.AnswerDenominator,"#2B7657"),self.CreateFractionShowMCQ(self.AnswerNumerator,self.AnswerDenominator,"#2B7657")],)
        random.shuffle(self.answers)
        
        self.answer1 = self.answers[0][0]
        self.value1 = self.answers[0][1]
        self.answer2 = self.answers[1][0]
        self.value2 = self.answers[1][1]
        self.answer3 = self.answers[2][0]
        self.value3 = self.answers[2][1]
        
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.multiplier1,self.multiplier2,self.GCF)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2,
                'answer3':self.answer3,'value3':self.value3}

    def GenerateProblemType3(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.fractions = random.choice([[1,2,5,12],
                                        [1,3,2,9],
                                        [1,3,4,9],
                                        [1,3,5,9],
                                        [1,3,5,12],
                                        [1,3,7,12]
                                        ])

        self.numerator1 = self.fractions[0]
        self.denominator1 = self.fractions[1]
        self.numerator2 = self.fractions[2]
        self.denominator2 = self.fractions[3]
        
        self.problem = "<div>"
        self.problem = self.problem + self.CreateFractionStatement("Find the sum of&nbsp;", self.numerator1, self.denominator1, "&nbsp;") + self.CreateFractionStatement("and&nbsp;", self.numerator2, self.denominator2, ".")
        self.problem = self.problem + '</div><div>Write your answer in the simplest form.</div>'

        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'

        self.LCM = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.multiplier1 = self.LCM/self.denominator1
        self.multiplier2 = self.LCM/self.denominator2
        
        self.denominator3 = self.LCM
        self.numerator3 = self.numerator1*self.LCM/self.denominator1 + self.numerator2*self.LCM/self.denominator2
        
        self.GCF = LcmGcf.LcmGcf().find_gcf(self.numerator3,self.denominator3)
        self.AnswerNumerator = self.numerator3 / self.GCF
        self.AnswerDenominator = self.denominator3 / self.GCF
        
        self.answer = str(self.AnswerNumerator)+"/"+str(self.AnswerDenominator)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.multiplier1,self.multiplier2,self.GCF)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def GenerateProblemTypeMCQ4(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.fractions = random.choice([[1,4,5,12],
                                        [1,4,7,12],
                                        [1,5,3,10],
                                        [1,5,7,10],
                                        [1,6,5,12],
                                        [1,6,7,12]
                                        ])

        self.numerator1 = self.fractions[0]
        self.denominator1 = self.fractions[1]
        self.numerator2 = self.fractions[2]
        self.denominator2 = self.fractions[3]
        
        self.problem = "Choose the correct answer from below in the simplest form.<br><br>"
        self.problem = self.problem + self.CreateFraction(self.numerator1, self.denominator1) + " + " + self.CreateFraction(self.numerator2, self.denominator2) + " = "
        

        self.LCM = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.multiplier1 = self.LCM/self.denominator1
        self.multiplier2 = self.LCM/self.denominator2
        
        self.denominator3 = self.LCM
        self.numerator3 = self.numerator1*self.LCM/self.denominator1 + self.numerator2*self.LCM/self.denominator2
        
        self.GCF = LcmGcf.LcmGcf().find_gcf(self.numerator3,self.denominator3)
        self.AnswerNumerator = self.numerator3 / self.GCF
        self.AnswerDenominator = self.denominator3 / self.GCF
        
        self.answer = self.CreateFractionShowMCQ(self.AnswerNumerator,self.AnswerDenominator,"#2B7657")
        
        self.answers = [[self.CreateFractionShowMCQ((self.numerator1+self.numerator2),self.AnswerDenominator,"#2B7657"),"WRONG"],
                        [self.CreateFractionShowMCQ((self.numerator1+self.numerator2),(self.denominator1+self.denominator2),"#2B7657"),"WRONG"],
                        [self.CreateFractionShowMCQ(self.AnswerNumerator,(self.denominator1+self.denominator2),"#2B7657"),"WRONG"],
                        ]
        
        self.answers = random.sample(self.answers,2)
        self.answers.append([self.CreateFractionShowMCQ(self.AnswerNumerator,self.AnswerDenominator,"#2B7657"),self.CreateFractionShowMCQ(self.AnswerNumerator,self.AnswerDenominator,"#2B7657")],)
        random.shuffle(self.answers)
        
        self.answer1 = self.answers[0][0]
        self.value1 = self.answers[0][1]
        self.answer2 = self.answers[1][0]
        self.value2 = self.answers[1][1]
        self.answer3 = self.answers[2][0]
        self.value3 = self.answers[2][1]
        
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.multiplier1,self.multiplier2,self.GCF)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2,
                'answer3':self.answer3,'value3':self.value3}

    def GenerateProblemType5(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.fractions = random.choice([[1,2,1,12,2,12],
                                        [1,2,1,10,3,10],
                                        [1,2,1,8,2,8],
                                        [1,3,1,12,3,12],
                                        [1,3,2,12,3,12],
                                        [1,3,3,12,4,12],
                                        [1,3,4,12,2,12],
                                        [1,3,1,9,2,9],
                                        [1,3,1,9,4,9],
                                        [1,3,2,6,1,6]
                                        ])

        self.numerator1 = self.fractions[0]
        self.denominator1 = self.fractions[1]
        self.numerator2 = self.fractions[2]
        self.denominator2 = self.fractions[3]
        self.numerator3 = self.fractions[4]
        self.denominator3 = self.fractions[5]
        
        self.problem = "Add " + self.CreateFraction(self.numerator1, self.denominator1) + ", " + self.CreateFraction(self.numerator2, self.denominator2) + " and " + self.CreateFraction(self.numerator3, self.denominator3) + "."
        
        self.problem = self.problem + '<div>Write your answer in the simplest form.</div>'
        
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'

        self.LCM = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.multiplier1 = self.LCM/self.denominator1
        self.multiplier2 = self.LCM/self.denominator2
        self.multiplier3 = self.LCM/self.denominator3
        
        self.denominator4 = self.LCM
        self.numerator4 = self.numerator1*self.LCM/self.denominator1 + self.numerator2*self.LCM/self.denominator2 + self.numerator3*self.LCM/self.denominator3 
        
        self.GCF = LcmGcf.LcmGcf().find_gcf(self.numerator4,self.denominator4)
        self.AnswerNumerator = self.numerator4 / self.GCF
        self.AnswerDenominator = self.denominator4 / self.GCF
        
        self.answer = str(self.AnswerNumerator)+"/"+str(self.AnswerDenominator)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.numerator3,self.denominator3,self.multiplier1,self.multiplier2,self.multiplier3,self.GCF)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,answerNumerator,answerDenominator,numerator1,denominator1,numerator2,denominator2,numerator3,denominator3,multiplier1,multiplier2,multiplier3,GCF):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(answerNumerator, answerDenominator,"white"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;=&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">&nbsp;?</div><br><br>'

        self.solution_text = self.solution_text + 'To add fractions, we must first express the fractions with the same denominator.<br><br>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 1:&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
        if multiplier1>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 2:&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        if multiplier2>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Fraction 3:&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3)+'</p></div>'
        if multiplier3>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3*multiplier3)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3*multiplier3)+'</p></div>'
        self.solution_text = self.solution_text + "<br><br>"
            
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Next, do the addition:</div><br>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3*multiplier3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3*multiplier3)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;=&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1+numerator2*multiplier2+numerator3*multiplier3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div><br><br>'
        
        if GCF>1:
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Finally, we simplify the fraction:</div><br>'
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1+numerator2*multiplier2+numerator3*multiplier3)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(GCF)+'<br><br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(GCF)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(answerNumerator)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answerDenominator)+'</p></div><br><br>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So,&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;=&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(answerNumerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answerDenominator)+'</p></div><br><br>'
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ6(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.fractions = random.choice([[1,3,1,4,1,4],
                                        [1,4,1,8,1,8],
                                        [1,4,3,8,1,8],
                                        [1,4,2,8,3,8],
                                        [1,5,1,10,1,10],
                                        [1,5,3,10,1,10],
                                        [1,5,3,10,2,10],
                                        [2,5,3,10,1,10],
                                        [1,6,1,12,1,12],
                                        [1,6,5,12,1,12],
                                        [1,6,7,12,1,12],
                                        [1,6,5,12,3,12]
                                        ])

        self.numerator1 = self.fractions[0]
        self.denominator1 = self.fractions[1]
        self.numerator2 = self.fractions[2]
        self.denominator2 = self.fractions[3]
        self.numerator3 = self.fractions[4]
        self.denominator3 = self.fractions[5]
        
        self.problem = "Choose the correct answer from below in the simplest form.<br><br>"
        
        self.problem = self.problem + self.CreateFraction(self.numerator1, self.denominator1) + " + " + self.CreateFraction(self.numerator2, self.denominator2) + " + " + self.CreateFraction(self.numerator3, self.denominator3) + " = "
        
        self.LCM = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.multiplier1 = self.LCM/self.denominator1
        self.multiplier2 = self.LCM/self.denominator2
        self.multiplier3 = self.LCM/self.denominator3
        
        self.denominator4 = self.LCM
        self.numerator4 = self.numerator1*self.LCM/self.denominator1 + self.numerator2*self.LCM/self.denominator2 + self.numerator3*self.LCM/self.denominator3
        
        self.GCF = LcmGcf.LcmGcf().find_gcf(self.numerator4,self.denominator4)
        self.AnswerNumerator = self.numerator4 / self.GCF
        self.AnswerDenominator = self.denominator4 / self.GCF
        
        self.answer = self.CreateFractionShowMCQ(self.AnswerNumerator,self.AnswerDenominator,"#2B7657")
        
        self.answers = [[self.CreateFractionShowMCQ((self.numerator1+self.numerator2+self.numerator3),self.AnswerDenominator,"#2B7657"),"WRONG"],
                        [self.CreateFractionShowMCQ((self.numerator1+self.numerator2+self.numerator3),(self.denominator1+self.denominator2+self.denominator3),"#2B7657"),"WRONG"],
                        [self.CreateFractionShowMCQ(self.AnswerNumerator,(self.denominator1+self.denominator2+self.denominator3),"#2B7657"),"WRONG"],
                        ]
        
        self.answers = random.sample(self.answers,2)
        self.answers.append([self.CreateFractionShowMCQ(self.AnswerNumerator,self.AnswerDenominator,"#2B7657"),self.CreateFractionShowMCQ(self.AnswerNumerator,self.AnswerDenominator,"#2B7657")],)
        random.shuffle(self.answers)
        
        self.answer1 = self.answers[0][0]
        self.value1 = self.answers[0][1]
        self.answer2 = self.answers[1][0]
        self.value2 = self.answers[1][1]
        self.answer3 = self.answers[2][0]
        self.value3 = self.answers[2][1]
        
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.numerator3,self.denominator3,self.multiplier1,self.multiplier2,self.multiplier3,self.GCF)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2,
                'answer3':self.answer3,'value3':self.value3}

    def GenerateProblemType7(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.names = random.sample(PersonName.AuntyName,1)+random.sample(PersonName.GirlName,2)
        
        self.fractions = random.choice([[1,2,1,10],
                                        [1,2,1,6],
                                        [1,2,1,4],
                                        [1,2,1,3],
                                        [1,2,1,5],
                                        [1,2,1,12],
                                        [1,3,1,6],
                                        [1,3,1,4],
                                        [1,3,1,9],
                                        [1,3,1,12],
                                        ])
        self.item = random.choice(['ribbon', 'lace', 'cloth', 'stick', 'tape', 'wire'])
        self.numerator1 = self.fractions[0]
        self.denominator1 = self.fractions[1]
        self.numerator2 = self.fractions[2]
        self.denominator2 = self.fractions[3]
        
        
        self.problem = '<div>%s had a %s.</div>' % (self.names[0],self.item)
        self.problem = self.problem + "<div>"
        #1
        stmt1 = "She cut"
        stmt2 = "of the %s for %s" % (self.item, self.names[1])
        self.problem = self.problem + self.CreateFractionStatement(stmt1, self.numerator1, self.denominator1, stmt2)

        #2
        stmt1 = " and "
        stmt2 = "of the %s for %s" % (self.item, self.names[2])
        self.problem = self.problem + self.CreateFractionStatement(stmt1, self.numerator2, self.denominator2, stmt2)
        
        self.problem = self.problem + "</div>"
        stmt1 = "What fraction of the %s did she cut altogether for the two children?<br />" % (self.item)
        self.problem = self.problem + stmt1
        self.problem = self.problem + "Write your answer in the simplest form."
        
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'

        self.LCM = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.multiplier1 = self.LCM/self.denominator1
        self.multiplier2 = self.LCM/self.denominator2
        
        self.denominator3 = self.LCM
        self.numerator3 = self.numerator1*self.LCM/self.denominator1 + self.numerator2*self.LCM/self.denominator2
        
        self.GCF = LcmGcf.LcmGcf().find_gcf(self.numerator3,self.denominator3)
        self.AnswerNumerator = self.numerator3 / self.GCF
        self.AnswerDenominator = self.denominator3 / self.GCF
        
        self.answer = str(self.AnswerNumerator)+"/"+str(self.AnswerDenominator)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.multiplier1,self.multiplier2,self.GCF,self.names[1],self.names[2],self.item,"She cut","altogether for the two children.")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,answerNumerator,answerDenominator,numerator1,denominator1,numerator2,denominator2,multiplier1,multiplier2,GCF,name1,name2,item,statement1,statement2):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(answerNumerator, answerDenominator,"white"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;=&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">&nbsp;?</div><br><br>'

        self.solution_text = self.solution_text + 'To add fractions, we must first express the fractions with the same denominator.<br><br>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;</div>'%(name1)
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
        if multiplier1>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;</div>'%(name2)
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        if multiplier2>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
        self.solution_text = self.solution_text + "<br><br>"
            
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Next, do the addition:</div><br>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;=&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1+numerator2*multiplier2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div><br><br>'
        
        if GCF>1:
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Finally, we simplify the fraction:</div><br>'
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1+numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(GCF)+'<br><br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(GCF)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(answerNumerator)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answerDenominator)+'</p></div><br><br>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s&nbsp;</div>'%(statement1)
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(answerNumerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answerDenominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">of the %s %s</div>'%(item,statement2)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.name = random.choice(PersonName.GirlName)
        self.item = random.choice(['watermelon', 'papaya', 'pineapple', 'melon'])
                
        self.fractions = random.choice([[1,2,1,12,2,12],
                                        [1,2,1,10,3,10],
                                        [1,2,1,8,2,8],
                                        [1,3,1,12,3,12],
                                        [1,3,2,12,3,12],
                                        [1,3,3,12,4,12],
                                        [1,3,4,12,2,12],
                                        [1,3,1,9,2,9],
                                        [1,3,1,9,4,9],
                                        [1,3,2,6,1,6]
                                        ])

        self.numerator1 = self.fractions[0]
        self.denominator1 = self.fractions[1]
        self.numerator2 = self.fractions[2]
        self.denominator2 = self.fractions[3]
        self.numerator3 = self.fractions[4]
        self.denominator3 = self.fractions[5]
        
        self.problem = '<div>%s had a %s.</div><br>' % (self.name,self.item)
        self.problem = self.problem + 'She used ' + self.CreateFraction(self.numerator1, self.denominator2) + " of it for shake, "
        self.problem = self.problem + self.CreateFraction(self.numerator2, self.denominator2) + " of it for a salad and "
        self.problem = self.problem + self.CreateFraction(self.numerator3, self.denominator3) + " of it for an icecream."
        
        self.problem = self.problem + '<div>What fraction of the %s did she use altogether?</div>' % (self.item)
        self.problem = self.problem + '<br><div>Write your answer in the simplest form.</div>'
        
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'

        self.LCM = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.multiplier1 = self.LCM/self.denominator1
        self.multiplier2 = self.LCM/self.denominator2
        self.multiplier3 = self.LCM/self.denominator3
        
        self.denominator4 = self.LCM
        self.numerator4 = self.numerator1*self.LCM/self.denominator1 + self.numerator2*self.LCM/self.denominator2 + self.numerator3*self.LCM/self.denominator3
        
        self.GCF = LcmGcf.LcmGcf().find_gcf(self.numerator4,self.denominator4)
        self.AnswerNumerator = self.numerator4 / self.GCF
        self.AnswerDenominator = self.denominator4 / self.GCF
        
        self.answer = str(self.AnswerNumerator)+"/"+str(self.AnswerDenominator)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.numerator3,self.denominator3,self.multiplier1,self.multiplier2,self.multiplier3,self.GCF,"Shake","Salad","Icecream",self.item,"She used")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,answerNumerator,answerDenominator,numerator1,denominator1,numerator2,denominator2,numerator3,denominator3,multiplier1,multiplier2,multiplier3,GCF,object1,object2,object3,item,statement):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(answerNumerator, answerDenominator,"white"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;=&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">&nbsp;?</div><br><br>'

        self.solution_text = self.solution_text + 'To add fractions, we must first express the fractions with the same denominator.<br><br>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;</div>'%(object1)
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div>'
        if multiplier1>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;</div>'%(object2)
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        if multiplier2>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s:&nbsp;</div>'%(object3)
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3)+'</p></div>'
        if multiplier3>1:
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3*multiplier3)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3*multiplier3)+'</p></div>'
        self.solution_text = self.solution_text + "<br><br>"
            
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Next, do the addition:</div><br>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator2*multiplier2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2*multiplier2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;+&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator3*multiplier3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator3*multiplier3)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;=&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1+numerator2*multiplier2+numerator3*multiplier3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div><br><br>'
        
        if GCF>1:
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Finally, we simplify the fraction:</div><br>'
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator1*multiplier1+numerator2*multiplier2+numerator3*multiplier3)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1*multiplier1)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(GCF)+'<br><br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(GCF)+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(answerNumerator)+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answerDenominator)+'</p></div><br><br>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">%s&nbsp;</div>'%(statement)
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(answerNumerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answerDenominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">of the %s altogether.</div>'%(item)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.names = random.sample(PersonName.BoyName,1)+random.sample(PersonName.GirlName,1)
        
        self.fractions = random.choice([[1,2,5,12],
                                        [1,3,2,9],
                                        [1,3,4,9],
                                        [1,3,5,9],
                                        [1,3,5,12],
                                        [1,3,7,12]
                                        ])
        
        self.item = random.choice(['pie', 'pizza', 'cake', 'chocolate bar'])
        self.numerator1 = self.fractions[0]
        self.denominator1 = self.fractions[1]
        self.numerator2 = self.fractions[2]
        self.denominator2 = self.fractions[3]
        
        self.problem = '<div>%s and %s bought a %s.</div>'%(self.names[0],self.names[1],self.item)
        
        #1
        stmt1 = "%s ate" % (self.names[0])
        stmt2 = " of the %s and " % (self.item)
        self.problem = self.problem + self.CreateFractionStatement(stmt1, self.numerator1, self.denominator1, stmt2)
        
        #2
        stmt1 = "%s ate" % (self.names[1])
        stmt2 = " of the %s." % (self.item)
        self.problem = self.problem + self.CreateFractionStatement(stmt1, self.numerator2, self.denominator2, stmt2)
        
        self.problem = self.problem + '<div><br />What fraction of the %s did they eat altogether?</div>' % (self.item)
        self.problem = self.problem + '<div>Write your answer in the simplest form.</div>'
        
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'

        self.LCM = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.multiplier1 = self.LCM/self.denominator1
        self.multiplier2 = self.LCM/self.denominator2
        
        self.denominator3 = self.LCM
        self.numerator3 = self.numerator1*self.LCM/self.denominator1 + self.numerator2*self.LCM/self.denominator2
        
        self.GCF = LcmGcf.LcmGcf().find_gcf(self.numerator3,self.denominator3)
        self.AnswerNumerator = self.numerator3 / self.GCF
        self.AnswerDenominator = self.denominator3 / self.GCF
        
        self.answer = str(self.AnswerNumerator)+"/"+str(self.AnswerDenominator)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.multiplier1,self.multiplier2,self.GCF,self.names[0],self.names[1],self.item,"They ate","altogether.")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def GenerateProblemType10(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.names = random.sample(PersonName.UncleName,1)+random.sample(PersonName.PersonName,3)
        self.item = random.choice(['bag of marbles', 'bag of cookies', 'box of chocolates', 'bag of chips'])
                
        self.fractions = random.choice([[1,3,1,4,1,4],
                                        [1,4,1,8,1,8],
                                        [1,4,3,8,1,8],
                                        [1,4,2,8,3,8],
                                        [1,5,1,10,1,10],
                                        [1,5,3,10,1,10],
                                        [1,5,3,10,2,10],
                                        [2,5,3,10,1,10],
                                        [1,6,1,12,1,12],
                                        [1,6,5,12,1,12],
                                        [1,6,7,12,1,12],
                                        [1,6,5,12,3,12]
                                        ])

        self.numerator1 = self.fractions[0]
        self.denominator1 = self.fractions[1]
        self.numerator2 = self.fractions[2]
        self.denominator2 = self.fractions[3]
        self.numerator3 = self.fractions[4]
        self.denominator3 = self.fractions[5]
        
        self.problem = '<div>%s had a %s.</div><br>' % (self.names[0],self.item)
        
        #1
        stmt1 = "He gave"
        stmt2 = "of the %s to %s," % (self.item,self.names[1])
        self.problem = self.problem + self.CreateFractionStatement(stmt1, self.numerator1, self.denominator1, stmt2)
        
        #2
        stmt1 = ""
        stmt2 = " of the %s to %s and" % (self.item,self.names[2])
        self.problem = self.problem + self.CreateFractionStatement(stmt1, self.numerator2, self.denominator2, stmt2)
        
        #3
        stmt1 = ""
        stmt2 = " of the %s to %s." % (self.item,self.names[3])
        self.problem = self.problem + self.CreateFractionStatement(stmt1, self.numerator3, self.denominator3, stmt2)
        
        self.problem = self.problem + '<br><br><div>What fraction of the %s did the children receive altogether?</div>' % (self.item)
        self.problem = self.problem + '<div>Write your answer in the simplest form.</div>'
        
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'

        self.LCM = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.multiplier1 = self.LCM/self.denominator1
        self.multiplier2 = self.LCM/self.denominator2
        self.multiplier3 = self.LCM/self.denominator3
        
        self.denominator4 = self.LCM
        self.numerator4 = self.numerator1*self.LCM/self.denominator1 + self.numerator2*self.LCM/self.denominator2 + self.numerator3*self.LCM/self.denominator3
        
        self.GCF = LcmGcf.LcmGcf().find_gcf(self.numerator4,self.denominator4)
        self.AnswerNumerator = self.numerator4 / self.GCF
        self.AnswerDenominator = self.denominator4 / self.GCF
        
        self.answer = str(self.AnswerNumerator)+"/"+str(self.AnswerDenominator)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator1,self.denominator1,self.numerator2,self.denominator2,self.numerator3,self.denominator3,self.multiplier1,self.multiplier2,self.multiplier3,self.GCF,self.names[1],self.names[2],self.names[3],self.item,"The children received")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}
        
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

    def CreateFractionShowMCQ(self,numerator,denominator,color):
        #fraction = ""
        #fraction = fraction + '<div style="width:40px;display:inline-block;margin-top:-17px;"><p style="line-height:20%;text-align:center;color:"'+color+';">'+str(numerator)+'<br>__<br></p>'
        #fraction = fraction + '<p style="line-height:20%;text-align:center;color:"'+color+';">'+str(denominator)+'</p></div>'
        
        #11-AUG-2016 -- using the createFraction function to create fraction display for the answers as well
        return self.CreateFraction(numerator, denominator, color)
   
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