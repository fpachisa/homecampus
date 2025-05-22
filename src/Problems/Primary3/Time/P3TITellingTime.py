'''
Created on Jun 20, 2013
Module: P3TITellingTime
Generates the Telling Time problems on Time for Primary 3

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

class P3TITellingTime:
    
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
                            9:["ProblemType9",],
                            10:["ProblemType10",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],
                                    5:[self.GenerateProblemType5(),],
                                    6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],
                                    8:[self.GenerateProblemType8(),],
                                    9:[self.GenerateProblemType9(),],
                                    10:[self.GenerateProblemType10(),],
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
        #return self.GenerateProblemType10()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10":self.GenerateProblemType10(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        What is the time in the clock below?
        [Example: Write your answer as 8.40 or 8:40]'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.items = [['P3TTPT1_110','1','10',1],['P3TTPT1_203','2','03',2],['P3TTPT1_320','3','20',1],['P3TTPT1_415','4','15',1],['P3TTPT1_525','5','25',1],['P3TTPT1_630','6','30',1],['P3TTPT1_748','7','48',3],['P3TTPT1_855','8','55',1],['P3TTPT1_937','9','37',3],['P3TTPT1_1008','10','08',3],['P3TTPT1_1123','11','23',3],['P3TTPT1_1242','12','42',3]]

        self.item = random.choice(self.items)
        self.flag = self.item[3]

        self.problem = "What is the time in the clock below?<br>"
        self.problem = self.problem + "[Example: Write your answer as 8.40 or 8:40]<br>"
        self.problem = self.problem + "<img src='/images/P3ProblemImages/"+self.item[0]+".png'>"
        
        self.answer = "%s.%s"%(self.item[1],self.item[2])
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.item[1],self.item[2],self.flag,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,hour,minutes,flag,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:
        
        if minute is a multiple of 5:
            2 &times; 5 minutes = 10 minutes      | There are 5 minutes between two adjacent big markings on the clock.|
            The minute hand shows 10 minutes.
        elif minute is less than 5:
            The minute hand shows 3 minutes.    | Each small marking on the clock stands for 1 minute. |
        else:
            9 &times; 5 minutes = 45 minutes      | Each small marking on the clock stands for 1 minute.   |
            45 + 3    = 48                  | There are 5 minutes between two adjacent big markings. |
            The minute hand shows 48 minutes.
        
        The hour hand is between 1 and 2.
        
        So, the time is 1.10.
        '''
        if flag==1:
            self.solution_text = "<div class='side' style='width:200px;'><font style='font-size:12px'>There are 5 minutes between two adjacent big markings on the clock.</font></div>"
            self.solution_text = self.solution_text + "<br><table border=0>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>%d &times; 5 &nbsp;=&nbsp; %s minutes</td></tr>"%(int(minutes)/5,minutes)
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>The minute hand shows %s minutes.</td></tr>"%(minutes)
            self.solution_text = self.solution_text+"</table>"
            self.solution_text = self.solution_text+"<br>"
        elif flag==2:
            self.solution_text = "<div class='side' style='width:200px;'><font style='font-size:12px'>Each small marking on the clock stands for 1 minute.</font></div>"
            self.solution_text = self.solution_text + "<br><table border=0>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>The minute hand shows %s minutes.</td></tr>"%(minutes)
            self.solution_text = self.solution_text+"</table>"
            self.solution_text = self.solution_text+"<br>"
        else:
            self.solution_text = "<div class='side' style='width:200px;'><font style='font-size:12px'>There are 5 minutes between two adjacent big markings on the clock.<br><br>Each small marking on the clock stands for 1 minute.</font></div>"
            self.solution_text = self.solution_text + "<br><table border=0>"
            tempQ, tempR = divmod(int(minutes),5)
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>%d &times; 5 &nbsp;=&nbsp; %d minutes</td></tr>"%(tempQ,tempQ*5)
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>%d + %d &nbsp;=&nbsp; %s minutes</td></tr>"%(tempQ*5,tempR,int(minutes))
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>The minute hand shows %s minutes.</td></tr>"%(minutes)
            self.solution_text = self.solution_text+"</table>"
            self.solution_text = self.solution_text+"<br>"
            
    
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>The hour hand is between %s and %d.</td></tr>"%(hour,int(hour)+1)
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>So, the time is %s.</td></tr>"%(answer)
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        Fill in the blank with 'past' or 'to'.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)

        self.items = [
                        [' arrives in school at','am','P3TTPT3a',randint(7,11)],
                        ["'s grandfather waters the garden at",'am','P3TTPT3b',randint(6,10)],
                        [' goes to the gym at','am','P3TTPT3c',randint(6,11)],
                        [' goes for a jog at','am','P3TTPT3d',randint(6,8)],
                        [' folds the laundry at','am','P3TTPT3e',randint(8,11)],
                        [' has supper at','pm','P3TTPT3f',randint(8,10)],
                        [' goes to the dance class at','pm','P3TTPT3g',randint(1,7)],
                        [' brushes her teeth at','pm','P3TTPT3h',randint(7,9)],
                        [' and her friends start studying at','pm','P3TTPT3i',randint(3,6)],
                        [' does the dishes at','pm','P3TTPT3j',randint(3,6)]
                    ]
        self.item = random.choice(self.items)
        
        self.flag = randint(1,10)
        
        if self.flag < 4:
            self.hour = str(randint(1,12))
            self.minutes = str(randint(5,30))
            self.minutes1 = self.minutes
            if len(self.minutes1) == 1:
                self.minutes1 = '0'+self.minutes1
            self.problem = "Fill in the blank with 'past' or 'to'.<br><br>"
            self.problem = self.problem + "%s.%s is %s minutes _______ %s."%(self.hour,self.minutes1,self.minutes,self.hour)
        else:
            self.hour = str(self.item[3])
            self.minutes = str(random.randrange(5,30,5))
            self.minutes1 = self.minutes
            if len(self.minutes1) == 1:
                self.minutes1 = '0'+self.minutes1
            self.problem = "<div style='display:inline-block;vertical-align:top;'>Fill in the blank with 'past' or 'to'.<br><br>"
            self.problem = self.problem + "%s %s %s.%s %s.<br><br>"%(self.name,self.item[0],self.hour,self.minutes1,self.item[1])
            self.problem = self.problem + "%s.%s is %s minutes _______ %s.</div>"%(self.hour,self.minutes1,self.minutes,self.hour)
            self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[2]+".png'></div>"
        
        self.answer = "past"
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.hour,self.minutes,self.minutes1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,hour,minutes,minutes1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:

        6.07 is 7 minutes after 6 o'clock.
        So, 6.07 is 7 minutes <b>past</b> 6.
        '''
        self.solution_text = "<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+hour+"."+minutes1+" is "+minutes+" minutes after "+hour+" o'clock.</td></tr>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>So, "+hour+"."+minutes1+" is "+minutes+" minutes <b>"+answer+"</b> "+hour+".</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        Fill in the blank with the correct time. [Example: 5.40 or 5:40.]'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.items = [
                        ['We arrived at the party at','P3TTPT5a',randint(3,9)],
                        ['We arrived at the beach at','P3TTPT5b',randint(1,12)],
                        ['He arrived at work at','P3TTPT5c',randint(6,10)],
                        ['She reached the supermarket at','P3TTPT5d',randint(1,12)],
                        ['I left home at','P3TTPT5e',randint(1,12)],
                        ['I rented the bike at','P3TTPT5f',randint(1,12)],
                        ['I boarded the train at','P3TTPT5g',randint(1,12)],
                        ['The art class ended at','P3TTPT5h',randint(8,12)],
                        ['The dance show began at','P3TTPT5i',randint(1,6)],
                        ['The concert ended at','P3TTPT5j',randint(4,8)]
                        ]
        self.item = random.choice(self.items)
        
        self.flag = randint(1,10)
        
        if self.flag < 4:
            self.hour = str(randint(1,12))
            self.minutes = str(randint(1,30))
            self.problem = "Fill in the blank with the correct time. [Example: 5.40 or 5:40.]<br><br>"
            self.problem = self.problem + "%s minutes past %s is _________."%(self.minutes,self.hour)
        else:
            self.hour = str(self.item[2])
            self.minutes = str(randint(1,30))
            self.problem = "<div style='display:inline-block;vertical-align:top;'>Fill in the blank with the correct time. [Example: 5.40 or 5:40.]<br><br>"
            self.problem = self.problem + "%s %s minutes past %s.<br><br>"%(self.item[0],self.minutes,self.hour)
            self.problem = self.problem + "%s minutes past %s is _________.</div>"%(self.minutes,self.hour)
            self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[1]+".png'></div>"
        
        self.minutes1 = self.minutes
        if len(self.minutes)==1:
            self.minutes1 = '0'+self.minutes
        
        self.answer = "%s.%s"%(self.hour,self.minutes1)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.hour,self.minutes,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,hour,minutes,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:

        15 minutes past 8 is 15 minutes after 8 o'clock.
        So, the time is <b>8.15</b>.
        '''
        self.solution_text = "<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>%s minutes past %s is %s minutes after %s o'clock.</td></tr>"%(minutes,hour,minutes,hour)
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>So, the time is <b>%s</b>.</td></tr>"%(answer)
        self.solution_text = self.solution_text+"</table>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        Find the missing number.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                        ['The bell rang at','P3TTPT7a',randint(6,12)],
                        ['The race began at','P3TTPT7b',randint(6,12)],
                        ['The meeting began at','P3TTPT7c',randint(1,5)],
                        ['The dinner was served at','P3TTPT7d',randint(6,9)],
                        ['The postman came at','P3TTPT7e',randint(8,12)],
                        ['The pizza delivery boy came at','P3TTPT7f',randint(1,12)],
                        ['The exam started at','P3TTPT7g',randint(7,12)],
                        ['I went to see the dentist at','P3TTPT7h',randint(1,6)],
                        ['My interview began at','P3TTPT7i',randint(9,12)],
                        ['I went to bed at','P3TTPT7j',randint(7,10)]
                    ]
        
        self.item = random.choice(self.items)
        
        self.flag = randint(1,10)
        
        if self.flag < 4:
            self.hour = str(randint(1,12))
            self.minutes = str(randint(1,30))
            self.minutes1 = self.minutes
            if len(self.minutes)==1:
                self.minutes1 = '0'+self.minutes
            self.problem = "Find the missing number.<br><br>"
            self.problem = self.problem + "%s.%s is ______ minutes past %s."%(self.hour,self.minutes1,self.hour)
        else:
            self.hour = str(self.item[2])
            self.minutes = str(randint(1,30))
            self.minutes1 = self.minutes
            if len(self.minutes)==1:
                self.minutes1 = '0'+self.minutes            
            self.problem = "<div style='display:inline-block;vertical-align:top;'>Find the missing number.<br><br>"
            self.problem = self.problem + "%s %s.%s.<br><br>"%(self.item[0],self.hour,self.minutes1)
            self.problem = self.problem + "%s.%s is ______ minutes past %s.</div>"%(self.hour,self.minutes1,self.hour)
            self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[1]+".png'></div>"
        
        self.answer = self.minutes
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.hour,self.minutes,self.minutes1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,hour,minutes,minutes1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation: (accept answer in numerals and words)

        6.15 is 15 minutes after 6 o'clock.
        So, 6.15 is <b>15</b> minutes past 6.
        '''
        self.solution_text = "<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>%s.%s is %s minutes after %s o'clock.</td></tr>"%(hour,minutes1,minutes,hour)
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>So, %s.%s is <b>%s</b> minutes past %s.</td></tr>"%(hour,minutes1,minutes,hour)
        self.solution_text = self.solution_text+"</table>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):
        '''e.g.:
        Find the missing number.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                        ['am when I reached the coffee shop.','P3TTPT9a',randint(6,11)],
                        ['am when we boarded the tram.','P3TTPT9b',randint(6,11)],
                        ['am when the shopkeeper opened the shop.','P3TTPT9c',randint(6,11)],
                        ['am when the milkman arrived.','P3TTPT9d',randint(6,11)],
                        ['am when the phone rang.','P3TTPT9e',randint(6,11)],
                        ['pm when my brother returned home.','P3TTPT9f',random.choice([12,1,2,3,4,5])],
                        ['pm when the doorbell rang.','P3TTPT9g',random.choice([12,1,2,3,4,5])],
                        ['pm when the stage show began.','P3TTPT9h',random.choice([12,1,2,3,4,5])],
                        ['pm when the dance show ended.','P3TTPT9i',random.choice([12,1,2,3,4,5])],
                        ['pm when the gates were closed.','P3TTPT9j',random.choice([12,1,2,3,4,5])]
                    ]
        
        self.item = random.choice(self.items)
        
        self.flag = randint(1,10)
        
        if self.flag < 4:
            self.hour = randint(1,12)
            self.minutes = randint(31,58)
            if self.hour == 12:
                self.hour1 = 1
            else:
                self.hour1 = self.hour + 1
            self.problem = "Find the missing number.<br><br>"
            self.problem = self.problem + "%d.%d is ______ minutes to %d."%(self.hour,self.minutes,self.hour1)
        else:
            self.hour = self.item[2]
            self.minutes = randint(31,58)
            if self.hour == 12:
                self.hour1 = 1
            else:
                self.hour1 = self.hour + 1            
            self.problem = "<div style='display:inline-block;vertical-align:top;'>Find the missing number.<br><br>"
            self.problem = self.problem + "It was %d.%d %s<br><br>"%(self.hour,self.minutes,self.item[0])
            self.problem = self.problem + "%d.%d is ______ minutes to %d.</div>"%(self.hour,self.minutes,self.hour1)
            self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[1]+".png'></div>"
        
        self.answer = 60 - self.minutes
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.hour,self.hour1,self.minutes,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,hour,hour1,minutes,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:

        6.45 is 15 minutes before 7 o'clock.      | 1 hour = 60 min        |
        So, 6.45 is <b>15</b> minutes to 7.      | 60 min - 45 min = 15 min |
        '''
        self.solution_text = "<div class='side' style='width:155px;'><font style='font-size:12px'>1 hour &nbsp;=&nbsp; 60 min<br>60 min &nbsp;&minus;&nbsp; %d min &nbsp;=&nbsp; %d min</font></div>"%(minutes,answer)
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>%d.%d is %d minutes before %d o'clock.</td></tr>"%(hour,minutes,answer,hour1)
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>So, %d.%d is <b>%d</b> minutes to %d.</td></tr>"%(hour,minutes,answer,hour1)
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        Rayan's school van picks him up at the time shown below.
        At what time does the van pick up Rayan?
        <image of clock>
        [Example: Write your answer as 8.40 or 8:40]'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)

        self.items = [
                        ["'s school van picks him up",' the van pick up','',random.choice([['P3TTPT2a_615','6','15'],['P3TTPT2a_725','7','25'],['P3TTPT2a_835','8','35'],['P3TTPT2a_945','9','45'],['P3TTPT2a_1155','11','55']]),'The van picks him up at'],
                        [' has his dinner','',' have dinner',random.choice([['P3TTPT2b_640','6','40'],['P3TTPT2b_650','6','50'],['P3TTPT2b_710','7','10'],['P3TTPT2b_720','7','20'],['P3TTPT2b_730','7','30']]),'He has his dinner at'],
                        [' goes to the playground','',' go to the playground',random.choice([['P3TTPT2c_430','4','30'],['P3TTPT2c_440','4','40'],['P3TTPT2c_455','4','55'],['P3TTPT2c_515','5','15'],['P3TTPT2c_520','5','20']]),'He goes to the playground at'],
                        ["'s gymnastics class begins",'',"'s gymnastics class begin", random.choice([['P3TTPT2d_210','2','10'],['P3TTPT2d_220','2','20'],['P3TTPT2d_225','2','25'],['P3TTPT2d_335','3','35'],['P3TTPT2d_350','3','50']]),'His gymnastics class begins at'],
                        [' goes for a swim','',' go for a swim', random.choice([['P3TTPT2e_105','1','05'],['P3TTPT2e_110','1','10'],['P3TTPT2e_1215','12','15'],['P3TTPT2e_1235','12','35'],['P3TTPT2e_1250','12','50']]),'He goes for a swim at'],
                        [' goes cycling','',' go cycling', random.choice([['P3TTPT2f_815','8','15'],['P3TTPT2f_845','8','45'],['P3TTPT2f_910','9','10'],['P3TTPT2f_935','9','35'],['P3TTPT2f_1020','10','20']]),'He goes cycling at'],
                        [' starts doing his homework','',' start doing his homework', random.choice([['P3TTPT2g_745','7','45'],['P3TTPT2g_310','3','10'],['P3TTPT2g_355','3','55'],['P3TTPT2g_420','4','20'],['P3TTPT2g_435','4','35']]),'He starts doing his homework at'],
                        [' packs his schoolbag','',' pack his schoolbag', random.choice([['P3TTPT2h_1005','10','05'],['P3TTPT2h_1015','10','15'],['P3TTPT2h_1035','10','35'],['P3TTPT2h_1110','11','10'],['P3TTPT2h_1120','11','20']]),'He packs his schoolbag at'],
                        [' wakes up','',' wake up', random.choice([['P3TTPT2i_600','6','00'],['P3TTPT2i_630','6','30'],['P3TTPT2i_645','6','45'],['P3TTPT2i_700','7','00'],['P3TTPT2i_730','7','30']]),'He wakes up at'],
                        [' goes to bed','',' goes to bed', random.choice([['P3TTPT2j_830','8','30'],['P3TTPT2j_845','8','45'],['P3TTPT2j_900','9','00'],['P3TTPT2j_915','9','15'],['P3TTPT2j_930','9','30']]),'He goes to bed at']
                    ]

        self.item = random.choice(self.items)

        self.problem = "%s%s at the time shown below.<br>"%(self.name,self.item[0])
        self.problem = self.problem + "At what time does%s %s%s?<br>"%(self.item[1],self.name,self.item[2])
        self.problem = self.problem + "[Example: Write your answer as 8.40 or 8:40]<br>"
        self.problem = self.problem + "<img src='/images/P3ProblemImages/"+self.item[3][0]+".png'>"
        
        self.answer = "%s.%s"%(self.item[3][1],self.item[3][2])
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.item[3][1],self.item[3][2],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,hour,minutes,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        '''
        Explanation:

        8 &times; 5 minutes = 40 minutes     | There are 5 minutes between each adjacent pair of numbers. |
        The minute hand shows 40 minutes.    
        
        The hour hand is between 8 and 9.
        
        So, the time is 8.40.
        
        The van picks up Rayan at 8.40.
        '''
        if int(minutes)==0:
            self.solution_text = "<br><table border=0>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>The minute hand is pointing at 12, so it shows "+minutes+" minutes.</td></tr>"
            self.solution_text = self.solution_text+"</table>"
            self.solution_text = self.solution_text+"<br>"
    
            self.solution_text = self.solution_text+"<table border=0>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>The hour hand is pointing at "+hour+".</td></tr>"
            self.solution_text = self.solution_text+"</table>"
            self.solution_text = self.solution_text+"<br>"

        else:
            self.solution_text = "<div class='side' style='width:200px;'><font style='font-size:12px'>There are 5 minutes between two adjacent big markings on the clock.</font></div>"
            self.solution_text = self.solution_text + "<br><table border=0>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+str(int(minutes)/5)+" &times; 5 &nbsp;=&nbsp; "+minutes+" minutes</td></tr>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>The minute hand shows "+minutes+" minutes.</td></tr>"
            self.solution_text = self.solution_text+"</table>"
            self.solution_text = self.solution_text+"<br>"
    
            self.solution_text = self.solution_text+"<table border=0>"
            self.solution_text = self.solution_text+"<tr><td style='text-align:left'>The hour hand is between "+hour+" and "+str(int(hour)+1)+".</td></tr>"
            self.solution_text = self.solution_text+"</table>"
            self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>So, the time is "+hour+"."+minutes+".</td></tr>"
        self.solution_text = self.solution_text+"</table>"
        self.solution_text = self.solution_text+"<br>"
        
        self.solution_text = self.solution_text+"<table border=0>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>"+item+" <b>"+hour+"."+minutes+"</b>.</td></tr>"
        self.solution_text = self.solution_text+"</table>"        
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        Fill in the blank with 'past' or 'to'.'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.items = [
                        ['The bus left school at','pm','P3TTPT4a',randint(1,5)],
                        ['The sun rose at','am','P3TTPT4b',randint(5,6)],
                        ['The sun set at','pm','P3TTPT4c',randint(5,6)],
                        ['It started raining at','pm','P3TTPT4d',randint(1,12)],
                        ['The cruise ship left the harbour at','pm','P3TTPT4e',randint(1,6)],
                        ['The plane landed at the airport at','am','P3TTPT4f',randint(1,12)],
                        ['The train arrived at the platorm at','am','P3TTPT4g',randint(5,11)],
                        ['The teacher entered the classroom at','am','P3TTPT4h',randint(7,11)],
                        ['The show ended at','pm','P3TTPT4i',randint(1,12)],
                        ['The game ended at','am','P3TTPT4j',randint(8,11)]
                    ]

        self.item = random.choice(self.items)
        
        self.flag = randint(1,10)
        
        if self.flag < 4:
            self.hour = randint(1,12)
            self.minutes = randint(31,58)
            if self.hour == 12:
                self.hour1 = 1
            else:
                self.hour1 = self.hour + 1
            self.minutes1 = 60 - int(self.minutes)
            self.problem = "Fill in the blank with 'past' or 'to'.<br><br>"
            self.problem = self.problem + "%d.%d is %d minutes _______ %d."%(self.hour,self.minutes,self.minutes1,self.hour1)
        else:
            self.hour = self.item[3]
            self.minutes = randint(31,58)
            if self.hour == 12:
                self.hour1 = 1
            else:
                self.hour1 = self.hour + 1
            self.minutes1 = 60 - int(self.minutes)
            self.problem = "<div style='display:inline-block;vertical-align:top;'>Fill in the blank with 'past' or 'to'.<br><br>"
            self.problem = self.problem + "%s %d.%d %s.<br><br>"%(self.item[0],self.hour,self.minutes,self.item[1])
            self.problem = self.problem + "%d.%d is %d minutes _______ %d.</div>"%(self.hour,self.minutes,self.minutes1,self.hour1)
            self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[2]+".png'></div>"
        
        self.answer = "to"
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.hour,self.hour1,self.minutes,self.minutes1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,hour,hour1,minutes,minutes1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:

        6.43 is 17 minutes before 7 o'clock.    | 1 hour = 60 min          |
        So, 6.43 is 17 minutes <b>to</b> 7.    | 60 min - 43 min = 17 min |
        '''
        self.solution_text = "<div class='side' style='width:200px;'><font style='font-size:12px'>1 hour &nbsp;=&nbsp; 60 min<br>60 min &nbsp;&minus;&nbsp; %d min &nbsp;=&nbsp; %d min</font></div>"%(minutes,minutes1)
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>%d.%d is %d minutes before %d o'clock.</td></tr>"%(hour,minutes,minutes1,hour1)
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>So, %d.%d is %d minutes <b>%s</b> %d.</td></tr>"%(hour,minutes,minutes1,answer,hour1)
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        Fill in the blank with the correct time. [Example: 5.40 or 5:40.]'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['was in the library at','P3TTPT6a',randint(1,12)],
                        ['was jogging at','P3TTPT6b',randint(5,8)],
                        ['was cycling at','P3TTPT6c',randint(5,8)],
                        ['was swimming at','P3TTPT6d',randint(5,8)],
                        ['was playing at','P3TTPT6e',randint(1,12)],
                        ['was cleaning at','P3TTPT6f',randint(1,12)],
                        ['was ironing clothes at','P3TTPT6g',randint(1,4)],
                        ['was studying at','P3TTPT6h',randint(1,4)],
                        ['was in the canteen at','P3TTPT6i',randint(9,12)],
                        ['was in the music room at','P3TTPT6j',randint(9,12)]
                    ]
        self.item = random.choice(self.items)
        
        self.flag = randint(1,10)
        
        if self.flag < 4:
            self.hour = randint(1,12)
            self.minutes = randint(1,29)
            if self.minutes==1:
                self.minOrMins = "minute"
            else:
                self.minOrMins = "minutes"
            self.problem = "Fill in the blank with the correct time. [Example: 5.40 or 5:40.]<br><br>"
            self.problem = self.problem + "%d %s to %d is _________."%(self.minutes,self.minOrMins,self.hour)
        else:
            self.hour = self.item[2]
            self.minutes = randint(1,29)
            if self.minutes==1:
                self.minOrMins = "minute"
            else:
                self.minOrMins = "minutes"
            self.problem = "<div style='display:inline-block;vertical-align:top;'>Fill in the blank with the correct time. [Example: 5.40 or 5:40.]<br><br>"
            self.problem = self.problem + "%s %s %d %s to %d.<br><br>"%(self.name,self.item[0],self.minutes,self.minOrMins,self.hour)
            self.problem = self.problem + "%d %s to %d is _________.</div>"%(self.minutes,self.minOrMins,self.hour)
            self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[1]+".png'></div>"
        
        if self.hour == 1:
            self.hour1 = 12
        else:
            self.hour1 = self.hour - 1
        
        self.minutes1 = 60 - self.minutes
        
        self.answer = "%s.%s"%(self.hour1,self.minutes1)
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.hour,self.hour1,self.minutes,self.minutes1,self.minOrMins,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,hour,hour1,minutes,minutes1,minOrMins,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:

        15 minutes to 6 is 45 minutes after 5 o'clock.     | 1 hour = 60 min          |
        So, the time is <b>5.45</b>.                      | 60 min - 15 min = 45 min |
        '''
        self.solution_text = "<div class='side' style='width:155px;'><font style='font-size:12px'>1 hour &nbsp;=&nbsp; 60 min<br>60 min &nbsp;&minus;&nbsp; %d min &nbsp;=&nbsp; %d min</font></div>"%(minutes,minutes1)
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>%d %s to %d is %d minutes after %d o'clock.</td></tr>"%(minutes,minOrMins,hour,minutes1,hour1)
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>So, the time is <b>%s</b>.</td></tr>"%(answer)
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        Find the missing number.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                        ['The mover came at','pm','P3TTPT8a',randint(1,7)],
                        ['He finished the race at','am','P3TTPT8b',randint(7,11)],
                        ['I have to finish my homework by','pm','P3TTPT8c',randint(1,7)],
                        ['The museum opens at','am','P3TTPT8d',randint(8,11)],
                        ['The zoo opens at','am','P3TTPT8e',randint(8,11)],
                        ['The park opens at','am','P3TTPT8f',randint(7,10)],
                        ['The pupils assembled in the hall by','am','P3TTPT8g',randint(8,11)],
                        ['The shop closes at','pm','P3TTPT8h',randint(6,11)],
                        ['The restaurant opens at','pm','P3TTPT8i',randint(4,7)],
                        ['I have to return home by','pm','P3TTPT8j',randint(4,9)]
                    ]
        
        self.item = random.choice(self.items)
        
        self.flag = randint(1,10)
        
        if self.flag < 4:
            self.hour = str(randint(1,12))
            self.minutes = str(randint(2,30))
            self.minutes1 = self.minutes
            if len(self.minutes)==1:
                self.minutes1 = '0'+self.minutes
            self.problem = "Find the missing number.<br><br>"
            self.problem = self.problem + "%s.%s is %s minutes past _______ ."%(self.hour,self.minutes1,self.minutes)
        else:
            self.hour = str(self.item[3])
            self.minutes = str(random.randrange(5,30,5))
            self.minutes1 = self.minutes
            if len(self.minutes)==1:
                self.minutes1 = '0'+self.minutes            
            self.problem = "<div style='display:inline-block;vertical-align:top;'>Find the missing number.<br><br>"
            self.problem = self.problem + "%s %s.%s %s.<br><br>"%(self.item[0],self.hour,self.minutes1,self.item[1])
            self.problem = self.problem + "%s.%s is %s minutes past _______ .</div>"%(self.hour,self.minutes1,self.minutes)
            self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[2]+".png'></div>"
        
        self.answer = self.hour
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.hour,self.minutes,self.minutes1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,hour,minutes,minutes1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation: (accept answer in numerals and words)
        
        6.15 is 15 minutes after 6 o'clock.
        So, 6.15 is 15 minutes past <b>6</b>.
        '''
        self.solution_text = "<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>%s.%s is %s minutes after %s o'clock.</td></tr>"%(hour,minutes1,minutes,hour)
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>So, %s.%s is %s minutes past <b>%s</b>.</td></tr>"%(hour,minutes1,minutes,hour)
        self.solution_text = self.solution_text+"</table>"
        
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:
        Find the missing number.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [
                        ['am','was baking a cake.','P3TTPT10a',randint(6,11)],
                        ['am','opened her shop.','P3TTPT10b',randint(6,11)],
                        ['am','was at the grocery store.','P3TTPT10c',randint(6,11)],
                        ['am','was driving to work.','P3TTPT10d',randint(6,11)],
                        ['am','was washing her car.','P3TTPT10e',randint(6,11)],
                        ['pm','was cooking dinner.','P3TTPT10f',random.choice([12,1,2,3,4,5])],
                        ['pm','was watching TV.','P3TTPT10g',random.choice([12,1,2,3,4,5])],
                        ['pm','was at the gym.','P3TTPT10h',random.choice([12,1,2,3,4,5])],
                        ['pm','went shopping.','P3TTPT10i',random.choice([12,1,2,3,4,5])],
                        ['pm','came out of the mall.','P3TTPT10j',random.choice([12,1,2,3,4,5])]
                    ]
        
        self.item = random.choice(self.items)
        
        self.flag = randint(1,10)
        
        if self.flag < 4:
            self.hour = randint(1,12)
            self.minutes = randint(31,58)
            if self.hour == 12:
                self.hour1 = 1
            else:
                self.hour1 = self.hour + 1
            self.problem = "Find the missing number.<br><br>"
            self.problem = self.problem + "%d.%d is %d minutes to _____ ."%(self.hour,self.minutes,60-self.minutes)
        else:
            self.hour = self.item[3]
            self.minutes = randint(31,58)
            if self.hour == 12:
                self.hour1 = 1
            else:
                self.hour1 = self.hour + 1            
            self.problem = "<div style='display:inline-block;vertical-align:top;'>Find the missing number.<br><br>"
            self.problem = self.problem + "At %d.%d %s %s %s<br><br>"%(self.hour,self.minutes,self.item[0],self.name,self.item[1])
            self.problem = self.problem + "%d.%d is %d minutes to _____ .</div>"%(self.hour,self.minutes,60-self.minutes)
            self.problem = self.problem + "<div style='display:inline-block;margin-left:20px;'><img src='/images/P3ProblemImages/"+self.item[2]+".png'></div>"
        
        self.answer = self.hour1
                   
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.hour,self.minutes,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,hour,minutes,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        '''
        Explanation:

        6.45 is 15 minutes before 7 o'clock.     | 1 hour = 60 min       |
        So, 6.45 is 15 minutes to <b>7</b>.     | 60 min - 45 min = 15 min |
        '''
        self.solution_text = "<div class='side' style='width:155px;'><font style='font-size:12px'>1 hour &nbsp;=&nbsp; 60 min<br>60 min &nbsp;&minus;&nbsp; %d min &nbsp;=&nbsp; %d min</font></div>"%(minutes,60-minutes)
        self.solution_text = self.solution_text+"<table>"
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>%d.%d is %d minutes before %d o'clock.</td></tr>"%(hour,minutes,60-minutes,answer)
        self.solution_text = self.solution_text+"<tr><td style='text-align:left'>So, %d.%d is %d minutes to <b>%d</b>.</td></tr>"%(hour,minutes,60-minutes,answer)
        self.solution_text = self.solution_text+"</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"")
                answer1 = answer.partition(".")[0]+":"+answer.partition(".")[2]
                return InputAnswer == answer or InputAnswer == answer1
            except ValueError:
                return False
        elif CheckAnswer == 2:
            try:
                InputAnswer = string.join(str(InputAnswer).split(),"")
                return str(answer)==str(InputAnswer).lower()
            except ValueError:
                return False
        elif CheckAnswer == 3:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False            
        