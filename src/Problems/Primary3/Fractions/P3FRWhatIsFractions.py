'''
Created on Jan 31, 2014
Module: P3FRWhatIsFractions
Generates the What is Fractions questions for Primary 3

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

class P3FRWhatIsFractions:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemType4",],
                            5:["ProblemType5",],6:["ProblemType6",],7:["ProblemType7",],8:["ProblemType8",],
                            9:["ProblemType9",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],9:[self.GenerateProblemType9(),],
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
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.numerator = randint(1,9)
        self.denominator = randint(self.numerator+2,12)
        self.fractionColorCode = "2B7657" 
        
        self.flag = randint(1,2)
        if self.flag == 1:
            self.problem = "What is the numerator in the given fraction?<br><br>"
            self.problem = self.problem + self.CreateFraction(self.numerator,self.denominator,self.fractionColorCode)
            self.answer = self.numerator
        else:
            self.problem = "What is the denominator in the given fraction?<br><br>"
            self.problem = self.problem + self.CreateFraction(self.numerator,self.denominator,self.fractionColorCode)
            self.answer = self.denominator           

        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,unit,dollar_unit,flag):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        if flag==1:
            self.solution_text = self.solution_text + "The top number in a fraction is the numerator.<br><br>In the given fraction, the numerator is %d.<br><br>"%(answer)
        else:
            self.solution_text = self.solution_text + "The bottom number in a fraction is the denominator.<br><br>In the given fraction, the denominator is %d.<br><br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3FR_WhatIsFractions_PT2a',2],['P3FR_WhatIsFractions_PT2b',3],['P3FR_WhatIsFractions_PT2c',4],
                       ['P3FR_WhatIsFractions_PT2d',2],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Express the shaded area in the figure below as a fraction.<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'
                   
        self.numerator = self.ProblemImage[1]
        self.denominator = 8 
        
        self.answer = str(self.numerator) + " / " + str(self.denominator)
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.numerator,self.denominator,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,numerator,denominator,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(numerator, denominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + "%d out of %d slices in the figure are shaded.<br><br>"%(numerator,denominator)
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So, the shaded area is&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">of the figure.</div>'

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.numbers = random.choice([[2,random.choice([["twice",2],["thrice",3],["four times",4],["five times",5]])],
                                      [3,random.choice([["twice",2],["thrice",3],["four times",4],])],
                                      [4,random.choice([["twice",2],["thrice",3],])],
                                      [5,random.choice([["twice",2],])],
                                      [6,random.choice([["twice",2],])],
                                      ])
        self.numerator = self.numbers[0]
        self.denominator = self.numerator * self.numbers[1][1]

        self.times = self.numbers[1][0]
        self.problem = "The numerator of a fraction is %d. The denominator of the fraction is %s its numerator. What fraction is it?<br>"%(self.numerator,self.times)
        
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'
        
        self.answer = str(self.numerator) + " / " + str(self.denominator)
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.numerator,self.denominator,self.unit,self.dollar_unit,self.numbers[1][1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,numerator,denominator,unit,dollar_unit,times):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(numerator, denominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:84px;'>Denominator</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;Numerator &nbsp;&times;&nbsp; %d</div><br>"%(times)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:84px;'></div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d &nbsp;&times;&nbsp; %d</div><br>"%(numerator,times)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:84px;'></div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d</div><br><br>"%(denominator)

        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So, the fraction is&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div>'

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3FR_WhatIsFractions_PT4a',5],['P3FR_WhatIsFractions_PT4b',5],['P3FR_WhatIsFractions_PT4c',3],
                       ['P3FR_WhatIsFractions_PT4d',3],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Express the shaded area in the figure below as a fraction.<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'><br>"

        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'
                   
        self.numerator = self.ProblemImage[1]
        self.denominator = 8 
        
        self.answer = str(self.numerator) + " / " + str(self.denominator)
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.numerator,self.denominator,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,numerator,denominator,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(numerator, denominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + "%d out of %d parts in the figure are shaded.<br><br>"%(numerator,denominator)
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So, the shaded area is&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">of the figure.</div>'

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.numerator = randint(5,8)
        self.denominator = randint(self.numerator+2,12)
        self.sum = self.numerator + self.denominator
        self.diff = self.denominator - self.numerator
        
        self.problem = "I am a fraction. The sum of my numerator and denominator is %d. "%(self.sum) 
        self.problem = self.problem + "My denominator is %d more than my numerator. What fraction am I?<br>"%(self.diff)

        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'
        
        self.answer = str(self.numerator) + " / " + str(self.denominator)
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.numerator,self.denominator,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,numerator,denominator,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(numerator, denominator,"ffffff"))
       
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        #beginning of model
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>? (a)</td><td>%d</td></tr>"%(denominator-numerator)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>numerator</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td><td rowspan=3 style='padding:0;vertical-align:middle;'>&nbsp;&nbsp;<img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;%d</td></tr>"%(self.color1,numerator+denominator)
        self.solution_text = self.solution_text + "<tr><td style='height:20px;'></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>denominator</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;width:100px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border:1px solid white;border-left:white dotted 1px;width:50px;'>&nbsp;</td></tr>"%(self.color2,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_large.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>? (b)</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:50px;'>2 units</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d &nbsp;&minus;&nbsp; %d</div><br>"%(numerator+denominator,denominator-numerator)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:50px;'></div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d</div><br>"%(numerator*2)
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:50px;'>1 unit</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d &nbsp; (numerator)</div><br><br>"%(numerator)
        
        self.solution_text = self.solution_text + "<div style='display:inline-block;vertical-align:top;width:50px;'>%d &nbsp;+&nbsp; %d</div><div style='display:inline-block;vertical-align:top;width:25px;text-align:center;'>=</div><div style='display:inline-block;vertical-align:top;'>&nbsp;%d &nbsp; (denominator)</div><br><br>"%(numerator,denominator-numerator,denominator)
        
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So, the fraction is &nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">.</div>'

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3FR_WhatIsFractions_PT6a',3],['P3FR_WhatIsFractions_PT6b',5],['P3FR_WhatIsFractions_PT6c',6],
                       ['P3FR_WhatIsFractions_PT6d',7],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Express the shaded area in the figure below as a fraction.<br><br>"

        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'
                   
        self.numerator = self.ProblemImage[1]
        self.denominator = 9 
        
        self.answer = str(self.numerator) + " / " + str(self.denominator)
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.numerator,self.denominator,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,numerator,denominator,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(numerator, denominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + "%d out of %d squares in the figure are shaded.<br><br>"%(numerator,denominator)
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So, the shaded area is&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">of the figure.</div>'

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        self.item = random.choice([["cake","pieces"],["pizza","slices"],["pie","pieces"]])
        self.SlicesCut = random.randrange(6,13,2)
        self.SlicesAte = randint(3,self.SlicesCut-2)
        self.SlicesLeft = self.SlicesCut - self.SlicesAte
        self.problem = "%s cut a %s into %d %s. She ate %d %s of the %s. "%(self.name,self.item[0],self.SlicesCut,self.item[1],self.SlicesAte,self.item[1],self.item[0])
        self.problem = self.problem + "What fraction of the %s is left?<br>"%(self.item[0])

        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'
                          
        self.numerator = self.SlicesLeft
        self.denominator = self.SlicesCut
        self.answer = str(self.numerator) + " / " + str(self.denominator)
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.numerator,self.denominator,self.unit,self.dollar_unit,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,numerator,denominator,unit,dollar_unit,item):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(numerator, denominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(denominator,denominator-numerator,numerator)
        self.solution_text = self.solution_text + "%d out of the %d %s of the %s are left.<br><br>"%(numerator,denominator,item[1],item[0])
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So,&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">of the %s is left.</div>'%(item[0])

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        self.item = random.choice(["pencils","erasers","crayons","balls","stickers"])
        self.relation = random.choice(["brother","sister","friend"])
        self.ItemInitial = randint(6,12)
        self.ItemGave = randint(3,self.ItemInitial-2)
        self.problem = "%s had %d %s. He gave %d %s to his %s. "%(self.name,self.ItemInitial,self.item,self.ItemGave,self.item,self.relation)
        self.problem = self.problem + "What fraction of the %s did he give to his %s?<br>"%(self.item,self.relation)
        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'
        self.numerator = self.ItemGave
        self.denominator = self.ItemInitial
        self.answer = str(self.numerator) + " / " + str(self.denominator)
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.numerator,self.denominator,self.unit,self.dollar_unit,self.item,self.relation)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,numerator,denominator,unit,dollar_unit,item,relation):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(numerator, denominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + "He gave %d out of the %d %s to his %s.<br><br>"%(numerator,denominator,item,relation)
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So, he gave&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">of the %s to his %s.</div>'%(item,relation)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        self.item = random.choice([["red toy cars","blue toy cars","toy cars","red"],["roses","lillies","flowers","roses"],
                                    ["big marbles","small marbles","marbles","big"]])
        self.TotalItem = randint(6,12)
        self.item1 = randint(3,self.TotalItem-2)
        self.item2 = self.TotalItem - self.item1
        
        self.problem = "%s has %d %s and %d %s. "%(self.name,self.item1,self.item[0],self.item2,self.item[1])
        self.problem = self.problem + "What fraction of his %s is %s?<br>"%(self.item[2],self.item[3])

        self.problem = self.problem + '<br><div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">(Type your answer as: If</div>'
        self.problem = self.problem + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;color:black;margin-top:-2px;"><p style="line-height:20%;text-align:center;color:black;">1<br>__<br></p>'
        self.problem = self.problem + '<p style="line-height:20%;text-align:center;color:black;">2<br></p></div>'
        self.problem = self.problem + '<div style="display:inline-block;vertical-align:top;margin-top:10px;font-size:0.8em;color:black;">then type as 1/2)</div>'
                          
        self.numerator = self.item1
        self.denominator = self.TotalItem
        self.answer = str(self.numerator) + " / " + str(self.denominator)
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.numerator,self.denominator,self.unit,self.dollar_unit,self.item1,self.item2,self.TotalItem,self.item[2],self.item[3])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,numerator,denominator,unit,dollar_unit,count1,count2,total,item2,item3):
        self.answer_text = "<br>The correct answer is:<br>%s"%(self.CreateFraction(numerator, denominator,"ffffff"))
       
        self.solution_text = "<font class='ExplanationFont'>"

        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(count1,count2,total)
        self.solution_text = self.solution_text + "He has %d %s altogether.<br><br><br>"%(total,item2)
        self.solution_text = self.solution_text + "%d out of his %d %s are %s.<br><br>"%(numerator,denominator,item2,item3)
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;">So,&nbsp;</div>'
        self.solution_text = self.solution_text + '<div style="width:40px;display:inline-block;vertical-align:top;margin-left:-7px;"><p style="line-height:20%;text-align:center;">'+str(numerator)+'<br>__<br></p>'
        self.solution_text = self.solution_text + '<p style="line-height:20%;text-align:center;"><br>'+str(denominator)+'</p></div>'
        self.solution_text = self.solution_text + '<div style="display:inline-block;vertical-align:top;margin-top:10px;margin-left:-5px;">of his %s is %s.</div>'%(item2,item3)

        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def CreateFraction(self,numerator,denominator,colorCode):
        #fraction = ""
        #fraction = fraction + '<div style="width:40px;display:inline-block;"><p style="line-height:20%;text-align:center;color:#'+colorCode+';">'+str(numerator)+'<br>__<br></p>'
        #fraction = fraction + '<p style="line-height:20%;text-align:center;color:#'+colorCode+';">'+str(denominator)+'</p></div>'
        
        fraction = ""
        fraction = fraction + "<table style='display:inline-block;padding:0 6px;'><tr style='padding: 0 5px;text-align: center;border-bottom: 1px solid;'><td>" + str(numerator) + "</td></tr> <tr><td>" + str(denominator) + "</td></tr></table>"
        
        return fraction

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