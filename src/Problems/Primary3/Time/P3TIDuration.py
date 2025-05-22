'''
Created on Jun 27, 2013
Module: P3TIDuration
Generates the Finding Starting Time and Finishing Time problems on Time for Primary 3

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

class P3TIDuration:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1a","ProblemType1b",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemType4",],
                            5:["ProblemType5a","ProblemType5b","ProblemType5c","ProblemType5d",],
                            6:["ProblemType6",],7:["ProblemType7",],8:["ProblemType8a","ProblemType8b",],
                            9:["ProblemType9",],10:["ProblemType10a","ProblemType10b",],11:["ProblemType11",],
                            12:["ProblemType12",],13:["ProblemType13a","ProblemType13b",],14:["ProblemType14",],
                            15:["ProblemType15",],16:["ProblemType16",]
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1a(),self.GenerateProblemType1b(),],2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],4:[self.GenerateProblemType4(),],
                                    5:[self.GenerateProblemType5a(),self.GenerateProblemType5b(),self.GenerateProblemType5c(),self.GenerateProblemType5d(),],
                                    6:[self.GenerateProblemType6(),],7:[self.GenerateProblemType7(),],
                                    8:[self.GenerateProblemType8a(),self.GenerateProblemType8b(),],
                                    9:[self.GenerateProblemType9(),],10:[self.GenerateProblemType10a(),self.GenerateProblemType10b(),],
                                    11:[self.GenerateProblemType11(),],12:[self.GenerateProblemType12(),],
                                    13:[self.GenerateProblemType13a(),self.GenerateProblemType13b(),],
                                    14:[self.GenerateProblemType14(),],15:[self.GenerateProblemType15(),],16:[self.GenerateProblemType16(),],                                   
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
        #return self.GenerateProblemType1a()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1a":self.GenerateProblemType1a(),"ProblemType1b":self.GenerateProblemType1b(),
                            "ProblemType2":self.GenerateProblemType2(),"ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5a":self.GenerateProblemType5a(),"ProblemType5b":self.GenerateProblemType5b(),
                            "ProblemType5c":self.GenerateProblemType5c(),"ProblemType5d":self.GenerateProblemType5d(),
                            "ProblemType6":self.GenerateProblemType6(),"ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8a":self.GenerateProblemType8a(),"ProblemType8b":self.GenerateProblemType8b(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10a":self.GenerateProblemType10a(),"ProblemType10b":self.GenerateProblemType10b(),
                            "ProblemType11":self.GenerateProblemType11(),"ProblemType12":self.GenerateProblemType12(),
                            "ProblemType13a":self.GenerateProblemType13a(),"ProblemType13b":self.GenerateProblemType13b(),
                            "ProblemType14":self.GenerateProblemType14(),"ProblemType15":self.GenerateProblemType15(),
                            "ProblemType16":self.GenerateProblemType16(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1a(self):       
        '''e.g.:
        What time is 2 hours after 6.30 p.m.?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.hour1 = randint(2,9)
        self.minutes = random.randrange(10,55,5)
        self.hour2 = randint(2,11-self.hour1)
        if self.hour2 > 5:
            self.hour2 = 10 - self.hour2
        self.AMPM = random.choice(["p.m.","a.m."])
        
        self.problem = "What time is %d hours after %d.%d %s?"%(self.hour2,self.hour1,self.minutes,self.AMPM)
        
        self.answer = "%d.%d %s"%(self.hour1+self.hour2,self.minutes,self.AMPM)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1a(self.problem,self.answer,self.hour1,self.hour2,self.minutes,self.AMPM,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1a(self,problem,answer,hour1,hour2,minutes,AMPM,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        self.solution_text = "<div class='side' style='width:130px;'>Count forwards.</div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hour1)+"."+str(minutes)+" "+str(AMPM)+"</td>"
        for i in range(self.hour2):
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hour1+i+1)+"."+str(minutes)+" "+str(AMPM)+"</td>"
        self.solution_text = self.solution_text+"</tr></table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType1b(self):       
        '''e.g.:
        What time is 4 hours before 3.15 p.m.?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.hour2 = randint(2,5)
        self.hour1 = randint(1,self.hour2-1)
        self.minutes = random.randrange(10,55,5)
        self.AMPM = "p.m."
        
        self.problem = "What time is %d hours before %d.%d %s?"%(self.hour2,self.hour1,self.minutes,self.AMPM)
        
        self.answer = "%d.%d %s"%(self.hour1+12-self.hour2,self.minutes,"a.m.")
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1b(self.problem,self.answer,self.hour1,self.hour2,self.minutes,self.AMPM,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1b(self,problem,answer,hour1,hour2,minutes,AMPM,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        hour1 = hour1 - hour2
        self.solution_text = "<div class='side' style='width:130px;'>Count backwards.</div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hour1+12)+"."+str(minutes)+" a.m.</td>"
        for i in range(self.hour2):
            if hour1+i+1 < 0:
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hour1+i+1+12)+"."+str(minutes)+" a.m.</td>"
            elif hour1+i+1 == 0:
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>12."+str(minutes)+" p.m.</td>"
            else:
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hour1+i+1)+"."+str(minutes)+" p.m.</td>"
        self.solution_text = self.solution_text+"</tr></table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        [Person.Name] <boarded a train> at 7.50 a.m. and <got off the train> at 9.50 a.m.
        How long <was his train journey>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                        ['boarded a train','got off the train','was his train journey',randint(2,9),'P3FDSFT2a','finding duration in hours and minutes primary 3','\'s train journey was',' long'],
                        ['boarded a bus','got off the bus','was his bus journey',randint(2,9),'P3FDSFT2b','finding duration in hours and minutes primary 3','\'s bus journey was',' long'],
                        ['entered the gym','came out of the gym','was he in the gym',randint(2,3),'P3FDSFT2c','finding duration in hours and minutes primary 3','was in the gym for',''],
                        ['entered the classroom','left the classroom','was he in the classroom',randint(2,4),'P3FDSFT2d','finding duration in hours and minutes primary 3','was in the classroom for',''],
                        ['arrived at school','left school at','was he in the school',randint(5,8),'P3FDSFT2e','finding duration in hours and minutes primary 3','was in the school for',''],
                        ['arrived at the playground','left the playground at','was he in the playground',randint(2,4),'P3FDSFT2f','finding duration in hours and minutes primary 3','was in the playground for',''],
                        ['left his home','returned home','was he away from home',randint(2,9),'P3FDSFT2g','finding duration in hours and minutes primary 3','was away from home for',''],
                        ['entered the library','left the library','was he in the library',randint(2,9),'P3FDSFT2h','finding duration in hours and minutes primary 3','was in the library for',''],
                        ['started cycling','finished cycling','did he cycle',randint(2,4),'P3FDSFT2i','finding duration in hours and minutes primary 3','cycled for',''],
                        ['started watching TV','finished watching TV','did he watch TV',randint(2,4),'P3FDSFT2j','finding duration in hours and minutes primary 3','watched TV for','']
                    ]
        
        self.item = random.choice(self.items)
        
        self.StartHour = randint(9,14)
        self.duration = self.item[3]
        self.EndHour = self.StartHour + self.duration
        self.minutes = random.randrange(10,55,5)        
        #This original start hour is required in explanation
        self.OriginalStartHour = self.StartHour
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."            

        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %s at %d.%d %s<br>"%(self.name,self.item[0],self.StartHour,self.minutes,self.AMPMStart)
        self.problem = self.problem + "He %s at %d.%d %s<br>"%(self.item[1],self.EndHour,self.minutes,self.AMPMEnd)
        self.problem = self.problem + "How long %s?</div>"%(self.item[2])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[4]+".png' title='"+self.item[5]+"'></div>"
        
        self.answer = self.duration
                   
        self.unit = "hours"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.minutes,self.duration,
                                              self.name,self.item[6],self.item[7])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,duration,name,text1,text2):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
                    1h                  1h
        7.50 a.m. ------>  8.50 a.m. ------>  9.50 a.m.
        
        His train journey was 2 hours.
        '''
        hours = self.Convert24HrsTo12Hrs(start_hour)
        self.solution_text = "<div class='side' style='width:130px;'>Count forwards.</div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        for i in range(duration):
            hours = self.Convert24HrsTo12Hrs(start_hour+i+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        self.solution_text = self.solution_text+"</tr></table>"
        self.solution_text = self.solution_text + "<br><b>%s %s %s %s%s.</b>"%(name,text1,answer,unit,text2)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        [Person.Girlname] <had some homework from school>.
        <She started doing her homework> at 2.35 p.m.
        <It took her> 2 h 10 min <to finish her homework>.
        At what time did <she finish her homework>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['had some homework from school','She started doing her homework','It took her','to finish her homework','she finish her homework',randint(8,17),random.randrange(65,155,5),'P3FDSFT3a','third grade time problem worksheets','finished her homework at'],
                        ['was going on a vacation','She started packing her bags','It took her','to pack her bags','she finish packing her bags',randint(8,17),random.randrange(65,155,5),'P3FDSFT3b','third grade time problem worksheets','finished packing her bags at'],
                        ['was wrapping return gifts for a party','She started wrapping the gifts','It took her','to wrap them','she finish wrapping them',randint(11,17),random.randrange(65,155,5),'P3FDSFT3c','third grade time problem worksheets','finished wrapping the gifts at'],
                        ['and her family were going to an amusement park','They started from their home','It took them','to reach the park','they arrive at the park',randint(8,11),random.randrange(65,115,5),'P3FDSFT3d','third grade time problem worksheets','and her family arrived at the park at'],
                        ['was stitching some cushion covers','She started stitching them','It took her','to stitch them','she finish stitching the cushion covers',randint(8,18),random.randrange(65,155,5),'P3FDSFT3e','third grade time problem worksheets','finished stitching the cushion covers at'],
                        ['received a phone call from her friend','Her friend called','They talked for','','she finish talking to her friend',randint(10,20),random.randrange(65,100,5),'P3FDSFT3f','third grade time problem worksheets','finished talking to her friends at'],
                        ['was helping her mother cook dinner','They started cooking','It took them','to cook the dinner','they finish cooking the dinner',randint(15,18),random.randrange(65,120,5),'P3FDSFT3g','third grade time problem worksheets','and her mother finished cooking at'],
                        ['and her friends went to a stadium to watch a game','They arrived at the stadium','They were at the stadium for','','they leave the stadium',randint(10,17),random.randrange(120,180,5),'P3FDSFT3h','third grade time problem worksheets','and her friends left the stadium at'],
                        ['went to a market with her mother','They arrived at the market','They were at the market for','','they leave the market',randint(10,18),random.randrange(65,120,5),'P3FDSFT3i','third grade time problem worksheets','and her mother left the market at'],
                        ['went to an excursion from school','They left for the excursion','They returned after','','they return',randint(10,14),random.randrange(180,240,5),'P3FDSFT3j','third grade time problem worksheets','and her classmates returned at']
                    ]        
        self.item = random.choice(self.items)
        
        self.StartHour = self.item[5]
        self.duration = self.item[6]
        if self.duration%60 == 0:
            self.duration = self.duration + 5
        self.DurationHour, self.DurationMinutes = divmod(self.duration,60)
        self.StartMinutes = random.randrange(10,55,5)
        self.EndMinutes = self.StartMinutes + self.DurationMinutes
        div,mod = divmod(self.EndMinutes,60)
        self.EndMinutes = mod
        self.EndHour = self.StartHour + div + self.DurationHour
        #This original start hour is required in explanation
        self.OriginalStartHour = self.StartHour
                
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."            
        
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %s.<br>"%(self.name,self.item[0])
        self.problem = self.problem + "%s at %d.%d %s<br>"%(self.item[1],self.StartHour,self.StartMinutes,self.AMPMStart)
        self.problem = self.problem + "%s %d h %d min %s.<br>"%(self.item[2],self.DurationHour,self.DurationMinutes,self.item[3])
        self.problem = self.problem + "At what time did %s?</div>"%(self.item[4])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[7]+".png' title='"+self.item[8]+"'></div>"
        
        if self.EndMinutes < 10:
            self.answer = "%d.0%d %s"%(self.EndHour,self.EndMinutes,self.AMPMEnd)
        else:
            self.answer = "%d.%d %s"%(self.EndHour,self.EndMinutes,self.AMPMEnd)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.StartMinutes,self.DurationHour,
                                              self.DurationMinutes,self.EndHour,self.AMPMEnd,self.name,self.item[9])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,duration_hour,duration_minutes,end_hour,ampm_end,name,text1):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
                    1h                  1h
        if 4.35 changes to the next hour when adding minutes:
        1h                  1h        25min         10 min
        2.35 p.m. ------>  3.35 p.m. ------>  4.35 p.m. ---->  5.00 p.m. -----> 5.10 p.m.
        
        else:
                1h                  1h        10min
        2.35 p.m. ------>  3.35 p.m. ------>  4.35 p.m. ---->  4.45 p.m.'''
        hours = self.Convert24HrsTo12Hrs(start_hour)
        self.solution_text = "<div class='side' style='width:130px;'>Count forwards.</div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        for i in range(duration_hour):
            hours = self.Convert24HrsTo12Hrs(start_hour+i+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        if start_minutes+duration_minutes<=60:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(answer)+"</td>"
        else:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(60-start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+".00 "+str(ampm_end)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(start_minutes+duration_minutes-60)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(answer)+"</td>"
        self.solution_text = self.solution_text+"</tr></table>"
        self.solution_text = self.solution_text + "<br><b>%s %s %s.</b>"%(name,text1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        <The singing lesson ended at> 3.45 p.m.
        <The lesson lasted> 1 h 35 min.
        <When did the lesson begin?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['The singing lesson ended at','The lesson lasted','When did the lesson begin?',randint(10,18),random.randrange(65,115,5),'P3FDSFT4a','third grade maths questions','The lesson began at'],
                        ['It stopped raining at','It rained for','When did it start raining?',randint(0,23),random.randrange(65,295,5),'P3FDSFT4b','third grade maths questions','It started raining at'],
                        ['The movie ended at','It lasted','When did it start?',randint(10,22),random.randrange(95,175,10),'P3FDSFT4c','third grade maths questions','The movie started at'],
                        ['The parade ended at','It lasted','When did it begin?',randint(10,18),random.randrange(125,245,15),'P3FDSFT4d','third grade maths questions','The parade started at'],
                        ['The air show ended at','It lasted','When did it begin?',randint(10,18),random.randrange(65,125,10),'P3FDSFT4e','third grade maths questions','The airshow began at'],
                        ['The drama ended at','It lasted','When did it begin?',randint(10,18),random.randrange(65,115,5),'P3FDSFT4f','third grade maths questions','The drama began at'],
                        ['It stopped snowing at','It snowed for','When did it start snowing?',randint(0,23),random.randrange(65,295,5),'P3FDSFT4g','third grade maths questions','It started snowing at'],
                        ['The show ended at','It lasted','When did it begin?',randint(10,20),random.randrange(65,125,10),'P3FDSFT4h','third grade maths questions','The show began at'],
                        ['The pharmacy closed at','It was open for','When did it open?',randint(10,12),random.randrange(390,630,60),'P3FDSFT4i','third grade maths questions','The pharmacy opened at'],
                        ['The bookstore closed at','It was open for','When did it open?',randint(10,12),random.randrange(315,615,60),'P3FDSFT4j','third grade maths questions','The bookstore opened at']
                    ]        
        self.item = random.choice(self.items)
        
        self.StartHour = self.item[3]
        self.duration = self.item[4]
        if self.duration%60 == 0:
            self.duration = self.duration + 5
        self.DurationHour, self.DurationMinutes = divmod(self.duration,60)
        self.StartMinutes = random.randrange(10,55,5)
        self.EndMinutes = self.StartMinutes + self.DurationMinutes
        div,mod = divmod(self.EndMinutes,60)
        self.EndMinutes = mod
        self.EndHour = self.StartHour + div + self.DurationHour
        #This original start hour is required in explanation
        self.OriginalStartHour = self.StartHour
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."
            
        self.EndMinutes = str(self.EndMinutes)
        if len(self.EndMinutes)==1:
            self.EndMinutes = '0'+self.EndMinutes       
        
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %d.%s %s<br>"%(self.item[0],self.EndHour,self.EndMinutes,self.AMPMEnd)
        self.problem = self.problem + "%s %d h %d min.<br>%s</div>"%(self.item[1],self.DurationHour,self.DurationMinutes,self.item[2])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[5]+".png' title='"+self.item[6]+"'></div>"
        
        self.answer = "%d.%d %s"%(self.StartHour,self.StartMinutes,self.AMPMStart)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.StartMinutes,self.DurationHour,
                                              self.DurationMinutes,self.EndHour,self.EndMinutes,self.AMPMEnd,self.item[7])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,duration_hour,duration_minutes,end_hour,end_minutes,ampm_end,text1):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
        if 2.45 changes to the previous hour when subtracting minutes:
                   10 min          45min         1h
        1.50 p.m. <------  2.00 p.m. <-----  2.45 p.m. <----- 3.45 p.m.
        
        else:
               35 min            1h
        2.10 p.m.  <-----  2.45 p.m.  <----  3.45 p.m.
        
        The lesson began at 2.10 p.m.'''
        hours = self.Convert24HrsTo12Hrs(start_hour)
        self.solution_text = "<div class='side' style='width:130px;'>Count backwards.</div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        if start_minutes+duration_minutes<60:
            start_hour = start_hour
            hours = self.Convert24HrsTo12Hrs(start_hour)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        elif start_minutes+duration_minutes==60:
            start_hour = start_hour + 1
            hours = self.Convert24HrsTo12Hrs(start_hour)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        else:
            start_hour = start_hour + 1
            hours = self.Convert24HrsTo12Hrs(start_hour)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(60-start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(duration_minutes+start_minutes-60)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        start_hour = start_hour + 1
        for i in range(duration_hour):
            hours = self.Convert24HrsTo12Hrs(start_hour+i)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        self.solution_text = self.solution_text+"</tr></table>"
        self.solution_text = self.solution_text + "<br><b>%s %s</b>"%(text1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5a(self):       
        '''e.g.:
        How many hours are there from 8.15 a.m. to 11.15 a.m.?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.hour1 = randint(1,9)
        self.minutes = random.randrange(0,55,5)
        self.hour2 = randint(self.hour1+2,11)
        self.AMPM = random.choice(["p.m.","a.m."])
        
        self.minutes = str(self.minutes)
        if len(self.minutes)==1:
            self.minutes = '0'+self.minutes
        
        self.problem = "How many hours are there from %d.%s %s to %d.%s %s?"%(self.hour1,self.minutes,self.AMPM,self.hour2,self.minutes,self.AMPM)
        
        self.answer = self.hour2 - self.hour1
                   
        if self.answer == 1:
            self.unit = "hour"
        else:
            self.unit = "hours"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5a(self.problem,self.answer,self.unit,self.dollar_unit,self.hour1,self.minutes,self.hour2,(self.hour2-self.hour1),self.AMPM)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5a(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,end_hour,duration,ampm):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
                    1h                  1h
        7.50 a.m. ------>  8.50 a.m. ------>  9.50 a.m.
        '''
        self.solution_text = "<div class='side' style='width:130px;'>Count forwards.</div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(start_hour)+"."+str(start_minutes)+" "+str(ampm)+"</td>"
        for i in range(duration):
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(start_hour+i+1)+"."+str(start_minutes)+" "+str(ampm)+"</td>"
        self.solution_text = self.solution_text+"</tr></table>"
        self.solution_text = self.solution_text + "<br><b>There are %s hours from %d.%s %s to %d.%s %s</b>"%(answer,start_hour,start_minutes,ampm,
                                                                                                             end_hour,start_minutes,ampm)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5b(self):       
        '''e.g.:
        How many hours are there from 8.45 a.m. to 1.45 p.m.?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.hour1 = randint(1,11)
        self.minutes = random.randrange(0,55,5)
        self.hour2 = randint(1,11)
        
        self.minutes = str(self.minutes)
        if len(self.minutes)==1:
            self.minutes = '0'+self.minutes
        
        self.problem = "How many hours are there from %d.%s %s to %d.%s %s?"%(self.hour1,self.minutes,"a.m.",self.hour2,self.minutes,"p.m.")
        
        self.answer = self.hour2 - self.hour1 + 12
                   
        self.unit = "hours"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5b(self.problem,self.answer,self.unit,self.dollar_unit,self.hour1,self.minutes,self.hour2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5b(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,end_hour):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
                    1h                  1h
        7.50 a.m. ------>  8.50 a.m. ------>  9.50 a.m.
        '''
        self.solution_text = "<div class='side' style='width:130px;'>Count forwards.</div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(start_hour)+"."+str(start_minutes)+" am</td>"
        self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(12-start_hour)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(12)+"."+str(start_minutes)+" pm</td>"
        self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(start_hour)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+"."+str(start_minutes)+" pm</td>"
        self.solution_text = self.solution_text+"</tr></table>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(12-start_hour)+" h + "+str(end_hour)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'><b>"+str(answer)+" hours</b></td></tr>"
        self.solution_text = self.solution_text+"</table>"
        
        self.solution_text = self.solution_text + "<br><b>There are %d hours from %d.%s am to %d.%s pm</b>"%(answer,start_hour,start_minutes,
                                                                                                             end_hour,start_minutes)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5c(self):       
        '''e.g.:
        How many hours are there from 8.00 p.m. to 1.00 a.m. on the next day?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.hour1 = randint(1,11)
        self.minutes = random.randrange(0,55,5)
        self.hour2 = randint(1,11)
        
        self.minutes = str(self.minutes)
        if len(self.minutes)==1:
            self.minutes = '0'+self.minutes
        
        self.problem = "How many hours are there from %d.%s %s to %d.%s %s on the next day?"%(self.hour1,self.minutes,"p.m.",self.hour2,self.minutes,"a.m.")
        
        self.answer = self.hour2 - self.hour1 + 12
                   
        self.unit = "hours"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5c(self.problem,self.answer,self.unit,self.dollar_unit,self.hour1,self.minutes,self.hour2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5c",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5c(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,end_hour):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
                    1h                  1h
        7.50 a.m. ------>  8.50 a.m. ------>  9.50 a.m.
        '''
        self.solution_text = "<div class='side' style='width:130px;'>Count forwards.</div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(start_hour)+"."+str(start_minutes)+" pm</td>"
        self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(12-start_hour)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(12)+"."+str(start_minutes)+" am</td>"
        self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(start_hour)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+"."+str(start_minutes)+" am</td>"
        self.solution_text = self.solution_text+"</tr></table>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(12-start_hour)+" h + "+str(end_hour)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'><b>"+str(answer)+" hours</b></td></tr>"
        self.solution_text = self.solution_text+"</table>"
        
        self.solution_text = self.solution_text + "<br><b>There are %d hours from %d.%s pm to %d.%s am on the next day.</b>"%(answer,start_hour,start_minutes,
                                                                                                             end_hour,start_minutes)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5d(self):       
        '''e.g.:
        How many hours are there from midnight to 5.00 a.m.?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.minutes = '00'
        self.hour1 = randint(2,11)
        self.AMPM = random.choice([['midnight','a.m.'],['noon','p.m.']])
               
        self.problem = "How many hours are there from %s to %d.%s %s?"%(self.AMPM[0],self.hour1,self.minutes,self.AMPM[1])
        
        self.answer = self.hour1
                   
        self.unit = "hours"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5d(self.problem,self.answer,self.unit,self.dollar_unit,self.AMPM[0],self.AMPM[1],self.hour1)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5d",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5d(self,problem,answer,unit,dollar_unit,ampm1,ampm2,end_hour):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
                    1h                  1h
        7.50 a.m. ------>  8.50 a.m. ------>  9.50 a.m.
        '''
        self.solution_text = "<div class='side' style='width:140px;'>%s : 12.00 %s</div>"%(ampm1.capitalize(),ampm2)
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>12.00 "+ampm2+"</td>"
        self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(end_hour)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+".00 "+ampm2+"</td>"
        self.solution_text = self.solution_text+"</tr></table>"
        
        self.solution_text = self.solution_text + "<br><b>There are %d hours from %s to %d.00 %s.</b>"%(answer,ampm1,end_hour,ampm2)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        <The craft lesson began> at 9.25 a.m. and <ended> at 10.10 a.m.
        How long <was the craft lesson>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['The craft lesson began','ended','was the craft lesson',randint(8,17),random.randrange(30,55,5),'P3FDSFT6a','grade 3 time problems','The craft lesson was'],
                        ['The magic show began','ended','was the magic show',randint(10,19),random.randrange(30,55,5),'P3FDSFT6b','grade 3 time problems','The magic show was'],
                        ['The exam began','ended','was the exam',randint(8,17),random.randrange(30,55,5),'P3FDSFT6c','grade 3 time problems','The exam was'],
                        ['The physical training started','finished','was the training',randint(8,17),random.randrange(30,55,5),'P3FDSFT6d','grade 3 time problems','The physical training was'],
                        ['The game started','finished','was the game',randint(11,20),random.randrange(30,55,5),'P3FDSFT6e','grade 3 time problems','The game was'],
                        ['The cartoon show began','ended','was the cartoon show',randint(10,19),random.randrange(15,30,5),'P3FDSFT6f','grade 3 time problems','The cartoon show was'],
                        ['The boy started his lunch','ended','did he spend on lunch',randint(11,14),random.randrange(20,40,5),'P3FDSFT6g','grade 3 time problems','His lunch was'],
                        ['The plane took off','landed','was the flight',randint(8,17),random.randrange(40,55,5),'P3FDSFT6h','grade 3 time problems','The flight was'],
                        ["The principal's speech began",'ended','was the speech',randint(8,17),random.randrange(20,45,5),'P3FDSFT6i','grade 3 time problems','The speech was'],
                        ['The interview began','ended','was the interview',randint(10,17),random.randrange(30,55,5),'P3FDSFT6j','grade 3 time problems','The interview was']
                    ]
        
        self.item = random.choice(self.items)
        
        self.StartHour = self.item[3]
        self.StartMinutes = random.randrange(10,55,5)
        self.duration = self.item[4]
        self.EndMinutes = self.StartMinutes + self.duration
        
        self.EndHour,self.EndMinutes = divmod(self.EndMinutes,60)
        self.EndHour = self.EndHour + self.StartHour        
        #for explanation
        self.OriginalStartHour = self.StartHour
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."            
        
        self.EndMinutes = str(self.EndMinutes)        
        if len(self.EndMinutes)==1:
            self.EndMinutes = '0'+self.EndMinutes
            
        self.problem = "%s at %d.%d %s and %s at %d.%s %s<br>"%(self.item[0],self.StartHour,self.StartMinutes,self.AMPMStart,
                                                                                                                      self.item[1],self.EndHour,self.EndMinutes,self.AMPMEnd)
        self.problem = self.problem + "<div style='display:inline-block;vertical-align:top;'>How long %s?<br>[Give your answer in minutes.]</div>"%(self.item[2])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[5]+".png' title='"+self.item[6]+"'></div>"
        
        self.answer = self.duration
                   
        self.unit = "minutes"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.StartMinutes,
                                              self.duration,self.EndMinutes,self.item[7])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}


    def ExplainType6(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,duration,end_minutes,text1):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
                    1h                  1h
        7.50 a.m. ------>  8.50 a.m. ------>  9.50 a.m.
        
        His train journey was 2 hours.
        '''
        hours = self.Convert24HrsTo12Hrs(start_hour)
        self.solution_text = "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        if start_minutes+duration>60:
            hours = self.Convert24HrsTo12Hrs(start_hour+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(60-start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration-60+start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        elif start_minutes+duration==60:
            hours = self.Convert24HrsTo12Hrs(start_hour+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        else:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"            
        self.solution_text = self.solution_text+"</tr></table><br>"

        if start_minutes+duration>60:
            self.solution_text = self.solution_text+"<table border=0>"
            self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(60-start_minutes)+" min + "+str(duration-60+start_minutes)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" min</td></tr>"
            self.solution_text = self.solution_text+"</table><br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text + "<tr><td>%s <b>%s %s</b> long."%(text1,answer,unit)+"</td></tr></table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        [Person.Girlname] <had a yoga lesson.>
        <It finished at> 2 p.m.
        <It lasted> 1 h 20 min<>.
        <When did it begin?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['had a yoga lesson.','It finished at','It lasted','','When did it begin?',randint(10,20),random.randrange(65,115,5),'P3FDSFT7a','primary 3 Singapore Maths','The yoga lesson began at'],
                        ['made a drawing.','She finished making it at','It took her',' to make it','When did she start making it?',randint(10,20),random.randrange(65,175,10),'P3FDSFT7b','primary 3 Singapore Maths','She started drawing at'],
                        ['wrote a blog post.','She finished writing it at','It took her',' to write it','When did she start writing it?',randint(10,20),random.randrange(65,115,5),'P3FDSFT7c','primary 3 Singapore Maths','She started writing blog at'],
                        ['wrote a composition.','She finished writing it at','It took her',' to write it','When did she start writing it?',randint(10,20),random.randrange(65,185,15),'P3FDSFT7d','primary 3 Singapore Maths','She started writing composition at'],
                        ['and her family visited a national park.','They left the park at','They were at the park for','','When did they arrive at the park?',randint(15,18),random.randrange(185,305,15),'P3FDSFT7e','primary 3 Singapore Maths','They arrived at the national park at'],
                        ['went skiing.','She finished skiing at','She skied for','','When did she begin skiing?',randint(14,16),random.randrange(125,295,10),'P3FDSFT7f','primary 3 Singapore Maths','She began skiing at'],
                        ['revised for a maths test.','She finished her revision at','She revised for','','When did she begin her revision?',randint(14,20),random.randrange(150,330,60),'P3FDSFT7g','primary 3 Singapore Maths','She began her revision at'],
                        ['went skating in a park.','She finished skating at','She skated for','','When did she begin skating?',randint(11,15),random.randrange(65,115,5),'P3FDSFT7h','primary 3 Singapore Maths','She began skating at'],
                        ['went to a cafe.','She left the cafe at','She was at the cafe for','','When did she arrive at the cafe?',randint(10,20),random.randrange(65,115,5),'P3FDSFT7i','primary 3 Singapore Maths','She arrived at the cafe at'],
                        ['went to the supermarket with her mother.','They left the supermarket at','They were at the supermarket for','','When did they arrive at the supermarket?',randint(12,20),random.randrange(65,175,10),'P3FDSFT7j','primary 3 Singapore Maths','The arrived at the supermarket at']
                    ]        
        self.item = random.choice(self.items)
        
        self.EndHour = self.item[5]
        self.duration = self.item[6]
        if self.duration%60 == 0:
            self.duration = self.duration + 5
        self.StartHour, self.StartMinutes = divmod(self.EndHour*60-self.duration,60)
        if self.StartMinutes == 0:
            self.duration = self.duration + 5
            self.StartMinutes = 5
        self.DurationHour, self.DurationMinutes = divmod(self.duration,60)
        self.OriginalStartHour = self.StartHour
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."     
        
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %s<br>"%(self.name,self.item[0])
        self.problem = self.problem + "%s %d %s<br>"%(self.item[1],self.EndHour,self.AMPMEnd)
        self.problem = self.problem + "%s %d h %d min%s.<br>%s</div>"%(self.item[2],self.DurationHour,self.DurationMinutes,self.item[3],self.item[4])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[7]+".png' title='"+self.item[8]+"'></div>"
        
        self.StartMinutes = str(self.StartMinutes)
        if len(self.StartMinutes)==1:
            self.StartMinutes = '0'+self.StartMinutes
            
        self.answer = "%d.%s %s"%(self.StartHour,self.StartMinutes,self.AMPMStart)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.StartMinutes,self.DurationHour,
                                              self.DurationMinutes,self.EndHour,"00",self.AMPMEnd,self.item[9])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}


    def ExplainType7(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,duration_hour,duration_minutes,end_hour,end_minutes,ampm_end,text1):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
        if 2.45 changes to the previous hour when subtracting minutes:
                   10 min          45min         1h
        1.50 p.m. <------  2.00 p.m. <-----  2.45 p.m. <----- 3.45 p.m.
        
        else:
               35 min            1h
        2.10 p.m.  <-----  2.45 p.m.  <----  3.45 p.m.
        
        The lesson began at 2.10 p.m.'''
        start_minutes = int(start_minutes)
        hours = self.Convert24HrsTo12Hrs(start_hour)
        self.solution_text = "<div class='side' style='width:130px;'>Count backwards.</div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        if start_minutes+duration_minutes<60:
            start_hour = start_hour
            hours = self.Convert24HrsTo12Hrs(start_hour)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        elif start_minutes+duration_minutes==60:
            start_hour = start_hour + 1
            hours = self.Convert24HrsTo12Hrs(start_hour)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        else:
            start_hour = start_hour + 1
            hours = self.Convert24HrsTo12Hrs(start_hour)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(60-start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(duration_minutes+start_minutes-60)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        start_hour = start_hour + 1
        for i in range(duration_hour):
            hours = self.Convert24HrsTo12Hrs(start_hour+i)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        self.solution_text = self.solution_text+"</tr></table><br>"

        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text + "<tr><td>%s <b>%s</b>"%(text1,answer)+"</td></tr></table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8a(self):       
        '''e.g.:
        [Person.Auntyname] took 3 hours <to mark her pupils' exam papers>.
        She <started> at 8.40 a.m.
        When did <she finish>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [
                        ["to mark her pupils' exam papers",'started','she finish',randint(2,4),randint(8,17),'P3FDSFT8a','third grade time homework help','finished marking her pupils\' exam paper at'],
                        ['to do the laundry','started','she finish',randint(2,4),randint(8,17),'P3FDSFT8b','third grade time homework help','finished doing the laundry at'],
                        ['to read a book','started','she finish',randint(2,4),randint(8,19),'P3FDSFT8c','third grade time homework help','finished reading the book at'],
                        ['to sew the curtains','started','she finish',randint(4,6),randint(8,14),'P3FDSFT8d','third grade time homework help','finished sewing the curtains at'],
                        ['to do household chores','started','she finish',randint(2,5),randint(8,12),'P3FDSFT8e','third grade time homework help','finished doing household chores at']
                    ]
        
        self.item = random.choice(self.items)
        
        self.StartHour = self.item[4]
        self.StartMinutes = random.randrange(10,55,5)
        self.duration = self.item[3]
        self.EndMinutes = self.StartMinutes
        self.EndHour = self.StartHour + self.duration
        #for explanation
        self.OriginalStartHour = self.StartHour
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."            
            
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s took %d hours %s.<br><br>"%(self.name,self.duration,self.item[0])
        self.problem = self.problem + "She %s at %d.%d %s<br><br>"%(self.item[1],self.StartHour,self.StartMinutes,self.AMPMStart)
        self.problem = self.problem + "When did %s?</div>"%(self.item[2])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[5]+".png' title='"+self.item[6]+"'></div>"
        
        self.answer = "%d.%d %s"%(self.EndHour,self.EndMinutes,self.AMPMEnd)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8a(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.StartMinutes,
                                               self.duration,self.name,self.item[7])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8a(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,duration,name,text1):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
                    1h                  1h
        7.50 a.m. ------>  8.50 a.m. ------>  9.50 a.m.
        '''
        self.solution_text = "<div class='side' style='width:130px;'>Count forwards.</div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        hours = self.Convert24HrsTo12Hrs(start_hour)
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        for i in range(duration):
            hours = self.Convert24HrsTo12Hrs(start_hour+i+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        self.solution_text = self.solution_text+"</tr></table><br>"
       
        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td>%s %s <b>%s</b></td></tr></table>"%(name,text1,answer)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8b(self):       
        '''e.g.:
        [Person.Unclename] took 6 hours <to do his office work>.
        He <started> at 8.40 a.m.
        When did <he finish>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [
                        ['to do his office work','started','he finish',randint(6,10),randint(8,10),'P3FDSFT8f','third grade time homework help','finished his office work at'],
                        ['to prepare his presentation','started','he finish',randint(2,5),randint(11,14),'P3FDSFT8g','third grade time homework help','finished preparing his presentation at'],
                        ['to drive from Town A to Town B','started from Town A','he reach Town B',randint(2,8),randint(11,15),'P3FDSFT8h','third grade time homework help','reached Town B at'],
                        ['to paint a house','started','he finish',randint(3,7),randint(10,14),'P3FDSFT8i','third grade time homework help','finished painting the house at'],
                        ['to repair his computer','started','he finish',randint(3,7),randint(10,14),'P3FDSFT8j','third grade time homework help','finished repairing the computer at']
                    ]
        
        self.item = random.choice(self.items)
        
        self.StartHour = self.item[4]
        self.StartMinutes = random.randrange(10,55,5)
        self.duration = self.item[3]
        self.EndMinutes = self.StartMinutes
        self.EndHour = self.StartHour + self.duration
        # for explanation
        self.OriginalStartHour = self.StartHour
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."            
            
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s took %d hours %s.<br><br>"%(self.name,self.duration,self.item[0])
        self.problem = self.problem + "He %s at %d.%d %s<br><br>"%(self.item[1],self.StartHour,self.StartMinutes,self.AMPMStart)
        self.problem = self.problem + "When did %s?</div>"%(self.item[2])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[5]+".png' title='"+self.item[6]+"'></div>"
        
        self.answer = "%d.%d %s"%(self.EndHour,self.EndMinutes,self.AMPMEnd)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8b(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.StartMinutes,self.EndHour,
                                               self.duration,self.name,self.item[7])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8b(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,end_hour,duration,name,text1):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
                    1h                  1h
        7.50 a.m. ------>  8.50 a.m. ------>  9.50 a.m.
        '''
        self.solution_text = "<div class='side' style='width:130px;'>Count forwards.</div>"
        if start_hour >=12:
            self.solution_text = self.solution_text + "<table border=0><tr>"
            hours = self.Convert24HrsTo12Hrs(start_hour)
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
            for i in range(duration):
                hours = self.Convert24HrsTo12Hrs(start_hour+i+1)
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text+"</tr></table><br>"
        else:
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(start_hour)+"."+str(start_minutes)+" am</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(12-start_hour)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(12)+"."+str(start_minutes)+" pm</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(end_hour)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+"."+str(start_minutes)+" pm</td>"
            self.solution_text = self.solution_text+"</tr></table><br>"
        
        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td>%s %s <b>%s</b></td></tr></table>"%(name,text1,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        <The movie started> at 6.30 p.m. and <ended> at 8.15 p.m.
        How long <was the movie>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                        ['The play started','ended','was the play',randint(8,17),random.randrange(65,120,5),'P3FDSFT9a','grade 3 time worksheets','The play was',' long.'],
                        ['The concert began','finished','was the concert',randint(15,21),random.randrange(90,180,10),'P3FDSFT9b','grade 3 time worksheets','The concert was',' long.'],
                        ['The shop opened','closed','was the shop open',randint(8,12),random.randrange(300,600,10),'P3FDSFT9c','grade 3 time worksheets','The shop was open for','.'],
                        ['The baby slept','woke up','was the baby asleep',randint(8,17),random.randrange(90,150,5),'P3FDSFT9d','grade 3 time worksheets','The baby was asleep for','.'],
                        ['The tennis match began','ended','was the tennis match',randint(8,17),random.randrange(90,150,5),'P3FDSFT9e','grade 3 time worksheets','The tennis match was',' long.'],
                        ['The party started','finished','was the party',randint(12,17),random.randrange(90,180,15),'P3FDSFT9f','grade 3 time worksheets','The party was',' long.'],
                        ['The food fest started','ended','was the food fest',randint(8,17),random.randrange(90,240,15),'P3FDSFT9g','grade 3 time worksheets','The food fest was',' long.'],
                        ['The chef started cooking','finished cooking','did the chef take to cook',randint(8,17),random.randrange(90,210,10),'P3FDSFT9h','grade 3 time worksheets','The chef took',' to cook.'],
                        ['The artist began painting','finished','did the artist spend on painting',randint(8,17),random.randrange(90,210,10),'P3FDSFT9i','grade 3 time worksheets','The artist spent','on the painting.'],
                        ['It started raining','stopped raining','did it rain',randint(6,17),random.randrange(65,145,5),'P3FDSFT9j','grade 3 time worksheets','It rained for','.']
                    ]
        
        self.item = random.choice(self.items)
        
        self.StartHour = self.item[3]
        self.StartMinutes = random.randrange(10,55,5)
        self.duration = self.item[4]
        self.DurationHour,self.DurationMinutes = divmod(self.duration,60)
        
        self.EndMinutes = self.StartMinutes + self.DurationMinutes 
        self.EndHour, self.EndMinutes = divmod(self.EndMinutes,60)
        self.EndHour = self.StartHour + self.EndHour + self.DurationHour
        #for explanation
        self.OriginalStartHour = self.StartHour
        
        if len(str(self.EndMinutes))==1:
            self.EndMinutes = '0'+str(self.EndMinutes)
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."
            
        self.problem = "%s at %d.%d %s and %s at %d.%s %s<br><br>"%(self.item[0],self.StartHour,self.StartMinutes,self.AMPMStart,self.item[1],
                                                                    self.EndHour,self.EndMinutes,self.AMPMEnd)
        self.problem = self.problem + "<div style='display:inline-block;vertical-align:top;'>How long %s?<br><br>"%(self.item[2])
        self.problem = self.problem + "[Write your answer as in example below:<br> 1 h 25 min]</div>"
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[5]+".png' title='"+self.item[6]+"'></div>"
        
        self.answer = "%d h %d min"%(self.DurationHour,self.DurationMinutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.StartMinutes,
                                              self.EndHour,self.EndMinutes,self.AMPMEnd,self.DurationHour,self.DurationMinutes,self.item[7],self.item[8])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,end_hour,end_minutes,end_ampm,duration_hour,duration_minutes,text1,text2):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
                    1h                  1h
        7.50 a.m. ------>  8.50 a.m. ------>  9.50 a.m.
        '''
        self.solution_text = "<div class='side' style='width:130px;'>Count forwards.</div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        hours = self.Convert24HrsTo12Hrs(start_hour)
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        for i in range(duration_hour):
            hours = self.Convert24HrsTo12Hrs(start_hour+i+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        if start_minutes+duration_minutes<=60:
            if duration_minutes > 0:
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+"."+str(end_minutes)+" "+str(end_ampm)+"</td>"
        else:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(60-start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+".00 "+str(end_ampm)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes+start_minutes-60)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+"."+str(end_minutes)+" "+str(end_ampm)+"</td>"
        self.solution_text = self.solution_text+"</tr></table><br>"
        
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
        if start_minutes+duration_minutes<=60:
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(duration_hour)+" h + "+str(duration_minutes)+" min </td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" </td></tr>"
        else:
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(duration_hour)+" h + "+str(60-start_minutes)+" min + "+str(duration_minutes+start_minutes-60)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" </td></tr>"
        self.solution_text = self.solution_text+"</table><br>"


        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td>%s <b>%s</b>%s</td></tr></table>"%(text1,answer,text2)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10a(self):       
        '''e.g.:
        What time is 45 minutes after 11.45 a.m.?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.minutes = random.choice([[45,random.randrange(15,55,5)],[30,random.randrange(30,55,5)],[15,random.randrange(45,55,5)]])
        self.hour = 11
        
        self.problem = "What time is %d minutes after %d.%d a.m.?"%(self.minutes[0],self.hour,self.minutes[1])
        
        self.EndMinutes = self.minutes[0]+self.minutes[1]
        self.EndHour,self.EndMinutes = divmod(self.EndMinutes,60)        
        self.EndHour = self.hour + self.EndHour
                
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
        
        self.EndMinutes = str(self.EndMinutes)
        
        if len(self.EndMinutes)==1:
            self.EndMinutes = '0'+self.EndMinutes
                        
        self.answer = "%d.%s p.m."%(self.EndHour,self.EndMinutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10a(self.problem,self.answer,self.unit,self.dollar_unit,self.minutes[1],self.minutes[0])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10a(self,problem,answer,unit,dollar_unit,start_minutes,duration):
        
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
                    1h                  1h
        7.50 a.m. ------>  8.50 a.m. ------>  9.50 a.m.
        '''
        self.solution_text = "<div class='side' style='width:130px;'>Count forwards.</div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(11)+"."+str(start_minutes)+" a.m.</td>"
        if start_minutes + duration > 60:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(60-start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(12)+".00 p.m.</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration-60+start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(answer)+"</td>"
        else:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(12)+".00 p.m.</td>"
        self.solution_text = self.solution_text+"</tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td>%d minutes after 11.%d a.m. is <b>%s</b></td></tr></table>"%(duration,start_minutes,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10b(self):       
        '''e.g.:
        What time is 15 minutes before 12.00 p.m.?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.minute = random.randrange(10,55,5)
        self.hour = 12
        self.AMPMs = random.choice([['a.m.','p.m.'],['p.m.','a.m.']])
        
        self.problem = "What time is %d minutes before 12.00 %s?"%(self.minute,self.AMPMs[0])
        
        self.EndMinutes = 60 - self.minute
        self.EndHour = 11
        
        self.EndMinutes = str(self.EndMinutes)
        
        if len(self.EndMinutes)==1:
            self.EndMinutes = '0'+self.EndMinutes
                        
        self.answer = "%d.%s %s"%(self.EndHour,self.EndMinutes,self.AMPMs[1])
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10b(self.problem,self.answer,self.unit,self.dollar_unit,self.minute,self.AMPMs[0])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10b(self,problem,answer,unit,dollar_unit,duration,ampm):
        
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<div class='side' style='width:220px;'>a.m. turns to p.m. at 12 noon.<br>p.m. turns to a.m. at 12 midnight.</div>"
        self.solution_text = self.solution_text + "<div><table border=0><tr>"
        if ampm == "a.m.":
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(11)+"."+str(60-duration)+" p.m.</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(duration)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(12)+".00 a.m.</td>"
        else:
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(11)+"."+str(60-duration)+" a.m.</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(duration)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(12)+".00 p.m.</td>"
        self.solution_text = self.solution_text+"</tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td>%d minutes before 12.00 %s is <b>%s</b></td></tr></table></div>"%(duration,ampm,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:
        [Person.Boyname] <took> 25 minutes< to polish his shoes.>
        <He started polishing the shoes at> 9.20 a.m.
        <At what time did he finish polishing the shoes?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                        ['took',' to polish his shoes.','He started polishing the shoes at','At what time did he finish polishing the shoes?',random.randrange(15,35,5),randint(8,20),'P3FDSFT11a','grade 3 time homework help','finished polishing the shoes at'],
                        ['spent',' in the canteen.','He went into the canteen at','At what time did he come out of the canteen?',random.randrange(15,55,5),randint(8,18),'P3FDSFT11b','grade 3 time homework help','came out of the canteen at'],
                        ['and his friends took',' to wash a car.','They started washing the car at','At what time did they finish washing the car?',random.randrange(20,50,5),randint(8,18),'P3FDSFT11c','grade 3 time homework help','and his friends finished washing the car at'],
                        ['waited for',' at the cash register.','He joined the queue at','At what time was he served?',random.randrange(10,20,5),randint(8,22),'P3FDSFT11d','grade 3 time homework help','was served at'],
                        ['took',' to walk to school from home.','He started from home at','At what time did he reach school?',random.randrange(10,25,5),randint(8,12),'P3FDSFT11e','grade 3 time homework help','reached school at'],
                        ['spent',' playing checkers with his father.','They began playing at','At what time did they finish playing?',random.randrange(20,40,5),randint(15,20),'P3FDSFT11f','grade 3 time homework help','and his father finished playing checker at'],
                        ['spent',' playing a video game.','He began playing at','At what time did he finish playing?',random.randrange(15,30,5),randint(10,20),'P3FDSFT11g','grade 3 time homework help','finished playing video game at'],
                        ['spent',' playing soccer.','He began playing at','At what time did he finish playing?',random.randrange(30,50,5),randint(10,20),'P3FDSFT11h','grade 3 time homework help','finished playing soccer at'],
                        ['took',' to deliver newspapers in his neighbourhood.','He began delivering the newspapers at','At what time did he finish delivering the newspapers?',random.randrange(20,50,5),randint(5,7),'P3FDSFT11i','grade 3 time homework help','finished delivering the newspapers at'],
                        ['took',' to iron his uniform.','He began ironing the uniform at','At what time did he finish ironing the uniform?',random.randrange(10,25,5),randint(15,20),'P3FDSFT11j','grade 3 time homework help','finished ironing the uniform at']
                    ]

        
        self.item = random.choice(self.items)
        
        self.StartHour = self.item[5]
        self.StartMinutes = random.randrange(10,55,5)
        self.DurationMinutes = self.item[4]
        
        self.EndMinutes = self.StartMinutes + self.DurationMinutes 
        self.EndHour, self.EndMinutes = divmod(self.EndMinutes,60)
        self.EndHour = self.StartHour + self.EndHour
        #for explanation
        self.OriginalStartHour = self.StartHour
        
        if len(str(self.EndMinutes))==1:
            self.EndMinutes = '0'+str(self.EndMinutes)
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."
            
        self.problem = "%s %s %d minutes%s<br><br>"%(self.name,self.item[0],self.DurationMinutes,self.item[1])
        self.problem = self.problem + "<div style='display:inline-block;vertical-align:top;'>%s %d.%d %s<br><br>"%(self.item[2],self.StartHour,self.StartMinutes,self.AMPMStart)
        self.problem = self.problem + "%s</div>"%(self.item[3])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[6]+".png' title='"+self.item[7]+"'></div>"
        
        self.answer = "%d.%s %s"%(self.EndHour,self.EndMinutes,self.AMPMEnd)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.StartMinutes,
                                               self.DurationMinutes,self.name,self.item[8])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,duration_minutes,name,text1):
        
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<div><table border=0><tr>"
        hours = self.Convert24HrsTo12Hrs(start_hour)
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        if start_minutes+duration_minutes>60:
            hours = self.Convert24HrsTo12Hrs(start_hour+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(60-start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes-60+start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(answer)+"</td>"
        else:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(answer)+"</td>"
        self.solution_text = self.solution_text+"</tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td>%s %s <b>%s</b></td></tr></table></div>"%(name,text1,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType12(self):       
        '''e.g.:
        [Person.Girlname] <spent> 45 minutes <playing hopscotch.>
        <She finished playing at> 12.05 p.m.
        <At what time did she start playing?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['and her friend spent','playing hopscotch.','They finished playing at','At what time did they start playing?',random.randrange(15,45,5),randint(10,18),'P3FDSFT12a','third grade time hour minute math problems','and her friends started playing hopscotch at'],
                        ['and her brother spent','making a sandcastle.','They finished making it at','At what time did they start making it?',random.randrange(15,45,5),randint(10,18),'P3FDSFT12b','third grade time hour minute math problems','and her brother started making sandcastle at'],
                        ['spent','making a greeting card for her mother.','She finished making it at','At what time did she start making it?',random.randrange(10,30,5),randint(10,18),'P3FDSFT12c','third grade time hour minute math problems','started making greeting card for her mother at'],
                        ['spent','writing in her diary.','She finished writing at','At what time did she start writing?',random.randrange(10,45,5),randint(20,24),'P3FDSFT12d','third grade time hour minute math problems','started writing in her diary at'],
                        ['and her father spent','watching a cartoon show.','They finished watching the show at','At what time did they start watching the show?',random.randrange(20,55,5),randint(20,24),'P3FDSFT12e','third grade time hour minute math problems','and her father started watching cartoon show at'],
                        ['spent','making paper animals.','She finished making the paper animals at','At what time did she start making them?',random.randrange(20,55,5),randint(10,20),'P3FDSFT12f','third grade time hour minute math problems','started making paper animals at'],
                        ['and her mother spent','making sandwiches.','They finished making the sandwiches at','At what time did they start making the sandwiches?',random.randrange(10,25,5),randint(7,16),'P3FDSFT12g','third grade time hour minute math problems','and her mother started making the sandwiches at'],
                        ['spent','making a sketch.','She finished making the sketch at','At what time did she start making the sketch?',random.randrange(30,55,5),randint(10,18),'P3FDSFT12h','third grade time hour minute math problems','started making the sketch at'],
                        ['spent','making a mask.','She finished making the mask at','At what time did she start making the mask?',random.randrange(30,55,5),randint(10,17),'P3FDSFT12i','third grade time hour minute math problems','started making the mask at'],
                        ['spent','making a mosaic.','She finished making the mosaic at','At what time did she start making the mosaic?',random.randrange(30,55,5),randint(10,18),'P3FDSFT12j','third grade time hour minute math problems','started making the mosaic at']
                    ]        
        self.item = random.choice(self.items)
        
        self.EndHour = self.item[5]
        self.EndMinutes = random.randrange(10,55,5)
        self.duration = self.item[4]
        self.StartHour, self.StartMinutes = divmod(self.EndHour*60+self.EndMinutes-self.duration,60)

        #for explanation
        self.OriginalStartHour = self.StartHour
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."     
        
        self.problem = "%s %s %d minutes %s<br>"%(self.name,self.item[0],self.duration,self.item[1])
        self.problem = self.problem + "<div style='display:inline-block;vertical-align:top;'>%s %d.%d %s<br>%s</div>"%(self.item[2],self.EndHour,self.EndMinutes,self.AMPMEnd,self.item[3])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[6]+".png' title='"+self.item[7]+"'></div>"
        
        self.StartMinutes = str(self.StartMinutes)
        if len(self.StartMinutes)==1:
            self.StartMinutes = '0'+self.StartMinutes
            
        self.answer = "%d.%s %s"%(self.StartHour,self.StartMinutes,self.AMPMStart)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.StartMinutes,
                                               self.EndHour,self.EndMinutes,self.duration,self.name,self.item[8])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType12(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,end_hour,end_minutes,duration_minutes,name,text1):
        
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<div><table border=0><tr>"
        hours = self.Convert24HrsTo12Hrs(start_hour)
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        if int(start_minutes)+duration_minutes>60:
            hours = self.Convert24HrsTo12Hrs(start_hour+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(60-int(start_minutes))+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(duration_minutes-60+int(start_minutes))+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        elif int(start_minutes)+duration_minutes<60:
            hours = self.Convert24HrsTo12Hrs(start_hour)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        elif int(start_minutes)+duration_minutes==60:
            hours = self.Convert24HrsTo12Hrs(start_hour+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
        self.solution_text = self.solution_text+"</tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td>%s %s <b>%s</b></td></tr></table></div>"%(name,text1,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType13a(self):       
        '''e.g.:
        How many minutes are there from 7.00 p.m. to 7.25 p.m.?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.StartHour = randint(1,10)
        self.StartMinutes = random.randrange(10,55,5)
        self.duration = random.randrange(5,55,5)
        self.EndMinutes = self.StartMinutes + self.duration
        
        self.EndHour,self.EndMinutes = divmod(self.EndMinutes,60)
        self.EndHour = self.EndHour + self.StartHour

        self.EndMinutes = str(self.EndMinutes)
        
        if len(self.EndMinutes)==1:
            self.EndMinutes = '0'+self.EndMinutes
            
        self.AMPM = random.choice(['a.m.','p.m.'])
        
        self.problem = "How many minutes are there from %d.%d %s to %d.%s %s?"%(self.StartHour,self.StartMinutes,self.AMPM,self.EndHour,self.EndMinutes,self.AMPM)
                        
        self.answer = self.duration
                   
        self.unit = "minutes"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13a(self.problem,self.answer,self.unit,self.dollar_unit,self.StartHour,self.StartMinutes,
                                                self.EndHour,self.EndMinutes,self.duration,self.AMPM)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType13a(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,end_hour,end_minutes,duration_minutes,ampm):
        
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<table border=0><tr>"
        if ampm == "a.m.":
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(start_hour)+"."+str(start_minutes)+" "+ampm+"</td>"
            if start_minutes+duration_minutes>60:
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(60-start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(start_hour+1)+".00 a.m.</td>"
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes-60+start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+"."+str(end_minutes)+" "+ampm+"</td>"
                self.solution_text = self.solution_text+"</tr></table><br>"
                self.solution_text = self.solution_text+"<table border=0>"
                self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
                self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(60-start_minutes)+" min + "+str(duration_minutes-60+start_minutes)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" min</td></tr>"
                self.solution_text = self.solution_text+"</table><br>"
            else:
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+"."+str(end_minutes)+" "+ampm+"</td>"
                self.solution_text = self.solution_text+"</tr></table><br>"
        else:
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(start_hour)+"."+str(start_minutes)+" "+ampm+"</td>"
            if start_minutes+duration_minutes>60:
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(60-start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(start_hour+1)+".00 p.m.</td>"
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes-60+start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+"."+str(end_minutes)+" "+ampm+"</td>"
                self.solution_text = self.solution_text+"</tr></table><br>"
                self.solution_text = self.solution_text+"<table border=0>"
                self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
                self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(60-start_minutes)+" min + "+str(duration_minutes-60+start_minutes)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" min</td></tr>"
                self.solution_text = self.solution_text+"</table><br>"
            else:
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+"."+str(end_minutes)+" "+ampm+"</td>"
                self.solution_text = self.solution_text+"</tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td>There are <b>%s %s</b> from %d.%d %s to %d.%s %s</tr></table>"%(answer,unit,start_hour,start_minutes,
                                                                                                                             ampm,end_hour,end_minutes,ampm)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType13b(self):       
        '''e.g.:
        How many minutes are there from 11.35 a.m. to 12.10 p.m.?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.StartHour = 11
        self.StartMinutes = random.randrange(10,55,5)
        self.duration = random.randrange(60-self.StartMinutes,55,5)
        self.EndMinutes = self.StartMinutes + self.duration - 60
        self.EndHour = 12

        self.EndMinutes = str(self.EndMinutes)
        
        if len(self.EndMinutes)==1:
            self.EndMinutes = '0'+self.EndMinutes
        
        self.problem = "How many minutes are there from %d.%d a.m. to %d.%s p.m.?"%(self.StartHour,self.StartMinutes,self.EndHour,self.EndMinutes)
                        
        self.answer = self.duration
                   
        self.unit = "minutes"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13b(self.problem,self.answer,self.unit,self.dollar_unit,self.StartHour,self.StartMinutes,self.EndHour,
                                                self.EndMinutes,self.duration)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType13b(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,end_hour,end_minutes,duration_minutes):
        
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(start_hour)+"."+str(start_minutes)+" a.m.</td>"
        if start_minutes+duration_minutes>60:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(60-start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(start_hour+1)+".00 p.m.</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes-60+start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+"."+str(end_minutes)+" p.m.</td>"
            self.solution_text = self.solution_text+"</tr></table><br>"
            self.solution_text = self.solution_text+"<table border=0>"
            self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(60-start_minutes)+" min + "+str(duration_minutes-60+start_minutes)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+" min</td></tr>"
            self.solution_text = self.solution_text+"</table><br>"
        else:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+"."+str(end_minutes)+" p.m.</td>"
            self.solution_text = self.solution_text+"</tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td>There are <b>%s %s</b> from %d.%d a.m. to %d.%s p.m.</tr></table>"%(answer,unit,start_hour,start_minutes,
                                                                                                                           end_hour,end_minutes)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType14(self):       
        '''e.g.:
        [Person.Boyname] <was at the park> from 10.40 a.m. to 2.25 p.m.
        How long <was he at the park>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                        ['was at the park','was he at the park',randint(8,14),random.randrange(185,295,10),'P3FDSFT14a','grade 3 time problem sums','was at the park for','.'],
                        ['was in the music room','was he in the music room',randint(8,14),random.randrange(75,145,10),'P3FDSFT14b','grade 3 time problem sums','was in the music room for','.'],
                        ["was at his cousin's house",'was his visit',randint(8,14),random.randrange(185,295,15),'P3FDSFT14c','grade 3 time problem sums',"was at his cousin's house for",'.'],
                        ['was at the school carnival','was he at the carnival',randint(8,13),random.randrange(125,305,10),'P3FDSFT14d','grade 3 time problem sums','was at school carnival for','.'],
                        ['was at the ice rink','was he at the rink',randint(8,13),random.randrange(125,245,10),'P3FDSFT14e','grade 3 time problem sums','was at the ice rink for','.'],
                        ['was at the bowling alley','was he at the bowling alley',randint(8,13),random.randrange(125,245,10),'P3FDSFT14f','grade 3 time problem sums','was at the bowling alley for','.'],
                        ['went for a picnic with his family','was their picnic',randint(10,15),random.randrange(185,305,10),'P3FDSFT14g','grade 3 time problem sums',"'s family picnic was",' long.'],
                        ['went for a swim','did he swim',randint(6,9),random.randrange(65,115,5),'P3FDSFT14h','grade 3 time problem sums','swam for','.'],
                        ['took his dog for a walk','did he walk his dog',randint(7,11),random.randrange(65,115,5),'P3FDSFT14i','grade 3 time problem sums','walked his dog for','.'],
                        ['worked on his science project','did he spend on the project',randint(8,15),random.randrange(185,305,10),'P3FDSFT14j','grade 3 time problem sums','spent',' on his science project.']
                    ]
        
        self.item = random.choice(self.items)
        
        self.StartHour = self.item[2]
        self.StartMinutes = random.randrange(10,55,5)
        self.duration = self.item[3]
        self.DurationHour,self.DurationMinutes = divmod(self.duration,60)
        
        self.EndMinutes = self.StartMinutes + self.DurationMinutes 
        self.EndHour, self.EndMinutes = divmod(self.EndMinutes,60)
        self.EndHour = self.StartHour + self.EndHour + self.DurationHour
        #for explanation
        self.OriginalStartHour = self.StartHour
        
        if len(str(self.EndMinutes))==1:
            self.EndMinutes = '0'+str(self.EndMinutes)
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."
            
        self.problem = "%s %s from %d.%d %s to %d.%s %s<br><br>"%(self.name,self.item[0],self.StartHour,self.StartMinutes,self.AMPMStart,
                                                                    self.EndHour,self.EndMinutes,self.AMPMEnd)
        self.problem = self.problem + "<div style='display:inline-block;vertical-align:top;'>How long %s?<br><br>"%(self.item[1])
        self.problem = self.problem + "[Write your answer as in example below:<br> 1 h 25 min]</div>"
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[4]+".png' title='"+self.item[5]+"'></div>"
        
        self.answer = "%d h %d min"%(self.DurationHour,self.DurationMinutes)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.StartMinutes,self.DurationHour,
                                               self.DurationMinutes,self.EndHour,self.EndMinutes,self.AMPMEnd,self.name,self.item[6],self.item[7])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType14(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,duration_hour,duration_minutes,end_hour,end_minutes,end_ampm,name,text1,text2):
        
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<div><table border=0><tr>"
        hours = self.Convert24HrsTo12Hrs(start_hour)
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        if start_minutes+duration_minutes>60:
            start_hour = start_hour + 1
            hours = self.Convert24HrsTo12Hrs(start_hour)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(60-start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            for i in range(duration_hour):
                hours = self.Convert24HrsTo12Hrs(start_hour+i+1)
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes-60+start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(end_hour)+"."+str(end_minutes)+" "+str(end_ampm)+"</td>"
            self.solution_text = self.solution_text+"</tr></table><br>"
            self.solution_text = self.solution_text+"<table>"
            self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(60-start_minutes)+" min + "+str(duration_hour)+" h + "+str(duration_minutes-60+start_minutes)+" min</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+"</td></tr>"
            self.solution_text = self.solution_text+"</table><br>"
        else:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
            for i in range(duration_hour):
                hours = self.Convert24HrsTo12Hrs(start_hour+i+1)
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text+"</tr></table><br>"
            self.solution_text = self.solution_text+"<table>"
            self.solution_text = self.solution_text+"<tr><td colspan=2 style='text-align:left'>So,</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(duration_minutes)+" min + "+str(duration_hour)+" h</td><td style='padding-left:0px; padding-right:0px'>=</td><td style='text-align:left'>"+str(answer)+"</td></tr>"
            self.solution_text = self.solution_text+"</table><br>"

        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td>%s %s <b>%s</b>%s</td></tr></table></div>"%(name,text1,answer,text2)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType15(self):       
        '''e.g.:
        [Person.Girlname] <baked some cookies for a party.>
        <She took> 1 h 40 min <to bake the cookies.>
        <She started baking them at> 11.15 a.m.
        <When did she finish baking them?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['baked some cookies for a party.','She took','to bake the cookies.','She started baking them at','When did she finish baking them?',random.randrange(75,175,10),randint(8,17),'P3FDSFT15a','grade 3 time','finished baking cookies at'],
                        ['packed some goodie bags for her birthday party.','She took','to pack the goodie bags.','She started packing them at','When did she finish packing them?',random.randrange(65,115,5),randint(8,21),'P3FDSFT15b','grade 3 time','finished packing goodie bags at'],
                        ['sold lemonade at a fundraiser.','It took her','to sell all the lemonade.','She started selling it at','When did she finish selling it?',random.randrange(130,280,15),randint(8,14),'P3FDSFT15c','grade 3 time','finished selling lemonade at'],
                        ['had a stall at a food festival.','She opened the stall for','.','She opened the stall at','When did she close the stall?',random.randrange(125,245,10),randint(8,14),'P3FDSFT15d','grade 3 time','closed the food stall at'],
                        ['arranged the books in her school library.','She took','to arrange the books.','She started at','When did she finish?',random.randrange(65,125,10),randint(8,14),'P3FDSFT15e','grade 3 time','finished arranging the books at'],
                        ['knitted a cap.','She took','to knit the cap.','She started knitting at','When did she finish knitting?',random.randrange(190,310,15),randint(8,12),'P3FDSFT15f','grade 3 time','finished knitting the cap at'],
                        ["and her classmates decorated their classroom for Children's Day.",'They took','to decorate the classroom.','They started at','When did they finish?',random.randrange(75,175,10),randint(8,14),'P3FDSFT15g','grade 3 time','and her classmates finished decorating the classroom at'],
                        ['and her friends revised together for an exam.','They took','to revise.','They started at','When did they finish?',random.randrange(190,310,15),randint(8,16),'P3FDSFT15h','grade 3 time','and her friends finished revising for the exam at'],
                        ['made a treehouse with sticks.','She took','to make the treehouse.','She started at','When did she finish?',random.randrange(190,310,15),randint(8,16),'P3FDSFT15i','grade 3 time','finished making the matchstick treehouse at'],
                        ['made bookmarks to sell at a carnival.','She took','to make the bookmarks.','She started at','When did she finish?',random.randrange(190,310,15),randint(8,16),'P3FDSFT15j','grade 3 time','finished making the bookmarks at']
                    ]
        
        self.item = random.choice(self.items)
        
        self.StartHour = self.item[6]
        self.StartMinutes = random.randrange(10,55,5)
        self.duration = self.item[5]
        if self.duration % 60 == 0:
            self.duration = self.duration + 5
        self.DurationHour,self.DurationMinutes = divmod(self.duration,60)
        
        self.EndMinutes = self.StartMinutes + self.DurationMinutes 
        self.EndHour, self.EndMinutes = divmod(self.EndMinutes,60)
        self.EndHour = self.StartHour + self.EndHour + self.DurationHour
        
        if len(str(self.EndMinutes))==1:
            self.EndMinutes = '0'+str(self.EndMinutes)
        #for explanation
        self.OriginalStartHour = self.StartHour
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."
            
        self.problem = "%s %s<br><br>"%(self.name,self.item[0])
        self.problem = self.problem + "<div style='display:inline-block;vertical-align:top;'>%s %d h %d min %s<br><br>"%(self.item[1],self.DurationHour,self.DurationMinutes,self.item[2])
        self.problem = self.problem + "%s %d.%d %s<br><br>%s</div>"%(self.item[3],self.StartHour,self.StartMinutes,self.AMPMStart,self.item[4])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[7]+".png' title='"+self.item[8]+"'></div>"
        
        self.answer = "%d.%s %s"%(self.EndHour,self.EndMinutes,self.AMPMEnd)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.StartMinutes,self.DurationHour,
                                               self.DurationMinutes,self.EndMinutes,self.name,self.item[9])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType15",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType15(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,duration_hour,duration_minutes,end_minutes,name,text1):
        
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<div><table border=0><tr>"
        hours = self.Convert24HrsTo12Hrs(start_hour)
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        if start_minutes+duration_minutes>60:
            start_hour = start_hour + 1
            hours = self.Convert24HrsTo12Hrs(start_hour)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(60-start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            for i in range(duration_hour):
                hours = self.Convert24HrsTo12Hrs(start_hour+i+1)
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes-60+start_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(answer)+"</td>"
        else:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(duration_minutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(end_minutes)+" "+str(hours[1])+"</td>"
            for i in range(duration_hour):
                hours = self.Convert24HrsTo12Hrs(start_hour+i+1)
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(answer)+"</td>"
        
        self.solution_text = self.solution_text+"</tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td>%s %s <b>%s</b></td></tr></table></div>"%(name,text1,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType16(self):       
        '''e.g.:
        [Person.Auntyname] <went to the laundromat.>
        <She was there for> two hours.
        <She left the laundromat at> 12.20 a.m.
        <When did she go to the laundromat?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [
                        ['went to the laundromat.','She was there for','She left the laundromat at','When did she go to the laundromat?',randint(1,3),randint(12,14),'P3FDSFT16a','third grade homeschooling for math','went to the laundromat at'],
                        ['went to the hair salon.','She was there for','She left the hair salon at','When did she go to the hair salon?',randint(1,3),randint(12,14),'P3FDSFT16b','third grade homeschooling for math','went to the hair salon at'],
                        ['went to the mall.','She was there for','She left the mall at','When did she go to the mall?',randint(1,3),randint(12,14),'P3FDSFT16c','third grade homeschooling for math','went to the mall at'],
                        ['went to her office.','She was there for','She left her office at','When did she arrive at her office?',randint(6,9),randint(15,18),'P3FDSFT16d','third grade homeschooling for math','arrived at her office at'],
                        ['went to her shop.','She was there for','She left her shop at','When did she arrive at her shop?',randint(6,9),randint(16,19),'P3FDSFT16e','third grade homeschooling for math','arrived at her shop at'],
                        ['went to her bakery.','She was there for','She left her bakery at','When did she arrive at her bakery?',randint(4,6),randint(12,16),'P3FDSFT16f','third grade homeschooling for math','arrived at her bakery at'],
                        ['took a bus to visit her aunt.','She was on the bus for','She got off the bus at','When did she board the bus?',randint(4,9),randint(10,20),'P3FDSFT16g','third grade homeschooling for math','boarded the bus at'],
                        ['went on a train to Town A.','She was on the train for','She got off the train at','When did she board the train?',randint(4,9),randint(10,20),'P3FDSFT16h','third grade homeschooling for math','boarded the train at'],
                        ['took her children to a theme park.','They were in the park for','They left the park at','When did they arrive at the park?',randint(4,7),randint(15,18),'P3FDSFT16i','third grade homeschooling for math','and her children arrived at the park at'],
                        ['and her children went to a zoo.','They were in the zoo for','They left the zoo at','When did they arrive at the zoo?',randint(3,5),randint(15,18),'P3FDSFT16j','third grade homeschooling for math','and her children arrived at the zoo at']
                    ]        
        self.item = random.choice(self.items)
        
        self.EndHour = self.item[5]
        self.EndMinutes = randint(10,59)
        self.duration = self.item[4]
        self.DurationInWords = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
        self.StartHour, self.StartMinutes = divmod(self.EndHour*60+self.EndMinutes-self.duration*60,60)
        #for explanation
        self.OriginalStartHour = self.StartHour
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
            
        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        else:
            self.AMPMEnd = "a.m."     
        
        self.problem = "<div style='display:inline-block;vertical-align:top;'>%s %s<br>"%(self.name,self.item[0])
        self.problem = self.problem + "%s %s hours.<br>"%(self.item[1],self.DurationInWords[self.duration])
        self.problem = self.problem + "%s %d.%d %s<br>%s</div>"%(self.item[2],self.EndHour,self.EndMinutes,self.AMPMEnd,self.item[3])
        self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[6]+".png' title='"+self.item[7]+"'></div>"
        
        self.StartMinutes = str(self.StartMinutes)
        if len(self.StartMinutes)==1:
            self.StartMinutes = '0'+self.StartMinutes
            
        self.answer = "%d.%s %s"%(self.StartHour,self.StartMinutes,self.AMPMStart)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType16(self.problem,self.answer,self.unit,self.dollar_unit,self.OriginalStartHour,self.StartMinutes,self.duration,
                                               self.name,self.item[8])
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType16",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType16(self,problem,answer,unit,dollar_unit,start_hour,start_minutes,duration_hour,name,text1):
        
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<div class='side' style='width:130px;'>Count backwards.</div>"
        self.solution_text = self.solution_text + "<div><table border=0><tr>"
        hours = self.Convert24HrsTo12Hrs(start_hour)
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        for i in range(duration_hour):
            hours = self.Convert24HrsTo12Hrs(start_hour+i+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_1h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(start_minutes)+" "+str(hours[1])+"</td>"
        
        self.solution_text = self.solution_text+"</tr></table><br>"

        self.solution_text = self.solution_text + "<table><tr>"
        self.solution_text = self.solution_text + "<td>%s %s <b>%s</b></td></tr></table></div>"%(name,text1,answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"").lower()
                answer = string.join(str(answer).split(),"")
                if "a" in InputAnswer:
                    InputAnswer1 = InputAnswer.partition("a")[0]
                    InputAnswer2 = InputAnswer.partition("a")[1]+InputAnswer.partition("a")[2]
                    if ":" in InputAnswer1:
                        InputAnswer1 = InputAnswer1.partition(":")[0]+"."+InputAnswer1.partition(":")[2]
                    if len(InputAnswer2)<5 and "m" in InputAnswer:
                        InputAnswer2 = "a.m."
                    InputAnswer = InputAnswer1+InputAnswer2
                elif "p" in InputAnswer:
                    InputAnswer1 = InputAnswer.partition("p")[0]
                    InputAnswer2 = InputAnswer.partition("p")[1]+InputAnswer.partition("p")[2]
                    if ":" in InputAnswer1:
                        InputAnswer1 = InputAnswer1.partition(":")[0]+"."+InputAnswer1.partition(":")[2]
                    if len(InputAnswer2)<5 and "m" in InputAnswer:
                        InputAnswer2 = "p.m."
                    InputAnswer = InputAnswer1+InputAnswer2                        
                return InputAnswer == answer
            except ValueError:
                return False  
        elif CheckAnswer == 2:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False
        elif CheckAnswer == 3:
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"").lower()
                answer = string.join(str(answer).split(),"")                
                return answer==InputAnswer
            except ValueError:
                return False

    def Convert24HrsTo12Hrs(self,hour):
        if hour > 12:
            hour = hour - 12
            ampm = "p.m."
        elif hour == 12:
            ampm = "p.m."
        else:
            ampm = "a.m."
        return [hour,ampm]