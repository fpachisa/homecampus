'''
Created on Jul 08, 2013
Module: P3TISubtraction
Generates the Subtraction Time problems on Time for Primary 3

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

class P3TISubtraction:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemType4",],
                            5:["ProblemType5",],6:["ProblemType6",],7:["ProblemType7",],8:["ProblemType8",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],4:[self.GenerateProblemType4(),],
                                    5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],7:[self.GenerateProblemType7(),],
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
        '''e.g.:
        5 h 40 min &minus; 3 h 25 min = _____ h ____ min
        (Write your answer as in the example below.
        Example: 3 h 45 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.hour1 = randint(5,12)
        self.hour2 = randint(3,self.hour1-1)
        self.minutes1 = random.randrange(30,55,5)
        self.minutes2 = random.randrange(5,self.minutes1-5,5)
        
        self.problem = "%d h %d min - %d h %d min = _____ h ____ min<br><br>"%(self.hour1,self.minutes1,self.hour2,self.minutes2)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 h 45 min)"
        
        self.answer = "%d h %d min"%(self.hour1-self.hour2,self.minutes1-self.minutes2)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.hour1,self.hour2,self.minutes1,self.minutes2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,hour1,hour2,minutes1,minutes2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        First, subtract the minutes.
        40 min &minus; 25 min = 15 min
        
        Then, subtract the hours.
        5 h &minus; 3 h = 2 h
        
        So, 5 h 40 min &minus; 3 h 25 min = <b>2 h 15 min</b>
        '''
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, subtract the minutes.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(minutes1-minutes2)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, subtract the hours.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h &nbsp;&minus;&nbsp; "+str(hour2)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1-hour2)+" h</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'><b>"+answer+"</b></td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        [Person.Girlname] <walked> 5 h 30 min< last week.>
        <She walked> 2 h 45 min< this week.>
        <How much longer did she walk last week than this week?>
        (Write your answer as in the example below.
        Example: 3 h 45 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['walked',' last week.','She walked',' this week.','How much longer did she walk last week than this week?','She walked ',' longer last week than this week.',randint(4,8),'P3TS2a','Elementary Singapore Maths'],
                        ['cycled',' indoor.','She cycled',' outdoor.','How much longer did she cycle indoor than outdoor?','She cycled ',' longer indoor than outdoor.',randint(4,8),'P3TS2b','Elementary Singapore Maths'],
                        ['did',' of yoga.','She did',' of aerobics.','How much longer did she spend doing yoga than aerobics?','She spent ',' longer doing yoga than aerobics.',randint(4,8),'P3TS2c','Elementary Singapore Maths'],
                        ['swam for','.','She studied for','.','How much longer did she spend swimming than studying?','She spent ',' longer swimming than studying.',randint(4,8),'P3TS2d','Elementary Singapore Maths'],
                        ['took',' to solve a worksheet.','She took',' to read a comic.','How much longer did she take to solve the worksheet than to read the comic?','She took ',' longer to solve the worksheet than to read the comic.',randint(3,4),'P3TS2e','Elementary Singapore Maths'],
                        ['spent',' decorating her room.','She spent',' making a poster.','How much longer did she spend decorating her room than making the poster?','She spent ',' longer decorating her room than making the poster.',randint(3,4),'P3TS2f','Elementary Singapore Maths']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[7]
        self.hour2 = randint(1,self.hour1-2)
        self.minute2 = random.randrange(30,55,5)
        self.minute1 = random.randrange(5,self.minute2-5,5)
        
        self.problem = "%s %s %d h %d min%s<br>"%(self.name,self.item[0],self.hour1,self.minute1,self.item[1])
        self.problem = self.problem + "%s %d h %d min%s<br>"%(self.item[2],self.hour2,self.minute2,self.item[3])
        self.problem = self.problem + "%s<br><br><div style='display:inline-block;vertical-align:top;'>(Write your answer as in the example below.<br>Example: 1 h 48 min)</div>"%(self.item[4])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;margin-top:-20px;'><img src='/images/P3ProblemImages/"+self.item[8]+".png' title='"+self.item[9]+"'></div>"
        
        self.minutes1 = self.hour1*60+self.minute1
        self.minutes2 = self.hour2*60+self.minute2
        
        self.hour,self.minutes = divmod(self.minutes1-self.minutes2,60)
        
        self.answer = "%d h %d min"%(self.hour,self.minutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.hour1,self.hour2,self.minute1,self.minute2,self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,hour1,hour2,minutes1,minutes2,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        5 h 30 min - 2 h 45 min = ?

        First, subtract the minutes.
        30 min &minus; 45 min = ?  | We cannot subtract 45 min from 30 min. So regroup 5 h 30 min. |
            
        Regroup 5 h 30 min.
        5 h 30 min = 4 h 90 min
        
        Then, subtract.
        4 h 90 min - 2 h 45 min = 2 h 45 min
        
        She walked for <b>2 h 45 min</b> longer last week than this week.
        '''

        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>We have to find out:</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min &nbsp;=&nbsp; ?</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>First, subtract the minutes.</td><td rowspan=3 style='padding-left:0px; padding-right:0px;text-align:left;vertical-align:top'><div class='side' style='width:270px;text-align:left'>We cannot subtract "+str(minutes2)+" min from "+str(minutes1)+" min.<br>So, we regroup "+str(hour1)+" h "+str(minutes1)+" min.</div></td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left;vertical-align:top'>"+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(minutes2)+" min &nbsp;=&nbsp; ?</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>Regroup "+str(hour1)+" h "+str(minutes1)+" min.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;=&nbsp; "+str(hour1-1)+" h "+str(minutes1+60)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>Then, subtract.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1-1)+" h "+str(minutes1+60)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item1+"<b>"+answer+"</b>"+item2+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        [Person.Boyname1] <took> 5 h 40 min< to complete a project.>
        [Person.Boyname2] <took> 4 h 35 min< to complete the same project.>
        <How much longer did> [Person.Boyname1] <take than> [Person.Boyname2]< to complete the project?>
        (Write your answer as in the example below.
        Example: 3 h 45 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.BoyName,2)

        self.items = [
                        ['took',' to complete a project.','took',' to complete the same project.','How much longer did','take than',' to complete the project?','took',' to complete the project.',randint(3,10),'P3TS3a','Singapore Maths worksheets'],
                        ['practised on the piano for','.','practised on the piano for','.','How much longer did','practice on the piano than','?','practised for','.',randint(3,5),'P3TS3b','Singapore Maths worksheets'],
                        ['jogged for','.','jogged for','.','How much longer did','jog for than','?','jogged for','.',randint(2,4),'P3TS3c','Singapore Maths worksheets'],
                        ['watched TV for',' last week.','watched TV for',' last week.','How much longer did','spend than',' watching TV last week?','spent',' watching TV last week.',randint(6,10),'P3TS3d','Singapore Maths worksheets'],
                        ['took',' to finish a race.','took',' to finish the race.','How much longer did','take than',' to finish the race?','took',' to finish the race.',randint(2,4),'P3TS3e','Singapore Maths worksheets'],
                        ['took',' to prepare a presentation.','took',' to prepare the presentation.','How much longer did','take than',' to prepare the presentation?','took',' to prepare the presentation.',randint(3,5),'P3TS3f','Singapore Maths worksheets']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[9]
        self.hour2 = randint(1,self.hour1-1)
        self.minutes1 = random.randrange(30,55,5)
        self.minutes2 = random.randrange(5,self.minutes1-5,5)
        name1 = self.names[0]
        name2 = self.names[1]
                
        self.problem = "%s %s %d h %d min%s<br>"%(name1,self.item[0],self.hour1,self.minutes1,self.item[1])
        self.problem = self.problem + "%s %s %d h %d min%s<br>"%(name2,self.item[2],self.hour2,self.minutes2,self.item[3])
        self.problem = self.problem + "%s %s %s %s%s"%(self.item[4],self.names[0],self.item[5],self.names[1],self.item[6])
        self.problem = self.problem + "<br><br><div style='display:inline-block;vertical-align:top;'>(Write your answer as in the example below.<br>Example: 1 h 48 min)</div>"
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;margin-top:-20px;'><img src='/images/P3ProblemImages/"+self.item[10]+".png' title='"+self.item[11]+"'></div>"
        
        self.answer = "%d h %d min"%(self.hour1-self.hour2,self.minutes1-self.minutes2)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.hour1,self.hour2,self.minutes1,self.minutes2,self.item[7],self.item[8],name1,name2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,hour1,hour2,minutes1,minutes2,item1,item2,name1,name2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        First, subtract the minutes.
        40 min &minus; 35 min = 5 min
        
        Then, subtract the hours.
        5 h &minus; 4 h = 1 h
        
        Rayan took <b>1 h 5 min</b> longer than Ali to complete the project.
        '''
        
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, subtract the minutes.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(minutes1-minutes2)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, subtract the hours.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h &nbsp;&minus;&nbsp; "+str(hour2)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1-hour2)+" h</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+name1+" "+item1+" <b>"+answer+"</b> longer than "+name2+item2+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        [Person.Unclename] <spent> 8 h 15 min <picking and selling coconuts.>
        <He spent> 4 h 30 min <picking the coconuts.>
        <How long did he spend selling the coconuts?>
        (Write your answer as in the example below.
        Example: 3 h 45 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [
                        ['spent','picking and selling coconuts.','He spent','picking the coconuts.','How long did he spend selling the coconuts?','He spent ',' selling the coconuts.',randint(6,9),'P3TS4a','Primary 3 Singapore Maths problem sums time hours minutes subtraction'],
                        ['spent','teaching Science and English.','He spent','teaching Science.','How long did he spend teaching English?','He spent ',' teaching English.',randint(8,15),'P3TS4b','Primary 3 Singapore Maths problem sums time hours minutes subtraction'],
                        ['took','to pot and water some plants.','He took','to pot the plants.','How long did he take to water the plants?','He took ',' to water the plants.',randint(3,4),'P3TS4c','Primary 3 Singapore Maths problem sums time hours minutes subtraction'],
                        ['took','to climb up and down a hill.','He took','to climb up the hill.','How long did he take to climb down the hill?','He took ',' to climb down the hill.',randint(5,8),'P3TS4d','Primary 3 Singapore Maths problem sums time hours minutes subtraction'],
                        ['took','to go from City A to City B and back.','He took','to go from City A to City B.','How long did he take to return from City B to City A?','He took ',' to return from City B to City A.',randint(8,12),'P3TS4e','Primary 3 Singapore Maths problem sums time hours minutes subtraction'],
                        ['took','to build and tile a wall.','He took','to build the wall.','How long did he take to tile the wall?','He took ',' to tile the wall.',randint(4,8),'P3TS4f','Primary 3 Singapore Maths problem sums time hours minutes subtraction']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[7]
        self.hour2 = self.item[7] / 2 + 1
        self.minutes1 = random.randrange(30,55,5)
        self.minutes2 = random.randrange(5,self.minutes1-5,5)
        
        self.problem = "%s %s %d h %d min %s<br>"%(self.name,self.item[0],self.hour1,self.minutes1,self.item[1])
        self.problem = self.problem + "<div style='display:inline-block;vertical-align:top;'>%s %d h %d min %s<br>"%(self.item[2],self.hour2,self.minutes2,self.item[3])
        self.problem = self.problem + "%s<br><br>(Write your answer as in the example below.<br>Example: 1 h 48 min)</div>"%(self.item[4])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[8]+".png' title='"+self.item[9]+"'></div>"
        
        self.answer = "%d h %d min"%(self.hour1-self.hour2,self.minutes1-self.minutes2)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.hour1,self.hour2,self.minutes1,self.minutes2,self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,hour1,hour2,minutes1,minutes2,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        First, subtract the minutes.
        40 min &minus; 35 min = 5 min
        
        Then, subtract the hours.
        5 h &minus; 4 h = 1 h
        
        He spent <b>5 h 45 min</b> selling the coconuts.
        '''

        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>We have to find out:</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min &nbsp;=&nbsp; ?</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, subtract the minutes.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(minutes1-minutes2)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
            
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, subtract the hours.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h &nbsp;&minus;&nbsp; "+str(hour2)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1-hour2)+" h</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'><b>"+answer+"</b></td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
            
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item1+"<b>"+answer+"</b>"+item2+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        3 h 15 min &minus; 1 h 35 min = ______ h ______ min
        (Write your answer as in the example below.
        Example: 3 h 45 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.hour1 = randint(5,12)
        self.hour2 = randint(3,self.hour1-2)
        self.minute2 = random.randrange(30,55,5)
        self.minute1 = random.randrange(5,self.minute2-5,5)
        
        self.problem = "%d h %d min &minus; %d h %d min = ______ h ______ min<br><br>"%(self.hour1,self.minute1,self.hour2,self.minute2)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 1 h 48 min)"
        
        self.minutes1 = self.hour1*60+self.minute1
        self.minutes2 = self.hour2*60+self.minute2
        
        self.hour,self.minutes = divmod(self.minutes1-self.minutes2,60)
        
        self.answer = "%d h %d min"%(self.hour,self.minutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.hour1,self.hour2,self.minute1,self.minute2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,hour1,hour2,minutes1,minutes2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        First, subtract the minutes.
        15 min &minus; 35 min = ?  | We cannot subtract 35 min from 15 min. So regroup 3 h 15 min. |
            
        Regroup 3 h 15 min.
        3 h 15 min = 2 h 75 min
        
        Then, subtract.
        2 h 75 min - 1 h 35 min = 1 h 40 min
        '''
        
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>First, subtract the minutes.</td><td rowspan=3 style='padding-left:0px; padding-right:0px;text-align:left;vertical-align:top'><div class='side' style='width:270px;text-align:left'>We cannot subtract "+str(minutes2)+" min from "+str(minutes1)+" min.<br>So, we regroup "+str(hour1)+" h "+str(minutes1)+" min.</div></td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left;vertical-align:top'>"+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(minutes2)+" min &nbsp;=&nbsp; ?</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>Regroup "+str(hour1)+" h "+str(minutes1)+" min.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;=&nbsp; "+str(hour1-1)+" h "+str(minutes1+60)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>Then, subtract.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1-1)+" h "+str(minutes1+60)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'><b>"+answer+"</b></td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        It took 2 hours <to load and unload a truck>.
        It took 1 h 45 min <to load the truck>.
        How long did it take to <unload the truck>>
        (Write your answer as in the example below.
        Example: 2 h 40 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                        ['to load and unload a truck','to load the truck','unload the truck',randint(2,3),random.randrange(10,45,5),'P3TS6a','Third grade Singapore Maths online learning'],
                        ['to pack and unpack some boxes','to pack the boxes','unpack the boxes',randint(2,3),random.randrange(10,30,5),'P3TS6b','Third grade Singapore Maths online learning'],
                        ['to wash and dry some clothes','to wash the clothes','dry the clothes',randint(2,3),random.randrange(15,30,5),'P3TS6c','Third grade Singapore Maths online learning'],
                        ['to fill a tank then empty it','to fill the tank','empty the tank',randint(2,4),random.randrange(20,40,5),'P3TS6d','Third grade Singapore Maths online learning'],
                        ['to plant some trees and water them','to plant the trees','water them',randint(2,4),random.randrange(10,25,5),'P3TS6e','Third grade Singapore Maths online learning'],
                        ['to tile and polish a floor','to tile the floor','polish the floor',randint(2,4),random.randrange(10,20,5),'P3TS6f','Third grade Singapore Maths online learning']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[3]
        self.hour2 = self.hour1 - 1
        self.minutes2 = self.item[4]
        
        self.problem = "<div style='display:inline-block;vertical-align:top;'>It took %d hours %s.<br>"%(self.hour1,self.item[0])
        self.problem = self.problem + "It took %d h %d min %s.<br>"%(self.hour2,self.minutes2,self.item[1])
        self.problem = self.problem + "How long did it take to %s?<br><br></div>"%(self.item[2])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[5]+".png' title='"+self.item[6]+"'></div>"
        
        self.answer = 60 - self.minutes2
                   
        self.unit = "minutes"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.hour1,self.hour2,self.minutes2,self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,hour1,hour2,minutes2,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        2 h - 1 h 45 min = 2 h 0 min - 1 h 45 min

        First, subtract the minutes.
        0 min &minus; 45 min = ? | We cannot subtract 45 min from 0 min. So regroup 2 h 0 min. |
            
        Regroup 2 h 0 min.
        2 h 0 min = 1 h 60 min
        
        Then, subtract.
        1 h 60 min - 1 h 45 min = 0 h 15 min
                    = 15 min
        
        It took <b>15 minutes</b> to unload the truck.
        '''

        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>We have to find out:</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h 0 min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min &nbsp;=&nbsp; ?</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"

        self.solution_text = self.solution_text+"<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>First, subtract the minutes.</td><td rowspan=3 style='padding-left:0px; padding-right:0px;text-align:left;vertical-align:top'><div class='side' style='width:270px;text-align:left'>We cannot subtract "+str(minutes2)+" min from 0 min.<br>So, we regroup "+str(hour1)+" h 0 min.</div></td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left;vertical-align:top'>0 min &nbsp;&minus;&nbsp; "+str(minutes2)+" min &nbsp;=&nbsp; ?</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>Regroup "+str(hour1)+" h 0 min.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h 0 min &nbsp;=&nbsp; "+str(hour1-1)+" h 60 min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>Then, subtract.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h 0 min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1-1)+" h 60 min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>It took <b>"+str(answer)+" minutes</b> to "+item2+".</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        [Person.Girlname] <took> 5 h 10 min <to bake and pack some cookies.>
        <She took> 3 h 40 min <to bake the cookies.>
        <How long did she take to pack the cookies?>
        (Write your answer as in the example below.
        Example: 3 h 30 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['took','to bake and pack some cookies.','She took','to bake the cookies.','How long did she take to pack the cookies?','She took ',' to pack the cookies.',randint(4,6),'P3TS7a','Third grade Singapore math practice worksheets'],
                        ['took','to sort out photos and arrange them in an album.','She took','to sort out the photos.','How long did she take to arrange them in the album?','She took ',' to arrange them in the album.',randint(3,5),'P3TS7b','Third grade Singapore math practice worksheets'],
                        ['spent','doing her homework, and then helping her mother in the kitchen.','She spent','doing her homework.','How long did she help her mother in the kitchen?','She helped her mother for ',' in the kitchen.',randint(3,5),'P3TS7c','Third grade Singapore math practice worksheets'],
                        ['spent','in the library and the museum.','She spent','in the library.','How long did she spend in the museum?','She spent ',' in the museum.',randint(3,5),'P3TS7d','Third grade Singapore math practice worksheets'],
                        ['took','to make and pack some ribbon bows.','She took','to make the bows.','How long did she take to pack them?','She took ',' to pack them.',randint(4,7),'P3TS7e','Third grade Singapore math practice worksheets'],
                        ['took','to make a necklace and earrings.','She took','to make the necklace.','How long did she take to make the earrings?','She took ',' to make the earrings.',randint(3,5),'P3TS7f','Third grade Singapore math practice worksheets']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[7]
        if self.hour1%2==0:
            self.hour2 = self.hour1 / 2
        else:
            self.hour2 = (self.hour1+1) / 2
            
        self.minute1 = random.randrange(5,55,5)
        self.minute2 = random.randrange(5,55,5)
        
        self.problem = "%s %s %d h %d min %s<br>"%(self.name,self.item[0],self.hour1,self.minute1,self.item[1])
        self.problem = self.problem + "<div style='display:inline-block;vertical-align:top;'>%s %d h %d min %s<br>"%(self.item[2],self.hour2,self.minute2,self.item[3])
        self.problem = self.problem + "%s<br><br>(Write your answer as in the example below.<br>Example: 1 h 48 min)</div>"%(self.item[4])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[8]+".png' title='"+self.item[9]+"'></div>"
        
        self.minutes1 = self.hour1*60+self.minute1
        self.minutes2 = self.hour2*60+self.minute2
        
        self.hour,self.minutes = divmod(self.minutes1-self.minutes2,60)
        
        self.answer = "%d h %d min"%(self.hour,self.minutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.hour1,self.hour2,self.minute1,self.minute2,self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,hour1,hour2,minutes1,minutes2,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        self.solution_text =  "Coming Soon!!"
        
        '''
        if minutes1 >= minutes 2:
            First, subtract the minutes.
            40 min &minus; 35 min = 5 min
        
            Then, subtract the hours.
            5 h &minus; 4 h = 1 h
        
        else:
            First, subtract the minutes.
            10 min &minus; 40 min = ? | We cannot subtract 40 min from 10 min. So regroup 5 h 10 min. |
            
            Regroup 5 h 10 min.
            5 h 10 min = 4 h 70 min
        
            Then, subtract.
            4 h 70 min - 3 h 40 min = 1 h 30 min
        
        She took <b>1 h 30 min</b> to pack the cookies.
        '''
        
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>We have to find out:</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min &nbsp;=&nbsp; ?</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        if minutes1 >= minutes2:
            self.solution_text = self.solution_text+"<table border=0>"
            self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, subtract the minutes.</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(minutes1-minutes2)+" min</td></tr>"
            self.solution_text = self.solution_text+"</table>"
            self.solution_text = self.solution_text+"<br>"
            
            self.solution_text = self.solution_text+"<table border=0>"
            self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, subtract the hours.</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h &nbsp;&minus;&nbsp; "+str(hour2)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1-hour2)+" h</td><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text+"</table>"
            self.solution_text = self.solution_text+"<br>"

            self.solution_text = self.solution_text+"<table border=0>"
            self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td></tr>"
            self.solution_text = self.solution_text+"</table>"
            self.solution_text = self.solution_text+"<br>"
            
        else:
            self.solution_text = self.solution_text+"<table border=0>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>First, subtract the minutes.</td><td rowspan=3 style='padding-left:0px; padding-right:0px;text-align:left;vertical-align:top'><div class='side' style='width:270px;text-align:left'>We cannot subtract "+str(minutes2)+" min from "+str(minutes1)+" min.<br>So, we regroup "+str(hour1)+" h "+str(minutes1)+" min.</div></td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left;vertical-align:top'>"+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(minutes2)+" min &nbsp;=&nbsp; ?</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>Regroup "+str(hour1)+" h "+str(minutes1)+" min.</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;=&nbsp; "+str(hour1-1)+" h "+str(minutes1+60)+" min</td></tr>"
            self.solution_text = self.solution_text+"</table>"
            self.solution_text = self.solution_text+"<br>"
    
            self.solution_text = self.solution_text+"<table border=0>"
            self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>Then, subtract.</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1-1)+" h "+str(minutes1+60)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td></tr>"
            self.solution_text = self.solution_text+"</table>"
            self.solution_text = self.solution_text+"<br>"
            
        if minutes1==minutes2:
            self.solution_text = self.solution_text+"<table border=0>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item1+"<b>"+str(hour1-hour2)+" hours</b>"+item2+"</td></tr>"
            self.solution_text = self.solution_text+"</table>"
        else:
            self.solution_text = self.solution_text+"<table border=0>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item1+"<b>"+answer+"</b>"+item2+"</td></tr>"
            self.solution_text = self.solution_text+"</table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        [Person.Auntyname] <opens her store for> 5 h 40 min <before lunch.>
        <She opens it again for> 4 h 15 min <after lunch.>
        <How much longer does she open the store before lunch than after lunch?>
        (Write your answer as in the example below.
        Example: 2 h 30 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [
                        ['opens her store for','before lunch.','She opens it again for','after lunch.','How much longer does she open the store before lunch than after lunch?','She opens the store for ',' longer before lunch than after lunch.',randint(3,5),'P3TS8a','Free Grade 3 Singapore math worksheets'],
                        ['teaches for','at a school.','She also teaches for','at a community centre.','How much longer does she teach at the school than at the community centre?','She teaches for ',' longer at the school than at the community centre.',randint(4,6),'P3TS8b','Free Grade 3 Singapore math worksheets'],
                        ['opens her cafe for','for dinner.','She also opens it for','for lunch.','How much longer does she open the cafe for dinner than for lunch?','She opens the cafe ',' longer for dinner than for lunch.',randint(3,5),'P3TS8c','Free Grade 3 Singapore math worksheets'],
                        ['works for','in the morning.','She works again for','in the afternoon.','How much longer does she work in the morning than in the afternoon?','She works ',' longer in the morning than in the afternoon.',randint(4,6),'P3TS8d','Free Grade 3 Singapore math worksheets'],
                        ['drives her taxi for','in the morning.','She drives her taxi again for','in the evening.','How much longer does she drive in the morning than in the afternoon?','She drives ',' longer in the morning than in the afternoon.',randint(5,7),'P3TS8e','Free Grade 3 Singapore math worksheets'],
                        ['works for','at a hospital.','She also works for','at a clinic.','How much longer does she work at the hospital than at the clinic?','She works for ',' longer at the hospital than at the clinic.',randint(4,6),'P3TS8f','Free Grade 3 Singapore math worksheets']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[7]
        self.hour2 = self.hour1 - randint(1,2)           
        self.minutes1 = random.randrange(30,55,5)
        self.minutes2 = random.randrange(10,self.minutes1-5,5)
        
        self.problem = "%s %s %d h %d min %s<br>"%(self.name,self.item[0],self.hour1,self.minutes1,self.item[1])
        self.problem = self.problem + "%s %d h %d min %s<br>"%(self.item[2],self.hour2,self.minutes2,self.item[3])
        self.problem = self.problem + "%s<div style='display:inline-block;vertical-align:top;'><br><br>(Write your answer as in the example below.<br>Example: 1 h 30 min)</div>"%(self.item[4])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[8]+".png' title='"+self.item[9]+"'></div>"
        
        self.answer = "%d h %d min"%(self.hour1-self.hour2,self.minutes1-self.minutes2)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.hour1,self.hour2,self.minutes1,self.minutes2,self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,hour1,hour2,minutes1,minutes2,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        First, subtract the minutes.
        40 min &minus; 15 min = 25 min
        
        Then, subtract the hours.
        5 h &minus; 4 h = 1 h
        
        She opens the store <b>1 h 25 min</b> longer before lunch than after lunch.
        '''
        
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>We have to find out:</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min &nbsp;=&nbsp; ?</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, subtract the minutes.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(minutes1-minutes2)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
            
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, subtract the hours.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h &nbsp;&minus;&nbsp; "+str(hour2)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1-hour2)+" h</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;&minus;&nbsp; "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item1+"<b>"+answer+"</b>"+item2+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"").lower()
                answer = string.join(str(answer).split(),"")              
                return answer==InputAnswer
            except ValueError:
                return False
        elif CheckAnswer == 2:
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"").lower()
                answer = string.join(str(answer).split(),"")
                answer1 = answer
                if answer.partition("h")[2]=="0min":
                    answer1 = answer.partition("h")[0]+answer.partition("h")[1]                
                return answer==InputAnswer or answer1==InputAnswer
            except ValueError:
                return False                      