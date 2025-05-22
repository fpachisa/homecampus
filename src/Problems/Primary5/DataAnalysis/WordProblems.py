'''
Created on Dec 15, 2011

Module: WordProblems
Generates "Word Problems on Data Analysis" problems for Primary 5

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

class WordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"easy":[self.GenerateProblemType1(),self.GenerateProblemType2(),self.GenerateProblemType3(),],
                            }
        try:
            return random.choice(self.ProblemType[level])
        except KeyError:
            return random.choice(random.choice(self.ProblemType.values()))
        #return self.GenerateProblemType7()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''                
        self.ProblemType = {1:"ProblemType1",2:"ProblemType2",3:"ProblemType3",
                            4:"ProblemType4",5:"ProblemType5a",6:"ProblemType5b"}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemType2(),3:self.GenerateProblemType3(),
                                    4:self.GenerateProblemType4(),5:self.GenerateProblemType5a(),6:self.GenerateProblemType5b(),}
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            3:["ProblemType3",],
                            4:["ProblemType4",],
                            5:["ProblemType5a","ProblemType5b"],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4()],
                                    5:[self.GenerateProblemType5a(),self.GenerateProblemType5b()],
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
        #return self.GenerateProblemType22()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5a":self.GenerateProblemType5a(),
                            "ProblemType5b":self.GenerateProblemType5b(),
                            }
        return self.ProblemType[problem_type]
                
    def GenerateProblemType1(self):
        '''e.g.:The table below shows the books that Louis borrowed from the library.
                What is the average number of pages that each book has?'''
           
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.PersonName)
        self.Dict = {1:['pages','The table below shows the books that','borrowed from the library.','Title','Number of pages',
                        'Exotic Cars','Dinosaurs for Kids','365 Bedtime Stories','A Desert Habitat','Art',
                        'What is the average number of pages that each book has?',randint(30,200),randint(30,200),randint(400,600),
                        randint(30,200),randint(30,200),],
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
        self.item10 = self.Dict[self.key][10]
        
        self.number1 = self.Dict[self.key][11]
        self.number2 = self.Dict[self.key][12]
        self.number3 = self.Dict[self.key][13]
        self.number4 = self.Dict[self.key][14]
        self.number5 = self.Dict[self.key][15]
        
        self.problem = self.item1+" "+self.name+" "+self.item2+"<br><br>"
        self.problem = self.problem + "<div><table id='ProblemTable'>"
        self.problem = self.problem + "<tr><th>"+self.item3+"</th><th>"+self.item4+"</th></tr>"
        self.problem = self.problem + "<tr><td>"+self.item5+"</td><td>"+str(self.number1)+"</td></tr>"
        self.problem = self.problem + "<tr class='alt'><td>"+self.item6+"</td><td>"+str(self.number2)+"</td></tr>"
        self.problem = self.problem + "<tr><td>"+self.item7+"</td><td>"+str(self.number3)+"</td></tr>"
        self.problem = self.problem + "<tr class='alt'><td>"+self.item8+"</td><td>"+str(self.number4)+"</td></tr>"
        self.problem = self.problem + "<tr><td>"+self.item9+"</td><td>"+str(self.number5)+"</td></tr>"
        self.problem = self.problem + "</table></div><br>"
        self.problem = self.problem + self.item10+"<br>"
        self.flag = randint(1,2)
        if self.flag == 1:    
            self.problem = self.problem + "(Round off to the nearest whole number)"
            self.answer = int(round(float(self.number1+self.number2+self.number3+self.number4+self.number5)/5,0))
        else:     
            self.answer = float(self.number1+self.number2+self.number3+self.number4+self.number5)/5
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit
                }

    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "ZIOUUQJt_tQ";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
                
    def GenerateProblemType2(self):
        '''e.g.:The average age of 3 girls is 11 years. The average age of 2 of the girls is 12 years.
                What is the age of the third girl?'''
           
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.Dict = {1:['years','The average age of','girls is','years.','The average age of','of the girls is','years.',
                        'What is the age of the','girl?',randint(3,8),randint(10,20),randint(10,20)],
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
        
        self.girls1 = self.number1
        self.girls2 = self.number1 - 1
        self.age = self.number2
        self.average2 = self.number3
        
        div,mod = divmod(self.age + self.girls2*self.average2,self.girls1)
        while mod!=0:
            self.age = self.age + 1
            div,mod = divmod(self.age + self.girls2*self.average2,self.girls1)
        
        self.average1 = div
        self.answer = self.age
        self.problem = self.item1+" "+str(self.girls1)+" "+self.item2+" "+str(self.average1)+" "+self.item3+"<br><br>"
        self.problem = self.problem + self.item4+" "+str(self.girls2)+" "+self.item5+" "+str(self.average2)+" "+self.item6+"<br><br>"
        self.problem = self.problem + self.item7+" last "+self.item8

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit
                }

    def ExplainType2(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "mVakD6TGBpc";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
                
    def GenerateProblemType3(self):
        '''e.g.:A team of 5 friends gets an average pocket money of $15 per week. 
                A sixth friend who gets $21 as pocket money per week joins their team. 
                What is the average pocket money of the team now?'''
           
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.Dict = {1:['$','A team of','friends gets an average pocket money of $','per week.','A','friend who gets $',
                        'as pocket money per week joins their team.','What is the average pocket money of the team now?',
                        randint(3,10),randint(10,30),randint(10,30)],
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
        
        self.ordinal = {4:"fourth",5:"fifth",6:"sixth",7:"seventh",8:"eighth",9:"ninth",10:"tenth",11:"eleventh"}
        self.flag = randint(1,2)
        
        self.problem = self.item1+" "+str(self.number1)+" "+self.item2+str(self.number2)+" "+self.item3+"<br><br>"
        self.problem = self.problem + self.item4+" "+self.ordinal[self.number1+1]+" "+self.item5+str(self.number3)+" "+self.item6+"<br><br>"
        self.problem = self.problem + self.item7+"<br><br>"
        if self.flag == 1:
            self.problem = self.problem + "(Round off your answer to the nearest whole number)"
            self.answer = int(round(float(self.number1*self.number2 + self.number3)/(self.number1+1),0))
        elif self.flag == 2:
            self.problem = self.problem + "(Round off your answer to two decimal places)"
            self.answer = round(float(self.number1*self.number2 + self.number3)/(self.number1+1),2)

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':"",'dollar_unit':"$"
                }

    def ExplainType3(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+unit+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "lWJ4j5mMKec";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
                
    def GenerateProblemType4(self):
        '''e.g.:Amy, Dennis and Ruby have an average salary of $2650 per month.
                Amy earns twice as much as Dennis and Ruby earns $260 more than Amy each month.
                What is Ruby's monthly salary?'''
           
        self.names = random.sample(PersonName.PersonName,3)
        self.complexity_level = "difficult"
        self.HCScore = 7
        
        self.ordinal = {1:"same",2:"twice as much",3:"thrice as much"}
        self.Dict = {1:['$',',','and','have an average salary of $','per month.','earns','as','and',
                        'earns $','more than','each month.','What is',"'s monthly salary?",
                        randint(2500,3500),randint(1,3),random.randrange(300,1000,10)],
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
        self.item10 = self.Dict[self.key][10]
        self.item11 = self.Dict[self.key][11]
        self.item12 = self.Dict[self.key][12]
                
        self.number1 = self.Dict[self.key][13]
        self.number2 = self.Dict[self.key][14]
        self.number3 = self.Dict[self.key][15]
        
        self.salary1 = self.number1
        self.salary2 = self.number1 * self.number2
        self.salary3 = self.salary2 + self.number3
        while (self.salary1+self.salary2+self.salary3)%3 != 0:
            self.number3 = self.number3 + 1
            self.salary3 = self.salary2 + self.number3
        
        self.average = (self.salary1+self.salary2+self.salary3) / 3
 
        self.answer = self.salary3
                 
        self.problem = self.names[0]+self.item1+" "+self.names[1]+" "+self.item2+" "+self.names[2]+" "+self.item3+str(self.average)+" "+self.item4+"<br><br>"
        self.problem = self.problem +self.names[0]+" "+self.item5+" "+self.ordinal[self.number2]+" "+self.item6+" "+self.names[1]+" "+self.item7+" "+self.names[2]+" "+self.item8+str(self.number3)+" "+self.item9+" "+self.names[0]+" "+self.item10+"<br><br>"
        self.problem = self.problem + self.item11+" "+self.names[2]+self.item12

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':"",'dollar_unit':"$"
                }

    def ExplainType4(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+unit+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "Suyj2fchdlw";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
                
    def GenerateProblemType5a(self):
        '''e.g.:The following table shows the number of children in 205 families in a township in 2010.
                What was the average number of children per family in 2010?'''

        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.Dict = {1:['children','The following table shows the number of children in','families in a township in',
                        'What was the average number of children per family in','?','(Round off your answer to 2 decimal places.)',
                        'number of families','number of children in the family',
                        randint(150,800),randint(1300,1500),randint(1800,2100),randint(1800,2100),randint(700,1000),randint(2000,2010)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.header1 = self.Dict[self.key][6]
        self.header2 = self.Dict[self.key][7]
                        
        self.number1 = self.Dict[self.key][8]
        self.number2 = self.Dict[self.key][9]
        self.number3 = self.Dict[self.key][10]
        self.number4 = self.Dict[self.key][11]
        self.number5 = self.Dict[self.key][12]
        self.year = self.Dict[self.key][13]
        
        self.children0 = int(self.number2*self.number1/10000)
        self.children1 = int(self.number3*self.number1/10000)
        self.children3 = int(self.number4*self.number1/10000)
        self.children4 = int(self.number5*self.number1/10000)
        self.children2 = self.number1 - (self.children0+self.children1+self.children3+self.children4)
                
        self.average = round(float(self.children0*0+self.children1*1+self.children2*2+self.children3*3+self.children4*4)/self.number1,2)
 
        self.answer = self.average
                 
        self.problem = self.item1+" "+str(self.number1)+" "+self.item2+" "+str(self.year)+"<br><br>"
        self.problem = self.problem + "<div><table id='ProblemTable'>"
        self.problem = self.problem + "<tr><th>"+self.header1+"</th><th>"+self.header2+"</th></tr>"
        self.problem = self.problem + "<tr><td>"+str(self.children0)+"</td><td>"+str(0)+"</td></tr>"
        self.problem = self.problem + "<tr class='alt'><td>"+str(self.children1)+"</td><td>"+str(1)+"</td></tr>"
        self.problem = self.problem + "<tr><td>"+str(self.children2)+"</td><td>"+str(2)+"</td></tr>"
        self.problem = self.problem + "<tr class='alt'><td>"+str(self.children3)+"</td><td>"+str(3)+"</td></tr>"
        self.problem = self.problem + "<tr><td>"+str(self.children4)+"</td><td>"+str(4)+"</td></tr>"      
        self.problem = self.problem + "</table></div><br>"
        self.problem = self.problem + self.item3+" "+str(self.year)+self.item4+"<br><br>"
        self.problem = self.problem + self.item5
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5a(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5a",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':""
                }

    def ExplainType5a(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "pbVrov3tZ3A";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
                
    def GenerateProblemType5b(self):
        '''e.g.:The following table shows the number of children in 205 families in a township in 2010.
                What was the average number of children per family in 2010?'''

        self.complexity_level = "difficult"
        self.HCScore = 7
        
        self.Dict = {1:['children','The following table shows the number of children in','families in a township in',
                        'In',', the number of children in the township increased by','while the total number of families remained unchanged.',
                        'What was the average number of children per family in the township in','?','(Round off your answer to 2 decimal places.)',
                        'number of families','number of children in the family',
                        randint(150,800),randint(1300,1500),randint(1800,2100),randint(1800,2100),randint(700,1000),randint(2000,2010),randint(5,15)],
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
        self.header1 = self.Dict[self.key][9]
        self.header2 = self.Dict[self.key][10]
                        
        self.number1 = self.Dict[self.key][11]
        self.number2 = self.Dict[self.key][12]
        self.number3 = self.Dict[self.key][13]
        self.number4 = self.Dict[self.key][14]
        self.number5 = self.Dict[self.key][15]
        self.year = self.Dict[self.key][16]
        self.number6 = self.Dict[self.key][17]
        
        self.children0 = int(self.number2*self.number1/10000)
        self.children1 = int(self.number3*self.number1/10000)
        self.children3 = int(self.number4*self.number1/10000)
        self.children4 = int(self.number5*self.number1/10000)
        self.children2 = self.number1 - (self.children0+self.children1+self.children3+self.children4)
        self.ChildrenIncreased = int(self.number1 * self.number6/100)
                
        self.average = round(float(self.children0*0+self.children1*1+self.children2*2+self.children3*3+self.children4*4+self.ChildrenIncreased)/self.number1,2)
 
        self.answer = self.average
                 
        self.problem = self.item1+" "+str(self.number1)+" "+self.item2+" "+str(self.year)+"<br><br>"
        self.problem = self.problem + "<div><table id='ProblemTable'>"
        self.problem = self.problem + "<tr><th>"+self.header1+"</th><th>"+self.header2+"</th></tr>"
        self.problem = self.problem + "<tr><td>"+str(self.children0)+"</td><td>"+str(0)+"</td></tr>"
        self.problem = self.problem + "<tr class='alt'><td>"+str(self.children1)+"</td><td>"+str(1)+"</td></tr>"
        self.problem = self.problem + "<tr><td>"+str(self.children2)+"</td><td>"+str(2)+"</td></tr>"
        self.problem = self.problem + "<tr class='alt'><td>"+str(self.children3)+"</td><td>"+str(3)+"</td></tr>"
        self.problem = self.problem + "<tr><td>"+str(self.children4)+"</td><td>"+str(4)+"</td></tr>"      
        self.problem = self.problem + "</table></div><br>"
        self.problem = self.problem + self.item3+" "+str(self.year+1)+self.item4+" "+str(self.ChildrenIncreased)+" "+self.item5+"<br><br>"
        self.problem = self.problem + self.item6+" "+str(self.year+1)+self.item7+"<br>"
        self.problem = self.problem + self.item8
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5b(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5b",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit,'dollar_unit':""
                }

    def ExplainType5b(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "pbVrov3tZ3A";
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