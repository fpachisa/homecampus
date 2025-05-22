'''
Created on Jun 26, 2013
Module: P3TIConversionTime
Generates the Converion Time in Hours and Minutes problems on Time for Primary 3

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

class P3TIConversionTime:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            3:["ProblemType3",],
                            4:["ProblemType4",],
                            5:["ProblemType5",],
                            6:["ProblemType6",],
                            7:["ProblemType7",],
                            8:["ProblemType8",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],
                                    5:[self.GenerateProblemType5(),],
                                    6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],
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
        #return self.GenerateProblemType3()
        
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
        How many minutes are there in 2 h 30 min?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.hour = randint(1,10)
        self.minutes = randint(1,59)
        
        self.problem = "How many minutes are there in %d h %d min?"%(self.hour,self.minutes)
        
        self.answer = self.hour*60+self.minutes
                   
        self.unit = "minutes"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.hour,self.minutes,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,hour,minutes,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        self.solution_text = "<br><table>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>We know,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>1 h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>60 min</td></tr>"
        if hour > 1:
            self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
            self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>"+str(hour)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour)+" &times; 60 min</td></tr>"
            self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour*60)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>Therefore,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>"+str(hour)+" h + "+str(minutes)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour*60)+" min + "+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>There are <b>"+str(answer)+"</b> minutes in "+str(hour)+" h "+str(minutes)+" min.</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        [Person.Boyname] <jogs for> 2 hours< each week>.
        How many minutes <does he spend jogging each week>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                        ['jogs for',' each week','does he spend jogging each week','He spends','jogging each week',randint(3,6),'P3CHM2a','conversion of hours and minutes'],
                        ['watches',' of TV each week','does he spend watching TV each week','He spends','watching TV each week',randint(2,5),'P3CHM2b','conversion of hours and minutes'],
                        ['spent',' practicing yoga last week','did he spend practicing yoga last week','He spent','practicing yoga last week',randint(4,8),'P3CHM2c','conversion of hours and minutes'],
                        ['swims for',' each week','does he spend swimming each week','He spends','swimming each week',randint(2,4),'P3CHM2d','conversion of hours and minutes'],
                        ['played outdoor for','','did he spend playing outdoor','He spent','playing outdoor',randint(3,6),'P3CHM2e','conversion of hours and minutes'],
                        ['practices maths for',' each week','does he practice maths each week','He practices maths for','each week',randint(5,10),'P3CHM2f','conversion of hours and minutes'],
                        ['has',' of music lessons each week','of music lessons does he have each week','He has','of music lessons each week',randint(2,5),'P3CHM2g','conversion of hours and minutes'],
                        ['has',' of English lessons each week','of English lessons does he have<br><br>each week','He has','of English lessons each week',randint(4,8),'P3CHM2h','conversion of hours and minutes'],
                        ['took',' to revise for the exam','did he take to revise for the exam','He took','to revise for the exam',randint(5,10),'P3CHM2i','conversion of hours and minutes'],
                        ['worked for',' on the computer','did he work on the computer for','He worked for','on the computer',randint(2,5),'P3CHM2j','conversion of hours and minutes']
                    ]
        self.item = random.choice(self.items)
        
        self.hour = self.item[5]
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %s %d hours%s.<br><br>"%(self.name,self.item[0],self.hour,self.item[1])
        self.problem = self.problem + "How many minutes %s?<br><br></div>"%(self.item[2])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[6]+".png' title='"+self.item[7]+"'></div>"
        
        self.answer = self.hour * 60
                   
        self.unit = "minutes"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.hour,self.item[3],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,hour,item3,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<br><table>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>We know,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>1 h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>60 min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>"+str(hour)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour)+" &times; 60 min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour*60)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item3+" <b>"+str(answer)+"</b> minutes "+item4+".</td></tr>"
        self.solution_text = self.solution_text+"</table>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        <It took> 138 minutes< to bake a cake>.
        How many hours and minutes did it take to bake the cake?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                        ['It took',' to bake a cake','How many hours and minutes did it take to bake the cake?','It took',' to bake the cake.',randint(1,2),'P3CHM8a','third grade time questions'],
                        ['It took us',' to pack our things','How many hours and minutes did it take us to pack our things?','It took us',' to pack our things.',randint(3,6),'P3CHM8b','third grade time questions'],
                        ['The magic show was',' long','How long was the magic show, in hours and minutes?','The magic show was','.',randint(2,3),'P3CHM8c','third grade time questions'],
                        ['It took',' to decorate the party hall','How many hours and minutes did it take to decorate the party hall?','It took',' to decorate the party hall.',randint(2,5),'P3CHM8d','third grade time questions'],
                        ['It took',' to stitch a dress','How many hours and minutes did it take to stitch the dress?','It took',' to stitch the dress.',randint(3,6),'P3CHM8e','third grade time questions'],
                        ['The phone call was',' long','How long was the phone call, in hours and minutes?','The phone call was','.',randint(1,2),'P3CHM8f','third grade time questions'],
                        ['It took her',' to prepare dinner','How many hours and minutes did it take her to prepare dinner?','It took her',' to prepare dinner.',randint(2,4),'P3CHM8g','third grade time questions'],
                        ['The alarm rang after','','After how many hours and minutes did the alarm ring?','The alarm rang after','.',randint(2,5),'P3CHM8h','third grade time questions'],
                        ['We were at the stadium for','','How long were we at the stadium, in hours and minutes?','We were at the stadium for','.',randint(2,4),'P3CHM8i','third grade time questions'],
                        ['She was at the mall for','','How long was she at the mall, in hours and minutes?','She was at the mall for','.',randint(3,6),'P3CHM8j','third grade time questions']
                    ]

        self.item = random.choice(self.items)
        
        self.hour = self.item[5]
        self.minutes = randint(1,59)
        self.TotalMinutes = self.hour*60+self.minutes
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %d minutes%s.<br>"%(self.item[0],self.TotalMinutes,self.item[1])
        self.problem = self.problem + self.item[2] + "<br><br>"
        self.problem = self.problem + "[Write your answer as below.<br>Example: 2 h 12 min]</div>"
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[6]+".png' title='"+self.item[7]+"'></div>"
        
        self.answer = "%d h %d min"%(self.hour,self.minutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.hour,self.minutes,self.item[3],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,hour,minutes,item3,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<br><table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str((hour*60)+minutes)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour*60)+" min + "+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour)+" h + "+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item3+" <b>"+str(answer)+"</b>"+item4+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        <The movie lasted> 2 h 18 min<>.
        How long was the movie in minutes?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                        ['The movie lasted','','How long was the movie, in minutes?','The movie was','minutes.',randint(1,2),'P3CHM5a','time questions grade 3'],
                        ['The concert was',' long','How long was the concert, in minutes?','The concert was','minutes.',randint(3,6),'P3CHM5b','time questions grade 3'],
                        ['We returned home after','','After how many minutes did we return home?','We returned home after','minutes.',randint(5,9),'P3CHM5c','time questions grade 3'],
                        ['The train ride was',' long','How long was the train ride, in minutes?','The train ride was','minutes.',randint(2,5),'P3CHM5d','time questions grade 3'],
                        ['The show lasted','','How long was the show, in minutes?','The show was','minutes.',randint(2,4),'P3CHM5e','time questions grade 3'],
                        ['The flight was',' long','How long was the flight, in minutes?','The flight was','minutes.',randint(4,8),'P3CHM5f','time questions grade 3'],
                        ['He finished the race in','','How many minutes did he take to finish the race?','He took','minutes to finish the race.',randint(1,2),'P3CHM5g','time questions grade 3'],
                        ['The car was parked in the carpark for','','How long was the car parked in the carpark, in minutes?','The car was parked in the carpark for','minutes.',randint(3,6),'P3CHM5h','time questions grade 3'],
                        ['The carpenter took',' to make a table','How many minutes did he take to make the table?','He took','minutes to make the table.',randint(6,9),'P3CHM5i','time questions grade 3'],
                        ['She was at the party for','','How long was she at the party, in minutes?','She was at the party for','minutes.',randint(2,4),'P3CHM5j','time questions grade 3']
                    ]

        self.item = random.choice(self.items)
        
        self.hour = self.item[5]
        self.minutes = randint(1,59)
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %d h %d min%s.<br><br>"%(self.item[0],self.hour,self.minutes,self.item[1])
        self.problem = self.problem + self.item[2] + "<br><br></div>"
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[6]+".png' title='"+self.item[7]+"'></div>"
        
        self.answer = self.hour * 60 + self.minutes
                   
        self.unit = "minutes"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.hour,self.minutes,self.item[3],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,hour,minutes,item3,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<br><table>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>We know,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>1 h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>60 min</td></tr>"
        if hour > 1:
            self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
            self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>"+str(hour)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour)+" &times; 60 min</td></tr>"
            self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour*60)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>Therefore,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>"+str(hour)+" h + "+str(minutes)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour*60)+" min + "+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item3+" <b>"+str(answer)+"</b> "+item4+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain


    def GenerateProblemType5(self):       
        '''e.g.:
        Give your answer in hours and minutes.
        95 min = ____ h ____ min
        [Write your answer as below.
        Example: 2 h 12 min ]'''

        self.complexity_level = "easy"
        self.HCScore = 3
               
        self.hour = randint(1,10)
        self.minutes = randint(1,59)
        self.problem = "Give your answer in hours and minutes.<br><br>"
        self.problem = self.problem + "%d min = ____ h ____ min<br><br>"%(self.hour*60+self.minutes)
        self.problem = self.problem + "[Write your answer as below.<br>Example: 2 h 12 min]"
        
        self.answer = "%d h %d min"%(self.hour,self.minutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.hour,self.minutes,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,hour,minutes,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<br><table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str((hour*60)+minutes)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour*60)+" min + "+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour)+" h + "+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>There are <b>"+str(answer)+"</b> in "+str((hour*60)+minutes)+" min.</td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        <The bus took> 2 hours< to reach Singapore>.
        How many minutes are there in 2 hours?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                        ['The bus took',random.choice([' to reach Singapore',' to reach New York City',' to reach London',' to reach home',' to reach the airport']),randint(2,5),'P3CHM3a','time sums primary 3'],
                        ['It rained for',random.choice([' yesterday',' on Monday',' last Saturday',' in the town',' in Mumbai']),randint(3,6),'P3CHM3b','time sums primary 3'],
                        ['The train was delayed by','',randint(4,8),'P3CHM3c','time sums primary 3'],
                        ['The shop opens for','',randint(6,9),'P3CHM3d','time sums primary 3'],
                        ['The gym opens for','',randint(6,9),'P3CHM3e','time sums primary 3'],
                        ['The cafe opens for','',randint(4,8),'P3CHM3f','time sums primary 3'],
                        ['The boat took',' to reach the island',randint(2,5),'P3CHM3g','time sums primary 3'],
                        ['The teacher taught for','',randint(2,4),'P3CHM3h','time sums primary 3'],
                        ['The library opens for','',randint(5,9),'P3CHM3i','time sums primary 3'],
                        ['The game lasted for','',randint(3,6),'P3CHM3j','time sums primary 3']
                    ]
        self.item = random.choice(self.items)
        
        self.hour = self.item[2]
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %d hours%s.<br><br>"%(self.item[0],self.hour,self.item[1])
        self.problem = self.problem + "How many minutes are there in %d hours?<br><br></div>"%(self.hour)
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[3]+".png' title='"+self.item[4]+"'></div>"
        
        self.answer = self.hour * 60
                   
        self.unit = "minutes"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.hour,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,hour,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<br><table>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>We know,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>1 h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>60 min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>"+str(hour)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour)+" &times; 60 min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour*60)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>There are <b>"+str(answer)+"</b> minutes in "+str(hour)+" hours.</td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        [Person.Girlname] <took> 125 minutes< to clean her room>.
        How many hours and minutes are there in 125 minutes?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['took',' to clean her room',randint(1,2),'P3CHM7a','third grade time problems'],
                        ['set a timer for','',randint(3,6),'P3CHM7b','third grade time problems'],
                        ['read a book in','',randint(5,9),'P3CHM7c','third grade time problems'],
                        ['was in the library for','',randint(2,5),'P3CHM7d','third grade time problems'],
                        ['took',' to do her homework',randint(2,4),'P3CHM7e','third grade time problems'],
                        ['spent',' gardening',randint(1,2),'P3CHM7f','third grade time problems'],
                        ['took',' to make a scrapbook',randint(4,8),'P3CHM7g','third grade time problems'],
                        ['cycled for','',randint(1,2),'P3CHM7h','third grade time problems'],
                        ['took',' to make a mosaic',randint(2,4),'P3CHM7i','third grade time problems'],
                        ['took',' to decorate a picture frame',randint(3,6),'P3CHM7j','third grade time problems']
                    ]

        self.item = random.choice(self.items)
        
        self.hour = self.item[2]
        self.minutes = randint(1,59)
        self.TotalMinutes = self.hour*60+self.minutes
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %s %d minutes%s.<br>"%(self.name,self.item[0],self.TotalMinutes,self.item[1])
        self.problem = self.problem + "How many hours and minutes are there in %d minutes?<br><br>"%(self.TotalMinutes)
        self.problem = self.problem + "[Write your answer as below.<br>Example: 2 h 12 min]</div>"
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[3]+".png' title='"+self.item[4]+"'></div>"
        
        self.answer = "%d h %d min"%(self.hour,self.minutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.hour,self.minutes,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,hour,minutes,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<br><table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str((hour*60)+minutes)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour*60)+" min + "+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour)+" h + "+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+answer+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>There are <b>"+str(answer)+"</b> in "+str((hour*60)+minutes)+" minutes.</td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def GenerateProblemType8(self):       
        '''e.g.:
        [Person.Girlname] <played the violin for> 1 h 30 min<>.
        Write this time in minutes.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['played the violin','',randint(1,2),'P3CHM4a','time sums grade 3'],
                        ['worked for','',randint(3,6),'P3CHM4b','time sums grade 3'],
                        ['took',' to make a painting',randint(5,9),'P3CHM4c','time sums grade 3'],
                        ['and her family were at the butterfly park for','',randint(2,4),'P3CHM4d','time sums grade 3'],
                        ['spent',' at the coin museum',randint(2,5),'P3CHM4e','time sums grade 3'],
                        ['traveled for',' to visit her grandmother',randint(4,8),'P3CHM4f','time sums grade 3'],
                        ['waited at the airport for','',randint(1,2),'P3CHM4g','time sums grade 3'],
                        ["played at her friend's house for",'',randint(3,6),'P3CHM4h','time sums grade 3'],
                        ['slept for','',randint(6,9),'P3CHM4i','time sums grade 3'],
                        ['took',' to write an essay',randint(2,4),'P3CHM4j','time sums grade 3']
                    ]

        self.item = random.choice(self.items)
        
        self.hour = self.item[2]
        self.minutes = random.randrange(5,55,5)
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %s %d h %d min%s.<br><br>"%(self.name,self.item[0],self.hour,self.minutes,self.item[1])
        self.problem = self.problem + "Write this time in minutes.<br><br></div>"
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[3]+".png' title='"+self.item[4]+"'></div>"
        
        self.answer = self.hour * 60 + self.minutes
                   
        self.unit = "minutes"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.hour,self.minutes,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,hour,minutes,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<br><table>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>We know,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>1 h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>60 min</td></tr>"
        if hour > 1:
            self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
            self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>"+str(hour)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour)+" &times; 60 min</td></tr>"
            self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour*60)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>Therefore,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>"+str(hour)+" h + "+str(minutes)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(hour*60)+" min + "+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text+"<tr><td>&nbsp;</td><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" min</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>There are <b>"+str(answer)+"</b> minutes in "+str(hour)+" h "+str(minutes)+" min.</td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False  
        elif CheckAnswer == 2:
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"")
                answer = string.join(str(answer).split(),"")
                return str(answer)==str(InputAnswer).lower()
            except ValueError:
                return False          
        elif CheckAnswer == 3:
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"")
                answer1 = answer.partition(".")[0]+":"+answer.partition(".")[2]
                return InputAnswer == answer or InputAnswer == answer1
            except ValueError:
                return False        