'''
Created on Feb 04, 2014
Module: P3FRSimplifyingFractions
Generates the Simplifying Fractions questions for Primary 3

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

class P3FRSimplifyingFractions:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemTypeMCQ2",],3:["ProblemType3",],4:["ProblemTypeMCQ4",],
                            5:["ProblemTypeMCQ5",],6:["ProblemType6",],7:["ProblemType7",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemTypeMCQ2(),],3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemTypeMCQ4(),],5:[self.GenerateProblemTypeMCQ5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],
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
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominator = randint(2,5)
        self.numerator = randint(1,self.denominator-1)
        
        self.multiplier = randint(2,5)
        self.denominator = self.denominator * self.multiplier
        self.numerator = self.numerator * self.multiplier

        self.problem = self.CreateFractionStatement("Write", self.numerator, self.denominator, "in its simplest form.", "#000")
        AnswerGCF = LcmGcf.LcmGcf().find_gcf(self.numerator,self.denominator)
        self.AnswerNumerator = self.numerator / AnswerGCF
        self.AnswerDenominator = self.denominator / AnswerGCF
        self.answer = str(self.AnswerNumerator) + "/" + str(self.AnswerDenominator)           

        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.unit,self.dollar_unit,self.numerator,self.denominator,AnswerGCF)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,answerNumerator,answerDenominator,unit,dollar_unit,numerator,denominator,GCF):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(answerNumerator, answerDenominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"
        
        self.solution_text = self.solution_text + "Both the numerator and the denominator can be divided by %d to get the simplest form of the given fraction.<br><br>"%(GCF)
        
        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(GCF)+'<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(GCF)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(answerNumerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answerDenominator)+'</p></div><br><br>'
        
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ2(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.CheckAnswerType = 3             
        
        self.denominator1 = randint(2,5)
        self.numerator1 = randint(1,self.denominator1-1)
        
        self.multiplier = randint(2,5)
        self.denominator = self.denominator1 * self.multiplier
        self.numerator = self.numerator1 * self.multiplier

        self.problem = self.CreateFractionStatement("The simplest equivalent fraction of", self.numerator, self.denominator, "is:", "#000")        
        AnswerGCF = LcmGcf.LcmGcf().find_gcf(self.numerator,self.denominator)
        self.AnswerNumerator = self.numerator / AnswerGCF
        self.AnswerDenominator = self.denominator / AnswerGCF
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator

        self.answer = [0,self.answer1,self.answer2]
            
        self.wrongAnswers = []
        '''generating 3 wrong answers and making sure any of it is not equal to the correct answer'''
        self.WrongMixed = 0
        self.wrongAnswers.append([self.WrongMixed,self.numerator,self.denominator/self.multiplier])
        self.wrongAnswers.append([self.WrongMixed,self.numerator/self.multiplier,self.denominator])
        self.wrongAnswers.append([self.WrongMixed,self.numerator1*2,self.denominator1*2])
        self.wrongAnswers.append([self.WrongMixed,self.numerator1*3,self.denominator1*3])
                           
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ2"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.AnswerNumerator,self.AnswerDenominator,self.numerator,self.denominator,AnswerGCF)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)      

    def ExplainType2(self,problem,answer,answerNumerator,answerDenominator,numerator,denominator,GCF):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(numerator, denominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"
        
        self.solution_text = self.solution_text + "Both the numerator and the denominator can be divided by %d to get the simplest form of the given fraction.<br><br>"%(GCF)
        
        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(GCF)+'<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(GCF)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(answerNumerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(answerDenominator)+'</p></div><br><br>'
        
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain    

    def GenerateProblemType3(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominator1 = randint(2,5)
        self.numerator1 = randint(1,self.denominator1-1)
        
        self.multiplier = randint(2,5)
        self.denominator2 = self.denominator1 * self.multiplier
        self.numerator2 = self.numerator1 * self.multiplier
        
        self.problem = "<table style='display:inline-block;padding:0 6px;line-height: 15px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>" + str(self.numerator2) + "</td></tr> <tr><td>" + str(self.denominator2) + "</td></tr></table>"
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top"> = </div>'
        self.problem = self.problem + "<table style='display:inline-block;padding:0 6px;line-height: 15px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>?</td></tr> <tr><td>" + str(self.denominator1) + "</td></tr></table>"
        self.answer = self.numerator1     

        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.numerator2,self.denominator2,self.denominator1,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,numerator2,denominator2,denominator1,GCF):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"
        
        self.solution_text = self.solution_text + "The denominator is divided by %d to simplify it.<br>So, we must also divide the numerator by %d to get a simplified equivalent fraction.<br><br>"%(GCF,GCF)
        
        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(numerator2)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator2)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(GCF)+'<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(GCF)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(answer)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator1)+'</p></div><br><br>'
        self.solution_text = self.solution_text + 'So, the missing numerator is %d.'%(answer)
        
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ4(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.fractions = random.choice([[1,2,4,8,"Yes",2,2],
                                        [2,4,4,8,"No",2,2],
                                        [3,6,6,12,"No",2,3],
                                        [2,4,6,12,"No",3,2],
                                        [1,2,6,12,"Yes",2,3],
                                        [2,6,4,12,"No",2,2],
                                        [1,3,4,12,"Yes",2,2],
                                        [1,3,3,9,"Yes",3,1],
                                        [1,2,3,6,"Yes",3,1],
                                        [3,4,9,12,"Yes",3,1],
                                        [4,5,8,10,"Yes",2,1],
                                        [4,6,8,12,"No",2,2],
                                        [2,3,8,12,"Yes",2,2]
                                        ])

        self.denominator1 = self.fractions[3]
        self.numerator1 = self.fractions[2]
        self.denominator2 = self.fractions[1]
        self.numerator2 = self.fractions[0]
        self.answer = self.fractions[4]
        
        self.problem = self.CreateFractionStatement("Is", self.numerator1, self.denominator2, "the simplest fraction", "#000")
        self.problem = self.problem + self.CreateFractionStatement("&nbsp;of", self.numerator2, self.denominator2, "?", "#000")
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.fractions)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':"Yes",'value1':"Yes",'answer2':"No",'value2':"No"}

    def ExplainType4(self,problem,answer,fractions):
        self.answer_text = "<br>The correct answer is:<br>%s"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"
        
        self.solution_text = self.solution_text + "We use division to find a fraction in its simplest form.<br><br>"
        
        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(fractions[2])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(fractions[5])+'<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(fractions[5])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(fractions[2]/fractions[5])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3]/fractions[5])+'</p></div>'
        
        if fractions[6]!=1:
            self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(fractions[6])+'<br><br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(fractions[6])+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(fractions[2]/fractions[5]/fractions[6])+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3]/fractions[5]/fractions[6])+'</p></div>'
        
        self.solution_text = self.solution_text + '<br><br>'

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">The simplest equivalent fraction of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(fractions[2])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(fractions[2]/fractions[5]/fractions[6])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3]/fractions[5]/fractions[6])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br><br>'
        
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ5(self):
        
        self.complexity_level = "easy"
        self.HCScore = 3
        self.grade = 3
        self.CheckAnswerType = 3             
        
        self.fractions = random.choice([[1,2,4,8,2,2,[2,4,8,16,1,8]],
                                        [1,3,4,12,2,2,[2,6,8,12,1,12]],
                                        [1,2,6,12,2,3,[2,4,3,6,2,6]],
                                        [1,3,3,9,3,1,[1,2,3,9,6,18]],
                                        [1,2,3,6,3,1,[1,6,1,3,6,12]],
                                        [3,4,9,12,3,1,[8,11,3,12,3,6]],
                                        [4,5,8,10,2,1,[10,8,5,4,8,20]],
                                        [2,3,8,12,2,2,[4,6,2,6,2,12]],
                                        [2,3,6,9,3,1,[9,6,3,2,1,3]],
                                        [1,4,3,12,3,1,[3,4,1,12,9,12]]
                                        ])

        self.denominator1 = self.fractions[3]
        self.numerator1 = self.fractions[2]

        self.problem = self.CreateFractionStatement("The simplest form of ", self.numerator, self.denominator, "is:", "#000") 
        
        self.AnswerNumerator = self.fractions[0]
        self.AnswerDenominator = self.fractions[1]
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator

        self.answer = [0,self.answer1,self.answer2]
            
        self.wrongAnswers = []
        '''generating 3 wrong answers and making sure any of it is not equal to the correct answer'''
        self.WrongMixed = 0
        self.wrongAnswers.append([self.WrongMixed,self.fractions[6][0],self.fractions[6][1]])
        self.wrongAnswers.append([self.WrongMixed,self.fractions[6][2],self.fractions[6][3]])
        self.wrongAnswers.append([self.WrongMixed,self.fractions[6][4],self.fractions[6][5]])
                           
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ5"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.fractions)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.grade,self.CheckAnswerType)      

    def ExplainType5(self,problem,answer,fractions):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(fractions[0], fractions[1],"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"
        
        self.solution_text = self.solution_text + "We use division to find a fraction in its simplest form.<br><br>"
        
        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(fractions[2])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(fractions[4])+'<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(fractions[4])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(fractions[2]/fractions[4])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3]/fractions[4])+'</p></div>'
        
        if fractions[5]!=1:
            self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(fractions[5])+'<br><br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(fractions[5])+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(fractions[2]/fractions[4]/fractions[5])+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3]/fractions[4]/fractions[5])+'</p></div>'
        
        self.solution_text = self.solution_text + '<br><br>'

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">The simplest equivalent fraction of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(fractions[2])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(fractions[2]/fractions[4]/fractions[5])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3]/fractions[4]/fractions[5])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br><br>'
        
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain    

    def GenerateProblemType6(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.fractions = random.choice([[1,2,4,8,2,2],
                                        [1,3,4,12,2,2],
                                        [1,2,6,12,2,3],
                                        [1,3,3,9,3,1],
                                        [1,2,3,6,3,1],
                                        [3,4,9,12,3,1],
                                        [4,5,8,10,2,1],
                                        [1,2,5,10,2,1],
                                        [2,3,8,12,2,2],
                                        [2,3,4,6,2,1],
                                        [2,3,6,9,3,1],
                                        [1,4,3,12,3,1],
                                        [5,6,10,12,2,1],
                                        [1,4,2,8,2,1],
                                        [3,4,6,8,2,1],
                                        ])

        self.numerator = self.fractions[2]
        self.denominator = self.fractions[3]

        self.problem = self.CreateFractionStatement("Write the simplest equivalent fraction of", self.numerator, self.denominator, ".", "#000")
        
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'
                
        self.answer = str(self.fractions[0]) + "/" + str(self.fractions[1])           

        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit,self.fractions)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,unit,dollar_unit,fractions):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(fractions[0], fractions[1],"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"
        
        self.solution_text = self.solution_text + "We use division to find a fraction in its simplest form.<br><br>"
        
        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(fractions[2])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(fractions[4])+'<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(fractions[4])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(fractions[2]/fractions[4])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3]/fractions[4])+'</p></div>'
        
        if fractions[5]!=1:
            self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(fractions[5])+'<br><br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(fractions[5])+'</p></div>'
            self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
            self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(fractions[2]/fractions[4]/fractions[5])+'<br>__<br></p>'
            self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3]/fractions[4]/fractions[5])+'</p></div>'
        
        self.solution_text = self.solution_text + '<br><br>'

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">The simplest equivalent fraction of&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(fractions[2])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">&nbsp;is&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(fractions[2]/fractions[4]/fractions[5])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3]/fractions[4]/fractions[5])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div><br><br>'
        
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.fractions = random.choice([[1,2,4,8,4],
                                        [2,4,4,8,2],
                                        [1,3,4,12,4],
                                        [2,6,4,12,2],
                                        [1,2,6,12,6],
                                        [3,6,6,12,2],
                                        [2,4,6,12,3],
                                        [1,3,3,9,3],
                                        [1,2,3,6,3],
                                        [3,4,9,12,3],
                                        [4,5,8,10,2],
                                        [1,2,5,10,2],
                                        [2,3,8,12,4],
                                        [4,6,8,12,2],
                                        [2,3,4,6,2],
                                        [2,3,6,9,3],
                                        [1,4,3,12,3],
                                        [5,6,10,12,2],
                                        [1,4,2,8,2],
                                        [3,4,6,8,2],
                                        ])

        self.numerator1 = self.fractions[0]
        self.denominator1 = self.fractions[1]

        self.numerator2 = self.fractions[2]
        self.denominator2 = self.fractions[3]

        self.problem = '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-5px;"><p style="line-height:20%;text-align:center;color:#2B7657;">'+str(self.numerator2)+'<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:#2B7657;">'+str(self.denominator2)+'<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-left:5px;margin-top:12px;"> = </div>'
        self.problem = self.problem + '<div style="width:60px;display:inline-block;vertical-align:top;"><p style="line-height:10%;text-align:center;color:#2B7657;">'+str(self.numerator1)+'<br>___<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;"><img src="/images/P3ProblemImages/P3FR_Simplifying_PT3.png"><br></p></div>'

        self.answer = self.denominator1     

        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.fractions)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,fractions):
        self.answer_text = "<br>The correct answer is:<br>%d"%(answer)
       
        self.solution_text = "<font class='ExplanationFont'>"
        
        self.solution_text = self.solution_text + "We divide the numerator by %d to get %d.<br>So, we must also divide the denominator by %d to get an equivalent fraction.<br><br>"%(fractions[4],fractions[0],fractions[4])
        
        self.solution_text = self.solution_text + '<div style="width:20px;display:inline-block;vertical-align:top;"><p style="line-height:20%;text-align:center;">'+str(fractions[2])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[3])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="width:45px;display:inline-block;vertical-align:top;text-align:left;"><p style="line-height:20%;text-align:left;">&nbsp;&divide;&nbsp;'+str(fractions[4])+'<br><br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:left;"><br>&nbsp;&divide;&nbsp;'+str(fractions[4])+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">=</div>'
        self.solution_text = self.solution_text + '<div style="width:30px;display:inline-block;vertical-align:top;margin-left:10px;"><p style="line-height:20%;text-align:center;">'+str(fractions[0])+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(fractions[1])+'</p></div>'
        self.solution_text = self.solution_text + '<br><br>'
        
        self.solution_text = self.solution_text + "So, the missing number is %d."%(answer)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def CreateFraction(self,numerator,denominator,colorCode):
        #fraction = ""
        #fraction = fraction + '<div style="width:40px;display:inline-block;"><p style="line-height:20%;text-align:center;color:#'+colorCode+';">'+str(numerator)+'<br>__<br></p>'
        #fraction = fraction + '<p style="line-height:20%;text-align:center;color:#'+colorCode+';">'+str(denominator)+'</p></div>'
        
        fraction = ""
        fraction = fraction + "<table style='display:inline-block;padding:0 6px;line-height: 15px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>" + str(numerator) + "</td></tr> <tr><td>" + str(denominator) + "</td></tr></table>"
        
        return fraction
    
    def CreateFractionStatement(self,statement1,numerator,denominator,statement2,colorCode):
        #fraction = '<div style="display:inline-block;vertical-align:top;margin-top:10px;">'+statement1+' </div>'
        #fraction = fraction + '<div style="width:40px;display:inline-block;vertical-align:bottom;margin-left:-5px;"><p style="line-height:20%;text-align:center;color:#'+colorCode+';">'+str(numerator)+'<br>__<br></p>'
        #fraction = fraction + '<p style="line-height:20%;text-align:center;color:#'+colorCode+';">'+str(denominator)+'<br></p></div>'
        #fraction = fraction + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">'+statement2+'</div>'
        
        fraction = "<p style='display:inline-block;line-height: 2;'>" + statement1 + "</p>" + self.CreateFraction(numerator, denominator, colorCode)+ "<p style='display:inline-block;line-height: 10px;'>" + statement2 + "</p>"
        
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
                return int(answer) == int(InputAnswer)
            except ValueError:
                return False
        elif CheckAnswer == 3:
            answer = str(answer)
            InputAnswer = "["+str(InputAnswer).partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[2]+"]"
            if(answer==InputAnswer):
                return True
            else:
                return False
        elif CheckAnswer == 4:
            try:
                return str(answer) == str(InputAnswer)
            except ValueError:
                return False                      