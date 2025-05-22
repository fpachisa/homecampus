'''
Created on Mar 16, 2011

Module: AreaOfTriangle
Generates "Calculating area of triangle" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random
from random import randint

class AreaOfTriangle:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        self.ProblemType = random.choice([self.GenerateProblemType1(),self.GenerateProblemType2(),
                                            self.GenerateProblemType3(),self.GenerateProblemType4()])
        return self.ProblemType
        #return self.GenerateProblemType4()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:"ProblemType1",2:"ProblemType2",3:"ProblemType3",4:"ProblemType4",}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemType2(),3:self.GenerateProblemType3(),
                                    4:self.GenerateProblemType4(),}
        
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(self.GenerateProblemType.values())
        else:
            if LastProblemID in self.ProblemType.values():
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if v == LastProblemID][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return self.GenerateProblemType[NextProblemKey]
            else:
                return random.choice(self.GenerateProblemType.values())
        #return self.GenerateProblemType1()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g.:
        Find the area of each shaded triangle'''
                  
        self.length = randint(60,110)
        self.divider = randint(4,10)
        self.DisplayLength = self.length/self.divider
        self.breadth = randint(60,110)
        self.DisplayBreadth = self.breadth/self.divider
        while self.DisplayBreadth*self.DisplayLength % 2 != 0 :
            self.DisplayBreadth = self.DisplayBreadth + 1
        
        self.answer = self.DisplayBreadth*self.DisplayLength/2
        
        self.template = "DrawTriangles.html"
        self.ProblemSelector = randint(1,2)
        if (self.ProblemSelector==1):
            self.FunctionCall = "DrawTriangle1("+str(self.length)+","+str(self.breadth)+","+str(self.DisplayLength)+","+str(self.DisplayBreadth)+")"
            self.problem = "Find the area of the shaded triangle:<br>(length of line AC="+str(self.DisplayLength)+" cm and length of line BC="+str(self.DisplayBreadth)+" cm )"
            self.flag = 1
        elif(self.ProblemSelector==2):
            self.FunctionCall = "DrawTriangle2("+str(self.length)+","+str(self.breadth)+","+str(self.DisplayBreadth)+","+str(self.DisplayLength)+")"
            self.problem = "Find the area of the shaded triangle:<br>(length of line AC="+str(self.DisplayBreadth)+" cm and length of line BD="+str(self.DisplayLength)+" cm )"
            self.flag = 2
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.DisplayBreadth,self.DisplayLength,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",'unit':"cm<sup>2</sup>",'FunctionCall':self.FunctionCall}

    def ExplainType1(self,problem,answer,base,height,flag):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+" cm<sup>2</sup>"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:"
        self.solution_text = self.solution_text + "<table cellspacing=0 cellpadding=1><tr>"
        self.solution_text = self.solution_text + "<td align='right'> Area of a triangle = </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;1&nbsp;</u><br>2</td>"
        self.solution_text = self.solution_text + "<td >&times; &nbsp; Base &nbsp; &times; &nbsp; Height</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        if flag == 1:
            self.solution_text = self.solution_text + "Given shaded triangle is a right angled triangle.<br><br>"
            self.solution_text = self.solution_text + "So the base of the triangle is BC and height is AC.<br><br>"
        elif flag == 2:
            self.solution_text = self.solution_text + "Height of a triangle is perpendicular to its base.<br><br>"
            self.solution_text = self.solution_text + "So the base of the shaded triangle is AC and height is BD.<br><br>"                      
        self.solution_text = self.solution_text + "<table cellspacing=0 cellpadding=1><tr>"
        self.solution_text = self.solution_text + "<td align='right'> Therefore, area of the triangle = </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;1&nbsp;</u><br>2</td>"
        self.solution_text = self.solution_text + "<td >&times; &nbsp; "+str(base)+" &nbsp; &times; &nbsp; "+str(height)+" = "+str(answer)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"        
        self.solution_text = self.solution_text + "<i><b>Hence area of the shaded triangle is "+str(answer)+" cm<sup>2</sup></b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.:
        Find the area of each shaded triangle'''
        
        self.StartX = 25       
        self.length = randint(90,160)
        self.divider = randint(4,10)
        self.DisplayLength = self.length/self.divider
        self.breadth = randint(70,140)
        self.DisplayBreadth = self.breadth/self.divider
        self.base = self.length*randint(5,10)/10
        self.DisplayBase = self.base/self.divider
        
        self.X = {1:[self.StartX,self.StartX,self.StartX+self.base,self.StartX+self.breadth,self.StartX,self.StartX+self.breadth],
                  2:[self.StartX+self.length,self.StartX,self.StartX+self.length-self.base,self.StartX+self.breadth,self.StartX+self.length,self.StartX+self.breadth],
                  3:[self.StartX+self.length,self.StartX+self.breadth,self.StartX+self.length-self.base,self.StartX,self.StartX+self.length,self.StartX],
                  4:[self.StartX,self.StartX+self.breadth,self.StartX+self.base,self.StartX,self.StartX,self.StartX]}
        
        self.XKey = self.X.keys()[randint(0,len(self.X)-1)]
        self.xA = self.X[self.XKey][0]
        self.yA = self.X[self.XKey][1]
        self.xB = self.X[self.XKey][2]
        self.yB = self.X[self.XKey][3]
        self.xC = self.X[self.XKey][4]
        self.yC = self.X[self.XKey][5]
        
        while self.DisplayBase*self.DisplayLength % 2 != 0 :
            self.DisplayBase = self.DisplayBase + 1
        
        self.answer = self.DisplayBase*self.DisplayLength/2
        
        self.template = "DrawTriangles.html"
        self.FunctionCall = "DrawTriangle3("+str(self.StartX)+","+str(self.StartX)+","+str(self.length)+","+str(self.breadth)+","+str(self.DisplayLength)+","+str(self.DisplayBase)+","+str(self.xA)+","+str(self.yA)+","+str(self.xB)+","+str(self.yB)+","+str(self.xC)+","+str(self.yC)+")"
        self.problem = "Find the area of the shaded triangle:<br>(length of line AC="+str(self.DisplayLength)+" cm and length of line BC="+str(self.DisplayBase)+" cm)"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.DisplayBase,self.DisplayLength)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",'unit':"cm<sup>2</sup>",'FunctionCall':self.FunctionCall}

    def ExplainType2(self,problem,answer,base,height):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+" cm<sup>2</sup>"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:"
        self.solution_text = self.solution_text + "<table cellspacing=0 cellpadding=1><tr>"
        self.solution_text = self.solution_text + "<td align='right'> Area of a triangle = </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;1&nbsp;</u><br>2</td>"
        self.solution_text = self.solution_text + "<td >&times; &nbsp; Base &nbsp; &times; &nbsp; Height</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "Given shaded triangle is a right angled triangle.<br><br>"
        self.solution_text = self.solution_text + "So the base of the triangle is BC and height is AC.<br><br>"                    
        self.solution_text = self.solution_text + "<table cellspacing=0 cellpadding=1><tr>"
        self.solution_text = self.solution_text + "<td align='right'> Therefore, area of the triangle = </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;1&nbsp;</u><br>2</td>"
        self.solution_text = self.solution_text + "<td >&times; &nbsp; "+str(base)+" &nbsp; &times; &nbsp; "+str(height)+" = "+str(answer)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"        
        self.solution_text = self.solution_text + "<i><b>Hence area of the shaded triangle is "+str(answer)+" cm<sup>2</sup></b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):
        '''e.g.:
        Find the area of each shaded triangle'''
        
        self.StartX = 25       
        self.breadth = randint(70,120)
        self.length = randint(self.breadth+10,160)
        self.divider = randint(4,10)
        self.DisplayLength = self.length/self.divider
        self.DisplayBreadth = self.breadth/self.divider
        self.PointXA = random.randrange(0,self.length)
        self.base1 = random.randrange(self.length/6,self.length/4)
        self.DisplayBase1 = self.base1/self.divider
        self.base2 = random.randrange(self.length/6,self.length/4)
        self.DisplayBase2 = self.base2/self.divider
        
        self.X = {1:[self.StartX+self.PointXA,self.StartX,self.StartX+self.base1,self.StartX+self.breadth,self.StartX+self.length-self.base2,self.StartX+self.breadth],
                  2:[self.StartX+self.PointXA,self.StartX+self.breadth,self.StartX+self.base1,self.StartX,self.StartX+self.length-self.base2,self.StartX]}
        self.XKey = self.X.keys()[randint(0,len(self.X)-1)]
        self.xA = self.X[self.XKey][0]
        self.yA = self.X[self.XKey][1]
        self.xB = self.X[self.XKey][2]
        self.yB = self.X[self.XKey][3]
        self.xC = self.X[self.XKey][4]
        self.yC = self.X[self.XKey][5]
        
        while (self.DisplayLength - self.DisplayBase1 - self.DisplayBase2)*self.DisplayBreadth % 2 != 0 :
            self.DisplayBase1 = self.DisplayBase1 + 1
        
        self.answer = (self.DisplayLength - self.DisplayBase1 - self.DisplayBase2)*self.DisplayBreadth/2
        
        self.template = "DrawTriangles.html"
        self.FunctionCall = "DrawTriangle4("+str(self.StartX)+","+str(self.StartX)+","+str(self.length)+","+str(self.breadth)+","+str(self.DisplayLength)+","+str(self.DisplayBase1)+","+str(self.DisplayBase2)+","+str(self.DisplayBreadth)+","+str(self.xA)+","+str(self.yA)+","+str(self.xB)+","+str(self.yB)+","+str(self.xC)+","+str(self.yC)+")"
        if self.XKey == 1:
            self.problem = "Find the area of the shaded triangle:<br>(length of line AB="+str(self.DisplayLength)+" cm and length of line BC="+str(self.DisplayBreadth)+" cm<br>length of line DF="+str(self.DisplayBase1)+" cm and length of line EC="+str(self.DisplayBase2)+" cm)"
            self.flag = 1
        elif self.XKey == 2:
            self.problem = "Find the area of the shaded triangle:<br>(length of line DC="+str(self.DisplayLength)+" cm and length of line BC="+str(self.DisplayBreadth)+" cm<br>length of line AF="+str(self.DisplayBase1)+" cm and length of line EB="+str(self.DisplayBase2)+" cm)"           
            self.flag = 2
            
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.DisplayLength,self.DisplayBase1,self.DisplayBase2,self.DisplayBreadth,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",'unit':"cm<sup>2</sup>",'FunctionCall':self.FunctionCall}

    def ExplainType3(self,problem,answer,base,base1,base2,height,flag):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+" cm<sup>2</sup>"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:"
        self.solution_text = self.solution_text + "<table cellspacing=0 cellpadding=1><tr>"
        self.solution_text = self.solution_text + "<td align='right'> Area of a triangle = </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;1&nbsp;</u><br>2</td>"
        self.solution_text = self.solution_text + "<td >&times; &nbsp; Base &nbsp; &times; &nbsp; Height</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "Base of the shaded triangle is FE and Height of a triangle is perpendicular to its base.<br><br>"
        self.solution_text = self.solution_text + "So the height is BC.<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "Length of FE = AB - (DF+EC) = "+str(base)+" - ("+str(base1)+" + "+str(base2)+") = "+str(base-base1-base2)+"<br><br>"                     
        elif flag == 2:
            self.solution_text = self.solution_text + "Length of FE = DC - (AF+EB) = "+str(base)+" - ("+str(base1)+" + "+str(base2)+") = "+str(base-base1-base2)+"<br><br>"                     
        self.solution_text = self.solution_text + "<table cellspacing=0 cellpadding=1><tr>"
        self.solution_text = self.solution_text + "<td align='right'> Therefore, area of the triangle = </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;1&nbsp;</u><br>2</td>"
        self.solution_text = self.solution_text + "<td >&times; &nbsp; "+str(base-base1-base2)+" &nbsp; &times; &nbsp; "+str(height)+" = "+str(answer)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"        
        self.solution_text = self.solution_text + "<i><b>Hence area of the shaded triangle is "+str(answer)+" cm<sup>2</sup></b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):
        '''e.g.:
        Find the area of each shaded triangle'''
        
        self.StartX = 25       
        self.breadth = randint(70,120)
        self.length = randint(self.breadth+10,160)
        self.divider = randint(4,10)
        self.DisplayLength = self.length/self.divider
        self.DisplayBreadth = self.breadth/self.divider
        self.PointXA = random.randrange(self.length/6,self.length/4)
        self.PointYA = random.randrange(self.breadth/6,self.breadth/4)
        self.DisplayHeight = self.PointYA/self.divider
        self.base1 = random.randrange(self.length/6,self.length/4)
        self.DisplayBase1 = self.base1/self.divider
        self.base2 = random.randrange(self.length/6,self.length/4)
        self.DisplayBase2 = self.base2/self.divider
        
        self.X = {1:[self.StartX+self.PointXA,self.StartX+self.PointYA,self.StartX+self.base1,self.StartX+self.breadth,self.StartX+self.length-self.base2,self.StartX+self.breadth],
                  2:[self.StartX+self.PointXA,self.StartX+self.breadth-self.PointYA,self.StartX+self.base1,self.StartX,self.StartX+self.length-self.base2,self.StartX]}

        self.XKey = self.X.keys()[randint(0,len(self.X)-1)]      
        self.xA = self.X[self.XKey][0]
        self.yA = self.X[self.XKey][1]
        self.xB = self.X[self.XKey][2]
        self.yB = self.X[self.XKey][3]
        self.xC = self.X[self.XKey][4]
        self.yC = self.X[self.XKey][5]
        
        while (self.DisplayLength - self.DisplayBase1 - self.DisplayBase2)*(self.DisplayBreadth - self.DisplayHeight)% 2 != 0 :
            self.DisplayBase1 = self.DisplayBase1 + 1
        
        self.answer = (self.DisplayLength - self.DisplayBase1 - self.DisplayBase2)*(self.DisplayBreadth - self.DisplayHeight)/2
        
        self.template = "DrawTriangles.html"
        self.FunctionCall = "DrawTriangle5("+str(self.StartX)+","+str(self.StartX)+","+str(self.length)+","+str(self.breadth)+","+str(self.DisplayLength)+","+str(self.DisplayBase1)+","+str(self.DisplayBase2)+","+str(self.DisplayBreadth)+","+str(self.DisplayHeight)+","+str(self.xA)+","+str(self.yA)+","+str(self.xB)+","+str(self.yB)+","+str(self.xC)+","+str(self.yC)+")"
        if self.XKey == 1:
            self.problem = "Find the area of the shaded triangle:<br>length of lines: <br>AB="+str(self.DisplayLength)+" cm&nbsp;&nbsp;&nbsp;BC="+str(self.DisplayBreadth)+" cm<br>DF="+str(self.DisplayBase1)+" cm&nbsp;&nbsp;&nbsp;GC="+str(self.DisplayBase2)+" cm<br>AE="+str(self.DisplayHeight)+" cm"
            self.flag = 1
        elif self.XKey == 2:
            self.problem = "Find the area of the shaded triangle:<br>length of lines: <br>AB="+str(self.DisplayLength)+" cm&nbsp;&nbsp;&nbsp;BC="+str(self.DisplayBreadth)+" cm<br>AF="+str(self.DisplayBase1)+" cm&nbsp;&nbsp;&nbsp;GB="+str(self.DisplayBase2)+" cm<br>DE="+str(self.DisplayHeight)+" cm"
            self.flag = 2           

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.DisplayLength,self.DisplayBase1,self.DisplayBase2,self.DisplayBreadth,self.DisplayHeight,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",'unit':"cm<sup>2</sup>",'FunctionCall':self.FunctionCall}

    def ExplainType4(self,problem,answer,base,base1,base2,height,height1,flag):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+" cm<sup>2</sup>"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:"
        self.solution_text = self.solution_text + "<table cellspacing=0 cellpadding=1><tr>"
        self.solution_text = self.solution_text + "<td align='right'> Area of a triangle = </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;1&nbsp;</u><br>2</td>"
        self.solution_text = self.solution_text + "<td >&times; &nbsp; Base &nbsp; &times; &nbsp; Height</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "Base of the shaded triangle is FG and Height of a triangle is perpendicular to its base.<br><br>"       
        if flag == 1:
            self.solution_text = self.solution_text + "So the height is DE.<br><br>"
            self.solution_text = self.solution_text + "Length of FG = AB - (DF+GC) = "+str(base)+" - ("+str(base1)+" + "+str(base2)+") = "+str(base-base1-base2)+"<br><br>"
            self.solution_text = self.solution_text + "Length of DE = BC - AE = "+str(height)+" - "+str(height1)+" = "+str(height-height1)+"<br><br>"                     
        elif flag == 2:
            self.solution_text = self.solution_text + "So the height is AE.<br><br>"
            self.solution_text = self.solution_text + "Length of FG = AB - (AF+GB) = "+str(base)+" - ("+str(base1)+" + "+str(base2)+") = "+str(base-base1-base2)+"<br><br>"
            self.solution_text = self.solution_text + "Length of AE = BC - DE = "+str(height)+" - "+str(height1)+" = "+str(height-height1)+"<br><br>"
                                 
        self.solution_text = self.solution_text + "<table cellspacing=0 cellpadding=1><tr>"
        self.solution_text = self.solution_text + "<td align='right'> Therefore, area of the triangle = </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;1&nbsp;</u><br>2</td>"
        self.solution_text = self.solution_text + "<td >&times; &nbsp; "+str(base-base1-base2)+" &nbsp; &times; &nbsp; "+str(height-height1)+" = "+str(answer)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"        
        self.solution_text = self.solution_text + "<i><b>Hence area of the shaded triangle is "+str(answer)+" cm<sup>2</sup></b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def checkAnswer(self,template,answer,InputAnswer):
        try:
            return (int(answer)==int(InputAnswer))
        except ValueError:
            return False  