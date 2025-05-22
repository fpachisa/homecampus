'''
Created on April 04, 2011

Module: Volume
Generates "Calculating volume of cube and cuboid" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random
import string
from random import randint

class Volume:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        self.ProblemType = random.choice([self.GenerateProblemType1(),self.GenerateProblemType2(),
                                          random.choice([self.GenerateProblemType3(),self.GenerateProblemType4(),self.GenerateProblemType5()]),
                                          self.GenerateProblemType6(),self.GenerateProblemType7()])
        return self.ProblemType
        #return self.GenerateProblemType7()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            3:["ProblemType3","ProblemType4","ProblemType5"],
                            4:["ProblemType6",],
                            5:["ProblemType7",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemType4(),self.GenerateProblemType5()],
                                    4:[self.GenerateProblemType6()],
                                    5:[self.GenerateProblemType7()],
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
        #return self.GenerateProblemType6()
        
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
        The cuboid measures 8cm by 2cm by 5cm. Find its volume.'''
                  
        self.DimensionsSet = [2,3,4,5,6,7,8,9]
        self.dimensions = random.sample(self.DimensionsSet,3)
        self.length = self.dimensions[0]
        self.breadth = self.dimensions[1]
        self.height = self.dimensions[2]
        
        self.problem1 = "The cuboid measures "+str(self.length)+"cm by "+str(self.breadth)+"cm by "+str(self.height)+"cm. Find its volume."
        self.problem2 = "Find the volume of a cuboid which measures "+str(self.length)+"cm by "+str(self.breadth)+"cm by "+str(self.height)+"cm."
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.length*self.breadth*self.height
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.length,self.breadth,self.height)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",'unit':"cm<sup>3</sup>"}

    def ExplainType1(self,problem,answer,length,breadth,height):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+" cm<sup>3</sup>"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Volume of a cuboid = Length &times; Breadth &times; Height.<br><br>"
        self.solution_text = self.solution_text + "So the volume of the given cuboid = "+str(length)+" &times; "+str(breadth)+" &times; "+str(height)
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the volume of the cuboid is "+str(answer)+" cm<sup>3</sup></b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.:
        The each side of a cube measures 8cm. Find its volume.'''
                  
        self.DimensionsSet = [2,3,4,5,6,7,8,9]
        self.dimensions = random.sample(self.DimensionsSet,1)
        self.length = self.dimensions[0]
        
        self.problem1 = "Each side of a cube measures "+str(self.length)+"cm. Find its volume."
        self.problem2 = "Find the volume of cube whose each side measures "+str(self.length)+"cm."
        self.problem = random.choice([self.problem1,self.problem2])              
        
        self.answer = self.length*self.length*self.length
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.length)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",'unit':"cm<sup>3</sup>"}

    def ExplainType2(self,problem,answer,length):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+" cm<sup>3</sup>"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Volume of a cube = Length &times; Length &times; Length.<br><br>"
        self.solution_text = self.solution_text + "So the volume of the given cube = "+str(length)+" &times; "+str(length)+" &times; "+str(length)
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the volume of the cube is "+str(answer)+" cm<sup>3</sup></b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):
        '''e.g.:
        Express in cubic centimeters.'''
                  
        self.volume = randint(1,999)         

        self.problem = "Express in cubic centimeters:<br><br>"+str(self.volume)+" ml"              
        
        self.answer = self.volume
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.volume)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",'unit':"cm<sup>3</sup>"}

    def ExplainType3(self,problem,answer,volume):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+" cm<sup>3</sup>"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "1ml = 1 cm<sup>3</sup>."
        self.solution_text = self.solution_text + "<br><br><i><b>Hence "+str(volume)+" ml = "+str(answer)+" cm<sup>3</sup></b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):
        '''e.g.:
        Express in cubic centimeters.'''
                  
        self.volume = randint(2,9)         

        self.problem = "Express in cubic centimeters:<br><br>"+str(self.volume)+" litres"              
        
        self.answer = self.volume*1000
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.volume)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",'unit':"cm<sup>3</sup>"}

    def ExplainType4(self,problem,answer,volume):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+" cm<sup>3</sup>"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "1 <i>l</i> = 1000 ml<br><br>"
        self.solution_text = self.solution_text + "1 ml = 1 cm<sup>3</sup>. Therefore, 1 <i>l</i> = 1000 cm<sup>3</sup>"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence "+str(volume)+" <i>l</i> = "+str(answer)+" cm<sup>3</sup></b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):
        '''e.g.:
        Express in cubic centimeters.'''
                  
        self.volume1 = randint(2,9)
        self.volume2 = randint(1,999)         

        self.problem = "Express in cubic centimeters:<br><br>"+str(self.volume1)+" <i>l</i> "+str(self.volume2)+" ml"              
        
        self.answer = self.volume1*1000+self.volume2
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.volume1,self.volume2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",'unit':"cm<sup>3</sup>"}

    def ExplainType5(self,problem,answer,volume1,volume2):
        self.answer_text = "The correct answer is:<br>"+str(self.answer)+" cm<sup>3</sup>"
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "1 <i>l</i> = 1000 ml<br><br>"
        self.solution_text = self.solution_text + "1 ml = 1 cm<sup>3</sup>. Therefore, 1 <i>l</i> = 1000 cm<sup>3</sup>"
        self.solution_text = self.solution_text + "<br><br><i><b>Hence "+str(volume1)+" <i>l</i> "+str(volume2)+" ml = "+str(volume1)+" &times; 1000 + "+str(volume2) +" = "+str(answer)+" cm<sup>3</sup></b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):
        '''e.g.:
        Express in litres and millilitres.(Write your answer as 3 l 200 ml)'''
                  
        self.volume1 = randint(2,9)
        self.volume2 = randint(100,999)         

        self.problem = "Express in litres and millilitres:<br>(Write your answer as 3 l 200 ml)<br><br>"+str(self.volume1)+str(self.volume2)+" cm<sup>3</sup>"              
        
        self.answer = str(self.volume1)+" l "+str(self.volume2)+" ml"
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.volume1,self.volume2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",'unit':"",'CheckAnswerType':2}

    def ExplainType6(self,problem,answer,volume1,volume2):
        self.answer_text = "The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "1 <i>l</i> = 1000 ml<br><br>"
        self.solution_text = self.solution_text + "1 ml = 1 cm<sup>3</sup>. Therefore, 1 <i>l</i> = 1000 cm<sup>3</sup><br><br>"
        self.solution_text = self.solution_text + str(self.volume1)+str(self.volume2)+ " cm<sup>3</sup> = "+str(self.volume1)+str(self.volume2)+ "ml <br><br>"
        self.solution_text = self.solution_text + "= "+str(self.volume1)+str(self.volume2)+" ml = "+answer
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the correct answer is "+str(answer)+"</i></b>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):
        '''e.g.:
        A rectangular water tank measures 8cm by 2cm by 5cm. Find the max volume of water it can contain.'''
                  
        self.DimensionsSet = [2,3,4,5,6,7,8,9]
        self.dimensions = random.sample(self.DimensionsSet,3)
        self.length = self.dimensions[0]
        self.breadth = self.dimensions[1]
        self.height = self.dimensions[2]
        
        self.problem1 = "A rectangular water tank measures "+str(self.length)+"cm by "+str(self.breadth)+"cm by "+str(self.height)+"cm. Find the maximum volume of water it can contain."
        self.problem2 = "Find the max volume of water in a tank which measures "+str(self.length)+"cm by "+str(self.breadth)+"cm by "+str(self.height)+"cm."
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = self.length*self.breadth*self.height
        
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.length,self.breadth,self.height)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",'unit':"ml"}

    def ExplainType7(self,problem,answer,length,breadth,height):
        self.answer_text = "The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Volume of rectangular water tank = length &times; breadth &times; height<br><br>"
        self.solution_text = self.solution_text + "= "+str(length)+" &times; "+str(breadth)+" &times; "+str(height)+" = "+str(answer)
        self.solution_text = self.solution_text + "<br><br><i><b>Hence the maximum volume of water in the tank is "+str(answer)+" ml</i></b>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
        if CheckAnswerType == 2:
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"")
                answer = string.join(str(answer).split(),"")
                return answer==InputAnswer
            except ValueError:
                return False
        else:
            try:
                InputAnswer = float(str(InputAnswer))
                answer = float(str(answer))
                return answer==InputAnswer
            except ValueError:
                return False
            