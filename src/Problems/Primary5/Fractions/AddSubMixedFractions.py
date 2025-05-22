'''
Created on Feb 20, 2011

Module: AddSubMixedFractions
Generates "Addition subtraction mixed fractions" problems for Primary 5

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
from Utils import LcmGcf
from decimal import Decimal

class AddSubMixedFractions:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        self.RandomQ = randint(1,10)
        #70% of the time it will generate MCQs
        if self.RandomQ > 3:
            self.ProblemType = random.choice([self.GenerateProblemTypeMCQ1(),self.GenerateProblemTypeMCQ2()])
        else:
            self.ProblemType = random.choice([self.GenerateProblemType1(),self.GenerateProblemType2()])
        return self.ProblemType
        #return self.GenerateProblemTypeMCQ2()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:"ProblemType1",2:"ProblemTypeMCQ2",3:"ProblemTypeMCQ1",4:"ProblemType2",}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemTypeMCQ2(),3:self.GenerateProblemTypeMCQ1(),
                                    4:self.GenerateProblemType2(),}
        
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
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        ''' Generating 2 proper unlike fractions(numerator>denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(self.denominator1+1,24)
        self.numerator2 = randint(self.denominator2+1,24)
        '''making sure mixed fraction is generated'''
        while self.numerator1%self.denominator1 == 0:
            self.numerator1 = randint(self.denominator1+1,24)
        while self.numerator2%self.denominator2 == 0:
            self.numerator2 = randint(self.denominator2+1,24)
        self.mixed1, self.numerator11 = divmod(self.numerator1,self.denominator1)
        self.mixed2, self.numerator22 = divmod(self.numerator2,self.denominator2)
        
        self.problem = "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<tr><td valing='center'>"+str(self.mixed1)+"</td>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator11)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td valign='center'>&nbsp; + &nbsp;</td>"
        self.problem = self.problem + "<td valing='center'>"+str(self.mixed2)+"</td>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator22)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td align='center'>&nbsp;=</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator = (self.numerator1*self.AnswerDenominator/self.denominator1 + self.numerator2*self.AnswerDenominator/self.denominator2)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.mixed1,self.mixed2,self.numerator11,self.numerator22,self.denominator1,self.denominator2,self.AnswerDenominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1"}            
    
    def ExplainType1(self,problem,answer1,answer2,mixed1,mixed2,numerator11,numerator22,denominator1,denominator2,AnswerDenominator):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))
        #Adding the simplified fraction if possible
        if(answer1%answer2!=0):
            if gcf!=1:
                self.SimpleAnswer1 = int(answer1)/gcf
                self.SimpleAnswer2 = int(answer2)/gcf
                if self.SimpleAnswer2!=1:
                    self.SimpleMixed1,self.SimpleAnswer11 = divmod(self.SimpleAnswer1,self.SimpleAnswer2)
                    self.answer_text = self.answer_text + "<td valign='center'>"+str(self.SimpleMixed1)+"</td>"
                    self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer11)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"              
                else:
                    self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.mixed1,self.answer11 = divmod(answer1,answer2)
        self.answer_text = self.answer_text + "<td valign='center'>"+str(self.mixed1)+"</td>"
        if self.answer11!=0:
            self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer11)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "To add mixed fractions, convert each mixed fraction to an improper fraction.<br>"
        self.solution_text = self.solution_text + "Multiply whole number by denominator, then add numerator to the product to get the new numerator.<br>"
        self.solution_text = self.solution_text + "Denominator stays the same.<br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(mixed1)+" &times; "+str(denominator1)+" + "+str(numerator11)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td valign='center'> + </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(mixed2)+" &times; "+str(denominator2)+" + "+str(numerator22)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'> = </td>"
        numerator1 = (mixed1*denominator1+numerator11)
        numerator2 = (mixed2*denominator2+numerator22)
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td valign='center'> + </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"

        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td valign='center'> and </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'> do not have same denominator. They are unlike fractions.</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "To add unlike fractions, first change them to like fractions.<br><br>"
        self.solution_text = self.solution_text + "Find the common multiple of denominators. In this case common multiple of "+str(denominator1)+" and "+str(denominator2)+" is "+str(AnswerDenominator)+"<br><br>"
        self.solution_text = self.solution_text + "Multiply numerator and denominator of both fractions so that denominators become "+str(AnswerDenominator)+"<br><br>"
        multiplier1 = AnswerDenominator/denominator1
        multiplier2 = AnswerDenominator/denominator2
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(multiplier1)+"</td>"
        self.solution_text = self.solution_text + "<td valign='center'> + </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+" &times; "+str(multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(multiplier2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'> = </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1*multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1*multiplier1)+"</td>"
        self.solution_text = self.solution_text + "<td valign='center'> + </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2*multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2*multiplier2)+"</td></tr></table>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is </td><td align='center'><u>&nbsp;"+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td>"               
        self.solution_text = self.solution_text + "</tr></table>"        
        self.solution_text = self.solution_text + "This can be expressed as mixed fraction"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
        if(answer1%answer2!=0):
            if gcf!=1:
                self.SimpleAnswer1 = int(answer1)/gcf
                self.SimpleAnswer2 = int(answer2)/gcf
                if self.SimpleAnswer2!=1:
                    self.SimpleMixed1,self.SimpleAnswer11 = divmod(self.SimpleAnswer1,self.SimpleAnswer2)
                    self.solution_text = self.solution_text + "<td valign='center'>"+str(self.SimpleMixed1)+"</td>"
                    self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer11)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"              
                else:
                    self.solution_text = self.solution_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
                self.solution_text = self.solution_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.mixed1,self.answer11 = divmod(answer1,answer2)
        self.solution_text = self.solution_text + "<td valign='center'>"+str(self.mixed1)+"</td>"
        if self.answer11!=0:
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.answer11)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.solution_text = self.solution_text + "</tr></table>"        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):
        ''' Generating 2 proper unlike fractions(numerator<denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(self.denominator1+1,24)
        self.numerator2 = randint(self.denominator2+1,24)
        while self.numerator1%self.denominator1 == 0:
            self.numerator1 = randint(self.denominator1+1,24)
        while self.numerator2%self.denominator2 == 0:
            self.numerator2 = randint(self.denominator2+1,24)
        self.mixed1, self.numerator11 = divmod(self.numerator1,self.denominator1)
        self.mixed2, self.numerator22 = divmod(self.numerator2,self.denominator2)

        '''Making sure that both fractions are not same'''
        if (Decimal(self.numerator1)/Decimal(self.denominator1)-Decimal(self.numerator2)/Decimal(self.denominator2)==0):
            self.numerator1 = self.numerator1 + 1
            self.mixed1, self.numerator11 = divmod(self.numerator1,self.denominator1)
            
        self.problem = "<table id='fractionTable' class='FractionsTable'>"
        if (Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2)):
            self.problem = self.problem + "<tr><td valing='center'>"+str(self.mixed1)+"</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator11)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td valign='center'>&nbsp; - &nbsp;</td>"
            self.problem = self.problem + "<td valing='center'>"+str(self.mixed2)+"</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator22)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.flag = 1
        else:
            self.problem = self.problem + "<tr><td valing='center'>"+str(self.mixed2)+"</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator22)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td valign='center'>&nbsp; - &nbsp;</td>"
            self.problem = self.problem + "<td valing='center'>"+str(self.mixed1)+"</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator11)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.flag = 2            
        self.problem = self.problem + "<td align='center'>&nbsp;=</td>"
        self.problem = self.problem + "</tr></table>"

        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator = abs(self.numerator1*self.AnswerDenominator/self.denominator1 - self.numerator2*self.AnswerDenominator/self.denominator2)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer1,self.answer2,self.mixed1,self.mixed2,self.numerator11,self.numerator22,self.denominator1,self.denominator2,self.AnswerDenominator,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''      

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2"}            
    
    def ExplainType2(self,problem,answer1,answer2,mixed1,mixed2,numerator11,numerator22,denominator1,denominator2,AnswerDenominator,flag):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))         
        '''Adding the simplified fraction if possible'''
        if(answer1%answer2!=0):
            if gcf>1:
                self.SimpleAnswer1 = int(answer1)/gcf
                self.SimpleAnswer2 = int(answer2)/gcf
                if self.SimpleAnswer2!=1:
                    self.SimpleMixed1,self.SimpleAnswer11 = divmod(self.SimpleAnswer1,self.SimpleAnswer2)
                    if self.SimpleMixed1!=0:
                        self.answer_text = self.answer_text + "<td valign='center'>"+str(self.SimpleMixed1)+"</td>"
                    self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer11)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"              
                else:
                    self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.mixed1,self.answer11 = divmod(answer1,answer2)
        if self.mixed1!=0:
            self.answer_text = self.answer_text + "<td valign='center'>"+str(self.mixed1)+"</td>"
        if self.answer11!=0:
            self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer11)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "To subtract mixed fractions, convert each mixed fraction to an improper fraction.<br>"
        self.solution_text = self.solution_text + "Multiply whole number by denominator, then add numerator to the product to get the new numerator.<br>"
        self.solution_text = self.solution_text + "Denominator stays the same.<br>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        numerator1 = (mixed1*denominator1+numerator11)
        numerator2 = (mixed2*denominator2+numerator22)
        if flag == 1:
            self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(mixed1)+" &times; "+str(denominator1)+" + "+str(numerator11)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(mixed2)+" &times; "+str(denominator2)+" + "+str(numerator22)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'> = </td>"   
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
        elif flag == 2:
            self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(mixed2)+" &times; "+str(denominator2)+" + "+str(numerator22)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(mixed1)+" &times; "+str(denominator1)+" + "+str(numerator11)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'> = </td>"   
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"            
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td valign='center'> and </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'> do not have same denominator. They are unlike fractions.</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "To subtract unlike fractions, first change them to like fractions.<br><br>"
        self.solution_text = self.solution_text + "Find the common multiple of denominators. In this case common multiple of "+str(denominator1)+" and "+str(denominator2)+" is "+str(AnswerDenominator)+"<br><br>"
        self.solution_text = self.solution_text + "Multiply numerator and denominator of both fractions so that denominators become "+str(AnswerDenominator)+"<br><br>"
        multiplier1 = AnswerDenominator/denominator1
        multiplier2 = AnswerDenominator/denominator2
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        if flag == 1:
            self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+" &times; "+str(multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'> = </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1*multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1*multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2*multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2*multiplier2)+"</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator2)+" &times; "+str(multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'> = </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2*multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2*multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1*multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1*multiplier1)+"</td></tr></table>"           
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the correct answer is </td><td align='center'><u>&nbsp;"+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td>"               
        self.solution_text = self.solution_text + "</tr></table>"        
        if(answer1>answer2):
            self.solution_text = self.solution_text + "This can be expressed as mixed fraction"
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr>"
            if(answer1%answer2!=0):
                if gcf!=1:
                    self.SimpleAnswer1 = int(answer1)/gcf
                    self.SimpleAnswer2 = int(answer2)/gcf
                    if self.SimpleAnswer2!=1:
                        self.SimpleMixed1,self.SimpleAnswer11 = divmod(self.SimpleAnswer1,self.SimpleAnswer2)
                        self.solution_text = self.solution_text + "<td valign='center'>"+str(self.SimpleMixed1)+"</td>"
                        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer11)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"              
                    else:
                        self.solution_text = self.solution_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
                    self.solution_text = self.solution_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
            self.mixed1,self.answer11 = divmod(answer1,answer2)
            self.solution_text = self.solution_text + "<td valign='center'>"+str(self.mixed1)+"</td>"
            if self.answer11!=0:
                self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.answer11)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
                   
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type):
                                    
        '''Randomly selecting 3 wrong answers and adding the correct answer as well'''
        try:
            wrongAnswers = random.sample(wrongAnswers,3)
        except ValueError:
            pass
            
        wrongAnswers.append(answer)
        random.shuffle(wrongAnswers)
        try:
            self.answer1 = wrongAnswers[0]
            self.answer2 = wrongAnswers[1]
            self.answer3 = wrongAnswers[2]
            self.answer4 = wrongAnswers[3]        
        except IndexError:
            pass
        try:
            self.value1 = str(self.answer1[0])+"/"+str(self.answer1[1])+"/"+str(self.answer1[2])
            self.value2 = str(self.answer2[0])+"/"+str(self.answer2[1])+"/"+str(self.answer2[2])
            self.value3 = str(self.answer3[0])+"/"+str(self.answer3[1])+"/"+str(self.answer3[2])
            self.value4 = str(self.answer4[0])+"/"+str(self.answer4[1])+"/"+str(self.answer4[2])
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answerM1':self.answer1[0],'answerN1':self.answer1[1],'answerD1':self.answer1[2],
                'answerM2':self.answer2[0],'answerN2':self.answer2[1],'answerD2':self.answer2[2],
                'answerM3':self.answer3[0],'answerN3':self.answer3[1],'answerD3':self.answer3[2],
                'answerM4':self.answer4[0],'answerN4':self.answer4[1],'answerD4':self.answer4[2],
                'value1':self.value1,'value2':self.value2,'value3':self.value3,'value4':self.value4,
                'explain':explain,'problem_type':problem_type}       

    def GenerateProblemTypeMCQ1(self):
        ''' Generating 2 proper unlike fractions(numerator>denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(self.denominator1+1,24)
        self.numerator2 = randint(self.denominator2+1,24)
        while self.numerator1%self.denominator1 == 0:
            self.numerator1 = randint(self.denominator1+1,24)
        while self.numerator2%self.denominator2 == 0:
            self.numerator2 = randint(self.denominator2+1,24)
        self.mixed1, self.numerator11 = divmod(self.numerator1,self.denominator1)
        self.mixed2, self.numerator22 = divmod(self.numerator2,self.denominator2)
        
        self.problem = "<table id='fractionTable' class='FractionsTable'>"
        self.problem = self.problem + "<tr><td valing='center'>"+str(self.mixed1)+"</td>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator11)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td valign='center'>&nbsp; + &nbsp;</td>"
        self.problem = self.problem + "<td valing='center'>"+str(self.mixed2)+"</td>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator22)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td align='center'>&nbsp;=</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator = (self.numerator1*self.AnswerDenominator/self.denominator1 + self.numerator2*self.AnswerDenominator/self.denominator2)
        
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)

        '''Simplifying the fraction if possible'''
        self.SimpleAnswerNumerator = self.AnswerNumerator/gcf
        self.SimpleAnswerDenominator = self.AnswerDenominator/gcf
        
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator 
        
        self.SimpleAnswer1 = self.SimpleAnswerNumerator
        self.SimpleAnswer2 = self.SimpleAnswerDenominator
        self.AnswerMixed1,self.answer11 = divmod(self.SimpleAnswer1,self.SimpleAnswer2)
        self.answer = [self.AnswerMixed1,self.answer11,self.SimpleAnswer2]
        
        self.wrongAnswers = []
        '''generating 5 wrong answers and making sure any of it is not equal to the correct answer'''
        i = 0
        while i!=5:
            self.WrongDenominator = randint(2,12)
            self.WrongNumerator = randint(self.WrongDenominator+1,24)            
            if(Decimal(self.WrongNumerator)/Decimal(self.WrongDenominator)!=Decimal(self.AnswerNumerator)/Decimal(self.AnswerDenominator) and self.WrongNumerator%self.WrongDenominator!=0):
                self.WrongMixed,self.WrongNumerator = divmod(self.WrongNumerator,self.WrongDenominator)
                if [self.WrongMixed,self.WrongNumerator,self.WrongDenominator] not in self.wrongAnswers:
                    self.wrongAnswers.append([self.WrongMixed,self.WrongNumerator,self.WrongDenominator])
                    i = i+1
                           
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ1"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.mixed1,self.mixed2,self.numerator11,self.numerator22,self.denominator1,self.denominator2,self.AnswerDenominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)      

    def GenerateProblemTypeMCQ2(self):
        ''' Generating 2 proper unlike fractions(numerator<denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(self.denominator1+1,24)
        self.numerator2 = randint(self.denominator2+1,24)
        while self.numerator1%self.denominator1 == 0:
            self.numerator1 = randint(self.denominator1+1,24)
        while self.numerator2%self.denominator2 == 0:
            self.numerator2 = randint(self.denominator2+1,24)
        self.mixed1, self.numerator11 = divmod(self.numerator1,self.denominator1)
        self.mixed2, self.numerator22 = divmod(self.numerator2,self.denominator2)

        '''Making sure that both fractions are not same'''
        if (Decimal(self.numerator1)/Decimal(self.denominator1)-Decimal(self.numerator2)/Decimal(self.denominator2)==0):
            self.numerator1 = self.numerator1 + 1
            
        self.problem = "<table id='fractionTable' class='FractionsTable'>"
        if (Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2)):
            self.problem = self.problem + "<tr><td valing='center'>"+str(self.mixed1)+"</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator11)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td valign='center'>&nbsp; - &nbsp;</td>"
            self.problem = self.problem + "<td valing='center'>"+str(self.mixed2)+"</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator22)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.flag = 1
        else:
            self.problem = self.problem + "<tr><td valing='center'>"+str(self.mixed2)+"</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator22)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td valign='center'>&nbsp; - &nbsp;</td>"
            self.problem = self.problem + "<td valing='center'>"+str(self.mixed1)+"</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator11)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.flag = 2            
        self.problem = self.problem + "<td align='center'>&nbsp;=</td>"
        self.problem = self.problem + "</tr></table>"

        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator = abs(self.numerator1*self.AnswerDenominator/self.denominator1 - self.numerator2*self.AnswerDenominator/self.denominator2)
        
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)

        '''Simplifying the fraction if possible'''
        self.SimpleAnswerNumerator = self.AnswerNumerator/gcf
        self.SimpleAnswerDenominator = self.AnswerDenominator/gcf
        
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator 
        
        self.SimpleAnswer1 = self.SimpleAnswerNumerator
        self.SimpleAnswer2 = self.SimpleAnswerDenominator
        self.AnswerMixed1,self.answer11 = divmod(self.SimpleAnswer1,self.SimpleAnswer2)
        self.answer = [self.AnswerMixed1,self.answer11,self.SimpleAnswer2]
        
        self.wrongAnswers = []
        '''generating 5 wrong answers and making sure any of it is not equal to the correct answer'''
        i = 0
        while i!=5:
            self.WrongDenominator = randint(2,12)
            self.WrongNumerator = random.choice([randint(1,self.WrongDenominator),randint(4,24)])            
            if(Decimal(self.WrongNumerator)/Decimal(self.WrongDenominator)!=Decimal(self.answer1)/Decimal(self.answer2)):
                self.WrongMixed,self.WrongNumerator = divmod(self.WrongNumerator,self.WrongDenominator)
                if [self.WrongMixed,self.WrongNumerator,self.WrongDenominator] not in self.wrongAnswers:
                    self.wrongAnswers.append([self.WrongMixed,self.WrongNumerator,self.WrongDenominator])
                    i = i+1                          
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ2"
        
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer1,self.answer2,self.mixed1,self.mixed2,self.numerator11,self.numerator22,self.denominator1,self.denominator2,self.AnswerDenominator,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''  
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)      
   
    def checkAnswer(self,template,answer,InputAnswer):
        if (template=="FractionMCQTypeProblems.html"):
            answer=str(answer)
            InputAnswer = "["+str(InputAnswer).partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[0]+", "+str(InputAnswer).partition("/")[2].partition("/")[2]+"]"
            if(answer==InputAnswer):
                return True
            else:
                return False
        else:
            try:
                AnswerNumerator = int(str(answer).partition("/")[0])
                AnswerDenominator = int(str(answer).partition("/")[2])
                
                if " " in str(InputAnswer):             
                    InputMixed = int(str(InputAnswer).partition(" ")[0])
                    RemainingInput = str(InputAnswer).partition(" ")[2]
                    InputDenominator = int(str(RemainingInput).partition("/")[2])
                    InputNumerator = int(str(RemainingInput).partition("/")[0])+InputMixed*InputDenominator
                elif "/" in str(InputAnswer):
                    InputMixed = 0
                    InputNumerator = int(str(InputAnswer).partition("/")[0])
                    InputDenominator = int(str(InputAnswer).partition("/")[2])
                else:
                    InputNumerator = int(str(InputAnswer))
                    InputDenominator = 1

                return Decimal(AnswerNumerator)/Decimal(AnswerDenominator)==Decimal(InputNumerator)/Decimal(InputDenominator)
            except ValueError:
                return False