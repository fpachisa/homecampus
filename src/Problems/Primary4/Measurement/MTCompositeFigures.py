'''
Created on Oct 23, 2012

Module: MTCompositeFigures
Generates "Finding area/perimeter of a composite figures" problems for Primary 4

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''
import random
from random import randint

class MTCompositeFigures:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        #return self.GenerateProblemType7()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''                
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            3:["ProblemType5",],
                            4:["ProblemType6",],
                            5:["ProblemType3",],
                            6:["ProblemType4",],
                            7:["ProblemType7",],
                            8:["ProblemType8",],

                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType5(),],
                                    4:[self.GenerateProblemType6(),],
                                    5:[self.GenerateProblemType3()],
                                    6:[self.GenerateProblemType4(),],
                                    7:[self.GenerateProblemType7(),],
                                    8:[self.GenerateProblemType8(),],                                    
                                    }
        
        #Creating one more problem type so it creates a list and not a list of lists
        self.ProblemTypes = []
        
        for i in self.ProblemType.values():
            for k in i:
                self.ProblemTypes.append(k)
                
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(random.choice(self.GenerateProblemType.values()))
        else:
            if LastProblemID in self.ProblemTypes:
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if LastProblemID in v][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return random.choice(self.GenerateProblemType[NextProblemKey])
            else:
                return random.choice(random.choice(self.GenerateProblemType.values()))
        #return self.GenerateProblemType8()

    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            }
        return self.ProblemType[problem_type]
            
    def GenerateProblemType1(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.l1 = randint(35,60)
        self.l2 = randint(self.l1,90)
        self.l3 = randint(35,100)
        self.l4 = randint(35,50)

        self.DisplayL1 = self.l1 / 5
        self.DisplayL2 = self.l2 / 5
        self.DisplayL3 = self.l3 / 5
        self.DisplayL4 = self.l4 / 5
        
        self.FunctionCall = "P4DrawRectangleSquare1("+str(self.l1)+","+str(self.l2)+","+str(self.l3)+","+str(self.l4)+","+str(self.DisplayL1)+","+str(self.DisplayL2)+","+str(self.DisplayL3)+","+str(self.DisplayL4)+")"
        self.answer = 1
     
        self.problem = "Find the area of the below figure.<br><br>"
        self.unit = "cm<sup>2</sup>"
        self.answer = self.DisplayL1*self.DisplayL2 + (self.DisplayL1+self.DisplayL3)*self.DisplayL4 

        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.DisplayL1,self.DisplayL2,self.DisplayL3,self.DisplayL4)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType1(self,problem,answer,d1,d2,d3,d4):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" cm<sup>2</sup>"
        self.solution_text = "Given dimensions as per figure are:<br><br>"
        self.solution_text = self.solution_text + "AB = "+str(d1)+" cm, "
        self.solution_text = self.solution_text + "BC = "+str(d2)+" cm, "
        self.solution_text = self.solution_text + "CD = "+str(d3)+" cm, "
        self.solution_text = self.solution_text + "DE = "+str(d4)+" cm<br><br>"
        self.solution_text = self.solution_text + "Given figure can be cut into two rectangles:<br><br>"
        self.solution_text = self.solution_text + "Rectangle 1 with length = BC and breadth = AB <br><br> Rectangle 2 with length = FE and breadth = DE<br><br>"
        self.solution_text = self.solution_text + "We know the values for all dimensions except FE <br><br> FE = AB + CD = "+str(d1)+" + "+str(d3)+" = "+str(d1+d3)+" cm<br><br>"
        self.solution_text = self.solution_text + "Therefore, area of rectangle 1 = BC &times AB = "+str(d2)+" &times; "+str(d1)+" = "+str(d2*d1)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Similarly area of rectangle 2 = FE &times DE = "+str(d1+d3)+" &times; "+str(d4)+" = "+str((d1+d3)*d4)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Hence total area of given figure = "+str(d1*d2)+" + "+str((d1+d3)*d4)+" = <b><i>"+str(answer)+"</b></i> cm<sup>2</sup>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemType2(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.l3 = randint(60,100)
        self.l4 = randint(30,50)
        self.l1 = randint(self.l3+30,160)
        self.l2 = randint(self.l4+30,100)  

        self.DisplayL1 = self.l1 / 8
        self.DisplayL2 = self.l2 / 8
        self.DisplayL3 = self.l3 / 8
        self.DisplayL4 = self.l4 / 8
        
        self.FunctionCall = "P4DrawRectangleSquare2("+str(self.l1)+","+str(self.l2)+","+str(self.l3)+","+str(self.l4)+","+str(self.DisplayL1)+","+str(self.DisplayL2)+","+str(self.DisplayL3)+","+str(self.DisplayL4)+")"
     
        self.problem = "Find the area of the below figure.<br><br>"
        self.unit = "cm<sup>2</sup>"
        self.answer = (self.DisplayL1-self.DisplayL3)*(self.DisplayL2-self.DisplayL4) + self.DisplayL2*self.DisplayL3 

        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.DisplayL1,self.DisplayL2,self.DisplayL3,self.DisplayL4)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':1,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType2(self,problem,answer,d1,d2,d3,d4):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" cm<sup>2</sup>"
        self.solution_text = "Given dimensions as per figure are:<br><br>"
        self.solution_text = self.solution_text + "AB = "+str(d1)+" cm, "
        self.solution_text = self.solution_text + "BC = "+str(d2)+" cm, "
        self.solution_text = self.solution_text + "CD = "+str(d3)+" cm, "
        self.solution_text = self.solution_text + "DE = "+str(d4)+" cm<br><br>"
        self.solution_text = self.solution_text + "Given figure can be cut into two rectangles:<br><br>"
        self.solution_text = self.solution_text + "Rectangle 1 with length = BC and breadth = CD <br><br> Rectangle 2 with length = AF and breadth = FE<br><br>"
        self.solution_text = self.solution_text + "We know the values for all dimensions except FE and AF<br><br> FE = AB - CD = "+str(d1)+" - "+str(d3)+" = "+str(d1-d3)+" cm<br><br>"
        self.solution_text = self.solution_text + "AF = BC - DE = "+str(d2)+" - "+str(d4)+" = "+str(d2-d4)+"<br><br>"
        self.solution_text = self.solution_text + "Therefore, area of rectangle 1 = BC &times CD = "+str(d2)+" &times; "+str(d3)+" = "+str(d2*d3)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Similarly area of rectangle 2 = FE &times AF = "+str(d1-d3)+" &times; "+str(d2-d4)+" = "+str((d1-d3)*(d2-d4))+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Hence total area of given figure = "+str(d2*d3)+" + "+str((d1-d3)*(d2-d4))+" = <b><i>"+str(answer)+"</b></i> cm<sup>2</sup>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemType3(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.l2 = randint(50,80)
        self.l3 = randint(50,80)
        self.l5 = randint(10,50)
        self.l4 = randint(30,60)
        self.l1 = randint(self.l3+self.l5+20,160)      
        
        self.DisplayL1 = self.l1 / 5
        self.DisplayL2 = self.l2 / 5
        self.DisplayL3 = self.l3 / 5
        self.DisplayL4 = self.l4 / 5
        self.DisplayL5 = self.l5 / 5
        
        self.FunctionCall = "P4DrawRectangleSquare3("+str(self.l1)+","+str(self.l2)+","+str(self.l3)+","+str(self.l4)+","+str(self.l5)+","+str(self.DisplayL1)+","+str(self.DisplayL2)+","+str(self.DisplayL3)+","+str(self.DisplayL4)+","+str(self.DisplayL5)+")"
     
        self.problem = "Find the area of the below figure."
        self.unit = "cm<sup>2</sup>"
        
        if self.l1-self.l3-self.l5>self.l5:
            self.flag = 1
        else:
            self.flag = 2
        self.answer = self.DisplayL1*self.DisplayL2 + self.DisplayL4*self.DisplayL5  

        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.DisplayL1,self.DisplayL2,self.DisplayL3,self.DisplayL4,self.DisplayL5,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType3(self,problem,answer,d1,d2,d3,d4,d5,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" cm<sup>2</sup>"
        self.solution_text = "Given dimensions as per figure are:<br><br>"
        self.solution_text = self.solution_text + "AB = "+str(d1)+" cm, "
        self.solution_text = self.solution_text + "BC = "+str(d2)+" cm, "
        self.solution_text = self.solution_text + "CD = "+str(d3)+" cm, "
        if flag == 2:
            self.solution_text = self.solution_text + "FE = "+str(d5)+" cm<br><br>"
        else:
            self.solution_text = self.solution_text + "GH = "+str(d1-d3-d5)+" cm<br><br>"
        self.solution_text = self.solution_text + "Total height of the figure = "+str(d2+d4)+" cm<br><br>"
        self.solution_text = self.solution_text + "Given figure can be cut into two rectangles: ABCH and DEFG<br><br>"
        self.solution_text = self.solution_text + "Area of rectangle ABCH = AB &times; BC = "+str(d1)+" &times; "+str(d2)+" = "+str(d1*d2)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Area of rectangle DEFG = DE &times; FE<br><br>"
        self.solution_text = self.solution_text + "DE = Total height of the figure - BC = "+str(d2+d4)+" - "+str(d2)+" = "+str(d4)+" cm<br><br>"
        if flag==1:
            self.solution_text = self.solution_text + "FE = AB - CD - GH = "+str(d1)+" - "+str(d3)+" - "+str(d1-d3-d5)+" = "+str(d5)+" cm<br><br>"
        self.solution_text = self.solution_text + "Therefore, area of rectangle DEFG = "+str(d4)+" &times; "+str(d5)+" = "+str(d4*d5)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Hence total area of given figure = "+str(d1*d2)+" + "+str(d4*d5)+" = <b><i>"+str(answer)+"</b></i> cm<sup>2</sup>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemType4(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.l2 = randint(50,80)
        self.l3 = randint(50,80)
        self.l5 = randint(10,50)
        self.l4 = randint(30,60)
        self.l1 = randint(self.l3+self.l5+20,160)      
        
        self.DisplayL1 = self.l1 / 6
        self.DisplayL2 = self.l2 / 6
        self.DisplayL3 = self.l3 / 6
        self.DisplayL4 = self.l4 / 6
        self.DisplayL5 = self.l5 / 6
        
        self.FunctionCall = "P4DrawRectangleSquare4("+str(self.l1)+","+str(self.l2)+","+str(self.l3)+","+str(self.l4)+","+str(self.l5)+","+str(self.DisplayL1)+","+str(self.DisplayL2)+","+str(self.DisplayL3)+","+str(self.DisplayL4)+","+str(self.DisplayL5)+")"
     
        self.problem = "Find the area of the below figure."
        self.unit = "cm<sup>2</sup>"
        
        if self.l1-self.l3-self.l5>self.l5:
            self.flag = 1
        else:
            self.flag = 2
        self.answer = self.DisplayL1*self.DisplayL2 + self.DisplayL4*self.DisplayL5  

        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.DisplayL1,self.DisplayL2,self.DisplayL3,self.DisplayL4,self.DisplayL5,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':1,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType4(self,problem,answer,d1,d2,d3,d4,d5,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" cm<sup>2</sup>"
        self.solution_text = "Given dimensions as per figure are:<br><br>"
        self.solution_text = self.solution_text + "AB = "+str(d1)+" cm, "
        self.solution_text = self.solution_text + "BC = "+str(d2)+" cm, "
        self.solution_text = self.solution_text + "CD = "+str(d3)+" cm, "
        if flag == 2:
            self.solution_text = self.solution_text + "FE = "+str(d5)+" cm<br><br>"
            self.solution_text = self.solution_text + "DE = "+str(d4)+" cm<br><br>"
        else:
            self.solution_text = self.solution_text + "GH = "+str(d1-d3-d5)+" cm<br><br>"
            self.solution_text = self.solution_text + "Total height of the figure = "+str(d2+d4)+" cm<br><br>"
        self.solution_text = self.solution_text + "Given figure can be cut into two rectangles: ABCH and DEFG<br><br>"
        self.solution_text = self.solution_text + "Area of rectangle ABCH = AB &times; BC = "+str(d1)+" &times; "+str(d2)+" = "+str(d1*d2)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Area of rectangle DEFG = DE &times; FE"
        if flag==2:
            self.solution_text = self.solution_text + " = "+str(d4)+" &times; "+str(d5)+" = "+str(d4*d5)+" cm<sup>2</sup><br><br>"
        if flag==1:
            self.solution_text = self.solution_text + "<br><br>DE = Total height of the figure - BC = "+str(d2+d4)+" - "+str(d2)+" = "+str(d4)+" cm<br><br>"
            self.solution_text = self.solution_text + "FE = AB - CD - GH = "+str(d1)+" - "+str(d3)+" - "+str(d1-d3-d5)+" = "+str(d5)+" cm<br><br>"
            self.solution_text = self.solution_text + "Therefore, area of rectangle DEFG = "+str(d4)+" &times; "+str(d5)+" = "+str(d4*d5)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Hence total area of given figure = "+str(d1*d2)+" + "+str(d4*d5)+" = <b><i>"+str(answer)+"</b></i> cm<sup>2</sup>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemType5(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.l1 = random.randrange(60,100,8)
        self.l2 = random.randrange(60,100,8)
        self.l3 = random.randrange(30,60,8)
        self.l4 = random.randrange(30,60,8)
        self.l5 = random.randrange(59,self.l1+self.l3-30,8)    
        
        self.DisplayL1 = self.l1 / 8
        self.DisplayL2 = self.l2 / 8
        self.DisplayL3 = self.l3 / 8
        self.DisplayL4 = self.l4 / 8
        self.DisplayL5 = self.l5 / 8
        
        if self.DisplayL3 == self.DisplayL5:
            self.l5 = self.l3 + 8
            self.DisplayL5 = self.l5 / 8
        
        self.FunctionCall = "P4DrawRectangleSquare5("+str(self.l1)+","+str(self.l2)+","+str(self.l3)+","+str(self.l4)+","+str(self.l5)+","+str(self.DisplayL1)+","+str(self.DisplayL2)+","+str(self.DisplayL3)+","+str(self.DisplayL4)+","+str(self.DisplayL5)+")"
     
        self.problem = "Find the area of the below figure."
        self.unit = "cm<sup>2</sup>"

        self.answer = self.DisplayL1*self.DisplayL2 + self.DisplayL4*self.DisplayL5  

        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.DisplayL1,self.DisplayL2,self.DisplayL3,self.DisplayL4,self.DisplayL5)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'CheckAnswerType':1,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType5(self,problem,answer,d1,d2,d3,d4,d5):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" cm<sup>2</sup>"
        self.solution_text = "Given dimensions as per figure are:<br><br>"
        self.solution_text = self.solution_text + "AB = "+str(d1)+" cm, "
        self.solution_text = self.solution_text + "BC = "+str(d2)+" cm, "
        self.solution_text = self.solution_text + "CD = "+str(d3)+" cm, "
        self.solution_text = self.solution_text + "GH = "+str(d1+d3-d5)+" cm<br><br>"
        self.solution_text = self.solution_text + "Total height of the figure = "+str(d2+d4)+" cm<br><br>"
        self.solution_text = self.solution_text + "Given figure can be cut into two rectangles: ABCH and DEFG<br><br>"
        self.solution_text = self.solution_text + "Area of rectangle ABCH = AB &times; BC = "+str(d1)+" &times; "+str(d2)+" = "+str(d1*d2)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Area of rectangle DEFG = DE &times; FE"
        self.solution_text = self.solution_text + "<br><br>DE = Total height of the figure - BC = "+str(d2+d4)+" - "+str(d2)+" = "+str(d4)+" cm<br><br>"
        self.solution_text = self.solution_text + "FE = AB + CD - GH = "+str(d1)+" + "+str(d3)+" - "+str(d1+d3-d5)+" = "+str(d5)+" cm<br><br>"
        self.solution_text = self.solution_text + "Therefore, area of rectangle DEFG = "+str(d4)+" &times; "+str(d5)+" = "+str(d4*d5)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Hence total area of given figure = "+str(d1*d2)+" + "+str(d4*d5)+" = <b><i>"+str(answer)+"</b></i> cm<sup>2</sup>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemType6(self):

        self.complexity_level = "difficult"
        self.HCScore = 7
        
        self.l1 = random.randrange(30,60,4)
        self.l2 = random.randrange(60,80,4)
        self.l4 = random.randrange(60,80,4)
        self.l5 = random.randrange(30,60,4)
        self.l3 = random.randrange(self.l5+30,100,4)
        self.l6 = random.randrange(40,50,4)

        if self.l4 - self.l6 < 4:
            self.l4 = self.l6 + 8
            
        self.DisplayL1 = self.l1 / 4
        self.DisplayL2 = self.l2 / 4
        self.DisplayL3 = self.l3 / 4
        self.DisplayL4 = self.l4 / 4
        self.DisplayL5 = self.l5 / 4
        self.DisplayL6 = self.l6 / 4
        
        self.FunctionCall = "P4DrawRectangleSquare6("+str(self.l1)+","+str(self.l2)+","+str(self.l3)+","+str(self.l4)+","+str(self.l5)+","+str(self.l6)+","+str(self.DisplayL1)+","+str(self.DisplayL2)+","+str(self.DisplayL3)+","+str(self.DisplayL4)+","+str(self.DisplayL5)+","+str(self.DisplayL6)+")"
     
        self.problem = "Find the area of the below figure."
        self.unit = "cm<sup>2</sup>"

        self.answer = self.DisplayL1*(self.DisplayL2+self.DisplayL4) + self.DisplayL4*self.DisplayL5 + (self.DisplayL4-self.DisplayL6)*(self.DisplayL3-self.DisplayL5)  

        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.DisplayL1,self.DisplayL2,self.DisplayL3,self.DisplayL4,self.DisplayL5,self.DisplayL6)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6",'CheckAnswerType':1,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType6(self,problem,answer,d1,d2,d3,d4,d5,d6):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" cm<sup>2</sup>"
        self.solution_text = "Given dimensions as per figure are:<br><br>"
        self.solution_text = self.solution_text + "AB = "+str(d1)+" cm, "
        self.solution_text = self.solution_text + "BC = "+str(d2)+" cm, "
        self.solution_text = self.solution_text + "CE = "+str(d3)+" cm, "
        self.solution_text = self.solution_text + "EF = "+str(d4)+" cm, "
        self.solution_text = self.solution_text + "FG = "+str(d5)+" cm, "
        self.solution_text = self.solution_text + "IJ = "+str(d6)+" cm<br><br>"
        self.solution_text = self.solution_text + "Given figure can be cut into 3 rectangles: ABJK, CDIH and DEFG<br><br>"
        self.solution_text = self.solution_text + "Area of rectangle ABJK = AB &times; AK<br><br>"
        self.solution_text = self.solution_text + "AK = BC + EF = "+str(d2)+" + "+str(d4)+" = "+str(d2+d4)+" cm<br><br>"
        self.solution_text = self.solution_text + "Therefore, area of rectangle ABJK = "+str(d1)+" &times; "+str(d2+d4)+" = "+str(d1*(d2+d4))+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Area of rectangle CDIH = CD &times; DH<br><br>"
        self.solution_text = self.solution_text + "CD = CE - FG = "+str(d3)+" - "+str(d5)+" = "+str(d3-d5)+" cm<br><br>"
        self.solution_text = self.solution_text + "DH = EF - GH = "+str(d4)+" - "+str(d6)+" = "+str(d4-d6)+" cm<br><br>"
        self.solution_text = self.solution_text + "Therefore, area of rectangle CDIH = "+str(d1+d3-d5)+" &times; "+str(d4-d6)+" = "+str((d3-d5)*(d4-d6))+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Area of rectangle DEFG = EF &times; FG = "+str(d4)+" &times; "+str(d5)+" = "+str(d4*d5)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Hence total area of given figure = "+str(d1*(d2+d4))+" + "+str((d3-d5)*(d4-d6))+" + "+str(d4*d5)+" = <b><i>"+str(answer)+"</b></i> cm<sup>2</sup>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemType7(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.l1 = random.randrange(120,160,4)
        self.l2 = random.randrange(self.l1/4,self.l1/2,4)
        self.l3 = random.randrange(self.l1/4,self.l1/2,4)

        if self.l2 == self.l3:
            self.l2 = self.l3 + 8
            
        self.DisplayL1 = self.l1 / 4
        self.DisplayL2 = self.l2 / 4
        self.DisplayL3 = self.l3 / 4
        
        self.FunctionCall = "P4DrawRectangleSquare7("+str(self.l1)+","+str(self.l2)+","+str(self.l3)+","+str(self.DisplayL1)+","+str(self.DisplayL2)+","+str(self.DisplayL3)+")"
     
        self.problem = "Find the area of the below shaded figure."
        self.unit = "cm<sup>2</sup>"

        self.answer = self.DisplayL1*self.DisplayL1 - self.DisplayL2*self.DisplayL3  

        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.DisplayL1,self.DisplayL2,self.DisplayL3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7",'CheckAnswerType':1,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType7(self,problem,answer,d1,d2,d3):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" cm<sup>2</sup>"
        self.solution_text = "To find the area of the shaded figure, first calculate the area of the outer square and then subtract the area of the inner rectangle from it.<br><br>"
        self.solution_text = self.solution_text + "Area of the outer square = "+str(d1)+" &times; "+str(d1)+" = "+str(d1*d1)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Area of the inner rectangle = "+str(d2)+" &times; "+str(d3)+" = "+str(d2*d3)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Hence, area of the shaded region = "+str(d1*d1)+" - "+str(d2*d3)+" = <b><i>"+str(answer)+" cm<sup>2</sup></i></b>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
            
    def GenerateProblemType8(self):

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.l1 = randint(30,50)

        self.DisplayL1 = random.randrange(6,20,2)
        
        self.FunctionCall = "P4DrawRectangleSquare8("+str(self.l1)+","+str(self.DisplayL1)+")"
     
        self.problem = "Find the area of the below shaded figure."
        self.unit = "cm<sup>2</sup>"

        self.answer = (3*self.DisplayL1+2*self.DisplayL1+self.DisplayL1)*self.DisplayL1   

        self.template = "DrawCompositeFigures.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.DisplayL1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8",'CheckAnswerType':1,'grade':4,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,
                'FunctionCall':self.FunctionCall}

    def ExplainType8(self,problem,answer,d1):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" cm<sup>2</sup>"
        self.solution_text = "The given figure can be divided into 3 rectangles as shown by the dotted lines.<br><br>"
        self.solution_text = self.solution_text + "Length of the first rectangle = "+str(3*d1)+" cm and breadth = "+str(d1)+" cm <br><br>"
        self.solution_text = self.solution_text + "Therefore area of the first rectangle = "+str(3*d1)+" &times; "+str(d1)+" = "+str(3*d1*d1)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Length of the second rectangle = "+str(d1)+" + "+str(d1)+" = "+str(2*d1)+" cm and breadth = "+str(d1)+" cm <br><br>"
        self.solution_text = self.solution_text + "Therefore area of the second rectangle = "+str(2*d1)+" &times; "+str(d1)+" = "+str(2*d1*d1)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Length of the third rectangle = "+str(d1)+" cm and breadth = "+str(3*d1)+" - "+str(2*d1)+" = "+str(d1)+" cm <br><br>"
        self.solution_text = self.solution_text + "Since length and breadth of third rectangle is same it's indeed a square<br><br>"
        self.solution_text = self.solution_text + "Therefore area of the square = "+str(d1)+" &times; "+str(d1)+" = "+str(d1*d1)+" cm<sup>2</sup><br><br>"
        self.solution_text = self.solution_text + "Hence area of the given figure = area of 2 rectangles + area of the square<br><br> = "+str(3*d1*d1)+" + "+str(2*d1*d1)+" + "+str(d1*d1)+" = <b><i>"+str(answer)+"cm<sup>2</sup></b></i>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckType):
        if CheckType==1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False               