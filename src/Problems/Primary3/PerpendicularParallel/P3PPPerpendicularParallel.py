'''
Created on Feb 10, 2014
Module: P3PPPerpendicularParallel
Generates the Perpendicular, Parallel lines questions for Primary 3

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
  

History:
  
'''
import random

class P3PPPerpendicularParallel:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemTypeMCQ1",],2:["ProblemTypeMCQ5",],3:["ProblemTypeMCQ2",],4:["ProblemTypeMCQ6",],
                            5:["ProblemTypeMCQ3",],6:["ProblemTypeMCQ7",],7:["ProblemTypeMCQ4",],8:["ProblemTypeMCQ8",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemTypeMCQ1(),],2:[self.GenerateProblemTypeMCQ5(),],
                                    3:[self.GenerateProblemTypeMCQ2(),],4:[self.GenerateProblemTypeMCQ6(),],
                                    5:[self.GenerateProblemTypeMCQ3(),],6:[self.GenerateProblemTypeMCQ7(),],
                                    7:[self.GenerateProblemTypeMCQ4(),],8:[self.GenerateProblemTypeMCQ8(),],                               
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
        #return self.GenerateProblemTypeMCQ8()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),
                            "ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemTypeMCQ1(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3PP_Perpendicular_PT1a',"red","True"],['P3PP_Perpendicular_PT1b',"red","True"],['P3PP_Perpendicular_PT1c',"green","True"],
                       ['P3PP_Perpendicular_PT1d',"green","True"],['P3PP_Perpendicular_PT1e',"blue","False"],['P3PP_Perpendicular_PT1f',"blue","False"],
                       ['P3PP_Perpendicular_PT1g',"yellow","True"],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "The pair of %s colour lines are perpendicular to each other. True or False.<br><br>"%(self.ProblemImage[1])
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[2]
        self.answer1 = "True"
        self.answer2 = "False"
        self.value1 = self.answer1
        self.value2 = self.answer2
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[1],"cm")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2}

    def ExplainType1(self,problem,answer,unit,dollar_unit,length,unit2):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Coming Soon!!"
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ2(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3PP_Perpendicular_PT2a',["AB and EF","AB and CD","AB and GH"]],
                       ['P3PP_Perpendicular_PT2b',["AB and OZ","AB and OX","AB and OY"]],
                       ['P3PP_Perpendicular_PT2c',["AB and CD","CD and CE","AB and CE"]],
                       ['P3PP_Perpendicular_PT2d',["AB and CD","CB and CD","AB and BC"]],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Identify the pair of perpendicular lines in the given figure.<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1][0]
        self.answers = self.ProblemImage[1]
        random.shuffle(self.answers)
        self.answer1 = self.answers[0]
        self.answer2 = self.answers[1]
        self.answer3 = self.answers[2]
        self.value1 = self.answer1
        self.value2 = self.answer2
        self.value3 = self.answer3
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[1],"cm")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2,
                'answer3':self.answer3,'value3':self.value3}

    def ExplainType2(self,problem,answer,unit,dollar_unit,length,unit2):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Coming Soon!!"
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ3(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        
        self.images = [[['P3PP_A_PT3','P3PP_E_PT3','P3PP_F_PT3'],'A'],
                       [['P3PP_K_PT3','P3PP_H_PT3','P3PP_I_PT3'],'K'],
                       [['P3PP_V_PT3','P3PP_E_PT3','P3PP_I_PT3'],'V'],
                       [['P3PP_Y_PT3','P3PP_F_PT3','P3PP_T_PT3'],'Y'],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Which of the given letters doesn't have perpendicular lines.<br><br>"
        
        self.answer = "<div style='display:inline-block;margin-top:-20px;'><img src='/images/P3ProblemImages/"+self.ProblemImage[0][0]+".png'></div>"
        self.DisplayAnswer = self.ProblemImage[1]
        self.answers = self.ProblemImage[0]
        
        random.shuffle(self.answers)
        self.answer1 = "<div style='display:inline-block;margin-top:-20px;'><img src='/images/P3ProblemImages/"+self.answers[0]+".png'></div>"
        self.answer2 = "<div style='display:inline-block;margin-top:-20px;'><img src='/images/P3ProblemImages/"+self.answers[1]+".png'></div>"
        self.answer3 = "<div style='display:inline-block;margin-top:-20px;'><img src='/images/P3ProblemImages/"+self.answers[2]+".png'></div>"
        self.value1 = self.answer1
        self.value2 = self.answer2
        self.value3 = self.answer3
        
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.DisplayAnswer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2,
                'answer3':self.answer3,'value3':self.value3}

    def ExplainType3(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Coming Soon!!"
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ4(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.images = [['P3PP_Perpendicular_PT4a',['AB and BC','BC and CD','CD and AD']],
                       ['P3PP_Perpendicular_PT4b',['EA and AB','BC and CD','CD and DE']],
                       ['P3PP_Perpendicular_PT4c',['CB and BA','BA and AE','AE and ED']],
                       ['P3PP_Perpendicular_PT4d',['GF and FE','ED and DC','CB and BA']],
                       ]        
        self.ProblemImage = random.choice(self.images)
        self.problem = "Which pair of lines in the given figure are perpendicular to each other?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1][0]

        self.answers = self.ProblemImage[1]
        
        random.shuffle(self.answers)
        self.answer1 = self.answers[0]
        self.answer2 = self.answers[1]
        self.answer3 = self.answers[2]
        self.value1 = self.answer1
        self.value2 = self.answer2
        self.value3 = self.answer3
        
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2,
                'answer3':self.answer3,'value3':self.value3}

    def ExplainType4(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Coming Soon!!"
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ5(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3PP_Parallel_PT5a',"not parallel"],['P3PP_Parallel_PT5b',"parallel"],['P3PP_Parallel_PT5c',"parallel"],
                       ['P3PP_Parallel_PT5d',"not parallel"],['P3PP_Parallel_PT5e',"parallel"],['P3PP_Parallel_PT5f',"not parallel"],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "The following pair of lines are ________ to each other.<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
        self.answer1 = "not parallel"
        self.answer2 = "parallel"
        self.value1 = self.answer1
        self.value2 = self.answer2
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[1],"cm")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2}

    def ExplainType5(self,problem,answer,unit,dollar_unit,length,unit2):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Coming Soon!!"
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ6(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3PP_Parallel_PT6a',["AB and EF","GH and CD","CD and EF"]],
                       ['P3PP_Parallel_PT6b',["CD and GH","AB and EF","CD and AB"]],
                       ['P3PP_Parallel_PT6c',["AB and GH","GH and CD","CD and EF"]],
                       ['P3PP_Parallel_PT6d',["AB and GH","AB and CD","CD and EF"]],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Identify the pair of parallel lines in the given figure.<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1][0]
        self.answers = self.ProblemImage[1]
        random.shuffle(self.answers)
        self.answer1 = self.answers[0]
        self.answer2 = self.answers[1]
        self.answer3 = self.answers[2]
        self.value1 = self.answer1
        self.value2 = self.answer2
        self.value3 = self.answer3
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[1],"cm")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2,
                'answer3':self.answer3,'value3':self.value3}

    def ExplainType6(self,problem,answer,unit,dollar_unit,length,unit2):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Coming Soon!!"
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ7(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        
        self.images = [[['P3PP_E_PT3','P3PP_A_PT3','P3PP_K_PT3'],'E'],
                       [['P3PP_H_PT3','P3PP_K_PT3','P3PP_V_PT3'],'H'],
                       [['P3PP_I_PT3','P3PP_V_PT3','P3PP_T_PT3'],'I'],
                       [['P3PP_F_PT3','P3PP_Y_PT3','P3PP_T_PT3'],'F'],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Which of the given letters has a pair of parallel lines.<br><br>"
        
        self.answer = "<div style='display:inline-block;margin-top:-20px;'><img src='/images/P3ProblemImages/"+self.ProblemImage[0][0]+".png'></div>"
        self.DisplayAnswer = self.ProblemImage[1]
        self.answers = self.ProblemImage[0]
        
        random.shuffle(self.answers)
        self.answer1 = "<div style='display:inline-block;margin-top:-20px;'><img src='/images/P3ProblemImages/"+self.answers[0]+".png'></div>"
        self.answer2 = "<div style='display:inline-block;margin-top:-20px;'><img src='/images/P3ProblemImages/"+self.answers[1]+".png'></div>"
        self.answer3 = "<div style='display:inline-block;margin-top:-20px;'><img src='/images/P3ProblemImages/"+self.answers[2]+".png'></div>"
        self.value1 = self.answer1
        self.value2 = self.answer2
        self.value3 = self.answer3
        
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.DisplayAnswer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2,
                'answer3':self.answer3,'value3':self.value3}

    def ExplainType7(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Coming Soon!!"
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ8(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.images = [['P3PP_Parallel_PT8a',['BC and FE','BC and ED','CD and FE']],
                       ['P3PP_Parallel_PT8b',['AB and DE','AB and CD','AE and DC']],
                       ['P3PP_Parallel_PT8c',['AF and CD','AB and EF','CB and DE']],
                       ['P3PP_Parallel_PT8d',['AB and ED','AF and CD','BC and FE']],

                       ]        
        self.ProblemImage = random.choice(self.images)
        self.problem = "Which pair of lines in the given figure are parallel to each other?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1][0]

        self.answers = self.ProblemImage[1]
        
        random.shuffle(self.answers)
        self.answer1 = self.answers[0]
        self.answer2 = self.answers[1]
        self.answer3 = self.answers[2]
        self.value1 = self.answer1
        self.value2 = self.answer2
        self.value3 = self.answer3
        
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'value1':self.value1,'answer2':self.answer2,'value2':self.value2,
                'answer3':self.answer3,'value3':self.value3}

    def ExplainType8(self,problem,answer,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Coming Soon!!"
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return str(answer)==str(InputAnswer)
            except ValueError:
                return False                              