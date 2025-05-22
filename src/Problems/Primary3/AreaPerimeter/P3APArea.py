'''
Created on Jan 22, 2014
Module: P3APArea
Generates the Area questions for Primary 3

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

class P3APArea:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemType4",],
                            5:["ProblemType5",],6:["ProblemType6",],7:["ProblemType7",],8:["ProblemType8",],
                            9:["ProblemType9",],10:["ProblemType10",],11:["ProblemType11",],
                            12:["ProblemType12",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],4:[self.GenerateProblemType4(),],
                                    5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],7:[self.GenerateProblemType7(),],
                                    8:[self.GenerateProblemType8(),],9:[self.GenerateProblemType9(),],
                                    10:[self.GenerateProblemType10(),],11:[self.GenerateProblemType11(),],
                                    12:[self.GenerateProblemType12(),],                                   
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
                            "ProblemType10":self.GenerateProblemType10(),
                            "ProblemType11":self.GenerateProblemType11(),
                            "ProblemType12":self.GenerateProblemType12(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_Area_PT1a',8],['P3AP_Area_PT1b',8],['P3AP_Area_PT1c',9],['P3AP_Area_PT1d',9],
                       ['P3AP_Area_PT1e',7],['P3AP_Area_PT1f',7],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Find the area of the given square.<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1] * self.ProblemImage[1]
                   
        self.unit = "cm<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[1],"cm")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,unit,dollar_unit,length,unit2):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of square &nbsp;=&nbsp; Length of side &nbsp;&times;&nbsp; Length of side<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s &nbsp;&times;&nbsp; %d %s<br><br>"%(length,unit2,length,unit2)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s<sup>2</sup><br>"%(answer,unit2)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_Area_PT2a',9,6],['P3AP_Area_PT2b',9,6],['P3AP_Area_PT2c',9,7],['P3AP_Area_PT2d',9,7],
                       ['P3AP_Area_PT2e',8,5],['P3AP_Area_PT2f',8,5],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "Find the area of the given rectangle.<br><br>"
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[1] * self.ProblemImage[2]
                   
        self.unit = "m<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[1],self.ProblemImage[2],"m")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,unit,dollar_unit,length,breadth,unit2):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of rectangle &nbsp;=&nbsp; Length &nbsp;&times;&nbsp; Breadth<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s &nbsp;&times;&nbsp; %d %s<br><br>"%(length,unit2,breadth,unit2)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s<sup>2</sup><br>"%(answer,unit2)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.side = randint(4,9)
        self.unit1 = random.choice(["cm","m"])
        self.problem = "What is the area of a square of side %d %s?"%(self.side,self.unit1)
        
        self.answer = self.side * self.side
                   
        self.unit = "%s<sup>2</sup>"%(self.unit1)
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit,self.dollar_unit,self.side,self.unit1)
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
        
        self.length = randint(5,9)
        self.breadth = self.length - 2
        
        self.unit1 = random.choice(["cm","m"])
        self.problem = "A rectangle has sides of %d %s and %d %s. What is the area of the rectangle?"%(self.length,self.unit1,self.breadth,self.unit1)
        
        self.answer = self.length * self.breadth
                   
        self.unit = "%s<sup>2</sup>"%(self.unit1)
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.dollar_unit,self.length,self.breadth,self.unit1)
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
        self.images = [['P3AP_Area_PT5a','','The figure below shows a rectangular field.','Find the area of the field.',9,6,'m','The area of the field is'],
                       ['P3AP_Area_PT5b',random.choice(PersonName.GirlName),' wants to hang the rug shown below on a wall.','What area of the wall will the rug cover?',7,5,'m','The rug will cover an area of'],
                       ['P3AP_Area_PT5c',random.choice(PersonName.GirlName),' makes a miniature painting shown below.','What is the area of the painting?',9,8,'cm','The painting has an area of'],
                       ['P3AP_Area_PT5d',random.choice(PersonName.GirlName),' hangs the frame shown below on her bedroom wall.','What area of the wall does the frame cover?',9,8,'cm','The frame covers an area of'],
                       ['P3AP_Area_PT5e',random.choice(PersonName.GirlName),' wants to build a wall as shown below.','What will be the area of the wall she builds?',9,6,'m','The area of the wall will be'],
                       ['P3AP_Area_PT5f','','The figure below shows a swimming pool.','Find the area it covers.',9,6,'m','The swimming pool covers an area of'],
                       ['P3AP_Area_PT5g','','The poster below is hung on a billboard.','Find the area of the billboard it covers.',4,3,'m','The area of the billboard covered by it is'],
                       ]
        self.ProblemImage = random.choice(self.images)
        self.problem = "%s %s %s<br><br>"%(self.ProblemImage[1],self.ProblemImage[2],self.ProblemImage[3],)
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[4] * self.ProblemImage[5]
        self.unit1 = self.ProblemImage[6]
                   
        self.unit = "%s<sup>2</sup>"%(self.unit1)
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[4],self.ProblemImage[5],self.unit1,self.ProblemImage[7])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,unit,dollar_unit,length,breadth,unit2,finalStatement):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of rectangle &nbsp;=&nbsp; Length &nbsp;&times;&nbsp; Breadth<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s &nbsp;&times;&nbsp; %d %s<br><br>"%(length,unit2,breadth,unit2)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s<sup>2</sup><br><br>"%(answer,unit2)
        self.solution_text = self.solution_text + "%s %d %s<sup>2</sup>.<br><br>"%(finalStatement,answer,unit2)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.name = random.choice(PersonName.GirlName)
        self.side = randint(4,9)
        self.item = random.choice(["cloth","paper"])
        
        self.problem = "%s cut out a %d-cm square from a piece of %s. Find the area of the square she cut out."%(self.name,self.side,self.item)
        
        self.answer = self.side * self.side
                   
        self.unit = "cm<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit,self.side)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,unit,dollar_unit,length):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of square &nbsp;=&nbsp; Length of side &nbsp;&times;&nbsp; Length of side<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d cm &nbsp;&times;&nbsp; %d cm<br><br>"%(length,length)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "The area of the square she cut out is %d %s.<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.name = random.choice(PersonName.BoyName)
        self.length = randint(5,9)
        self.breadth = self.length - randint(1,3)
        self.item = random.choice([["piece of wood","wood"],["piece of glass","glass"],["of wall","wall"]])
        
        self.problem = "%s painted a %d m by %d m %s. What is the area of the %s he painted?"%(self.name,self.length,self.breadth,self.item[0],self.item[1])
        
        self.answer = self.length * self.breadth
                   
        self.unit = "m<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.dollar_unit,self.length,self.breadth,self.item[1])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,unit,dollar_unit,length,breadth,item):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of rectangle &nbsp;=&nbsp; Length &nbsp;&times;&nbsp; Breadth<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d m &nbsp;&times;&nbsp; %d m<br><br>"%(length,breadth)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d m<sup>2</sup><br><br>"%(answer)
        self.solution_text = self.solution_text + "The area of the %s he painted is %d m<sup>2</sup>.<br><br>"%(item,answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.side = randint(3,9)
        
        self.problem = "The length of one side of a square sheet of paper is %d cm. What is the area of the sheet of paper?"%(self.side)
        
        self.answer = self.side * self.side
                   
        self.unit = "cm<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.unit,self.dollar_unit,self.side)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,unit,dollar_unit,length):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of square &nbsp;=&nbsp; Length of side &nbsp;&times;&nbsp; Length of side<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d cm &nbsp;&times;&nbsp; %d cm<br><br>"%(length,length)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "The area of the sheet of paper is %d %s.<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.name = random.choice(PersonName.GirlName)
        self.length = randint(5,9)
        self.breadth = self.length - randint(1,3)
        
        self.problem = "%s mowed her garden. The garden has sides of %d m and %d m. What is the area of the garden?"%(self.name,self.length,self.breadth)
        
        self.answer = self.length * self.breadth
                   
        self.unit = "m<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.unit,self.dollar_unit,self.length,self.breadth)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,unit,dollar_unit,length,breadth):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of rectangle &nbsp;=&nbsp; Length &nbsp;&times;&nbsp; Breadth<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d m &nbsp;&times;&nbsp; %d m<br><br>"%(length,breadth)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d m<sup>2</sup><br><br>"%(answer)
        self.solution_text = self.solution_text + "The area of the garden is %d m<sup>2</sup>.<br><br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.side = randint(3,9)
        
        self.problem = "A square sheet of pastry is %d cm long. Find the area of the sheet of pastry."%(self.side)
        
        self.answer = self.side * self.side
                   
        self.unit = "cm<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.unit,self.dollar_unit,self.side)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,unit,dollar_unit,length):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of square &nbsp;=&nbsp; Length of side &nbsp;&times;&nbsp; Length of side<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d cm &nbsp;&times;&nbsp; %d cm<br><br>"%(length,length)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "The area of the sheet of pastry is %d %s.<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.side = randint(3,9)
        
        self.problem = "The length of a square plate is %d cm. What is the area of the plate?"%(self.side)
        
        self.answer = self.side * self.side
                   
        self.unit = "cm<sup>2</sup>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.unit,self.dollar_unit,self.side)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,unit,dollar_unit,length):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of square &nbsp;=&nbsp; Length of side &nbsp;&times;&nbsp; Length of side<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d cm &nbsp;&times;&nbsp; %d cm<br><br>"%(length,length)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "The area of the square plate is %d %s.<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType12(self):       
        '''e.g.:'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        '''PT1 = Problem Type 1, first number stands for answer'''
        self.images = [['P3AP_Area_PT12a','drew a rectangle in the sand','rectangle he drew',7,5,'m'],
                       ['P3AP_Area_PT12b','dyed a piece of cloth','cloth he dyed',8,6,'cm'],
                       ['P3AP_Area_PT12c','painted a glass window','glass window he painted',9,5,'m'],
                       ]
        self.name = random.choice(PersonName.BoyName)
        self.ProblemImage = random.choice(self.images)
        
        self.problem = "%s %s. What is the area of the %s?<br><br>"%(self.name,self.ProblemImage[1],self.ProblemImage[2])
        self.problem = self.problem + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/images/P3ProblemImages/"+self.ProblemImage[0]+".png'>"
        
        self.answer = self.ProblemImage[3] * self.ProblemImage[4]
        
        self.unit1 = self.ProblemImage[5]           
        self.unit = "%s<sup>2</sup>"%(self.unit1)
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.unit,self.dollar_unit,self.ProblemImage[3],self.ProblemImage[4],self.ProblemImage[2],self.unit1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType12(self,problem,answer,unit,dollar_unit,length,breadth,item,unit2):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
       
        self.solution_text = "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Area of rectangle &nbsp;=&nbsp; Length &nbsp;&times;&nbsp; Breadth<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s &nbsp;&times;&nbsp; %d %s<br><br>"%(length,unit2,breadth,unit2)
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp; %d %s<br><br>"%(answer,unit)
        self.solution_text = self.solution_text + "The area of the %s is %d %s.<br><br>"%(item,answer,unit)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False                              