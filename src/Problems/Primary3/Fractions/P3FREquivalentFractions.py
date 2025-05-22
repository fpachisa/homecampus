'''
Created on Feb 03, 2014
Module: P3FREquivalentFractions
Generates the Equivalent Fractions questions for Primary 3

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
from Utils import LcmGcf

class P3FREquivalentFractions:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemTypeMCQ3",],3:["ProblemType5",],4:["ProblemType7",],
                            5:["ProblemType2",],6:["ProblemTypeMCQ4",],7:["ProblemType6",],8:["ProblemType8",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemTypeMCQ3(),],3:[self.GenerateProblemType5(),],
                                    4:[self.GenerateProblemType7(),],5:[self.GenerateProblemType2(),],6:[self.GenerateProblemTypeMCQ4(),],
                                    7:[self.GenerateProblemType6(),],8:[self.GenerateProblemType8(),],
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
        #return self.GenerateProblemType1()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominator = randint(2,5)
        self.numerator = randint(1,self.denominator-1)
        self.fractionColorCode = "2B7657"

        self.ProblemStatement1 = "Write any equivalent fraction of"
        self.ProblemStatement2 = "."
        self.problem = self.CreateFractionStatement(self.ProblemStatement1,self.numerator,self.denominator,self.ProblemStatement2,self.fractionColorCode)

        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'
                
        self.AnswerNumerator = self.numerator * 2
        self.AnswerDenominator = self.denominator * 2
        self.answer = str(self.AnswerNumerator) + "/" + str(self.AnswerDenominator)           

        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.unit,self.dollar_unit,self.numerator,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,answerNumerator,answerDenominator,unit,dollar_unit,numerator,denominator):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(answerNumerator, answerDenominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">To get an equivalent fraction of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">,</div>'
        self.solution_text = self.solution_text + '<br>we multiply its numerator and denominator by the same number.<br><br><br>'
        
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Examples:</div><br>'
        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&times;&nbsp;2<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&times;&nbsp;2</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(numerator*2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*2)+'</p></div><br><br>'

        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&times;&nbsp;3<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&times;&nbsp;3</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(numerator*3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*3)+'</p></div><br><br>'

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">The first 8 equivalent fractions of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">by multiplying both %d and %d by 2, 3, .... 9 are:</div><br>'%(numerator,denominator)

        for i in range (8):
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator*(i+1))+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*(i+1))+'</p></div>'
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator*9)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*9)+'</p></div>'

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominator = randint(6,12)
        self.numerator = randint(1,self.denominator-1)
        self.fractionColorCode = "2B7657"

        self.ProblemStatement1 = "Write any equivalent fraction of"
        self.ProblemStatement2 = "."
        self.problem = self.CreateFractionStatement(self.ProblemStatement1,self.numerator,self.denominator,self.ProblemStatement2,self.fractionColorCode)

        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'
        
        self.AnswerNumerator = self.numerator * 2
        self.AnswerDenominator = self.denominator * 2
        self.answer = str(self.AnswerNumerator) + "/" + str(self.AnswerDenominator)           

        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.unit,self.dollar_unit,self.numerator,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,answerNumerator,answerDenominator,unit,dollar_unit,numerator,denominator):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(numerator, denominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">To get an equivalent fraction of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">,</div>'
        self.solution_text = self.solution_text + '<br>we multiply its numerator and denominator by the same number.<br><br><br>'
        
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Examples:</div><br>'
        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&times;&nbsp;2<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&times;&nbsp;2</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(numerator*2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*2)+'</p></div><br><br>'

        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&times;&nbsp;3<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&times;&nbsp;3</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(numerator*3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*3)+'</p></div><br><br>'

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">The first 8 equivalent fractions of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">by multiplying both %d and %d by 2, 3, .... 9 are:</div><br>'%(numerator,denominator)

        for i in range (8):
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator*(i+1))+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*(i+1))+'</p></div>'
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator*9)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*9)+'</p></div>'

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ3(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.CheckAnswerType = 3             
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = randint(3,6)
        self.numerator = randint(1,self.denominator-1)
        self.fractionColorCode = "2B7657"
        
        self.ProblemStatement1 = "Which of the following fractions is not an equivalent fraction of"
        self.ProblemStatement2 = "?"
        self.problem = self.CreateFractionStatement(self.ProblemStatement1,self.numerator,self.denominator,self.ProblemStatement2,self.fractionColorCode)
        
        self.Answers = random.choice([[self.numerator*2,self.denominator*3],[self.numerator,self.denominator*2],[self.numerator*2,self.denominator*4]])
        self.AnswerDenominator = self.Answers[1]
        self.AnswerNumerator = self.Answers[0]
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator

        self.answer = [0,self.answer1,self.answer2]
            
        self.wrongAnswers = []
        '''generating 3 wrong answers and making sure any of it is not equal to the correct answer'''
        self.WrongMixed = 0
        self.wrongAnswers.append([self.WrongMixed,self.numerator*2,self.denominator*2])
        self.wrongAnswers.append([self.WrongMixed,self.numerator*3,self.denominator*3])
        self.wrongAnswers.append([self.WrongMixed,self.numerator*4,self.denominator*4])
        self.wrongAnswers.append([self.WrongMixed,self.numerator*5,self.denominator*5])
        self.wrongAnswers.append([self.WrongMixed,self.numerator*6,self.denominator*6])
                           
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ3"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)      

    def ExplainType3(self,problem,answer,answerNumerator,answerDenominator,numerator,denominator):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(answerNumerator, answerDenominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">To get an equivalent fraction of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">,</div>'
        self.solution_text = self.solution_text + '<br>we multiply its numerator and denominator by the same number.<br><br><br>'
        
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Examples:</div><br>'
        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&times;&nbsp;2<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&times;&nbsp;2</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(numerator*2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*2)+'</p></div><br><br>'

        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&times;&nbsp;3<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&times;&nbsp;3</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(numerator*3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*3)+'</p></div><br><br>'

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">The first 8 equivalent fractions of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">by multiplying both %d and %d by 2, 3, .... 9 are:</div><br>'%(numerator,denominator)

        for i in range (8):
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator*(i+1))+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*(i+1))+'</p></div>'
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator*9)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*9)+'</p></div><br><br>'

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So,&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(answerNumerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answerDenominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">is not an equivalent fraction of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div>'

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain    

    def GenerateProblemTypeMCQ4(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.CheckAnswerType = 3             
        
        ''' Generating 2 proper like fractions(numerator>denominator) and denominator<= 12'''
        self.denominator = randint(3,8)
        self.numerator = randint(1,self.denominator-1)
        self.fractionColorCode = "2B7657"
        
        self.ProblemStatement1 = "Which of the following fraction is an equivalent fraction of"
        self.ProblemStatement2 = "?"
        self.problem = self.CreateFractionStatement(self.ProblemStatement1,self.numerator,self.denominator,self.ProblemStatement2,self.fractionColorCode)
        
        self.Answers = random.choice([[self.numerator*2,self.denominator*2],[self.numerator*3,self.denominator*3],[self.numerator*4,self.denominator*4],
                                      [self.numerator*5,self.denominator*5],[self.numerator*6,self.denominator*6]])
        self.AnswerDenominator = self.Answers[1]
        self.AnswerNumerator = self.Answers[0]
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator

        self.answer = [0,self.answer1,self.answer2]
            
        self.wrongAnswers = []
        '''generating 3 wrong answers and making sure any of it is not equal to the correct answer'''
        self.WrongMixed = 0
        self.wrongAnswers.append([self.WrongMixed,self.numerator*2,self.denominator*3])
        self.wrongAnswers.append([self.WrongMixed,self.numerator*4,self.denominator*3])
        self.wrongAnswers.append([self.WrongMixed,self.numerator*4,self.denominator*2])
        self.wrongAnswers.append([self.WrongMixed,self.numerator*3,self.denominator*6])
        self.wrongAnswers.append([self.WrongMixed,self.numerator*4,self.denominator*6])
                           
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ4"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)      

    def ExplainType4(self,problem,answer,answerNumerator,answerDenominator,numerator,denominator):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(answerNumerator, answerDenominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">To get an equivalent fraction of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">,</div>'
        self.solution_text = self.solution_text + '<br>we multiply its numerator and denominator by the same number.<br><br><br>'
        
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">Examples:</div><br>'
        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&times;&nbsp;2<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&times;&nbsp;2</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(numerator*2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*2)+'</p></div><br><br>'

        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&times;&nbsp;3<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&times;&nbsp;3</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(numerator*3)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*3)+'</p></div><br><br>'

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">The first 8 equivalent fractions of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">by multiplying both %d and %d by 2, 3, .... 9 are:</div><br>'%(numerator,denominator)

        for i in range (8):
            self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator*(i+1))+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*(i+1))+'</p></div>'
            self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;margin-top:10px;margin-left:5px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator*9)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*9)+'</p></div><br><br>'

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So,&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(answerNumerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answerDenominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">is an equivalent fraction of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div>'

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain    

    def GenerateProblemType5(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominator1 = randint(3,5)
        self.numerator1 = randint(1,self.denominator1-1)
        
        self.multiplier = randint(2,8)
        self.denominator2 = self.denominator1 * self.multiplier
        self.numerator2 = self.numerator1 * self.multiplier

        self.problem = "<table style='display:inline-block;padding:0 6px;line-height: 15px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>" + str(self.numerator1) + "</td></tr> <tr><td>" + str(self.denominator1) + "</td></tr></table>"
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top"> = </div>'
        self.problem = self.problem + "<table style='display:inline-block;padding:0 6px;line-height: 15px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>?</td></tr> <tr><td>" + str(self.denominator2) + "</td></tr></table>"
        self.answer = self.numerator2

        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.numerator1,self.denominator1,self.denominator2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,numerator,denominator,denominator2):
        self.answer_text = "<br>The correct answer is: %d"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"
        
        self.solution_text = self.solution_text + "The denominator, %d, is multiplied by %d to get %d.<br>So, we must also multiply the numerator, %d, by %d to get an equivalent fraction.<br><br>"%(denominator,denominator2/denominator,denominator2,numerator,denominator2/denominator)

        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&times;&nbsp;'+str(denominator2/denominator)+'<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&times;&nbsp;'+str(denominator2/denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(numerator*denominator2/denominator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div><br><br>'
        
        self.solution_text = self.solution_text + "So, the missing number is %d."%(answer)
        
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominator1 = randint(6,10)
        self.numerator1 = randint(1,self.denominator1-1)
        
        self.multiplier = randint(2,8)
        self.denominator2 = self.denominator1 * self.multiplier
        self.numerator2 = self.numerator1 * self.multiplier
        
        self.problem = "<table style='display:inline-block;padding:0 6px;line-height: 15px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>" + str(self.numerator1) + "</td></tr> <tr><td>" + str(self.denominator1) + "</td></tr></table>"
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top"> = </div>'
        self.problem = self.problem + "<table style='display:inline-block;padding:0 6px;line-height: 15px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>" + str(self.numerator2) + "</td></tr> <tr><td>?</td></tr></table>"
        
        
        self.answer = self.denominator2

        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.numerator1,self.denominator1,self.numerator2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,numerator,denominator,numerator2):
        self.answer_text = "<br>The correct answer is: %d"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"
        
        self.solution_text = self.solution_text + "The numerator, %d, is multiplied by %d to get %d.<br>So, we must also multiply the denominator, %d, by %d to get an equivalent fraction.<br><br>"%(numerator,numerator2/numerator,numerator2,denominator,numerator2/numerator)
        
        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&times;&nbsp;'+str(numerator2/numerator)+'<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&times;&nbsp;'+str(numerator2/numerator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator*numerator2/numerator)+'</p></div><br><br>'
        
        self.solution_text = self.solution_text + "So, the missing number is %d."%(answer)
        
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominator1 = randint(3,5)
        self.numerator1 = randint(1,self.denominator1-1)
        
        self.multiplier = randint(2,8)
        self.denominator2 = self.denominator1 * self.multiplier
        self.numerator2 = self.numerator1 * self.multiplier
        
        self.problem = "<table style='display:inline-block;padding:0 6px;line-height: 15px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>?</td></tr> <tr><td>" + str(self.denominator1) + "</td></tr></table>"
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top"> = </div>'
        self.problem = self.problem + "<table style='display:inline-block;padding:0 6px;line-height: 15px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>" + str(self.numerator2) + "</td></tr> <tr><td>" + str(self.denominator2) + "</td></tr></table>"
        
        self.answer = self.numerator1

        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.numerator2,self.denominator2,self.denominator1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,numerator2,denominator2,denominator):
        self.answer_text = "<br>The correct answer is: %d"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"
        
        self.solution_text = self.solution_text + "The denominator, %d, is divided by %d to get %d.<br>So, we must also divide the numerator, %d, by %d to get an equivalent fraction.<br><br>"%(denominator2,denominator2/denominator,denominator,numerator2,denominator2/denominator)

        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(denominator2/denominator)+'<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(denominator2/denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(answer)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div><br><br>'
        
        self.solution_text = self.solution_text + "So, the missing number is %d."%(answer)
        
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominator1 = randint(6,10)
        self.numerator1 = randint(1,self.denominator1-1)
        
        self.multiplier = randint(2,8)
        self.denominator2 = self.denominator1 * self.multiplier
        self.numerator2 = self.numerator1 * self.multiplier

        self.problem = "<table style='display:inline-block;padding:0 6px;line-height: 15px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>" + str(self.numerator1) + "</td></tr> <tr><td>?</td></tr></table>"
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top"> = </div>'
        self.problem = self.problem + "<table style='display:inline-block;padding:0 6px;line-height: 15px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>" + str(self.numerator2) + "</td></tr> <tr><td>" + str(self.denominator2) + "</td></tr></table>"
        
        self.answer = self.denominator1

        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.numerator2,self.denominator2,self.numerator1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,numerator2,denominator2,numerator):
        self.answer_text = "<br>The correct answer is: %d"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"
        
        self.solution_text = self.solution_text + "The numerator, %d, is divided by %d to get %d.<br>So, we must also divide the denominator, %d, by %d to get an equivalent fraction.<br><br>"%(numerator2,numerator2/numerator,numerator,denominator2,numerator2/numerator)

        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(numerator2/numerator)+'<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(numerator2/numerator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answer)+'</p></div><br><br>'
        
        self.solution_text = self.solution_text + "So, the missing number is %d."%(answer)
        
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
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswer == 2:
            AnswerNumerator = int(str(answer).partition("/")[0])
            AnswerDenominator = int(str(answer).partition("/")[2])
            if "/" in str(InputAnswer)    :
                try:
                    InputNumerator = int(str(InputAnswer).partition("/")[0])
                    InputDenominator = int(str(InputAnswer).partition("/")[2])
                    AnswerGCF = LcmGcf.LcmGcf().find_gcf(AnswerNumerator,AnswerDenominator)
                    InputGCF = LcmGcf.LcmGcf().find_gcf(InputNumerator,InputDenominator)
                    return (AnswerNumerator/AnswerGCF==InputNumerator/InputGCF and AnswerDenominator/AnswerGCF==InputDenominator/InputGCF)
                except ValueError:
                    return False               
            else:
                return False
        elif CheckAnswer == 3:
            answer = str(answer)
            InputAnswer = "["+str(InputAnswer).partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[2]+"]"
            if(answer==InputAnswer):
                return True
            else:
                return False            