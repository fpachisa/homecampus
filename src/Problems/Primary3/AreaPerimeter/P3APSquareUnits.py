'''
Created on Jan 16, 2014
Module: P3APSquareUnits
Generates the Area in square units for Primary 3

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
import logging

class P3APSquareUnits:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemType4",],
                            5:["ProblemType5",],6:["ProblemType6",],7:["ProblemType7",],8:["ProblemType8",],
                            9:["ProblemType9",],10:["ProblemType10",],11:["ProblemType11",],12:["ProblemType12",],
                            13:["ProblemType13",],14:["ProblemType14",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],9:[self.GenerateProblemType9(),],
                                    10:[self.GenerateProblemType10(),],11:[self.GenerateProblemType11(),],12:[self.GenerateProblemType12(),],
                                    13:[self.GenerateProblemType13(),],14:[self.GenerateProblemType14(),],                                  
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
        #return self.GenerateProblemType14()
        
    def GenerateTestProblem(self,problem_type):
        logging.info(problem_type)
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10":self.GenerateProblemType10(),
                            "ProblemType11":self.GenerateProblemType11(),
                            "ProblemType12":self.GenerateProblemType12(),
                            "ProblemType13":self.GenerateProblemType13(),
                            "ProblemType14":self.GenerateProblemType14(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT1_5_a','5'],['P3AP_PT1_5_b','5'],['P3AP_PT1_6_a','6'],['P3AP_PT1_6_b','6'],['P3AP_PT1_7_a','7'],['P3AP_PT1_7_b','7'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Number of shaded squares in the figure &nbsp;=&nbsp; %s<br><br>"%(answer)
        self.solution_text = self.solution_text + "Area of the shaded figure &nbsp;=&nbsp; %s %s<br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT2_7_a','7'],['P3AP_PT2_7_b','7'],['P3AP_PT2_8_a','8'],['P3AP_PT2_8_b','8'],['P3AP_PT2_8_c','8'],
                       ['P3AP_PT2_9_a','9'],['P3AP_PT2_9_b','9'],['P3AP_PT2_9_c','9'],['P3AP_PT2_10_a','10'],['P3AP_PT2_10_b','10'],['P3AP_PT2_10_c','10'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def GenerateProblemType3(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT3_10_a','10'],['P3AP_PT3_10_b','10'],['P3AP_PT3_11_a','11'],['P3AP_PT3_11_b','11'],
                       ['P3AP_PT3_12_a','12'],['P3AP_PT3_12_b','12'],['P3AP_PT3_13_a','13'],['P3AP_PT3_13_b','13'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def GenerateProblemType4(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT4_12_a','12'],['P3AP_PT4_12_b','12'],['P3AP_PT4_13_a','13'],['P3AP_PT4_13_b','13'],
                       ['P3AP_PT4_14_a','14'],['P3AP_PT4_14_b','14'],['P3AP_PT4_15_a','15'],['P3AP_PT4_15_b','15'],
                       ['P3AP_PT4_16_a','16'],['P3AP_PT4_16_b','16'],['P3AP_PT4_17_a','17'],['P3AP_PT4_17_b','17'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def GenerateProblemType5(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT5_15_a','15'],['P3AP_PT5_15_b','15'],['P3AP_PT5_16_a','16'],['P3AP_PT5_16_b','16'],
                       ['P3AP_PT5_17_a','17'],['P3AP_PT5_17_b','17'],['P3AP_PT5_18_a','18'],['P3AP_PT5_18_b','18'],
                       ['P3AP_PT5_19_a','19'],['P3AP_PT5_19_b','19'],['P3AP_PT5_20_a','20'],['P3AP_PT5_20_b','20'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def GenerateProblemType6(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT6_4_a','4'],['P3AP_PT6_4_b','4'],['P3AP_PT6_5_a','5'],['P3AP_PT6_5_b','5'],['P3AP_PT6_6_a','6'],['P3AP_PT6_6_b','6'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Number of full shaded squares in the figure &nbsp;=&nbsp; %d<br><br>"%(int(answer)-1)
        self.solution_text = self.solution_text + "Number of half shaded squares in the figure &nbsp;=&nbsp; 2 &nbsp;=&nbsp; 1 full square<br><br>"
        self.solution_text = self.solution_text + "Total number of shaded squares in the figure &nbsp;=&nbsp; %s<br><br>"%(answer)
        self.solution_text = self.solution_text + "Area of the shaded figure &nbsp;=&nbsp; %s %s<br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT7_5_a','5'],['P3AP_PT7_6_a','6'],['P3AP_PT7_7_a','7'],['P3AP_PT7_8_a','8'],['P3AP_PT7_9_a','9'],['P3AP_PT7_10_a','10'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def GenerateProblemType8(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT8_9_a','9'],['P3AP_PT8_10_a','10'],['P3AP_PT8_11_a','11'],['P3AP_PT8_12_a','12'],['P3AP_PT8_13_a','13'],['P3AP_PT8_14_a','14'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def GenerateProblemType9(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT9_12_a','12'],['P3AP_PT9_13_a','13'],['P3AP_PT9_14_a','14'],['P3AP_PT9_15_a','15'],['P3AP_PT9_16_a','16'],['P3AP_PT9_17_a','17'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit)
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
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT10_16_a','16'],['P3AP_PT10_17_a','17'],['P3AP_PT10_18_a','18'],['P3AP_PT10_19_a','19'],['P3AP_PT10_20_a','20'],['P3AP_PT10_21_a','21'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def GenerateProblemType11(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT11_12_a','12','green','yellow','5','7'],['P3AP_PT11_13_a','13','pink','green','5','8'],['P3AP_PT11_14_a','14','light blue','dark blue','6','8'],['P3AP_PT11_16_a','16','blue','pink','7','9'],['P3AP_PT11_18_a','18','orange','blue','8','10'],['P3AP_PT11_18_b','18','yellow','purple','9','9'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the total area of the two shaded figures given below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
        firstColour = self.ProblemImage[2]
        secondColour = self.ProblemImage[3]
        firstArea = self.ProblemImage[4]
        secondArea = self.ProblemImage[5]
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.unit,self.dollar_unit,firstColour,secondColour,firstArea,secondArea)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,unit,dollar_unit,firstColour,secondColour,firstArea,secondArea):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of the %s figure &nbsp;=&nbsp; %s<br><br>"%(firstColour,firstArea)
        self.solution_text = self.solution_text + "Area of the %s figure &nbsp;=&nbsp; %s<br><br>"%(secondColour,secondArea)
        self.solution_text = self.solution_text + "Total area of the 2 shaded figures &nbsp;=&nbsp; %s &nbsp;+&nbsp; %s &nbsp;=&nbsp; %s %s<br><br>"%(firstArea,secondArea,answer,unit)
        self.solution_text = self.solution_text + "</font>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType12(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT12_11_a','11','purple','red','5','6'],['P3AP_PT12_12_a','12','blue','pink','5','7'],['P3AP_PT12_13_a','13','yellow','pink','7','6'],['P3AP_PT12_14_a','14','blue','pink','8','6'],['P3AP_PT12_14_b','14','green','blue','6','8'],['P3AP_PT12_14_c','14','blue','green','7','7'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the total area of the two shaded figures given below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
        firstColour = self.ProblemImage[2]
        secondColour = self.ProblemImage[3]
        firstArea = self.ProblemImage[4]
        secondArea = self.ProblemImage[5]
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.unit,self.dollar_unit,firstColour,secondColour,firstArea,secondArea)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def GenerateProblemType13(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT5_15_a','15'],['P3AP_PT5_15_b','15'],['P3AP_PT5_16_a','16'],['P3AP_PT5_16_b','16'],
                       ['P3AP_PT5_17_a','17'],['P3AP_PT5_17_b','17'],['P3AP_PT5_18_a','18'],['P3AP_PT5_18_b','18'],
                       ['P3AP_PT5_19_a','19'],['P3AP_PT5_19_b','19'],['P3AP_PT5_20_a','20'],['P3AP_PT5_20_b','20'],]
        self.ProblemImage = random.choice(self.images)
        self.Area = int(self.ProblemImage[1])
        self.add = randint(2,4)
        self.FinalArea = self.Area + self.add
        self.problem = "How many square units should be added to the shaded figure below to change its area to %d square units?<br><br>"%(self.FinalArea)
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.add
                   
        self.unit = "square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.unit,self.dollar_unit,self.Area,self.FinalArea)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType13(self,problem,answer,unit,dollar_unit,area,finalArea):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of the shaded figure &nbsp;=&nbsp; %d %s<br><br>"%(area,unit)
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(finalArea,area,answer)
        self.solution_text = self.solution_text + "%d %s should be added to the shaded figure to change its area to %d %s.<br><br>"%(answer,unit,finalArea,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType14(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_PT10_16_a','16'],['P3AP_PT10_17_a','17'],['P3AP_PT10_18_a','18'],['P3AP_PT10_19_a','19'],['P3AP_PT10_20_a','20'],['P3AP_PT10_21_a','21'],]
        self.ProblemImage = random.choice(self.images)
        self.Area = int(self.ProblemImage[1])
        self.add = randint(2,4)
        self.FinalArea = self.Area + self.add
        self.problem = "How many half-square units should be added to the figure below to change its area to %d square units?<br><br>"%(self.FinalArea)
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.add * 2
                   
        self.unit = "half-square units"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.unit,self.dollar_unit,self.Area,self.FinalArea)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType14(self,problem,answer,unit,dollar_unit,area,finalArea):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of the shaded figure &nbsp;=&nbsp; %d square units<br><br>"%(area)
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d square units<br><br>"%(finalArea,area,finalArea-area)
        self.solution_text = self.solution_text + "%d square units &nbsp;&times;&nbsp; 2 &nbsp;=&nbsp; %d half-square units<br><br>"%(finalArea-area,answer)
        self.solution_text = self.solution_text + "%d %s should be added to the shaded figure to change its area to %d square units.<br><br>"%(answer,unit,finalArea)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False                    