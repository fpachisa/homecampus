'''
Created on Jan 18, 2014
Module: P3APSquareCmM
Generates the Area in cm & m square for Primary 3

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
  

History:
  
'''
import random

class P3APSquareCmM:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemType4",],
                            5:["ProblemType5",],6:["ProblemTypeMCQ6",],7:["ProblemTypeMCQ7",],8:["ProblemTypeMCQ8",],
                            9:["ProblemTypeMCQ9",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],4:[self.GenerateProblemType4(),],
                                    5:[self.GenerateProblemType5(),],6:[self.GenerateProblemTypeMCQ6(),],7:[self.GenerateProblemTypeMCQ7(),],
                                    8:[self.GenerateProblemTypeMCQ8(),],9:[self.GenerateProblemTypeMCQ9(),],                                   
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
        #return self.GenerateProblemTypeMCQ9()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemTypeMCQ6":self.GenerateProblemTypeMCQ6(),
                            "ProblemTypeMCQ7":self.GenerateProblemTypeMCQ7(),
                            "ProblemTypeMCQ8":self.GenerateProblemTypeMCQ8(),
                            "ProblemTypeMCQ9":self.GenerateProblemTypeMCQ9(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3CmM_PT1_5_a','5'],['P3CmM_PT1_5_b','5'],['P3CmM_PT1_6_a','6'],['P3CmM_PT1_6_b','6'],
                       ['P3CmM_PT1_7_a','7'],['P3CmM_PT1_7_b','7'],]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "cm<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit,"cm")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,unit,dollar_unit,unit2):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Number of shaded squares in the figure &nbsp;=&nbsp; %s<br><br>"%(answer)
        self.solution_text = self.solution_text + "The figure is made up of &nbsp;<b>%s</b>&nbsp; 1-%s squares.<br><br>"%(answer,unit2)
        self.solution_text = self.solution_text + "The area of each 1-%s square is 1 %s.<br><br>"%(unit2,unit)
        self.solution_text = self.solution_text + "So, the area of the shaded figure is <b>%s %s</b>.<br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3CmM_PT2_7_a','7'],['P3CmM_PT2_8_a','8'],['P3CmM_PT2_9_a','9'],['P3CmM_PT2_10_a','10'],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "m<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit,"m")
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
        self.images = [['P3CmM_PT3_8_a','8','m'],['P3CmM_PT3_10_a','10','cm'],['P3CmM_PT3_10_b','10','m'],['P3CmM_PT3_12_a','12','cm'],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "%s<sup>2</sup>"%(self.ProblemImage[2])
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[2])
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
        self.images = [['P3CmM_PT4_9_a','9','cm','2'],['P3CmM_PT4_10_a','10','m','4'],['P3CmM_PT4_11_a','11','m','4'],['P3CmM_PT4_12_a','12','cm','4'],
                       ]
        
        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "%s<sup>2</sup>"%(self.ProblemImage[2])
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[2],self.ProblemImage[3])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,unit,dollar_unit,unit2,halfSquares):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Number of full shaded squares in the figure &nbsp;=&nbsp; %d<br><br>"%(int(answer)-int(halfSquares)/2)
        if int(halfSquares)/2==1:
            self.solution_text = self.solution_text + "Number of half shaded squares in the figure &nbsp;=&nbsp; %s &nbsp;=&nbsp; %s full shaded square<br><br>"%(int(halfSquares),int(halfSquares)/2)
        else:
            self.solution_text = self.solution_text + "Number of half shaded squares in the figure &nbsp;=&nbsp; %s &nbsp;=&nbsp; %s full shaded squares<br><br>"%(int(halfSquares),int(halfSquares)/2)
        self.solution_text = self.solution_text + "Total number of shaded squares in the figure &nbsp;=&nbsp; %s &nbsp;+&nbsp; %s &nbsp;=&nbsp; %s<br><br>"%(int(answer)-int(halfSquares)/2,int(halfSquares)/2,answer)
        self.solution_text = self.solution_text + "The figure is made up of &nbsp;<b>%s</b>&nbsp; 1-%s squares.<br><br>"%(answer,unit2)
        self.solution_text = self.solution_text + "So, the area of the shaded figure is <b>%s %s</b>.<br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3CmM_PT5_11_a','11','cm','2'],['P3CmM_PT5_11_b','11','cm','4'],['P3CmM_PT5_11_c','11','m','4'],['P3CmM_PT5_12_a','12','m','4'],
                       ]

        self.ProblemImage = random.choice(self.images)
        self.problem = "What is the area of the shaded figure below?<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1]
                   
        self.unit = "%s<sup>2</sup>"%(self.ProblemImage[2])
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[2],self.ProblemImage[3])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def GenerateProblemTypeMCQ6(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.images = [['P3CmM_PT6_a','B','5','7','6'],['P3CmM_PT6_b','A','6','5','4'],['P3CmM_PT6_c','C','6','5','7'],['P3CmM_PT6_d','A','7','5','5'],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Which of the figures below has the greatest area?<br><br>"
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
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[2],self.ProblemImage[3],self.ProblemImage[4])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'value1':self.value1,'value2':self.value2,'value3':self.value3}

    def ExplainType6(self,problem,answer,unit,dollar_unit,squaresA,squaresB,squaresC):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Number of shaded squares in Figure A &nbsp;=&nbsp; %s<br>"%(squaresA)
        self.solution_text = self.solution_text + "Area of Figure A is %s cm<sup>2</sup>.<br><br>"%(squaresA)
        self.solution_text = self.solution_text + "Number of shaded squares in Figure B &nbsp;=&nbsp; %s<br>"%(squaresB)
        self.solution_text = self.solution_text + "Area of Figure B is %s cm<sup>2</sup>.<br><br>"%(squaresB)
        self.solution_text = self.solution_text + "Number of shaded squares in Figure C &nbsp;=&nbsp; %s<br>"%(squaresC)
        self.solution_text = self.solution_text + "Area of Figure C is %s cm<sup>2</sup>.<br><br>"%(squaresC)
        self.solution_text = self.solution_text + "So, <b>%s</b> has the greatest area.<br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ7(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.images = [['P3CmM_PT7_a','C','6','6','5'],['P3CmM_PT7_b','C','6','6','5'],['P3CmM_PT7_c','A','6','7','7'],['P3CmM_PT7_d','B','8','7','8'],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Which of the figures below has the smallest area?<br><br>"
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
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[2],self.ProblemImage[3],self.ProblemImage[4])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'value1':self.value1,'value2':self.value2,'value3':self.value3}

    def ExplainType7(self,problem,answer,unit,dollar_unit,squaresA,squaresB,squaresC):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Number of shaded squares in Figure A &nbsp;=&nbsp; %s<br>"%(squaresA)
        self.solution_text = self.solution_text + "Area of Figure A is %s m<sup>2</sup>.<br><br>"%(squaresA)
        self.solution_text = self.solution_text + "Number of shaded squares in Figure B &nbsp;=&nbsp; %s<br>"%(squaresB)
        self.solution_text = self.solution_text + "Area of Figure B is %s m<sup>2</sup>.<br><br>"%(squaresB)
        self.solution_text = self.solution_text + "Number of shaded squares in Figure C &nbsp;=&nbsp; %s<br>"%(squaresC)
        self.solution_text = self.solution_text + "Area of Figure C is %s m<sup>2</sup>.<br><br>"%(squaresC)
        self.solution_text = self.solution_text + "So, <b>%s</b> has the smallest area.<br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ8(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.images = [['P3CmM_PT6_a','7','cm','B','5','7','6'],['P3CmM_PT6_b','6','cm','A','6','5','4'],['P3CmM_PT6_c','7','cm','C','6','5','7'],['P3CmM_PT6_d','7','cm','A','7','5','5'],
                       ['P3CmM_PT7_a','5','m','C','6','6','5'],['P3CmM_PT7_b','5','m','C','6','6','5'],['P3CmM_PT7_c','6','m','A','6','7','7'],['P3CmM_PT7_d','7','m','B','8','7','8'],
                       ]

        self.ProblemImage = random.choice(self.images)
        self.problem = "Which figure has an area of %s %s<sup>2</sup>?<br><br>"%(self.ProblemImage[1],self.ProblemImage[2])
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = "Figure "+self.ProblemImage[3]
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
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[1],self.ProblemImage[2],self.ProblemImage[4],self.ProblemImage[5],self.ProblemImage[6])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'value1':self.value1,'value2':self.value2,'value3':self.value3}

    def ExplainType8(self,problem,answer,unit,dollar_unit,area,unit2,squaresA,squaresB,squaresC):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Number of shaded squares in Figure A &nbsp;=&nbsp; %s<br>"%(squaresA)
        self.solution_text = self.solution_text + "Area of Figure A is %s %s<sup>2</sup>.<br><br>"%(squaresA,unit2)
        self.solution_text = self.solution_text + "Number of shaded squares in Figure B &nbsp;=&nbsp; %s<br>"%(squaresB)
        self.solution_text = self.solution_text + "Area of Figure B is %s %s<sup>2</sup>.<br><br>"%(squaresB,unit2)
        self.solution_text = self.solution_text + "Number of shaded squares in Figure C &nbsp;=&nbsp; %s<br>"%(squaresC)
        self.solution_text = self.solution_text + "Area of Figure C is %s %s<sup>2</sup>.<br><br>"%(squaresC,unit2)
        self.solution_text = self.solution_text + "So, <b>%s</b> has an area of %s %s<sup>2</sup>.<br>"%(answer,area,unit2)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemTypeMCQ9(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.areas = [["a football field",7140,"m","A football field that has an area of 7140 cm<sup>2</sup> would be too small to play on!"],
                      ["an olympic size pool",1250,"m","A pool that has an area of 1250 cm<sup>2</sup> would be too small to swim in!"],
                      ["the top of a study desk",6400,"cm","A study desk top that is 6400 m<sup>2</sup> in area would be too big to fit in a room! Go ahead and measure the sides of the top of your study desk."],
                      ["a home TV screen",4500,"cm","A TV screen that has an area of 4500 m<sup>2</sup> would be too big to fit inside a house! Go ahead and measure the length and width of the TV screen in your home."],
                      ["a classroom floor",81,"m","It's normal for a classroom floor to be 9 m by 9 m. That is an area of 81 m<sup>2</sup>!"],
                      ["a door mat",1000,"cm","A door mat that has an area of 1000 m<sup>2</sup> would be really really huge!"]]
        
        self.area = random.choice(self.areas)
        
        self.problem = "The area of %s is %d ____. Choose the correct unit."%(self.area[0],self.area[1])
        
        self.answer = "%s<sup>2</sup>"%(self.area[2])
        self.answer1 = "cm<sup>2</sup>"
        self.answer2 = "m<sup>2</sup>"
        self.value1 = self.answer1
        self.value2 = self.answer2
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "MCQType2Choices.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.unit,self.dollar_unit,self.area[3])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemTypeMCQ9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'answer1':self.answer1,'answer2':self.answer2,'value1':self.value1,'value2':self.value2}

    def ExplainType9(self,problem,answer,unit,dollar_unit,explanation):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%s<br>"%(explanation)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        if CheckAnswer == 2:
            try:
                return answer==InputAnswer
            except ValueError:
                return False                                