'''
Created on Jul 08, 2013
Module: P3TIAddition
Generates the Addition Time problems on Time for Primary 3

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

class P3TIAddition:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemType4",],
                            5:["ProblemType5",],6:["ProblemType6",],7:["ProblemType7",],8:["ProblemType8a","ProblemType8b",],
                            9:["ProblemType9",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],4:[self.GenerateProblemType4(),],
                                    5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],7:[self.GenerateProblemType7(),],
                                    8:[self.GenerateProblemType8a(),self.GenerateProblemType8b(),],
                                    9:[self.GenerateProblemType9(),],                                   
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
        #return self.GenerateProblemType2()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8a":self.GenerateProblemType8a(),"ProblemType8b":self.GenerateProblemType8b(),
                            "ProblemType9":self.GenerateProblemType9(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        2 h 23 min + 3 h 18 min = _____ h ____ min
        (Write your answer as in the example below.
        Example: 5 h 48 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.hour1 = randint(2,8)
        self.hour2 = randint(2,8)
        self.minutes1 = randint(5,50)
        self.minutes2 = randint(5,59-self.minutes1)
        
        self.problem = "%d h %d min + %d h %d min = _____ h ____ min<br><br>"%(self.hour1,self.minutes1,self.hour2,self.minutes2)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 h 48 min)"
        
        self.answer = "%d h %d min"%(self.hour1+self.hour2,self.minutes1+self.minutes2)
                   
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
        First, add the minutes.
        23 min + 18 min = 41 min

        Then, add the hours.
        2 h + 3 h = 5 h

        So, 2 h 23 min + 3 h 18 min = <b>5 h 41 min</b>
        '''
       
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, add the minutes.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(minutes1)+" min + "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(minutes1+minutes2)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, add the hours.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h + "+str(hour2)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1+hour2)+" h</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min + "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'><b>"+answer+"</b></td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        [Person.Girlname] <walked> 37 minutes <in the morning.>
        <She walked> 28 minutes <in the evening.>
        <How long did she walk altogether?>
        (Write your answer as in the example below.
        Example: 1 h 48 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['walked','in the morning.','She walked','in the evening.','How long did she walk altogether?','She walked for','altogether. ',randint(25,40),'P3A2a','Grade 3 Singapore Maths'],
                        ['cycled','in the afternoon.','She cycled','at night.','How long did she cycle altogether?','She cycled for','altogether.',randint(25,40),'P3A2b','Grade 3 Singapore Maths'],
                        ['exercised','in the gym.','She exercised','outdoor.','How long did she exercise altogether?','She exercised','altogether.',randint(25,40),'P3A2c','Grade 3 Singapore Maths'],
                        ['swam for','.','She played on the slides for','.','How long did she spend on the two activities?','She spent','on the two activities.',randint(25,40),'P3A2d','Grade 3 Singapore Maths'],
                        ['spent','reading a storybook.','She spent','solving a maths worksheet.','How long did she spend on the two tasks?','She spent','on the two tasks.',randint(25,40),'P3A2e','Grade 3 Singapore Maths'],
                        ['spent','making a card.','She spent','wrapping a present.','How long did she spend on the two tasks?','She spent','on the two tasks.',randint(25,40),'P3A2f','Grade 3 Singapore Maths']
                    ]
        
        self.item = random.choice(self.items)
                
        self.minutes1 = self.item[7]
        self.minutes2 = randint(60-self.minutes1,50)
        
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %s %d minutes %s<br>"%(self.name,self.item[0],self.minutes1,self.item[1])
        self.problem = self.problem + "%s %d minutes %s<br>"%(self.item[2],self.minutes2,self.item[3])
        self.problem = self.problem + "%s<br><br>(Write your answer as in the example below.<br>Example: 1 h 48 min)</div>"%(self.item[4])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[8]+".png' title='"+self.item[9]+"'></div>"
        
        self.hour,self.minutes = divmod(self.minutes1+self.minutes2,60)
        
        self.answer = "%d h %d min"%(self.hour,self.minutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.minutes1,self.minutes2,self.minutes,self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,minutes1,minutes2,minutes3,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        37 min + 28 min = 65 min

        if (65  > 60 min)
        65 min = 60 min + 5 min
               = 1 h 5 min
        
        else
        60 min = 1 h 0 min

        Falaq walked for 1 h 5 min altogether.
        '''
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(minutes1)+" min + "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(minutes1+minutes2)+" min</td></tr>"
        if minutes3 > 0:
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>60 min + "+str(minutes3)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>1 h "+str(minutes3)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        if minutes3 > 0:
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item1+" <b>"+answer+"</b> "+item2+"</td></tr>"
        else:
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item1+" <b>1 hour</b> "+item2+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        [Person.Boyname] <had> 5 h 35 min <of Science lessons and> 6 h 40 min <of Maths lessons last week.>
        <How long were his Science and Maths lessons altogether last week?>
        (Write your answer as in the example below.
        Example: 5 h 48 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                        ['had','of Science lessons and','of Maths lessons last week.','How many hours and minutes of Science and Maths lessons did he have altogether last week?','He had','of Science and Maths lessons last week.',randint(3,5),randint(5,7),'P3A3a','Primary 3 Singapore Maths tuition'],
                        ['played','at his home and',"at his friend's house.",'How long did he play at the two places altogether?','He played for','at the two places.',randint(1,2),randint(3,5),'P3A3b','Primary 3 Singapore Maths tuition'],
                        ['watched','of TV on Saturday and','of TV on Sunday.','How much time did he spend watching TV on the two days?','He spent','watching TV on the two days.',randint(1,3),randint(1,3),'P3A3c','Primary 3 Singapore Maths tuition'],
                        ['spent','practising on his drums then','listening to music.','How many hours and minutes did he spend on the two activities?','He spent','on the two activities.',randint(1,3),randint(1,3),'P3A3d','Primary 3 Singapore Maths tuition'],
                        ['spent','watching a tennis game then','watching a basketball game.','How long did he spend watching the two games?','He spent','watching the two games.',randint(1,2),randint(1,2),'P3A3e','Primary 3 Singapore Maths tuition'],
                        ['spent','doing his homework then','playing.','How long did he spend on the two activities?','He spent','on the two activities.',randint(1,3),randint(1,3),'P3A3f','Primary 3 Singapore Maths tuition']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[6]
        self.hour2 = self.item[7]        
        self.minutes1 = random.randrange(25,55,5)
        self.minutes2 = random.randrange(65-self.minutes1,55,5)
        
        self.problem = "%s %s %d h %d min %s %d h %d min %s<br>"%(self.name,self.item[0],self.hour1,self.minutes1,
                                                                                                                        self.item[1],self.hour2,self.minutes2,self.item[2])
        self.problem = self.problem + "%s<br><br><div style='display:inline-block;vertical-align:top;'>(Write your answer as in the example below.<br>Example: 1 h 48 min)</div>"%(self.item[3])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;margin-top:-20px;'><img src='/images/P3ProblemImages/"+self.item[8]+".png' title='"+self.item[9]+"'></div>"
        
        self.hour,self.minutes = divmod(self.minutes1+self.minutes2,60)
        
        self.answer = "%d h %d min"%(self.hour+self.hour1+self.hour2,self.minutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.hour1,self.hour2,self.hour,self.minutes1,self.minutes2,self.minutes,self.item[4],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,hour1,hour2,hour3,minutes1,minutes2,minutes3,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        '''
        First, add the minutes.
        35 min + 40 min = 75 min   | 75 min is more than 60 min. So, regroup the result. |
        75 min = 60 min + 15 min
               = 1 h 15 min
        
        Then, add the hours.
        5 h + 6 h + 1 h 15 min = 12 h 15 min
        
        His Science and Maths lessons were 12 h 15 min altogether.
        '''
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, add the minutes.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left;vertical-align:top'>"+str(minutes1)+" min + "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>=</td><td style='text-align:left;vertical-align:top'>"+str(minutes1+minutes2)+" min</td><td rowspan=3 style='padding-left:0px; padding-right:0px;vertical-align:top'><div class='side' style='width:200px;text-align:left'>"+str(minutes1+minutes2)+" min is more than 60 min.<br>So, regroup the result.</div></td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>60 min + "+str(minutes3)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>1 h "+str(minutes3)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, add the hours.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h + "+str(hour2)+" h + "+str(hour3)+" h "+str(minutes3)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item1+" <b>"+answer+"</b> "+item2+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        [Person.Unclename] <spent> 2 h 15 min <picking coconuts on his farm.>
        <Then he spent> 4 h 30 min <selling the coconuts in the market.>
        <How long did he spend picking and selling the coconuts?>
        (Write your answer as in the example below.
        Example: 5 h 48 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [
                        ['spent','picking coconuts on his farm.','Then he spent','selling the coconuts in the market.','How long did he spend picking and selling the coconuts?','He spent','picking and selling the coconuts.',randint(1,3),randint(3,5),'P3A4a','Primary 3 Singapore Maths problem sums time hours minutes addition'],
                        ['spent','teaching in the classroom.','Then he spent','teaching outdoor.','How long did he spend teaching?','He spent','teaching.',randint(2,4),randint(1,2),'P3A4b','Primary 3 Singapore Maths problem sums time hours minutes addition'],
                        ['spent','cutting the grass.','Then he spent','planting some trees.','How long did he spend on the two activities?','He spent','on the two activities.',randint(1,2),randint(2,3),'P3A4c','Primary 3 Singapore Maths problem sums time hours minutes addition'],
                        ['took','to climb up a hill.','Then he took','to climb down the hill.','How much time did he take to climb up and down the hill?','He took','to climb up and down the hill.',randint(3,4),randint(1,2),'P3A4d','Primary 3 Singapore Maths problem sums time hours minutes addition'],
                        ['took','to go from City A to City B.','He took','to return from City B to City A.','How long did he take to make the round trip?','He took','to make the round trip.',randint(3,4),randint(4,5),'P3A4e','Primary 3 Singapore Maths problem sums time hours minutes addition'],
                        ['took','to build a wall.','He took','to paint the wall.','How long did he take to build and paint the wall?','He took','to build and paint the wall.',randint(8,10),randint(1,2),'P3A4f','Primary 3 Singapore Maths problem sums time hours minutes addition']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[7]
        self.hour2 = self.item[8]        
        self.minutes1 = random.randrange(15,40,5)
        self.minutes2 = random.randrange(5,55-self.minutes1,5)
        
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %s %d h %d min %s<br>"%(self.name,self.item[0],self.hour1,self.minutes1,self.item[1])
        self.problem = self.problem + "%s %d h %d min %s<br>"%(self.item[2],self.hour2,self.minutes2,self.item[3])
        self.problem = self.problem + "%s<br><br>(Write your answer as in the example below.<br>Example: 5 h 48 min)</div>"%(self.item[4])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[9]+".png' title='"+self.item[10]+"'></div>"
        
        self.answer = "%d h %d min"%(self.hour1+self.hour2,self.minutes1+self.minutes2)
                   
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
        First, add the minutes.
        15 min + 30 min = 45 min
        
        Then, add the hours.
        2 h + 4 h = 6 h
        
        So, 2 h 15 min + 4 h 30 min = <b>6 h 45 min</b>
        
        He spent <b>6 h 45 min</b> picking and selling the coconuts.
        '''
        
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, add the minutes.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(minutes1)+" min + "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(minutes1+minutes2)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, add the hours.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h + "+str(hour2)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1+hour2)+" h</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min + "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item1+" <b>"+answer+"</b> "+item2+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        43 min + 38 min = ______ h ______ min
        (Write your answer as in the example below.
        Example: 1 h 48 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
     
        self.minutes1 = randint(15,55)
        self.minutes2 = randint(65-self.minutes1,55)
        
        self.problem = "%d min + %d min = ______ h ______ min<br><br>"%(self.minutes1,self.minutes2)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 1 h 48 min)"
        
        self.hour,self.minutes = divmod(self.minutes1+self.minutes2,60)
                
        self.answer = "%d h %d min"%(self.hour,self.minutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.minutes1,self.minutes2,self.minutes,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,minutes1,minutes2,minutes3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        43 min + 38 min = 81 min

        if (65  > 60 min)
        81 min = 60 min + 21 min
               = 1 h 21 min
        
        else
        60 min = 1 h 0 min
        
        So, 43 min + 38 min = <b>1 h 21 min</b>
        '''
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left;vertical-align:top'>"+str(minutes1)+" min + "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>=</td><td style='text-align:left;vertical-align:top'>"+str(minutes1+minutes2)+" min</td><td rowspan=3 style='padding-left:0px; padding-right:0px;vertical-align:top'><div class='side' style='width:200px;text-align:left'>"+str(minutes1+minutes2)+" min is more than 60 min.<br>So, regroup the result.</div></td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>60 min + "+str(minutes3)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>1 h "+str(minutes3)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(minutes1)+" min + "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'><b>"+answer+"</b></td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        <It took> 1 h 45 min <to load the truck.>
        <It took> 15 mintues <to unload the truck.>
        <How long did it take to load and unload the truck?>
        (Write your answer as in the example below.
        Example: 5 h 48 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                        ['It took','to load a truck.','It took','to unload the truck.','How long did it take to load and unload the truck?','It took','to load and unload the truck.',randint(2,3),random.randrange(10,45,5),'P3A6a','Primary 3 Singapore Maths home tuition'],
                        ['It took','to pack some boxes.','It took','to unpack the boxes.','How long did it take to pack and unpack the boxes?','It took','to pack and unpack the boxes.',randint(1,2),random.randrange(10,30,5),'P3A6b','Primary 3 Singapore Maths home tuition'],
                        ['It took','to wash some clothes.','It took','to dry the clothes.','How long did it take to wash and dry the clothes?','It took','to wash and dry the clothes.',randint(1,2),random.randrange(15,30,5),'P3A6c','Primary 3 Singapore Maths home tuition'],
                        ['It took','to fill a tank.','It took','to empty the tank.','How long did it take to fill and empty the tank?','It took','to fill and empty the tank.',randint(1,3),random.randrange(20,40,5),'P3A6d','Primary 3 Singapore Maths home tuition'],
                        ['It took','to pot some plants.','It took','to water them.','How long did it take to pot the plants and water them?','It took','to pot the plants and water them.',randint(2,3),random.randrange(10,25,5),'P3A6e','Primary 3 Singapore Maths home tuition'],
                        ['It took','to tile a floor.','It took','to polish the floor.','How long did it take to tile and polish the floor?','It took','to tile and polish the floor.',randint(1,3),random.randrange(10,20,5),'P3A6f','Primary 3 Singapore Maths home tuition']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[7]        
        self.minutes1 = self.item[8]
        self.minutes2 = 60 - self.minutes1
        
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %d h %d min %s<br>"%(self.item[0],self.hour1,self.minutes1,self.item[1])
        self.problem = self.problem + "%s %d mintues %s<br>"%(self.item[2],self.minutes2,self.item[3])
        self.problem = self.problem + "%s<br><br>(Write your answer as in the example below.<br>Example: 5 h 48 min)</div>"%(self.item[4])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[9]+".png' title='"+self.item[10]+"'></div>"
        
        self.answer = "%d h 0 min"%(self.hour1+1)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.hour1,self.minutes1,self.minutes2,self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,hour1,minutes1,minutes2,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        First, add the minutes.
        45 min + 15 min = 60 min
                = 1 h 0 min
        
        Then, add the hours.
        1 h + 1 h 0 min = 2 h
        
        So, 1 h 45 min + 15 min = <b>2 h 0 min</b>
        
        It took <b>2 h 0 min</b> to load and unload the truck.
        '''

        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, add the minutes.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(minutes1)+" min + "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>60 min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>1 h 0 min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, add the hours.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h + 1 h 0 min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1+1)+" h 0 min</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min + "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item1+" <b>"+str(hour1+1)+" hours</b> "+item2+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        [Person.Auntyname] <runs a handicrafts store.>
        <Each day, she opens her store for> 5 h 40 min <before lunch.>
        <She opens it again for> 4 h 15 min <after lunch.>
        <How long does she open the store every day?>
        (Write your answer as in the example below.
        Example: 5 h 48 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [
                        ['runs a handicrafts store.','Each day, she opens her store for','before lunch.','She opens it again for','after lunch.','How long does she open the store every day?','She opens the store for','every day.',randint(3,5),randint(3,5),'P3A7a','Grade 3 Singapore math worksheets'],
                        ['is a teacher.','Each morning, she teaches for','at a school.','She also teaches for','at a community centre each evening.','How long does she teach every day?','She teaches','every day.',randint(3,5),randint(1,2),'P3A7b','Grade 3 Singapore math worksheets'],
                        ['runs a cafe.','Each day, she opens her cafe for','for lunch.','She opens it again for','for dinner.','How long does she open her cafe every day?','She opens her cafe for','every day.',randint(3,4),randint(3,5),'P3A7c','Grade 3 Singapore math worksheets'],
                        ['is a tailor.','Each day, she works for','in the morning.','She works again for','in the afternoon.','How long does she work every day?','She works','every day.',randint(2,3),randint(3,4),'P3A7d','Grade 3 Singapore math worksheets'],
                        ['is a taxi driver.','Each day, she works for','in the morning.','She works again for','in the afternoon.','How long does she work every day?','She works','every day.',randint(3,4),randint(3,4),'P3A7e','Grade 3 Singapore math worksheets'],
                        ['is a nurse.','Each morning, she works for','at a hospital.','She also works for','at a clinic each evening.','How long does she work every day?','She works','every day.',randint(2,3),randint(3,4),'P3A7f','Grade 3 Singapore math worksheets']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[8]
        self.hour2 = self.item[9]        
        self.minutes1 = random.randrange(15,35,5)
        self.minutes2 = random.randrange(15,55-self.minutes1,5)
        
        self.problem = "%s %s<br>"%(self.name,self.item[0])
        self.problem = self.problem + "%s %d h %d min %s<br>"%(self.item[1],self.hour1,self.minutes1,self.item[2])
        self.problem = self.problem + "%s %d h %d min %s<br>"%(self.item[3],self.hour2,self.minutes2,self.item[4])
        self.problem = self.problem + "<div style='display:inline-block;vertical-align:top;'>%s<br><br>(Write your answer as in the example below.<br>Example: 5 h 48 min)</div>"%(self.item[5])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:40px;'><img src='/images/P3ProblemImages/"+self.item[10]+".png' title='"+self.item[11]+"'></div>"
        
        self.answer = "%d h %d min"%(self.hour1+self.hour2,self.minutes1+self.minutes2)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.hour1,self.hour2,self.minutes1,self.minutes2,self.item[6],self.item[7],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,hour1,hour2,minutes1,minutes2,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        First, add the minutes.
        40 min + 15 min = 55 min
        
        Then, add the hours.
        5 h + 4 h = 9 h
        
        So, 5 h 40 min + 4 h 15 min = <b>9 h 55 min</b>
        
        She opens the store for <b>9 h 55 min</b> every day.
        '''
        
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, add the minutes.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(minutes1)+" min + "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(minutes1+minutes2)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, add the hours.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h + "+str(hour2)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1+hour2)+" h</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min + "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item1+" <b>"+answer+"</b> "+item2+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8a(self):       
        '''e.g.:
        2 h 24 min + 3 h 36 min = ______ h ______ min
        (Write your answer as in the example below.
        Example: 5 h 48 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.hour1 = randint(3,8)
        self.hour2 = randint(3,8)        
        self.minutes1 = randint(10,40)
        self.minutes2 = 60 - self.minutes1
        
        self.problem = "%d h %d min + %d h %d min = ______ h ______ min<br><br>"%(self.hour1,self.minutes1,self.hour2,self.minutes2)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 h 48 min)"
        
        self.answer = "%d h 0 min"%(self.hour1+self.hour2+1)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8a(self.problem,self.answer,self.hour1,self.hour2,self.minutes1,self.minutes2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8a(self,problem,answer,hour1,hour2,minutes1,minutes2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        First, add the minutes.
        24 min + 36 min = 60 min
                        = 1 h 0 min
        
        Then, add the hours.
        5 h + 2 h + 1 h 0 min = 8 h 0 min
        
        So, 5 h 24 min + 2 h 36 min = <b>8 h 0 min</b>
        '''
        
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, add the minutes.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(minutes1)+" min + "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>60 min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>1 h 0 min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, add the hours.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h + "+str(hour2)+" h + 1 h 0 min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour1+hour2+1)+" h 0 min</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min + "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'><b>"+answer+"</b></td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8b(self):       
        '''e.g.:
        2 h 24 min + 3 h 36 min = ______ h ______ min
        (Write your answer as in the example below.
        Example: 5 h 48 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.hour1 = randint(3,8)
        self.hour2 = randint(3,8)        
        self.minutes1 = randint(25,45)
        self.minutes2 = randint(65-self.minutes1,55)
        
        self.problem = "%d h %d min + %d h %d min = ______ h ______ min<br><br>"%(self.hour1,self.minutes1,self.hour2,self.minutes2)
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 h 48 min)"
        
        self.hour,self.minutes = divmod(self.minutes1+self.minutes2,60)
        self.answer = "%d h %d min"%(self.hour1+self.hour2+self.hour,self.minutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8b(self.problem,self.answer,self.hour1,self.hour2,self.hour,self.minutes1,self.minutes2,self.minutes,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8b(self,problem,answer,hour1,hour2,hour3,minutes1,minutes2,minutes3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        First, add the minutes.
        19 min + 47 min = 66 min   | 66 min is more than 60 min. So, regroup the result. |
        66 min = 60 min + 6 min
               = 1 h 6 min
        
        Then, add the hours.
        5 h + 2 h + 1 h 6 min = 8 h 6 min
        
        So, 5 h 19 min + 2 h 47 min = <b>8 h 6 min</b>
        '''
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, add the minutes.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left;vertical-align:top'>"+str(minutes1)+" min + "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>=</td><td style='text-align:left;vertical-align:top'>"+str(minutes1+minutes2)+" min</td><td rowspan=3 style='padding-left:0px; padding-right:0px;vertical-align:top'><div class='side' style='width:200px;text-align:left'>"+str(minutes1+minutes2)+" min is more than 60 min.<br>So, regroup the result.</div></td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>60 min + "+str(minutes3)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>1 h "+str(minutes3)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, add the hours.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h + "+str(hour2)+" h + "+str(hour3)+" h "+str(minutes3)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min + "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'><b>"+answer+"</b></td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        [Person.Girlname] <took> 3 h 20 min <to bake some biscuits.>
        <She took> 1 h 20 min <to pack them into boxes.>
        <How long did she take to bake and pack the bisuits?>
        (Write your answer as in the example below.
        Example: 5 h 48 min)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['took','to bake some biscuits.','She took','to pack them into boxes.','How long did she take to bake and pack the biscuits?','She took','to bake and pack the biscuits.',randint(3,4),randint(1,2),'P3A9a','Grade 3 Singapore math practice worksheets'],
                        ['spent','collecting shells.','She spent','decorating a scrapbook with the shells.','How long did she take to do the two activities?','She took','to do the two activities.',randint(3,4),randint(1,2),'P3A9b','Grade 3 Singapore math practice worksheets'],
                        ['spent','doing her homework.','She spent','helping her mother in the kitchen.','How long did she spend on the two tasks?','She spent','on the two tasks.',randint(2,3),randint(1,2),'P3A9c','Grade 3 Singapore math practice worksheets'],
                        ['spent','in the library.','She spent','in the museum.','How much time did she spend at the two places?','She spent','at the two places.',randint(1,3),randint(1,3),'P3A9d','Grade 3 Singapore math practice worksheets'],
                        ['took','to make some ribbon bows.','She took','to pack them into bags.','How much time did she spend making and packing the bows?','She spent','making and packing the bows.',randint(3,5),randint(1,2),'P3A9e','Grade 3 Singapore math practice worksheets'],
                        ['took','to make a necklace.','She took','to make a pair of earrings.','How much time did she take to make the necklace and the earrings?','She took','to make the necklace and the earrings.',randint(1,2),randint(2,3),'P3A9f','Grade 3 Singapore math practice worksheets']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[7]
        self.hour2 = self.item[8]        
        self.minutes1 = random.randrange(25,35,5)
        self.minutes2 = random.randrange(65-self.minutes1,55,5)
        
        self.problem = "%s %s %d h %d min %s<br>"%(self.name,self.item[0],self.hour1,self.minutes1,self.item[1])
        self.problem = self.problem + "%s %d h %d min %s<br>"%(self.item[2],self.hour2,self.minutes2,self.item[3])
        self.problem = self.problem + "%s<br><br><div style='display:inline-block;vertical-align:top;'>(Write your answer as in the example below.<br>Example: 5 h 48 min)</div>"%(self.item[4])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:40px;margin-top:-20px;'><img src='/images/P3ProblemImages/"+self.item[9]+".png' title='"+self.item[10]+"'></div>"
        
        self.hour,self.minutes = divmod(self.minutes1+self.minutes2,60)
        
        self.answer = "%d h %d min"%(self.hour1+self.hour2+self.hour,self.minutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.hour1,self.hour2,self.hour,self.minutes1,self.minutes2,self.minutes,self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,hour1,hour2,hour3,minutes1,minutes2,minutes3,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        First, add the minutes.
        40 min + 30 min = 70 min   | 70 min is more than 60 min. So, regroup the result. |
        if (70  > 60 min)
        70 min = 60 min + 10 min
               = 1 h 10 min
        
        else
        60 min = 1 h 0 min
        
        Then, add the hours.
        3 h + 1 h + 1 h 10 min = 5 h 10 min
        
        So, 3 h 40 min + 1 h 30 min = <b>5 h 10 min</b>
        '''
        self.solution_text = "<br><table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=3 style='text-align:left'>First, add the minutes.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left;vertical-align:top'>"+str(minutes1)+" min + "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px;vertical-align:top'>=</td><td style='text-align:left;vertical-align:top'>"+str(minutes1+minutes2)+" min</td><td rowspan=3 style='padding-left:0px; padding-right:0px;vertical-align:top'><div class='side' style='width:200px;text-align:left'>"+str(minutes1+minutes2)+" min is more than 60 min.<br>So, regroup the result.</div></td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>60 min + "+str(minutes3)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>1 h "+str(minutes3)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>Then, add the hours.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h + "+str(hour2)+" h + "+str(hour3)+" h "+str(minutes3)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=4 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(hour1)+" h "+str(minutes1)+" min + "+str(hour2)+" h "+str(minutes2)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item1+" <b>"+answer+"</b> "+item2+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"").lower()
                answer = string.join(str(answer).split(),"")
                hour = answer.partition("h")[0]
                mins = answer.partition("h")[2].partition("min")[0]
                answers = ["%shours%sminutes"%(hour,mins),"%shour%sminutes"%(hour,mins),"%shrs%sminutes"%(hour,mins),"%shr%sminutes"%(hour,mins),"%sh%sminutes"%(hour,mins),
                           "%shours%smins"%(hour,mins),"%shour%smins"%(hour,mins),"%shrs%smins"%(hour,mins),"%shr%smins"%(hour,mins),"%sh%smins"%(hour,mins),
                           "%shours%smin"%(hour,mins),"%shour%smin"%(hour,mins),"%shrs%smin"%(hour,mins),"%shr%smin"%(hour,mins),"%sh%smin"%(hour,mins),answer]
                return InputAnswer in answers
            except ValueError:
                return False
        elif CheckAnswer == 2:
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"").lower()
                answer = string.join(str(answer).split(),"")
                hour = answer.partition("h")[0]
                mins = answer.partition("h")[2].partition("min")[0]
                answers = ["%shours%sminutes"%(hour,mins),"%shour%sminutes"%(hour,mins),"%shrs%sminutes"%(hour,mins),"%shr%sminutes"%(hour,mins),"%sh%sminutes"%(hour,mins),
                           "%shours%smins"%(hour,mins),"%shour%smins"%(hour,mins),"%shrs%smins"%(hour,mins),"%shr%smins"%(hour,mins),"%sh%smins"%(hour,mins),
                           "%shours%smin"%(hour,mins),"%shour%smin"%(hour,mins),"%shrs%smin"%(hour,mins),"%shr%smin"%(hour,mins),"%sh%smin"%(hour,mins),answer]
                answers1 = answers
                if answer.partition("h")[2]=="0min":
                    answers1 = ["%sh"%(hour),"%shr"%(hour),"%shrs"%(hour),"%shour"%(hour),"%shours"%(hour),]                
                return InputAnswer in answers or InputAnswer in answers1
            except ValueError:
                return False                      