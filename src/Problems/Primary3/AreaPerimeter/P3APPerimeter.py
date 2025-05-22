'''
Created on Jan 24, 2014
Module: P3APPerimeter
Generates the Perimeter questions for Primary 3

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

class P3APPerimeter:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemTypeMCQ4",],
                            5:["ProblemTypeMCQ5",],6:["ProblemTypeMCQ6",],7:["ProblemTypeMCQ7",],8:["ProblemType8",],
                            9:["ProblemType9",],10:["ProblemType10",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],4:[self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemTypeMCQ5(),],6:[self.GenerateProblemTypeMCQ6(),],7:[self.GenerateProblemTypeMCQ7(),],
                                    8:[self.GenerateProblemType8(),],9:[self.GenerateProblemType9(),],10:[self.GenerateProblemType10(),],                                   
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
                            "ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10":self.GenerateProblemType10(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_Perimeter_PT1a_12',12,'cm'],['P3AP_Perimeter_PT1b_12',12,'cm'],['P3AP_Perimeter_PT1c_12',12,'cm'],
                       ['P3AP_Perimeter_PT1d_12',12,'cm'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the perimeter of the shaded figure below?<br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit1 = self.ProblemImage[2]
        self.unit = "%s"%(self.unit1)
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
        self.solution_text = self.solution_text + "The perimeter of a figure is the distance around it.<br><br>"
        self.solution_text = self.solution_text + "The perimeter of the given figure is <b>%d %s</b>.<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_Perimeter_PT2a_18',18,'m'],['P3AP_Perimeter_PT2b_16',16,'m'],['P3AP_Perimeter_PT2c_16',16,'m'],
                       ['P3AP_Perimeter_PT2d_18',18,'m'],['P3AP_Perimeter_PT2e_18',18,'m'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the perimeter of the shaded figure below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit1 = self.ProblemImage[2]
        self.unit = "%s"%(self.unit1)
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
        self.images = [['P3AP_Perimeter_PT3a_14',14,'cm'],['P3AP_Perimeter_PT3b_14',14,'cm'],['P3AP_Perimeter_PT3c_14',14,'cm'],
                       ['P3AP_Perimeter_PT3d_14',14,'cm'],['P3AP_Perimeter_PT3e_16',16,'cm'],['P3AP_Perimeter_PT3f_16',16,'cm'],]
        self.ProblemImage = random.choice(self.images)
        self.name = random.choice(PersonName.BoyName)
        self.problem1 = "%s makes a figure on a geoboard as shown below. Find the perimeter of the figure.<br><br>"%(self.name)
        self.problem2 = "%s uses a rubber band to form a figure on a grid. What is the perimeter of the figure?<br><br>"%(self.name)
        
        self.problem = random.choice([self.problem1,self.problem2])
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit1 = self.ProblemImage[2]
        self.unit = "%s"%(self.unit1)
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

    def GenerateProblemTypeMCQ4(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.images = [['P3AP_Perimeter_PT4a','False','blue','pink',18,16,"cm"],['P3AP_Perimeter_PT4b','False','blue','red',18,20,"cm"],['P3AP_Perimeter_PT4c','True','green','blue',18,18,"m"],['P3AP_Perimeter_PT4d','True','brown','blue',26,26,"cm"],
                       ]

        self.ProblemImage = random.choice(self.images)
        self.problem = "Do these figures have the same perimeter?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
        self.answer1 = "True"
        self.answer2 = "False"
        self.value1 = self.answer1
        self.value2 = self.answer2
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[2],self.ProblemImage[3],self.ProblemImage[4],self.ProblemImage[5],self.ProblemImage[6])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'answer2':self.answer2,
                'value1':self.value1,'value2':self.value2}

    def ExplainType4(self,problem,answer,unit,dollar_unit,first,second,count1,count2,unit2):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The perimeter of a figure is the distance around it.<br><br>"
        self.solution_text = self.solution_text + "The perimeter of the %s figure is %d %s.<br><br>"%(first,count1,unit2)
        self.solution_text = self.solution_text + "The perimeter of the %s figure is %d %s.<br><br>"%(second,count2,unit2)
        if answer=="True":
            self.solution_text = self.solution_text + "So, the two figures have the same perimeter.<br><br>"
        else:
            self.solution_text = self.solution_text + "So, the two figures do not have the same perimeter.<br><br>"
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ5(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.images = [['P3AP_Perimeter_PT5a_A','A',10,12,12],['P3AP_Perimeter_PT5b_C','C',12,12,10],['P3AP_Perimeter_PT5c_A','A',10,12,12],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Which of the figures below has the smallest perimeter?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = "Figure "+self.ProblemImage[1]
        self.answer1 = "Figure A"
        self.answer2 = "Figure B"
        self.answer3 = "Figure C"
        self.value1 = self.answer1
        self.value2 = self.answer2
        self.value3 = self.answer3
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[2],self.ProblemImage[3],self.ProblemImage[4])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'value1':self.value1,'value2':self.value2,'value3':self.value3}

    def ExplainType5(self,problem,answer,unit,dollar_unit,figureA,figureB,figureC):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The perimeter of a figure is the distance around it.<br><br>"
        self.solution_text = self.solution_text + "The perimeter of Figure A is %d cm.<br>"%(figureA)
        self.solution_text = self.solution_text + "The perimeter of Figure B is %d cm.<br>"%(figureB)
        self.solution_text = self.solution_text + "The perimeter of Figure C is %d cm.<br><br>"%(figureC)
        self.solution_text = self.solution_text + "So, the figure with the smallest perimeter is <b>%s</b>.<br><br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ6(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.images = [['P3AP_Perimeter_PT6a_B','B',12,16,14,"cm"],['P3AP_Perimeter_PT6b_A','A',18,12,10,"cm"],['P3AP_Perimeter_PT6c_C','C',12,12,14,"cm"],['P3AP_Perimeter_PT6d_A','A',14,12,10,"m"],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Which of the figures below has the greatest perimeter?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = "Figure "+self.ProblemImage[1]
        self.answer1 = "Figure A"
        self.answer2 = "Figure B"
        self.answer3 = "Figure C"
        self.value1 = self.answer1
        self.value2 = self.answer2
        self.value3 = self.answer3
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType3Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[2],self.ProblemImage[3],self.ProblemImage[4],self.ProblemImage[5])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'value1':self.value1,'value2':self.value2,'value3':self.value3}

    def ExplainType6(self,problem,answer,unit,dollar_unit,figureA,figureB,figureC,unit2):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The perimeter of a figure is the distance around it.<br><br>"
        self.solution_text = self.solution_text + "The perimeter of Figure A is %d %s.<br>"%(figureA,unit2)
        self.solution_text = self.solution_text + "The perimeter of Figure B is %d %s.<br>"%(figureB,unit2)
        self.solution_text = self.solution_text + "The perimeter of Figure C is %d %s.<br><br>"%(figureC,unit2)
        self.solution_text = self.solution_text + "So, the figure with the greatest perimeter is <b>%s</b>.<br><br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ7(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.images = [['P3AP_Perimeter_PT7a_12','A',12,12,16],['P3AP_Perimeter_PT7b_14','B',14,12,14],['P3AP_Perimeter_PT7c_16','B',16,14,16],['P3AP_Perimeter_PT7d_20','B',20,18,20],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Which of the figures below has perimeter of %d cm?<br><br>"%(self.ProblemImage[2])
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = "Figure "+self.ProblemImage[1]
        self.answer1 = "Figure A"
        self.answer2 = "Figure B"
        self.value1 = self.answer1
        self.value2 = self.answer2
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[2],self.ProblemImage[3],self.ProblemImage[4])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'answer2':self.answer2,
                'value1':self.value1,'value2':self.value2}

    def ExplainType7(self,problem,answer,unit,dollar_unit,count,countA,countB):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The perimeter of a figure is the distance around it.<br><br>"
        self.solution_text = self.solution_text + "The perimeter of Figure A is %d cm.<br>"%(countA)
        self.solution_text = self.solution_text + "The perimeter of Figure B is %d cm.<br><br>"%(countB)
        self.solution_text = self.solution_text + "So, the figure with a perimeter of %d cm is <b>%s</b>.<br><br>"%(count,answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_Perimeter_PT8a',8,'cm'],['P3AP_Perimeter_PT8b',8,'cm'],['P3AP_Perimeter_PT8c',9,'cm'],
                       ['P3AP_Perimeter_PT8d',9,'cm'],['P3AP_Perimeter_PT8e',7,'cm'],['P3AP_Perimeter_PT8f',7,'cm'],]

        self.ProblemImage = random.choice(self.images)
        
        self.problem = "Find the perimeter of the given square.<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = 4*self.ProblemImage[1]
                   
        self.unit1 = self.ProblemImage[2]
        self.unit = "%s"%(self.unit1)
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,unit,dollar_unit,length):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "A square has 4 sides of the same length.<br><br><br>"
        self.solution_text = self.solution_text + "Perimeter of square &nbsp;=&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d<br><br>"%(length,length,length,length)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_Perimeter_PT9a',9,6,'m'],['P3AP_Perimeter_PT9b',9,6,'m'],['P3AP_Perimeter_PT9c',9,7,'m'],
                       ['P3AP_Perimeter_PT9d',9,7,'m'],['P3AP_Perimeter_PT9e',8,5,'m'],['P3AP_Perimeter_PT9f',8,5,'m'],]
        self.ProblemImage = random.choice(self.images)
        
        self.problem = "Find the perimeter of the given rectangle.<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = 2*(self.ProblemImage[1]+self.ProblemImage[2])
                   
        self.unit1 = self.ProblemImage[3]
        self.unit = "%s"%(self.unit1)
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[1],self.ProblemImage[2])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,unit,dollar_unit,length,breadth):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Perimeter of rectangle &nbsp;=&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d &nbsp;+&nbsp; %d<br><br>"%(length,breadth,length,breadth)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_Perimeter_PT10a',[5,5,6,8,6],'cm'],['P3AP_Perimeter_PT10b',[6,4,6,6,4],'cm'],
                       ['P3AP_Perimeter_PT10c',[3,5,5,7,8],'cm'],['P3AP_Perimeter_PT10d',[3,2,3,3,2,3],'cm'],]

        self.ProblemImage = random.choice(self.images)
        
        self.problem = "Find the perimeter of the given figure.<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = 0
        for i in range(len(self.ProblemImage[1])):
            self.answer = self.answer + self.ProblemImage[1][i]
                   
        self.unit1 = self.ProblemImage[2]
        self.unit = "%s"%(self.unit1)
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,unit,dollar_unit,count):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "The perimeter of a figure is the distance around it.<br><br>"
        self.solution_text = self.solution_text + "Perimeter of the given figure &nbsp;=&nbsp; %d"%(count[0])
        for i in range(len(count)-1):
            self.solution_text = self.solution_text + " &nbsp;+&nbsp; %d"%(count[i+1])

        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "So, the perimeter of the given figure is <b>%d %s</b>.<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswer == 2:    
            try:
                return str(answer)==str(InputAnswer)
            except ValueError:
                return False            