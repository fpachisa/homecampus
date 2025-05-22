'''
Created on Sep 16, 2011

Module: WordProblems
Generates "Word Problems on Ratio" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''
import random
import string
from random import randint
from Utils import LcmGcf
from Problems import PersonName


class WordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        ''' first grouping the questions as per problem type in the ppt and then first randomly picking the problem type and then problem from the problem type'''
        ProblemList = [[self.GenerateProblemType1a(),self.GenerateProblemType1b(),self.GenerateProblemType1c(),self.GenerateProblemType1d()],
                       [self.GenerateProblemType2()],
                       [self.GenerateProblemType3()],
                       [self.GenerateProblemType4()],
                       [self.GenerateProblemType5()],
                       [self.GenerateProblemType6()],
                       [self.GenerateProblemType7()],
                       [self.GenerateProblemType8()],
                       [self.GenerateProblemType9()],
                       ]
        return random.choice(random.choice(ProblemList))
        #return self.GenerateProblemType9()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1a","ProblemType1b","ProblemType1c","ProblemType1d"],
                            2:["ProblemType2",],
                            3:["ProblemType3",],
                            4:["ProblemType4",],
                            5:["ProblemType5",],
                            6:["ProblemType6",],
                            7:["ProblemType7",],
                            8:["ProblemType8",],
                            9:["ProblemType9",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1a(),self.GenerateProblemType1b(),self.GenerateProblemType1c(),self.GenerateProblemType1d()],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4()],
                                    5:[self.GenerateProblemType5()],
                                    6:[self.GenerateProblemType6()],
                                    7:[self.GenerateProblemType7()],
                                    8:[self.GenerateProblemType8()],
                                    9:[self.GenerateProblemType9()],
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
        self.ProblemType = {"ProblemType1a":self.GenerateProblemType1a(),
                            "ProblemType1b":self.GenerateProblemType1b(),
                            "ProblemType1c":self.GenerateProblemType1c(),
                            "ProblemType1d":self.GenerateProblemType1d(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),
                            "ProblemType8":self.GenerateProblemType8(),
                            "ProblemType9":self.GenerateProblemType9(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1a(self):
        '''e.g.:300 children participated in a painting contest. 120 of them were boys. 
                Find the ratio of the number of boys to the number of girls.
              Express the ratio in its simplest form.'''

        self.Dict = {1:["children participated in a painting contest.","of them were boys.",
                        "Find the ratio of the number of boys to the number of girls.",
                        "(Express the ratio in its simplest form and input it as a:b)",randint(1,6),randint(1,6),randint(5,10)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.item1 = self.Dict[self.key][0]
        self.item2 = self.Dict[self.key][1]
        self.item3 = self.Dict[self.key][2]
        self.item4 = self.Dict[self.key][3]
        self.number1 = self.Dict[self.key][4]
        self.number2 = self.Dict[self.key][5]
        self.number3 = self.Dict[self.key][6] 
        
        self.boys = self.number1 * self.number3
        self.girls = self.number2 * self.number3
        self.total = self.boys + self.girls
                
        self.problem = str(self.total)+" "+self.item1+" "+str(self.boys)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+"<br>"
        self.problem = self.problem + self.item4     

        gcf = LcmGcf.LcmGcf().find_gcf(self.boys,self.girls)
        self.answer = str(self.boys/gcf)+":"+str(self.girls/gcf) 
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":1}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType1a"}

    def GenerateProblemType1b(self):
        '''e.g.:300 children participated in a painting contest. 120 of them were boys. 
                Find the ratio of the number of girls to the number of boys.
              Express the ratio in its simplest form.'''

        self.Dict = {1:["children participated in a painting contest.","of them were boys.",
                        "Find the ratio of the number of girls to the number of boys.",
                        "(Express the ratio in its simplest form and input it as a:b)",randint(1,6),randint(1,6),randint(5,10)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.item1 = self.Dict[self.key][0]
        self.item2 = self.Dict[self.key][1]
        self.item3 = self.Dict[self.key][2]
        self.item4 = self.Dict[self.key][3]
        self.number1 = self.Dict[self.key][4]
        self.number2 = self.Dict[self.key][5]
        self.number3 = self.Dict[self.key][6] 
        
        self.boys = self.number1 * self.number3
        self.girls = self.number2 * self.number3
        self.total = self.boys + self.girls
                
        self.problem = str(self.total)+" "+self.item1+" "+str(self.boys)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+"<br>"
        self.problem = self.problem + self.item4
                
        gcf = LcmGcf.LcmGcf().find_gcf(self.boys,self.girls)
        self.answer = str(self.girls/gcf)+":"+str(self.boys/gcf) 
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":1}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType1b"}

    def GenerateProblemType1c(self):
        '''e.g.:300 children participated in a painting contest. 120 of them were boys. 
                Find the ratio of the number of boys to the total number of children.
              Express the ratio in its simplest form.'''

        self.Dict = {1:["children participated in a painting contest.","of them were boys.",
                        "Find the ratio of the number of boys to the total number of children.",
                        "(Express the ratio in its simplest form and input it as a:b)",randint(1,6),randint(1,6),randint(5,10)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.item1 = self.Dict[self.key][0]
        self.item2 = self.Dict[self.key][1]
        self.item3 = self.Dict[self.key][2]
        self.item4 = self.Dict[self.key][3]
        self.number1 = self.Dict[self.key][4]
        self.number2 = self.Dict[self.key][5]
        self.number3 = self.Dict[self.key][6] 
        
        self.boys = self.number1 * self.number3
        self.girls = self.number2 * self.number3
        self.total = self.boys + self.girls
                
        self.problem = str(self.total)+" "+self.item1+" "+str(self.boys)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+"<br>"
        self.problem = self.problem + self.item4
                
        gcf = LcmGcf.LcmGcf().find_gcf(self.boys,self.total)
        self.answer = str(self.boys/gcf)+":"+str(self.total/gcf) 
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":1}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType1c"}

    def GenerateProblemType1d(self):
        '''e.g.:300 children participated in a painting contest. 120 of them were boys. 
                Find the ratio of the number of girls to the total number of children.
              Express the ratio in its simplest form.'''

        self.Dict = {1:["children participated in a painting contest.","of them were boys.",
                        "Find the ratio of the number of girls to the total number of children.",
                        "(Express the ratio in its simplest form and input it as a:b)",randint(1,6),randint(1,6),randint(5,10)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.item1 = self.Dict[self.key][0]
        self.item2 = self.Dict[self.key][1]
        self.item3 = self.Dict[self.key][2]
        self.item4 = self.Dict[self.key][3]
        self.number1 = self.Dict[self.key][4]
        self.number2 = self.Dict[self.key][5]
        self.number3 = self.Dict[self.key][6] 
        
        self.boys = self.number1 * self.number3
        self.girls = self.number2 * self.number3
        self.total = self.boys + self.girls
                
        self.problem = str(self.total)+" "+self.item1+" "+str(self.boys)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+"<br>"
        self.problem = self.problem + self.item4
                
        gcf = LcmGcf.LcmGcf().find_gcf(self.girls,self.total)
        self.answer = str(self.girls/gcf)+":"+str(self.total/gcf) 
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":1}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType1d"}

    def ExplainType1(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "QaZlJaiCrHc";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.:Mia has 20 black marbles and 15 red marbles.
                Alex has 8 black marbles and some red marbles.
                The ratio of the number of black marbles to the number of red marbles
                that Mia has is the same as the ratio of the number of black marbles 
                to the number of red marbles that Alex has.
                Find the number of red marbles that Alex has.'''

        self.Dict = {1:["red marbles","has","black marbles and","red marbles.","has","black marbles and some red marbles.",
                        "The ratio of the number of black marbles to the number of red marbles", "that",
                        "has is the same as the ratio of the number of black marbles","to the number of red marbles that","has.",
                        "Find the number of red marbles that","has.",
                        randint(1,8),randint(1,8),randint(2,8),randint(2,8)],
                     }
        self.names = random.sample(PersonName.PersonName,2)
        self.name1 = self.names[0]
        self.name2 = self.names[1]
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
        self.number4 = self.Dict[self.key][16] 
        
        self.MiaBlackMarbles = self.number1 * self.number3
        self.MiaRedMarbles = self.number2 * self.number3
        self.AlexBlackMarbles = self.number1 * self.number4
        self.answer = str(self.number2 * self.number4)
                
        self.problem = self.name1+" "+self.item1+" "+str(self.MiaBlackMarbles)+" "+self.item2+" "+str(self.MiaRedMarbles)+" "+self.item3+"<br>"
        self.problem = self.problem + self.name2+" "+self.item4+" "+str(self.AlexBlackMarbles)+" "+self.item5+"<br>"
        self.problem = self.problem + self.item6+"<br>"
        self.problem = self.problem + self.item7+" "+self.name1+" "+self.item8+"<br>"
        self.problem = self.problem + self.item9+" "+self.name2+" "+self.item10+"<br>"
        self.problem = self.problem + self.item11+" "+self.name2+" "+self.item12
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":2}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType2"}

    def ExplainType2(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "sKH47_xNKSM";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):
        '''e.g.:Mac has 200 white and black horses on his farm.
                The ratio of the number of black horses to the number of white horses is 2 : 3.
                Find the number of white horses on Mac's farm.'''

        self.Dict = {1:["white horses","has","white and black horses on his farm.",
                        "The ratio of the number of black horses to the number of white horses is",":",".",
                        "Find the number of white horses on","'s farm.",
                        randint(3,10),randint(1,7),randint(1,7)],
                     }

        self.name1 = random.choice(PersonName.BoyName)
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
        
        self.total = self.number1*(self.number2+self.number3)
        self.answer = str(self.number1 * self.number3)
        
        #making sure that ratios are in simplest form
        gcf = LcmGcf.LcmGcf().find_gcf(self.number2,self.number3)
        self.number2 = self.number2/gcf
        self.number3 = self.number3/gcf
                                
        self.problem = self.name1+" "+self.item1+" "+str(self.total)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+str(self.number2)+" "+self.item4+" "+str(self.number3)+self.item5+"<br>"
        self.problem = self.problem + self.item6+" "+self.name1+self.item7
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":2}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType3"}

    def ExplainType3(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "RUq7_TOgFbA";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):
        '''e.g.:Rita is 12 years 6 months old. 
                Jet is 4 years 2 months younger to Rita.
                Find the ratio of Jet's age to Rita's age.
                Express the ratio in its simplest form.'''

        self.names = random.sample(PersonName.PersonName,2)
        self.name1 = self.names[0]
        self.name2 = self.names[1]
        self.Dict = {1:[self.name1,self.name2,"is","years","months old.","is","years","months younger to",".",
                        "Find the ratio of","'s age to","'s age.","Express the ratio in its simplest form.",
                        randint(2,8),randint(13,20),12]
                     }
        
        self.key = randint(1,len(self.Dict))
        self.name1 = self.Dict[self.key][0]
        self.name2 = self.Dict[self.key][1]
        self.item1 = self.Dict[self.key][2]
        self.item2 = self.Dict[self.key][3]
        self.item3 = self.Dict[self.key][4]
        self.item4 = self.Dict[self.key][5]
        self.item5 = self.Dict[self.key][6]
        self.item6 = self.Dict[self.key][7]
        self.item7 = self.Dict[self.key][8]
        self.item8 = self.Dict[self.key][9]
        self.item9 = self.Dict[self.key][10]
        self.item10 = self.Dict[self.key][11]
        self.item11 = self.Dict[self.key][12]
        self.number1 = self.Dict[self.key][13]
        self.number2 = self.Dict[self.key][14]
        self.number3 = self.Dict[self.key][15]
        
        self.number11 = randint(1,self.number1-1)
        
        self.months1 = self.number1 * self.number2
        if (self.months1%12==0):
            self.number2 = self.number2 + 1
            self.months1 = self.number1 * self.number2
                
        self.months11 = self.number11 * self.number2
        self.diff = self.months1 - self.months11
        if (self.diff%12==0):
            self.number2 = self.number2 + 1
            self.months1 = self.number1 * self.number2
            self.months11 = self.number11 * self.number2
            self.diff = self.months1 - self.months11       
        
        self.year1, self.months1 = divmod(self.months1,self.number3)
        self.year11, self.months11 = divmod(self.diff,self.number3)      
                
        #making sure that ratios are in simplest form
        gcf = LcmGcf.LcmGcf().find_gcf(self.number1,self.number11)
        self.number1 = self.number1/gcf
        self.number11 = self.number11/gcf
        
        self.answer = str(self.number11)+":"+str(self.number1)                      
        self.problem = self.name1+" "+self.item1+" "+str(self.year1)+" "+self.item2+" "+str(self.months1)+" "+self.item3+"<br>"
        if self.year11 == 0:
            self.problem = self.problem + self.name2+" "+self.item4+" "+str(self.months11)+" "+self.item6+" "+self.name1+self.item7+"<br>"
        elif self.year11>1:
            self.problem = self.problem + self.name2+" "+self.item4+" "+str(self.year11)+" "+self.item5+" "+str(self.months11)+" "+self.item6+" "+self.name1+self.item7+"<br>"           
        elif self.year11<=1:
            self.problem = self.problem + self.name2+" "+self.item4+" "+str(self.year11)+" year "+str(self.months11)+" "+self.item6+" "+self.name1+self.item7+"<br>"
        self.problem = self.problem + self.item8+" "+self.name2+self.item9+" "+self.name1+self.item10+"<br>"
        self.problem = self.problem + self.item11 
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":1}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType4"}

    def ExplainType4(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "Noos-cIz0Us";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):
        '''e.g.:Following ingredients are used to make strawberry shake for 4 children:
                - 12 cups milk
                - 8 cups strawberries
                - 4 cups ice-cubes
                What is the quantity of milk that you will need to make strawberry shake for 7 children?'''

        self.Dict = {1:["cups","Following ingredients are used to make strawberry shake for","children:","cups milk",
                        "cups strawberries","cups ice-cubes","What is the quantity of",
                        "that you will need to make strawberry shake for","children?",3,2,1,randint(3,8),randint(3,12),random.choice(["milk","strawberries","ice-cubes"])]
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
        self.ratio1 = self.Dict[self.key][9]
        self.ratio2 = self.Dict[self.key][10]
        self.ratio3 = self.Dict[self.key][11]
        self.number1 = self.Dict[self.key][12]
        self.number2 = self.Dict[self.key][13]
        self.item = self.Dict[self.key][14]
        
        if self.item == "milk":
            self.answer = str(self.ratio1 * self.number2)
        elif self.item == "strawberries":
            self.answer = str(self.ratio2 * self.number2)
        elif self.item == "ice-cubes":
            self.answer = str(self.ratio3 * self.number2)
            
        self.problem = self.item1+" "+str(self.number1)+" "+self.item2+"<br><br>"
        self.problem = self.problem + "- "+str(self.ratio1*self.number1)+" "+self.item3+"<br>"
        self.problem = self.problem + "- "+str(self.ratio2*self.number1)+" "+self.item4+"<br>"
        self.problem = self.problem + "- "+str(self.ratio3*self.number1)+" "+self.item5+"<br><br>"
        self.problem = self.problem + self.item6+" "+self.item+" "+self.item7+" "+str(self.number2)+" "+self.item8
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":2}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType5"}

    def ExplainType5(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "qnbdjcA_ycg";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):
        '''e.g.:Town A has 2/5 the population of Town B.
                What is the ratio of the population of Town A to the population of Town B?'''

        self.Dict = {1:["Town A has","the population of Town B.","What is the ratio of the population of Town A to the population of Town B?",
                        randint(2,12)]
                     }
        
        self.key = randint(1,len(self.Dict))
        self.item1 = self.Dict[self.key][0]
        self.item2 = self.Dict[self.key][1]
        self.item3 = self.Dict[self.key][2]
        self.number1 = self.Dict[self.key][3]
        
        self.number2 = randint(1,self.number1-1)
        #making sure that ratios are in simplest form
        gcf = LcmGcf.LcmGcf().find_gcf(self.number1,self.number2)
        self.number1 = self.number1/gcf
        self.number2 = self.number2/gcf
            
        self.problem = "<table class='FractionsTable'><tr>"
        self.problem = self.problem + "<td>"+self.item1+"&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.number2)+"&nbsp;</u><br>&nbsp;"+str(self.number1)+"</td>"
        self.problem = self.problem + "<td>&nbsp;"+self.item2+"</td></tr></table>"
        self.problem = self.problem + self.item3
        
        self.answer = str(self.number2)+":"+str(self.number1)
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":1}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType6"}

    def ExplainType6(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "gRSwPW2SQPM";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):
        '''e.g.:A piece of fabric is coloured green, white and pink in the ratio 3 : 2 : 1.
                If 45 cm of the fabric is coloured green, 
                what is the length of the fabric that is coloured white?'''

        self.Dict = {1:["cm","A piece of fabric is coloured green, white and pink in the ratio",":",":",".",
                        "If","cm of the fabric is coloured","what is the length of the fabric that is coloured","?",
                        random.sample(["green","white","pink"],2),randint(3,8),randint(3,8)]
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
        self.colour = self.Dict[self.key][9]
        self.ratio1 = self.Dict[self.key][10]
        self.number1 = self.Dict[self.key][11]
        
        self.ratio2 = randint(2,self.ratio1-1)
        self.ratio3 = randint(1,self.ratio2-1)
        
        #making sure that ratios are in simplest form
        gcf = LcmGcf.LcmGcf().find_gcf(LcmGcf.LcmGcf().find_gcf(self.ratio1,self.ratio2),self.ratio3)
        self.ratio1 = self.ratio1/gcf
        self.ratio2 = self.ratio2/gcf
        self.ratio3 = self.ratio3/gcf
        
        if self.colour[0] == "green":
            self.length = self.ratio1 * self.number1
        elif self.colour[0] == "white":
            self.length = self.ratio2 * self.number1
        elif self.colour[0] == "pink":
            self.length = self.ratio3 * self.number1

        if self.colour[1] == "green":
            self.answer = self.ratio1 * self.number1
        elif self.colour[1] == "white":
            self.answer = self.ratio2 * self.number1
        elif self.colour[1] == "pink":
            self.answer = self.ratio3 * self.number1
                                                
        self.problem = self.item1+" "+str(self.ratio1)+" "+self.item2+" "+str(self.ratio2)+" "+self.item3+" "+str(self.ratio3)+self.item4+"<br>"
        self.problem = self.problem + self.item5+" "+str(self.length)+" "+self.item6+" "+self.colour[0]+",<br>"
        self.problem = self.problem + self.item7+" "+self.colour[1]+self.item8
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":2}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType7"}

    def ExplainType7(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "uLU3WoyzN6s";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):
        '''e.g.:160 m of fence is used to border a 50-m long rectangular field.
                Find the ratio of the length to the width of this rectangular field.'''

        self.Dict = {1:["m","m of fence is used to border a","-m long rectangular field.",
                        "Find the ratio of the length to the width of this rectangular field.",
                        randint(2,8),randint(2,8)]
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.ratio1 = self.Dict[self.key][4]
        self.number1 = self.Dict[self.key][5]
        
        self.ratio2 = randint(1,self.ratio1-1)
        
        #making sure that ratios are in simplest form
        gcf = LcmGcf.LcmGcf().find_gcf(self.ratio1,self.ratio2)
        self.ratio1 = self.ratio1/gcf
        self.ratio2 = self.ratio2/gcf
        
        self.length = self.ratio1 * self.number1
        self.breadth = self.ratio2 * self.number1        
        self.perimeter = 2 *(self.length + self.breadth)
        
        self.answer = str(self.ratio1)+":"+str(self.ratio2)                                               
        
        self.problem = str(self.perimeter)+" "+self.item1+" "+str(self.length)+self.item2+"<br>"
        self.problem = self.problem + self.item3
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":1}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType8"}

    def ExplainType8(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "eGg9xE3Ld70";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):
        '''e.g.:A fruiterer makes fruit baskets with apples, oranges and mangoes in the ratio 3 : 5 : 2.
                If he packs a total of 90 mangoes with 6 mangoes in each basket,
                how many total fruits does he pack altogether?'''

        self.Dict = {1:["A fruiterer makes fruit baskets with apples, oranges and mangoes in the ratio",
                        ".","If he packs a total of","with","in each basket,","how many total fruits does he pack altogether?",
                        randint(5,8),randint(3,8),randint(3,8),random.choice(["apples","mangoes","oranges"])]
                     }
        
        self.key = randint(1,len(self.Dict))
        self.item1 = self.Dict[self.key][0]
        self.item2 = self.Dict[self.key][1]
        self.item3 = self.Dict[self.key][2]
        self.item4 = self.Dict[self.key][3]
        self.item5 = self.Dict[self.key][4]
        self.item6 = self.Dict[self.key][5]
        self.number1 = self.Dict[self.key][6]
        self.number2 = self.Dict[self.key][7]
        self.number3 = self.Dict[self.key][8]
        self.fruit = self.Dict[self.key][9]
        
        self.ratio1 = self.number1
        self.ratio2 = randint(2,self.ratio1-1)
        self.ratio3 = randint(1,self.ratio2-1)
        
        self.ratios = [self.ratio1,self.ratio2,self.ratio3]
        
        random.shuffle(self.ratios)
        
        self.apples = self.ratios[0]
        self.oranges = self.ratios[1]
        self.mangoes = self.ratios[2]

        if self.fruit=="apples":
            self.fruitQ1 = self.apples * self.number2 * self.number3
        elif self.fruit=="oranges":
            self.fruitQ1 = self.oranges * self.number2 * self.number3
        elif self.fruit=="mangoes":
            self.fruitQ1 = self.mangoes * self.number2 * self.number3
                                
        self.answer = str((self.apples+self.oranges+self.mangoes)*self.number2*self.number3)                                               
        
        self.problem = self.item1+" "+str(self.apples)+" : "+str(self.oranges)+" : "+str(self.mangoes)+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+str(self.fruitQ1)+" "+self.fruit+" "+self.item4+" "+str(self.number3)+" "+self.fruit+" "+self.item5+"<br>"
        self.problem = self.problem + self.item6
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":2}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType9"}

    def ExplainType9(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "aj7axpkUiXU";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
                                        
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
        
        if CheckAnswerType == 1:
            try:
                InputAnswer= string.join(InputAnswer.split(),"")
                return (str(answer)==str(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswerType == 2:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        else:
            return False                             