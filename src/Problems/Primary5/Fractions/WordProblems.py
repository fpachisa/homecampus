'''
Created on Aug 16, 2011

Module: WordProblems
Generates "Word Problems on Fractions" problems for Primary 5

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
from Utils import LcmGcf
from decimal import *

class WordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        ''' first grouping the questions as per problem type in the ppt and then first randomly picking the problem type and then problem from the problem type'''
        ProblemList = [[self.GenerateProblemType1(),self.GenerateProblemType2(),self.GenerateProblemType3(),self.GenerateProblemType4()],
                       [self.GenerateProblemType5(),self.GenerateProblemType6(),self.GenerateProblemType7(),self.GenerateProblemType8()],
                       [self.GenerateProblemType9(),self.GenerateProblemType10()],
                       [self.GenerateProblemType11()],
                       [self.GenerateProblemType12()],
                       [self.GenerateProblemType13(),self.GenerateProblemType14()],
                       [self.GenerateProblemType15()],
                       [self.GenerateProblemType16()],
                       [self.GenerateProblemType17()],
                       [self.GenerateProblemType18()],
                       [self.GenerateProblemType19()],
                       [self.GenerateProblemType20(),self.GenerateProblemType21()],
                       [self.GenerateProblemType22()],
                       ]
        return random.choice(random.choice(ProblemList))
        #return self.GenerateProblemType14()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1","ProblemType2","ProblemType3","ProblemType4"],
                            2:["ProblemType5","ProblemType6","ProblemType7","ProblemType8"],
                            3:["ProblemType9","ProblemType10"],
                            4:["ProblemType11",],
                            5:["ProblemType12",],
                            6:["ProblemType13","ProblemType14"],
                            7:["ProblemType15",],
                            8:["ProblemType16",],
                            9:["ProblemType17",],
                            10:["ProblemType18",],
                            11:["ProblemType19",],
                            12:["ProblemType20","ProblemType21",],
                            13:["ProblemType22",]
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemType2(),self.GenerateProblemType3(),self.GenerateProblemType4()],
                                    2:[self.GenerateProblemType5(),self.GenerateProblemType6(),self.GenerateProblemType7(),self.GenerateProblemType8()],
                                    3:[self.GenerateProblemType9(),self.GenerateProblemType10()],
                                    4:[self.GenerateProblemType11()],
                                    5:[self.GenerateProblemType12()],
                                    6:[self.GenerateProblemType13(),self.GenerateProblemType14()],
                                    7:[self.GenerateProblemType15()],
                                    8:[self.GenerateProblemType16()],
                                    9:[self.GenerateProblemType17()],
                                    10:[self.GenerateProblemType18()],
                                    11:[self.GenerateProblemType19()],
                                    12:[self.GenerateProblemType20(),self.GenerateProblemType21()],
                                    13:[self.GenerateProblemType22()],
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
                            "ProblemType15":self.GenerateProblemType15(),
                            "ProblemType16":self.GenerateProblemType16(),
                            "ProblemType17":self.GenerateProblemType17(),
                            "ProblemType18":self.GenerateProblemType18(),
                            "ProblemType19":self.GenerateProblemType19(),
                            "ProblemType20":self.GenerateProblemType20(),
                            "ProblemType21":self.GenerateProblemType21(),
                            "ProblemType22":self.GenerateProblemType22(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g.:Mala has 1/2 l of water in a bottle. 
        	She drinks 1/3 l of the water.
                How much water is left in the bottle?'''
           
        self.GirlName = random.choice(PersonName.GirlName)
        self.Dict = {1:["litre ",["water ","juice ","milk ","apple cider ","orange juice ",
                                       "apple juice ","lemonade ","milk shake ","yogurt drink ",
                                       "cold coffee ","iced tea ","chocolate milk ","strawberry milk ",
                                       "strawberry shake "],"in a ",["bottle","jar","carton","can",],
                                       "drinks ",[""],"in the ",],
                     2:["litre ",["water ","juice ","milk ","apple cider ","orange juice ",
                                       "apple juice ","lemonade ","milk shake ","yogurt drink ",
                                       "cold coffee ","iced tea ","chocolate milk ","strawberry milk ",
                                       "strawberry shake "],"",["",],
                                       "drinks ",[""],"",],
                     3:["m ",["cloth ","fabric "],"",["",],
                                       "uses ",["to make ribbons","to make handerchiefs"],"",],
                     4:["hr ",["break time ","spare time ","lunch time "],"",["",],
                                       "uses ",["to read a book","to take a rest"],"",],
                     5:["kg ",["sugar ","rice ","flour ","coffee beans ","tea leaves ","cookies ","almonds ","peanuts ","candies ","fertilizer ",
                               "plant food ","fish food ","cocoa powder "],"",["",],
                                       "uses ",[""],"",],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = random.choice(self.Dict[self.key][1])
        self.ina = self.Dict[self.key][2]
        self.item2 = random.choice(self.Dict[self.key][3])
        self.action1 = self.Dict[self.key][4]
        self.action2 = random.choice(self.Dict[self.key][5])
        self.inthe = self.Dict[self.key][6]
        
        ''' Generating 2 proper unlike fractions(numerator<denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)

        '''Making sure that both fractions are not same'''
        while (Decimal(self.numerator1)/Decimal(self.denominator1)-Decimal(self.numerator2)/Decimal(self.denominator2)==0):
            self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
            self.denominator1 = self.denominators[0]
            self.denominator2 = self.denominators[1]
            self.numerator1 = randint(1,self.denominator1-1)
            self.numerator2 = randint(1,self.denominator2-1)
            
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.GirlName + " has &nbsp;</td>"        
        if (Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2)):
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>&nbsp;"+self.unit+"of "+self.item1+self.ina+self.item2+"</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>She "+self.action1+"&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.flag = 1
        else:
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td>&nbsp;"+self.unit+"of "+self.item1+self.ina+self.item2+"</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>She "+self.action1+"&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.flag = 2            
        
        self.problem = self.problem + "<td>&nbsp;"+self.unit+"of the "+self.item1+self.action2+"</td></tr></table>"
        self.problem = self.problem + "How much "+self.item1+"has she left "+self.inthe+self.item2+"? "
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator = abs(self.numerator1*self.AnswerDenominator/self.denominator1 - self.numerator2*self.AnswerDenominator/self.denominator2)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,self.denominator2,
                                              self.AnswerDenominator,self.flag,self.GirlName,self.item1,self.item2,self.action1,self.action2,self.unit,self.ina,self.inthe)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType1"}

    def ExplainType1(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2,AnswerDenominator,flag,girl,item1,item2,action1,action2,unit,ina,inthe):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.answer1), int(self.answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"        
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        if flag == 1:
            self.solution_text = self.solution_text + "<tr><td>At first "+girl+" had </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
            self.solution_text = self.solution_text + "<td> "+unit+"of "+item1 +ina+item2+". "
            self.solution_text = self.solution_text + "After she "+action1+"</td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td><td>"+unit+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>The "+item1+" left is: </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td></tr></table>"
        if flag == 2:
            self.solution_text = self.solution_text + "<tr><td>At first "+girl+" had </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
            self.solution_text = self.solution_text + "<td> "+unit+"of "+item1 +ina+item2+". "
            self.solution_text = self.solution_text + "After she "+action1+"</td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td><td>"+unit+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>The "+item1+" left is: </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td></tr></table>"
                    
        self.solution_text = self.solution_text + "To subtract the fractions follow the below steps:"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td valign='center'> and </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'> do not have same denominator. They are unlike fractions.</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        self.solution_text = self.solution_text + "<br><i>Step1</i>:<br> To subtract unlike fractions, first change them to like fractions.<br><br>"
        self.solution_text = self.solution_text + "<i>Step2</i>:<br> Find the common multiple of denominators. In this case common multiple of "+str(denominator1)+" and "+str(denominator2)+" is "+str(AnswerDenominator)+"<br><br>"
        self.solution_text = self.solution_text + "<i>Step3</i>:<br> Multiply numerator and denominator of both fractions so that denominators become "+str(AnswerDenominator)+"<br><br>"
        multiplier1 = AnswerDenominator/denominator1
        multiplier2 = AnswerDenominator/denominator2
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        if flag == 1:
            self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+" &times; "+str(multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'> = </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1*multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1*multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2*multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2*multiplier2)+"</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator2)+" &times; "+str(multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'> = </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2*multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2*multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1*multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1*multiplier1)+"</td></tr></table>"           
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the "+item1+" left "+inthe+item2+ " is: </td><td align='center'><u>&nbsp;"+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td><td>"+unit+"</td></tr></table>"
        if gcf!=1:
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>It can be further simplified to </td>"
            if self.SimpleAnswer2!=1:
                self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.solution_text = self.solution_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "qsQ-W0xZffs";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g.:: Mala had 4/5 litre of water. 
                How much water had she left after giving 1/3 litre of the water to Alice? (Give your answer in the fraction format.)'''
           
        self.GirlNames = random.sample(PersonName.GirlName,2)
        self.girl1 = self.GirlNames[0]
        self.girl2 = self.GirlNames[1]
        self.Dict = {1:["litre ",["water ","juice ","milk ","apple cider ","orange juice ",
                                       "apple juice ","lemonade ","milk shake ","yogurt drink ",
                                       "cold coffee ","iced tea ",],],
                     2:["m ",["cloth ","fabric ","rope ","string "],],
                     3:["kg ",["sugar ","rice ","flour ","coffee beans ","tea leaves ","cookies ","almonds ","peanuts ","candies ","fertilizer ",
                               "plant food ","fish food ","cocoa powder "],],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = random.choice(self.Dict[self.key][1])
        
        ''' Generating 2 proper unlike fractions(numerator<denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)

        '''Making sure that both fractions are not same'''
        while (Decimal(self.numerator1)/Decimal(self.denominator1)-Decimal(self.numerator2)/Decimal(self.denominator2)==0):
            self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
            self.denominator1 = self.denominators[0]
            self.denominator2 = self.denominators[1]
            self.numerator1 = randint(1,self.denominator1-1)
            self.numerator2 = randint(1,self.denominator2-1)
            
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.girl1 + " has&nbsp;</td>"        
        if (Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2)):
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>&nbsp;"+self.unit+"of "+self.item1+".</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>How much "+self.item1+"had she left after giving&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.flag = 1
        else:
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td>&nbsp;"+self.unit+"of "+self.item1+".</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>How much "+self.item1+"had she left after giving&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.flag = 2            
        
        self.problem = self.problem + "<td>&nbsp;"+self.unit+"of the "+self.item1+"to "+self.girl2+"?</td></tr></table>"
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
                
        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator = abs(self.numerator1*self.AnswerDenominator/self.denominator1 - self.numerator2*self.AnswerDenominator/self.denominator2)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,self.denominator2,
                                              self.AnswerDenominator,self.flag,self.girl1,self.girl2,self.item1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType2"}

    def ExplainType2(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2,AnswerDenominator,flag,girl1,girl2,item1,unit):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.answer1), int(self.answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"        
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        if flag == 1:
            self.solution_text = self.solution_text + "<tr><td>At first "+girl1+" had </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
            self.solution_text = self.solution_text + "<td> "+unit+"of "+item1+". "
            self.solution_text = self.solution_text + "After she gave "+"</td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td><td>"+unit+" to "+girl2+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>The "+item1+" left is: </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td></tr></table>"
        if flag == 2:
            self.solution_text = self.solution_text + "<tr><td>At first "+girl1+" had </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
            self.solution_text = self.solution_text + "<td> "+unit+"of "+item1+". "
            self.solution_text = self.solution_text + "After she gave "+"</td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td><td>"+unit+" to "+girl2+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>The "+item1+" left is: </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td></tr></table>"
                    
        self.solution_text = self.solution_text + "To subtract the fractions follow the below steps:"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td valign='center'> and </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'> do not have same denominator. They are unlike fractions.</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        self.solution_text = self.solution_text + "<br><i>Step1</i>:<br> To subtract unlike fractions, first change them to like fractions.<br><br>"
        self.solution_text = self.solution_text + "<i>Step2</i>:<br> Find the common multiple of denominators. In this case common multiple of "+str(denominator1)+" and "+str(denominator2)+" is "+str(AnswerDenominator)+"<br><br>"
        self.solution_text = self.solution_text + "<i>Step3</i>:<br> Multiply numerator and denominator of both fractions so that denominators become "+str(AnswerDenominator)+"<br><br>"
        multiplier1 = AnswerDenominator/denominator1
        multiplier2 = AnswerDenominator/denominator2
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        if flag == 1:
            self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+" &times; "+str(multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'> = </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1*multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1*multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2*multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2*multiplier2)+"</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator2)+" &times; "+str(multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'> = </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2*multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2*multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1*multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1*multiplier1)+"</td></tr></table>"           
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the "+item1+" left is: </td><td align='center'><u>&nbsp;"+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td><td>"+unit+"</td></tr></table>"
        if gcf!=1:
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>It can be further simplified to </td>"
            if self.SimpleAnswer2!=1:
                self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.solution_text = self.solution_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "qsQ-W0xZffs";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g.:: Mala buys 4/5 kg of apples from the market. She uses 1/3 kg of the apples to make custard. How much apples has she left? '''
           
        self.girl1 = random.choice(PersonName.GirlName)
        self.Dict = {1:["kg ",["apples ","bananas ","strawberries ","blueberries ","berries ","fruit ","pineapple "],
                        ["market ","grocery store ","store "],["eats "],[""]],
                     2:["kg ",["apples ","bananas ","strawberries ","blueberries ","berries ","fruit ","pineapple "],
                        ["market ","grocery store ","store "],["uses "],["to make custard ","to make cake ","to make shake "]],
                     3:["kg ",["vegetables ","onions ","potatoes ","carrots ","meat ","chicken ","tomatoes ","lean meat ","rice "],
                        ["market ","grocery store ","store "],["cooks ","uses "],[""]],
                     4:["m ",["cloth ","fabric "],
                        ["market ","store "],["uses "],["to make ribbons ","to make handkerchiefs "]],
                     5:["m ",["cloth ","fabric ","rope ","string "],
                        ["market ","store "],["uses "],[""]],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = random.choice(self.Dict[self.key][1])
        self.item2 = random.choice(self.Dict[self.key][2])
        self.action1 = random.choice(self.Dict[self.key][3])
        self.action2 = random.choice(self.Dict[self.key][4])
        
        ''' Generating 2 proper unlike fractions(numerator<denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)

        '''Making sure that both fractions are not same'''
        while (Decimal(self.numerator1)/Decimal(self.denominator1)-Decimal(self.numerator2)/Decimal(self.denominator2)==0):
            self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
            self.denominator1 = self.denominators[0]
            self.denominator2 = self.denominators[1]
            self.numerator1 = randint(1,self.denominator1-1)
            self.numerator2 = randint(1,self.denominator2-1)
            
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.girl1 + " buys&nbsp;</td>"        
        if (Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2)):
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td> "+self.unit+"of "+self.item1+"from the "+self.item2+".</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>She "+self.action1+"&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.flag = 1
        else:
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td> "+self.unit+"of "+self.item1+"from the "+self.item2+".</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>She "+self.action1+"&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.flag = 2            
        
        self.problem = self.problem + "<td> "+self.unit+"of the "+self.item1+self.action2+".</td></tr></table>"
        self.problem = self.problem + "How much "+self.item1+" has she left?" 

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
               
        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator = abs(self.numerator1*self.AnswerDenominator/self.denominator1 - self.numerator2*self.AnswerDenominator/self.denominator2)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,self.denominator2,
                                              self.AnswerDenominator,self.flag,self.girl1,self.item1,self.item2,self.unit,self.action1,self.action2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType3"}

    def ExplainType3(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2,AnswerDenominator,flag,girl1,item1,item2,unit,action1,action2):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.answer1), int(self.answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"        
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        if flag == 1:
            self.solution_text = self.solution_text + "<tr><td>At first "+girl1+" had </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
            self.solution_text = self.solution_text + "<td> "+unit+"of "+item1+". "
            self.solution_text = self.solution_text + "After she "+action1+"</td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td><td>"+unit+action2+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>The "+item1+" left is: </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td></tr></table>"
        if flag == 2:
            self.solution_text = self.solution_text + "<tr><td>At first "+girl1+" had </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
            self.solution_text = self.solution_text + "<td> "+unit+"of "+item1+". "
            self.solution_text = self.solution_text + "After she "+action1+"</td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td><td>"+unit+action2+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>The "+item1+" left is: </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td></tr></table>"
                    
        self.solution_text = self.solution_text + "To subtract the fractions follow the below steps:"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td valign='center'> and </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'> do not have same denominator. They are unlike fractions.</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br><i>Step1</i>:<br> To subtract unlike fractions, first change them to like fractions.<br><br>"
        self.solution_text = self.solution_text + "<i>Step2</i>:<br> Find the common multiple of denominators. In this case common multiple of "+str(denominator1)+" and "+str(denominator2)+" is "+str(AnswerDenominator)+"<br><br>"
        self.solution_text = self.solution_text + "<i>Step3</i>:<br> Multiply numerator and denominator of both fractions so that denominators become "+str(AnswerDenominator)+"<br><br>"
        multiplier1 = AnswerDenominator/denominator1
        multiplier2 = AnswerDenominator/denominator2
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        if flag == 1:
            self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+" &times; "+str(multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'> = </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1*multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1*multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2*multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2*multiplier2)+"</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator2)+" &times; "+str(multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'> = </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2*multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2*multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1*multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1*multiplier1)+"</td></tr></table>"           
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the "+item1+" left is: </td><td align='center'><u>&nbsp;"+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td><td>"+unit+"</td></tr></table>"
        if gcf!=1:
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>It can be further simplified to </td>"
            if self.SimpleAnswer2!=1:
                self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.solution_text = self.solution_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "qsQ-W0xZffs";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

        
    def GenerateProblemType4(self):
        '''e.g.:: Mala buys 4/5 kg of apples from the market. She uses 1/3 kg of the apples to make custard. How much apples has she left? '''
           
        self.GirlNames = random.sample(PersonName.GirlName,2)
        self.girl1 = self.GirlNames[0]
        self.girl2 = self.GirlNames[1]
        self.Dict = {1:["kg ",["apples ","bananas ","strawberries ","blueberries ","berries ","fruit ","pineapple "],
                        ["market","grocery store","store"]],
                     2:["kg ",["vegetables ","onions ","potatoes ","carrots ","meat ","chicken ","tomatoes ","lean meat ","rice "],
                        ["market","grocery store","store"]],
                     3:["m ",["cloth ","fabric ","rope ","string "],
                        ["market","store"]],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = random.choice(self.Dict[self.key][1])
        self.place = random.choice(self.Dict[self.key][2])
        
        ''' Generating 2 proper unlike fractions(numerator<denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)

        '''Making sure that both fractions are not same'''
        while (Decimal(self.numerator1)/Decimal(self.denominator1)-Decimal(self.numerator2)/Decimal(self.denominator2)==0):
            self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
            self.denominator1 = self.denominators[0]
            self.denominator2 = self.denominators[1]
            self.numerator1 = randint(1,self.denominator1-1)
            self.numerator2 = randint(1,self.denominator2-1)
            
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.girl1 + " bought&nbsp;</td>"        
        if (Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2)):
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td> "+self.unit+"of "+self.item1+"from the "+self.place+".</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>She gave&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.flag = 1
        else:
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td> "+self.unit+"of "+self.item1+"from the "+self.place+".</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>She gave&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.flag = 2            
        
        self.problem = self.problem + "<td> "+self.unit+"of the "+self.item1+"to "+self.girl2+".</td></tr></table>"
        self.problem = self.problem + "How much "+self.item1+" had she left?" 

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
               
        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator = abs(self.numerator1*self.AnswerDenominator/self.denominator1 - self.numerator2*self.AnswerDenominator/self.denominator2)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,self.denominator2,
                                              self.AnswerDenominator,self.flag,self.girl1,self.girl2,self.item1,self.place,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType4"}

    def ExplainType4(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2,AnswerDenominator,flag,girl1,girl2,item1,place,unit):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.answer1), int(self.answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<i>"+problem + "</i><br><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"        
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        if flag == 1:
            self.solution_text = self.solution_text + "<tr><td>At first "+girl1+" had </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
            self.solution_text = self.solution_text + "<td> "+unit+"of "+item1+". "
            self.solution_text = self.solution_text + "After she gave</td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td><td>"+unit+"to "+girl2+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>The "+item1+" left is: </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td></tr></table>"
        if flag == 2:
            self.solution_text = self.solution_text + "<tr><td>At first "+girl1+" had </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
            self.solution_text = self.solution_text + "<td> "+unit+"of "+item1+". "
            self.solution_text = self.solution_text + "After she gave</td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td><td>"+unit+"to "+girl2+"</td></tr></table>"
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>The "+item1+" left is: </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td></tr></table>"
                    
        self.solution_text = self.solution_text + "To subtract the fractions follow the below steps:"
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+"</td>"
        self.solution_text = self.solution_text + "<td valign='center'> and </td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'> do not have same denominator. They are unlike fractions.</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br><i>Step1</i>:<br> To subtract unlike fractions, first change them to like fractions.<br><br>"
        self.solution_text = self.solution_text + "<i>Step2</i>:<br> Find the common multiple of denominators. In this case common multiple of "+str(denominator1)+" and "+str(denominator2)+" is "+str(AnswerDenominator)+"<br><br>"
        self.solution_text = self.solution_text + "<i>Step3</i>:<br> Multiply numerator and denominator of both fractions so that denominators become "+str(AnswerDenominator)+"<br><br>"
        multiplier1 = AnswerDenominator/denominator1
        multiplier2 = AnswerDenominator/denominator2
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'>"
        if flag == 1:
            self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2)+" &times; "+str(multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'> = </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1*multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1*multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2*multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2*multiplier2)+"</td></tr></table>"
        else:
            self.solution_text = self.solution_text + "<tr><td align='center'><u>&nbsp;"+str(numerator2)+" &times; "+str(multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2)+" &times; "+str(multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1)+" &times; "+str(multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1)+" &times; "+str(multiplier1)+"</td>"
            self.solution_text = self.solution_text + "<td align='center'> = </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator2*multiplier2)+"&nbsp;</u><br>&nbsp;"+str(denominator2*multiplier2)+"</td>"
            self.solution_text = self.solution_text + "<td valign='center'> - </td>"
            self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(numerator1*multiplier1)+"&nbsp;</u><br>&nbsp;"+str(denominator1*multiplier1)+"</td></tr></table>"           
        self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>Hence the "+item1+" left is: </td><td align='center'><u>&nbsp;"+str(answer1)+"&nbsp;</u><br>&nbsp;"+str(answer2)+"</td><td>"+unit+"</td></tr></table>"
        if gcf!=1:
            self.solution_text = self.solution_text + "<table class='FractionsTable' style='color:white'><tr><td>It can be further simplified to </td>"
            if self.SimpleAnswer2!=1:
                self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.solution_text = self.solution_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "qsQ-W0xZffs";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemType5(self):
        '''e.g.: Mala had 4/5 litre of water at first. She gave 1/3 litre of the water to Alice. 
                How much water had Mala after receiving 3/4 litre of water from Betty?'''
           
        self.GirlNames = random.sample(PersonName.GirlName,3)
        self.girl1 = self.GirlNames[0]
        self.girl2 = self.GirlNames[1]
        self.girl3 = self.GirlNames[2]
        self.Dict = {1:["litre ",["water ","juice ","milk ","apple cider ","orange juice ",
                                       "apple juice ","lemonade ","milk shake ","yogurt drink ",
                                       "cold coffee ","iced tea ",]
                                 ],
                     2:["m ",["cloth ","fabric ","rope ","string "]],
                     3:["kg ",["sugar ","rice ","flour ","coffee beans ","tea leaves ","cookies ","almonds ","peanuts ","candies ","fertilizer ",
                               "plant food ","fish food ","cocoa powder "]],
                     4:["kg ",["apples ","bananas ","strawberries ","blueberries ","berries ","fruit ","pineapple "]],
                     5:["kg ",["vegetables ","onions ","potatoes ","carrots ","meat ","chicken ","tomatoes ","lean meat ","rice "]],

                     }
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item = random.choice(self.Dict[self.key][1])
                
        ''' Generating 2 proper unlike fractions(numerator<denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)      

        '''Making sure that both fractions are not same'''
        while (Decimal(self.numerator1)/Decimal(self.denominator1)-Decimal(self.numerator2)/Decimal(self.denominator2)==0):
            self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],3)
            self.denominator1 = self.denominators[0]
            self.denominator2 = self.denominators[1]
            self.numerator1 = randint(1,self.denominator1-1)
            self.numerator2 = randint(1,self.denominator2-1)
        
        self.denominator3 = self.denominator2
        self.numerator3 = randint(1,self.denominator3-1)
                        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.girl1+" had&nbsp;</td>"        
        if (Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2)):
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item+"at first.</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>She gave&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item+"to "+self.girl2+".</td></tr></table>"         
            self.flag = 1
        else:
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item+"at first.</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<td>She gave&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item+"to "+self.girl2+".</td></tr></table>"          
            self.flag = 2            
        
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>How much "+self.item+"had "+self.girl1+" after receiving</td></tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'>"          
        self.problem = self.problem + "<tr><td align='center'><u>&nbsp;"+str(self.numerator3)+"&nbsp;</u><br>&nbsp;"+str(self.denominator3)+"</td>"
        self.problem = self.problem + "<td>"+self.unit+"of "+self.item+"from "+self.girl3+"?</td></tr></table>"

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator1 = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator1 = abs(self.numerator1*self.AnswerDenominator1/self.denominator1 - self.numerator2*self.AnswerDenominator1/self.denominator2)
        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.AnswerDenominator1, self.denominator3)
        self.AnswerNumerator = (self.AnswerNumerator1*self.AnswerDenominator/self.AnswerDenominator1 + self.numerator3*self.AnswerDenominator/self.denominator3)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,
                                              self.denominator2,self.AnswerDenominator,self.flag,self.girl1,self.girl2,self.girl3,
                                              self.item,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType5"}

    def ExplainType5(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2,AnswerDenominator,flag,girl1,
                     girl2,girl3,item,unit):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.answer1), int(self.answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer1)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "qsQ-W0xZffs";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemType6(self):
        '''e.g.:After pouring 1/3 litre of water from a bottle into a cup, 
                Mala fills another 3/4 litre of water in the bottle.
                If she had 4/5 litre of water in the bottle at first, 
                how much water has she got in the bottle now?'''
           
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["litre ",["drinking"],["water ","juice ","milk ","apple cider ","orange juice ",
                                       "apple juice ","lemonade ","milk shake ","yogurt drink ",
                                       "cold coffee ","iced tea ","chocolate milk ","strawberry milk ",
                                       "strawberry shake "],"from a ",["bottle","jar","carton","can",],
                                       [""],"fills ","in the ",""],
                     2:["litre ",["pouring"],["water ","juice ","milk ","apple cider ","orange juice ",
                                       "apple juice ","lemonade ","milk shake ","yogurt drink ",
                                       "cold coffee ","iced tea ","chocolate milk ","strawberry milk ",
                                       "strawberry shake "],"from a ",["bottle","jar","carton","can",],
                                       [" into a cup "," into a glass "],"fills ","in the ",""],
                     3:["litre ",["spilling"],["water ","juice ","milk ","apple cider ","orange juice ",
                                       "apple juice ","lemonade ","milk shake ","yogurt drink ",
                                       "cold coffee ","iced tea ","chocolate milk ","strawberry milk ",
                                       "strawberry shake "],"from a ",["bottle","jar","carton","can",],
                                       [" onto the floor "],"fills ","in the ",""],
                     4:["m ",["using"],["cloth ","fabric "],"",[""],["to make ribbons ","to make handkerchiefs "],"buys ","","unused "],
                     5:["hour ",["using","spending"],["break time "],"",[""],["to read a story ","to take a rest "],"gets ","","unused "],
                     6:["hour ",["using","spending"],["study time "],"",[""],["to do homework ","to solve maths problems "],"gets ","","unused "],
                     7:["hour ",["using","spending"],["lunch time "],"",[""],["to eat lunch ","to make a phone call "],"gets ","","unused "],
                     8:["hour ",["using","spending"],["play time "],"",[""],["to solve a puzzle ","to play in the playground "],"gets ","","unused "],
                     9:["kg ",["using"],["sugar ","rice ","flour ","coffee beans ","tea leaves ","cookies ","almonds ","peanuts ","candies ","fertilizer ",
                               "plant food ","fish food ","cocoa powder "],
                        "",[""],[""],"buys ","","unused "],
                     }
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.action1 = random.choice(self.Dict[self.key][1])
        self.item1 = random.choice(self.Dict[self.key][2])
        self.froma = self.Dict[self.key][3]
        self.item2 = random.choice(self.Dict[self.key][4])
        self.item3 = random.choice(self.Dict[self.key][5])
        self.action2 = self.Dict[self.key][6]
        self.inthe = self.Dict[self.key][7]
        self.item4 = self.Dict[self.key][8]
                
        ''' Generating 2 proper unlike fractions(numerator<denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],3)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)

        '''Making sure that both fractions are not same'''
        while (Decimal(self.numerator1)/Decimal(self.denominator1)-Decimal(self.numerator2)/Decimal(self.denominator2)==0):
            self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],3)
            self.denominator1 = self.denominators[0]
            self.denominator2 = self.denominators[1]
            self.numerator1 = randint(1,self.denominator1-1)
            self.numerator2 = randint(1,self.denominator2-1)
        
        self.denominator3 = self.denominator2
        self.numerator3 = randint(1,self.denominator3-1)
                        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>After "+self.action1+"&nbsp;</td>"        
        if (Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2)):
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item1+self.froma+self.item2+self.item3+ ",</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>"+self.boy1+" "+self.action2+"another&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator3)+"&nbsp;</u><br>&nbsp;"+str(self.denominator3)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item1+self.inthe+self.item2+".</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>If he had&nbsp;</td>"        
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item1+self.inthe+self.item2+" at first,</td></tr></table>"            
            self.flag = 1
        else:
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item1+self.froma+self.item2+self.item3+ ",</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>"+self.boy1+" "+self.action2+"another&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator3)+"&nbsp;</u><br>&nbsp;"+str(self.denominator3)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item1+self.inthe+self.item2+".</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>If he had&nbsp;</td>"        
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item1+self.inthe+self.item2+" at first,</td></tr></table>"
            self.flag = 2            
        
        self.problem = self.problem + "How much "+self.item4+self.item1+" has he got "+self.inthe+self.item2+" now?"

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator1 = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator1 = abs(self.numerator1*self.AnswerDenominator1/self.denominator1 - self.numerator2*self.AnswerDenominator1/self.denominator2)
        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.AnswerDenominator1, self.denominator3)
        self.AnswerNumerator = (self.AnswerNumerator1*self.AnswerDenominator/self.AnswerDenominator1 + self.numerator3*self.AnswerDenominator/self.denominator3)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,
                                              self.denominator2,self.AnswerDenominator,self.flag,self.boy1,self.item1,self.item2,
                                              self.item3,self.item4,self.action1,self.action2,self.froma,self.inthe,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType6"}

    def ExplainType6(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2,AnswerDenominator,flag,boy1,item1,
                     item2,item3,item4,action1,action2,froma,inthe,unit):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.answer1), int(self.answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer1)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "qsQ-W0xZffs";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemType7(self):
        '''e.g.: Mala buys 4/5 kg of apples from the market. 
        	She uses 1/3 kg of the apples to make custard. 
        	If she buys another 3/4 kg of apples, 
        	find the quantity of apples she has now? '''
           
        self.girl1 = random.choice(PersonName.GirlName)
        self.Dict = {1:["kg ",["apples ","bananas ","strawberries ","blueberries ","berries ","fruit ","pineapple "],
                        ["market","grocery store","store"],["eats "],[""]],
                     2:["kg ",["apples ","bananas ","strawberries ","blueberries ","berries ","fruit ","pineapple "],
                        ["market","grocery store","store"],["uses "],["to make custard","to make a cake","to make shake"]],
                     3:["kg ",["vegetables ","onions ","potatoes ","carrots ","meat ","chicken ","tomatoes ","lean meat ","rice "],
                        ["market","grocery store","store"],["uses ","cooks "],[""]],
                     4:["m ",["cloth ","fabric "],["market","store"],["uses "],["to make ribbons ","to make handkerchiefs"]],
                     5:["m ",["cloth ","fabric ","rope ","string "],["market","store"],["uses "],[""]],
                     }
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = random.choice(self.Dict[self.key][1])
        self.item2 = random.choice(self.Dict[self.key][2])
        self.action1 = random.choice(self.Dict[self.key][3])
        self.action2 = random.choice(self.Dict[self.key][4])
                
        ''' Generating 2 proper unlike fractions(numerator<denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)      

        '''Making sure that both fractions are not same'''
        while (Decimal(self.numerator1)/Decimal(self.denominator1)-Decimal(self.numerator2)/Decimal(self.denominator2)==0):
            self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],3)
            self.denominator1 = self.denominators[0]
            self.denominator2 = self.denominators[1]
            self.numerator1 = randint(1,self.denominator1-1)
            self.numerator2 = randint(1,self.denominator2-1)
        
        self.denominator3 = self.denominator2
        self.numerator3 = randint(1,self.denominator3-1)
                        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.girl1+" buys&nbsp;</td>"        
        if (Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2)):
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item1+"from the "+self.item2+".</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>She "+self.action1+"&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of the "+self.item1+self.action2+".</td></tr></table>"         
            self.flag = 1
        else:
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item1+"from the "+self.item2+".</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'>"
            self.problem = self.problem + "<tr><td>She "+self.action1+"&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of the "+self.item1+self.action2+".</td></tr></table>"
            self.flag = 2            
        
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>If she buys another&nbsp;</td>"          
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator3)+"&nbsp;</u><br>&nbsp;"+str(self.denominator3)+"</td>"
        self.problem = self.problem + "<td>"+self.unit+"of "+self.item1+",</td></tr></table>"
        self.problem = self.problem + "Find the amount of "+self.item1+"she has now?"

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator1 = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator1 = abs(self.numerator1*self.AnswerDenominator1/self.denominator1 - self.numerator2*self.AnswerDenominator1/self.denominator2)
        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.AnswerDenominator1, self.denominator3)
        self.AnswerNumerator = (self.AnswerNumerator1*self.AnswerDenominator/self.AnswerDenominator1 + self.numerator3*self.AnswerDenominator/self.denominator3)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,
                                              self.denominator2,self.AnswerDenominator,self.flag,self.girl1,self.item1,self.item2,
                                              self.action1,self.action2,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType7"}

    def ExplainType7(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2,AnswerDenominator,flag,girl1,
                     item1,item2,action1,action2,unit):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.answer1), int(self.answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer1)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "qsQ-W0xZffs";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
    
    def GenerateProblemType8(self):
        '''e.g.: Mala bought 4/5 kg of apples from the market. 
                She gave 1/3 kg of the apples to Alice. 
                Find the amount of apples that Mala had 
                if she bought another 3/4 kg of apples.  '''
           
        self.BoyNames = random.sample(PersonName.BoyName,2)
        self.boy1 = self.BoyNames[0]
        self.boy2 = self.BoyNames[1]
        
        self.Dict = {1:["kg ",["apples ","bananas ","strawberries ","blueberries ","berries ","fruit ","pineapple "],
                        ["market","grocery store","store"]],
                     2:["kg ",["vegetables ","onions ","potatoes ","carrots ","meat ","chicken ","tomatoes ","lean meat ","rice "],
                        ["market","grocery store","store"]],
                     3:["m ",["cloth ","fabric ","rope ","string "],["market","store"]],
                     }
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = random.choice(self.Dict[self.key][1])
        self.item2 = random.choice(self.Dict[self.key][2])
                
        ''' Generating 2 proper unlike fractions(numerator<denominator) and denominator<= 12'''
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)      

        '''Making sure that both fractions are not same'''
        while (Decimal(self.numerator1)/Decimal(self.denominator1)-Decimal(self.numerator2)/Decimal(self.denominator2)==0):
            self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],3)
            self.denominator1 = self.denominators[0]
            self.denominator2 = self.denominators[1]
            self.numerator1 = randint(1,self.denominator1-1)
            self.numerator2 = randint(1,self.denominator2-1)
        
        self.denominator3 = self.denominator2
        self.numerator3 = randint(1,self.denominator3-1)
                        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.boy1+" bought&nbsp;</td>"        
        if (Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2)):
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item1+"from the "+self.item2+".</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'><tr><td>He gave&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of the "+self.item1+"to "+self.boy2+".</td></tr></table>"         
            self.flag = 1
        else:
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of "+self.item1+"from the "+self.item2+".</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'><tr><td>He gave&nbsp;</td>"
            self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+"of the "+self.item1+"to "+self.boy2+".</td></tr></table>"            
            self.flag = 2            
        self.problem = self.problem + "Find the amount of "+self.item1+"that "+self.boy1+" had"
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>if he bought another&nbsp;</td>"          
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.numerator3)+"&nbsp;</u><br>&nbsp;"+str(self.denominator3)+"</td>"
        self.problem = self.problem + "<td>"+self.unit+"of "+self.item1+".</td></tr></table>"

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator1 = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator1 = abs(self.numerator1*self.AnswerDenominator1/self.denominator1 - self.numerator2*self.AnswerDenominator1/self.denominator2)
        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.AnswerDenominator1, self.denominator3)
        self.AnswerNumerator = (self.AnswerNumerator1*self.AnswerDenominator/self.AnswerDenominator1 + self.numerator3*self.AnswerDenominator/self.denominator3)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,
                                              self.denominator2,self.AnswerDenominator,self.flag,self.boy1,self.boy2,self.item1,self.item2,
                                              self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType8"}

    def ExplainType8(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2,AnswerDenominator,flag,boy1,
                     boy2,item1,item2,unit):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.answer1), int(self.answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer1)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "qsQ-W0xZffs";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):
        '''e.g.:1/4 of the girls in a class have short hair, 
                2/3 of the girls in the class have medium-length hair while 
                the rest of the girls in the class have long hair. 
                What fraction of the girls in the class have long hair?'''
           
        self.Dict = {1:["girls","in a class","in the class","have short hair","have medium-length hair","have long hair"],
                     2:["boys","in a sports school","in the sports school","play soccer","play hockey","play cricket"],
                     3:["children","in a playground","in the playground","are playing hopscotch","are playing on the swing","are playing on the slides"],
                     4:["employess","at a company","at the company","work full-time","work part-time","work on weekends"],
                     5:["pupils","in a music school","in the music school","are learning the piano","are learning the ukelele","are learning the guitar"],
                     6:["plant","at a nursery","at the nursery","are flowering plants","are non-flowering plants","are fruit-bearing plants"],
                     7:["T-shirts","at a clearance sale","at the clearance sale","are blue","are white","are purple"],
                     8:["tickets","at a concert","at the concert","are Class A tickets","are Class B tickets","are Class C Tickets"],
                     9:["fruits","in a fruit basket","in the fruit basket","are apples","are oranges","are pears"],
                     10:["shops","at a mall","at the mall","sell food","sell clothes","sell toys"],
                     11:["pupils","in a school","in the school","go to school by bus","go to school on foot","go to schools with their parents"],
                     }
        self.key = randint(1,len(self.Dict))
        self.item1 = self.Dict[self.key][0]
        self.item2 = self.Dict[self.key][1]
        self.item3 = self.Dict[self.key][2]
        self.item4 = self.Dict[self.key][3]
        self.item5 = self.Dict[self.key][4]
        self.item6 = self.Dict[self.key][5]

        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        
        '''Making sure that sum of above two fractions is less than 0.9 (1/12) as we need to accomodate one more fraction and sum all of these to 1'''
        while float(Decimal(self.numerator1)/Decimal(self.denominator1)+Decimal(self.numerator2)/Decimal(self.denominator2))>0.9:
            self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
            self.denominator1 = self.denominators[0]
            self.denominator2 = self.denominators[1]
            self.numerator1 = randint(1,self.denominator1-1)
            self.numerator2 = randint(1,self.denominator2-1)
                                       
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of the "+self.item1+" "+self.item2+" "+self.item4+",</td></tr></table>"        
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of the "+self.item1+" "+self.item3+" "+self.item5+",</td></tr></table>"
        self.problem = self.problem + "while the rest of the "+self.item1+" "+self.item3+" "+self.item6+".<br><br>"
        self.problem = self.problem + "What fraction of the "+self.item1+" "+self.item3+" "+self.item6+"?"      

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.AnswerNumerator = self.AnswerDenominator - self.numerator1*self.AnswerDenominator/self.denominator1 - self.numerator2*self.AnswerDenominator/self.denominator2
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.denominator1,self.denominator2,
                                              self.AnswerDenominator,self.item1,self.item2,self.item3,self.item4,self.item5,self.item6)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':'',
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType9"}

    def ExplainType9(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2,AnswerDenominator,
                     item1,item2,item3,item4,item5,item6):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.answer1), int(self.answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer1)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "voizy2UnqOc";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain           

    def GenerateProblemType10(self):
        '''e.g.:1/4 of the girls in a class have short hair, 
                2/3 of the girls in the class have medium-length hair 
                while the rest of the girls in the class have long hair. 
                If there are 36 girls in the class, how many of them have long hair?'''
           
        self.Dict = {1:["girls","in a class","in the class","have short hair","have medium-length hair","have long hair",randint(6,10)],
                     2:["boys","in a sports school","in the sports school","play soccer","play hockey","play cricket",randint(6,10)],
                     3:["children","in a playground","in the playground","are playing hopscotch","are playing on the swing","are playing on the slides",randint(2,4)],
                     4:["employess","at a company","at the company","work full-time","work part-time","work on weekends",randint(6,10)],
                     5:["pupils","in a music school","in the music school","are learning the piano","are learning the ukelele","are learning the guitar",randint(4,6)],
                     6:["plant","at a nursery","at the nursery","are flowering plants","are non-flowering plants","are fruit-bearing plants",randint(6,10)],
                     7:["T-shirts","at a clearance sale","at the clearance sale","are blue","are white","are purple",randint(6,10)],
                     8:["tickets","at a concert","at the concert","are Class A tickets","are Class B tickets","are Class C Tickets",randint(6,10)],
                     9:["fruits","in a fruit basket","in the fruit basket","are apples","are oranges","are pears",randint(2,4)],
                     10:["shops","at a mall","at the mall","sell food","sell clothes","sell toys",randint(4,6)],
                     11:["pupils","in a school","in the school","go to school by bus","go to school on foot","go to school with their parents",randint(6,10)],
                     }
        self.key = randint(1,len(self.Dict))
        self.item1 = self.Dict[self.key][0]
        self.item2 = self.Dict[self.key][1]
        self.item3 = self.Dict[self.key][2]
        self.item4 = self.Dict[self.key][3]
        self.item5 = self.Dict[self.key][4]
        self.item6 = self.Dict[self.key][5]
        self.multiplier = self.Dict[self.key][6]

        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        
        '''Making sure that sum of above two fractions is less than 0.9 (1/12) as we need to accomodate one more fraction and sum all of these to 1'''
        while float(Decimal(self.numerator1)/Decimal(self.denominator1)+Decimal(self.numerator2)/Decimal(self.denominator2))>0.9:
            self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
            self.denominator1 = self.denominators[0]
            self.denominator2 = self.denominators[1]
            self.numerator1 = randint(1,self.denominator1-1)
            self.numerator2 = randint(1,self.denominator2-1)
            
        self.total = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)*self.multiplier
                                       
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td align='center'><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of the "+self.item1+" "+self.item2+" "+self.item4+",</td></tr></table>"        
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td align='center'><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of the "+self.item1+" "+self.item3+" "+self.item5+",</td></tr></table>"
        self.problem = self.problem + "while the rest of the "+self.item1+" "+self.item3+" "+self.item6+".<br><br>"
        self.problem = self.problem + "If there are "+str(self.total)+" "+self.item1+" "+self.item3+", how many of them "+self.item6+"?"      
        
        self.ThirdDenominator = LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2)
        self.ThirdNumerator = self.ThirdDenominator - self.numerator1*self.ThirdDenominator/self.denominator1 - self.numerator2*self.ThirdDenominator/self.denominator2
        self.answer = str(self.ThirdNumerator*self.total/self.ThirdDenominator)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.numerator1,self.numerator2,self.denominator1,self.denominator2,
                                              self.item1,self.item2,self.item3,self.item4,self.item5,self.item6,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':'',
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType10"}

    def ExplainType10(self,problem,answer,numerator1,numerator2,denominator1,denominator2,
                     item1,item2,item3,item4,item5,item6,total):
        self.answer_text = "The correct answer is: "+answer

        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "voizy2UnqOc";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain           

    def GenerateProblemType11(self):
        '''e.g.:After school, Tim spends 1/2 hour resting, 
                2-1/2 hours studying, 1-1/2 hours playing 
                and 3/4 hour watching TV. 
                Altogether, how much time does he spend in the above activities after school?'''
           
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["hour","hours",["After school"],["spends"],["resting"],["studying"],["playing"],["watching TV"],
                        "Altogether, how much time does he spend in the above activites after school?"],
                     2:["hour","hours",["Each day"],["spends"],["in the Music class"],["in the English class"],["in the Maths class"],["in the Phyical Education class"],
                        "Altogether, how much time does he spend in the above classes each day?"],
                     3:["hour","hours",["Each week"],["does"],["of swimming"],["of running"],["of cycling"],["of weight training"],
                        "Altogether, how many hours of exercise does he do each week?"],
                     4:["m","m",["For a school project"],["needs"],["of yellow string"],["of blue string"],["of white string"],["of red string"],
                        "Altogether, how much string does he need for the project?"],
                     5:["m","m",["To make an artistic quilt"],["uses"],["of silk fabric"],["of cotton fabric"],["of linen fabric"],["of satin fabric"],
                        "Altogether, how much fabric does he use to make the quilt?"],
                     6:["cup","cups",["To make strawberry shake"],["uses"],["of strawberries"],["of milk"],["of ice"],["of sugar"],
                        "Altogether, how many cups of ingredients does he need to make the shake?"],
                     7:["cup","cups",["To make a soup"],["needs"],["of beans"],["of water"],["of canned tomatoes"],["of potatoes"],
                        "Altogether, how many cups of ingredients does he need to make the soup?"],
                     8:["km","km",["At a hiking trip"],["did"],["of jogging in the forest"],["of trekking in the mountains"],["of cycling"],["of swimming in the river"],
                        "Altogether, how much distance did he cover on the hiking trip?"],
                     9:["kg","kg",["At the supermarket"],["bought"],["of lamb","of lean beef","of low fat beef","of beef","of red meat","of steak"],
                        ["of chicken","of lamb","of duck","of poultry","of chicken fillet","of fish"],["of vegetables","of tomatoes","of potatoes","of onions"],
                        ["of fruit","of apples","of bananas","of strawberries","of cherries","of chickoos","of pears","of oranges"],
                        "Altogether, how much grocery did he buy?"],
                     10:["kg","kg",["At a speciality tea shop"],["purchased"],["of orange flavoured tea"],["of Indian masala tea"],
                         ["of Chinese herbal tea"],["of Japanese green tea"],"Altogether, how much tea did he purchase?"],
                     }
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.units = self.Dict[self.key][1]
        self.item1 = random.choice(self.Dict[self.key][2])
        self.item2 = random.choice(self.Dict[self.key][3])
        self.item3 = random.choice(self.Dict[self.key][4])
        self.item4 = random.choice(self.Dict[self.key][5])
        self.item5 = random.choice(self.Dict[self.key][6])
        self.item6 = random.choice(self.Dict[self.key][7])
        self.item7 = self.Dict[self.key][8]

        # Generating 2 mixed fractions
        self.denominators = random.sample([2,3,4,5,6],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        self.mixed1 = randint(1,2)
        self.mixed2 = randint(1,2)
        self.numerator11 = self.mixed1*self.denominator1 + self.numerator1
        self.numerator22 = self.mixed2*self.denominator2 + self.numerator2
        
        # Generating 2 proper fractions
        self.denominators = random.sample([2,3,4,5,6],2)
        self.denominator3 = self.denominators[0]
        self.denominator4 = self.denominators[1]
        self.numerator3 = randint(1,self.denominator3-1)
        self.numerator4 = randint(1,self.denominator4-1)
        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.item1+", "+self.boy1+" "+self.item2+"&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator3)+"&nbsp;</u><br>&nbsp;"+str(self.denominator3)+"</td><td>"+self.unit+" "+self.item3+",</td></tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'><tr>"
        self.problem = self.problem + "<tr><td >"+str(self.mixed1)+"</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td><td>"+self.units+" "+self.item4+",&nbsp;</td>"
        self.problem = self.problem + "<td >"+str(self.mixed2)+"</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td><td>"+self.units+" "+self.item5+"</td></tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'><tr>"      
        self.problem = self.problem + "<td>and&nbsp;</td><td><u>&nbsp;"+str(self.numerator4)+"&nbsp;</u><br>&nbsp;"+str(self.denominator4)+"</td><td>"+self.unit+" "+self.item6+".</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + self.item7

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        #finding lcm of 4 different denominators
        self.AnswerDenominator = LcmGcf.LcmGcf().find_lcm(LcmGcf.LcmGcf().find_lcm(LcmGcf.LcmGcf().find_lcm(self.denominator1, self.denominator2),self.denominator3),self.denominator4)
        self.AnswerNumerator = (self.numerator11*self.AnswerDenominator/self.denominator1 + self.numerator22*self.AnswerDenominator/self.denominator2 + self.numerator3*self.AnswerDenominator/self.denominator3 + self.numerator4*self.AnswerDenominator/self.denominator4)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer1,self.answer2,self.mixed1,self.mixed2,self.numerator1,self.numerator2,self.denominator1,self.denominator2,self.AnswerDenominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.units,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType11"}

    def ExplainType11(self,problem,answer1,answer2,mixed1,mixed2,numerator1,numerator2,denominator1,denominator2,AnswerDenominator):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))
        #Adding the simplified fraction if possible
        if(answer1%answer2!=0):
            if gcf!=1:
                self.SimpleAnswer1 = int(answer1)/gcf
                self.SimpleAnswer2 = int(answer2)/gcf
                if self.SimpleAnswer2!=1:
                    self.SimpleMixed1,self.SimpleAnswer11 = divmod(self.SimpleAnswer1,self.SimpleAnswer2)
                    self.answer_text = self.answer_text + "<td valign='center'>"+str(self.SimpleMixed1)+"</td>"
                    self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer11)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"              
                else:
                    self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.mixed1,self.answer11 = divmod(answer1,answer2)
        self.answer_text = self.answer_text + "<td valign='center'>"+str(self.mixed1)+"</td>"
        if self.answer11!=0:
            self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer11)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
        
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "X7GNZ9TtL0o";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
             
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType12(self):
        '''e.g.:Lily had 4/5 m of cloth. 
                She used 3/4 of it to make handkerchiefs. 
                How much cloth had she left? '''
           
        self.girl1 = random.choice(PersonName.GirlName)
        self.Dict = {1:["m",["cloth"],["make handkerchiefs"]],
                     2:["m",["stick"],["make a stick robot"]],
                     3:["hour",["lunch break"],["eat lunch","read a book","take a rest","make a phone call"]],
                     4:["hour",["study time"],["solve math problems","do homework","read a science book","work on a school project"]],
                     5:["hour",["play time"],["solve a puzzle","play in the playground"]],
                     6:["cup",["milk"],["make a strawberry shake","make an apple shake","make a banana shake","make a choco shake","make a custard","make a pudding"]],
                     7:["cup",["onions","tomatoes","potatoes","vegetables","beans"],["make a soup"]],
                     8:["litre",["milk"],["make a strawberry shake","make an apple shake","make a banana shake","make a choco shake","make a custard","make a pudding"]],
                     9:["litre",["oil"],["fry nuggets","fry fries","fry chicken","fry onion rings"]],
                     10:["kg",["apples","bananas","peaches","strawberries"],["make a shake","make a cake","make a pudding"]],
                     11:["kg",["chicken","lean meat","red meat","low fat meat","fish fillet"],["make a pie","make a sandwich","make a burger"]],
                     12:["kg",["flour","wheat flour","plain flour","bread flour"],["make a bread","make biscuits","make cookies","make pastries","make muffins"]],
                     }
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = random.choice(self.Dict[self.key][1])
        self.item2 = random.choice(self.Dict[self.key][2])

        # Generating 2 mixed fractions
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        
        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.girl1+" had&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>"+self.unit+" of "+self.item1+".</td></tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'><tr>"
        self.problem = self.problem + "<tr><td >She used&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of it to "+self.item2+".</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "How much "+self.item1+" had she left?"

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator1 * self.denominator2
        self.AnswerNumerator = (self.denominator2 - self.numerator2)*self.numerator1
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)  
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,
                                               self.denominator1,self.denominator2,self.AnswerDenominator,self.unit,self.item1,self.item2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType12"}

    def ExplainType12(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2,AnswerDenominator,unit,item1,item2):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer1)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
                
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "TDpuiHuTEl4";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
             
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain            

    def GenerateProblemType13(self):
        '''e.g.:Rose had some rice. 
            She gave 1/4 of it to her sister and cooked 1/6 of the remaining. 
            What fraction of the rice did she cook? '''
           
        self.girl1 = random.choice(PersonName.GirlName)
        self.Dict = {1:[["rice"],"gave",["it to her sister",],"cooked","cook"],
                     2:[["ribbon"],"shared",["it with a friend","it with her sister","it with her brother","it with a cousin"],"made decorative flowers with",
                        "make decorative flowers with"],
                     3:[["ribbon"],"used",["it to decorate her dress","it to decorate her blouse"],"made bows with","make bows with"],
                     4:[["ribbon"],"used",["it for making bows","it for making decorative flowers"],"gave away","give away"],
                     5:[["wooden stick"],"used",["it to make a toy boat"],"made a stick robot with","make the stick robot with"],
                     6:[["milk"],"used",["it to make a strawberry shake","it to make an apple shake","it to make a banana shake",
                                         "it to make a chikoo shake","it to make a custard","it to make a pudding"],"drank","drink"],
                     7:[["milk"],"gave",["it to a friend","it to her sister","it to her brother"],"spilled","spill"],
                     8:[["onions","tomatoes","potatoes","vegetables","beans"],"used",["them for a salad","them for a side dish","them for a roasted vegetable dish"],
                        "made a soup with","make the soup with"],
                     9:[["pasta"],"used",["it to make a cheesy pasta","it to make pasta bolognese"],"made a salad with","make the salad with"],
                     10:[["cheese"],"used",["it to make a cheese sandwich","it for a side dish","it for a cheese polenta","it for a cheese cake",
                                            "it for a pizza topping"],"grated","grate"],
                     11:[["oil"],"used",["it for frying nuggets","it for frying chicken"],"spilled","spill"],
                     12:[["apples","bananas","peaches","strawberries"],"used",["it to make a shake","it for making a custard"],"ate","eat"],
                     13:[["chiken","meat","fish"],"used",["it to make a pie","it to make a sandwich","it to make a burger"],"froze","freeze"],
                     14:[["flour","wheat flour","bread flour"],"used",["it to make a bread","it to make biscuits","it to make muffins"],"packed","pack"]
                     }
        self.key = randint(1,len(self.Dict))
        self.item1 = random.choice(self.Dict[self.key][0])
        self.item2 = self.Dict[self.key][1]
        self.item3 = random.choice(self.Dict[self.key][2])
        self.item4 = self.Dict[self.key][3]
        self.item5 = self.Dict[self.key][4]

        # Generating 2 mixed fractions
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        
        self.problem = self.girl1+" had some "+self.item1+"."
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td> She "+self.item2+"&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of "+self.item3+"</td></tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'><tr><td>"+" and "+self.item4+"&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of the remaining.</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "What fraction of the "+self.item1+" did she "+self.item5+"?"

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.denominator1 * self.denominator2
        self.AnswerNumerator = (self.denominator1 - self.numerator1)*self.numerator2
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)  
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,
                                               self.denominator1,self.denominator2,self.AnswerDenominator,self.item1,self.item2,self.item3,self.item4,self.item5)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':'',
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType13"}

    def ExplainType13(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2,AnswerDenominator,item1,item2,item3,item4,item5):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer1)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
                
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "igISgktSd0M";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
             
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain            

    def GenerateProblemType14(self):
        '''e.g.:Rose had some rice. 
            She gave 1/4 of it to her sister and cooked 1/6 of the remaining. 
            If she cooked 1/2 kg of rice, 
            how much rice had she at first? '''
           
        self.girl1 = random.choice(PersonName.GirlName)
        self.Dict = {1:["kg",["rice"],"gave",["it to her sister",],"cooked","cook"],
                     2:["m",["ribbon"],"shared",["it with a friend","it with her sister","it with her brother","it with a cousin"],"made decorative flowers with",
                        "make decorative flowers with"],
                     3:["m",["ribbon"],"used",["it to decorate her dress","it to decorate her blouse"],"made bows with","make bows with"],
                     4:["m",["ribbon"],"used",["it for making bows","it for making decorative flowers"],"gave away","give away"],
                     5:["m",["wooden stick"],"used",["it to make a toy boat"],"made a stick robot with","make the stick robot with"],
                     6:["litre",["milk"],"used",["it to make a strawberry shake","it to make an apple shake","it to make a banana shake",
                                         "it to make a chikoo shake","it to make a custard","it to make a pudding"],"drank","drink"],
                     7:["litre",["milk"],"gave",["it to a friend","it to her sister","it to her brother"],"spilled","spill"],
                     8:["kg",["onions","tomatoes","potatoes","vegetables","beans"],"used",["them for a salad","them for a side dish","them for a roasted vegetable dish"],
                        "made a soup with","make the soup with"],
                     9:["kg",["pasta"],"used",["it to make a cheesy pasta","it to make pasta bolognese"],"made a salad with","make the salad with"],
                     10:["kg",["cheese"],"used",["it to make a cheese sandwich","it for a side dish","it for a cheese polenta","it for a cheese cake",
                                            "it for a pizza topping"],"grated","grate"],
                     11:["litre",["oil"],"used",["it for frying nuggets","it for frying chicken"],"spilled","spill"],
                     12:["kg",["apples","bananas","peaches","strawberries"],"used",["it to make a shake","it for making a custard"],"ate","eat"],
                     13:["kg",["chiken","meat","fish"],"used",["it to make a pie","it to make a sandwich","it to make a burger"],"froze","freeze"],
                     14:["kg",["flour","wheat flour","bread flour"],"used",["it to make a bread","it to make biscuits","it to make muffins"],"packed","pack"]
                     }
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = random.choice(self.Dict[self.key][1])
        self.item2 = self.Dict[self.key][2]
        self.item3 = random.choice(self.Dict[self.key][3])
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]

        # Generating 2 mixed fractions
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        self.denominator3 = random.choice([2,3,4,5,6])
        self.numerator3 = randint(1,self.denominator3-1)
        
        self.problem = self.girl1+" had some "+self.item1+"."
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td> She "+self.item2+"&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of "+self.item3+"</td></tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'><tr><td>"+" and "+self.item4+"&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td>&nbsp;of the remaining.</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>If she "+self.item4+"&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator3)+"&nbsp;</u><br>&nbsp;"+str(self.denominator3)+"</td>"        
        self.problem = self.problem + "<td>"+self.unit + " of "+self.item1+",</td>"        
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "how much "+self.item1+" had she at first?"
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
                
        self.AnswerDenominator = self.denominator3 * (self.denominator1-self.numerator1) * self.numerator2
        self.AnswerNumerator = self.numerator3 * self.denominator1 * self.denominator2
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.numerator3,
                                               self.denominator1,self.denominator2,self.denominator3,self.unit,self.item1,self.item2,
                                               self.item3,self.item4,self.item5)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType14"}

    def ExplainType14(self,problem,answer1,answer2,numerator1,numerator2,numerator3,denominator1,denominator2,denominator3,unit,item1,item2,item3,item4,item5):
        
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))
        #Adding the simplified fraction if possible
        if(answer1%answer2!=0):
            if gcf!=1:
                self.SimpleAnswer1 = int(answer1)/gcf
                self.SimpleAnswer2 = int(answer2)/gcf
                if self.SimpleAnswer2!=1:
                    self.SimpleMixed1,self.SimpleAnswer11 = divmod(self.SimpleAnswer1,self.SimpleAnswer2)
                    self.answer_text = self.answer_text + "<td>"+str(self.SimpleMixed1)+"</td>"
                    self.answer_text = self.answer_text + "<td><u>&nbsp;"+str(self.SimpleAnswer11)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"              
                else:
                    self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.mixed1,self.answer11 = divmod(answer1,answer2)
        self.answer_text = self.answer_text + "<td valign='center'>"+str(self.mixed1)+"</td>"
        if self.answer11!=0:
            self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer11)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
                
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "igISgktSd0M";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
             
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain            

    def GenerateProblemType15(self):
        '''e.g.:A dictionary is 3-1/3 cm thick. 
                Find the height of the stack made by 20 such dictionaries when placed on top of each other. '''
           
        self.girl1 = random.choice(PersonName.GirlName)
        self.Dict = {1:["m","m","A dictionary is","thick","Find the height of the stack made by",
                        "such dictionaries when placed on top of each other."],
                     2:["m","m","A tailor needs","of ribbon to border a skirt","Find the length of ribbon needed to border","such skirts."],
                     3:["m","m","You need","of wooden stick to make a toy house","Find the length of wooden stick you will need to make","such toy houses."],
                     4:["m","m","To make a dress it takes","of fabric","Find the amount of fabric needed to make","such dresses."],
                     5:["litre","litre","A can of milk contains","of milk","How much milk do","such cans contain?"],
                     6:["litre","litre","A cube of chicken stock can make","of broth","How much broth can","such cubes make?"],
                     7:["kg","kg","A can of vegetables makes","of stock","Find the amount of stock that","such cans of vegetables will make."],
                     8:["kg","kg","A bag of tomatoes when pureed make","of puree","Find the amount of puree made by","such bags of tomatoes."],
                     9:["kg","kg","A bunch of ripe bananas makes","of banana bread","How much cake will","such bunches of ripe bananas make?"],
                     10:["glass","glasses","A bag of apples can make","of cider","How many glasses of cider will","such bags of apples make?"],
                     11:["cup","cups","One block of cheese makes","of grated cheese","Find the amount of grated cheese that","such cheese blocks will make."],
                     12:["cup","cups","One bag of pasta contains","of pasta","How much pasta do","such bags of pasta contain?"],
                     13:["kg","kg","You can make","of cookies with a bag of flour","How much cookies can you make with","such bags of flour?"]                   
                     }
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.units = self.Dict[self.key][1]
        self.item1 = self.Dict[self.key][2]
        self.item2 = self.Dict[self.key][3]
        self.item3 = self.Dict[self.key][4]
        self.item4 = self.Dict[self.key][5]
        self.quantity = randint(4,20)

        # Generating 2 mixed fractions
        self.denominator1 = random.choice([2,3,4,5,6,7,8,9,10,11,12])
        self.numerator1 = randint(1,20)
        '''making sure a whole number is not generated'''
        while self.numerator1%self.denominator1 == 0:
            self.numerator1 = randint(1,20)
            
        self.mixed1, self.numerator11 = divmod(self.numerator1,self.denominator1)
        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.item1 +"&nbsp;</td>"
        if self.mixed1==0:
            self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>"+self.unit+" "+self.item2+"."
        else:
            self.problem = self.problem + "<td>"+str(self.mixed1)+"</td>"
            self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator11)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>"+self.units+" "+self.item2+"."
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + self.item3+" "+str(self.quantity)+" "+self.item4 
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
                
        self.AnswerDenominator = self.denominator1
        self.AnswerNumerator = self.numerator1 * self.quantity
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator11,self.mixed1,
                                               self.denominator1,self.unit,self.item1,self.item2,
                                               self.item3,self.item4)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.units,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType15"}

    def ExplainType15(self,problem,answer1,answer2,numerator1,numerator11,mixed1,denominator1,unit,item1,item2,item3,item4):
        
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))
        #Adding the simplified fraction if possible
        if(answer1%answer2!=0):
            if gcf!=1:
                self.SimpleAnswer1 = int(answer1)/gcf
                self.SimpleAnswer2 = int(answer2)/gcf
                if self.SimpleAnswer2!=1:
                    self.SimpleMixed1,self.SimpleAnswer11 = divmod(self.SimpleAnswer1,self.SimpleAnswer2)
                    self.answer_text = self.answer_text + "<td valign='center'>"+str(self.SimpleMixed1)+"</td>"
                    self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer11)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"              
                else:
                    self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.mixed1,self.answer11 = divmod(answer1,answer2)
        self.answer_text = self.answer_text + "<td valign='center'>"+str(self.mixed1)+"</td>"
        if self.answer11!=0:
            self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer11)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
                
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "gLsxayQGUlg";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
             
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain            

    def GenerateProblemType16(self):
        '''e.g.:Pam packs 4 kg of onions equally into 10 bags. 
                What is the mass of onions in each bag? Give your answer as a fraction in its simplest form.'''
           
        self.name1 = random.choice(PersonName.PersonName)
        self.Dict = {1:["kg","packs","of onions equally into","bags","What is the mass of onions in each bag?"],
                     2:["m","divides","of a lace equally among","children","How much lace does each child get?"],
                     3:["m","cuts","of a piece of cloth equally into","pieces","Find the length of each piece."],
                     4:["m","cuts","of a pole equally into","pieces","What is the length of each piece?"],
                     5:["m","divides","of drawing paper equally among","artists","Find the length of drawing paper that each artist gets."],
                     6:["litre","packs","of cooking oil equally into","bottles","What is the volume of cooking oil in each bottle?"],
                     7:["litre","divides","of milk equally into","cartons","Find the volume of milk in each carton."],
                     8:["pots","serves","of soup equally into","bowls","How much soup does each bowl have?"],
                     9:["pails","packs","of wall paint equally into","cans","How much wall paint has each can?"],
                     10:["jars","pours","of juice equally into","glasses","Find the volume of juice in each glass."],
                     11:["bottles","fills","of ink equally into","vials","What is the volume of ink in each vial?"],
                     12:["kettles","pours","of tea equally into","mugs","Find the amount of tea in each mug."],
                     13:["kg","divides","of potatoes equally into","bags","Find the mass of potatoes in each bag."],
                     14:["kg","distributes","of fruit equally into","baskets","What is the mass of fruit in each basket?"],
                     15:["kg","divides","of nuts equally into","packets","How much nuts has each packet?"],
                     16:["kg","divides","of flour equally among","dessert","How much flour is used for each dessert recipe?"],
                     17:["cups","distibutes","of pasta equally into","people","How much pasta does each person get?"],
                     18:["blocks","divides","of cheese equally among","children","Find the amount of cheese that each child gets."],
                     19:["kg","puts","of cookies equally into","jars","What is the mass of cookies in each jar?"],
                     }
        self.key = randint(1,len(self.Dict))
        self.units = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]

        self.number2 = randint(2,12)
        self.number1 = randint(1,self.number2-1)

        self.problem = self.name1 + " "+self.item1+" "+str(self.number1)+" "+self.units+" "+self.item2+" "+str(self.number2)+" "+self.item3+". "
        self.problem = self.problem + self.item4
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2.)</td>"
        self.problem = self.problem + "</tr></table>" 
                
        self.AnswerDenominator = self.number2       
        self.AnswerNumerator = self.number1
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType16(self.problem,self.answer1,self.answer2,self.number1,self.number2,self.units,self.item1,self.item2,
                                               self.item3,self.item4)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.units,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType16"}

    def ExplainType16(self,problem,answer1,answer2,number1,number2,unit,item1,item2,item3,item4):
        
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer1)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
                
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "D1Q63n6FC4A";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
             
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain            

    def GenerateProblemType17(self):
        '''e.g.:3/4 kg of candies and 6/7 kg of cookies are shared equally among 3 children. 
                What is the total mass of candies and cookies that each child gets? '''
           
        self.girl1 = random.choice(PersonName.GirlName)
        self.Dict = {1:["kg","kg","candies","cookies","are shared equally among","children","What is the total mass of candies and cookies that each child gets?"],
                     2:["m","m","lace","ribbon","are divided equally among","children","Find the total length of lace and ribbon that each child gets."],
                     3:["m","m","silk cloth","cotton cloth","are cut and packed equally into","bundles","What is the total length of cloth in each bundle?"],
                     4:["m","m","bamboo pole","plastic pole","are divided equally into","bundles","Find the total length of pole in each bundle."],
                     5:["m","m","painting canvas","drawing paper","are cut and divided equally among","painters","What is the total length of painting canvas and drawing paper that each painter gets?"],
                     6:["pail","pails","green paint","blue paint","are packed equally into","cans","Find the amount of purple paint that each can has. [Hint:Green and blue makes purple.]"],
                     7:["kg","kg","red potatoes","white potatoes","are packed equally into","bags","What is total mass of potatoes in each bag?"],
                     8:["kg","kg","apples","oranges","are packed equally into","baskets","What is the mass of fruit in each basket?"],
                     9:["kg","kg","cashews","almonds","are divided equally into","packets","How much nuts has each packet?"],
                     10:["kg","kg","butter cookies","plain cookies","are put equally into","jars","What is the mass of cookies in each jar?"],
                     }
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.units = self.Dict[self.key][1]
        self.item1 = self.Dict[self.key][2]
        self.item2 = self.Dict[self.key][3]
        self.item3 = self.Dict[self.key][4]
        self.item4 = self.Dict[self.key][5]
        self.item5 = self.Dict[self.key][6]

        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        self.number1 = randint(2,5)
        
        self.problem = "<table class='FractionsTable'><tr>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>"+self.unit+" of "+self.item1+" and&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td>"+self.unit+" of "+self.item2
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + self.item3 + " " + str(self.number1)+" "+self.item4+".<br><br>"
        self.problem = self.problem + self.item5

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2.)</td>"
        self.problem = self.problem + "</tr></table>" 
                        
        self.AnswerDenominator = self.denominator1 * self.denominator2 * self.number1
        self.AnswerNumerator = (self.numerator1 * self.denominator2 + self.numerator2 * self.denominator1)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType17(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,
                                               self.denominator1,self.denominator2,self.number1,self.units,self.item1,
                                               self.item2,self.item3,self.item4,self.item5)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.units,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType17"}

    def ExplainType17(self,problem,answer1,answer2,numerator1,numerator2,denominator1,denominator2,number1,unit,item1,item2,item3,item4,item5):
        
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))         
        '''Adding the simplified fraction if possible'''
        if gcf>1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
            else:
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
            self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer1)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
                
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "XKcc1-tUQl4";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
             
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain            

    def GenerateProblemType18(self):
        '''e.g.:Sam had 260 erasers. 
                He had 3/4 as many sharpeners as erasers. 
                He had 5 times as many markers as sharpeners. How many markers did he have?'''
           
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["","","had","erasers.","He had","as many sharpeners as erasers.","He had","times as many markers as sharpeners. How many markers did he have?",randint(1,3)],
                     2:["","","had","red marbles.","He had","as many blue marbles as red marbles.","He had","times as many green marbles as blue. How many green marbles did he have?",randint(2,4)],
                     3:["","","runs a gift shop. Last week he sold","toys,","","as many posters as toys, and","","times as many cards as posters. How many cards did he sell last week?",randint(2,5)],
                     4:["","","has","toy cars,","","as many toy robots, and","","times as many board games. Find the number of board games he has.",randint(2,5)],
                     5:["","","puts","apples in a fruit basket.","He puts","as many oranges as apples, and","","times as many mangoes as oranges. How many mangoes does he put in the fruit basket?",randint(1,2)],
                     6:["","","carries","types of vegetable plants in his nursery.","He carries","as many types of fruit plants as vegetable plants, and","","times as many types of flowering shrubs as fruit plants. How many types of flowering shrubs does he carry?",randint(2,4)],
                     7:["","$","won a sum of money in a game show of which he donates $","to Charity A,","","as much money to Charity B as Charity A, and","","times as much money to Charity C as Charity B. How much money did he donate to Charity C?",randint(500,1000)],
                     8:["","$","spent $","on a T-shirt.","He spent","as much money on a tie as the T-shirt, and","","times as much money on a watch as the tie. How much did the watch cost him?",randint(3,5)],
                     9:["m","","bought","m of lace for a craft project.","He bought","as much ribbon as lace for the project.","He bought","times as much rope as ribbon for the project. How much rope did he buy?",randint(1,3)],
                     10:["km","","lives","km from his school.","He lives","times as far from the public playground as the school, and","","times as far from the shopping mall as the public playground. How far is the shopping mall from his house?",randint(1,2)],
                     11:["kg","","bought","kg sugar.","He bought","as much flour as sugar.","He bought","times as much rice as flour. Find the mass of rice that he bought.",randint(1,2)],
                     12:["cups","","packs","cups of cashew nuts,","","as much almonds as cashew nuts, and","","times as much raisins as almonds. How much raisins does he pack?",randint(2,4)],
                     13:["pails","","is painting his house. He uses","pails of green paint.","He uses","as much blue paint as green paint and","","times as much white paint as blue paint. How much white paint does he use?",randint(2,4)],
                     }
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.DollarUnit = self.Dict[self.key][1]
        self.item1 = self.Dict[self.key][2]
        self.item2 = self.Dict[self.key][3]
        self.item3 = self.Dict[self.key][4]
        self.item4 = self.Dict[self.key][5]
        self.item5 = self.Dict[self.key][6]
        self.item6 = self.Dict[self.key][7]
        self.multiplier = self.Dict[self.key][8]
        
        self.denominator1 = randint(2,12)
        self.numerator1 = randint(1,self.denominator1-1)
        self.number1 = self.multiplier * self.denominator1
        self.number2 = randint(2,5)
        
        self.problem = self.boy1 + " " +self.item1+" " +str(self.number1) + " " + self.item2
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.item3+"&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp;"+self.item4+"</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + self.item5 + " " + str(self.number2) +" "+ self.item6
                       
        self.answer = str(self.number1*self.number2*self.numerator1/self.denominator1)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType18(self.problem,self.answer,self.numerator1,
                                               self.denominator1,self.number1,self.number2,self.unit,self.item1,
                                               self.item2,self.item3,self.item4,self.item5,self.item6)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':self.DollarUnit,'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType18"}

    def ExplainType18(self,problem,answer,numerator1,denominator1,number1,number2,unit,item1,item2,item3,item4,item5,item6):

        self.answer_text = "The correct answer is: "+str(answer)
               
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "6LhgCLxQ6bs";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
             
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain            

    def GenerateProblemType19(self):
        '''e.g.:There are 2442 Class A and Class B seats at a concert. 
                2/3 of the total number of Class A seats is equal to 
                1/4 of the total number of Class B seats. 
                How many Class A seats are there?'''
           
        self.Dict = {1:["There are","Class A and Class B seats at a concert.","of the total number of Class A seats is equal to","of the total number of Class B seats.","How many Class A seats are there?",randint(5,15)],                  
                     2:["A dance school has","ballet and hip-hop dancers. If","of the total number ballet dancers is equal to","of the toal number of hip-hop dancers","find the number of ballet dancers.",randint(2,7)],
                     3:["A fabric merchant carries","rolls of silk and cotton fabrics. If","of the rolls of silk fabric is equal to","of the roll of cotton fabric,","how many rolls of silk fabric does he carry?",randint(3,10)],
                     4:["There are","mangoes and pears in a fruit basket.","of the mangoes is equal to","of the pears.","How many mangoes are there in the fruit basket?",randint(1,3)],
                     5:["There were","multiple-choice and open-ended questions on an exam.","of the total number of multiple-choice questions was equal to","of the total number of open-ended questions.","Find the number of multiple-choice questions on the exam.",randint(2,4)],
                     6:["Printer A and Printer B printed","pages.","of the pages printed by Printer A is equal to","of the pages printed by Printer B.","How many pages did Printer A print?",randint(3,8)],
                     7:["An amusement park received","adults and children. If","of the adults was equal to","of the children,","how many adults were there?",randint(3,8)],
                     8:["Last week a bakery sold","cakes and pies.","of the cakes it sold was equal to","of the pies it sold.","How many cakes did the bakery sell?",randint(5,15)],
                     9:["There are","pupils in school","of the total number of girls is equal to","of the total number of boys.","How many girls are there in the school?",randint(6,15)],
                     10:["A department store has","dresses and blouses. If","of the total number of dresses is equal to","of the total number of blouses,","how many dresses does it have?",randint(4,10)],
                     11:["A plant nursery carries","shrubs and trees.","of the shrubs that it carries is equal to","of the trees it carries.","Find the number of shrubs that the nursery carries.",randint(4,10)],
                     12:["A movie rental shop has collection of","animated and drama movies. If","of the animated movies is equal to","of the drama movies,","how many animated movies does it have?",randint(4,10)]
                     }
        self.key = randint(1,len(self.Dict))
        self.item1 = self.Dict[self.key][0]
        self.item2 = self.Dict[self.key][1]
        self.item3 = self.Dict[self.key][2]
        self.item4 = self.Dict[self.key][3]
        self.item5 = self.Dict[self.key][4]
        self.multiplier = self.Dict[self.key][5]


        self.denominators = random.sample([2,3,4,5,6,7,8,9],2)
        
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        self.number1 = self.multiplier * (self.numerator1*self.denominator2+self.numerator2*self.denominator1)
        
        self.problem = self.item1+" "+str(self.number1)+" "+self.item2
        self.problem = self.problem + "<table class='FractionsTable'><tr>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>&nbsp;"+self.item3+"</td></tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'><tr>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td>&nbsp;"+self.item4+"</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + self.item5

        self.answer = str(self.multiplier*self.denominator1*self.numerator2)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType19(self.problem,self.answer,self.numerator1,self.numerator2,
                                               self.denominator1,self.denominator2,self.number1,self.item1,
                                               self.item2,self.item3,self.item4,self.item5)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType19"}

    def ExplainType19(self,problem,answer,numerator1,numerator2,denominator1,denominator2,number1,item1,item2,item3,item4,item5):

        self.answer_text = "The correct answer is: "+str(answer)
                        
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "dkKIiOr75aQ";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
             
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain            

    def GenerateProblemType20(self):
        '''e.g.:Nina is making 5 curtains and 3 cushion covers. 
                She uses 2-1/2 m of fabric for each curtain 
                and 1-1/3 m of fabric for each cushion cover. 
                How much fabric does she need altogether?'''
           
        self.girl1 = random.choice(PersonName.GirlName)
        self.Dict = {1:["m","is making","curtains and","cushion covers.","She uses","m of fabric for each curtain","and","m of fabric for each cushion cover.",
                        "How much fabric does she need altogether?"],
                     2:["cups","is baking","cakes and","pizzas.","She needs","cups of flour for each cake","and","cups of flour for each pizza.",
                        "How much flour does she need altogether?"],
                     3:["m","is knitting","sweaters and","caps.","She needs","m of yarn for each sweater","and","m of yarn for each cap.",
                        "Find the amount of yarn she will need altogether."],
                     4:["m","is stiching","blouses and","skirts.","She uses","m of cloth for each blouse","and","m of cloth for each skirt.","Find the amount of cloth she will need altogether."],
                     5:["cups","is making","pies and","cakes.","She needs","cups of fruit for each pie","and","cups of fruit for each cake.","Find the amount of fruit she will need altogether."],
                     6:["kg","bought","watermelons and","papayas.","Each watermelon had a mass of","kg","and each papaya had a mass of","kg","Find the total mass of fruit she bought."],
                     7:["litre","has","bottles and","cans.","Each bottle contains","litres of juice","while each can contains","litre of soda.","What is total volume of beverages that she has?"],
                     8:["litre","renovated her house using","pails of paint and","tins of varnish.","If each pail contained","litres of paint","and each tin contained","litres of varnish,","how much paint and varnish did she use altogether?"],
                     9:["litre","has","containers and","barrels.","If each container has a capacity of","litres","and each barrel has a capacity of","litres,","what is the maximum volume of juice that they can hold altogether?"],
                     10:["cups","is making a dessert using","bags of nuts and","packets of cheese.","Each bag contains","cups of nuts","and each packet contains","cups of cheese.","What is total amount of ingredients she uses for the dessert?"],
                     11:["tins","mixes","pails of green paint with","cans of blue paint.","If each pail holds the same amount of paint as","tins","and each can holds the same amount of paint as","tins,","how many tins of paint does she mix altogether?"],
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
        
        self.number1 = randint(4,20)
        self.number2 = randint(4,20)

        # Generating 2 mixed fractions
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(self.denominator1+1,20)
        self.numerator2 = randint(self.denominator2+1,20)
        '''making sure a whole number is not generated'''
        while self.numerator1%self.denominator1 == 0:
            self.numerator1 = randint(self.denominator1+1,20)
        
        while self.numerator2%self.denominator2 == 0:
            self.numerator2 = randint(self.denominator2+1,20)
                        
        self.mixed1, self.numerator11 = divmod(self.numerator1,self.denominator1)
        self.mixed2, self.numerator22 = divmod(self.numerator2,self.denominator2)
        
        self.problem = self.girl1+" "+self.item1+" "+str(self.number1)+" "+self.item2+" "+str(self.number2)+" "+self.item3
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.item4+"&nbsp;</td>"
        self.problem = self.problem + "<td>"+str(self.mixed1)+"</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator11)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>"+self.item5+"</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.item6+"&nbsp;</td>"
        self.problem = self.problem + "<td>"+str(self.mixed2)+"</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator22)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td>"+self.item7+"</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + self.item8
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>" 
                
        self.AnswerDenominator = self.denominator1 * self.denominator2
        self.AnswerNumerator = (self.numerator1 * self.number1 * self.denominator2) + (self.numerator2 * self.number2 * self.denominator1)
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType20(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator11,self.mixed1,
                                               self.denominator1,self.numerator2,self.numerator22,self.mixed2,
                                               self.denominator2,self.unit,self.item1,self.item2,
                                               self.item3,self.item4,self.item5,self.item6,
                                               self.item7,self.item8)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType20"}

    def ExplainType20(self,problem,answer1,answer2,numerator1,numerator11,mixed1,denominator1,
                      numerator2,numerator22,mixed2,denominator2,unit,item1,item2,item3,item4,item5,item6,item7,item8):
        
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))
        #Adding the simplified fraction if possible
        if(answer1%answer2!=0):
            if gcf!=1:
                self.SimpleAnswer1 = int(answer1)/gcf
                self.SimpleAnswer2 = int(answer2)/gcf
                if self.SimpleAnswer2!=1:
                    self.SimpleMixed1,self.SimpleAnswer11 = divmod(self.SimpleAnswer1,self.SimpleAnswer2)
                    self.answer_text = self.answer_text + "<td valign='center'>"+str(self.SimpleMixed1)+"</td>"
                    self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer11)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"              
                else:
                    self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        self.mixed1,self.answer11 = divmod(answer1,answer2)
        self.answer_text = self.answer_text + "<td valign='center'>"+str(self.mixed1)+"</td>"
        if self.answer11!=0:
            self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer11)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
                
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "cj4x7G-8XMc";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
             
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain            

    def GenerateProblemType21(self):
        '''e.g.:Nina is making 5 curtains and 3 cushion covers. 
                She uses 2-1/2 m of fabric for each curtain 
                and 1-1/3 m of fabric for each cushion cover. 
                Each metre of fabric costs $38. How much did Nina spend on the fabric?'''
           
        self.girl1 = random.choice(PersonName.GirlName)
        self.Dict = {1:["m","is making","curtains and","cushion covers.","She uses","m of fabric for each curtain","and","m of fabric for each cushion cover.",
                        "Each metre of fabric costs $",". How much did","spend on the fabric?",randint(3,40)],
                     2:["cups","is baking","cakes and","pizzas.","She needs","cups of flour for each cake","and","cups of flour for each pizza.",
                        "If each cup of flour costs $",", find the sum of money","spent on the flour.",randint(1,3)],
                     3:["m","is knitting","sweaters and","caps.","She needs","m of yarn for each sweater","and","m of yarn for each cap.",
                        "Each meter of yarn costs $",". How much did","spend on the yarn?",randint(1,4)],
                     4:["m","is stiching","blouses and","skirts.","She uses","m of cloth for each blouse","and","m of cloth for each skirt.",
                        "Each meter of cloth costs $",". How much did","spend on the cloth?",randint(1,5)],
                     5:["cups","is making","pies and","cakes.","She needs","cups of fruit for each pie","and","cups of fruit for each cake.",
                        "If each cup of fruit costs $",", find the sum of money","paid for the fruit.",randint(1,3)],
                     6:["kg","bought","watermelons and","papayas.","Each watermelon had a mass of","kg","and each papaya had a mass of","kg",
                        "If each kg of fruit costs $",", find the sum of money","paid for the fruit.",randint(2,5)],
                     7:["litre","has","bottles and","cans.","Each bottle contains","litres of juice","while each can contains","litre of soda.",
                        "If each litre of beverage costs $",", what is the cost of beverages to","?",randint(2,5)],
                     8:["litre","renovated her house using","pails of paint and","tins of varnish.","Each pail contained","litres of paint","and each tin contained","litres of varnish.",
                        "If each litre of paint or varnish cost $",", how much did","spend on the renovation?",randint(5,15)],
                     9:["litre","has","containers and","barrels.","Each container has","litres of lemonade","while each barrel has","litres of lemonade.",
                        "If she sells each litre of lemonade for $",", how much will","collect?",randint(1,3)],
                     10:["tins","mixes","pails of green paint with","cans of blue paint.","Each pail holds the same amount of paint as","tins","and each can holds the same amount of paint as","tins.",
                         "If she paid $","for a tin of paint, how much did","spend on the paints altogether?",randint(4,15)],
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
        self.cost = self.Dict[self.key][11]
        
        # Generating 2 mixed fractions
        self.denominators = random.sample([2,3,4,5,6,7,8,9,10,11,12],2)
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(self.denominator1+1,20)
        self.numerator2 = randint(self.denominator2+1,20)
        '''making sure a whole number is not generated'''
        while self.numerator1%self.denominator1 == 0:
            self.numerator1 = randint(self.denominator1+1,20)
        
        while self.numerator2%self.denominator2 == 0:
            self.numerator2 = randint(self.denominator2+1,20)
                        
        self.mixed1, self.numerator11 = divmod(self.numerator1,self.denominator1)
        self.mixed2, self.numerator22 = divmod(self.numerator2,self.denominator2)
        
        self.number1 = randint(2,5) * self.denominator1
        self.number2 = randint(2,5) * self.denominator2
        
        self.problem = self.girl1+" "+self.item1+" "+str(self.number1)+" "+self.item2+" "+str(self.number2)+" "+self.item3
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.item4+"&nbsp;</td>"
        self.problem = self.problem + "<td>"+str(self.mixed1)+"</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator11)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
        self.problem = self.problem + "<td>"+self.item5+"</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.item6+"&nbsp;</td>"
        self.problem = self.problem + "<td>"+str(self.mixed2)+"</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator22)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
        self.problem = self.problem + "<td>"+self.item7+"</td>"
        self.problem = self.problem + "</tr></table>"
        self.problem = self.problem + self.item8+str(self.cost)+" "+self.item9+" "+self.girl1+" " +self.item10
                
        self.AnswerDenominator = self.denominator1 * self.denominator2
        self.AnswerNumerator = (self.numerator1 * self.number1 * self.denominator2) + (self.numerator2 * self.number2 * self.denominator1)

        self.answer = str(self.AnswerNumerator*self.cost/self.AnswerDenominator)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType21(self.problem,self.answer,self.numerator1,self.numerator11,self.mixed1,
                                               self.denominator1,self.numerator2,self.numerator22,self.mixed2,
                                               self.denominator2,self.cost,self.unit,self.item1,self.item2,
                                               self.item3,self.item4,self.item5,self.item6,
                                               self.item7,self.item8,self.item9,self.item10)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"$",'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType21"}

    def ExplainType21(self,problem,answer,numerator1,numerator11,mixed1,denominator1,
                      numerator2,numerator22,mixed2,denominator2,cost,unit,item1,item2,item3,item4,item5,item6,item7,item8,item9,item10):
        
        self.answer_text = "The correct answer is: "+answer
                
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "cj4x7G-8XMc";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
             
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain 

    def GenerateProblemType22(self):
        '''e.g.:Roy and Sandy have the same amount of paint at first. 
                Sandy spills 2/5 of her paint. 
                After Roy uses 1/3 of his paint to paint a wall, 
                Roy still has 1/3 litre more paint than Sandy. 
                How much paint did they each have at first?'''
           
        self.girl1 = random.choice(PersonName.GirlName)
        self.boy1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["litre","have the same amount of paint at first.","","spills","of her paint.","After","uses","of his paint to paint a wall,",
                        "","still has","litre more paint than","How much paint did they have at first?"],                  
                     2:["litre","have the same amount of paint at first.","After","gives","of her paint to her brother and","","uses","of his paint to paint a wall,",
                        "","has","litre more paint than","Find the amount of paint they each had first."],
                     3:["m","have the same amount of fabric at first.","After","uses","of her fabric to make a dress and","","gives away","of his fabric to a friend,",
                        "","is left with","m more fabric than","Find the amount of fabric they each had at first."],
                     4:["cups","have the same amount of flour at first.","After","uses","of her flour to bake a cake and","","uses","of his flour to make a pizza,",
                        "","has","cup more flour than","Find the amount of flour they each had at first."],
                     5:["balls","have the same amount of yarn at first.","After","uses","of her yarn to knit a sweater and","","gives away","of his yarn to his sister,",
                        "","has","ball more yarn than","How much yarn did they each had at first?"],
                     6:["rolls","have the same amount of gift wrappers at first.","","accidentally spoils","of her wrapper","After","uses","of his wrapper to wrap gifts,",
                        "","has","roll more wrapper than","Find the amount of wrapper they each had at first."],
                     7:["km","start a race from the same point.","When","has","of the distance left to run,","","only has","of the distance left to run and",
                        "","is","km ahead of","How long is the race?"],
                     8:["cups","buy the same amount of fruit from a fruit vendor.","After","uses","of her fruit to make a custard and","","uses","of his fruit to make a shake,",
                        "","is left with","cup more fruit than","Find the amount of fruit they each had at first."],
                     9:["kg","bought the same amount of vegetable from a grocer.","After","ate","of her vegetables while","","ate","of his vegetables,",
                        "","had","kg more vegetables than","How much vegetables they each had at first?"],
                     10:["litre","had the same amount of fruit juice with them.","Then,","blended","of her juice into a smoothie while","","drank","of his fruit juice.",
                        "Now,","has","litre more fruit juice than","How much fruit juice had they each at first?"],
                     11:["m<sup>2</sup>","had the same amount of wooden plank at first.","Then,","used","of her plank to make a bed frame while","","used","of his plank to make a doghouse.",
                        "Now,","has","m<sup>2</sup> more plank left than","Find the amount of wooden plank they each had at first."],
                     12:["cups","had the same amount of strawberries at first.","Then,","used","of her strawberries to make a dessert while","","ate","of his strawberries.",
                        "Now,","has","cup more strawberries than","How much strawberries had they each at first?"],
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

        self.denominators = random.sample([2,3,4,5,6],2)
        
        self.denominator1 = self.denominators[0]
        self.denominator2 = self.denominators[1]
        self.numerator1 = randint(1,self.denominator1-1)
        self.numerator2 = randint(1,self.denominator2-1)
        
        '''Making sure that both fractions are not same'''
        while (Decimal(self.numerator1)/Decimal(self.denominator1)-Decimal(self.numerator2)/Decimal(self.denominator2)==0):
            self.denominators = random.sample([2,3,4,5,6],2)
            self.denominator1 = self.denominators[0]
            self.denominator2 = self.denominators[1]
            self.numerator1 = randint(1,self.denominator1-1)
            self.numerator2 = randint(1,self.denominator2-1)
        
        self.denominator3 = randint(2,6)
        self.numerator3 = randint(1,self.denominator3-1)
                  
        self.problem = self.boy1+" and "+self.girl1+" "+self.item1
        self.problem = self.problem + "<table class='FractionsTable'><tr>"
        if (Decimal(self.numerator1)/Decimal(self.denominator1)>Decimal(self.numerator2)/Decimal(self.denominator2)):
            self.problem = self.problem + "<td>"+ self.item2+" "+self.girl1+" "+self.item3+"&nbsp;</td>"
            self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>&nbsp;"+self.item4+"</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'><tr>"
            self.problem = self.problem + "<td>"+ self.item5+" "+self.boy1+" "+self.item6+"&nbsp;</td>"
            self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td>&nbsp;"+self.item7+"</td></tr></table>"
        else:
            self.problem = self.problem + "<td>"+ self.item2+" "+self.girl1+" "+self.item3+"&nbsp;</td>"
            self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator2)+"&nbsp;</u><br>&nbsp;"+str(self.denominator2)+"</td>"
            self.problem = self.problem + "<td>&nbsp;"+self.item4+"</td></tr></table>"
            self.problem = self.problem + "<table class='FractionsTable'><tr>"
            self.problem = self.problem + "<td>"+ self.item5+" "+self.boy1+" "+self.item6+"&nbsp;</td>"
            self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator1)+"&nbsp;</u><br>&nbsp;"+str(self.denominator1)+"</td>"
            self.problem = self.problem + "<td>&nbsp;"+self.item7+"</td></tr></table>"

        self.problem = self.problem + "<table class='FractionsTable'><tr>"
        self.problem = self.problem + "<td>"+ self.item8+" "+self.boy1+" "+self.item9+"&nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;"+str(self.numerator3)+"&nbsp;</u><br>&nbsp;"+str(self.denominator3)+"</td>"
        self.problem = self.problem + "<td>&nbsp;"+self.item10+" "+self.girl1+"</td></tr></table>"
        self.problem = self.problem + self.item11+"<br>"

        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If &nbsp;</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>"
                
        self.AnswerDenominator = self.denominator3 * abs(self.denominator2*(self.denominator1-self.numerator1)-self.denominator1*(self.denominator2-self.numerator2))
        self.AnswerNumerator = self.denominator1 * self.denominator2 * self.numerator3
        
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType22(self.problem,self.answer1,self.answer2,self.numerator1,self.numerator2,self.numerator3,
                                               self.denominator1,self.denominator2,self.denominator3,self.item1,self.item2,self.item3,
                                               self.item4,self.item5,self.item6,self.item7,self.item8,self.item9,self.item10,self.item11)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType22"}

    def ExplainType22(self,problem,answer1,answer2,numerator1,numerator2,numerator3,denominator1,denominator2,denominator3,item1,item2,item3,item4,item5,
                      item6,item7,item8,item9,item10,item11):

        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(int(answer1), int(answer2))
        #Adding the simplified fraction if possible
        if(answer1%answer2!=0):
            if gcf!=1:
                self.SimpleAnswer1 = int(answer1)/gcf
                self.SimpleAnswer2 = int(answer2)/gcf
                if self.SimpleAnswer2!=1:
                    if (self.SimpleAnswer1>self.SimpleAnswer2):
                        self.SimpleMixed1,self.SimpleAnswer11 = divmod(self.SimpleAnswer1,self.SimpleAnswer2)
                        self.answer_text = self.answer_text + "<td valign='center'>"+str(self.SimpleMixed1)+"</td>"
                        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer11)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
                    else:
                        self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>&nbsp;"+str(self.SimpleAnswer2)+"</td>"
                else:
                    self.answer_text = self.answer_text + "<td align='center'>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</td>"
                self.answer_text = self.answer_text + "<td align='center'>&nbsp;Or&nbsp;</td>"
        if(answer1>answer2):
            self.mixed1,self.answer11 = divmod(answer1,answer2)
            self.answer_text = self.answer_text + "<td valign='center'>"+str(self.mixed1)+"</td>"
            if self.answer11!=0:
                self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer11)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        else:
            self.answer_text = self.answer_text + "<td align='center'><u>&nbsp;"+str(self.answer1)+"&nbsp;</u><br>&nbsp;"+str(self.answer2)+"</td>"
        self.answer_text = self.answer_text + "</tr></table>"
                        
        self.solution_text = "<b><u>Solution</b></u>:<br/>"
        self.solution_text = "<div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "Ru3_lZe7csE";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
             
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain            
    
    def checkAnswer(self,template,answer,input):    
        if (template=="FractionMCQTypeProblems.html"):
            answer=str(answer[0])+"/"+str(answer[1])+"/"+str(answer[2])
            if(answer==input):
                return True
            else:
                return False
        else:
            try:
                if "/" in str(answer):
                    AnswerNumerator = int(str(answer).partition("/")[0])
                    AnswerDenominator = int(str(answer).partition("/")[2])
                else:
                    AnswerNumerator = int(str(answer))
                    AnswerDenominator = 1
                
                if " " in str(input):             
                    InputMixed = int(str(input).partition(" ")[0])
                    RemainingInput = str(input).partition(" ")[2]
                    if "/" in str(RemainingInput):
                        InputDenominator = int(str(RemainingInput).partition("/")[2])
                        InputNumerator = int(str(RemainingInput).partition("/")[0])+InputMixed*InputDenominator
                    else:
                        InputDenominator = 1
                        InputNumerator = InputMixed
                else:
                    if "/" in str(input):
                        InputNumerator = int(str(input).partition("/")[0])
                        InputDenominator = int(str(input).partition("/")[2])
                    else:
                        InputNumerator = int(str(input))
                        InputDenominator = 1

                return Decimal(AnswerNumerator)/Decimal(AnswerDenominator)==Decimal(InputNumerator)/Decimal(InputDenominator)
            except ValueError:
                return False
