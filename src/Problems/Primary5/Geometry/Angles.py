'''
Created on April 17, 2011

Module: Angles
Generates "Find the unknown angles" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random

class Angles:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        self.ProblemType = random.choice([self.GenerateProblemType1(),self.GenerateProblemType2(),self.GenerateProblemType3(),
                                          self.GenerateProblemType4(),self.GenerateProblemType5(),self.GenerateProblemType6(),
                                          self.GenerateProblemType7()])
        return self.ProblemType
        #return self.GenerateProblemType7()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:"ProblemType1",2:"ProblemType2",3:"ProblemType3",4:"ProblemType4",
                            5:"ProblemType5",6:"ProblemType6",7:"ProblemType7",}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemType2(),3:self.GenerateProblemType3(),4:self.GenerateProblemType4(),
                                    5:self.GenerateProblemType5(),6:self.GenerateProblemType6(),7:self.GenerateProblemType7(),}
        
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
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g.:
        Find the '''
                       
        self.angle1 = random.randrange(30,150,10)
        while self.angle1 == 90:
            self.angle1 = random.randrange(30,150,10)
        self.answer = 180 - self.angle1
        
        self.template = "Geometry.html"
        self.FunctionCall = "DrawAngles"+str(random.choice([1,3]))+"("+str(self.angle1)+")" 
        self.problem = "Find the unknown marked angle:"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.angle1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",'unit':"&deg;",'FunctionCall':self.FunctionCall}

    def ExplainType1(self,problem,answer,angle1):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+"&deg;"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "The sum of the angles on a straight line is 180&deg;<br><br>"
        self.solution_text = self.solution_text + str(angle1)+"&deg; + &ang;X = 180&deg;<br><br>"
        self.solution_text = self.solution_text + "&ang;X = 180&deg; - "+str(angle1)+"&deg;"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the missing angle is "+str(answer)+"&deg;</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.:
        Find the '''
                       
        self.angle1 = random.randrange(30,70,10)
        self.angle2 = random.randrange(30,70,10)
        self.answer = 180 - self.angle1 - self.angle2
        
        self.template = "Geometry.html"
        self.FunctionCall = "DrawAngles2("+str(self.angle1)+","+str(self.angle2)+")" 
        self.problem = "Find the unknown marked angle:"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.angle1,self.angle2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",'unit':"&deg;",'FunctionCall':self.FunctionCall}

    def ExplainType2(self,problem,answer,angle1,angle2):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+"&deg;"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "The sum of the angles on a straight line is 180&deg;<br><br>"
        self.solution_text = self.solution_text + str(angle1)+"&deg; + "+str(angle2)+"&deg; + &ang;X = 180&deg;<br><br>"
        self.solution_text = self.solution_text + "&ang;X = 180&deg; - "+str(angle1)+"&deg; - "+str(angle2)+"&deg;"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the missing angle is "+str(answer)+"&deg;</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):
        '''e.g.:
        Find the '''
                       
        self.angle1 = random.randrange(30,150,10)
        while self.angle1 == 90:
            self.angle1 = random.randrange(30,150,10)
            
        self.answer = self.angle1
        
        self.template = "Geometry.html"
        self.FunctionCall = "DrawAngles4("+str(self.angle1)+")" 
        self.problem = "Find the unknown marked angle:"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.angle1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",'unit':"&deg;",'FunctionCall':self.FunctionCall}

    def ExplainType3(self,problem,answer,angle1):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+"&deg;"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Vertically opposite angles are equal.<br><br>"
        self.solution_text = self.solution_text + "&ang;"+str(angle1)+" and &ang;X are vertically opposite.<br><br>"
        self.solution_text = self.solution_text + "Therefore, &ang;X = "+str(angle1)+"&deg;"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the missing angle is "+str(answer)+"&deg;</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):
        '''e.g.:
        Find the '''
                       
        self.angle1 = random.randrange(30,70,5)
        self.angle2 = random.randrange(30,70,5)
        self.angle3 = random.randrange(30,70,5)
        self.angle4 = random.randrange(30,70,5)

        self.answer = 180 - self.angle3 - self.angle4
        
        self.template = "Geometry.html"
        self.FunctionCall = "DrawAngles5("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+","+str(self.angle4)+")" 
        self.problem = "Find the unknown marked angle:"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.angle1,self.angle2,self.angle3,self.angle4)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",'unit':"&deg;",'FunctionCall':self.FunctionCall}

    def ExplainType4(self,problem,answer,angle1,angle2,angle3,angle4):
        DisplayAngle1 = angle1+angle3
        DisplayAngle2 = 180-angle1-angle2
        DisplayAngle3 = angle2+angle4
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+"&deg;"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "The sum of the angles at a point is 360&deg;.<br><br>"
        self.solution_text = self.solution_text + str(DisplayAngle1)+"&deg; + "+str(DisplayAngle2)+"&deg; + "+str(DisplayAngle3)+"&deg; + &ang;X = 360&deg;<br><br>"
        self.solution_text = self.solution_text + "&ang;X = 360 - ("+str(DisplayAngle1)+"&deg; + "+str(DisplayAngle2)+"&deg; + "+str(DisplayAngle3)+"&deg;)"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the missing angle is "+str(answer)+"&deg;</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):
        '''e.g.:
        Find the '''
                       
        self.angle1 = random.randrange(30,70,5)
        self.angle2 = random.randrange(30,70,5)

        self.answer = 180 + self.angle1 + self.angle2
        
        self.template = "Geometry.html"
        self.FunctionCall = "DrawAngles6("+str(self.angle1)+","+str(self.angle2)+")" 
        self.problem = "Find the unknown marked angle:"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.angle1,self.angle2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",'unit':"&deg;",'FunctionCall':self.FunctionCall}

    def ExplainType5(self,problem,answer,angle1,angle2):
        DisplayAngle1 = 180-angle1-angle2
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+"&deg;"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "The sum of the angles at a point is 360&deg;.<br><br>"
        self.solution_text = self.solution_text + str(DisplayAngle1)+"&deg; + &ang;X = 360&deg;<br><br>"
        self.solution_text = self.solution_text + "&ang;X = 360&deg; - "+str(DisplayAngle1)+"&deg;"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the missing angle is "+str(answer)+"&deg;</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):
        '''e.g.:
        Find the '''
                       
        self.angle1 = random.randrange(30,70,5)
        self.angle2 = random.randrange(30,70,5)
        self.angle3 = int(1.5*self.angle2 + 20)

        self.answer = self.angle1 + self.angle2
        
        self.template = "Geometry.html"
        self.FunctionCall = "DrawAngles7("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+")" 
        self.problem = "AB and CD are two straight lines. &ang;COE = "+str(self.angle3-self.angle2)+"&deg; &ang;BOD = "+str(180-self.angle1-self.angle2)+"&deg;<br>Find the unknown marked angle:"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.angle1,self.angle2,self.angle3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",'unit':"&deg;",'FunctionCall':self.FunctionCall}

    def ExplainType6(self,problem,answer,angle1,angle2,angle3):
        DisplayAngle1 = 180-angle1-angle2
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+"&deg;"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "<i>Vertically opposite angles are equal.</i><br><br>"
        self.solution_text = self.solution_text + "Since AB and CD are two straight lines, &ang;COA and &ang;BOD are vertically opposite.<br><br>"
        self.solution_text = self.solution_text + "&ang;BOD = &ang;COA = "+str(DisplayAngle1)+"&deg;<br><br>"
        self.solution_text = self.solution_text + "<i>Sum of angles on a straight line is 180&deg;</i><br><br>"
        self.solution_text = self.solution_text + "Since AB is a straight line, &ang;X + &ang;COA = 180&deg;<br><br>"
        self.solution_text = self.solution_text + "&ang;X = 180&deg; - &ang;COA = 180&deg; - "+str(DisplayAngle1)+"&deg;"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the missing angle is "+str(answer)+"&deg;</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):
        '''e.g.:
        Find the '''
                       
        self.angle1 = random.randrange(30,50,5)
        self.angle2 = random.randrange(30,50,5)
        self.angle3 = int(1.5*self.angle2 + 20)

        self.answer = 180 - self.angle1 - self.angle3
        
        self.template = "Geometry.html"
        self.FunctionCall = "DrawAngles8("+str(self.angle1)+","+str(self.angle2)+","+str(self.angle3)+")" 
        self.problem = "AB and CD are two straight lines. &ang;COE = "+str(self.angle3-self.angle2)+"&deg; &ang;BOD = "+str(180-self.angle1-self.angle2)+"&deg;<br>Find the &ang;AOE:"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.angle1,self.angle2,self.angle3)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",'unit':"&deg;",'FunctionCall':self.FunctionCall}

    def ExplainType7(self,problem,answer,angle1,angle2,angle3):
        DisplayAngle1 = angle3-angle2
        DisplayAngle2 = 180-angle1-angle2
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+"&deg;"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "<i>Vertically opposite angles are equal.</i><br><br>"
        self.solution_text = self.solution_text + "Since AB and CD are two straight lines, &ang;COA and &ang;BOD are vertically opposite.<br><br>"
        self.solution_text = self.solution_text + "&ang;BOD = &ang;COA = "+str(DisplayAngle2)+"&deg;<br><br>"
        self.solution_text = self.solution_text + "&ang;COA = &ang;X + &ang;COE<br><br>"
        self.solution_text = self.solution_text + "&ang;X = &ang;COA - &ang;COE = "+str(DisplayAngle2)+"&deg; - "+str(DisplayAngle1)+"&deg;"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the missing angle is "+str(answer)+"&deg;</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer):
        try:
            return (int(answer)==int(InputAnswer))
        except ValueError:
            return False  