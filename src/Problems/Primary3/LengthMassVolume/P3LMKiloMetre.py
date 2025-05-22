'''
Created on Apr 26, 2013
Module: P3LMKiloMetre
Generates the Metre and Kilometre problems on Length Mass Volume for Primary 3

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

class P3LMKiloMetre:
    
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
                            14:["ProblemType14",],15:["ProblemType15",],16:["ProblemType16",],17:["ProblemType17",],
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
                                    15:[self.GenerateProblemType15(),],16:[self.GenerateProblemType16(),],
                                    17:[self.GenerateProblemType17(),],
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
                            "ProblemType14":self.GenerateProblemType14(),"ProblemType15":self.GenerateProblemType15(),"ProblemType16":self.GenerateProblemType16(),
                            "ProblemType17":self.GenerateProblemType17(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),"ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),"ProblemTypeMCQ4":self.GenerateProblemTypeMCQ4(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        Write in metres.
         5 km 24 m = _________ m'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(100,999)

        self.problem = "Write in metres.<br><br>%d km %d m = _____ m"%(self.number1,self.number2)
        
        self.answer = self.number1*1000+self.number2
                   
        self.unit = "m"
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
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d km = %d m</font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d km %d m</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        Write in metres.
         5 km 24 m = _________ m'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(1,99)

        self.problem = "Write in metres.<br><br>%d km %d m = _____ m"%(self.number1,self.number2)
        
        self.answer = self.number1*1000+self.number2
                   
        self.unit = "m"
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
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d km = %d m</font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d km %d m</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        Write in kilometres and metres.
         3456 m = _____ km _____ m
        (Write your answer as in the example below.
        Example: 5 km 238 m)'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.number3 = randint(1,9)
        self.number4 = randint(1,9)

        self.number = int(str(self.number1)+str(self.number2)+str(self.number3)+str(self.number4))
        self.problem = "Write in kilometres and metres.<br><br>"
        self.problem = self.problem + "%d m = ___ km  ___ m<br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 km 293 m)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d km %d m"%(div,mod)
        
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

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d km</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        Write in kilometres and metres.
         3456 m = _____ km _____ m
        (Write your answer as in the example below.
        Example: 5 km 238 m)'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.number1 = randint(1,9)
        self.number2 = randint(0,9)
        self.number3 = randint(1,9)
        self.number = int(str(self.number1)+'0'+str(self.number2)+str(self.number3))

        self.problem = "Write in kilometres and metres.<br><br>"
        self.problem = self.problem + "%d m = ___ km  ___ m<br><br>"%(self.number)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 km 293 m)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d km %d m"%(div,mod)
        
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

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d km</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        [Person.Boyname] <takes a van to school.>
        <His school is> 3 km and 258 m <away from his home.>
        Express this distance in metres.
        '''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['takes a van to school.','His school is','away from his home.',randint(3000,9999)],['walks to school.','He lives','away from his school.',randint(1000,2000)],['and his sister cycle to school.','Their school is','away from their house.',randint(1000,3000)],['drove to the amusement park with his father.','The amusement park is','from their house.',randint(5000,9999)],['took a bus to visit his grandmother.','His grandmother lives','away from his house.',randint(4000,9999)],['and his brother went to a beach for swimming.','They swam','to an island.',randint(1000,2000)],["walked his dog to his friend's house.","They walked",".",randint(1000,3000)],['loves the library.','The distance between his house and the library is','.',randint(1000,5000)],['is going to the mall with his mother.','The mall is','away.',randint(1000,9999)],['and his class are going for a visit to the farm.','The farm is','from their school.',randint(5000,9999)]]

        self.item = random.choice(self.items)
        
        self.number = self.item[3]
        
        self.number1,self.number2 = divmod(self.number,1000)
        
        self.problem = "%s %s<br><br>"%(self.name,self.item[0])
        self.problem = self.problem + "%s %d km and %d m %s<br><br>"%(self.item[1],self.number1,self.number2,self.item[2])
        self.problem = self.problem + "Express this distance in metres."
        
        self.answer = self.number
                   
        self.unit = "m"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d km = %d m</font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d km %d m</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        <Every day >[Person.Girlname]< and her brother go to school by van.>
        <Their school is> 3258 m< from their house.>
        What is this <distance> in kilometres and metres?
        (Write your answer as in the example below.
        Example: 5 km 238 m)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['Every day ',' and her brother go to school by van.','Their school is',' from their house.','distance',randint(3000,9999)],['Every morning ',' walks to school with her sister.','They live',' away from their school.','distance',randint(1000,2000)],['Every Sunday ',' and her family cycle from their home to the park.','The park is',' from their home.','distance',randint(4000,9999)],["Every morning ","'s father drives to work.","His workplace is"," away from their house.","distance",randint(5000,9999)],['Last Saturday ',' went to visit her uncle.','Her uncle lives',' away from her house.','distance',randint(4000,9999)],['',' is going on a vacation with her family on a plane.','Their plane is flying at a height of',' from ground.','height',randint(1000,9999)],["This morning "," went to her friend's house to do her homework.","Her friend lives"," away.","distance",randint(1000,3000)],['On Sunday, ',' and her brothers went to the bird park with their parents.','The distance between their house and the bird park is',' .','distance',randint(3000,9999)],['',' is going to the mall with her mother.','The mall is',' away.','distance',randint(1000,9999)],['',' and his class are going on a picnic.','The picnic spot is',' from their school.','distance',randint(5000,9999)]]

        self.item = random.choice(self.items)        
        
        self.number = self.item[5]

        self.problem = "%s%s%s<br><br>"%(self.item[0],self.name,self.item[1])
        self.problem = self.problem + "%s %d m%s<br><br>"%(self.item[2],self.number,self.item[3])
        self.problem = self.problem + "What is this %s in kilometres and metres?<br><br>"%(self.item[4])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 km 293 m)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d km %d m"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,number,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d km</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        <A road> is 3 km and 590 m long.
        Find the <length of the road> in metres.
        '''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['A road','length of the road',randint(1000,5000),'road'],
                      ['A jogging track in a park','length of the jogging track',randint(3000,9999),'jogging track'],
                      ['A road connecting an aquarium to a zoo','length of the road',randint(3000,9999),'road'],
                      ['A seashore','length of the seashore',randint(5000,9999),'seashore'],
                      ['A certain cargo train','length of the cargo train',randint(1000,4000),'cargo train'],
                      ['A runway','length of the runway',randint(1800,3350),'runway'],
                      ['A nature park trail','length of the trail',randint(1000,5000),'trail'],
                      ['A cycling trail','length of the trail',randint(5000,9999),'trail'],
                      ['An ice skating trail','length of the trail',randint(1000,8500),'trail'],
                      ['A walking trail','length of the walking trail',randint(1000,5000),'trail']]

        self.item = random.choice(self.items)
        
        self.number = self.item[2]
        
        self.number1,self.number2 = divmod(self.number,1000)
        
        self.problem = "%s is %d km and %d m long.<br><br>"%(self.item[0],self.number1,self.number2)
        self.problem = self.problem + "Find the %s in metres."%(self.item[1])
        
        self.answer = self.number
                   
        self.unit = "m"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,number1,number2,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d km = %d m</font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d km %d m</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The %s is %d m long.</font>"%(item3,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        <A road> is 3590 m long.
        What is the <length of the road> in kilometres and metres?
        (Write your answer as in the example below.
        Example: 5 km 238 m)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['A road','length of the road',randint(1000,5000),'road'],
                      ['A jogging track in a park','length of the jogging track',randint(3000,9999),'jogging track'],
                      ['A road connecting an aquarium to a zoo','length of the road',randint(3000,9999),'road'],
                      ['A seashore','length of the seashore',randint(5000,9999),'seashore'],
                      ['A certain cargo train','length of the cargo train',randint(1000,4000),'cargo train'],
                      ['A runway','length of the runway',randint(1800,3350),'runway'],
                      ['A nature park trail','length of the trail',randint(1000,5000),'trail'],
                      ['A cycling trail','length of the trail',randint(5000,9999),'trail'],
                      ['An ice skating trail','length of the trail',randint(1000,8500),'trail'],
                      ['A walking trail','length of the walking trail',randint(1000,5000),'trail']]

        self.item = random.choice(self.items)        
        
        self.number = self.item[2]

        self.problem = "%s is %d m long.<br><br>"%(self.item[0],self.number)
        self.problem = self.problem + "What is the %s in kilometres and metres?<br><br>"%(self.item[1])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 km 293 m)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d km %d m"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number,self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,number,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d km</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The %s is %s long.</font>"%(item3,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        [Person.Boyname] participated in a 5 km 300 m <race>.
        <How far did he run in metres?>
        '''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['race','How far did he run in metres?',random.randrange(1000,9900,100),'He ran'],
                      ['three-legged race','What was this distance in metres?',random.randrange(1000,2000,100),'This distance was'],
                      ['one-legged race','How far did he run in metres?',random.randrange(1000,2000,100),'He ran'],
                      ['sack race','What was this distance in metres?',random.randrange(1000,2000,100),'This distance was'],
                      ['cycling competition','How far did he cycle in metres?',random.randrange(3000,9900,100),'He cycled'],
                      ['swimming competition','What was this distance in metres?',random.randrange(1000,3000,100),'This distance was'],
                      ['inline skating event','How far did he skate in metres?',random.randrange(5000,9900,100),'He skated'],
                      ['ice skating event','How far did he skate in metres?',random.randrange(1000,3000,100),'He skated'],
                      ['slow cycle race','How far did he slow cycle in metres?',random.randrange(1000,2000,100),'He slow cycled'],
                      ['skipping rope race','How far did he skip in metres?',random.randrange(1000,3000,100),'He skipped']]

        self.item = random.choice(self.items)
        
        self.number = self.item[2]
        
        self.number1,self.number2 = divmod(self.number,1000)
        
        self.problem = "%s participated in a %d km %d m %s.<br><br>"%(self.name,self.number1,self.number2,self.item[0])
        self.problem = self.problem + "%s"%(self.item[1])
        
        self.answer = self.number
                   
        self.unit = "m"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,number1,number2,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d km = %d m</font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d km %d m</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>%s %d m.</font>"%(item3,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:
        [Person.Girlname] participated in a 5300 m <race>.
        <How far did she run in kilometres and metres?>
        (Write your answer as in the example below.
        Example: 5 km 238 m)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['race','How far did she run in kilometres and metres?',random.randrange(1000,9900,100),'She ran'],
                      ['three-legged race','What was this distance in kilometres and metres?',random.randrange(1000,2000,100),'This distance was'],
                      ['one-legged race','How far did she run in kilometres and metres?',random.randrange(1000,2000,100),'She ran'],
                      ['sack race','What was this distance in kilometres and metres?',random.randrange(1000,2000,100),'This distance was'],
                      ['cycling competition','How far did she cycle in kilometres and metres?',random.randrange(3000,9900,100),'She cycled'],
                      ['swimming competition','What was this distance in kilometres and metres?',random.randrange(1000,3000,100),'This distance was'],
                      ['inline skating event','How far did she skate in kilometres and metres?',random.randrange(5000,9900,100),'She skated'],
                      ['ice skating event','How far did she skate in kilometres and metres?',random.randrange(1000,3000,100),'She skated'],
                      ['slow cycle race','How far did she slow cycle in kilometres and metres?',random.randrange(1000,2000,100),'She slow cycled'],
                      ['skipping rope race','How far did she skip in kilometres and metres?',random.randrange(1000,3000,100),'She skipped']]

        self.item = random.choice(self.items)        
        
        self.number = self.item[2]

        self.problem = "%s participated in a %d m %s.<br><br>"%(self.name,self.number,self.item[0])
        self.problem = self.problem + "%s<br><br>"%(self.item[1])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 km 293 m)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d km %d m"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.number,self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,number,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d km</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>%s %s.</font>"%(item3,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:
        [Person.Name1]'s <house> is 2 km 34 m from [Person.Name2]'s <house>.
        What is the distance between their <houses> in metres?
        '''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.PersonName,2)
        
        self.items = [['house','houses'],['school','schools'],['bus stop','bus stops'],['train station','train stations'],['workplace','workplaces'],['gym','gyms'],['playground','playgrounds'],['shop','shops'],['farmhouse','farmhouses'],['building','buildings']]

        self.item = random.choice(self.items)
        
        self.number = randint(1000,9999)
        
        self.number1,self.number2 = divmod(self.number,1000)
        
        self.problem = "%s's %s is %d km %d m from %s's %s.<br><br>"%(self.names[0],self.item[0],self.number1,self.number2,self.names[1],self.item[0])
        self.problem = self.problem + "What is the distance between their %s in metres?"%(self.item[1])
        
        self.answer = self.number
                   
        self.unit = "m"
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
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d km = %d m</font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d km %d m</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The distance between their %s is %d m.</font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType12(self):       
        '''e.g.:
        [Person.Name1]'s <house> is 2034 m from [Person.Name2]'s <house>.
        Find the distance between their <houses> in kilometres and metres?
        (Write your answer as in the example below.
        Example: 5 km 238 m)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.PersonName,2)
        
        self.items = [['house','houses'],['school','schools'],['bus stop','bus stops'],['train station','train stations'],['workplace','workplaces'],['gym','gyms'],['playground','playgrounds'],['shop','shops'],['farmhouse','farmhouses'],['building','buildings']]

        self.item = random.choice(self.items)        
        
        self.number = randint(1000,9999)

        self.problem = "%s's %s is %d m from %s's %s.<br><br>"%(self.names[0],self.item[0],self.number,self.names[1],self.item[0])
        self.problem = self.problem + "Find the distance between their %s in kilometres and metres?<br><br>"%(self.item[1])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 km 293 m)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d km %d m"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.number,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType12(self,problem,answer,number,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d km</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>The distance between their %s is %s.</font>"%(item1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType13(self):       
        '''e.g.:
        The distance between <the first lamp post and the last lamp post on a road is> 2 km 34 m.
        Express this distance in metres.
        '''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = ['the first lamp post and the last lamp post on a road is','two farms is','two office buildings is','two buses on a road is','two malls is','two vegetable markets is','two parks is','the front gate and the back gate of a public garden is','two restaurants is','two colleges is','two barns is','two construction sites is']

        self.item = random.choice(self.items)
        
        self.number = randint(1000,9999)
        
        self.number1,self.number2 = divmod(self.number,1000)
        
        self.problem = "The distance between %s %d km %d m.<br><br>"%(self.item,self.number1,self.number2)
        self.problem = self.problem + "Express this distance in metres."
        
        self.answer = self.number
                   
        self.unit = "m"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.number1,self.number2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType13(self,problem,answer,number1,number2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d km = %d m</font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d km %d m</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType14(self):       
        '''e.g.:
        The distance between <the first lamp post and the last lamp post on a road is> 2034 m.
        What is this distance in kilometres and metres.
        (Write your answer as in the example below.
        Example: 5 km 238 m)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.PersonName,2)
        
        self.items = ['the first lamp post and the last lamp post on a road is','two farms is','two office buildings is','two buses on a road is','two malls is','two vegetable markets is','two parks is','the front gate and the back gate of a public garden is','two restaurants is','two colleges is','two barns is','two construction sites is']

        self.item = random.choice(self.items)        
        
        self.number = randint(1000,9999)

        self.problem = "The distance between %s %d m.<br><br>"%(self.item,self.number)
        self.problem = self.problem + "What is the distance in kilometres and metres?<br><br>"
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 km 293 m)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d km %d m"%(div,mod)
        
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

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d km</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType15(self):       
        '''e.g.:
        Fill in the blank with 'km' or 'm'.
         <A highway is> 60 ____ <long.>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['A highway is','long.','km',random.choice([30,40,50,60,70,80,90,100,110,120,130]),'The length of a highway is commonly measured in kilometres.<br>It is normal for a highway to be','km long.<br>A highway that is only','m in length would be too short to be called a highway!'],
                      ['An aeroplane cruises at a height of','.','km',random.choice([7,8,9,10,11,12,13,14,15]),'Aeroplanes fly at high altitudes.<br>It is normal for an aeroplane to cruise at a height of','km.<br>It would be too low for an aeroplane to cruise at a height of','m!'],
                      ['Some of the longest rivers in the world are about','long.','km',random.choice([3000,3500,4000,4500,5000,5500,6000,6500]),'Rivers usually run very long.<br>The longest rivers in the world run as long as or even longer than','km.<br>A river that is only','m in length is not considered long!'],
                      ['Some of the longest bridges in the world are about','long.','km',random.choice([25,26,27,28,29,30,35,40,50,80,110,165]),'The longest bridges in the world are as long as or even longer than','km.<br>A bridge that is only','m in length is not considered long!'],
                      ['High speed trains can travel faster than','in an hour.','km',random.choice([200,210,220,230,240,250,260,270,280,290,300]),'High speed trains travel super fast.<br>It is normal for a high speed train to cover','km or even more in an hour.<br>Only toy trains travel at','m in an hour!'],
                      ['A building is','high.','m',random.choice([10,20,30,40,50,60,70,80,90,100]),'The height of a building is usually measured in metres.<br>It is normal for a building to be','m tall.<br>A building that is','km in height is too tall to exist!'],
                      ['A soccer field is about','long.','m',random.choice([90,92,94,96,98,100,102,104,106,108,110]),'The length of a soccer field is usually measured in metres.<br>A regular soccer field has a length of','m.<br>A field that is','km in length is certainly not for playing soccer!'],
                      ['A train is about','long.','m',random.choice([400,430,450,470,500,520,550,570,600]),"It's common to measure the length of a train in metres.<br>A train of length",'m is normal.<br>A train of length','km would be too long to exist!'],
                      ['A bus is about','long.','m',random.choice([9,10,11,12,13,14,15,16,17,18,19]),"It's common to measure the length of a bus in metres.<br>A bus of length",'m is normal.<br>A bus of length','km would be too long to exist!'],
                      ['A swimming pool is','wide.','m',random.choice([8,10,12,14,16,18,20,22,24,25]),'The length, depth and width of a swimming pool is measured in metres.<br>It is common for a swimming pool to have a width of',"m.<br>A swimming pool that's",'km wide is considered a lake and not a swimming pool!']]

        self.item = random.choice(self.items)
        
        self.number = self.item[3]

        self.problem = "Fill in the blank with 'km' or 'm'.<br><br>"
        self.problem = self.problem + "%s %d ____ %s"%(self.item[0],self.number,self.item[1])
        
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

    def GenerateProblemType16(self):       
        '''e.g.:
        The height of Mount Everest is 8848 m.
        Express this height in kilometres and metres.
        (Write your answer as in the example below.
        Example: 5 km 678 m)'''

        self.complexity_level = "easy"
        self.HCScore = 3
                
        self.items = [['The height of Mount Everest, the highest mountain on Earth, is 8848 m.','height','8848','The height of Mount Everest is'],
                      ['The height of K2, the second-highest mountain on Earth is 8611 m.','height','8611','The height of K2 is'],
                      ['Mount McKinley, the highest mountain in the United States, has its peak at 6194 m.','height','6194','The height of Mount McKinley is'],
                      ['Mount Kilimanjaro, the highest mountain in Africa, has its peak at 5895 m.','height','5895','The height of Mount Kilimanjaro is'],
                      ['The famous Golden Gate Bridge of USA is about 2737 m long.','length','2737','The length of Golden Gate Bridge is'],
                      ['The Pearl Bridge of Japan is 3911 m long.','length','3911','The length of Pearl Bridge is'],
                      ['The Humber Bridge of England is 2220 m long.','length','2220','The length of Humber Bridge is'],
                      ['Victoria Falls, the largest waterfall in the world, is 1708 m wide.','width','1708','The width of Victoria Falls is'],
                      ['The famous Niagara Falls of North America is 1203 m wide.','width','1203','The width of Niagara Falls is'],
                      ['Iguazu Falls located in South America is 2700 m wide.','width','2700','The width of Iguazu Falls is'],
                      ['Bald eagles can fly up to a height of 3048 m.','height','3048','Bald eagles can fly up to a height of']]

        self.item = random.choice(self.items)        
        
        self.number = int(self.item[2])

        self.problem = "%s<br><br>"%(self.item[0])
        self.problem = self.problem + "Express this %s in kilometres and metres.<br><br>"%(self.item[1])
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 km 293 m)"
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d km %d m"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType16(self.problem,self.answer,self.number,self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType16",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType16(self,problem,answer,number,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number,1000)
        if div > 1:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d m = %d km</font></div></td>"%(div*1000,div)
        else:
            self.solution_text = "<br><div class='side' style='width:150px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 m = 1 km</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number,div*1000,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(div,mod)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>%s %s.</font>"%(item3,answer)
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType17(self):       
        '''e.g.:
        <The height of Mount Everest is 8 km 848 m.>
        Express this <height> in metres.
        '''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['The height of Mount Everest, the highest mountain on Earth, is 8 km 848 m.','height','8848','The height of Mount Everest is'],
                      ['The height of K2, the second-highest mountain on Earth is 8 km 611 m.','height','8611','The height of K2 is'],
                      ['Mount McKinley, the highest mountain in the United States, has its peak at 6 km 194 m.','height','6194','The height of Mount McKinley is'],
                      ['Mount Kilimanjaro, the highest mountain in Africa, has its peak at 5 km 895 m.','height','5895','The height of Mount Kilimanjaro is'],
                      ['The famous Golden Gate Bridge of USA is about 2 km 737 m long.','length','2737','The length of Golden Gate Bridge is'],
                      ['The Pearl Bridge of Japan is 3 km 911 m long.','length','3911','The length of Pearl Bridge is'],
                      ['The Humber Bridge of England is 2 km 220 m long.','length','2220','The length of Humber Bridge is'],
                      ['Victoria Falls, the largest waterfall in the world, is 1 km 708 m wide.','width','1708','The width of Victoria Falls is'],
                      ['The famous Niagara Falls of North America is 1 km 203 m wide.','width','1203','The width of Niagara Falls is'],
                      ['Iguazu Falls located in South America is 2 km 700 m wide.','width','2700','The width of Iguazu Falls is'],
                      ['Bald eagles can fly up to a height of 3 km 48 m.','height','3048','Bald eagles can fly up to a height of']]

        self.item = random.choice(self.items)
        
        self.number = int(self.item[2])
        
        self.number1,self.number2 = divmod(self.number,1000)
        
        self.problem = "%s<br><br>"%(self.item[0])
        self.problem = self.problem + "Express this %s in metres."%(self.item[1])
        
        self.answer = self.number
                   
        self.unit = "m"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType17(self.problem,self.answer,self.number1,self.number2,self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType17",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType17(self,problem,answer,number1,number2,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        if number1 > 1:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m<br>So,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%d km = %d m</font></div></td>"%(number1,number1*1000)
        else:
            self.solution_text = "<br><div class='side' style='width:130px'><font class='ExplanationFont'>We know,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 km = 1000 m</font></div></td>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d km %d m</td><td>=</td><td>%d km &nbsp;+&nbsp; %d m</td></tr>"%(number1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m &nbsp;+&nbsp; %d m</td></tr>"%(number1*1000,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>=</td><td>%d m</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>&nbsp;&nbsp;&nbsp;<font class='ExplanationFont'>%s %d m.</font>"%(item3,answer)

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
        Write in metres.
         5 km 24 m = _________ m'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ1"
        self.CheckAnswerType = 1

        self.number1 = randint(1,9)
        self.number2 = randint(100,999)

        self.problem = "Write in metres.<br><br>%d km %d m = _____ m"%(self.number1,self.number2)
        
        self.answer = self.number1*1000+self.number2
                   
        self.unit = "m"
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number1*100+self.number2,
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
        Write in metres.
         5 km 24 m = _________ m'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ2"
        self.CheckAnswerType = 1

        self.number1 = randint(1,9)
        self.number2 = randint(1,99)

        self.problem = "Write in metres.<br><br>%d km %d m = _____ m"%(self.number1,self.number2)
        
        self.answer = self.number1*1000+self.number2
                   
        self.unit = "m"
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = [self.number1*100+self.number2,
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
        Write in kilometres and metres.
         3456 m = _____ km _____ m
        (Write your answer as in the example below.
        Example: 5 km 238 m)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ3"
        self.CheckAnswerType = 2

        self.number1 = randint(1,9)
        self.number2 = randint(1,9)
        self.number3 = randint(1,9)
        self.number4 = randint(1,9)

        self.number = int(str(self.number1)+str(self.number2)+str(self.number3)+str(self.number4))
        self.problem = "Write in kilometres and metres.<br><br>"
        self.problem = self.problem + "%d m = ___ km  ___ m<br><br>"%(self.number)
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d km %d m"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = ["%d km %d m"%(divmod(self.number,10)),
                             "%d km %d m"%(divmod(self.number,100)),
                             "%d km %d m"%(divmod(self.number,1)),
                             str(self.number1)+str(self.number2)+" km "+str(self.number3)+" m"]
           
                           
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
        Write in kilometres and metres.
         3456 m = _____ km _____ m
        (Write your answer as in the example below.
        Example: 5 km 238 m)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        self.problem_type = "ProblemTypeMCQ4"
        self.CheckAnswerType = 2

        self.number1 = randint(1,9)
        self.number2 = randint(0,9)
        self.number3 = randint(1,9)
        self.number = int(str(self.number1)+'0'+str(self.number2)+str(self.number3))

        self.problem = "Write in kilometres and metres.<br><br>"
        self.problem = self.problem + "%d m = ___ km  ___ m<br><br>"%(self.number)
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d km %d m"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
                
        self.template = "MCQTypeProblems.html"
        
        self.wrongAnswers = ["%d km %d m"%(divmod(self.number,10)),
                             "%d km %d m"%(divmod(self.number,100)),
                             "%d km %d m"%(divmod(self.number,1)),
                             str(self.number1)+str(self.number2)+" km "+str(self.number3)+" m"]
           
                           
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
                '''If user enter answer as 1km 007 m that should also be correct'''
                if len(answer1.partition("km")[2])==3:
                    answer2 = answer1.partition("km")[0]+"km0"+answer1.partition("km")[2]
                elif len(answer1.partition("km")[2])==2:
                    answer2 = answer1.partition("km")[0]+"km00"+answer1.partition("km")[2]
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