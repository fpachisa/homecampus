'''
Created on Mar 10, 2012
Module: DecimalsFractions
Generates the "Decimals and Fractions" problems for Primary 4

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
from Utils import LcmGcf

class DecimalsFractions:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            3:["ProblemType3",],
                            4:["ProblemType4",],
                            5:["ProblemType5",],
                            6:["ProblemType6",],
                            7:["ProblemType7",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],
                                    5:[self.GenerateProblemType5(),],
                                    6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],
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
        #return self.GenerateProblemType7()

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
        Convert the fraction 1/5 to a decimal.'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.denominator = random.choice([2,5])
        self.numerator = randint(1,self.denominator-1)
                     
        self.problem = "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td>Convert the fraction<td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator)+"&nbsp;</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp; to a decimal.</td></tr></table>"     
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.numerator) / self.denominator

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.numerator,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType1(self,problem,answer,numerator,denominator):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        multiplier = 10 / denominator
        self.solution_text = self.solution_text + "First, Convert denominator to 10. To get that multiply both numerator and denominator by "+str(multiplier)+"<br><br>"      
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(self.numerator)+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(self.numerator)+" &times; "+str(multiplier)+"&nbsp;</u><br>&nbsp;"+str(self.denominator)+" &times; "+str(multiplier)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(self.numerator*multiplier)+"&nbsp;</u><br>"+str(self.denominator*multiplier)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(self.numerator*multiplier)+"&nbsp;</u><br>"+str(self.denominator*multiplier)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(answer)+"</td>"        
        self.solution_text = self.solution_text + "</tr></table>"
                
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>Hence, &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(self.numerator)+"</u><br>&nbsp;"+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;can be expressed in decimals as <i><b>"+str(answer)+"</i></b></td>"
        self.solution_text = self.solution_text + "</tr></table>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g.:
        Convert the fraction 1/4 to a decimal.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.denominator = random.choice([4,20,25,50])
        self.numerator = randint(1,self.denominator-1)
                     
        self.problem = "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td>Convert the fraction<td>"
        self.problem = self.problem + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp; to a decimal.</td></tr></table>"     
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.numerator) / self.denominator

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.numerator,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType2(self,problem,answer,numerator,denominator):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        multiplier = 100 / denominator
        self.solution_text = self.solution_text + "First, Convert denominator to 100. To get that multiply both numerator and denominator by "+str(multiplier)+"<br><br>"      
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(self.numerator)+" &times; "+str(multiplier)+"&nbsp;</u><br>&nbsp;"+str(self.denominator)+" &times; "+str(multiplier)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator*multiplier))+str(self.numerator*multiplier)+"&nbsp;"*len(str(self.denominator*multiplier))+"</u><br>"+"&nbsp;"*len(str(self.numerator*multiplier))+str(self.denominator*multiplier)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator*multiplier))+str(self.numerator*multiplier)+"&nbsp;"*len(str(self.denominator*multiplier))+"</u><br>"+"&nbsp;"*len(str(self.numerator*multiplier))+str(self.denominator*multiplier)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(answer)+"</td>"        
        self.solution_text = self.solution_text + "</tr></table>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>Hence, &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;can be expressed in decimals as <i><b>"+str(answer)+"</i></b></td>"
        self.solution_text = self.solution_text + "</tr></table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g.:
        Convert the fraction 7/5 to a decimal.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.denominator = random.choice([2,5])
        self.numerator = randint(self.denominator+1,self.denominator+10)
        while self.numerator%self.denominator == 0:
            self.numerator = randint(self.denominator+1,self.denominator+10)
                     
        self.problem = "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td>Convert the fraction<td>"
        self.problem = self.problem + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp; to a decimal.</td></tr></table>"     
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.numerator) / self.denominator

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.numerator,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType3(self,problem,answer,numerator,denominator):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        multiplier = 10 / denominator
        div,mod = divmod(numerator,denominator)
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(div*denominator)+" + "+str(mod)+"&nbsp;</u><br>"+"&nbsp;"*(len(str(div*denominator))+3)+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;"+str(div)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "<td> + &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(mod)+"&nbsp;</u><br>"+"&nbsp;"*len(str(mod))+str(self.denominator)+"</td>"       
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;"+str(div)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; + &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(mod)+" &times; "+str(multiplier)+"&nbsp;</u><br>&nbsp;"+str(self.denominator)+" &times; "+str(multiplier)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;"+str(div)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "<td> + &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator*multiplier))+str(mod*multiplier)+"&nbsp;"*len(str(self.denominator*multiplier))+"</u><br>"+"&nbsp;"*len(str(mod*multiplier))+str(self.denominator*multiplier)+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(div)+" + "+str(float(mod)/denominator)+"</td>"        
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(answer)+"</td>"        
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>Hence, &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;can be expressed in decimals as <i><b>"+str(answer)+"</i></b></td>"
        self.solution_text = self.solution_text + "</tr></table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain               
        
    def GenerateProblemType4(self):
        '''e.g.:
        Convert the fraction 7/4 to a decimal.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.denominator = random.choice([4,20,25,50])
        self.numerator = randint(self.denominator+1,self.denominator+10)
        
        while self.numerator%self.denominator == 0:
            self.numerator = randint(self.denominator+1,self.denominator+10)
                     
        self.problem = "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td>Convert the fraction<td>"
        self.problem = self.problem + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp; to a decimal.</td></tr></table>"     
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.numerator) / self.denominator

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.numerator,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType4(self,problem,answer,numerator,denominator):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        multiplier = 100 / denominator
        div,mod = divmod(numerator,denominator)
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(div*denominator)+" + "+str(mod)+"&nbsp;</u><br>"+"&nbsp;"*(len(str(div*denominator))+3)+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;"+str(div)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "<td> + &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(mod)+"&nbsp;</u><br>"+"&nbsp;"*len(str(mod))+str(self.denominator)+"</td>"       
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;"+str(div)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "<td> + &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(mod)+" &times; "+str(multiplier)+"&nbsp;</u><br>&nbsp;"+str(self.denominator)+" &times; "+str(multiplier)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;"+str(div)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "<td> + &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator*multiplier))+str(mod*multiplier)+"&nbsp;"*len(str(self.denominator*multiplier))+"</u><br>"+"&nbsp;"*len(str(mod*multiplier))+str(self.denominator*multiplier)+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(div)+" + "+str(float(mod)/denominator)+"</td>"        
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(answer)+"</td>"        
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>Hence, &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;can be expressed in decimals as <i><b>"+str(answer)+"</i></b></td>"
        self.solution_text = self.solution_text + "</tr></table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain               
        
    def GenerateProblemType5(self):
        '''e.g.:
        Convert the fraction 2 1/4 to a decimal.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.mixed = randint(1,9)
        self.denominator = random.choice([4,5,20,25,50])
        self.numerator = randint(1,self.denominator-1)
                     
        self.problem = "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td>Convert the fraction "+str(self.mixed)+"&nbsp;<td>"        
        self.problem = self.problem + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp; to a decimal.</td></tr></table>"     
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.mixed + float(self.numerator) / self.denominator

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.mixed,self.numerator,self.denominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType5(self,problem,answer,mixed,numerator,denominator):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        if denominator == 5:
            multiplier = 10 / denominator
        else:
            multiplier = 100 / denominator
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>"+str(mixed)+"&nbsp;</td>" 
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(mixed)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "<td> + &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"       
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>"+str(mixed)+"&nbsp;</td>" 
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(mixed)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "<td> + &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(numerator)+" &times; "+str(multiplier)+"&nbsp;</u><br>&nbsp;"+str(self.denominator)+" &times; "+str(multiplier)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;"+str(mixed)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "<td> + &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator*multiplier))+str(numerator*multiplier)+"&nbsp;"*len(str(self.denominator*multiplier))+"</u><br>"+"&nbsp;"*len(str(numerator*multiplier))+str(self.denominator*multiplier)+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>"+str(mixed)+"&nbsp;</td>" 
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(mixed)+" + "+str(float(numerator)/denominator)+"</td>"        
        self.solution_text = self.solution_text + "<td>&nbsp; = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(answer)+"</td>"        
        self.solution_text = self.solution_text + "</tr></table><br>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>Hence, &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(mixed)+"&nbsp;</td>" 
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(self.denominator))+str(self.numerator)+"&nbsp;"*len(str(self.denominator))+"</u><br>"+"&nbsp;"*len(str(self.numerator))+str(self.denominator)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;can be expressed in decimals as <i><b>"+str(answer)+"</i></b></td>"
        self.solution_text = self.solution_text + "</tr></table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain               
        
    def GenerateProblemType6(self):
        '''e.g.:
        Convert 0.2 to a fraction in its simplest form.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number = randint(1,9)
        self.FloatNumber = float(self.number) / 10
        
        self.problem = "Convert "+str(self.FloatNumber)+" to a fraction in its simplest form."

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2.</td>"
        self.problem = self.problem + "</tr></table>"
                        
        self.template = "EnterTypeProblems.html"
        
        gcf = LcmGcf.LcmGcf().find_gcf(self.number,10)        
        self.AnswerDenominator = 10/gcf
        self.AnswerNumerator = self.number/gcf
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        
        self.answer = str(self.answer1)+"/"+str(self.answer2)

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer1,self.answer2,self.FloatNumber,gcf)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}            

    def ExplainType6(self,problem,answer1,answer2,FloatNumber,gcf):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        self.answer_text = self.answer_text + "<td><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>"+str(FloatNumber)+" can be expressed as &nbsp;</td>" 
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(FloatNumber)+"&nbsp;</u><br>"+"&nbsp;"*len(str(FloatNumber))+str(1)+"</td>"    
        self.solution_text = self.solution_text + "</tr></table><br>"      
        
        self.solution_text = self.solution_text + "Now multiply both numerator and denominator by 10<br><br>" 
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(FloatNumber)+" &times; 10"+"&nbsp;</u><br>"+"&nbsp;"*len(str(FloatNumber))+"1 &times; 10</td>"    
        self.solution_text = self.solution_text + "<td>&nbsp;=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;&nbsp;"+str(int(FloatNumber*10))+"&nbsp;&nbsp;</u><br>"+"&nbsp;"*len(str(int(FloatNumber*10)))+"10</td>"
        self.solution_text = self.solution_text + "</tr></table><br>" 
        
        if gcf!=1:
            self.solution_text = self.solution_text + "The above fraction can be further simplified by dividing numerator and denominator by "+str(gcf)+"<br><br>"
        
            self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
            self.solution_text = self.solution_text + "<td><u>&nbsp;<del>"+str(int(FloatNumber*10))+"</del>"+str(int(FloatNumber*10/gcf))+"&nbsp;</u><br>&nbsp;<del>10</del>"+str(10/gcf)+"</td>"
            self.solution_text = self.solution_text + "</tr></table><br>" 
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>Hence, "+str(FloatNumber)+" can be expressed as &nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(answer2))+str(answer1)+"&nbsp;"*len(str(answer2))+"</u><br>"+"&nbsp;"*len(str(answer1))+str(answer2)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain               
        
    def GenerateProblemType7(self):
        '''e.g.:
        Convert 1.2 to a mixed fraction in its simplest form.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number = randint(11,99)
        while self.number%10==0:
            self.number = randint(11,99)
        self.FloatNumber = float(self.number) / 10
        
        self.problem = "Convert "+str(self.FloatNumber)+" to a mixed fraction in its simplest form."

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.7em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
                        
        self.template = "EnterTypeProblems.html"
        
        div,mod = divmod(self.number,10)
        gcf = LcmGcf.LcmGcf().find_gcf(mod,10)        
        self.mixed = div
        self.AnswerDenominator = 10/gcf
        self.AnswerNumerator = mod/gcf
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer3 = self.mixed
        
        self.answer = str(self.answer3)+" "+str(self.answer1)+"/"+str(self.answer2)

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer1,self.answer2,self.answer3,self.FloatNumber,gcf)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3}            

    def ExplainType7(self,problem,answer1,answer2,answer3,FloatNumber,gcf):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        self.answer_text = self.answer_text + "<td>"+str(answer3)+"&nbsp;</td>"
        self.answer_text = self.answer_text + "<td><u>"+"&nbsp;"*len(str(self.answer2))+str(self.answer1)+"&nbsp;"*len(str(self.answer2))+"</u><br>"+"&nbsp;"*len(str(self.answer1))+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text =  "<b><u>Problem</b></u>:<br/><br>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>"+str(FloatNumber)+" = "+str(answer3)+" + "+str(FloatNumber-answer3)+" = &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(answer3)+" +&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(FloatNumber-answer3)+"&nbsp;</u><br>"+"&nbsp;"*len(str(FloatNumber-answer3))+str(1)+"</td>"    
        self.solution_text = self.solution_text + "</tr></table><br>"      
        
        self.solution_text = self.solution_text + "Now multiply both numerator and denominator by 10<br><br>" 
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>"+str(answer3)+" +&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;"+str(FloatNumber-answer3)+" &times; 10"+"&nbsp;</u><br>"+"&nbsp;"*len(str(FloatNumber-answer3))+"1 &times; 10</td>"    
        self.solution_text = self.solution_text + "<td>&nbsp;=&nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(answer3)+" +&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>&nbsp;&nbsp;"+str(int((FloatNumber-answer3)*10))+"&nbsp;&nbsp;</u><br>"+"&nbsp;"*len(str(int((FloatNumber-answer3)*10)))+"10</td>"
        self.solution_text = self.solution_text + "</tr></table><br>" 
        
        if gcf!=1:
            self.solution_text = self.solution_text + "The above fraction can be further simplified by dividing numerator and denominator by "+str(gcf)+"<br><br>"
        
            self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
            self.solution_text = self.solution_text + "<td>"+str(answer3)+"</td>"
            self.solution_text = self.solution_text + "<td><u>&nbsp;<del>"+str(int((FloatNumber-answer3)*10))+"</del>"+str(int((FloatNumber-answer3)*10/gcf))+"&nbsp;</u><br>&nbsp;<del>10</del>"+str(10/gcf)+"</td>"
            self.solution_text = self.solution_text + "</tr></table><br>" 
        
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>Hence, "+str(FloatNumber)+" can be expressed as &nbsp;</td>"
        self.solution_text = self.solution_text + "<td>"+str(answer3)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><u>"+"&nbsp;"*len(str(answer2))+str(answer1)+"&nbsp;"*len(str(answer2))+"</u><br>"+"&nbsp;"*len(str(answer1))+str(answer2)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain               
                  
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswer == 2:
                if "/" in str(InputAnswer):             
                    try:
                        InputDenominator = int(str(InputAnswer).partition("/")[2])
                        InputNumerator = int(str(InputAnswer).partition("/")[0])            
                        AnswerDenominator = int(str(answer).partition("/")[2])
                        AnswerNumerator = int(str(answer).partition("/")[0])
                        return (AnswerNumerator==InputNumerator and AnswerDenominator==InputDenominator)
                    except ValueError:
                        return False
        elif CheckAnswer == 3:
                if " " in str(InputAnswer):             
                    try:
                        InputMixed = int(str(InputAnswer).partition(" ")[0])
                        RemainingInput = str(InputAnswer).partition(" ")[2]
                        InputDenominator = int(str(RemainingInput).partition("/")[2])
                        InputNumerator = int(str(RemainingInput).partition("/")[0])            
                        AnswerMixed = int(str(answer).partition(" ")[0])
                        RemainingInput = str(answer).partition(" ")[2]
                        AnswerDenominator = int(str(RemainingInput).partition("/")[2])
                        AnswerNumerator = int(str(RemainingInput).partition("/")[0])
                        return (AnswerMixed==InputMixed and AnswerNumerator==InputNumerator and AnswerDenominator==InputDenominator)
                    except ValueError:
                        return False                                     