'''
Created on Jan 18, 2011

Module: MultiplyDivide
Generates "Multiply and Divide Decimals by 10,100,1000s" problems for Primary 5

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

class MultiplyDivide:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        self.ProblemType = random.choice([self.GenerateProblemType1(),self.GenerateProblemType2()
                                          ,self.GenerateProblemTypeMCQ1(),self.GenerateProblemTypeMCQ2()])
        return self.ProblemType
        #return self.GenerateProblemTypeMCQ2()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4a","ProblemTypeMCQ4a","ProblemType4b","ProblemTypeMCQ4b",],
                            5:["ProblemType5","ProblemTypeMCQ5",],
                            6:["ProblemType6a","ProblemTypeMCQ6a","ProblemType6b","ProblemTypeMCQ6b",],
                            7:["ProblemType7a","ProblemTypeMCQ7a","ProblemType7b","ProblemTypeMCQ7b",],
                            8:["ProblemType8a","ProblemTypeMCQ8a","ProblemType8b","ProblemTypeMCQ8b","ProblemType8c","ProblemTypeMCQ8c",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4a(),self.GenerateProblemTypeMCQ4a(),self.GenerateProblemType4b(),self.GenerateProblemTypeMCQ4b(),],
                                    5:[self.GenerateProblemType5(),self.GenerateProblemTypeMCQ5(),],
                                    6:[self.GenerateProblemType6a(),self.GenerateProblemTypeMCQ6a(),self.GenerateProblemType6b(),self.GenerateProblemTypeMCQ6b(),],
                                    7:[self.GenerateProblemType7a(),self.GenerateProblemTypeMCQ7a(),self.GenerateProblemType7b(),self.GenerateProblemTypeMCQ7b(),],
                                    8:[self.GenerateProblemType8a(),self.GenerateProblemTypeMCQ8a(),self.GenerateProblemType8b(),self.GenerateProblemTypeMCQ8b(),self.GenerateProblemType8c(),self.GenerateProblemTypeMCQ8c(),],
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
        #return self.GenerateProblemTypeMCQ8c()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4a":self.GenerateProblemType4a(),
                            "ProblemType4b":self.GenerateProblemType4b(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6a":self.GenerateProblemType6a(),
                            "ProblemType6b":self.GenerateProblemType6b(),
                            "ProblemType7a":self.GenerateProblemType7a(),
                            "ProblemType7b":self.GenerateProblemType7b(),
                            "ProblemType8a":self.GenerateProblemType8a(),
                            "ProblemType8b":self.GenerateProblemType8b(),
                            "ProblemType8c":self.GenerateProblemType8c(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4a":self.GenerateProblemTypeMCQ4a(),
                            "ProblemTypeMCQ4b":self.GenerateProblemTypeMCQ4b(),
                            "ProblemTypeMCQ5":self.GenerateProblemTypeMCQ5(),
                            "ProblemTypeMCQ6a":self.GenerateProblemTypeMCQ6a(),
                            "ProblemTypeMCQ6b":self.GenerateProblemTypeMCQ6b(),
                            "ProblemTypeMCQ7a":self.GenerateProblemTypeMCQ7a(),
                            "ProblemTypeMCQ7b":self.GenerateProblemTypeMCQ7b(),
                            "ProblemTypeMCQ8a":self.GenerateProblemTypeMCQ8a(),
                            "ProblemTypeMCQ8b":self.GenerateProblemTypeMCQ8b(),
                            "ProblemTypeMCQ8c":self.GenerateProblemTypeMCQ8c(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g.:
        What is 0.382 x 1000?'''
        self.complexity_level = "easy"
        self.HCScore = 3        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.number = str(randint(1,9))+"."+str(randint(100,999))
        
        self.problem1 = "What is %s &times; %d?"%(self.number,self.multiplier)
        self.problem2 = "%s &times; %d = "%(self.number,self.multiplier)
        self.problem3 = "Multiply %s by %d."%(self.number,self.multiplier)
        self.problem4 = "What is the product of %s and %d?"%(self.number,self.multiplier)
        self.problem5 = "Find the product of %s and %d."%(self.number,self.multiplier)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4, self.problem5])
        
        self.answer = float(self.number)*self.multiplier          

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType1(self,problem,answer,number,multiplier):
        self.place = {2:10,3:100,4:1000}
        if(str(answer)[-2:]==".0"):
            answer1 = int(answer)
        else:
            answer1 = answer
        self.answer_text = "<br>The correct answer is:<br>"+str(answer1)
        
        self.solution_text = "<table><tr><td style='text-align:left'><b>"+number+" &times; " +str(multiplier)+"</b></td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+number+" &times; "+str(multiplier)[0]+" &times; "+str(self.place[len(str(multiplier))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(answer/self.place[len(str(multiplier))])+" &times; "+str(self.place[len(str(multiplier))])+"</td></tr>"
        if(str(len(str(multiplier))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer1)+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is multiplied by "+str(self.place[len(str(multiplier))])+", its decimal point moves "+str(len(str(multiplier))-1)+" place to the right.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer1)+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is multiplied by "+str(self.place[len(str(multiplier))])+", its decimal point moves "+str(len(str(multiplier))-1)+" places to the right.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Multiply-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.:
        What is 382 / 1000?'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.divisor = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = random.choice(["."+str(randint(100,900)),str(randint(1,9))+"."+str(randint(100,900))])
        self.number = str(self.divisor * float(self.answer))
                                
        self.problem1 = "Divide %s by %d."%(self.number,self.divisor)
        self.problem2 = "%s &divide; %d = "%(self.number,self.divisor)
        self.problem3 = "What is %s &divide; %d?"%(self.number,self.divisor)
        self.problem4 = "What do you get when you divide %s by %d?"%(self.number,self.divisor)
        self.problem5 = "Find the result of %s &divide; %d."%(self.number,self.divisor)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])

        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.divisor)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType2(self,problem,answer,number,divisor):
        self.place = {2:10,3:100,4:1000}
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)

        self.solution_text = "<table><tr><td style='text-align:left'><b>"+number+" &divide; " +str(divisor)+"</b></td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+number+" &divide; "+str(divisor)[0]+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(float(answer)*self.place[len(str(divisor))])+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        if(str(len(str(divisor))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" place to the left.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" places to the left.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Divide-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):
        '''e.g.:
        A [table] is <decimal> cm long. Find the total length of <10's, 100's or 1000's> such [tables] arranged end to end.'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.number = str(randint(1,9))+"."+str(randint(10,99))

        self.items = random.choice([['table cloth','table cloths'],['piece of cloth','pieces of cloth'],
                      ['strip of ribbon','strips of ribbon'],['piece of lace','pieces of lace'],['strip of tape','strips of tape'],
                      ['piece of wire','pieces of wire'],['piece of string','pieces of string'],['stick','sticks'],
                      ['straw','straws'],['pipe','pipes'],['pole','poles']])

        
        self.problem1 = "A "+self.items[0]+" is "+str(self.number)+" cm long. Find the total length of "+str(self.multiplier)+" such "+self.items[1]+" arranged end to end."
        self.problem2 = "What is the total length of "+str(self.multiplier)+" identical "+self.items[1]+" arranged end to end if each "+self.items[0]+" has a length of "+str(self.number)+" cm?"
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = float(self.number)*self.multiplier          
        self.unit = "cm"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number,self.multiplier,self.items[0],self.items[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'grade':5,'unit':self.unit,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType3(self,problem,answer,number,multiplier,item1,item2,unit):
        self.place = {2:10,3:100,4:1000}
        if(str(answer)[-2:]==".0"):
            answer1 = int(answer)
        else:
            answer1 = answer
        self.answer_text = "<br>The correct answer is:<br>"+str(answer1)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Length of a "+item1+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item2+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(multiplier)+"</td></tr></table><br>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left'>Total length</td><td>=</td><td style='text-align:left'>"+str(number)+" &times; " +str(multiplier)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(number)+" &times; "+str(multiplier)[0]+" &times; "+str(self.place[len(str(multiplier))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(answer/self.place[len(str(multiplier))])+" &times; "+str(self.place[len(str(multiplier))])+"</td></tr>"
        if(str(len(str(multiplier))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer1)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is multiplied by "+str(self.place[len(str(multiplier))])+", its decimal point moves "+str(len(str(multiplier))-1)+" place to the right.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer1)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is multiplied by "+str(self.place[len(str(multiplier))])+", its decimal point moves "+str(len(str(multiplier))-1)+" places to the right.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Multiply-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4a(self):
        '''e.g.:
        The total length of <10's, 100's or 1000's> identical [tables] arranged end to end is <decimal> cm. What is the length of each [table]?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = str(randint(1,9))+"."+str(randint(10,99))
        self.number = float(self.answer)*self.multiplier
        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice([['table cloth','table cloths'],['piece of cloth','pieces of cloth'],
                      ['strip of ribbon','strips of ribbon'],['piece of lace','pieces of lace'],['strip of tape','strips of tape'],
                      ['piece of wire','pieces of wire'],['piece of string','pieces of string'],['stick','sticks'],
                      ['straw','straws'],['pipe','pipes'],['pole','poles']])

        
        self.problem = "The total length of "+str(self.multiplier)+" identical "+self.items[1]+" arranged end to end is "+str(self.number)+" cm. What is the length of each "+self.items[0]+"?"
        
        self.unit = "cm"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4a(self.problem,self.answer,self.number,self.multiplier,self.items[0],self.items[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4a",'grade':5,'unit':self.unit,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType4a(self,problem,answer,number,divisor,item1,item2,unit):
        self.place = {2:10,3:100,4:1000}
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total length</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item2+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(divisor)+"</td></tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left'>Length of each "+item1+"</td><td>=</td><td style='text-align:left'>"+str(number)+" &divide; " +str(divisor)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(number)+" &divide; "+str(divisor)[0]+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(float(answer)*self.place[len(str(divisor))])+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        if(str(len(str(divisor))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" place to the left.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" places to the left.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Divide-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4b(self):
        '''e.g.:
        A [roll of string] <decimal> cm long is cut into <10's, 100's or 1000's> equal pieces. What is the length of each piece?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = str(randint(1,9))+"."+str(randint(10,99))
        self.number = float(self.answer)*self.multiplier
        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice(['roll of string','bale of cloth','roll of ribbon','spool of lace','roll of tape','roll of wire','spool of string','pipe','stick'])

        
        self.problem = "A "+self.items+" "+str(self.number)+" cm long is cut into "+str(self.multiplier)+" equal pieces. What is the length of each piece?"
        
        self.unit = "cm"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4b(self.problem,self.answer,self.number,self.multiplier,self.items,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4b",'grade':5,'unit':self.unit,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType4b(self,problem,answer,number,divisor,item1,unit):
        self.place = {2:10,3:100,4:1000}
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Original length of the "+item1+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of pieces</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(divisor)+"</td></tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left'>Length of each piece</td><td>=</td><td style='text-align:left'>"+str(number)+" &divide; " +str(divisor)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(number)+" &divide; "+str(divisor)[0]+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(float(answer)*self.place[len(str(divisor))])+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        if(str(len(str(divisor))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" place to the left.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" places to the left.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Divide-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5(self):
        '''e.g.:
        A [bag of flour] has a mass of <decimal> kg. What is the total mass of <10's, 100's or 1000's> such [bags of flour]?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.number = str(randint(1,3))+"."+str(randint(100,999))

        self.items = random.choice([['bag of flour','bags of flour'],['bag of soil','bags of soil'],['packet of sugar','packets of sugar'],
                                    ['box of colours','boxes of colours'],['can of paint','cans of paint'],['block of wood','blocks of wood'],
                                    ['book','books'],['box','boxes'],['package','packages'],['parcel','parcels'],])

        
        self.problem1 = "A "+self.items[0]+" has a mass of "+str(self.number)+" kg. What is the total mass of "+str(self.multiplier)+" such "+self.items[1]+"?"
        self.problem2 = "Find the total mass of "+str(self.multiplier)+" identical "+self.items[1]+" if each "+self.items[0]+" has a mass of "+str(self.number)+" kg."
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = float(self.number)*self.multiplier          
        self.unit = "kg"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number,self.multiplier,self.items[0],self.items[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'grade':5,'unit':self.unit,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType5(self,problem,answer,number,multiplier,item1,item2,unit):
        self.place = {2:10,3:100,4:1000}
        if(str(answer)[-2:]==".0"):
            answer1 = int(answer)
        else:
            answer1 = answer
        self.answer_text = "<br>The correct answer is:<br>"+str(answer1)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Mass of a "+item1+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item2+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(multiplier)+"</td></tr></table><br>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left'>Total mass</td><td>=</td><td style='text-align:left'>"+str(number)+" &times; " +str(multiplier)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(number)+" &times; "+str(multiplier)[0]+" &times; "+str(self.place[len(str(multiplier))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(float(answer)/self.place[len(str(multiplier))])+" &times; "+str(self.place[len(str(multiplier))])+"</td></tr>"
        if(str(len(str(multiplier))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer1)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is multiplied by "+str(self.place[len(str(multiplier))])+", its decimal point moves "+str(len(str(multiplier))-1)+" place to the right.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer1)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is multiplied by "+str(self.place[len(str(multiplier))])+", its decimal point moves "+str(len(str(multiplier))-1)+" places to the right.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Multiply-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6a(self):
        '''e.g.:
        The total mass of <10's, 100's or 1000's> identical [bags of flour] is <decimal> kg. Find the mass of each [bag of flour].'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = str(randint(1,3))+"."+str(randint(100,999))
        self.number = float(self.answer)*self.multiplier

        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice([['bags of flour','bag of flour'],['bags of soil','bag of soil'],['packets of sugar','packet of sugar'],
                                    ['boxes of colours','box of colours'],['cans of paint','can of paint'],['blocks of wood','block of wood'],
                                    ['books','book'],['boxes','box'],['packages','package'],['parcels','parcel'],])

        
        self.problem1 = "The total mass of "+str(self.multiplier)+" identical "+self.items[0]+" is "+str(self.number)+" kg. Find the mass of each "+self.items[1]+"."
        self.problem2 = "What is the mass of a "+self.items[1]+" if "+str(self.multiplier)+" such "+self.items[0]+" have a mass of "+str(self.number)+" kg altogether?"
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.unit = "kg"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6a(self.problem,self.answer,self.number,self.multiplier,self.items[0],self.items[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6a",'grade':5,'unit':self.unit,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType6a(self,problem,answer,number,divisor,item1,item2,unit):
        self.place = {2:10,3:100,4:1000}
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total mass</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item1+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(divisor)+"</td></tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left'>Mass of each "+item2+"</td><td>=</td><td style='text-align:left'>"+str(number)+" &divide; " +str(divisor)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(number)+" &divide; "+str(divisor)[0]+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(float(answer)*self.place[len(str(divisor))])+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        if(str(len(str(divisor))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" place to the left.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" places to the left.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Divide-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6b(self):
        '''e.g.:
        <decimal> grams of [flour] is packed equally into <10's, 100's or 1000's> [bags]. What is the mass of [flour] in each [bag]?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = str(randint(1,3))+"."+str(randint(100,999))
        self.number = float(self.answer)*self.multiplier
        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice([['wheat flour','bags','bag'],['fertilized soil','bags','bag'],['fine sugar','packets','packet'],
                                    ['fragrant rice','packets','packet'],['beads','packets','packet'],['coarse sand','packets','packet'],
                                    ['cake mix','packets','packet'],['Fuji apples','bags','bag'],['mandarins','bags','bag'],
                                    ['chocolate cookies','boxes','box'],['gummy sweets','packets','packet'],['powdered milk','boxes','box']])

        
        self.problem = str(self.number)+" kg of "+self.items[0]+" is packed equally into "+str(self.multiplier)+" "+self.items[1]+". What is the mass of "+self.items[0]+" in each "+self.items[2]+"?"
        
        self.unit = "kg"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6b(self.problem,self.answer,self.number,self.multiplier,self.items[1],self.items[2],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6b",'grade':5,'unit':self.unit,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType6b(self,problem,answer,number,divisor,item1,item2,unit):
        self.place = {2:10,3:100,4:1000}
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total mass</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item1+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(divisor)+"</td></tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left'>Mass of each "+item2+"</td><td>=</td><td style='text-align:left'>"+str(number)+" &divide; " +str(divisor)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(number)+" &divide; "+str(divisor)[0]+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(float(answer)*self.place[len(str(divisor))])+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        if(str(len(str(divisor))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" place to the left.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" places to the left.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Divide-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7a(self):
        '''e.g.:
        A [pail of water can hold] <decimal> l of [water]. Find the maximum volume of [water] that <10's, 100's or 1000's> such [pails can hold] altogether?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.number = "1."+str(random.randrange(50,950,50))
        self.items = random.choice([['pail of water can hold','water','pails can hold','pail','pails'],
                                    ['juice dispenser contains','juice','dispensers contain','dispenser','dispensers'],
                                    ['bottle of milk has','milk','bottles have','bottle','bottles'],
                                    ['tank contains','water','tanks contain','tank','tanks'],
                                    ['can of paint holds','paint','cans of paint hold','can','cans'],
                                    ['canister of oil has','oil','canisters of oil have','canister','canisters'],
                                    ['glass container has','liquid','glass containers have','container','containers'],
                                    ['can holds','beverage','cans hold','can','cans']])

        
        self.problem = "A "+self.items[0]+" "+str(self.number)+" litres of "+self.items[1]+". Find the maximum volume of "+self.items[1]+" that "+str(self.multiplier)+" such "+self.items[2]+" altogether?"
        
        self.answer = float(self.number)*self.multiplier          
        self.unit = "litres"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7a(self.problem,str(self.answer),self.number,self.multiplier,self.items[3],self.items[4],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7a",'grade':5,'unit':self.unit,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType7a(self,problem,answer,number,multiplier,item1,item2,unit):
        self.place = {2:10,3:100,4:1000}
        if answer.partition(".")[2]=="0":
            answer = answer.partition(".")[0]

        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a "+item1+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item2+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(multiplier)+"</td></tr></table><br>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left'>Total volume</td><td>=</td><td style='text-align:left'>"+str(number)+" &times; " +str(multiplier)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(number)+" &times; "+str(multiplier)[0]+" &times; "+str(self.place[len(str(multiplier))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(float(answer)/self.place[len(str(multiplier))])+" &times; "+str(self.place[len(str(multiplier))])+"</td></tr>"
        if(str(len(str(multiplier))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is multiplied by "+str(self.place[len(str(multiplier))])+", its decimal point moves "+str(len(str(multiplier))-1)+" place to the right.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is multiplied by "+str(self.place[len(str(multiplier))])+", its decimal point moves "+str(len(str(multiplier))-1)+" places to the right.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Multiply-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7b(self):
        '''e.g.:
        What is the maximum volume of [water] that <10's, 100's or 1000's> identical [pails can hold] if each [pail] has a capacity of <decimal> l?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.number = "1."+str(random.randrange(50,950,50))
        self.items = random.choice([['water','pails can hold','pail','pails'],['juice','juice dispensers contain','dispenser','dispensers'],
                                    ['milk','bottles have','bottle','bottles'],['water','tanks contain','tank','tanks'],
                                    ['paint','cans hold','can','cans'],['oil','canisters have','canister','canisters'],['liquid','glass containers have','glass container','glass containers'],
                                    ['beverage','cans hold','can','cans']])

        
        self.problem = "What is the maximum volume of "+self.items[0]+" that "+str(self.multiplier)+" identical "+self.items[1]+" if each "+self.items[2]+" has a capacity of "+str(self.number)+" litres?"
        
        self.answer = float(self.number)*self.multiplier          
        self.unit = "litres"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7b(self.problem,self.answer,self.number,self.multiplier,self.items[2],self.items[3],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7b",'grade':5,'unit':self.unit,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType7b(self,problem,answer,number,multiplier,item1,item2,unit):
        self.place = {2:10,3:100,4:1000}
        if(str(answer)[-2:]==".0"):
            answer1 = int(answer)
        else:
            answer1 = answer
        self.answer_text = "<br>The correct answer is:<br>"+str(answer1)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Volume of a "+item1+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item2+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(multiplier)+"</td></tr></table><br>"
        
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left'>Total volume</td><td>=</td><td style='text-align:left'>"+str(number)+" &times; " +str(multiplier)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(number)+" &times; "+str(multiplier)[0]+" &times; "+str(self.place[len(str(multiplier))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(float(answer)/self.place[len(str(multiplier))])+" &times; "+str(self.place[len(str(multiplier))])+"</td></tr>"
        if(str(len(str(multiplier))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer1)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is multiplied by "+str(self.place[len(str(multiplier))])+", its decimal point moves "+str(len(str(multiplier))-1)+" place to the right.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer1)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is multiplied by "+str(self.place[len(str(multiplier))])+", its decimal point moves "+str(len(str(multiplier))-1)+" places to the right.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Multiply-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8a(self):
        '''e.g.:
        <10's, 100's or 1000's> identical [pails can hold] a maximum of <decimal> l of [water] altogether. What is the capacity of each [pail]?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = str(randint(1,3))+"."+str(randint(100,999))
        self.number = float(self.answer)*self.multiplier
        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice([['pails can hold','water','pail','pails'],['juice dispensers contain','juice','dispenser','dispensers'],
                                    ['bottles of milk have','milk','bottle','bottles'],['tanks contain','water','tank','tanks'],
                                    ['cans of paint hold','paint','can','cans'],['canisters of oil have','oil','canister','canisters'],
                                    ['glass containers have','liquid','glass container','glass containers'],['cans hold','beverage','can','cans']])

        
        self.problem = str(self.multiplier)+" identical "+self.items[0]+" a maximum of "+str(self.number)+" litres of "+self.items[1]+" altogether. What is the capacity of each "+self.items[2]+"?"
        
        self.unit = "litres"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8a(self.problem,self.answer,self.number,self.multiplier,self.items[3],self.items[2],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8a",'grade':5,'unit':self.unit,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType8a(self,problem,answer,number,divisor,item1,item2,unit):
        self.place = {2:10,3:100,4:1000}
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item1+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(divisor)+"</td></tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left'>Capacity of each "+item2+"</td><td>=</td><td style='text-align:left'>"+str(number)+" &divide; " +str(divisor)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(number)+" &divide; "+str(divisor)[0]+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(float(answer)*self.place[len(str(divisor))])+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        if(str(len(str(divisor))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" place to the left.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" places to the left.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Divide-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8b(self):
        '''e.g.:
        Find the capacity of each [pail] if <10's, 100's or 1000's> such [pails] have a total capacity of <decimal> l.'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = str(randint(1,3))+"."+str(randint(100,999))
        self.number = float(self.answer)*self.multiplier
        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice([['pail','pails'],['juice dispenser','juice dispensers'],['bottle','bottles'],['water tank','water tanks'],
                                    ['bucket','buckets'],['oil canister','oil canisters'],['glass container','glass containers'],
                                    ['beverage can','beverage cans']])

        
        self.problem = "Find the capacity of each "+self.items[0]+" if "+str(self.multiplier)+" such "+self.items[1]+" have a total capacity of "+str(self.number)+" litres."
        
        self.unit = "litres"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8b(self.problem,self.answer,self.number,self.multiplier,self.items[1],self.items[0],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8b",'grade':5,'unit':self.unit,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType8b(self,problem,answer,number,divisor,item1,item2,unit):
        self.place = {2:10,3:100,4:1000}
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item1+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(divisor)+"</td></tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left'>Capacity of each "+item2+"</td><td>=</td><td style='text-align:left'>"+str(number)+" &divide; " +str(divisor)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(number)+" &divide; "+str(divisor)[0]+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(float(answer)*self.place[len(str(divisor))])+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        if(str(len(str(divisor))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" place to the left.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" places to the left.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Divide-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8c(self):
        '''e.g.:
        <decimal> l of [water] is [packed] equally into <10's, 100's or 1000's> [bottles]. What is the volume of water in each [bottle]?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = "."+str(random.randrange(100,800,50))
        self.number = float(self.answer)*self.multiplier

        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice([['water','packed','bottles','bottle'],['sparkling water','poured','glasses','glass'],
                                    ['mango juice','poured','cups','cup'],['strawberry milk','poured','mugs','mug'],
                                    ['chocolate milk','packed','cartons','carton'],['oil paint','packed','cans','can'],
                                    ['carbonated drink','poured','cups','cup'],['cooking oil','packed','cans','can'],
                                    ['liquid','poured','containers','container'],['green tea','poured','cups','cup']])

        
        self.problem = str(self.number)+" litres of "+self.items[0]+" is "+self.items[1]+" equally into "+str(self.multiplier)+" "+self.items[2]+". What is the volume of "+self.items[0]+" in each "+self.items[3]+"?"
        
        self.unit = "litre"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8c(self.problem,self.answer,self.number,self.multiplier,self.items[2],self.items[3],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType8c",'grade':5,'unit':self.unit,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}

    def ExplainType8c(self,problem,answer,number,divisor,item1,item2,unit):
        self.place = {2:10,3:100,4:1000}
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit

        self.solution_text = "<table><tr><td style='text-align:left' colspan='2'><br>Given,</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Total volume</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(number)+" "+unit+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'>Number of "+item1+"</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(divisor)+"</td></tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left'>Volume of each "+item2+"</td><td>=</td><td style='text-align:left'>"+str(number)+" &divide; " +str(divisor)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(number)+" &divide; "+str(divisor)[0]+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left' colspan='2'>"+str(float(answer)*self.place[len(str(divisor))])+" &divide; "+str(self.place[len(str(divisor))])+"</td></tr>"
        if(str(len(str(divisor))-1)=="1"): 
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" place to the left.</div></td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;vertical-align:top;'>=</td><td style='text-align:left;vertical-align:top;'>"+str(answer)+" "+unit+"</td><td style='text-align:left;padding-left:0px;padding-right:0px;padding-top:0px;'><div class='side' style='width:200px;font-size:.8em;'>When a decimal is divided by "+str(self.place[len(str(divisor))])+", its decimal point moves "+str(len(str(divisor))-1)+" places to the left.</div></td></tr></table>"
        self.solution_text = self.solution_text + '<br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-5/Decimal/Divide-by-10-100-1000" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;">Click here for a detailed explanation</font></a>'
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore):
        
        '''Removing correct answers from the wrongAnswers list'''
        wrongAnswers = filter(self.removeCorrectAnswer,wrongAnswers)
        
        self.answer1=''
        self.answer2=''
        self.answer3=''
        self.answer4=''
                             
        '''Randomly selecting 3 wrong answers and adding the correct answer as well'''
        try:
            wrongAnswers = random.sample(wrongAnswers,3)
        except ValueError:
            pass
            
        wrongAnswers.append(answer)
        random.shuffle(wrongAnswers)
        try:
            self.answer1 = str(wrongAnswers[0])
            self.answer2 = str(wrongAnswers[1])
            self.answer3 = str(wrongAnswers[2])
            self.answer4 = str(wrongAnswers[3])        
        except IndexError:
            pass
        try:
            self.value1 = self.answer1
            self.value2 = self.answer2
            self.value3 = self.answer3
            self.value4 = self.answer4
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'answer4':self.answer4,'value1':self.value1,'value2':self.value2
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type,
                'grade':5,"complexity_level":complexity_level,"HCScore":HCScore}       

    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        What is 0.382 x 1000?'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1"

        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(10,90,10),random.randrange(100,900,100),random.randrange(1000,9000,1000)])
        self.number = str(randint(1,9))+"."+str(randint(100,999))

        self.problem1 = "What is %s &times; %d?"%(self.number,self.multiplier)
        self.problem2 = "%s &times; %d = "%(self.number,self.multiplier)
        self.problem3 = "Multiply %s by %d."%(self.number,self.multiplier)
        self.problem4 = "What is the product of %s and %d?"%(self.number,self.multiplier)
        self.problem5 = "Find the product of %s and %d."%(self.number,self.multiplier)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4, self.problem5])
        self.answer = float(self.number)*self.multiplier     
        
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer*10))
        self.wrongAnswers.append(str(self.answer/10))
        self.wrongAnswers.append(str(self.answer/100))
        self.wrongAnswers.append(str(self.answer*100))
        self.wrongAnswers.append(self.number)
        self.wrongAnswers.append(str(self.multiplier))

        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1

        self.answer1 = self.answer
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
        if "." in self.answer and self.answer.partition(".")[2]==str(0):
            self.answer=self.answer.partition(".")[0]
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.number,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''        
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)
         
    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        What is 382 x 1000?'''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ2"
        
        self.divisor = random.choice([random.randrange(10,90,10),random.randrange(100,900,100),random.randrange(1000,9000,1000)])
        self.answer = float(random.choice(["."+str(randint(100,900)),str(randint(1,9))+"."+str(randint(100,900))]))
        self.number = str(self.divisor * float(self.answer))
        if "." in self.number and self.number.partition(".")[2]==str(0):
            self.number=self.number.partition(".")[0]
                                            
        self.problem1 = "Divide %s by %d"%(self.number,self.divisor)
        self.problem2 = "%s &divide; %d = "%(self.number,self.divisor)
        self.problem3 = "What is %s &divide; %d?"%(self.number,self.divisor)
        self.problem4 = "What do you get when you divide %s by %d?"%(self.number,self.divisor)
        self.problem5 = "Find the result of %s &divide; %d."%(self.number,self.divisor)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])
        
        self.template = "MCQTypeProblems.html"
                
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer*10))
        self.wrongAnswers.append(str(self.answer/10))
        self.wrongAnswers.append(str(self.answer*100))
        self.wrongAnswers.append(self.number)
        self.wrongAnswers.append(str(self.divisor))
          
        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1

        self.answer1 = self.answer
        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number,self.divisor)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
               
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)
         
    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
        A [table] is <decimal> cm long. Find the total length of <10's, 100's or 1000's> such [tables] arranged end to end.'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.number = str(randint(1,9))+"."+str(randint(10,99))

        self.items = random.choice([['table cloth','table cloths'],['piece of cloth','pieces of cloth'],
                      ['strip of ribbon','strips of ribbon'],['piece of lace','pieces of lace'],['strip of tape','strips of tape'],
                      ['piece of wire','pieces of wire'],['piece of string','pieces of string'],['stick','sticks'],
                      ['straw','straws'],['pipe','pipes'],['pole','poles']])

        
        self.problem1 = "A "+self.items[0]+" is "+str(self.number)+" cm long. Find the total length of "+str(self.multiplier)+" such "+self.items[1]+" arranged end to end."
        self.problem2 = "What is the total length of "+str(self.multiplier)+" identical "+self.items[1]+" arranged end to end if each "+self.items[0]+" has a length of "+str(self.number)+" cm?"
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = float(self.number)*self.multiplier          
        
        self.unit = "cm"
        
        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ3"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer*10))
        self.wrongAnswers.append(str(self.answer/10))
        self.wrongAnswers.append(str(self.answer/100))
        self.wrongAnswers.append(str(self.number))
        self.wrongAnswers.append(str(self.multiplier))
          
        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1
          
        self.answer = str(self.answer)
        if self.answer.partition(".")[2]=="0":
            self.answer = self.answer.partition(".")[0]                  
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,float(self.answer),self.number,self.multiplier,self.items[0],self.items[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
               
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)
         
    def GenerateProblemTypeMCQ4a(self):
        '''e.g.:
        The total length of <10's, 100's or 1000's> identical [tables] arranged end to end is <decimal> cm. What is the length of each [table]?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = str(randint(1,9))+"."+str(randint(10,99))
        self.number = float(self.answer)*self.multiplier
        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice([['table cloth','table cloths'],['piece of cloth','pieces of cloth'],
                      ['strip of ribbon','strips of ribbon'],['piece of lace','pieces of lace'],['strip of tape','strips of tape'],
                      ['piece of wire','pieces of wire'],['piece of string','pieces of string'],['stick','sticks'],
                      ['straw','straws'],['pipe','pipes'],['pole','poles']])

        
        self.problem = "The total length of "+str(self.multiplier)+" identical "+self.items[1]+" arranged end to end is "+str(self.number)+" cm. What is the length of each "+self.items[0]+"?"
        
        self.unit = "cm"

        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ4a"
        
        self.answer = float(self.answer)
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer*10))
        self.wrongAnswers.append(str(self.answer/10))
        self.dummyAdd = float(randint(100,150))/100
        self.wrongAnswers.append(str(self.answer+self.dummyAdd))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)/10))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)*10))
        self.wrongAnswers.append(str(self.number))
        self.wrongAnswers.append(str(self.multiplier))
          
        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1
          
        self.answer = str(self.answer)
        if self.answer.partition(".")[2]=="0":
            self.answer = self.answer.partition(".")[0]
                               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4a(self.problem,self.answer,self.number,self.multiplier,self.items[0],self.items[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
               
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)
         
    def GenerateProblemTypeMCQ4b(self):
        '''e.g.:
        A [roll of string] <decimal> cm long is cut into <10's, 100's or 1000's> equal pieces. What is the length of each piece?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = str(randint(1,9))+"."+str(randint(10,99))
        self.number = float(self.answer)*self.multiplier
        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice(['roll of string','bale of cloth','roll of ribbon','spool of lace','roll of tape','roll of wire','spool of string','pipe','stick'])

        
        self.problem = "A "+self.items+" "+str(self.number)+" cm long is cut into "+str(self.multiplier)+" equal pieces. What is the length of each piece?"
        
        self.unit = "cm"

        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ4b"
        
        
        self.answer = float(self.answer)
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer*10))
        self.wrongAnswers.append(str(self.answer/10))
        self.dummyAdd = float(randint(100,150))/100
        self.wrongAnswers.append(str(self.answer+self.dummyAdd))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)/10))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)*10))
        self.wrongAnswers.append(str(self.number))
        self.wrongAnswers.append(str(self.multiplier))
          
        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1
          
        self.answer = str(self.answer)
        if self.answer.partition(".")[2]=="0":
            self.answer = self.answer.partition(".")[0]
          
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4b(self.problem,self.answer,self.number,self.multiplier,self.items,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
               
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)
         
    def GenerateProblemTypeMCQ5(self):
        '''e.g.:
        A [bag of flour] has a mass of <decimal> kg. What is the total mass of <10's, 100's or 1000's> such [bags of flour]?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.number = str(randint(1,3))+"."+str(randint(100,999))

        self.items = random.choice([['bag of flour','bags of flour'],['bag of soil','bags of soil'],['packet of sugar','packets of sugar'],
                                    ['box of colours','boxes of colours'],['can of paint','cans of paint'],['block of wood','blocks of wood'],
                                    ['book','books'],['box','boxes'],['package','packages'],['parcel','parcels'],])

        
        self.problem1 = "A "+self.items[0]+" has a mass of "+str(self.number)+" kg. What is the total mass of "+str(self.multiplier)+" such "+self.items[1]+"?"
        self.problem2 = "Find the total mass of "+str(self.multiplier)+" identical "+self.items[1]+" if each "+self.items[0]+" has a mass of "+str(self.number)+" kg."
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.answer = float(self.number)*self.multiplier          
        self.unit = "kg"

        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ5"
        
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer/10))
        self.dummyAdd1 = randint(10,50)
        self.dummyAdd2 = randint(10,50)
        self.wrongAnswers.append(str(self.answer+self.dummyAdd1))
        self.wrongAnswers.append(str(self.answer+self.dummyAdd1+self.dummyAdd2))
        self.wrongAnswers.append(str(self.number))
        self.wrongAnswers.append(str(self.multiplier))
         
        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1
                  
        self.answer = str(self.answer)
        if self.answer.partition(".")[2]=="0":
            self.answer = self.answer.partition(".")[0]
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number,self.multiplier,self.items[0],self.items[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
               
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)
         
    def GenerateProblemTypeMCQ6a(self):
        '''e.g.:
        The total mass of <10's, 100's or 1000's> identical [bags of flour] is <decimal> kg. Find the mass of each [bag of flour].'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = str(randint(1,3))+"."+str(randint(100,999))
        self.number = float(self.answer)*self.multiplier

        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice([['bags of flour','bag of flour'],['bags of soil','bag of soil'],['packets of sugar','packet of sugar'],
                                    ['boxes of colours','box of colours'],['cans of paint','can of paint'],['blocks of wood','block of wood'],
                                    ['books','book'],['boxes','box'],['packages','package'],['parcels','parcel'],])

        
        self.problem1 = "The total mass of "+str(self.multiplier)+" identical "+self.items[0]+" is "+str(self.number)+" kg. Find the mass of each "+self.items[1]+"."
        self.problem2 = "What is the mass of a "+self.items[1]+" if "+str(self.multiplier)+" such "+self.items[0]+" have a mass of "+str(self.number)+" kg altogether?"
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.unit = "kg"

        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ6a"
        
        self.answer = float(self.answer)
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer*10))
        self.wrongAnswers.append(str(self.answer/10))
        self.dummyAdd = float(randint(100,150))/100
        self.wrongAnswers.append(str(self.answer+self.dummyAdd))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)/10))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)*10))
        self.wrongAnswers.append(str(self.number))
        self.wrongAnswers.append(str(self.multiplier))
          
        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1
          
        self.answer = str(self.answer)
        if self.answer.partition(".")[2]=="0":
            self.answer = self.answer.partition(".")[0]
                               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6a(self.problem,self.answer,self.number,self.multiplier,self.items[0],self.items[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
               
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)
         
    def GenerateProblemTypeMCQ6b(self):
        '''e.g.:
        <decimal> grams of [flour] is packed equally into <10's, 100's or 1000's> [bags]. What is the mass of [flour] in each [bag]?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = str(randint(1,3))+"."+str(randint(100,999))
        self.number = float(self.answer)*self.multiplier
        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice([['wheat flour','bags','bag'],['fertilized soil','bags','bag'],['fine sugar','packets','packet'],
                                    ['fragrant rice','packets','packet'],['beads','packets','packet'],['coarse sand','packets','packet'],
                                    ['cake mix','packets','packet'],['Fuji apples','bags','bag'],['mandarins','bags','bag'],
                                    ['chocolate cookies','boxes','box'],['gummy sweets','packets','packet'],['powdered milk','boxes','box']])

        
        self.problem = str(self.number)+" kg of "+self.items[0]+" is packed equally into "+str(self.multiplier)+" "+self.items[1]+". What is the mass of "+self.items[0]+" in each "+self.items[2]+"?"
        
        self.unit = "kg"

        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ6b"
        
        self.answer = float(self.answer)
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer*10))
        self.wrongAnswers.append(str(self.answer/10))
        self.dummyAdd = float(randint(100,150))/100
        self.wrongAnswers.append(str(self.answer+self.dummyAdd))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)/10))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)*10))
        self.wrongAnswers.append(str(self.number))
        self.wrongAnswers.append(str(self.multiplier))
          
        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1
          
        self.answer = str(self.answer)
        if self.answer.partition(".")[2]=="0":
            self.answer = self.answer.partition(".")[0]
                               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6b(self.problem,self.answer,self.number,self.multiplier,self.items[0],self.items[1],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
               
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)
         
    def GenerateProblemTypeMCQ7a(self):
        '''e.g.:
        A [pail of water can hold] <decimal> l of [water]. Find the maximum volume of [water] that <10's, 100's or 1000's> such [pails can hold] altogether?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.number = "1."+str(random.randrange(50,950,50))
        self.items = random.choice([['pail of water can hold','water','pails can hold','pail','pails'],
                                    ['juice dispenser contains','juice','dispensers contain','dispenser','dispensers'],
                                    ['bottle of milk has','milk','bottles have','bottle','bottles'],
                                    ['tank contains','water','tanks contain','tank','tanks'],
                                    ['can of paint holds','paint','cans of paint hold','can','cans'],
                                    ['canister of oil has','oil','canisters of oil have','canister','canisters'],
                                    ['glass container has','liquid','glass containers have','container','containers'],
                                    ['can holds','beverage','cans hold','can','cans']])

        
        self.problem = "A "+self.items[0]+" "+str(self.number)+" litres of "+self.items[1]+". Find the maximum volume of "+self.items[1]+" that "+str(self.multiplier)+" such "+self.items[2]+" altogether?"
        
        self.answer = float(self.number)*self.multiplier          
        self.unit = "litres"

        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ7a"
        
        self.answer = float(self.answer)
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer/10))
        self.dummyAdd1 = randint(10,50)
        self.dummyAdd2 = randint(10,50)
        self.wrongAnswers.append(str(self.answer+self.dummyAdd1))
        self.wrongAnswers.append(str(self.answer+self.dummyAdd1+self.dummyAdd2))
        self.wrongAnswers.append(str(self.number))
        self.wrongAnswers.append(str(self.multiplier))
          
        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1
          
        self.answer = str(self.answer)
        if self.answer.partition(".")[2]=="0":
            self.answer = self.answer.partition(".")[0]
                               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7a(self.problem,str(self.answer),self.number,self.multiplier,self.items[3],self.items[4],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
               
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)
         
    def GenerateProblemTypeMCQ7b(self):
        '''e.g.:
        What is the maximum volume of [water] that <10's, 100's or 1000's> identical [pails can hold] if each [pail] has a capacity of <decimal> l?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.number = "1."+str(random.randrange(50,950,50))
        self.items = random.choice([['water','pails can hold','pail','pails'],['juice','juice dispensers contain','dispenser','dispensers'],
                                    ['milk','bottles have','bottle','bottles'],['water','tanks contain','tank','tanks'],
                                    ['paint','cans hold','can','cans'],['oil','canisters have','canister','canisters'],['liquid','glass containers have','glass container','glass containers'],
                                    ['beverage','cans hold','can','cans']])

        
        self.problem = "What is the maximum volume of "+self.items[0]+" that "+str(self.multiplier)+" identical "+self.items[1]+" if each "+self.items[2]+" has a capacity of "+str(self.number)+" litres?"
        
        self.answer = float(self.number)*self.multiplier          
        self.unit = "litres"

        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ7b"
        
        self.answer = float(self.answer)
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer/10))
        self.dummyAdd1 = randint(10,50)
        self.dummyAdd2 = randint(10,50)
        self.wrongAnswers.append(str(self.answer+self.dummyAdd1))
        self.wrongAnswers.append(str(self.answer+self.dummyAdd1+self.dummyAdd2))
        self.wrongAnswers.append(str(self.number))
        self.wrongAnswers.append(str(self.multiplier))
          
        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1
          
        self.answer = str(self.answer)
        if self.answer.partition(".")[2]=="0":
            self.answer = self.answer.partition(".")[0]
                               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7b(self.problem,self.answer,self.number,self.multiplier,self.items[2],self.items[3],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
               
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)
         
    def GenerateProblemTypeMCQ8a(self):
        '''e.g.:
        <10's, 100's or 1000's> identical [pails can hold] a maximum of <decimal> l of [water] altogether. What is the capacity of each [pail]?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = str(randint(1,3))+"."+str(randint(100,999))
        self.number = float(self.answer)*self.multiplier
        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice([['pails can hold','water','pail','pails'],['juice dispensers contain','juice','dispenser','dispensers'],
                                    ['bottles of milk have','milk','bottle','bottles'],['tanks contain','water','tank','tanks'],
                                    ['cans of paint hold','paint','can','cans'],['canisters of oil have','oil','canister','canisters'],
                                    ['glass containers have','liquid','glass container','glass containers'],['cans hold','beverage','can','cans']])

        
        self.problem = str(self.multiplier)+" identical "+self.items[0]+" a maximum of "+str(self.number)+" litres of "+self.items[1]+" altogether. What is the capacity of each "+self.items[2]+"?"
        
        self.unit = "litres"

        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ8a"
        
        self.answer = float(self.answer)
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer*10))
        self.wrongAnswers.append(str(self.answer/10))
        self.dummyAdd = float(randint(100,150))/100
        self.wrongAnswers.append(str(self.answer+self.dummyAdd))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)/10))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)*10))
        self.wrongAnswers.append(str(self.number))
        self.wrongAnswers.append(str(self.multiplier))
          
        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1
          
        self.answer = str(self.answer)
        if self.answer.partition(".")[2]=="0":
            self.answer = self.answer.partition(".")[0]
                               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8a(self.problem,self.answer,self.number,self.multiplier,self.items[3],self.items[2],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
               
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)
         
    def GenerateProblemTypeMCQ8b(self):
        '''e.g.:
        Find the capacity of each [pail] if <10's, 100's or 1000's> such [pails] have a total capacity of <decimal> l.'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = str(randint(1,3))+"."+str(randint(100,999))
        self.number = float(self.answer)*self.multiplier
        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice([['pail','pails'],['juice dispenser','juice dispensers'],['bottle','bottles'],['water tank','water tanks'],
                                    ['bucket','buckets'],['oil canister','oil canisters'],['glass container','glass containers'],
                                    ['beverage can','beverage cans']])

        
        self.problem = "Find the capacity of each "+self.items[0]+" if "+str(self.multiplier)+" such "+self.items[1]+" have a total capacity of "+str(self.number)+" litres."
        
        self.unit = "litres"

        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ8b"
        
        self.answer = float(self.answer)
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer*10))
        self.wrongAnswers.append(str(self.answer/10))
        self.dummyAdd = float(randint(100,150))/100
        self.wrongAnswers.append(str(self.answer+self.dummyAdd))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)/10))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)*10))
        self.wrongAnswers.append(str(self.number))
        self.wrongAnswers.append(str(self.multiplier))
          
        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1
          
        self.answer = str(self.answer)
        if self.answer.partition(".")[2]=="0":
            self.answer = self.answer.partition(".")[0]
                               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8b(self.problem,self.answer,self.number,self.multiplier,self.items[1],self.items[0],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
               
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)
         
    def GenerateProblemTypeMCQ8c(self):
        '''e.g.:
        <decimal> l of [water] is [packed] equally into <10's, 100's or 1000's> [bottles]. What is the volume of water in each [bottle]?'''
        self.complexity_level = "medium"
        self.HCScore = 5        
        '''Randomly choose multiplier that is 10,100 or 1000s'''
        self.multiplier = random.choice([random.randrange(20,90,10),random.randrange(200,900,100),random.randrange(2000,9000,1000)])
        self.answer = "."+str(random.randrange(100,800,50))
        self.number = float(self.answer)*self.multiplier

        if str(self.number).partition(".")[2]=="0":
            self.number = int(self.number)        

        self.items = random.choice([['water','packed','bottles','bottle'],['sparkling water','poured','glasses','glass'],
                                    ['mango juice','poured','cups','cup'],['strawberry milk','poured','mugs','mug'],
                                    ['chocolate milk','packed','cartons','carton'],['oil paint','packed','cans','can'],
                                    ['carbonated drink','poured','cups','cup'],['cooking oil','packed','cans','can'],
                                    ['liquid','poured','containers','container'],['green tea','poured','cups','cup']])

        
        self.problem = str(self.number)+" litres of "+self.items[0]+" is "+self.items[1]+" equally into "+str(self.multiplier)+" "+self.items[2]+". What is the volume of "+self.items[0]+" in each "+self.items[3]+"?"
        
        self.unit = "litre"

        self.template = "MCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ8c"
        
        self.answer = float(self.answer)
        self.wrongAnswers = []
        self.wrongAnswers.append(str(self.answer*10))
        self.wrongAnswers.append(str(self.answer/10))
        self.dummyAdd = float(randint(100,150))/100
        self.wrongAnswers.append(str(self.answer+self.dummyAdd))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)/10))
        self.wrongAnswers.append(str((self.answer+self.dummyAdd)*10))
        self.wrongAnswers.append(str(self.number))
        self.wrongAnswers.append(str(self.multiplier))
          
        '''Removing the zero if the answer is e.g. 123.0'''
        i = 0
        for i in range(len(self.wrongAnswers)):
            if "." in self.wrongAnswers[i] and self.wrongAnswers[i].partition(".")[2]==str(0):
                self.wrongAnswers[i]=self.wrongAnswers[i].partition(".")[0]
            i=i+1
          
        self.answer = str(self.answer)
        if self.answer.partition(".")[2]=="0":
            self.answer = self.answer.partition(".")[0]
                               
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8c(self.problem,self.answer,self.number,self.multiplier,self.items[2],self.items[3],self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
               
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.complexity_level,self.HCScore)

    def checkAnswer(self,template,answer,InputAnswer):
        try:
            return (float(answer)==float(InputAnswer))
        except ValueError:
            return False  