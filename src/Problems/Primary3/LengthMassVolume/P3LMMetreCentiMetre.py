'''
Created on Apr 25, 2013
Module: P3LMMetreCentiMetre
Generates the Metre and Centi-metre problems on Length Mass Volume for Primary 3

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
from random import randint
import string

class P3LMMetreCentiMetre:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemTypeMCQ1",],
                            2:["ProblemType2","ProblemTypeMCQ2",],
                            3:["ProblemType3","ProblemTypeMCQ3",],
                            4:["ProblemType4","ProblemTypeMCQ4",],
                            5:["ProblemType5",],6:["ProblemType6",],7:["ProblemType7",],
                            8:["ProblemType8",],9:["ProblemType9",],10:["ProblemType10",],
                            11:["ProblemType11",],12:["ProblemType12",],13:["ProblemType13",],
                            14:["ProblemType14",],15:["ProblemType15",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                                    2:[self.GenerateProblemType2(),self.GenerateProblemTypeMCQ2(),],
                                    3:[self.GenerateProblemType3(),self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemType4(),self.GenerateProblemTypeMCQ4(),],
                                    5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],
                                    9:[self.GenerateProblemType9(),],10:[self.GenerateProblemType10(),],
                                    11:[self.GenerateProblemType11(),],12:[self.GenerateProblemType12(),],
                                    13:[self.GenerateProblemType13(),],14:[self.GenerateProblemType14(),],
                                    15:[self.GenerateProblemType15(),],
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
        #return self.GenerateProblemType15()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),"ProblemType2":self.GenerateProblemType2(),"ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),"ProblemType5":self.GenerateProblemType5(),"ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),"ProblemType8":self.GenerateProblemType8(),"ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10":self.GenerateProblemType10(),
                            "ProblemType11":self.GenerateProblemType11(),"ProblemType12":self.GenerateProblemType12(),"ProblemType13":self.GenerateProblemType13(),
                            "ProblemType14":self.GenerateProblemType14(),"ProblemType15":self.GenerateProblemType15(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),"ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),"ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        Write in centimetres.
         5 m 24 cm = _________ cm'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(10,99)

        self.problem = "Write in centimetres.<br><br>%d m %d cm = _____ cm"%(self.number1,self.number2)
        
        self.answer = self.number1*100+self.number2
                   
        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d cm</font></div></td>"%(number1,number1*100)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m %d cm</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number1*100,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        Write in centimetres.
         5 m 2 cm = _________ cm'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)

        self.problem = "Write in centimetres.<br><br>%d m %d cm = _____ cm"%(self.number1,self.number2)
        
        self.answer = self.number1*100+self.number2
                   
        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d cm</font></div></td>"%(number1,number1*100)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m %d cm</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number1*100,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        Write in metres and centimetres.
         345 cm = _____ m _____ cm
        (Write your answer as in the example below.
        Example: 5 m 23 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.number3 = randint(1,9)

        self.number = int(str(self.number1)+str(self.number2)+str(self.number3))
        self.problem = "Write in metres and centimetres.<br><br>"
        self.problem = self.problem + "%d cm = ___ m  ___ cm<br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 23 cm)"
        
        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,number,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,100)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d cm = %d m</font></div></td>"%(div*100,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d cm</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number,div*100,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        Write in metres and centimetres.
         305 cm = _____ m _____ cm
        (Write your answer as in the example below.
        Example: 5 m 23 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.number = int(str(self.number1)+'0'+str(self.number2))

        self.problem = "Write in metres and centimetres.<br><br>"
        self.problem = self.problem + "%d cm = ___ m  ___ cm<br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 23 cm)"
        
        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,number,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,100)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d cm = %d m</font></div></td>"%(div*100,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d cm</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number,div*100,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        [Person.Girlname] <has a> <rope> of length 2 m and 25 cm.
        What is the length of the <rope> in centimetres?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['has a','rope'],['has a','beaded string'],['has a','ribbon'],['has a','lace'],['has a','tape'],['draws a','line'],['has a','piece of cloth'],['has a','wire'],['folds a','piece of fabric'],['has a','yarn thread']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(1,9)
        self.number2 = randint(10,99)

        self.problem = "%s %s %s of length %d m and %d cm.<br><br>"%(self.name,self.item[0],self.item[1],self.number1,self.number2)
        self.problem = self.problem + "What is the length of the %s in centimetres?"%(self.item[1])
        
        self.answer = self.number1*100+self.number2
                   
        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,number1,number2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d cm</font></div></td>"%(number1,number1*100)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m %d cm</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number1*100,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The length of the %s is %d cm.</font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        [Person.Boyname] <has a> <rope> that is 225 cm long.
        Express the length of the <rope> in metres and centimetres?
        (Write your answer as in the example below.
        Example: 5 m 23 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['has a','plastic rope'],['has a','string'],['has a','hose'],['has a','cord'],['has an','adhesive tape'],['draws a','line'],['has a','piece of fabric'],['has a','copper wire'],['folds a','piece of crepe paper'],['has a','black thread']]
        
        self.item = random.choice(self.items)
        
        self.number = randint(100,999)

        self.problem = "%s %s %s that is %d cm long.<br><br>"%(self.name,self.item[0],self.item[1],self.number)
        self.problem = self.problem + "Express the length of the %s in metres and centimetres?<br><br>"%(self.item[1])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 23 cm)"

        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,number,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,100)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d cm = %d m</font></div></td>"%(div*100,div)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d cm</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number,div*100,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The length of the %s is %s.</font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        A <wall> is 3 m and 50 cm <high>.
        Find the <height> of the <wall> in centimetres.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['wall','high','height',randint(100,999)],['book shelf','tall','height',randint(100,250)],['window','tall','height',randint(100,350)],['tree','tall','height',randint(250,999)],['boy','tall','height',randint(100,183)],['room','long','length',randint(400,999)],['carpet','long','length',randint(100,999)],['truck','long','length',randint(500,999)],['cinema screen','wide','width',randint(600,999)],['pool','wide','width',randint(300,999)]]
        
        self.item = random.choice(self.items)
        
        self.number1,self.number2 = divmod(self.item[3],100)

        self.problem = "A %s is %d m and %d cm %s.<br><br>"%(self.item[0],self.number1,self.number2,self.item[1])
        self.problem = self.problem + "Find the %s of the %s in centimetres."%(self.item[2],self.item[0])
        
        self.answer = self.item[3]
                   
        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.item[2],self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,number1,number2,item2,item0,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d cm</font></div></td>"%(number1,number1*100)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m %d cm</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number1*100,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The %s of the %s is %d cm.</font>"%(item2,item0,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        A <pillar> is 350 cm <high>.
        What is the height of the <pillar> in metres and centimetres?
        (Write your answer as in the example below.
        Example: 5 m 23 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['pillar','high','height',randint(100,999)],['cabinet','tall','height',randint(100,250)],['door','tall','height',randint(100,350)],['ceiling','high','height',randint(250,999)],['man','tall','height',randint(150,190)],['hall','long','length',randint(400,999)],['mat','long','length',randint(100,999)],['tram','long','length',randint(500,999)],['curtain','wide','width',randint(600,999)],['stream','wide','width',randint(300,999)]]
        
        self.item = random.choice(self.items)
        
        self.number = self.item[3]

        self.problem = "A %s is %d cm %s.<br><br>"%(self.item[0],self.number,self.item[1])
        self.problem = self.problem + "What is the %s of the %s in metres and centimetres?<br><br>"%(self.item[2],self.item[0])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 23 cm)"

        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number,self.item[2],self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,number,item2,item0,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,100)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d cm = %d m</font></div></td>"%(div*100,div)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d cm</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number,div*100,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The %s of the %s is %s.</font>"%(item2,item0,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        <A boy climbed a> 2 m 30 cm <wall>.
        <How high did he climb in centimetres?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['A boy climbed a','wall.','How high did he climb in centimetres?',randint(100,400),'He climbed',''],
                      ['A baby crawled','to a toy.','How far did she crawl in centimetres?',randint(100,500),'She crawled',''],
                      ['An athlete jumped','from the starting line.','How far did she jump in centimetres?',randint(500,700),'She jumped',' far'],
                      ['A child threw a discus','from the starting point.','How far away did the discus fall in centimetres?',randint(400,590),'The discus fell',' away'],
                      ['A kid threw a javelin','away.','How far did the javelin travel in centimetres?',randint(200,470),'The javelin traveled',''],
                      ['A girl threw a ball','from the starting point.','How far away did the ball fall in centimetres?',randint(100,999),'The ball fell',' away'],
                      ['In a certain race, the runner-up was','behind the winner.','What was this distance in centimetres?',randint(100,999),'The distance was',''],
                      ['An athlete jumped a height of','in a high jump event.','How high did he jump in centimetres?',randint(150,230),'He jumped',' high'],
                      ['In a certain swimming competition, the winner was ahead of the runner-up by','.','What was this distance in centimetres?',randint(100,999),'The distance was',''],
                      ['A boy flung a pebble into the water which landed','away.','What was this distance in centimetres?',randint(100,999),'The distance was','']]
        
        self.item = random.choice(self.items)
        
        self.number1,self.number2 = divmod(self.item[3],100)

        self.problem = "%s %d m %d cm %s<br><br>"%(self.item[0],self.number1,self.number2,self.item[1])
        self.problem = self.problem + "%s"%(self.item[2])
        
        self.answer = self.item[3]
                   
        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.item[4],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,number1,number2,item4,item5,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d cm</font></div></td>"%(number1,number1*100)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m %d cm</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number1*100,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>%s %d cm%s.</font>"%(item4,answer,item5)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:
        <A boy climbed a> 230 cm <wall>.
        <How many metres and centimetres did he climb?>
        (Write your answer as in the example below.
        Example: 5 m 23 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['A boy climbed a','wall.','How many metres and centimetres did he climb?',randint(100,400),'He climbed',''],
                      ['A baby crawled','to a toy.','How many metres and centimetres did she crawl?',randint(100,500),'She crawled',''],
                      ['An athlete jumped','from the starting line.','How many metres and centimetres did she jump?',randint(500,700),'She jumped',''],
                      ['A child threw a discus','from the starting point.','How far away did the discus fall in metres and centimetres?',randint(400,590),'The discus fell',' away'],
                      ['A kid threw a javelin','away.','How far did the javelin travel in metres and centimetres?',randint(200,470),'The javelin traveled',' far'],
                      ['A girl threw a ball','from the starting point.','How far away did the ball fall in metres and centimetres?',randint(100,999),'The ball fell',' away'],
                      ['In a certain race, the runner-up was','behind the winner.','What was this distance in metres and centimetres?',randint(100,999),'The distance was',''],
                      ['An athlete jumped a height of','in a high jump event.','How high did he jump in metres and centimetres?',randint(150,230),'He jumped',' high'],
                      ['In a certain swimming competition, the winner was ahead of the runner-up by','.','What was this distance in metres and centimetres?',randint(100,999),'The distance was',''],
                      ['A boy flung a pebble into the water and it landed','away.','What was this distance in metres and centimetres?',randint(100,999),'The distance was','']]
        
        self.item = random.choice(self.items)
        
        self.number = self.item[3]

        self.problem = "%s %d cm %s<br><br>"%(self.item[0],self.number,self.item[1])
        self.problem = self.problem + "%s<br><br>"%(self.item[2])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 23 cm)"

        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.number,self.item[4],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,number,item4,item5,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,100)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d cm = %d m</font></div></td>"%(div*100,div)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d cm</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number,div*100,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>%s %s %s.</font>"%(item4,answer,item5)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:
        [Person.Girlname] <plants two trees> 2 m 34 cm apart.
        What is the distance between <the trees> in centimetres?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['plants two trees','the trees'],['puts two stones','the stones'],['puts two flags','the flags'],['digs two holes','the holes'],['and her friend are standing','them'],['places two books','the books'],['installs two poles in the ground','the poles'],['paints two walls that are','the walls'],['paints two chairs that are','the chairs'],['places two shelves','the shelves']]
        
        self.item = random.choice(self.items)
        
        self.number = randint(100,999)
        self.number1,self.number2 = divmod(self.number,100)

        self.problem = "%s %s %d m %d cm apart.<br><br>"%(self.name,self.item[0],self.number1,self.number2)
        self.problem = self.problem + "What is the distance between %s in centimetres?"%(self.item[1])
        
        self.answer = self.number
                   
        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.number1,self.number2,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,number1,number2,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d cm</font></div></td>"%(number1,number1*100)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m %d cm</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number1*100,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The distance between %s is %d cm.</font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType12(self):       
        '''e.g.:
        The distance between two <tables in a hall> is 3 m 87 cm.
        Express this distance in centimetres.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = ['tables in a hall','lampposts in a street','horses on a farm','players on a field','trees on a roadside','wooden platforms by a lake','printers in an office','towels hanging on a clothesline','babies sitting on a floor','benches in a park']
        
        self.item = random.choice(self.items)
        
        self.number = randint(100,999)
        self.number1,self.number2 = divmod(self.number,100)

        self.problem = "The distance between two %s is %d m %d cm.<br><br>"%(self.item,self.number1,self.number2)
        self.problem = self.problem + "Express this distance in centimetres."
        
        self.answer = self.number
                   
        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType12(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d cm</font></div></td>"%(number1,number1*100)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 m = 100 cm</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m %d cm</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number1*100,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d cm</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType13(self):       
        '''e.g.:
        [Person.Girlname] <plants two trees> 234 cm apart.
        What is the distance between <the trees> in metres and centimetres?
        (Write your answer as in the example below.
        Example: 5 m 23 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['plants two trees','the trees'],['puts two stones','the stones'],['puts two flags','the flags'],['digs two holes','the holes'],['and her friend are standing','them'],['places two books','the books'],['installs two poles in the ground','the poles'],['paints two walls that are','the walls'],['paints two chairs that are','the chairs'],['places two shelves','the shelves']]
        
        self.item = random.choice(self.items)
        
        self.number = randint(100,999)

        self.problem = "%s %s %d cm apart.<br><br>"%(self.name,self.item[0],self.number)
        self.problem = self.problem + "What is the distance between %s in metres and centimetres?<br><br>"%(self.item[1])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 23 cm)"

        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.number,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType13(self,problem,answer,number,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,100)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d cm = %d m</font></div></td>"%(div*100,div)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d cm</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number,div*100,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The distance between %s is %s.</font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType14(self):       
        '''e.g.:
        The distance between two <tables in a hall> is 387 cm.
        Express this distance in metres and centimetres.
        (Write your answer as in the example below.
        Example: 5 m 23 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = ['tables in a hall','lampposts in a street','horses on a farm','players on a field','trees on a roadside','wooden platforms by a lake','printers in an office','towels hanging on a clothesline','babies sitting on a floor','benches in a park']
        
        self.item = random.choice(self.items)
        
        self.number = randint(100,999)

        self.problem = "The distance between two %s is %d cm.<br><br>"%(self.item,self.number)
        self.problem = self.problem + "Express this distance in metres and centimetres."

        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType14(self,problem,answer,number,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,100)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d cm = %d m</font></div></td>"%(div*100,div)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100 cm = 1 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d cm</td><td>=</td><td>%d cm &nbsp;+&nbsp; %d cm</td></tr>"%(number,div*100,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d cm</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType15(self):       
        '''e.g.:
        Fill in the blank with 'm' or 'cm'.
         <A table is> 60 ____ <high>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['A table is','high','cm',random.choice([60,70,80,90,100,110,120,130]),'A table of height','cm is normal.<br>A table of height','m would be very high!'],
                      ['A water bottle is','tall','cm',random.choice([10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]),'A regular-sized water bottle is about','cm tall.<br>A water bottle of height','m would be very tall!'],
                      ['A dictionary is','thick','cm',random.choice([2,3,4,5,6,7]),'The thickness of any book is measured in centimetres.<br>A dictionary of','cm thickness is normal.<br>A dictionary of','m thickness would be very thick!'],
                      ['A cricket bat is about','long','cm',random.choice([64,70,73,76,78,81,83,85,88,97]),'The length of a cricket bat is measured in centimetres.<br>A cricket bat of','cm length is normal.<br>A cricket bat of','m length would be very long!'],
                      ['A hand is','long','cm',random.choice([5,6,7,8,9,10,11,12,13,14,15,16,17,18]),"Hands come in different sizes.<br>However, they are all still measured in centimetres.<br>It's normal to have a hand of length",'cm.<br>A hand that is','m would be very long!'],
                      ['A shirt is','wide','cm',random.choice([25,30,35,40,45,50,55,60,65,70,75,80,85]),'The length, height and width of any shirt is measured in centimetres.<br>It is normal for a shirt to be','cm wide.<br>A shirt that is','m wide would be very wide!'],
                      ['A building is','high','m',random.choice([10,20,30,40,50,60,70,80,90,100]),"It's normal for a building to have a height of",'m.<br>A building of height','cm would be very tiny!'],
                      ['A soccer field is about','long','m',random.choice([90,92,94,96,98,100,102,104,106,108,110]),'The length of a soccer field is usually measured in metres.<br>A regular soccer field is about','m long.<br>A soccer field of length','cm would be too small to play a real game on!'],
                      ['A real train is about','long','m',random.choice([400,430,450,470,500,520,550,570,600]),"It's common to measure the length of a train in metres.<br>A train of length",'m is normal.<br>A train of length','cm would not be a real train!'],
                      ['A bus is about','long','m',random.choice([9,10,11,12,13,14,15,16,17,18,19]),"It's common to measure the length of a bus in metres.<br>A bus of length",'m is normal.<br>A bus of length','cm would probably be a toy bus!'],
                      ['A swimming pool is','wide','m',random.choice([5,6,7,8,9,10,11,12,13,14]),'The length, depth and width of a swimming pool is measured in metres.<br>It is common for a swimming pool to have a width of',"m.<br>A swimming pool that's",'cm wide would be too tiny to swim in!']]
        
        self.item = random.choice(self.items)

        self.problem = "Fill in the blank with 'm' or 'cm'.<br><br>"
        self.problem = self.problem + "%s %d ____ %s."%(self.item[0],self.item[3],self.item[1])
        
        self.answer = self.item[2]
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.item[3],self.item[4],self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType15",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType15(self,problem,answer,item3,item4,item5,item6,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        self.solution_text =  "<font class='ExplanationFont'>%s %d %s %d %s</font>"%(item4,item3,item5,item3,item6)
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,complexity_level,HCScore,CheckAnswerType):
        
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
                'grade':3,"complexity_level":complexity_level,"HCScore":HCScore,"CheckAnswerType":CheckAnswerType}
        
    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        Write in centimetres.
         5 m 24 cm = _________ cm'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1"
        self.CheckAnswerType = 1

        self.number1 = randint(1,9)
        self.number2 = randint(10,99)

        self.problem = "Write in centimetres.<br><br>%d m %d cm = _____ cm"%(self.number1,self.number2)
        
        self.answer = self.number1*100+self.number2
                   
        self.unit = "cm"
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number1*1000+self.number2,self.number1*1000+self.number2*10,
                             str(self.number1)+"."+str(self.number2),float(self.answer)/10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ2(self):
        '''e.g.:
        Write in centimetres.
         5 m 2 cm = _________ cm'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ2"
        self.CheckAnswerType = 1

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)

        self.problem = "Write in centimetres.<br><br>%d m %d cm = _____ cm"%(self.number1,self.number2)
        
        self.answer = self.number1*100+self.number2
                   
        self.unit = "cm"
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number1*1000+self.number2,self.number1*1000+self.number2*10,
                             str(self.number1)+"."+str(self.number2),float(self.answer)/10]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ3(self):
        '''e.g.:
        Write in metres and centimetres.
         345 cm = _____ m _____ cm
        (Write your answer as in the example below.
        Example: 5 m 23 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ3"
        self.CheckAnswerType = 2

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.number3 = randint(1,9)

        self.number = int(str(self.number1)+str(self.number2)+str(self.number3))
        self.problem = "Write in metres and centimetres.<br><br>"
        self.problem = self.problem + "%d cm = ___ m  ___ cm<br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 23 cm)"
        
        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = ["%d m %d cm"%(divmod(self.number,10)),
                             "%d m %d cm"%(divmod(self.number,1000)),
                             "%d m %d cm"%(divmod(self.number,1)),
                             str(self.number1)+str(self.number2)+" m "+str(self.number3)+" cm"]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
        
    def GenerateProblemTypeMCQ4(self):
        '''e.g.:
        Write in metres and centimetres.
         305 cm = _____ m _____ cm
        (Write your answer as in the example below.
        Example: 5 m 23 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ4"
        self.CheckAnswerType = 2

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.number = int(str(self.number1)+'0'+str(self.number2))

        self.problem = "Write in metres and centimetres.<br><br>"
        self.problem = self.problem + "%d cm = ___ m  ___ cm<br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 23 cm)"
        
        div,mod = divmod(self.number,100)
        
        self.answer = "%d m %d cm"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [
                             "%d m %d cm"%(divmod(self.number,1000)),
                             "%d m %d cm"%(divmod(self.number,1)),
                             str(self.number1)+"0 m "+str(self.number2)+" cm"]
           
                           
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type,
                                self.complexity_level,self.HCScore,self.CheckAnswerType)
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswer == 2:
            try:
                answer1 = string.join(str(answer).split(),"")
                '''If user enter answer as 1m 04 cm that should also be correct'''
                if len(answer1.partition("m")[2])==3:
                    answer2 = answer1.partition("m")[0]+"m0"+answer1.partition("m")[2]
                else:
                    answer2 = answer1
                InputAnswer = string.join(str(InputAnswer).split(),"")
                return answer1.capitalize() == InputAnswer.capitalize() or answer2.capitalize() == InputAnswer.capitalize()
            except ValueError:
                return False
        elif CheckAnswer == 3:
            try:
                return str(answer).capitalize() == str(InputAnswer).capitalize()
            except ValueError:
                return False                       