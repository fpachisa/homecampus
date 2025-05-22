'''
Created on Aug 28, 2011

Module: WordProblems
Generates "Word Problems on Decimals" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''
import random
from random import randint
from Problems import PersonName
from decimal import *

class WordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        ''' first grouping the questions as per problem type in the ppt and then first randomly picking the problem type and then problem from the problem type'''
        ProblemList = [[self.GenerateProblemType1(),self.GenerateProblemType1a(),self.GenerateProblemType2(),self.GenerateProblemType2a()],
                       [self.GenerateProblemType3()],
                       [self.GenerateProblemType4(),self.GenerateProblemType4a()],
                       [self.GenerateProblemType5()],
                       [self.GenerateProblemType6()],
                       [self.GenerateProblemType7()],
                       [self.GenerateProblemType8()],
                       [self.GenerateProblemType9()],
                       [self.GenerateProblemType10()],
                       [self.GenerateProblemType11(),self.GenerateProblemType12()],
                       [self.GenerateProblemType13(),self.GenerateProblemType14()],
                       ]
        return random.choice(random.choice(ProblemList))
        #return self.GenerateProblemType14()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemType1a","ProblemType2","ProblemType2a"],
                            2:["ProblemType3",],
                            3:["ProblemType4","ProblemType4a"],
                            4:["ProblemType5",],
                            5:["ProblemType6",],
                            6:["ProblemType7",],
                            7:["ProblemType8",],
                            8:["ProblemType9",],
                            9:["ProblemType10",],
                            10:["ProblemType11","ProblemType12",],
                            11:["ProblemType13","ProblemType14",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemType1a(),self.GenerateProblemType2(),self.GenerateProblemType2a()],
                                    2:[self.GenerateProblemType3()],
                                    3:[self.GenerateProblemType4(),self.GenerateProblemType4a()],
                                    4:[self.GenerateProblemType5()],
                                    5:[self.GenerateProblemType6()],
                                    6:[self.GenerateProblemType7()],
                                    7:[self.GenerateProblemType8()],
                                    8:[self.GenerateProblemType9()],
                                    9:[self.GenerateProblemType10()],
                                    10:[self.GenerateProblemType11(),self.GenerateProblemType12()],
                                    11:[self.GenerateProblemType13(),self.GenerateProblemType14()],
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
        #return self.GenerateProblemType8()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType1a":self.GenerateProblemType1a(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType2a":self.GenerateProblemType2a(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType4a":self.GenerateProblemType4a(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10":self.GenerateProblemType10(),
                            "ProblemType11":self.GenerateProblemType11(),
                            "ProblemType12":self.GenerateProblemType12(),
                            "ProblemType13":self.GenerateProblemType13(),
                            "ProblemType14":self.GenerateProblemType14(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g.:Ray was 53 cm long at birth.
                He is 5 years old now and is 1.12 m tall.
                How much has Ray grown in height in the past 5 years?
                Express your answer in centimetres as well as metres.'''
           
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["cm","was","cm at birth.","He is","years old now and is","m tall.","How much has he grown in height in the past","years?",
                        "Express your answer in centimetres.",randint(40,60),randint(4,6),randint(101,125),100],
                    2:["gm","was","grams at birth.","He is","years old now and has a mass of","kg.","How much has he grown in mass in the past",
                       "years?","Express your answer in grams.",randint(2500,4000),randint(4,6),randint(12001,15999),1000],
                    3:["gm","had","grams of sugar at first.","He added","bags of sugar to it to get a total of","kg of sugar.",
                       "How much sugar did the","bags contain together?","Give your answer in grams.",randint(300,700),randint(2,8),randint(2000,6000),1000],
                    4:["gm","put","grams of soil in a flower pot.","Then he added","bags of soil into the flower pot so the pot had",
                       "kg of soil.","What was the amount of soil in the","bags together?","Give your answer in grams.",
                       randint(250,400),randint(2,10),randint(2000,6000),1000],
                    5:["gm","put","grams of cookies in a jar.","Then he added","boxes of cookies into the jar so the jar had","kg of cookies.",
                       "Find the mass of cookies in the","boxes together.","Express your answer in grams.",
                       randint(250,400),randint(2,10),randint(2000,6000),1000],
                    6:["gm","had","grams of flour.","Then he bought","bags of flour so he had","kg of flour altogether.",
                       "What was the mass of flour in the","bags together?","Give your answer in grams.",
                       randint(250,400),randint(2,10),randint(2000,8000),1000],
                    7:["gm","had","grams of wool.","Then he sheared","lambs and had","kg of wool altogether.",
                       "What was the mass of wool he sheared from the","lambs together?","Express your answer in grams.",
                       randint(250,400),randint(2,10),randint(2000,6000),1000],
                    8:["ml","had","ml of water in a jar.","He put","balls into the jar raising its water level to","litres.","Find the total volume of the",
                       "balls that he put into the jar.","Express your answer in ml.",
                       randint(250,400),randint(2,10),randint(1000,3000),1000],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]
        self.item7 = self.Dict[self.key][7]
        self.item8 = self.Dict[self.key][8]

        self.number1 = self.Dict[self.key][9]
        self.number2 = self.Dict[self.key][10]
        self.number3 = self.Dict[self.key][11]
        self.number4 = self.Dict[self.key][12]
        
        self.problem = self.boy1+" "+self.item1+" "+str(self.number1)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+str(self.number2)+" "+self.item4+" "+str(float(self.number3)/self.number4)+" "+self.item5+"<br>"
        self.problem = self.problem + self.item6+" "+str(self.number2)+" "+self.item7+"<br>"
        self.problem = self.problem + self.item8
        
        
        self.answer = self.number3 - self.number1     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'CheckAnswerType':1}

    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "TyOeHD_JDv8";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType1a(self):
        '''e.g.:Ray was 53 cm long at birth.
                He is 5 years old now and is 1.12 m tall.
                How much has Ray grown in height in the past 5 years?'''
           
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["m","was","cm at birth.","He is","years old now and is","m tall.","How much has he grown in height in the past","years?",
                        "Express your answer in metres.",randint(40,60),randint(4,6),randint(101,125),100],
                    2:["kg","was","grams at birth.","He is","years old now and has a mass of","kg.","How much has he grown in mass in the past",
                       "years?","Express your answer in kg.",randint(2500,4000),randint(4,6),randint(12001,15999),1000],
                    3:["kg","had","grams of sugar at first.","He added","bags of sugar to it to get a total of","kg of sugar.",
                       "How much sugar did the","bags contain together?","Give your answer in kg.",randint(300,700),randint(2,8),randint(2000,6000),1000],
                    4:["kg","put","grams of soil in a flower pot.","Then he added","bags of soil into the flower pot so the pot had",
                       "kg of soil.","What was the amount of soil in the","bags together?","Give your answer in kg.",
                       randint(250,400),randint(2,10),randint(2000,6000),1000],
                    5:["kg","put","grams of cookies in a jar.","Then he added","boxes of cookies into the jar so the jar had","kg of cookies.",
                       "Find the mass of cookies in the","boxes together.","Express your answer in kg.",
                       randint(250,400),randint(2,10),randint(2000,6000),1000],
                    6:["kg","had","grams of flour.","Then he bought","bags of flour so he had","kg of flour altogether.",
                       "What was the mass of flour in the","bags together?","Give your answer in kg.",
                       randint(250,400),randint(2,10),randint(2000,8000),1000],
                    7:["kg","had","grams of wool.","Then he sheared","lambs and had","kg of wool altogether.",
                       "What was the mass of wool he sheared from the","lambs together?","Express your answer in kg.",
                       randint(250,400),randint(2,10),randint(2000,6000),1000],
                    8:["l","had","ml of water in a jar.","He put","balls into the jar raising its water level to","litres.","Find the total volume of the",
                       "balls that he put into the jar.","Express your answer in litres.",
                       randint(250,400),randint(2,10),randint(1000,3000),1000],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]
        self.item7 = self.Dict[self.key][7]
        self.item8 = self.Dict[self.key][8]
        self.item9 = self.Dict[self.key][9]

        self.number1 = self.Dict[self.key][9]
        self.number2 = self.Dict[self.key][10]
        self.number3 = self.Dict[self.key][11]
        self.number4 = self.Dict[self.key][12]
                
        self.problem = self.boy1+" "+self.item1+" "+str(self.number1)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+str(self.number2)+" "+self.item4+" "+str(float(self.number3)/self.number4)+" "+self.item5+"<br>"
        self.problem = self.problem + self.item6+" "+str(self.number2)+" "+self.item7+"<br>"
        self.problem = self.problem + self.item8
        
        
        self.answer = str((float(self.number3) - float(self.number1))/self.number4)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1a(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType1a",
                'CheckAnswerType':1}

    def ExplainType1a(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "TyOeHD_JDv8";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g.:Ray spent 10 minutes of the recess reading a story.
                If he had 0.5 hours of recess at first,
                how much recess time as he left now?
                Express your answer in minutes.'''
           
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["minutes","spent","minutes of the recess reading a story.","If he had","hours of recess at first,",
                        "how much recess time has he left now?","Express your answer in minutes.",randint(5,20),randint(4,15)],
                    2:["minutes","used","minutes of his break to take a rest.","He had","hours of break at first.",
                       "How much break time has he left now?","Give your answer in minutes.",randint(5,20),randint(4,15)],
                    3:["minutes","used","minutes of his study time to do homework.","If he had","hours of study time at first,",
                       "how much study time has he left now?","Give your answer in minutes.",randint(10,30),randint(7,15)],
                    4:["minutes","spent","minutes of his study time solving math problems.","He had","hours of study time at first.",
                       "How much study time has he left now?","Express your answer in minutes.",randint(10,30),randint(7,15)],
                    5:["minutes","spends","minutes of his lunch time eating lunch.","If he had","hours of lunch time at first,",
                       "how much lunch time has he left now?","Express your answer in minutes.",randint(5,20),randint(4,15)],
                    6:["minutes","uses","minutes of his lunch time making a phone call.","He had","hours of lunch time at first.",
                       "How much lunch time has he left now?","Give your answer in minutes.",randint(5,20),randint(4,15)],
                    7:["minutes","spent","minutes of his play time solving a puzzle.","He had","hours of play time at first.",
                       "How much play time has he left now?","Give your answer in minutes.",randint(10,30),randint(7,15)],
                    8:["minutes","spends","minutes of his play time in the playground.","If he had","hours of play time at first,",
                       "how much play time has he left now?","Express your answer in minutes.",randint(5,20),randint(4,15)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]

        self.number1 = self.Dict[self.key][7]
        self.number2 = self.Dict[self.key][8]
                
        self.problem = self.boy1+" "+self.item1+" "+str(self.number1)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+str(float(self.number2)/10)+" "+self.item4+" "+"<br>"
        self.problem = self.problem + self.item5+"<br>"
        self.problem = self.problem + self.item6
        
        
        self.answer = str(self.number2*6 - self.number1)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'CheckAnswerType':1}

    def ExplainType2(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "TyOeHD_JDv8";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType2a(self):
        '''e.g.:Ray spent 10 minutes of the recess reading a story.
                If he had 0.5 hours of recess at first,
                how much recess time as he left now?
                Express your answer in hours.'''
           
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["hours","spent","minutes of the recess reading a story.","If he had","hours of recess at first,",
                        "how much recess time has he left now?","Express your answer in hours.",randint(5,20),randint(4,15)],
                    2:["hours","used","minutes of his break to take a rest.","He had","hours of break at first.",
                       "How much break time has he left now?","Give your answer in hours.",randint(5,20),randint(4,15)],
                    3:["hours","used","minutes of his study time to do homework.","If he had","hours of study time at first,",
                       "how much study time has he left now?","Give your answer in hours.",randint(10,30),randint(7,15)],
                    4:["hours","spent","minutes of his study time solving math problems.","He had","hours of study time at first.",
                       "How much study time has he left now?","Express your answer in hours.",randint(10,30),randint(7,15)],
                    5:["hours","spends","minutes of his lunch time eating lunch.","If he had","hours of lunch time at first,",
                       "how much lunch time has he left now?","Express your answer in hours.",randint(5,20),randint(4,15)],
                    6:["hours","uses","minutes of his lunch time making a phone call.","He had","hours of lunch time at first.",
                       "How much lunch time has he left now?","Give your answer in hours.",randint(5,20),randint(4,15)],
                    7:["hours","spent","minutes of his play time solving a puzzle.","He had","hours of play time at first.",
                       "How much play time has he left now?","Give your answer in hours.",randint(10,30),randint(7,15)],
                    8:["hours","spends","minutes of his play time in the playground.","If he had","hours of play time at first,",
                       "how much play time has he left now?","Express your answer in hours.",randint(5,20),randint(4,15)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]
        
        self.number1 = random.randrange(6,24,6)      
        self.number3 = randint(2,12)
        self.number2 = self.number3 + self.number1/6 
        
        self.problem = self.boy1+" "+self.item1+" "+str(self.number1)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+str(float(self.number2)/10)+" "+self.item4+" "+"<br>"
        self.problem = self.problem + self.item5+"<br>"
        self.problem = self.problem + self.item6

        self.answer = str(float(self.number3)/10)
               
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2a(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType2a",
                'CheckAnswerType':1}

    def ExplainType2a(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "TyOeHD_JDv8";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g.:Everyday Pete walks to his school which is 520 metres from his home.
                He also returns home from school on foot.
                How much does he walk altogether while going to and coming back from school in a 5-day week?
                Round off your answer to the nearest kilometre.'''
           
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["km","Everyday","walks to his school which is","metres from his home.","He also returns home from school on foot.",
                        "How much does he walk altogether while going to and coming back from school in a week?","(1 school-week = 5 days)",
                        "Round off your answer to the nearest kilometre.",random.randrange(500,800,10),5,1000],
                     2:["m","","weaves","cm of carpet in the morning and","as much carpet in the evening.",
                        "Find the length of carpet that he will have woven in a month.","(1 month = 30 days)",
                        "Round off your answer to the nearest metre.",randint(200,800),30,100],
                    3:["km","Everyday","swims","metres in the morning and","as much in the evening.",
                       "How much does he swim over a month?","(1 month = 30 days)",
                       "Round off your answer to the nearest km.",random.randrange(50,500,50),30,1000],
                    4:["kg","Each day","'s family consumes","grams of coffee in the morning and","the same amount of coffee in the afternoon.",
                       "How much coffee does the family consume in a month?","(1 month = 30 days)",
                       "Round off your answer to the nearest kg.",randint(20,80),30,1000],
                    5:["kg","","feeds","grams of fish food to his fishes in the morning and","the same amount of fish food in the evening.",
                       "Find the amount of fish food that he feeds to the fishes altogether in a month.","(1 month = 30 days)",
                       "Round off your answer to the nearest kg.",random.randrange(150,400,5),30,1000],
                    6:["kg","Each day","feeds","grams of dog food to his dog in the morning and","the same amount of dog food in the evening.",
                       "How much dog food does he feed to his dog in a week?","(1 week = 7 days)",
                       "Round off your answer to the nearest kg.",random.randrange(150,400,5),7,1000],
                    7:["kg","","'s family eats","grams of rice for lunch each day.","The family also eats the same amount of rice for dinner each day.",
                       "How much rice does the family eat in a month?","(1 month = 30 days)",
                       "Round off your answer to the nearest kg.",random.randrange(150,400,5),30,1000],
                    8:["kg","","is a fruiterer. He sells","grams of fruit in the morning and","as much fruit in the evening.",
                       "Find the total mass of fruit that he sells in a month.","(1 month = 30 days)",
                       "Round off your answer to the nearest kg.",random.randrange(5000,10000,50),30,1000],
                    9:["kg","Everyday","uses","grams of detergent to wash his laundry in the morning.","He uses the same amount of detergent to wash his laundry in the evening.",
                       "How much detergent does he use altogether in a month?","(1 month = 30 days)",
                       "Round off your answer to the nearest kg.",random.randrange(50,150,5),30,1000],
                    10:["l","Everyday","goes to work by car from his home and uses","ml of petrol.","He takes the same route while returning home from work.",
                        "How much petrol does he use altogether while going to and coming back from work in a month?","(1 month = 20 working days)",
                        "Round off your answer to the nearest litre.",random.randrange(1000,2000,25),20,1000],
                    11:["l","Each day","drinks","ml of protein drink in the morning.","He also drinks the same amount of protein drink in the evening.",
                        "How much protein drink does he drink altogether in a week?","",
                        "Round off your answer to the nearest litre.",random.randrange(150,350,25),7,1000],
                    12:["l","","drinks","ml of milk in the morning and","the same amount of milk at night.",
                        "How much milk does he drink altogether in a month?","(1 month = 30 days)",
                        "Round off your answer to the nearest litre.",random.randrange(150,400,5),30,1000],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]
        self.item7 = self.Dict[self.key][7]

        self.number1 = self.Dict[self.key][8]
        self.number2 = self.Dict[self.key][9]
        self.number3 = self.Dict[self.key][10]
        
        self.problem = self.item1+" "+self.boy1+" "+self.item2+" "+str(self.number1)+" "+self.item3+"<br>"
        self.problem = self.problem + self.item4+"<br>"
        self.problem = self.problem + self.item5+" "+self.item6+"<br>"
        self.problem = self.problem + self.item7
                
        self.answer = int(round(2 * float(self.number1)*float(self.number2)/self.number3,0))     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'CheckAnswerType':1}

    def ExplainType3(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "tds0lvaguXw";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g.:2 soda bottles together contain 11 times as much beverage as a can of soda.
                If each soda bottle contains 1.8 litres of beverage,
                how much beverage (in ml) does each can of soda contain?'''
           
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["ml","soda bottles together contain","times as much beverage as a can of soda.",
                        "","If each soda bottle contains","litres of beverage,","",
                        "how much beverage (in ml) does each can of soda contain?",randint(4,6),random.randrange(200,350,10),randint(1,4),1000],
                     2:["ml","juice bottles together have","times as much beverage as a glass of juice.",
                        "","If each bottle has","litres of juice,","","how much juice (in ml) does each glass have?",randint(4,6),random.randrange(200,350,10),randint(1,4),1000],
                    3:["ml","cans together contain","times as much milk as a carton.","","If each can contains",
                       "litres of milk,","","find the volume of milk (in ml) that each carton contains.",randint(4,6),random.randrange(200,350,10),randint(1,4),1000],
                    4:["ml","tins together have","times as much paint as a bottle.","","If each tin has","litres of paint,","",
                       "find the volume of paint that each bottle has.",randint(4,6),random.randrange(300,650,10),randint(1,4),1000],
                    5:["gm","bags together contain","times as much sand as a packet.","","If each bag contains","kg of sand,","",
                       "what is the mass of sand (in grams) that each packet contains?",randint(4,6),random.randrange(200,600,5),randint(1,4),1000],
                    6:["gm","bags together have","times as much candies as a packet.","","If each bag has","kg of candies,","",
                       "find the mass of candies (in grams) that each packet has.",randint(4,6),random.randrange(200,350,5),randint(1,4),1000],
                    7:["gm","dumbbells together have","times as much mass as a metal ball.","","If each dumbbell has a mass of","kg,","",
                        "what is the mass (in grams) of each metal ball?",randint(4,6),random.randrange(500,800,10),randint(1,4),1000],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]
        self.item7 = self.Dict[self.key][7]
        self.number1 = self.Dict[self.key][8]
        self.number2 = self.Dict[self.key][9]
        self.number3 = self.Dict[self.key][10]
        self.number4 = self.Dict[self.key][11]
               
        self.problem = str(self.number3)+" "+self.item1+" "+str(self.number1*self.number3)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+self.item4+" "+str(round(float(self.number2)*float(self.number1)/self.number4,3))+" "+self.item5+"<br>"
        self.problem = self.problem + self.item6 +" "+self.item7
                
        self.answer = self.number2     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,str(self.answer),self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'CheckAnswerType':1}
        
    def GenerateProblemType4a(self):
        '''e.g.:2 soda bottles together contain 11 times as much beverage as a can of soda.
                If each soda bottle contains 1.8 litres of beverage,
                how much beverage (in ml) does each can of soda contain?'''
           
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["ml","bottles together have","times as much fusion drink as a cup.","",
                       "Find the volume of fusion drink (in ml) that each cup has","","if each bottle has","litres of the drink.",randint(4,6),random.randrange(200,350,10),randint(1,4),1000],
                    2:["ml","bottles together contain","times as much iced tea as a cup.","",
                       "How much iced tea (in ml) does each cup contain","","if each bottle contains","litres of iced tea?",randint(4,6),random.randrange(200,350,10),randint(1,4),1000],
                    3:["gm","bags together contain","times as much flour as a packet.","","What is the mass of flour (in grams) inside each packet","",
                       "if each bag contains","kg of flour?",randint(4,6),random.randrange(200,700,10),randint(1,4),1000],
                    4:["cm","spools together have","times as much ribbon as a roll.","","Find the length of ribbon (in cm) on each roll","",
                        "if each spool has","metres of ribbon.",randint(4,6),random.randrange(200,800,5),randint(1,4),100],
                    5:["cm","balls of yarn together contain","times as much yarn as a roll.","","What is the length of yarn (in cm) on each roll","",
                        "if each ball has","metres of yarn?",randint(4,6),random.randrange(200,800,5),randint(1,4),100],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]
        self.item7 = self.Dict[self.key][7]
        self.number1 = self.Dict[self.key][8]
        self.number2 = self.Dict[self.key][9]
        self.number3 = self.Dict[self.key][10]
        self.number4 = self.Dict[self.key][11]
               
        self.problem = str(self.number3)+" "+self.item1+" "+str(self.number1*self.number3)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+self.item4+" "+self.item5+"<br>"
        self.problem = self.problem + self.item6 +" "+str(round(float(self.number2)*float(self.number1)/self.number4,3))+" "+self.item7
                
        self.answer = self.number2     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,str(self.answer),self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType4a",
                'CheckAnswerType':1}

    def ExplainType4(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "lYl61VbT4V8";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType5(self):
        '''e.g.:You need 600 grams of flour and 200 grams of sugar to make a cake.
                How much flour and sugar will you need altogether to make 6 such cakes?
                Give your answer in kilograms.'''
           
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["kg","You need","grams of flour and","grams of sugar to make a cake.",
                        "How much flour and sugar will you need altogether to make","such cakes?","Give your answer in kilograms.",
                        random.randrange(100,350,10),randint(2,4),randint(8,20),1000],
                     2:["kg",self.boy1+" uses","grams of flour and","grams of cheese to make a cheese pizza.",
                        "How much flour and cheese will he need altogether to make","such cheese pizzas?","Give your answer in kilograms.",
                        random.randrange(100,350,10),randint(2,4),randint(8,20),1000],
                    3:["kg",self.boy1+" mixes","grams of potting soil and","grams of fertilizer to pot one plant.",
                       "How much potting soil and fertilizer will he need to mix altogether to pot","such plants?","Express your answer in kilograms.",
                       random.randrange(200,500,10),randint(2,4),randint(8,20),1000],
                    4:["kg",self.boy1+" is packing assorted confectioneries with","grams of marshmallows and","grams of candies into each packet.",
                       "What is the mass of marshmallows and candies that he will pack altogether into","such packets of confectioneries?","Express your answer in kilograms.",
                       random.randrange(100,350,10),randint(2,4),randint(8,20),1000],
                    5:["kg","A grocer is packing assorted snacks with","grams of dried fruits and","grams of nuts into each packet.",
                       "What is the mass of dried fruits and nuts that he will pack altogether into","such packets of assorted snacks?","Give your answer in kilograms.",
                       random.randrange(100,350,10),randint(2,4),randint(8,20),1000],
                    6:["l","It takes","ml of milk and","ml of rose syrup to make a bottle of shake.",
                       "What is the volume of rose syrup and milk that it will take altogether to make","such bottles of shake?","Express your answer in litres.",
                       random.randrange(10,40,10),randint(5,8),randint(8,20),1000],
                    7:["l",self.boy1+" mixes","ml of yogurt","ml of strawberry syrup to make a cup of strawberry yogurt.",
                       "Find the volume of yogurt and strawberry syrup that he will mix altogether to make","such cups of strawberry yogurt?","Give your answer in litres.",
                       random.randrange(10,40,10),randint(5,8),randint(8,20),1000],
                    8:["l","You need","ml of water and","ml of lemon syrup to make a glass of lemonade.",
                       "How much lemon syrup and water will you need altogether to make","such glasses of lemonade?","Express your answer in litres.",
                       random.randrange(10,40,10),randint(5,8),randint(8,20),1000],
                    9:["l",self.boy1+" is mixing","ml of red paint and","ml of blue paint to get a tin of purple paint.",
                       "Find the volume of red and blue paints that he will need to mix altogether to get","such tins of purple paint.","Give your answer in litres.",
                       random.randrange(100,500,10),randint(2,4),randint(8,20),1000],
                    10:["m",self.boy1+" is using","cm of golden ribbon and","cm of silver ribbon to make a pompom.",
                        "Find the length of golden and silver ribbons that he will need to make","such pompoms.","Express your answer in metres.",
                        random.randrange(50,200,10),randint(2,5),randint(8,20),100],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]
        self.number1 = self.Dict[self.key][7]
        self.number2 = self.Dict[self.key][8]*self.number1
        self.number3 = self.Dict[self.key][9]
        self.number4 = self.Dict[self.key][10]
                      
        self.problem = self.item1+" "+str(self.number2)+" "+self.item2+" "+str(self.number1)+" "+self.item3+"<br>"
        self.problem = self.problem + self.item4+" "+str(self.number3)+" "+self.item5+"<br>"
        self.problem = self.problem + self.item6
                
        self.answer = float(self.number1+self.number2)*float(self.number3)/float(self.number4)   
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,str(self.answer),self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'CheckAnswerType':1}

    def ExplainType5(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "nxQmdAk9wWw";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType6(self):
        '''e.g.:The price of a happy meal is $4.15.
                How much do 10 such happy meals cost?
                Round off your answer to the nearest dollar.'''
           
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["$","","The price of a happy meal is $",".","How much do","such happy meals cost?",
                        "Round off your answer to the nearest dollar.",random.randrange(350,550,5),
                        random.randrange(10,90,10),100],
                     2:["$","","A litre of petrol costs $",".","What is the price of","litres of petrol?",
                        "Round off your answer to the nearest dollar.",randint(100,250),
                        random.randrange(10,90,10),100],
                    3:["$","","A movie ticket costs $",".","How much did a group of","people pay altogether for movie tickets?",
                       "Round off your answer to the nearest dollar.",random.randrange(600,1500,5),
                       random.randrange(10,90,10),100],
                    4:["","litres","A bottle has "," litres of coconut water.","How much coconut water is there in","such bottles.",
                       "Round off your answer to the nearest litre.",random.randrange(1050,2000,5),
                       random.randrange(10,90,10),1000],
                    5:["","litres","A can contains "," litres of milk","What is the volume of milk in","such cans?",
                       "Round off your answer to the nearest litre.",random.randrange(1050,2000,5),
                       random.randrange(10,90,10),1000],
                    6:["","kg","A bag contains "," kg of sugar.","What is the mass of sugar in","such bags?",
                        "Round off your answer to the nearest kg.",random.randrange(1050,2000,5),
                       random.randrange(10,90,10),1000],
                    7:["","kg","A container contains "," kg of peanuts.","What is the mass of peanuts in","such containers?",
                        "Round off your answer to the nearest kg.",random.randrange(1050,2000,5),
                       random.randrange(10,90,10),1000],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.dollar = self.Dict[self.key][0]
        self.unit = self.Dict[self.key][1]
        self.item1 = self.Dict[self.key][2]
        self.item2 = self.Dict[self.key][3]
        self.item3 = self.Dict[self.key][4]
        self.item4 = self.Dict[self.key][5]
        self.item5 = self.Dict[self.key][6]
        self.number1 = self.Dict[self.key][7]
        self.number2 = self.Dict[self.key][8]
        self.number3 = self.Dict[self.key][9]
        
        self.cost = float(self.number1)/self.number3

        self.answer = int(round(self.cost*self.number2,0)) 
        
        if (len(str(self.cost).partition(".")[2])==1):
            self.cost = str(self.cost) + "0"
        else:
            self.cost = str(self.cost)       
                             
        self.problem = self.item1+self.cost+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+str(self.number2)+" "+self.item4+"<br>"
        self.problem = self.problem + self.item5
 
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,str(self.answer),self.dollar,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':self.dollar,'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'CheckAnswerType':1}

    def ExplainType6(self,problem,answer,dollar,unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "wYhIdVkO9-I";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType7(self):
        '''e.g.:An LED TV costs $5849 when paid by cash upfront.
                If Alex buys the LED TV payable over 60 monthly installments of $108.31 each,
                how much more than the cash price does the LED TV cost her?
                Give your answer correct to the nearest dollar.'''
           
        self.girl1 = random.choice(PersonName.GirlName)
        self.Dict = {1:["An LED TV costs $","when paid by cash upfront.","If","buys the LED TV payable over","monthly installments of $",
                        "each,","how much more than the cash price does the LED TV cost her?",
                        "Give your answer correct to the nearest dollar.",randint(500,5000),random.randrange(12,60,3),randint(50,1000)],
                     2:["A mattress costs $","when paid by cash upfront.","If","buys the mattress payable over",
                        "monthly installments of $","each,","how much more than the cash price does the mattress cost her?",
                        "Give your answer correct to the nearest dollar.",randint(300,3000),random.randrange(12,45,3),randint(50,1000)],
                    3:["A sofa set costs $","when paid by cash upfront.","If","buys the sofa set payable over",
                       "monthly installments of $","each,","how much more than the cash price does the sofa set cost her?",
                       "Give your answer correct to the nearest dollar.",randint(300,3000),random.randrange(12,45,3),randint(50,1000)],
                    4:["A dining table costs $","when paid by cash upfront.","If","buys the dining table payable over",
                       "monthly installments of $","each,","how much more than the cash price does the dining table cost her?",
                       "Give your answer correct to the nearest dollar.",randint(300,3000),random.randrange(12,45,3),randint(50,1000)],
                    5:["A computer costs $","when paid by cash upfront.","If","buys the computer payable over",
                       "monthly installments of $","each,","how much more than the cash price does the computer cost her?",
                       "Give your answer correct to the nearest dollar.",randint(600,2000),random.randrange(12,45,3),randint(50,1000)],
                    6:["A laptop costs $","when paid by cash upfront.","If","buys the laptop payable over",
                       "monthly installments of $","each,","how much more than the cash price does the laptop cost her?",
                       "Give your answer correct to the nearest dollar.",randint(900,3000),random.randrange(12,45,3),randint(50,1000)],
                    7:["A refrigerator costs $","when paid by cash upfront.","If","buys the refrigerator payable over",
                       "monthly installments of $","each,","how much more than the cash price does the refrigerator cost her?",
                       "Give your answer correct to the nearest dollar.",randint(600,3000),random.randrange(12,45,3),randint(50,1000)],
                    8:["A photocopier costs $","when paid by cash upfront.","If","buys the photocopier payable over",
                       "monthly installments of $","each,","how much more than the cash price does the photocopier cost her?",
                       "Give your answer correct to the nearest dollar.",randint(300,3000),random.randrange(12,45,3),randint(50,1000)],
                    9:["A diamond ring costs $","when paid by cash upfront.","If","buys the diamond ring payable over",
                       "monthly installments of $","each,","how much more than the cash price does the diamond ring cost her?",
                       "Give your answer correct to the nearest dollar.",randint(900,10000),random.randrange(12,60,3),randint(50,1000)],
                    10:["A pool table costs $","when paid by cash upfront.","If","buys the pool table payable over",
                        "monthly installments of $","each,","how much more than the cash price does the pool table cost her?",
                        "Give your answer correct to the nearest dollar.",randint(300,3000),random.randrange(12,45,3),randint(50,1000)],
                    11:["An entertainment system costs $","when paid by cash upfront.","If","busy the entertainment system payable over",
                        "monthly installments of $","each,","how much more than the cash price does the entertainment system cost her?",
                        "Give your answer correct to the nearest dollar.",randint(300,3000),random.randrange(12,45,3),randint(50,1000)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.item1 = self.Dict[self.key][0]
        self.item2 = self.Dict[self.key][1]
        self.item3 = self.Dict[self.key][2]
        self.item4 = self.Dict[self.key][3]
        self.item5 = self.Dict[self.key][4]
        self.item6 = self.Dict[self.key][5]
        self.item7 = self.Dict[self.key][6]
        self.item8 = self.Dict[self.key][7]
        self.cost = self.Dict[self.key][8]
        self.months = self.Dict[self.key][9]
        self.interest = self.Dict[self.key][10]
        
        self.installment = round(float(self.interest*self.cost)/(10000*12)+float(self.cost/self.months),2)
        
        self.answer = int(round(self.installment*self.months-self.cost,0)) 
                      
        self.problem = self.item1+str(self.cost)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+self.girl1+" "+self.item4+" "+str(self.months)+" "+self.item5+str(self.installment)+" "+self.item6+"<br>"
        self.problem = self.problem + self.item7+"<br>"
        self.problem = self.problem + self.item8
 
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,str(self.answer))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"$",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'CheckAnswerType':1}
        
    def ExplainType7(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>$"+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "wtWK9jMEFO8";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemType8(self):
        '''e.g.:Mrs. Jones bought 1.65 kg of meat.
                She cooked a pie using 1/3 of it and froze the rest.
                What is the mass of the meat (in grams) that she froze?'''
           
        self.aunty1 = random.choice(PersonName.AuntyName)
        self.Dict = {1:["gm","bought","kg of meat.","She cooked a pie using","of it and froze the rest.",
                        "What is the quantity of meat (round off to the nearest gram) that she froze?",
                        random.randrange(1050,5000,10),1000],
                     2:["gm","had","kg of soil.","She used","of it to pot some plants and packed the rest.",
                        "Find the quantity of soil (round off to the nearest gram) that she packed.",
                        random.randrange(1050,5000,10),1000],
                    3:["gm","bought","kg of potatoes.","She cooked mashed potatoes with","of it and used the rest to make fries.",
                       "What is the mass of potatoes (round off to the nearest gram) that she used to make fries?",
                       random.randrange(1050,5000,10),1000],
                    4:["gm",", who is a tea merchant, bought","kg of tea leaves.","She kept","of it for herself and sold the rest.",
                       "What is the mass of tea leaves (round off to the nearest gram) that she sold?",
                       random.randrange(5050,10000,10),1000],
                    5:["cm","had","metre of ribbon.","She made decorative flowers with","of it and packed away the rest.",
                       "What is the length of ribbon (round off to the nearest cm) that she packed away?",
                       random.randrange(500,5000,10),100],
                    6:["cm","had","metres of rope.","She used","of it for a clothesline and threw the rest away.",
                       "What is the length of rope (round off to the nearest cm) that she threw away?",
                       random.randrange(500,2000,10),100],
                    7:["m",", who is a kite seller, purchased","km of kite string from a wholesaler.","She sold",
                       "of it and gave away the rest to her staff.","What is the length of kite string (round off to the nearest m) that she gave away to her staff?",
                       random.randrange(1000,5000,10),1000],
                    8:["ml","had","litre of juice.","She spilled","of it and drank the rest.",
                       "Find the volume of juice (round off to the nearest ml) that she drank.",
                       random.randrange(1000,2500,10),1000],
                    9:["ml","purchased","litres of cooking oil from a supplier.","She packed","of it into cans and kept the rest for herself.",
                        "What is the volume of cooking oil (round off to the nearest ml) that she kept for herself?",
                        random.randrange(1000,2500,10),1000],
                    10:["ml","had","litres of soda.","She kept","of it for herself and shared the rest with her friends.",
                        "Find the volume of soda (round off to the nearest ml) that she shared with her friends.",
                        random.randrange(1000,2500,10),1000],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.number1 = self.Dict[self.key][7]
        self.weight = float(self.Dict[self.key][6])/self.number1
        
        self.denominator1 = randint(2,8)
        self.numerator1 = randint(1,self.denominator1-1)
        
        self.answer = int(round((self.denominator1-self.numerator1)*self.weight*self.number1/self.denominator1,0)) 
                      
        self.problem = self.aunty1+" "+self.item1+" "+str(self.weight)+" "+self.item2+"<br>"
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.item3+"&nbsp;</td>"        
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp;"+self.item4+"</td>"
        self.problem = self.problem + "</tr></table>" 
        self.problem = self.problem + self.item5
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,str(self.answer),self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'CheckAnswerType':1}

    def ExplainType8(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "Z3ZPqaeGvmU";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemType9(self):
        '''e.g.:At a school fair, Jimmy and Ricky had juice stalls.
                Jimmy sold 160 glasses each containing 265 ml of juice, 
                while Ricky sold 30 bottles each containing 1.325 litres of juice.
                Who sold a greater volume of juice?'''
           
        self.BoyNames = random.sample(PersonName.BoyName,2)
        self.boy1 = self.BoyNames[0]
        self.boy2 = self.BoyNames[1]
        
        self.Dict = {1:["At a school fair,","had juice stalls.","sold","glasses each containing","ml of juice, while",
                        "sold","bottles each containing","litres of juice.","Who sold a greater volume of juice?",
                        random.randrange(50,200,10),random.randrange(10,40,10),random.randrange(150,350,5),random.randrange(1000,2000,10),1000],
                     2:["","bought milk from a supermarket.","bought","cartons each containing","ml of milk, while",
                        "bought","cans each containing","litres of milk.","Who bought more milk?",
                        random.randrange(5,10,1),random.randrange(2,4,1),random.randrange(250,350,5),random.randrange(1000,2000,10),1000],
                    3:["At a racial harmony carnival,","sold fusion drinks.","sold","cups each containing","ml of drink, while","sold",
                       "bottles each containing","litres of drink.","Who sold more drink?",
                       random.randrange(50,200,10),random.randrange(10,40,10),random.randrange(150,350,5),random.randrange(1000,2000,10),1000],
                    4:["At a carnival,","sold iced tea.","sold","cups each containing","ml of iced tea, while","sold","bottles each containing",
                       "litres of iced tea.","Who sold more iced tea?",
                       random.randrange(50,200,10),random.randrange(10,40,10),random.randrange(150,350,5),random.randrange(1000,2000,10),1000],
                    5:["Last week","went to an art expo.","bought","bottles of oil paint each containing","ml of paint, while","bought",
                       "tins of wall paint each containing","litres of paint.","Who bought a greater volume of paint at the art expo?",
                       random.randrange(50,200,10),random.randrange(10,40,10),random.randrange(150,350,5),random.randrange(1000,2000,10),1000],
                    6:["At an art festival,","bought coloured sand.","bought","packets each containing","grams of coloured sand, while",
                       "bought","bags each containing","kg of coloured sand.","Who bought more sand?",
                       random.randrange(50,200,10),random.randrange(10,40,10),random.randrange(150,350,5),random.randrange(1000,2000,10),1000],
                    7:["","had some candies.","had","packets each containing","grams of candies, while","had","bags each containing",
                       "kg of candies.","Who had a greater mass of candies?",
                       random.randrange(50,200,10),random.randrange(10,40,10),random.randrange(150,350,5),random.randrange(1000,2000,10),1000],
                    8:["","each used some flour to bake cakes and muffins.","used","packets each containing","grams of flour, while","used",
                       "bags each containing","kg of flour.","Who used a greater amount of flour?",
                       random.randrange(5,20,1),random.randrange(2,5,1),random.randrange(150,350,5),random.randrange(1000,2000,10),1000],
                    9:["","each had some ribbon.","had","rolls each containing","cm of ribbon, while","had","spools each containing","m ribbon.",
                        "Who had more ribbon?",random.randrange(50,200,10),random.randrange(10,40,10),random.randrange(150,350,5),random.randrange(1000,2000,10),100],
                    10:["","used some yarn for a knitting project.","used","rolls each containing","cm of yarn, while","used",
                        "balls each containing","m of yarn.","Who used more yarn for the knitting project?",
                        random.randrange(10,80,5),random.randrange(5,25,1),random.randrange(150,350,5),random.randrange(1000,2000,10),100],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.item1 = self.Dict[self.key][0]
        self.item2 = self.Dict[self.key][1]
        self.item3 = self.Dict[self.key][2]
        self.item4 = self.Dict[self.key][3]
        self.item5 = self.Dict[self.key][4]
        self.item6 = self.Dict[self.key][5]
        self.item7 = self.Dict[self.key][6]
        self.item8 = self.Dict[self.key][7]
        self.item9 = self.Dict[self.key][8]

        self.number1 = self.Dict[self.key][9]
        self.number2 = self.Dict[self.key][10]
        self.volume1 = self.Dict[self.key][11]
        self.volume2 = self.Dict[self.key][12]
        self.number3 = self.Dict[self.key][13]
        
        # making sure the total volumes is differnt in both cases
        if (self.number1*self.volume1 == self.number2*self.volume2):
            self.number1 = self.number1 + 10
        
        if (self.number1*self.volume1 > self.number2*self.volume2):
            self.answer = self.boy1
        else:
            self.answer = self.boy2
                      
        self.problem = self.item1+" "+self.boy1+" and "+self.boy2+" "+self.item2+"<br>"
        self.problem = self.problem + self.boy1+" "+self.item3+" "+str(self.number1)+" "+self.item4+" "+str(self.volume1)+" "+self.item5+"<br>"
        self.problem = self.problem + " "+self.boy2+" "+self.item6+" "+str(self.number2)+" "+self.item7+" "+str(float(self.volume2)/self.number3)+" "+self.item8+"<br>"
        self.problem = self.problem + self.item9
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,str(self.answer))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'CheckAnswerType':2}

    def ExplainType9(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "CsB1fbghhC8";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemType10(self):
        '''e.g.:It costs $225 to tile 1 m-2 of floor area with marble.
                Help Joe work out the cost of tiling a rectangular floor measuring 8.55 m by 14.6 m with marble.'''
                  
        self.boy1 = random.choice(PersonName.BoyName)

        self.Dict = {1:["$","","It costs $","to tile 1 m<sup>2</sup> of floor area with marble.","Help",
                        self.boy1+" work out the cost of tiling a rectangular floor","measuring","m by","m with marble.",
                        "(Round off your answer to the nearest dollar)",
                        random.randrange(50,250,5),randint(100,800),randint(500,1500),100],
                     2:['$','','1 m<sup>2</sup> of carpet costs $','.','How much will',self.boy1+' pay for a rectangular carpet',
                        'that measures','m by','m?','Round off your answer to the nearest dollar.',
                        random.randrange(10,150,5),randint(100,800),randint(500,1500),100],
                    3:['','','In City C, there are ','people per km<sup>2</sup>.','Find the population of City C if it is a rectangular city',
                       '','measuring','km by','km.','Round off your answer to the nearest whole number.',
                       random.randrange(50,5000,5),randint(500,1500),randint(2000,4000),100],
                    4:['','tiles','It takes ','tiles to parquet 1 m<sup>2</sup> of floor area.','How many tiles will',
                       self.boy1+' need to parquet his bedroom floor','measuring','m by','m?',
                       'Round off your answer to the nearest whole number.',
                       randint(3,8),randint(100,800),randint(500,1500),100],
                    5:['','ml','It takes ','ml of paint to paint 1 m<sup>2</sup> of wall.','Find the volume of paint that',
                       self.boy1+' will need to paint a wall','measuring','m by','m.','Round off your answer to the nearest ml.',
                       random.randrange(50,250,5),randint(100,800),randint(500,1500),100],
                    6:['','days','It takes ','days to weave 1 m<sup>2</sup> of designer carpet.',
                       'How many days will it take to weave a rectangular designer carpet','','measuring','m by','m?',
                       'Round off your answer to the nearest whole number.',
                       random.randrange(2,4,1),randint(100,800),randint(500,1500),100],
                    7:['','gm','A farmer needs ','gm of seeds to sow 1 m<sup>2</sup> of his farm.',
                       'Find the mass of seeds that he will need to sow his farm','','measuring','m by','m.','Round off your answer to the nearest gm.',
                       random.randrange(5,10,1),randint(100,800),randint(500,1500),100],
                    8:['$','','1 m<sup>2</sup> of wallpaper costs $','.','How much will',self.boy1+' pay','for','m by','m of the wallpaper?',
                       'Round off your answer to the nearest dollar.',
                       random.randrange(3,8,1),randint(100,800),randint(500,1500),100],
                    9:['','trees','1 km<sup>2</sup> of a forest has ','trees.','If the forest has a land area of','','','km by','km, how many trees does it have?',
                       'Round off your answer to the nearest whole number.',
                       random.randrange(40,100,1),randint(100,800),randint(500,1500),100],
                    10:['','schools','There are ','schools in 1 km<sup>2</sup> of a city.','If the city has a land area of','','','km by',
                        'km, how many schools does it have?','Round off your answer to the nearest whole number.',
                        random.randrange(2,3,1),randint(400,800),randint(900,1500),100],
                    11:['','bandanas','A tailor can make ','bandanas with 1 m<sup>2</sup> of cloth.','How many bandanas can he make with','','',
                        'm by','m of cloth?','Round off your answer to the nearest whole number.',
                        random.randrange(3,10,1),randint(100,800),randint(500,1500),100],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.dollar = self.Dict[self.key][0]
        self.unit = self.Dict[self.key][1]
        self.item1 = self.Dict[self.key][2]
        self.item2 = self.Dict[self.key][3]
        self.item3 = self.Dict[self.key][4]
        self.item4 = self.Dict[self.key][5]
        self.item5 = self.Dict[self.key][6]
        self.item6 = self.Dict[self.key][7]
        self.item7 = self.Dict[self.key][8]
        self.item8 = self.Dict[self.key][9]

        self.cost = self.Dict[self.key][10]
        self.length = self.Dict[self.key][11]
        self.breadth = self.Dict[self.key][12]
        self.number1 = self.Dict[self.key][13]
        
        self.answer = int(round(float(self.length)*float(self.breadth)*self.cost/(self.number1*self.number1),0))
                              
        self.problem = self.item1+str(self.cost)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+self.item4+"<br>"
        self.problem = self.problem + self.item5+" "+str(float(self.length)/self.number1)+" "+self.item6+" "+str(float(self.breadth)/self.number1)+" "+self.item7+"<br><br>"
        self.problem = self.problem + self.item8
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,str(self.answer),self.dollar,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':self.dollar,'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'CheckAnswerType':1}

    def ExplainType10(self,problem,answer,dollar,unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "hWo6rOe9qrg";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemType11(self):
        '''e.g.:Mary has 5 lambs each having a mass of 12 kg.
                Mary shears 1200 grams of wool from each lamb.
                What is the total mass of the lambs after the shearing?
                Give your answer in kg correct to 2 decimal places.'''
                  
        self.girl1 = random.choice(PersonName.GirlName)

        self.Dict = {1:['kg','has','lambs each having a mass of','kg.','She shears','grams of wool from each lamb.',
                        'What is the total mass of the lambs after the shearing?','Give your answer in kg.',
                        randint(8,100),random.randrange(10000,20000,500),random.randrange(1000,2000,25),1000],
                     2:['kg','has','bags each containing','kg of rice.','She removes','grams of rice from each bag.',
                        'What is the total mass of rice she has now?','Give your answer in kg.',
                        randint(4,10),random.randrange(10000,20000,500),random.randrange(1000,2000,25),1000],
                    3:['kg','has','bags each containing','kg of apples.','She throws away','grams of rotten apples from each bag.',
                       'Find the total mass of apples she is left with.','Give your answer in kg.',
                       randint(4,10),random.randrange(10000,20000,500),random.randrange(1000,2000,25),1000],
                    4:['kg','bought','watermelons each having a mass of','kg.','She removed','grams of skin from each watermelon.',
                       'What was the total mass of flesh inside the watermelons?','Give your answer in kg.',
                       randint(4,10),random.randrange(1500,5000,500),random.randrange(100,200,25),1000],
                    5:['kg','had','tins of cookies, each with a mass of','kg.','If each empty tin had a mass of','grams,',
                       'find the total mass of cookies that she had.','Give your answer in kg.',
                       randint(4,10),random.randrange(1500,5000,500),random.randrange(100,200,25),1000],
                    6:['litres','bought','bottles of juice each containing','litres of juice.','She drank','ml of juice from each bottle.',
                       'How much juice has she left altogether?','Give your answer in litres.',
                       randint(4,10),random.randrange(1500,5000,500),random.randrange(100,200,25),1000],
                    7:['litres','had','bottles of water each containing','litres of water.','She used','ml of water from each bottle.',
                       'Find the volume of water she had left altogether in the bottles.','Give your answer in litres.',
                       randint(4,10),random.randrange(1500,5000,500),random.randrange(100,200,25),1000],
                    8:['litres','had','cans of sugar syrup each containing','litres of syrup.','She used','ml of sugar syrup from each can.',
                       'Find the total volume of sugar syrup she had left.','Give your answer in litres.',
                       randint(4,10),random.randrange(1500,5000,500),random.randrange(100,200,25),1000],
                    9:['litres','purchased','tins of paint each containing','litres of paint.','She used',
                       'ml of paint from each tin for a painting project.','How much paint had she left altogether?','Give your answer in litres.',
                       randint(4,10),random.randrange(1500,5000,500),random.randrange(100,1400,25),1000],
                    10:['m','had','pieces of cloth each measuring','m.','She used','cm of cloth from each piece.',
                        'How much cloth had she left altogether?','Give your answer in m.',
                        randint(4,10),random.randrange(1500,5000,500),random.randrange(100,500,25),100],
                    11:['m','purchased','rolls of ribbon each containing','m of ribbon.','She cut out','cm of ribbon from each roll to make bows.',
                        'What is the total length of ribbon she had left on the rolls.','Give your answer in m.',
                        randint(4,10),random.randrange(1500,5000,500),random.randrange(100,1400,25),100],
                    12:['m','bought','spools each containing','m of string.','She gave away','cm of string from each spool to her friends.',
                        'How much string had she left altogether?','Give your answer in m.',
                        randint(4,10),random.randrange(1500,5000,500),random.randrange(100,1400,25),100],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]
        self.item7 = self.Dict[self.key][7]

        self.number1 = self.Dict[self.key][8]
        self.weight1 = self.Dict[self.key][9]
        self.weight2 = self.Dict[self.key][10]
        self.number2 = self.Dict[self.key][11]
        
        self.answer = round(self.number1 * float(self.weight1-self.weight2)/self.number2,2)
                              
        self.problem = self.girl1+" "+self.item1+" "+str(self.number1)+" "+self.item2+" "+str(float(self.weight1)/self.number2)+" "+self.item3+"<br>"
        self.problem = self.problem + self.item4+" "+str(self.weight2)+" "+self.item5+"<br>"
        self.problem = self.problem + self.item6+"<br>"
        self.problem = self.problem + self.item7+"<br><br>"
        self.problem = self.problem + "Round off your answer to 2 decimal places"
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,str(self.answer),self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'CheckAnswerType':1}

    def ExplainType11(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "kAYGK9TdomA";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemType12(self):
        '''e.g.:Mary has 5 lambs each having a mass of 12 kg.
                Mary shears 1200 grams of wool from each lamb.
                What is the total mass of the lambs after the shearing?
                Give your answer in gm.'''
                  
        self.girl1 = random.choice(PersonName.GirlName)

        self.Dict = {1:['gm','has','lambs each having a mass of','kg.','She shears','grams of wool from each lamb.',
                        'What is the total mass of the lambs after the shearing?','Give your answer in gm.',
                        randint(8,100),random.randrange(10000,20000,500),random.randrange(1000,2000,25),1000],
                     2:['gm','has','bags each containing','kg of rice.','She removes','grams of rice from each bag.',
                        'What is the total mass of rice she has now?','Give your answer in gm.',
                        randint(4,10),random.randrange(10000,20000,500),random.randrange(1000,2000,25),1000],
                    3:['gm','has','bags each containing','kg of apples.','She throws away','grams of rotten apples from each bag.',
                       'Find the total mass of apples she is left with.','Give your answer in gm.',
                       randint(4,10),random.randrange(10000,20000,500),random.randrange(1000,2000,25),1000],
                    4:['gm','bought','watermelons each having a mass of','kg.','She removed','grams of skin from each watermelon.',
                       'What was the total mass of flesh inside the watermelons?','Give your answer in gm.',
                       randint(4,10),random.randrange(1500,5000,500),random.randrange(100,200,25),1000],
                    5:['gm','had','tins of cookies, each with a mass of','kg.','If each empty tin had a mass of','grams,',
                       'find the total mass of cookies that she had.','Give your answer in gm.',
                       randint(4,10),random.randrange(1500,5000,500),random.randrange(100,200,25),1000],
                    6:['ml','bought','bottles of juice each containing','litres of juice.','She drank','ml of juice from each bottle.',
                       'How much juice has she left altogether?','Give your answer in ml.',
                       randint(4,10),random.randrange(1500,5000,500),random.randrange(100,200,25),1000],
                    7:['ml','had','bottles of water each containing','litres of water.','She used','ml of water from each bottle.',
                       'Find the volume of water she had left altogether in the bottles.','Give your answer in ml.',
                       randint(4,10),random.randrange(1500,5000,500),random.randrange(100,200,25),1000],
                    8:['ml','had','cans of sugar syrup each containing','litres of syrup.','She used','ml of sugar syrup from each can.',
                       'Find the total volume of sugar syrup she had left.','Give your answer in ml.',
                       randint(4,10),random.randrange(1500,5000,500),random.randrange(100,200,25),1000],
                    9:['ml','purchased','tins of paint each containing','litres of paint.','She used',
                       'ml of paint from each tin for a painting project.','How much paint had she left altogether?','Give your answer in ml.',
                       randint(4,10),random.randrange(1500,5000,500),random.randrange(100,1400,25),1000],
                    10:['cm','had','pieces of cloth each measuring','m.','She used','cm of cloth from each piece.',
                        'How much cloth had she left altogether?','Give your answer in cm.',
                        randint(4,10),random.randrange(1500,5000,500),random.randrange(100,500,25),100],
                    11:['cm','purchased','rolls of ribbon each containing','m of ribbon.','She cut out','cm of ribbon from each roll to make bows.',
                        'What is the total length of ribbon she had left on the rolls.','Give your answer in cm.',
                        randint(4,10),random.randrange(1500,5000,500),random.randrange(100,1400,25),100],
                    12:['cm','bought','spools each containing','m of string.','She gave away','cm of string from each spool to her friends.',
                        'How much string had she left altogether?','Give your answer in cm.',
                        randint(4,10),random.randrange(1500,5000,500),random.randrange(100,1400,25),100],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]
        self.item7 = self.Dict[self.key][7]

        self.number1 = self.Dict[self.key][8]
        self.weight1 = self.Dict[self.key][9]
        self.weight2 = self.Dict[self.key][10]
        self.number2 = self.Dict[self.key][11]
        
        self.answer = self.number1 * (self.weight1-self.weight2)
                              
        self.problem = self.girl1+" "+self.item1+" "+str(self.number1)+" "+self.item2+" "+str(float(self.weight1)/self.number2)+" "+self.item3+"<br>"
        self.problem = self.problem + self.item4+" "+str(self.weight2)+" "+self.item5+"<br>"
        self.problem = self.problem + self.item6+"<br>"
        self.problem = self.problem + self.item7
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,str(self.answer),self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'CheckAnswerType':1}

    def ExplainType12(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "kAYGK9TdomA";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemType13(self):
        '''e.g.:Challenging Problem:
                A kite and a spool cost $29.75 together.
                Jason paid $228.55 for 12 kites and 5 spools.
                How much will Ted pay for 2 kites and 4 spools?'''
                  
        self.BoyNames = random.sample(PersonName.BoyName,2)
        self.boy1 = self.BoyNames[0]
        self.boy2 = self.BoyNames[1]
        
        self.Dict = {1:['A kite and a spool cost $','together.','paid $','for','kites and','spools.',
                        'How much will','pay for','kites and','spools?',random.randrange(300,1500,5),
                        random.randrange(300,1500,5),randint(2,20),randint(2,7),randint(2,20),randint(2,7)],
                     2:['A notebook and a pen cost $','together.','paid $','for','notebooks and','pens.','How much will','pay for',
                        'notebooks and','pens?',random.randrange(300,500,5),
                        random.randrange(125,350,5),randint(2,20),randint(2,7),randint(2,20),randint(2,7)],
                    3:['An eraser and a sharpener sell for $','together.','collected $','from the sale of','erasers and','sharpeners.',
                       'How much will','collect from the sale of','erasers and','sharpeners?',random.randrange(300,500,5),
                        random.randrange(125,350,5),randint(5,20),randint(5,20),randint(5,20),randint(5,20)],
                    4:['A bag and a T-shirt cost $','together.','paid $','for','bags and','T-shirts.','How much will','pay for','bags and','T-shirts?'
                       ,random.randrange(500,3000,5),random.randrange(500,2500,5),randint(2,20),randint(2,7),randint(2,20),randint(2,7)],                   
                    5:['A tie and a belt cost $','together.','paid $','for','ties and','belts.','How much will','pay for','ties and','belts?'
                       ,random.randrange(500,3000,5),random.randrange(500,2500,5),randint(2,20),randint(2,7),randint(2,20),randint(2,7)],
                    6:['A bar of chocolate and a box of cookies sell for $','together.','collected $','from the sale of','bars of chocolate and',
                       'boxes of cookies.','How much will','collect from the sale of','bars of chocolate and','boxes of cookies?'
                       ,random.randrange(200,600,5),random.randrange(300,600,5),randint(2,20),randint(2,7),randint(2,20),randint(2,7)],
                    7:['An apple and an orange sell for $','together.','collected $','from the sale of','apples and','oranges.',
                       'How much will','collect from the sale of','apples and','oranges?'
                       ,random.randrange(50,200,5),random.randrange(50,200,5),randint(2,20),randint(2,7),randint(2,20),randint(2,7)],
                    8:['A mug and a glass cost $','together.','paid $','for','mugs and','glasses.','How much will','pay for','mugs and','glasses?'
                       ,random.randrange(200,800,5),random.randrange(200,800,5),randint(2,20),randint(2,7),randint(2,20),randint(2,7)],
                    9:['A photo frame and a movie DVD cost $','together.','paid $','for','photo frames and','movie DVDs.','How much will','pay for',
                        'photo frames and','movie DVDs?',random.randrange(500,2000,5),random.randrange(700,2000,5),randint(2,7),randint(2,20)
                        ,randint(2,7),randint(2,20)],
                    10:['A pail and a tumbler cost $','together.','paid $','for','pails and','tumblers.','How much will','pay for','pails and','tumblers?'
                        ,random.randrange(200,800,5),random.randrange(200,800,5),randint(2,20),randint(2,7),randint(2,20),randint(2,7)],
                    11:['A flower pot and a plant sell for $','together.','collected $','from the sale of','flower pots and','plants.',
                        'How much will','collect from the sale of','flower pots and','plants?'
                        ,random.randrange(200,800,5),random.randrange(200,800,5),randint(2,20),randint(2,7),randint(2,20),randint(2,7)],
                    12:['A bag of soil and a bag of fertilizer cost $','together.','paid $','for','bags of soil and','bags of fertilizer.',
                        'How much will','pay for','bags of soil and','bags of fertilizer?'
                        ,random.randrange(200,800,5),random.randrange(200,800,5),randint(2,20),randint(2,7),randint(2,20),randint(2,7)],
                    13:['A toy car and a toy robot cost $','together.','paid $','for','toy cars and','toy robots.','How much will','pay for',
                        'toy cars and','toy robots?',random.randrange(200,800,5),random.randrange(200,800,5),randint(2,20),randint(2,7)
                        ,randint(2,20),randint(2,7)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.item1 = self.Dict[self.key][0]
        self.item2 = self.Dict[self.key][1]
        self.item3 = self.Dict[self.key][2]
        self.item4 = self.Dict[self.key][3]
        self.item5 = self.Dict[self.key][4]
        self.item6 = self.Dict[self.key][5]
        self.item7 = self.Dict[self.key][6]
        self.item8 = self.Dict[self.key][7]
        self.item9 = self.Dict[self.key][8]
        self.item10 = self.Dict[self.key][9]

        self.price1 = self.Dict[self.key][10]
        self.price2 = self.Dict[self.key][11]
        self.number1 = self.Dict[self.key][12]
        self.number2 = self.Dict[self.key][13]
        self.number3 = self.Dict[self.key][14]
        self.number4 = self.Dict[self.key][15]
        
        if self.number1==self.number3 and self.number2==self.number4:
            self.number3 = self.number1 + 1
            self.number4 = self.number2 + 1
            
        if self.number1 == self.number2:
            self.number1 = self.number2 + 1
            
        if self.number3 == self.number4:
            self.number3 = self.number4 + 1
        
        self.answer = self.number3 * float(self.price1)/100 + self.number4 * float(self.price2)/100
        
        self.cost1 = float(self.price1)/100+float(self.price2)/100
        self.cost2 = self.number1*float(self.price1)/100 + self.number2*float(self.price2)/100
        
        #adding zero if there is only one decimal place
        
        if len(str(self.cost1).partition(".")[2])==1:
            self.cost1 = str(self.cost1)+"0"
        
        if len(str(self.cost2).partition(".")[2])==1:
            self.cost2 = str(self.cost2)+"0"        
        
        self.problem = self.item1+str(self.cost1)+" "+self.item2+"<br>"
        self.problem = self.problem + self.boy1+" "+self.item3+str(self.cost2)
        self.problem = self.problem + " "+self.item4+" "+str(self.number1)+" "+self.item5+" "+str(self.number2)+" "+self.item6+"<br>"
        self.problem = self.problem + self.item7+" "+self.boy2+" "+self.item8+" "+str(self.number3)+" "+self.item9+" "+str(self.number4)+" "+self.item10
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,str(self.answer))
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"$",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType13",
                'CheckAnswerType':1}

    def ExplainType13(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>$"+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "44K3nCDtNWc";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemType14(self):
        '''e.g.:Challenging Problem:
                A bar of chocolate and a box of cookies have a mass of 0.375 kg together.
                If 12 bars of chocolate and 5 boxes of cookies have a mass of 2.265 kg, 
                find the mass of 2 bars of chocolate and 4 boxes of cookies.'''
        
        self.Dict = {1:['kg','A bar of chocolate and a box of cookies have a mass of','kg together.','If',
                        'bars of chocolate and','boxes of cookies have a mass of',
                        'kg,','find the mass of','bars of chocolate and','boxes of cookies.'
                        ,random.randrange(100,450,5),random.randrange(100,450,5),randint(2,20),randint(2,20),
                        randint(2,20),randint(2,20),1000],
                     2:['kg','A cake and a bun have a mass of','kg together.','If','cakes and','buns have a mass of',
                        'kg,','what is the mass of','cakes and','buns?'
                        ,random.randrange(100,450,5),random.randrange(100,450,5),randint(2,20),randint(2,20),
                        randint(2,20),randint(2,20),1000],
                    3:['kg','A bag of soil and a bag of fertilizer have a mass of','kg together.','If','bags of soil and',
                       'bags of fertilizer have a mass of','kg,','find the mass of','bags of soil and','bags of fertilizer.'
                       ,random.randrange(100,750,5),random.randrange(100,750,5),randint(2,20),randint(2,20),
                        randint(2,20),randint(2,20),1000],
                    4:['kg','A plate and a bowl have a mass of','kg together.','If','plates and','bowls have a mass of','kg,',
                       'what is the mass of','plates and','bowls?'
                       ,random.randrange(100,250,5),random.randrange(100,250,5),randint(2,20),randint(2,20),
                        randint(2,20),randint(2,20),1000],
                    5:['litres','A bottle of water and a can of juice have a volume of','litre together.','If',
                       'bottles of water and','cans of juice have a volume of','litres,','what is the volume of',
                       'bottles of water and','cans of juice?'
                       ,random.randrange(100,250,5),random.randrange(100,250,5),randint(5,20),randint(5,20),
                        randint(5,20),randint(5,20),1000],
                    6:['litres','A cup and a jar together have a capacity of','litre.','If',
                       'cups and','jars have a capacity of','litres,','find the capacity of','cups and','jars.'
                       ,random.randrange(100,250,5),random.randrange(100,250,5),randint(5,20),randint(5,20),
                        randint(5,20),randint(5,20),1000],
                    7:['litres','A pot and a bowl can hold','litres of soup together.','If','pots and','bowls can hold',
                       'litres of soup,','how much soup can','pots and','bowls hold?'
                       ,random.randrange(500,750,5),random.randrange(600,800,5),randint(5,20),randint(5,20),
                        randint(5,20),randint(5,20),1000],
                    8:['m','To make a dress and a skirt you need','m of fabric altogether.','To make','dresses and',
                       'skirts you need','m of fabric.','How much fabric will you need to make','dresses and','skirts?'
                       ,random.randrange(100,150,5),random.randrange(100,150,5),randint(5,20),randint(5,20),
                        randint(5,20),randint(5,20),100],
                    9:['m','To make a bow and a decorative flower it takes','m of ribbon altogether.','To make',
                       'bows and','decorative flowers you use','m of ribbon.','How much ribbon will you use to make',
                       'bows and','decorative flowers?'
                       ,random.randrange(20,80,5),random.randrange(20,80,5),randint(5,20),randint(5,20),
                        randint(5,20),randint(5,20),100],
                    10:['m<sup>2</sup>','A white tile and a black tile cover an area of','m<sup>2</sup> together.','If',
                        'white tiles and','black tiles cover an area of','m<sup>2</sup>,','find the area covered by','white tiles and',"black tiles."
                        ,random.randrange(25,75,5),random.randrange(25,75,5),randint(5,20),randint(5,20),
                        randint(5,20),randint(5,20),100],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]
        self.item7 = self.Dict[self.key][7]
        self.item8 = self.Dict[self.key][8]
        self.item9 = self.Dict[self.key][9]

        self.weight1 = self.Dict[self.key][10]
        self.weight2 = self.Dict[self.key][11]
        self.number1 = self.Dict[self.key][12]
        self.number2 = self.Dict[self.key][13]
        self.number3 = self.Dict[self.key][14]
        self.number4 = self.Dict[self.key][15]
        self.number5 = self.Dict[self.key][16]
        
        if self.number1==self.number3 and self.number2==self.number4:
            self.number3 = self.number1 + 1
            self.number4 = self.number2 + 1
            
        if self.number3 == self.number4:
            self.number3 = self.number4 + 1

        if self.number1 == self.number2:
            self.number1 = self.number2 + 1
        
        self.answer = self.number3 * float(self.weight1)/self.number5 + self.number4 * float(self.weight2)/self.number5
                              
        self.problem = self.item1+" "+str(float(self.weight1)/self.number5+float(self.weight2)/self.number5)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+str(self.number1)+" "+self.item4+" "+str(self.number2)+" "+self.item5+" "+str(self.number1*float(self.weight1)/self.number5 + self.number2*float(self.weight2)/self.number5)+" "+self.item6+"<br>"
        self.problem = self.problem + self.item7+" "+str(self.number3)+" "+self.item8+" "+str(self.number4)+" "+self.item9
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,str(self.answer),self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType14",
                'CheckAnswerType':1}

    def ExplainType14(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "44K3nCDtNWc";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
        
        if CheckAnswerType == 1:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswerType == 2:
            try:
                return (str(answer).lower()==str(InputAnswer).lower())
            except ValueError:
                return False            