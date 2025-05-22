'''
Created on Jul 10, 2013
Module: P3TIWordProblems
Generates the word problems on Time for Primary 3

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

class P3TIWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemType4",],
                            5:["ProblemType5",],6:["ProblemType6",],7:["ProblemType7",],8:["ProblemType8",],
                            9:["ProblemType9a","ProblemType9b",],10:["ProblemType10",],11:["ProblemType11",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],4:[self.GenerateProblemType4(),],
                                    5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],
                                    9:[self.GenerateProblemType9a(),self.GenerateProblemType9b(),],
                                    10:[self.GenerateProblemType10(),],11:[self.GenerateProblemType11(),],                                   
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
        #return self.GenerateProblemType4()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9a":self.GenerateProblemType9a(),
                            "ProblemType9b":self.GenerateProblemType9b(),
                            "ProblemType10":self.GenerateProblemType10(),
                            "ProblemType11":self.GenerateProblemType11(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        [Person.Girlname] <baked two cakes.>
        <She baked the first cake in> 2 h 30 min <followed by the second one in> 3 h 40 min<.>
        <She finished baking the cakes at> 7.20 p.m.
        <At what time did she start baking the cakes?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['baked two cakes.','She baked the first cake in','followed <br>by the second one in','.','She finished baking the cakes at','At what time did she start baking the cakes?',randint(2,3),randint(2,3),randint(16,20),'baking the two cakes.','She started baking the cakes at'],
                        ['wrote two essays one after the other.','She wrote the first essay<br> in','and the second essay in','.','She finished writing the essays at','At what time did she start writing the essays?',randint(1,2),randint(1,2),randint(12,22),'writing the two essays.','She started writing the essays at'],
                        ['watched two movies back to back.','The first movie lasted','<br>and the second movie lasted','.','She finished watching the movies at','At what time did she start watching the movies?',randint(1,2),randint(1,2),randint(15,23),'watching the two movies.','She started watching the movies at'],
                        ['worked two shifts back to back.','The first shift ended after','<br>and the second shift ended after','.','She finished work at','At what time did she begin work?',randint(4,6),randint(4,6),randint(15,23),'working the two shifts.','She began work at'],
                        ['painted two rooms.','She took','to paint the first room <br>and',' to paint the second room.','She finished painting at','At what time did she begin painting?',randint(1,3),randint(1,3),randint(14,22),'painting the two rooms.','She started painting the rooms at'],
                        ['cooked two dishes one after the other.','She took','to cook the first dish and',' to cook the second dish.','She finished cooking at','At what time did she begin cooking?',randint(1,2),randint(1,2),randint(12,16),'cooking the two dishes.','She began cooking at']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[6]
        self.hour2 = self.item[7]
        self.minutes1 = random.randrange(5,50,5)
        self.minutes2 = random.randrange(5,55,5)
        if self.minutes1 == self.minutes2:
            self.minutes2 = self.minutes1 + 5
                   
        self.TotalMinutes1 = self.hour1*60+self.minutes1
        self.TotalMinutes2 = self.hour2*60+self.minutes2
        
        self.TotalHours,self.TotalMinutes = divmod((self.TotalMinutes1+self.TotalMinutes2),60)
        
        self.EndHour = self.item[8]
        self.EndMinute = random.randrange(10,55,5)
        
        self.StartHour,self.StartMinute = divmod(self.EndHour*60+self.EndMinute-(self.TotalMinutes1+self.TotalMinutes2),60)
        
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
            
        self.StartMinute = str(self.StartMinute)
        if len(self.StartMinute)==1:
            self.StartMinute = '0'+self.StartMinute       
        
        self.problem = "%s %s "%(self.name,self.item[0])
        self.problem = self.problem + "%s %d h %d min %s %d h %d min%s<br>"%(self.item[1],self.hour1,self.minutes1,self.item[2],self.hour2,self.minutes2,self.item[3])
        self.problem = self.problem + "%s %d.%d %s<br>%s"%(self.item[4],self.EndHour,self.EndMinute,self.AMPMEnd,self.item[5])
        
        self.answer = "%d.%s %s"%(self.StartHour,self.StartMinute,self.AMPMStart)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.OriginalStartHour,self.StartHour,self.StartMinute,self.AMPMStart,self.EndHour,self.EndMinute,self.AMPMEnd,self.hour1,self.hour2,self.minutes1,self.minutes2,self.TotalHours,self.TotalMinutes,self.item[9],self.item[10],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,OriginalStartHour,StartHour,StartMinute,AMPMStart,EndHour,EndMinute,AMPMEnd,hour1,hour2,minutes1,minutes2,TotalHours,TotalMinutes,item9,item10,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        2 h 30 min + 3 h 40 min = 6 h 10 min
        She spent 6 h 10 min baking the two cakes.
        
                   10 min             6h
        1.10 p.m. <-----  1.20 p.m. <----  7.20 p.m.
        She started baking the cakes at 1.10 p.m.
        '''
        
        self.solution_text = "<br><font class='ExplanationFont'>%d h %d min &nbsp;+&nbsp; %d h %d min &nbsp;=&nbsp; %d h %d min</font>"%(hour1,minutes1,hour2,minutes2,TotalHours,TotalMinutes)
        self.solution_text = self.solution_text + "<br>"
        if TotalMinutes==0:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>She spent %d hours %s</font>"%(TotalHours,item9)
        else:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>She spent %d h %d min %s</font>"%(TotalHours,TotalMinutes,item9)
        self.solution_text = self.solution_text + "<br><br>"
        
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+" "+str(AMPMStart)+"</td>"
        if int(StartMinute)+TotalMinutes<60:
            if TotalMinutes!=0:
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(TotalMinutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(int(StartMinute)+TotalMinutes)+" "+str(AMPMStart)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(TotalHours)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+" "+str(AMPMEnd)+"</td>"
        elif int(StartMinute)+TotalMinutes==60:
            hours = self.Convert24HrsTo12Hrs(OriginalStartHour+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(TotalMinutes)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(TotalHours)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+" "+str(AMPMEnd)+"</td>"
        else:
            hours = self.Convert24HrsTo12Hrs(OriginalStartHour+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(60-int(StartMinute))+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(TotalMinutes-60+int(StartMinute))+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(EndMinute)+" "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(TotalHours)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+" "+str(AMPMEnd)+"</td>"
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s <b>%d.%s %s</b></font>"%(item10,StartHour,StartMinute,AMPMStart)

        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        [Person.Boyname] <loves milk.>
        <He drinks a glass of milk every> 5 hours, 3 times a day.
        <He drank his first glass of milk> for the day at 6.30 a.m.
        <At what time should he drink his last glass of milk> for the day?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                        ['loves milk.','He drinks a glass of milk every','He drank his first glass of milk','At what time should he drink his last glass of milk',random.choice([[4,3,8],[4,3,9],[4,3,10],[4,4,6],[4,4,7],[4,4,8],[5,3,6],[5,3,7],[5,3,8],[5,4,6],[6,3,6],[6,3,7],[6,3,8]]),'He has to drink','more glasses of milk after the first one','He should drink his last glass of milk'],
                        ['has an aquarium.','He feeds the fishes in the aquarium every','He gave them their first feed','At what time should he give them their last feed',random.choice([[5,3,6],[5,3,7],[5,3,8],[5,4,6],[6,3,6],[6,3,7],[6,3,8],[7,3,5],[7,3,6]]),'He has to give them','more feeds after the first one','He should give them their last feed'],
                        ['and his pet dog love the outdoors.','On Sundays, they go for a walk every','Last Sunday, they went for their first walk','At what time did they go for their last walk',random.choice([[5,3,6],[5,3,7],[5,3,8],[5,4,6],[6,3,6],[6,3,7],[6,3,8],[7,3,5],[7,3,6]]),'They went for','more walks after the first one','They went for their last walk'],
                        ['has a special collection of plants.','He needs to water them every','He watered them for the first time','At what time should he water them for the last time',random.choice([[4,3,8],[4,3,9],[4,3,10],[4,4,6],[4,4,7],[4,4,8],[5,3,6],[5,3,7],[5,3,8],[5,4,6],[6,3,6],[6,3,7],[6,3,8]]),'He has to water them','more times after the first one','He should water them for the last time'],
                        ['loves food.','He eats a meal every','He had his first meal','At what time should he have his last meal',random.choice([[3,5,7],[3,5,8],[3,5,9],[3,6,6],[4,4,6],[4,4,7],[4,4,8],[4,4,9],[5,4,6]]),'He has to have','more meals after the first one','He should have his last meal'],
                        ['is participating in a concert.','He needs to practise every','He did his first practice','At what time should he do his last practice',random.choice([[4,3,8],[4,3,9],[4,3,10],[4,4,6],[4,4,7],[4,4,8],[5,3,6],[5,3,7],[5,3,8],[5,4,6],[6,3,6],[6,3,7],[6,3,8]]),'He has to do','more practices after the first one','He should do his last practice']
                    ]
        
        self.item = random.choice(self.items)
        
        self.hour1 = self.item[4][0]
        self.times = self.item[4][1]
        self.StartHour = self.item[4][2]
        self.StartMinute = random.randrange(15,45,15)
        
        self.TotalMinutes1 = self.hour1*(self.times-1)*60
        
        self.EndHour,self.EndMinute = divmod(self.StartHour*60+self.StartMinute+self.TotalMinutes1,60)
        
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
            
        self.EndMinute = str(self.EndMinute)
        if len(self.EndMinute)==1:
            self.EndMinute = '0'+self.EndMinute       
        
        self.problem = "%s %s<br>"%(self.name,self.item[0])
        self.problem = self.problem + "%s %d hours, %d times a day.<br>"%(self.item[1],self.hour1,self.times)
        self.problem = self.problem + "%s for the day at %d.%d %s<br>"%(self.item[2],self.StartHour,self.StartMinute,self.AMPMStart)
        self.problem = self.problem + "%s for the day?"%(self.item[3])
        
        self.answer = "%d.%s %s"%(self.EndHour,self.EndMinute,self.AMPMEnd)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.StartHour,self.StartMinute,self.AMPMStart,self.EndHour,self.EndMinute,self.AMPMEnd,self.hour1,self.times,self.item[5],self.item[6],self.item[7],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,StartHour,StartMinute,AMPMStart,EndHour,EndMinute,AMPMEnd,hour1,times,item5,item6,item7,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        5 h &times; 2 = 10 h                                                 | 3-1 = 2
        He should drink his last glass of milk for the day 10 hours later.  | He has to drink 2 more glasses of milk.
        
                   10 h
        6.30 a.m. ----> 4.30 p.m.
        He should drink his last glass of milk for the day at 4.30 p.m.
        '''
        self.solution_text = "<div class='side'><font style='font-size:12px'>%d &nbsp;&minus;&nbsp; 1 &nbsp;=&nbsp; %d<br>%s %d %s.</font></div>"%(times,times-1,item5,times-1,item6)
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>%d h &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d h</font>"%(hour1,times-1,hour1*(times-1))
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s for the day %d hours later.</font>"%(item7,hour1*(times-1))
        self.solution_text = self.solution_text + "<br><br>"
        
        '''self.solution_text = self.solution_text + "%d.%s %s + %d h = %d.%s %s"%(StartHour,StartMinute,AMPMStart,hour1*(times-1),EndHour,EndMinute,AMPMEnd)
        self.solution_text = self.solution_text + "<br>"'''
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+" "+str(AMPMStart)+"</td>"
        self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(hour1*(times-1))+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+" "+str(AMPMEnd)+"</td>"
        self.solution_text = self.solution_text+"</tr></table>"
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>%s for the day at <b>%d.%s %s</b><br></font>"%(item7,EndHour,EndMinute,AMPMEnd)


        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        [Person.Auntyname] works at <a tailoring shop.>
        She takes 30 minutes <to sew a skirt>.
        She is paid $5 for an hour of work.
        <Last Tuesday, she sewed> 8 <skirts.>
        How much money did she earn for <sewing> the 8 <skirts>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [
                        ['a tailoring shop','to sew a skirt','Last Tuesday, she sewed','skirts','sewing','skirts',random.choice([[30,4],[30,6],[30,8],[40,3],[40,6],[40,9],[45,4],[45,8],[50,6]]),randint(5,9),'skirt','to sew'],
                        ['a car wash','to wash a car','Last Saturday, she washed','cars','washing','cars',random.choice([[30,4],[30,6],[30,8],[40,3],[40,6],[40,9],[45,4],[45,8],[50,6]]),randint(5,9),'car','to wash'],
                        ['a tea plantation','to pick a basket of tea leaves','Today, she picked','baskets of tea leaves','picking','baskets of tea leaves',random.choice([[30,4],[30,6],[30,8],[40,3],[40,6],[40,9],[45,4],[45,8],[50,6]]),randint(3,5),'basket','to pick'],
                        ['an ironing service','to iron a load of clothes','Yesterday, she ironed','loads of clothes','ironing','loads of clothes',random.choice([[30,4],[30,6],[30,8],[40,3],[40,6],[40,9],[45,4],[45,8],[50,6]]),randint(3,7),'load','to iron'],
                        ['a bakery','to bake a tray of pies','Last Sunday, she baked','trays of pies','baking','trays of pies',random.choice([[30,4],[30,6],[30,8],[40,3],[40,6],[40,9],[45,4],[45,8],[50,6]]),randint(5,9),'tray','to bake'],
                        ['a hair salon','to serve a client','Yesterday, she served','clients','serving','clients',random.choice([[30,4],[30,6],[30,8],[40,3],[40,6],[40,9],[45,4],[45,8],[50,6]]),randint(5,9),'client','to serve']
                    ]
        
        self.item = random.choice(self.items)
        
        self.minutes = self.item[6][0]
        self.quantity = self.item[6][1]
        self.pay = self.item[7]
        
        self.totalHours = self.minutes*self.quantity/60
        
        self.problem = "%s works at %s.<br>"%(self.name,self.item[0])
        self.problem = self.problem + "She takes %d minutes %s.<br>"%(self.minutes,self.item[1])
        self.problem = self.problem + "She is paid $%d for an hour of work.<br>"%(self.pay)
        self.problem = self.problem + "%s %d %s.<br>"%(self.item[2],self.quantity,self.item[3])
        self.problem = self.problem + "How much money did she earn for %s the %d %s?"%(self.item[4],self.quantity,self.item[5])
        
        self.answer = self.minutes*self.quantity*self.pay/60
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.totalHours,self.minutes,self.quantity,self.pay,self.item[4],self.item[5],self.item[8],self.item[9],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,totalHours,minutes,quantity,pay,item4,item5,item8,item9,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        1 skirt  -> 30 min            | 1 h = 60 min = 6 &times; 10 min
        8 skirts -> 8 &times; 30 min  | 4 h = 4 &times; 60 min
              = 240 min               | Think of the times table of 6.
              = 4 h                   | 4 &times; 6 = 24
                                      | So, 4 &times; 60 = 240 min
        She took 4 hours to sew 8 skirts.
        
        1 h -> $5
        4 h -> 4 &times; $5
             = $20
        She earned $20 for sewing the 8 skirts.
        '''
        self.solution_text = "<div class='side'><font style='font-size:12px'>60 min = 1 h<br>"+str(totalHours*60)+" min = ? <br>Think of the times table of 6.<br><b>"+str(totalHours)+"</b> &times; 6 = "+str(totalHours*6)+"<br>So, <b>"+str(totalHours)+"</b> &times; 60 min = "+str(totalHours*60)+" min = <b>"+str(totalHours)+" h</b></font></div>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>" 
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 "+item8+"</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>"+str(quantity)+" "+item8+"s</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(quantity)+" &times; "+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>"+str(minutes*quantity)+" minutes</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>"+str(totalHours)+" hours</td></tr>"
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>She took "+str(totalHours)+" hours "+item9+" "+str(quantity)+" "+item5+".</td></tr>"
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text +"<br><br>"
        
        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>" 
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 hour</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>$"+str(pay)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>"+str(totalHours)+" hours</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(totalHours)+" &times; $"+str(pay)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>$"+str(totalHours*pay)+"</td></tr>"
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>She earned <b>$"+str(answer)+"</b> for "+item4+" the "+str(quantity)+" "+item5+".</td></tr>"
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        Rita's clock is 30 minutes <slow>.
        Joe's clock is 15 minutes <fast>.
        What is the time shown on Joe's clock?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = [random.choice(PersonName.GirlName),random.choice(PersonName.BoyName)]
        self.StartHour = randint(1,12)
        self.StartMinute = random.randrange(5,55,5)
        self.SlowFastMinutes1 = random.randrange(5,30,5)
        self.SlowFastMinutes2 = random.randrange(5,30,5)
        if self.SlowFastMinutes1 == self.SlowFastMinutes2:
            self.SlowFastMinutes1 = self.SlowFastMinutes1 + 5
            
        self.flag = randint(1,4)
        if self.flag == 1:
            ''' both slow '''
            self.SlowFast1 = "slow"
            self.SlowFast2 = "slow"
            self.EndHour,self.EndMinute = divmod(self.StartHour*60+self.StartMinute+self.SlowFastMinutes1-self.SlowFastMinutes2,60)
            self.ActualHour,self.ActualMinute = divmod((self.StartHour*60+self.StartMinute+self.SlowFastMinutes1),60)
            self.ActualMinute = str(self.ActualMinute)
            self.StartMinute = str(self.StartMinute)
            if len(self.ActualMinute)==1:
                self.ActualMinute = '0'+self.ActualMinute
            if len(self.StartMinute)==1:
                self.StartMinute = '0'+self.StartMinute
        elif self.flag == 2:
            ''' slow fast'''
            self.SlowFast1 = "slow"
            self.SlowFast2 = "fast"
            self.EndHour,self.EndMinute = divmod(self.StartHour*60+self.StartMinute+self.SlowFastMinutes1+self.SlowFastMinutes2,60)
            self.ActualHour,self.ActualMinute = divmod((self.StartHour*60+self.StartMinute+self.SlowFastMinutes1),60)
            self.ActualMinute = str(self.ActualMinute)
            self.StartMinute = str(self.StartMinute)
            if len(self.ActualMinute)==1:
                self.ActualMinute = '0'+self.ActualMinute
            if len(self.StartMinute)==1:
                self.StartMinute = '0'+self.StartMinute
        elif self.flag == 3:
            ''' fast slow'''
            self.SlowFast1 = "fast"
            self.SlowFast2 = "slow"
            self.EndHour,self.EndMinute = divmod(self.StartHour*60+self.StartMinute-self.SlowFastMinutes1-self.SlowFastMinutes2,60)
            self.ActualHour,self.ActualMinute = divmod((self.StartHour*60+self.StartMinute-self.SlowFastMinutes1),60)
            self.ActualMinute = str(self.ActualMinute)
            self.StartMinute = str(self.StartMinute)
            if len(self.ActualMinute)==1:
                self.ActualMinute = '0'+self.ActualMinute
            if len(self.StartMinute)==1:
                self.StartMinute = '0'+self.StartMinute
        elif self.flag == 4:
            ''' fast fast'''
            self.SlowFast1 = "fast"
            self.SlowFast2 = "fast"
            self.EndHour,self.EndMinute = divmod(self.StartHour*60+self.StartMinute-self.SlowFastMinutes1+self.SlowFastMinutes2,60)            
            self.ActualHour,self.ActualMinute = divmod((self.StartHour*60+self.StartMinute-self.SlowFastMinutes1),60)
            self.ActualMinute = str(self.ActualMinute)
            self.StartMinute = str(self.StartMinute)
            if len(self.ActualMinute)==1:
                self.ActualMinute = '0'+self.ActualMinute
            if len(self.StartMinute)==1:
                self.StartMinute = '0'+self.StartMinute
        
        if self.StartHour > 12:
            self.StartHour = self.StartHour - 12
            self.AMPMStart = "p.m."
        elif self.StartHour == 12:
            self.AMPMStart = "p.m."
        else:
            self.AMPMStart = "a.m."
        
        if self.ActualHour > 12:
            self.ActualHour = self.ActualHour - 12
            self.AMPMActual = "p.m."
        elif self.ActualHour == 12:
            self.AMPMActual = "p.m."
        elif self.ActualHour == 0:
            self.ActualHour = 12
            self.AMPMEnd = "a.m."
        else:
            self.AMPMActual = "a.m."

        if self.EndHour > 12:
            self.EndHour = self.EndHour - 12
            self.AMPMEnd = "p.m."
        elif self.EndHour == 12:
            self.AMPMEnd = "p.m."
        elif self.EndHour == 0:
            self.EndHour = 12
            self.AMPMEnd = "a.m."
        else:
            self.AMPMEnd = "a.m."
            
        self.EndMinute = str(self.EndMinute)
        if len(self.EndMinute)==1:
            self.EndMinute = '0'+self.EndMinute       
        
        self.problem = "<div>%s's clock is %d minutes %s.<br>"%(self.names[0],self.SlowFastMinutes1,self.SlowFast1)
        self.problem = self.problem + "%s's clock is %d minutes %s.<br>"%(self.names[1],self.SlowFastMinutes2,self.SlowFast2)
        self.problem = self.problem + "What is the time shown on %s's clock?<br><br>"%(self.names[1])
        self.problem = self.problem + "(Write your answer as in the example. E.g.: 2.35)</div>"
        self.problem = self.problem + "<div style='display:inline-block;margin-left:40px;margin-top:30px;'><font style='color:blue';>"+self.names[0]+"'s clock</font></div>"
        self.problem = self.problem + "<div style='display:inline-block;margin-left:120px;margin-top:30px;'><font style='color:blue';>"+self.names[1]+"'s clock</font></div>"
        self.FunctionCall = "DrawClock1("+str(self.StartHour)+","+str(self.StartMinute)+")"
        self.answer = "%d.%s"%(self.EndHour,self.EndMinute)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "DrawClocks.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.flag,self.names,self.StartHour,self.StartMinute,self.ActualHour,self.ActualMinute,self.EndHour,self.EndMinute,self.SlowFastMinutes1,self.SlowFastMinutes2,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit,'FunctionCall':self.FunctionCall}

    def ExplainType4(self,problem,answer,flag,names,StartHour,StartMinute,ActualHour,ActualMinute,EndHour,EndMinute,SlowFastMinutes1,SlowFastMinutes2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        Option1: (slow, slow)
        The time shown on Rita's clock is 9.35.

        9.35 + 30 min = 10.05        | Rita's clock is 30 minutes behind the actual time. |
        The actual time is 10.05.
        
        10.05 - 15 min = 9.50    | Joe's clock is 15 minutes behind the actual time. |

        The time shown on Joe's clock is 9.50.
        ===
        
        Option 2: (slow, fast)
        The time shown on Rita's clock is 9.35.
        
        9.35 + 30 min = 10.05        | Rita's clock is 30 minutes behind the actual time. |
        The actual time is 10.05.
        
        10.05 + 15 min = 10.20    | Joe's clock is 15 minutes ahead of the actual time. |
        The time shown on Joe's clock is 10.20.
        ===        

        Option 3: (fast, slow)
        The time shown on Rita's clock is 9.35.
        
        9.35 - 30 min = 9.05        | Rita's clock is 30 minutes ahead of the actual time. |
        The actual time is 9.05.
        
        9.05 - 15 min = 8.50    | Joe's clock is 15 minutes behind the actual time. |
        The time shown on Joe's clock is 9.05.
        ===
        
        Option 4: (fast, fast)
        The time shown on Rita's clock is 9.35.
        
        9.35 - 30 min = 9.05        | Rita's clock is 30 minutes ahead of the actual time. |
        The actual time is 9.05.
        
        9.05 + 15 min = 9.20    | Joe's clock is 15 minutes ahead of the actual time. |
        The time shown on Joe's clock is 9.20.
        '''
        
        if flag==1:
            self.solution_text = "<br><font class='ExplanationFont'>The time shown on %s's clock is %d.%s.</font><br><br>"%(names[0],StartHour,StartMinute)
            self.solution_text = self.solution_text + "<div class='side'><font style='font-size:12px'>%s's clock is %d minutes behind the actual time.</font></div>"%(names[0],SlowFastMinutes1)            
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(SlowFastMinutes1)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(ActualHour)+"."+str(ActualMinute)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the actual time is %d.%s.<br></font>"%(ActualHour,str(ActualMinute))
            self.solution_text = self.solution_text + "<br><br><div class='side'><font style='font-size:12px'>%s's clock is %d minutes behind the actual time.</font></div>"%(names[1],SlowFastMinutes2)
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(SlowFastMinutes2)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(ActualHour)+"."+str(ActualMinute)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the time shown on %s's clock is <b>%d.%s</b>.</font><br>"%(names[1],EndHour,EndMinute)
        elif flag==2:
            self.solution_text = "<br><font class='ExplanationFont'>The time shown on %s's clock is %d.%s.</font><br><br>"%(names[0],StartHour,StartMinute)
            self.solution_text = self.solution_text + "<div class='side'><font style='font-size:12px'>%s's clock is %d minutes behind the actual time.</font></div>"%(names[0],SlowFastMinutes1)            
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(SlowFastMinutes1)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(ActualHour)+"."+str(ActualMinute)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the actual time is %d.%s.</font><br>"%(ActualHour,str(ActualMinute))
            self.solution_text = self.solution_text + "<br><br><div class='side'><font style='font-size:12px'>%s's clock is %d minutes ahead of the actual time.</font></div>"%(names[1],SlowFastMinutes2)
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(ActualHour)+"."+str(ActualMinute)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(SlowFastMinutes2)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the time shown on %s's clock is <b>%d.%s</b>.</font><br>"%(names[1],EndHour,EndMinute)
        elif flag==3:
            self.solution_text = "<br><font class='ExplanationFont'>The time shown on %s's clock is %d.%s.</font><br><br>"%(names[0],StartHour,StartMinute)
            self.solution_text = self.solution_text + "<div class='side'><font style='font-size:12px'>%s's clock is %d minutes ahead of the actual time.</font></div>"%(names[0],SlowFastMinutes1)            
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(ActualHour)+"."+str(ActualMinute)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(SlowFastMinutes1)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the actual time is %d.%s.</font><br>"%(ActualHour,str(ActualMinute))
            self.solution_text = self.solution_text + "<br><br><div class='side'><font style='font-size:12px'>%s's clock is %d minutes behind the actual time.</font></div>"%(names[1],SlowFastMinutes2)
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(SlowFastMinutes2)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(ActualHour)+"."+str(ActualMinute)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the time shown on %s's clock is <b>%d.%s</b>.</font><br>"%(names[1],EndHour,EndMinute)
        elif flag==4:
            self.solution_text = "<br><font class='ExplanationFont'>The time shown on %s's clock is %d.%s.</font><br><br>"%(names[0],StartHour,StartMinute)
            self.solution_text = self.solution_text + "<div class='side'><font style='font-size:12px'>%s's clock is %d minutes ahead of the actual time.</font></div>"%(names[0],SlowFastMinutes1)            
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(ActualHour)+"."+str(ActualMinute)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(SlowFastMinutes1)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the actual time is %d.%s.</font><br>"%(ActualHour,str(ActualMinute))
            self.solution_text = self.solution_text + "<br><br><div class='side'><font style='font-size:12px'>%s's clock is %d minutes ahead of the actual time.</font></div>"%(names[1],SlowFastMinutes2)
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(ActualHour)+"."+str(ActualMinute)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(SlowFastMinutes2)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>So, the time shown on %s's clock is <b>%d.%s</b>.</font><br>"%(names[1],EndHour,EndMinute)

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        [Person.Unclename] is <a plumber>.
        <He takes> 45 minutes< to repair a sink pipe>.
        He is paid $30 an hour.
        <He was called to an office building to repair> 8 <sink pipes>.
        How much did he receive for <repairing the> 8 <sink pipes>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [
                        ['a plumber','He takes',' to repair a sink pipe','He was called to an office building to repair','sink pipes','repairing the','sink pipes',random.choice([[30,4],[30,6],[30,8],[40,3],[40,6],[40,9],[45,4],[45,8],[50,6]]),random.randrange(25,40,5),'pipe','to repair','pipes'],
                        ['an air conditioning service contractor','He takes',' to service an air conditioning unit','He serviced','air conditioning units at a school','servicing the','air conditioning units',random.choice([[15,8],[30,4],[30,6],[30,8],[40,3],[40,6],[40,9]]),random.randrange(40,80,5),'unit','to service','units'],
                        ['a mattress cleaning professional','He takes',' to clean a mattress','He cleaned','mattresses at a hotel','cleaning the','mattresses',random.choice([[30,4],[30,6],[30,8],[40,3],[40,6],[40,9],[45,4],[45,8],[50,6]]),random.randrange(40,80,5),'mattress','to clean','mattresses'],
                        ['a part-time swimming instructor','Each of his lessons is',' long','Last week, he gave','such lessons','those','lessons',random.choice([[30,4],[30,6],[30,8],[40,3],[40,6],[40,9],[45,4],[45,8],[50,6]]),random.randrange(30,50,5),'lesson','to give','lessons'],
                        ['a fitness trainer','Each of his training sessions lasts','','Yesterday, he conducted','such sessions','those','sessions',random.choice([[30,4],[30,6],[30,8],[40,3],[40,6],[40,9],[45,4],[45,8],[50,6]]),random.randrange(40,75,5),'session','to conduct','sessions'],
                        ['a balloon sculptor','He spends',' at a balloon sculpting session','Last weekend, he delivered','such sessions','delivering those','sessions',random.choice([[30,4],[30,6],[30,8],[40,3],[40,6],[40,9],[45,4],[45,8],[50,6]]),random.randrange(25,50,5),'session','to deliver','sessions']
                    ]
        
        self.item = random.choice(self.items)
        
        self.minutes = self.item[7][0]
        self.quantity = self.item[7][1]
        self.pay = self.item[8]
        
        self.totalHours = self.minutes*self.quantity/60
        
        self.problem = "%s is %s.<br>"%(self.name,self.item[0])
        self.problem = self.problem + "%s %d minutes%s.<br>"%(self.item[1],self.minutes,self.item[2])
        self.problem = self.problem + "He is paid $%d an hour.<br>"%(self.pay)
        self.problem = self.problem + "%s %d %s.<br>"%(self.item[3],self.quantity,self.item[4])
        self.problem = self.problem + "How much did he receive for %s %d %s?"%(self.item[5],self.quantity,self.item[6])
        
        self.answer = self.minutes*self.quantity*self.pay/60
                   
        self.unit = ""
        self.dollar_unit = "$"
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.totalHours,self.minutes,self.quantity,self.pay,self.item[5],self.item[6],self.item[9],self.item[10],self.item[11],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,totalHours,minutes,quantity,pay,item5,item6,item9,item10,item11,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        1 pipe   -> 45 min            | 60 min = 1 h
        8 pipes  -> 8 &times; 45 min  | 360 min = ?
              = 360 min               | Think of the times table of 6.
              = 6 h                   | 6 &times; 6 = 36
                                      | So, 6 &times; 60 = 360 min = 6 h
        He took 6 hours to repair 8 pipes.
        
        1 h -> $30
        6 h -> 6 &times; $30
             = $180
        He received $180 for repairing the 8 pipes.
        '''
        self.solution_text = "<div class='side'><font style='font-size:12px'>60 min = 1 h<br>"+str(totalHours*60)+" min = ? <br>Think of the times table of 6.<br><b>"+str(totalHours)+"</b> &times; 6 = "+str(totalHours*6)+"<br>So, <b>"+str(totalHours)+"</b> &times; 60 min = "+str(totalHours*60)+" min = <b>"+str(totalHours)+" h</b></font></div>"
        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 "+item9+"</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>"+str(quantity)+" "+item11+"</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(quantity)+" &times; "+str(minutes)+" min</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>"+str(minutes*quantity)+" minutes</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>"+str(totalHours)+" hours</td></tr>"
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>He took "+str(totalHours)+" hours "+item10+" "+str(quantity)+" "+item6+".</td></tr>"
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text +"<br><br>"
        
        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>" 
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 hour</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>$"+str(pay)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>"+str(totalHours)+" hours</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(totalHours)+" &times; $"+str(pay)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>$"+str(totalHours*pay)+"</td></tr>"
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>He received <b>$"+str(answer)+"</b> for "+item5+" "+str(quantity)+" "+item6+".</td></tr>"
        self.solution_text = self.solution_text + "</table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        [Person.Girlname] <had a music lesson at> 3.15 p.m.
        <The lesson lasted> 1 h 55 min<.>
        <She arrived home> 2 h 20 min <after the lesson.>
        <At what time did she arrive home?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['had a music lesson at school at','The lesson lasted','.','She arrived home',' after the lesson.','At what time did she arrive home?',randint(8,14),randint(1,2),randint(1,4),'She spent','at school and before arriving home.','She arrived home at'],
                        ['started doing her homework at','She took',' to do her homework.','Then she watched a TV show for','.','At what time did she finish watching the show?',randint(8,14),randint(2,3),1,'She spent','doing her homework and watching the TV show.','She finished watching the show at'],
                        ['and her mother arrived at a mall at','They shopped for','.','Then they went to watch a movie that lasted','.','At what time did the movie end?',randint(11,14),randint(1,2),randint(1,2),'They spent','shopping and watching the movie.','The movie ended at'],
                        ['and her family left home to visit a zoo at','They arrived at the zoo after','.','Then they spent',' at the zoo.','At what time did they come out of the zoo?',randint(9,11),1,randint(3,5),'They spent','altogether.','They came out of the zoo at'],
                        ['started making some bookmarks at','She took',' to make the bookmarks.','Then she spent',' packing the bookmarks.','At what time did she finish packing the bookmarks?',randint(8,11),randint(1,4),1,'She spent','making and packing the bookmarks.','She finished packing the bookmarks at'],
                        ['made some cupcakes at home at','She took',' to pack the cupcakes.','Then she went out to sell the cupcakes and returned home after','.','At what time did she return home?',randint(8,14),1,randint(2,3),'She spent','packing and selling the cupcakes.','She returned home at']
                    ]
        
        self.item = random.choice(self.items)
        
        self.StartHour = self.item[6]
        self.StartMinute = random.randrange(10,55,5)
        self.hour1 = self.item[7]
        self.minutes1 = random.randrange(10,55,5)
        self.hour2 = self.item[8]
        self.minutes2 = random.randrange(10,55,5)
        
        self.TotalMinutes1 = self.hour1*60+self.minutes1
        self.TotalMinutes2 = self.hour2*60+self.minutes2
        
        self.EndHour,self.EndMinute = divmod(self.StartHour*60+self.StartMinute+self.TotalMinutes1+self.TotalMinutes2,60)
        #explanation
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
            
        self.EndMinute = str(self.EndMinute)
        if len(self.EndMinute)==1:
            self.EndMinute = '0'+self.EndMinute       
        
        self.problem = "%s %s %d.%d %s<br>"%(self.name,self.item[0],self.StartHour,self.StartMinute,self.AMPMStart)
        self.problem = self.problem + "%s %d h %d min%s<br>"%(self.item[1],self.hour1,self.minutes1,self.item[2])
        self.problem = self.problem + "%s %d h %d min %s<br>%s"%(self.item[3],self.hour2,self.minutes2,self.item[4],self.item[5])
        
        self.answer = "%d.%s %s"%(self.EndHour,self.EndMinute,self.AMPMEnd)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.OriginalStartHour,self.hour1,self.hour2,self.minutes1,self.minutes2,self.StartHour,self.StartMinute,self.AMPMStart,self.EndHour,self.EndMinute,self.AMPMEnd,self.item[9],self.item[10],self.item[11],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,OriginalStartHour,hour1,hour2,minutes1,minutes2,StartHour,StartMinute,AMPMStart,EndHour,EndMinute,AMPMEnd,item9,item10,item11,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        1 h 55 min + 2 h 20 min = 4 h 15 min
        She spent 4 h 15 min altogether.
        
                   4 h              15 min
        3.15 p.m. ----->  7.15 p.m. ----->  7.30 p.m.
        She arrived home at 7.30 p.m.
        '''
        totalTimeSpent = hour1*60+hour2*60+minutes1+minutes2
        totalHr,totalMin = divmod(totalTimeSpent,60)
        self.solution_text = "<font class='ExplanationFont'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;+&nbsp; "+str(hour2)+" h "+str(minutes2)+"mine &nbsp;=&nbsp; "+str(totalHr)+" h "+str(totalMin)+" min</font>"
        self.solution_text = self.solution_text + "<br>"
        if totalMin == 0:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"+item9+" "+str(totalHr)+" hours "+item10+"</font>"
        else:
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"+item9+" "+str(totalHr)+" h "+str(totalMin)+" min "+item10+"</font>"
        self.solution_text = self.solution_text + "<br><br>"
        
        if totalMin == 0:
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+" "+str(AMPMStart)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(totalHr)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+" "+str(AMPMEnd)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
        else:
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+" "+str(AMPMStart)+"</td>"
            hours = self.Convert24HrsTo12Hrs(OriginalStartHour+totalHr)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(totalHr)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(StartMinute)+" "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(totalMin)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+" "+str(AMPMEnd)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"

        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"+item11+" <b>"+str(EndHour)+"."+str(EndMinute)+" "+str(AMPMEnd)+"</b></font>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:       
            [Person.Boyname] <went to a library.>
            <He spent> 1 h 40 min <in the children's section.>
            <Then he spent another> 45 minutes <in the multimedia section.>
            <He came out of the multimedia section at> 5.30 p.m.
            <At what time did he enter the children's section?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                        ['went to a library.','He spent','in the children\'s section.','Then he spent another','in the multimedia section.','He came out of the multimedia section at','At what time did he enter the children\'s section?',randint(1,3),randint(13,20),'altogether','He entered the children\'s section at '],
                        ['went to a gym.','He spent','on various exercise machines.','Then he spent another','swimming.','He finished swimming at','At what time did he start exercising on the machines?',1,randint(9,21),'altogether','He started exercising on the machines at '],
                        ['went to a beach.','He spent','playing beach volleyball.','Then he spent another','playing frisbee.','He finished playing frisbee at','At what time did he start playing beach volleyball?',randint(1,2),randint(12,18),'playing volleyball and frisbee','He started playing beach volleyball at '],
                        ['went to a park.','He spent','cycling.','Then he spent another','roller skating.','He finished roller skating at','At what time did he start cycling?',randint(1,2),randint(10,20),'cycling and roller skating','He started cycling at '],
                        ['went to a sports complex.','He spent','ice skating.','Then he spent another','bowling.','He finished bowling at','At what time did he start ice skating?',randint(1,2),randint(14,20),'ice skating and bowling','He started ice skating at '],
                        ['boarded a train.','The train ride was','long.','Then he got off the train and waited','for his next train.','The next train arrived at','At what time did he board the first train?',randint(3,10),randint(12,23),'riding the first train and waiting for the next train','He boarded the first train at ']
                    ]
        
        self.item = random.choice(self.items)
        
        self.EndHour = self.item[8]
        self.EndMinute = random.randrange(10,55,5)
        self.hour1 = self.item[7]
        self.minutes1 = random.randrange(10,55,5)
        self.minutes2 = random.randrange(30,55,5)
        
        self.TotalMinutes1 = self.hour1*60+self.minutes1
        self.TotalMinutes2 = self.minutes2
        
        self.StartHour,self.StartMinute = divmod(self.EndHour*60+self.EndMinute-self.TotalMinutes1-self.TotalMinutes2,60)
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
            
        self.StartMinute = str(self.StartMinute)
        if len(self.StartMinute)==1:
            self.StartMinute = '0'+self.StartMinute       
        
        self.problem = "%s %s<br>"%(self.name,self.item[0])
        self.problem = self.problem + "%s %d h %d min %s<br>"%(self.item[1],self.hour1,self.minutes1,self.item[2])
        self.problem = self.problem + "%s %d minutes %s<br>"%(self.item[3],self.minutes2,self.item[4])
        self.problem = self.problem + "%s %d.%d %s<br>%s"%(self.item[5],self.EndHour,self.EndMinute,self.AMPMEnd,self.item[6])
        
        self.answer = "%d.%s %s"%(self.StartHour,self.StartMinute,self.AMPMStart)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.hour1,self.minutes1,self.minutes2,self.OriginalStartHour,self.StartHour,self.StartMinute,self.AMPMStart,self.EndHour,self.EndMinute,self.AMPMEnd,self.item[9],self.item[10],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,hour1,minutes1,minutes2,OriginalStartHour,StartHour,StartMinute,AMPMStart,EndHour,EndMinute,AMPMEnd,item9,item10,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        1 h 40 min + 45 min = 2 h 25 min
        He spent 2 h 25 min in the library.
        
               25 min           2h
        3.05 p.m. <-----  3.30 p.m. <----  5.30 p.m.
        He entered the children's section at 3.05 p.m.
        '''
        totalTimeSpent = hour1*60+minutes1+minutes2
        totalHr,totalMin = divmod(totalTimeSpent,60)
        if totalMin == 0:
            self.solution_text = "<font class='ExplanationFont'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;+&nbsp; "+str(minutes2)+" min &nbsp;=&nbsp; "+str(totalHr)+" h</font>"
            self.solution_text = self.solution_text + "<br>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>He spent "+str(totalHr)+" h "+item9+".</font>"
            self.solution_text = self.solution_text + "<br><br>"
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+" "+str(AMPMStart)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(totalHr)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+" "+str(AMPMEnd)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
        else:
            self.solution_text = "<font class='ExplanationFont'>"+str(hour1)+" h "+str(minutes1)+" min &nbsp;+&nbsp; "+str(minutes2)+" min &nbsp;=&nbsp; "+str(totalHr)+" h "+str(totalMin)+" min</font>"
            self.solution_text = self.solution_text + "<br>"
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>He spent "+str(totalHr)+" h "+str(totalMin)+" min "+item9+".</font>"
            self.solution_text = self.solution_text + "<br><br>"
            self.solution_text = self.solution_text + "<table border=0><tr>"
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+" "+str(AMPMStart)+"</td>"
            if int(StartMinute)+totalMin<60:
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(totalMin)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(int(StartMinute)+int(totalMin))+" "+str(AMPMStart)+"</td>"
            elif int(StartMinute)+totalMin==60:
                hours = self.Convert24HrsTo12Hrs(OriginalStartHour+1)
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(totalMin)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            else:
                hours = self.Convert24HrsTo12Hrs(OriginalStartHour+1)
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(60-int(StartMinute))+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
                self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(totalMin-60+int(StartMinute))+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+str(EndMinute)+" "+str(hours[1])+"</td>"

            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(totalHr)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+" "+str(AMPMEnd)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
        
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"+item10+" <b>"+str(StartHour)+"."+str(StartMinute)+" "+str(AMPMStart)+"</b></font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        [Person.Girlname] <took> 7 mintues <to make an animal mask.>
        <She made> 15 <such animal masks for a craft project.>
        <She started making them at> 11.30 a.m.
        <At what time did she finish making all the animal masks?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['took','to make an animal mask.','She made','such animal masks for a craft project.','She started making them at','At what time did she finish making all the animal masks?',randint(3,9),randint(10,25),randint(8,19),'mask','to make all the masks','She finished making all the masks at'],
                        ['took','to cycle once around a field.','She cycled','times around the field.','She started cycling at','At what time did she finish cycling?',randint(11,20),randint(4,7),randint(6,20),'round','to cycle all the rounds','She finished cycling all the rounds at'],
                        ['spent','painting a poster.','She painted','such posters for a carnival spending the same amount of time on each poster.','She started painting the posters at','At what time did she finish painting them?',randint(11,20),randint(4,7),randint(8,20),'poster','to paint all the posters','She finished painting all the posters at'],
                        ['spent','making a lantern.','She made','such lanterns for a festival.','She started making the lanterns at','At what time did she finish making all the lanterns?',randint(4,7),randint(11,20),randint(10,19),'lantern','to make all the lanterns','She finished making all the lanterns at'],
                        ['took','to pot a plant.','She potted','plants spending the same amount of time on each plant.','She started potting the plants at','At what time did she finish potting all of them?',randint(4,7),randint(11,20),randint(8,16),'plant','to pot all the plants','She finished potting all the plants at'],
                        ['spent','playing at each station at a video game parlour.','She visited','stations at the parlour.','She started playing at','At what time did she finish playing?',randint(3,5),randint(11,20),randint(11,20),'station','to visit all the stations','She finished playing at']
                    ]
        
        self.item = random.choice(self.items)
        
        self.minutes1 = self.item[6]
        self.quantity = self.item[7]
        self.StartHour = self.item[8]
        self.StartMinute = random.randrange(10,55,5)
        
        self.TotalMinutes1 = self.minutes1*self.quantity
        
        self.EndHour,self.EndMinute = divmod(self.StartHour*60+self.StartMinute+self.TotalMinutes1,60)
        
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
            
        self.EndMinute = str(self.EndMinute)
        if len(self.EndMinute)==1:
            self.EndMinute = '0'+self.EndMinute       
        
        self.problem = "%s %s %d minutes %s<br>"%(self.name,self.item[0],self.minutes1,self.item[1])
        self.problem = self.problem + "%s %d %s<br>"%(self.item[2],self.quantity,self.item[3])
        self.problem = self.problem + "%s %d.%d %s<br>%s"%(self.item[4],self.StartHour,self.StartMinute,self.AMPMStart,self.item[5])
        
        self.answer = "%d.%s %s"%(self.EndHour,self.EndMinute,self.AMPMEnd)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.StartHour,self.StartMinute,self.AMPMStart,self.EndHour,self.EndMinute,self.AMPMEnd,self.quantity,self.minutes1,self.item[9],self.item[10],self.item[11],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,StartHour,StartMinute,AMPMStart,EndHour,EndMinute,AMPMEnd,quantity,minutes1,item9,item10,item11,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        1 mask   -> 7 min
        15 masks -> 15 &times; 7 min
              = 105 min
              = 1 h 45 min
        She took 1 h 15 min to make all the masks.
        
                    1 h              45 min
        11.30 a.m. -----> 12.30 p.m. -----> 1.15 p.m.
        She finished making all the masks at 1.15 p.m.
        '''
        tempHr,tempMin = divmod(minutes1*quantity,60)
        self.solution_text = "<table class='ExplanationTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 "+item9+"</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(minutes1)+" min</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>"+str(quantity)+" "+item9+"s</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>"+str(quantity)+" &times; "+str(minutes1)+" min</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>"+str(minutes1*quantity)+" min</td></tr>"
        if tempHr > 0:
            if tempMin==0:
                self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>"+str(tempHr)+" h</td></tr>"
            else:
                self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>"+str(tempHr)+" h "+str(tempMin)+" min</td></tr>"
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>"
        if tempHr == 0:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>She took "+str(tempMin)+" minutes "+item10+".</td></tr>"
        elif tempMin==0:
            if tempHr==1:
                self.solution_text = self.solution_text + "<tr><td style='text-align:left'>She took "+str(tempHr)+" hour "+item10+".</td></tr>"
            else:
                self.solution_text = self.solution_text + "<tr><td style='text-align:left'>She took "+str(tempHr)+" hours "+item10+".</td></tr>"
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:left'>She took "+str(tempHr)+" h "+str(tempMin)+" min "+item10+".</td></tr>"
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text +"<br><br>"
        
        if tempMin==0:
            self.solution_text = self.solution_text + "<table border=0><tr><td>&nbsp;</td><td style='text-align:center;padding-bottom:0px'>%d h</td><td>&nbsp;</td></tr>"%(tempHr)
            self.solution_text = self.solution_text + "<tr><td style='padding-left:0px;padding-right:0px;'>%d.%s %s</td><td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow.png' /></td><td style='text-align:left'>%d.%s %s</td></tr></table>"%(StartHour,StartMinute,AMPMStart,EndHour,EndMinute,AMPMEnd)
        elif tempHr==0:
            self.solution_text = self.solution_text + "<table border=0><tr><td>&nbsp;</td><td style='text-align:center;padding-bottom:0px'>%d min</td><td>&nbsp;</td></tr>"%(tempMin)
            self.solution_text = self.solution_text + "<tr><td style='padding-left:0px;padding-right:0px;'>%d.%s %s</td><td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow.png' /></td><td style='text-align:left'>%d.%s %s</td></tr></table>"%(StartHour,StartMinute,AMPMStart,EndHour,EndMinute,AMPMEnd)
        else:
            self.solution_text = self.solution_text + "<table border=0><tr><td>&nbsp;</td><td style='text-align:center;padding-bottom:0px'>%d hr %d min</td><td>&nbsp;</td></tr>"%(tempHr,tempMin)
            self.solution_text = self.solution_text + "<tr><td style='padding-left:0px;padding-right:0px;'>%d.%s %s</td><td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow.png' /></td><td style='text-align:left'>%d.%s %s</td></tr></table>"%(StartHour,StartMinute,AMPMStart,EndHour,EndMinute,AMPMEnd)
        self.solution_text = self.solution_text + "<font class='ExplanationFont'><br>&nbsp;%s <b>%d.%s %s</b></font>"%(item11,EndHour,EndMinute,AMPMEnd)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9a(self):       
        '''e.g.:
        [Person.Boyname] works as a <maths tutor>.
        He is paid $35 an hour.
        The chart below shows the number of hours he spends <tutoring> a week.
        How much does [Person.Boyname] earn in a week?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                        ['maths tutor','tutoring',random.randrange(20,40,5)],
                        ['tennis coach','coaching',random.randrange(20,50,5)],
                        ['gymnastics trainer','working',random.randrange(20,50,5)]
                    ]
        
        self.item = random.choice(self.items)
        
        self.hours = random.choice([[3,3,1,1,1,0,0],[3,2,2,1,1,0,0],[2,2,2,1,1,0,0],[3,1,1,2,1,0,0]])
        self.days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        self.fees = self.item[2]
        random.shuffle(self.hours)
        self.TotalHours = 0
        
        self.problem = "%s works as a %s.<br>"%(self.name,self.item[0])
        self.problem = self.problem + "He is paid $%d an hour.<br>"%(self.fees)
        self.problem = self.problem + "The chart below shows the number of hours he spends %s a week.<br>"%(self.item[1])
        self.problem = self.problem + "How much does %s earn in a week?<br><br>"%(self.name)
        self.problem = self.problem + "<table style='margin-left:20px;'>"
        self.problem = self.problem + "<tr><td style='background-color:pink;'>Days</td>"
        for i in range(len(self.days)):
            self.problem = self.problem + "<td style='background-color:#fff2c9;'>"+self.days[i]+"</td>"
        self.problem = self.problem + "</tr><tr><td style='background-color:pink;'>Hours</td>"
        for j in range(len(self.hours)):
            self.TotalHours = self.TotalHours + self.hours[j]
            if self.hours[j] == 0:
                hour = "off day"
            else:
                hour = str(self.hours[j])
            self.problem = self.problem + "<td style='background-color:#fff2c9;'>"+hour+"</td>"            

        self.problem = self.problem + "</tr></table>"
        
        self.answer = self.TotalHours * self.fees
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9a(self.problem,self.answer,self.hours,self.name,self.TotalHours,self.fees,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9a",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9a(self,problem,answer,hours,name,TotalHours,fees,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        2h + 2h + 3h + 0h + 2h + 0h + 0h = 9h
        Rayan works 9 hours in a week.
        
        1 hour  -> $35
        9 hours -> 9 &times; $35
             = $315
        Rayan earns $315 in a week.
        '''
        self.solution_text = "<table class='ExplanationTable' border=0><tr><td style='text-align:left'>"        
        for j in range(len(hours)-1):
            self.solution_text = self.solution_text +str(hours[j])+" h + "            
        self.solution_text = self.solution_text +str(hours[len(hours)-1])+" h</td>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>"+str(TotalHours)+" h</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+name+" works "+str(TotalHours)+" hours in a week.</td></tr>"
        self.solution_text = self.solution_text+"</table><br>"

        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>1 hour</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>$"+str(fees)+"</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(TotalHours)+" hours</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>"+str(TotalHours)+" &times; $"+str(fees)+"</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>$"+str(TotalHours*fees)+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(name)+" earns <b>$"+str(TotalHours*fees)+"</b> in a week.</td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9b(self):       
        '''e.g.:
        [Person.Girlname] works as a <cashier at a fast food restaurant>.
        She is paid $7 an hour.
        The chart below shows the number of hours she spends working a week.
        How much does [Person.Girlname] earn in a week?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['cashier at a fast food restaurant'],['receptionist'],['salesgirl at a department store']]
        
        self.item = random.choice(self.items)
        
        self.hours = [randint(5,8),randint(5,8),randint(5,8),randint(5,8),randint(5,8),0,0]
        self.days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        self.fees = randint(6,9)
        random.shuffle(self.hours)
        self.TotalHours = 0
        
        self.problem = "%s works as a %s.<br>"%(self.name,self.item[0])
        self.problem = self.problem + "She is paid $%d an hour.<br>"%(self.fees)
        self.problem = self.problem + "The chart below shows the number of hours she spends working a week.<br>"
        self.problem = self.problem + "How much does %s earn in a week?<br><br>"%(self.name)
        self.problem = self.problem + "<table style='margin-left:20px;'>"
        self.problem = self.problem + "<tr><td style='background-color:pink;'>Days</td>"
        for i in range(len(self.days)):
            self.problem = self.problem + "<td style='background-color:#fff2c9;'>"+self.days[i]+"</td>"
        self.problem = self.problem + "</tr><tr><td style='background-color:pink;'>Hours</td>"
        for j in range(len(self.hours)):
            self.TotalHours = self.TotalHours + self.hours[j]
            if self.hours[j] == 0:
                hour = "off day"
            else:
                hour = str(self.hours[j])
            self.problem = self.problem + "<td style='background-color:#fff2c9;'>"+hour+"</td>"            

        self.problem = self.problem + "</tr></table>"
                
        self.answer = self.TotalHours * self.fees
                   
        self.unit = ""
        self.dollar_unit = "$"      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9b(self.problem,self.answer,self.hours,self.name,self.TotalHours,self.fees,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9b",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9b(self,problem,answer,hours,name,TotalHours,fees,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        5h + 8h + 6h + 7h + 8h + 0h + 0h = 34h
        Falaq works 34 hours in a week.
        
        1 hour   -> $7
        34 hours -> 34 &times; $7
             = $238
        Falaq earns $238 in a week.
        '''
        self.solution_text = "<table class='ExplanationTable' border=0><tr><td style='text-align:left'>"        
        for j in range(len(hours)-1):
            self.solution_text = self.solution_text +str(hours[j])+" h + "            
        self.solution_text = self.solution_text +str(hours[len(hours)-1])+" h</td>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>"+str(TotalHours)+" h</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+name+" works "+str(TotalHours)+" hours in a week.</td></tr>"
        self.solution_text = self.solution_text+"</table><br>"

        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>1 hour</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>$"+str(fees)+"</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(TotalHours)+" hours</td><td style='padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td>"+str(TotalHours)+" &times; $"+str(fees)+"</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>$"+str(TotalHours*fees)+"</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(name)+" earns <b>$"+str(TotalHours*fees)+"</b> in a week.</td></tr>"
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:       
            <A flight was scheduled to arrive at the destination at> 5.10 p.m.
            <However, due to bad weather conditions it arrived> 15 minutes <late.>
            <The flight took> 8 h 15 min< to reach the destination.>
            <At what time did it take off from the origin?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                        ['A flight was scheduled to arrive at the destination at','However, due to bad weather conditions it arrived','late.','The flight took',' to reach the destination.','At what time did it take off from the origin?',randint(10,23),randint(3,9),'The flight arrived at the destination at','The flight took off from the origin at'],
                        ['A bus was scheduled to arrive at the destination at','However, due to a traffic jam it arrived','late.','The bus took',' to reach the destination.','At what time did it leave from the origin?',randint(10,23),randint(3,9),'The bus arrived at the destination at','The bus left from the origin at'],
                        ['A guided tour was scheduled to end at','However, it ended','late.','The tour lasted','.','At what time did the tour start?',randint(14,19),randint(2,5),'The tour ended at','The tour started at'],
                        ['A ship from Port A was scheduled to arrive at Port B at','However, because of choppy waters it arrived','late at Port B.','The ship took',' to sail from Port A to Port B.','At what time did it leave Port A?',randint(10,23),randint(3,9),'The ship arrived at Port B at','The ship left Port A at'],
                        ['A cargo train from Station S was scheduled to arrive at Station T at','However, because of a railroad jam it arrived','late at Station T.','The train took',' to travel from Station S to Station T.','At what time did it leave Station S?',randint(10,23),randint(3,9),'The train arrived at Station T at','The train left Station S at'],
                        ['A meeting was scheduled to end at','However, it ended','late.','The meeting lasted','.','At what time did it start?',randint(14,19),randint(2,5),'The meeting ended at','The meeting started at']
                    ]
        
        self.item = random.choice(self.items)
        
        self.EndHour = self.item[6]
        self.EndMinute = random.randrange(10,55,5)
        self.hour1 = self.item[7]
        self.minutes1 = random.randrange(10,55,5)
        self.minutes2 = random.randrange(10,55,5)
        
        self.TotalMinutes1 = self.hour1*60+self.minutes1
        self.TotalMinutes2 = self.minutes2
        
        self.StartHour,self.StartMinute = divmod(self.EndHour*60+self.EndMinute-self.TotalMinutes1+self.TotalMinutes2,60)
        #for explanation
        self.OriginalStartHour = self.StartHour
        self.OriginalEndHour = self.EndHour
        
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
            
        self.StartMinute = str(self.StartMinute)
        if len(self.StartMinute)==1:
            self.StartMinute = '0'+self.StartMinute       
        
        self.problem = "%s %d.%d %s<br>"%(self.item[0],self.EndHour,self.EndMinute,self.AMPMEnd)
        self.problem = self.problem + "%s %d minutes %s<br>"%(self.item[1],self.minutes2,self.item[2])
        self.problem = self.problem + "%s %d h %d min%s<br>%s"%(self.item[3],self.hour1,self.minutes1,self.item[4],self.item[5])
        
        self.answer = "%d.%s %s"%(self.StartHour,self.StartMinute,self.AMPMStart)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.OriginalStartHour,self.OriginalEndHour,self.EndHour,self.EndMinute,self.AMPMEnd,
                                               self.StartHour,self.StartMinute,self.AMPMStart,self.minutes2,self.hour1,self.minutes1,
                                               self.item[8],self.item[9],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,OriginalStartHour,OriginalEndHour,EndHour,EndMinute,AMPMEnd,StartHour,StartMinute,AMPMStart,minutes2,hour1,minutes1,item8,item9,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
                  15 min
        5.10 p.m. -----> 5.25 p.m.
        The flight arrived at the destination at 5.25 p.m.
        
                  15 min            8 h
        9.10 a.m. <---- 9.25 a.m. <---- 5.25 p.m.
        It took off from the origin at 9.10 a.m.

        '''
        self.solution_text = "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+" "+str(AMPMEnd)+"</td>"
        if EndMinute+minutes2<60:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(minutes2)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute+minutes2)+" "+str(AMPMEnd)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
            self.ItermediateTime = str(EndHour)+"."+str(EndMinute+minutes2)+" "+str(AMPMEnd)
        elif EndMinute+minutes2==60:
            hours = self.Convert24HrsTo12Hrs(OriginalEndHour+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(minutes2)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
            self.ItermediateTime = str(hours[0])+".00 "+str(hours[1])
        else:
            hours = self.Convert24HrsTo12Hrs(OriginalEndHour+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(60-EndMinute)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            if len(str(minutes2-60+EndMinute))==1:
                self.ItermediateMinute = '0'+str(minutes2-60+EndMinute)
            else:
                self.ItermediateMinute = str(minutes2-60+EndMinute)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(minutes2-60+EndMinute)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+self.ItermediateMinute+" "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
            self.ItermediateTime = str(hours[0])+"."+self.ItermediateMinute+" "+str(hours[1])
        
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"+item8+" "+self.ItermediateTime+"</font><br><br>"
        
        self.solution_text = self.solution_text + "<table border=0><tr>"
        self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+" "+str(AMPMStart)+"</td>"
        if int(StartMinute)+minutes1<60:
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(minutes1)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(int(StartMinute)+minutes1)+" "+str(AMPMStart)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(hour1)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+self.ItermediateTime+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
        elif int(StartMinute)+minutes1==60:
            hours = self.Convert24HrsTo12Hrs(OriginalStartHour+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(minutes1)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(hour1)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+self.ItermediateTime+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
        else:
            hours = self.Convert24HrsTo12Hrs(OriginalStartHour+1)
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(60-int(StartMinute))+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+".00 "+str(hours[1])+"</td>"
            if len(str(minutes1-60+int(StartMinute)))==1:
                self.ItermediateMinute2 = '0'+str(minutes1-60+int(StartMinute))
            else:
                self.ItermediateMinute2 = str(minutes1-60+int(StartMinute))
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(minutes1-60+int(StartMinute))+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+self.ItermediateMinute2+" "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(hour1)+"h.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+self.ItermediateTime+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
        
        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"+item9+" <b>"+str(StartHour)+"."+str(StartMinute)+" "+str(AMPMStart)+"</b></font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:
        <The time now is> 7.20 a.m.
        [Person.Boyname]<'s watch is> 15 minutes <slow.>
        [Person.Girlname]<'s watch is> 30 minutes <faster than> [Person.Boyname]<'s watch.>
        <What time does> [Person.Girlname]<'s watch show?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = [random.choice(PersonName.BoyName),random.choice(PersonName.GirlName)]
        
        self.items = [
                        ['The time now is',"'s watch is",'slow.',"'s watch is",'faster than',"'s watch.",'What time does',"'s watch show?",randint(1,23),random.randrange(15,45,5),random.randrange(15,45,5),'behind the actual time',"'s watch shows",'ahead of',"'s watch"],
                        ['The music concert started at',' arrived','before the concert started.',' arrived','later than',' at the concert.','At what time did',' arrive at the concert?',randint(18,20),random.randrange(15,45,5),random.randrange(15,45,5),'before the concert started',' arrived at','after',''],
                        ['The karate lesson began at',' came','before the lesson began.',' came','later than',' for the lesson.','At what time did',' come for the lesson?',randint(8,18),random.randrange(5,20,5),random.randrange(10,30,5),'before the lesson began',' came at','after',''],
                        ['The party started at',' came','before the party started.',' came','later than',' to the party.','At what time did',' come to the party?',randint(14,18),random.randrange(5,20,5),random.randrange(10,45,5),'before the party started',' came at','after',''],
                        ['The assignment was due at',' handed in his assignment','before it was due.',' handed in her assignment','later than','.','At what time did',' hand in her assignment?',randint(10,15),random.randrange(5,30,5),random.randrange(30,50,5),'before it was due',' handed in the assignment at','after',''],
                        ['The football game started at',' arrived at the stadium','before the game started.',' arrived at the stadium','later than','.','At what time did',' arrive at the stadium?',randint(10,18),random.randrange(10,30,5),random.randrange(20,40,5),'before the game started',' arrived at','after','']
                    ]
        
        self.item = random.choice(self.items)
        
        self.StartHour = self.item[8]
        self.StartMinute = random.randrange(10,55,5)
        self.minutes1 = self.item[9]
        self.minutes2 = self.item[10]
        if self.minutes1 == self.minutes2:
            self.minutes2 = self.minutes2 + 5
        
        self.EndHour,self.EndMinute = divmod(self.StartHour*60+self.StartMinute-self.minutes1+self.minutes2,60)
        #for explanation
        self.OriginalStartHour = self.StartHour
        self.OriginalEndHour = self.EndHour
        
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
            
        self.EndMinute = str(self.EndMinute)
        if len(self.EndMinute)==1:
            self.EndMinute = '0'+self.EndMinute       
        
        self.problem = "%s %d.%d %s<br>"%(self.item[0],self.StartHour,self.StartMinute,self.AMPMStart)
        self.problem = self.problem + "%s%s %d minutes %s<br>"%(self.names[0],self.item[1],self.minutes1,self.item[2])
        self.problem = self.problem + "%s%s %d minutes %s %s%s<br>"%(self.names[1],self.item[3],self.minutes2,self.item[4],self.names[0],self.item[5])
        self.problem = self.problem + "%s %s%s"%(self.item[6],self.names[1],self.item[7])
        
        self.answer = "%d.%s %s"%(self.EndHour,self.EndMinute,self.AMPMEnd)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.StartHour,self.StartMinute,self.AMPMStart,self.EndHour,
                                               self.EndMinute,self.AMPMEnd,self.minutes1,self.minutes2,self.OriginalStartHour,self.OriginalEndHour,
                                               self.names,self.item[1],self.item[3],self.item[11],self.item[12],self.item[13],self.item[14],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,StartHour,StartMinute,AMPMStart,EndHour,EndMinute,AMPMEnd,minutes1,minutes2,OriginalStartHour,OriginalEndHour,
                      names,item1,item3,item11,item12,item13,item14,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
                  15 min
        7.05 a.m. <----- 7.20 a.m.     | Rayan's watch is 15 minutes behind the actual time. |
        Rayan's watch shows 7.05 a.m.
        
                  30 min
        7.05 a.m. -----> 7.35 a.m.    | Falaq's watch is 30 minutes ahead of Rayan's watch. |
        Falaq's watch shows 7.35 a.m.
        '''
        self.solution_text = "<div class='side'><font style='font-size:12px'>"+names[0]+item1+" "+str(minutes1)+" minutes "+item11+".</font></div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        if StartMinute-minutes1>=0:
            self.IntermediateMinute = str(StartMinute-minutes1)
            if len(self.IntermediateMinute)==1:
                self.IntermediateMinute = '0'+self.IntermediateMinute
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+self.IntermediateMinute+" "+str(AMPMStart)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(minutes1)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+" "+str(AMPMStart)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
            self.ItermediateTime = str(StartHour)+"."+self.IntermediateMinute+" "+str(AMPMStart)
        else:
            self.IntermediateMinute = str(60+StartMinute-minutes1)
            if len(self.IntermediateMinute)==1:
                self.IntermediateMinute = '0'+self.IntermediateMinute
            hours = self.Convert24HrsTo12Hrs(OriginalStartHour-1)
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+str(hours[0])+"."+self.IntermediateMinute+" "+str(hours[1])+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(60-int(self.IntermediateMinute))+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+".00 "+str(AMPMStart)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/left_curved_arrow_"+str(StartMinute)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(StartHour)+"."+str(StartMinute)+" "+str(AMPMStart)+"</td>"            
            self.solution_text = self.solution_text + "</tr></table>"
            self.ItermediateTime = str(hours[0])+"."+self.IntermediateMinute+" "+str(hours[1])

        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"+names[0]+item12+" "+self.ItermediateTime+"</font>"
        
        self.solution_text = self.solution_text + "<br><br><div class='side'><font style='font-size:12px'>"+names[1]+item3+" "+str(minutes2)+" minutes "+item13+" "+names[0]+item14+".</font></div>"
        self.solution_text = self.solution_text + "<table border=0><tr>"
        if int(self.IntermediateMinute)+minutes2<=60:
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+self.ItermediateTime+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(minutes2)+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+" "+str(AMPMEnd)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"
        else:
            self.solution_text = self.solution_text + "<td style='padding-left:0px;padding-right:0px;'>"+self.ItermediateTime+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(60-int(self.IntermediateMinute))+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+".00 "+str(AMPMEnd)+"</td>"
            self.solution_text = self.solution_text + "<td style='padding-right:0px;padding-top:3px;padding-left:0px;padding-right:0px;'><img src='/images/explanation/right_curved_arrow_"+str(minutes2-60+int(self.IntermediateMinute))+"m.png' /></td><td style='padding-left:0px;padding-right:0px;'>"+str(EndHour)+"."+str(EndMinute)+" "+str(AMPMEnd)+"</td>"
            self.solution_text = self.solution_text + "</tr></table>"

        self.solution_text = self.solution_text + "<br><font class='ExplanationFont'>"+names[1]+item12+" <b>"+str(EndHour)+"."+str(EndMinute)+" "+AMPMEnd+"</b></font>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"").lower()
                answer = string.join(str(answer).split(),"")
                if "a" in InputAnswer:
                    InputAnswer1 = InputAnswer.partition("a")[0]
                    '''If answer is 1.00 am then 1 am should also be correct'''
                    if "." not in InputAnswer1 and ":" not in InputAnswer1:
                        InputAnswer1 = InputAnswer1+".00"
                    InputAnswer2 = InputAnswer.partition("a")[1]+InputAnswer.partition("a")[2]
                    if ":" in InputAnswer1:
                        InputAnswer1 = InputAnswer1.partition(":")[0]+"."+InputAnswer1.partition(":")[2]
                    if len(InputAnswer2)<5 and "m" in InputAnswer:
                        InputAnswer2 = "a.m."
                    InputAnswer = InputAnswer1+InputAnswer2
                elif "p" in InputAnswer:
                    InputAnswer1 = InputAnswer.partition("p")[0]
                    if "." not in InputAnswer1 and ":" not in InputAnswer1:
                        InputAnswer1 = InputAnswer1+".00"
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
                if ":" in InputAnswer:
                    InputAnswer = InputAnswer.partition(":")[0]+"."+InputAnswer.partition(":")[2]
                return InputAnswer == answer
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